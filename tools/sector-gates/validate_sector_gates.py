#!/usr/bin/env python3
"""Validate sector regulatory gates and print an applicable checklist."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_GATES = ROOT / "references/sector-regulatory-gates.json"
DEFAULT_SOURCES = ROOT / "docs/source-registers/country-market-data.json"
REQUIRED_GATE = {"id", "question", "evidence", "model_impact", "stop_condition", "sources"}


def validate(gates_path: Path = DEFAULT_GATES, sources_path: Path = DEFAULT_SOURCES) -> list[str]:
    data = json.loads(gates_path.read_text(encoding="utf-8"))
    source_ids = {item["id"] for item in json.loads(sources_path.read_text(encoding="utf-8"))["entries"]}
    errors: list[str] = []
    sectors: set[str] = set()
    gate_ids: set[str] = set()
    for sector in data.get("sectors", []):
        name = sector.get("sector", "")
        if not name or name in sectors:
            errors.append(f"duplicate or empty sector: {name!r}")
        sectors.add(name)
        if len(sector.get("gates", [])) < 2:
            errors.append(f"{name}: fewer than two gates")
        for gate in sector.get("gates", []):
            missing = REQUIRED_GATE - set(gate)
            if missing:
                errors.append(f"{name}: gate missing {sorted(missing)}")
                continue
            if gate["id"] in gate_ids:
                errors.append(f"duplicate gate id: {gate['id']}")
            gate_ids.add(gate["id"])
            unknown = set(gate["sources"]) - source_ids
            if unknown:
                errors.append(f"{gate['id']}: unknown sources {sorted(unknown)}")
            for field in ("question", "evidence", "model_impact", "stop_condition"):
                if not gate[field].strip():
                    errors.append(f"{gate['id']}: empty {field}")
    if len(sectors) != 12:
        errors.append(f"expected 12 sector families, found {len(sectors)}")
    return errors


def checklist(sector_names: list[str], path: Path = DEFAULT_GATES) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    by_name = {item["sector"]: item for item in data["sectors"]}
    unknown = set(sector_names) - set(by_name)
    if unknown:
        raise ValueError(f"unknown sector families: {', '.join(sorted(unknown))}")
    return [gate | {"sector": name, "status": "not-assessed"}
            for name in sector_names for gate in by_name[name]["gates"]]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gates", type=Path, default=DEFAULT_GATES)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--sector", action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    errors = validate(args.gates, args.sources)
    if errors:
        print("\n".join(f"FAIL: {error}" for error in errors))
        return 1
    if args.sector:
        try:
            payload = checklist(args.sector, args.gates)
        except ValueError as exc:
            print(f"FAIL: {exc}")
            return 1
        rendered = json.dumps(payload, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")
    else:
        print("PASS: 12 sector families and 24 regulatory gates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
