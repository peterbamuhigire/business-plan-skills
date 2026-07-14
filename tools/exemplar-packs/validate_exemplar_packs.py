#!/usr/bin/env python3
"""Validate complete audience exemplar packages."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACK_ROOT = ROOT / "examples/full-plan-packages"
EXPECTED = {"dfi-loan-uganda": "dfi", "grant-east-africa": "grant",
            "vc-east-africa": "vc", "owner-manager-uganda": "owner-board"}
REQUIRED_FILES = {"plan.md", "deck.md", "model-overlay.json", "evidence-manifest.json",
                  "annex-index.md", "committee-manifest.json", "committee-result.json",
                  "release-bundle.json"}
PLAN_SECTIONS = [f"## {number}." for number in range(1, 11)]


def validate() -> list[str]:
    errors = []
    for pack, audience in EXPECTED.items():
        directory = PACK_ROOT / pack
        missing = [name for name in REQUIRED_FILES if not (directory / name).exists()]
        if missing:
            errors.append(f"{pack}: missing {sorted(missing)}")
            continue
        plan = (directory / "plan.md").read_text(encoding="utf-8")
        for heading in PLAN_SECTIONS:
            if heading not in plan:
                errors.append(f"{pack}: missing plan section {heading}")
        deck = (directory / "deck.md").read_text(encoding="utf-8")
        if sum(1 for line in deck.splitlines() if line[:1].isdigit() and ". **" in line) < 10:
            errors.append(f"{pack}: deck has fewer than 10 decision slides")
        overlay = json.loads((directory / "model-overlay.json").read_text(encoding="utf-8"))
        if overlay.get("audience") != audience:
            errors.append(f"{pack}: audience mismatch")
        base = ROOT / overlay.get("base_workbook", "")
        if not base.is_file():
            errors.append(f"{pack}: base workbook missing")
        if len(overlay.get("scenarios", {})) < 3 or len(overlay.get("required_checks", [])) < 5:
            errors.append(f"{pack}: incomplete scenarios or model checks")
        if not (ROOT / overlay.get("formula_map", "")).is_file():
            errors.append(f"{pack}: formula-map report missing")
        evidence = json.loads((directory / "evidence-manifest.json").read_text(encoding="utf-8"))
        if not evidence.get("fictional") or len(evidence.get("claims", [])) < 3:
            errors.append(f"{pack}: evidence manifest incomplete")
        if not all({"id", "claim", "class", "source", "status"} <= set(item) for item in evidence.get("claims", [])):
            errors.append(f"{pack}: malformed evidence claim")
        committee = json.loads((directory / "committee-manifest.json").read_text(encoding="utf-8"))
        for name, value in committee.get("artefacts", {}).items():
            target = value.split("#", 1)[0]
            if not (directory / target).resolve().is_file():
                errors.append(f"{pack}: committee artefact {name} is missing: {target}")
        result = json.loads((directory / "committee-result.json").read_text(encoding="utf-8"))
        if result.get("status") != "pass" or result.get("audience") != audience:
            errors.append(f"{pack}: committee result is invalid")
        release = json.loads((directory / "release-bundle.json").read_text(encoding="utf-8"))
        if release.get("release_state") != "blocked" or release.get("audience") != audience:
            errors.append(f"{pack}: exemplar release bundle must remain honestly blocked")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        sys.exit(1)
    print("PASS: 4 complete audience exemplar packs; 32 required artefacts")
