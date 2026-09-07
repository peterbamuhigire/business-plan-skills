#!/usr/bin/env python3
"""Validate a synthetic business-plan claim/cell/output trace and recalculation record."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def validate(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or data.get("fixture_label") != "FICTIONAL TEST DATA":
        return ["fixture_label must be FICTIONAL TEST DATA"]
    claims = data.get("claims")
    cells = data.get("cells")
    outputs = data.get("outputs")
    if not all(isinstance(x, list) for x in (claims, cells, outputs)):
        return ["claims, cells and outputs must be lists"]
    claim_ids = {x.get("id") for x in claims if isinstance(x, dict)}
    cell_ids = {x.get("id") for x in cells if isinstance(x, dict)}
    output_ids = {x.get("id") for x in outputs if isinstance(x, dict)}
    for claim in claims:
        if not isinstance(claim, dict) or not claim.get("id") or not claim.get("source_or_assumption"):
            errors.append("each claim needs id and source_or_assumption")
        elif not claim.get("cell_ids"):
            errors.append(f"claim {claim['id']} needs cell_ids")
        else:
            errors.extend(f"claim {claim['id']} references unknown cell {cid}" for cid in claim["cell_ids"] if cid not in cell_ids)
    for cell in cells:
        if not isinstance(cell, dict) or not cell.get("id") or not cell.get("output_ids"):
            errors.append("each cell needs id and output_ids")
        elif any(oid not in output_ids for oid in cell["output_ids"]):
            errors.append(f"cell {cell.get('id')} references unknown output")
    for output in outputs:
        if not isinstance(output, dict) or not output.get("id") or not output.get("value"):
            errors.append("each output needs id and nonzero value")
    recalc = data.get("recalculation")
    if not isinstance(recalc, dict) or recalc.get("status") != "recalculated":
        errors.append("recalculation status must be recalculated")
    if isinstance(recalc, dict) and recalc.get("scenario") not in {"base", "downside"}:
        errors.append("recalculation scenario must be base or downside")
    if isinstance(recalc, dict) and recalc.get("revenue") != recalc.get("units", 0) * recalc.get("price", 0):
        errors.append("recalculated revenue does not equal units times price")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_plan_trace.py TRACE.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1
    errors = validate(data)
    print("PASS" if not errors else "FAIL")
    for error in errors:
        print(f"[ERROR] {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
