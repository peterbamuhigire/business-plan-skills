#!/usr/bin/env python3
"""Recalculate an XLSX workbook in a spreadsheet engine and test declared tie-outs.

`formula_map.py` is a structural scan: it reads the values a file already
carries. Many generators write formulas with a placeholder value of 0, so those
cached values prove nothing. This tool opens a copy of the workbook in
LibreOffice (headless, throwaway profile, no network, original untouched),
recomputes every formula, and then:

* reports formula cells whose stored value differs from the recalculated value
  (stale cache: a warning, or an error with --require-fresh-cache);
* reports any cell that evaluates to a spreadsheet error after recalculation;
* evaluates the same `reconciliation-checks` contract that `formula_map.py`
  reads (schema_version 1.0.0), but on recalculated values, so both sides of a
  tie-out may be formulas (a three-statement model).

Exit codes: 0 pass, 1 fail, 2 NOT_ASSESSED (no usable engine, timeout or engine
failure). A missing engine is never a pass.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
_SPEC = importlib.util.spec_from_file_location("formula_map", HERE / "formula_map.py")
fm = importlib.util.module_from_spec(_SPEC)
assert _SPEC.loader
sys.modules.setdefault("formula_map", fm)
_SPEC.loader.exec_module(fm)

ENGINE_NAMES = ("soffice", "libreoffice")
DEFAULT_TIMEOUT_SECONDS = 180
REL_TOLERANCE = 1e-9
ABS_TOLERANCE = 1e-6
SAMPLE_LIMIT = 25
PROFILE_SETTINGS = """<?xml version="1.0" encoding="UTF-8"?>
<oor:items xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="OOXMLRecalcMode" oor:op="fuse"><value>0</value></prop></item>
<item oor:path="/org.openoffice.Office.Calc/Formula/Load"><prop oor:name="ODFRecalcMode" oor:op="fuse"><value>0</value></prop></item>
</oor:items>
"""


class EngineUnavailable(Exception):
    """The engine is missing, timed out or failed; the result is NOT_ASSESSED."""


def find_engine(explicit: str | None = None) -> str | None:
    if explicit:
        return explicit if Path(explicit).is_file() else shutil.which(explicit)
    for name in ENGINE_NAMES:
        found = shutil.which(name)
        if found:
            return found
    return None


def engine_version(engine: str) -> str:
    try:
        result = subprocess.run([engine, "--version"], capture_output=True, text=True,
                                timeout=60, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return "unknown"
    return (result.stdout or result.stderr).strip().splitlines()[0] if (result.stdout or result.stderr).strip() else "unknown"


def recalculate(workbook: Path, engine: str, workdir: Path, timeout: int) -> Path:
    """Return the path of a recalculated copy; raise EngineUnavailable on failure."""
    source = workdir / "input.xlsx"
    shutil.copyfile(workbook, source)
    profile = workdir / "profile"
    (profile / "user").mkdir(parents=True)
    (profile / "user" / "registrymodifications.xcu").write_text(PROFILE_SETTINGS, encoding="utf-8")
    out_dir = workdir / "out"
    out_dir.mkdir()
    command = [engine, f"-env:UserInstallation={profile.as_uri()}", "--headless", "--norestore",
               "--convert-to", "xlsx:Calc MS Excel 2007 XML", "--outdir", str(out_dir), str(source)]
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
    except subprocess.TimeoutExpired as exc:
        raise EngineUnavailable(f"engine timed out after {timeout} seconds") from exc
    except OSError as exc:
        raise EngineUnavailable(f"engine could not start: {exc}") from exc
    produced = out_dir / "input.xlsx"
    if completed.returncode != 0 or not produced.is_file():
        raise EngineUnavailable(f"engine exit {completed.returncode} and no recalculated file produced")
    return produced


def read_cells(path: Path) -> dict[str, dict]:
    """Map 'Sheet!A1' to {formula, value, kind} using formula_map's parsing helpers."""
    cells: dict[str, dict] = {}
    with zipfile.ZipFile(path) as zf:
        shared = fm._shared_strings(zf)
        wb = fm._xml(zf, "xl/workbook.xml")
        rels = fm._xml(zf, "xl/_rels/workbook.xml.rels")
        targets = {r.get("Id"): r.get("Target") for r in rels.findall("p:Relationship", fm.NS)}
        for sheet in wb.findall("m:sheets/m:sheet", fm.NS):
            target = targets.get(sheet.get(f"{{{fm.NS['r']}}}id"), "")
            part = target.lstrip("/") if target.startswith("/") else str(Path("xl") / target).replace("\\", "/")
            if part not in zf.namelist():
                continue
            name = sheet.get("name", "")
            for cell in fm._xml(zf, part).findall(".//m:c", fm.NS):
                formula = cell.findtext("m:f", default="", namespaces=fm.NS)
                cells[f"{name}!{cell.get('r', '?')}"] = {
                    "formula": formula,
                    "value": fm._cell_text(cell, shared),
                    "kind": cell.get("t") or "n",
                }
    return cells


def _same(left: dict, right: dict) -> bool:
    a, b = left["value"], right["value"]
    x, y = fm._number(a), fm._number(b)
    if x is not None and y is not None:
        return math.isclose(x, y, rel_tol=REL_TOLERANCE, abs_tol=ABS_TOLERANCE)
    return (a or "") == (b or "")


def compare(original: dict[str, dict], recalculated: dict[str, dict]) -> dict:
    formula_cells = [key for key, cell in original.items() if cell["formula"]]
    stale: list[dict] = []
    errors: list[dict] = []
    missing = 0
    for key in formula_cells:
        after = recalculated.get(key)
        if after is None:
            missing += 1
            continue
        if after["kind"] == "e" or after["value"] in fm.ERROR_VALUES:
            errors.append({"location": key, "value": after["value"]})
        if not _same(original[key], after):
            stale.append({"location": key, "cached": original[key]["value"],
                          "recalculated": after["value"]})
    return {"formula_cells": len(formula_cells), "missing_after_recalculation": missing,
            "stale_cache_count": len(stale), "stale_cache_sample": stale[:SAMPLE_LIMIT],
            "error_count": len(errors), "error_sample": errors[:SAMPLE_LIMIT]}


def evaluate_contract(contract_path: Path, recalculated: dict[str, dict]) -> dict:
    result = {"status": "fail", "checks": [], "findings": [], "contract_sha256": None}
    try:
        raw = contract_path.read_bytes()
        contract = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        result["findings"].append({"code": "invalid-reconciliation-contract", "message": str(exc)})
        return result
    result["contract_sha256"] = hashlib.sha256(raw).hexdigest()
    if (not isinstance(contract, dict) or contract.get("schema_version") != "1.0.0"
            or not isinstance(contract.get("checks"), list) or not contract["checks"]):
        result["findings"].append({"code": "invalid-reconciliation-contract",
                                   "message": "Expected schema_version 1.0.0 and a non-empty checks list"})
        return result
    seen: set[str] = set()
    for item in contract["checks"]:
        check = {"id": "", "status": "fail", "findings": []}
        result["checks"].append(check)

        def fail(code: str, message: str) -> None:
            check["findings"].append({"code": code, "message": message})

        if not isinstance(item, dict):
            fail("invalid-reconciliation-check", "Each check must be an object")
            continue
        check_id = item.get("id")
        check["id"] = check_id if isinstance(check_id, str) else ""
        if not isinstance(check_id, str) or not check_id.strip() or check_id in seen:
            fail("invalid-reconciliation-check-id", "Check IDs must be unique non-empty strings")
            continue
        seen.add(check_id)
        locations = [item.get("left_cell"), item.get("right_cell"), item.get("check_cell")]
        parsed = [fm._parse_location(value) for value in locations]
        if any(p is None for p in parsed) or len({p[0] for p in parsed if p}) != 1:
            fail("invalid-reconciliation-location", "All cells must be valid references on the same worksheet")
            continue
        tolerance = item.get("tolerance")
        if (isinstance(tolerance, bool) or not isinstance(tolerance, (int, float))
                or not math.isfinite(float(tolerance)) or tolerance < 0):
            fail("invalid-reconciliation-tolerance", "Tolerance must be a finite non-negative number")
            continue
        left, right, mark = (recalculated.get(loc) for loc in locations)
        if left is None or right is None or mark is None:
            fail("recalc-cell-missing", "One or more declared cells are missing after recalculation")
            continue
        a, b, c = fm._number(left["value"]), fm._number(right["value"]), fm._number(mark["value"])
        if a is None or b is None or c is None:
            fail("recalc-value-not-numeric", "Both sides and the check cell must be finite numbers after recalculation")
            continue
        if not mark["formula"]:
            fail("recalc-check-cell-not-formula", "The check cell must be a formula, not a typed value")
        difference = a - b
        check.update({"left_cell": locations[0], "right_cell": locations[1], "check_cell": locations[2],
                      "left_value": a, "right_value": b, "recalculated_difference": difference,
                      "recalculated_check_value": c, "tolerance": float(tolerance)})
        if abs(difference) > tolerance:
            fail("recalc-values-differ", f"Recalculated sides differ by {difference}; tolerance is {float(tolerance)}")
        if abs(c - difference) > max(float(tolerance), ABS_TOLERANCE):
            fail("recalc-check-cell-disagrees", f"Check cell recalculates to {c} but the sides differ by {difference}")
        check["status"] = "pass" if not check["findings"] else "fail"
    result["status"] = "pass" if all(c["status"] == "pass" for c in result["checks"]) and not result["findings"] else "fail"
    return result


def audit(workbook: Path, contract: Path | None = None, engine: str | None = None,
          timeout: int = DEFAULT_TIMEOUT_SECONDS, require_fresh_cache: bool = False,
          require_contract: bool = False) -> dict:
    workbook = Path(workbook)
    report: dict = {"workbook": workbook.as_posix(), "status": "not-assessed", "engine": None,
                    "findings": [], "warnings": []}
    if workbook.suffix.lower() != ".xlsx":
        report["status"] = "fail"
        report["findings"].append({"code": "unsupported-file-type", "message": "Only .xlsx workbooks are recalculated"})
        return report
    try:
        report["workbook_sha256"] = hashlib.sha256(workbook.read_bytes()).hexdigest()
    except OSError as exc:
        report["status"] = "fail"
        report["findings"].append({"code": "unreadable-workbook", "message": str(exc)})
        return report
    if require_contract and contract is None:
        report["status"] = "fail"
        report["findings"].append({"code": "missing-reconciliation-contract",
                                   "message": "A reconciliation-checks JSON file is required"})
        return report
    binary = find_engine(engine)
    if binary is None:
        report["findings"].append({"code": "engine-unavailable",
                                   "message": "No LibreOffice engine found; recalculation is NOT_ASSESSED, not a pass"})
        return report
    report["engine"] = {"name": Path(binary).name, "version": engine_version(binary)}
    with tempfile.TemporaryDirectory(prefix="recalc-check-") as temp:
        try:
            recalculated_path = recalculate(workbook, binary, Path(temp), timeout)
            original_cells = read_cells(workbook)
            recalculated_cells = read_cells(recalculated_path)
        except EngineUnavailable as exc:
            report["findings"].append({"code": "engine-failed", "message": str(exc)})
            return report
        except (OSError, zipfile.BadZipFile, ET.ParseError, KeyError) as exc:
            report["status"] = "fail"
            report["findings"].append({"code": "unreadable-workbook", "message": str(exc)})
            return report
    summary = compare(original_cells, recalculated_cells)
    report.update(summary)
    if summary["error_count"]:
        report["findings"].append({"code": "error-after-recalculation",
                                   "message": f"{summary['error_count']} formula cells evaluate to a spreadsheet error"})
    if summary["missing_after_recalculation"]:
        report["findings"].append({"code": "formula-lost-in-recalculation",
                                   "message": f"{summary['missing_after_recalculation']} formula cells absent from the recalculated copy"})
    if summary["stale_cache_count"]:
        entry = {"code": "stale-formula-cache",
                 "message": f"{summary['stale_cache_count']} of {summary['formula_cells']} formula cells store a value that differs from the recalculated value"}
        (report["findings"] if require_fresh_cache else report["warnings"]).append(entry)
    if contract is not None:
        report["reconciliation"] = evaluate_contract(Path(contract), recalculated_cells)
        for item in report["reconciliation"]["findings"]:
            report["findings"].append(item)
        for check in report["reconciliation"]["checks"]:
            for item in check["findings"]:
                report["findings"].append({**item, "check": check["id"]})
    report["status"] = "pass" if not report["findings"] else "fail"
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--checks", type=Path, help="reconciliation-checks JSON (schema_version 1.0.0)")
    parser.add_argument("--require-checks", action="store_true", help="fail when no contract is supplied")
    parser.add_argument("--require-fresh-cache", action="store_true",
                        help="treat stale stored values as an error rather than a warning")
    parser.add_argument("--engine", help="path or name of the soffice or libreoffice binary")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args(argv)
    report = audit(args.workbook, args.checks, args.engine, args.timeout,
                   args.require_fresh_cache, args.require_checks)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    label = {"pass": "PASS", "fail": "FAIL", "not-assessed": "NOT_ASSESSED"}[report["status"]]
    print(f"{label}: {report['workbook']} ({len(report['findings'])} findings, {len(report['warnings'])} warnings)")
    for item in report["findings"] + report["warnings"]:
        print(f"- {item['code']}: {item['message']}")
    return {"pass": 0, "fail": 1, "not-assessed": 2}[report["status"]]


if __name__ == "__main__":
    sys.exit(main())
