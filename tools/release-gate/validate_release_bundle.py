#!/usr/bin/env python3
"""Validate blocker-first business-plan release evidence bundles."""

from __future__ import annotations

import argparse
import json
from runpy import run_path
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STAGES = {"intake", "evidence", "business-logic", "sections", "model-finance",
          "challenge", "assembly", "finalisation"}
HANDOFFS = {"research", "finance", "spreadsheet", "design", "document", "security"}
STATES = {"pass", "pass-with-caveats", "fail", "not-assessed", "not-applicable"}


def _state(value: object, allowed: set[str] = STATES) -> bool:
    return isinstance(value, str) and value in allowed


def _text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _resolve(bundle_path: Path, value: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute():
        return candidate
    local = (bundle_path.parent / candidate).resolve()
    return local if local.exists() else (ROOT / candidate).resolve()


def _check_paths(bundle_path: Path, values: object, label: str, errors: list[str]) -> None:
    if not isinstance(values, list):
        errors.append(f"{label}: evidence must be a list")
        return
    for value in values:
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}: evidence entries must be non-empty paths")
        elif not _resolve(bundle_path, value).is_file():
            errors.append(f"{label}: evidence path does not exist: {value}")


def _check_workbook_reconciliation(bundle_path: Path, handoff: dict,
                                   label: str, errors: list[str]) -> None:
    workbook_values = handoff.get("input_versions", [])
    if not isinstance(workbook_values, list):
        return
    workbook_refs = [value for value in workbook_values
                     if isinstance(value, str) and value.lower().endswith(".xlsx")]
    if not workbook_refs:
        return
    state = handoff.get("state")
    requires_pass = state in {"pass", "pass-with-caveats"}
    report_ref = handoff.get("reconciliation_report")
    contract_ref = handoff.get("reconciliation_contract")
    if (not isinstance(report_ref, str) or not report_ref.strip()
            or not isinstance(contract_ref, str) or not contract_ref.strip()):
        if requires_pass:
            errors.append(f"{label}: a passing XLSX handoff requires reconciliation_report and reconciliation_contract")
        return
    report_path = _resolve(bundle_path, report_ref)
    contract_path = _resolve(bundle_path, contract_ref)
    if not report_path.is_file():
        errors.append(f"{label}: reconciliation report does not exist: {report_ref}")
        return
    if not contract_path.is_file():
        errors.append(f"{label}: reconciliation contract does not exist: {contract_ref}")
        return
    if len(workbook_refs) != 1:
        errors.append(f"{label}: reconciliation report must be tied to exactly one XLSX input")
        return
    workbook_path = _resolve(bundle_path, workbook_refs[0])
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{label}: reconciliation report cannot be read: {exc}")
        return
    if not isinstance(report, dict):
        errors.append(f"{label}: reconciliation report must be an object")
        return
    try:
        audit = run_path(str(ROOT / "tools/workbook-audit/formula_map.py"))["audit_workbook"]
        recomputed = audit(workbook_path, reconciliation_checks=contract_path,
                           require_reconciliation=True)
    except Exception as exc:
        errors.append(f"{label}: workbook reconciliation cannot be recomputed: {exc}")
        return
    checks = recomputed.get("reconciliation", {}).get("checks", [])
    if (recomputed.get("status") != "pass"
            or recomputed.get("reconciliation", {}).get("status") != "pass"
            or not checks
            or any(not isinstance(check, dict) or check.get("status") != "pass"
                   for check in checks)):
        if requires_pass:
            errors.append(f"{label}: recomputed workbook reconciliation is missing or non-passing")
        return
    if report.get("status") != "pass" or report.get("workbook_sha256") != recomputed.get("workbook_sha256"):
        if requires_pass:
            errors.append(f"{label}: reconciliation report does not match the workbook audit")
        return
    if report.get("reconciliation") != recomputed.get("reconciliation"):
        if requires_pass:
            errors.append(f"{label}: reconciliation report does not match recomputed check results")


def validate(bundle_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(bundle_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"bundle cannot be read: {exc}"]
    if not isinstance(data, dict):
        return ["bundle must be an object"]
    if data.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    for key in ("artefact", "audience"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"{key} is required")

    stages = data.get("stages")
    if not isinstance(stages, list):
        errors.append("stages must be a list")
        stages = []
    stage_ids = {item.get("id") for item in stages
                 if isinstance(item, dict) and isinstance(item.get("id"), str)}
    if stage_ids != STAGES or len(stages) != len(STAGES):
        errors.append(f"stages must contain exactly {sorted(STAGES)}")
    for item in stages:
        if not isinstance(item, dict):
            errors.append("stage entries must be objects")
            continue
        state = item.get("state")
        if not _state(state, STATES - {"not-applicable"}):
            errors.append(f"stage {item.get('id')}: invalid state {state}")
        if not _text(item.get("owner")):
            errors.append(f"stage {item.get('id')}: owner is required")
        _check_paths(bundle_path, item.get("evidence"), f"stage {item.get('id')}", errors)
        if state in ("pass", "pass-with-caveats") and not item.get("evidence"):
            errors.append(f"stage {item.get('id')}: passing state requires evidence")

    handoffs = data.get("handoffs")
    if not isinstance(handoffs, dict) or set(handoffs) != HANDOFFS:
        errors.append(f"handoffs must contain exactly {sorted(HANDOFFS)}")
        handoffs = handoffs if isinstance(handoffs, dict) else {}
    for name, item in handoffs.items():
        if not isinstance(item, dict):
            errors.append(f"handoff {name}: must be an object")
            continue
        applicable = item.get("applicable")
        state = item.get("state")
        if not isinstance(applicable, bool) or not _state(state):
            errors.append(f"handoff {name}: applicability and state are invalid")
        if applicable and state == "not-applicable":
            errors.append(f"handoff {name}: applicable handoff cannot be not-applicable")
        if not applicable and (state != "not-applicable" or not _text(item.get("reason"))):
            errors.append(f"handoff {name}: non-applicable handoff needs reason and not-applicable state")
        if not _text(item.get("receiver")):
            errors.append(f"handoff {name}: receiver is required")
        if not isinstance(item.get("requested_decision"), str) or not item["requested_decision"].strip():
            errors.append(f"handoff {name}: requested_decision is required")
        _check_paths(bundle_path, item.get("input_versions"), f"handoff {name} input_versions", errors)
        if applicable and not item.get("input_versions"):
            errors.append(f"handoff {name}: applicable handoff requires input_versions")
        _check_paths(bundle_path, item.get("evidence"), f"handoff {name}", errors)
        if name == "spreadsheet":
            _check_workbook_reconciliation(bundle_path, item, f"handoff {name}", errors)
        if applicable and state in ("pass", "pass-with-caveats") and not item.get("evidence"):
            errors.append(f"handoff {name}: passing state requires evidence")
        if state == "pass-with-caveats" and not item.get("caveats"):
            errors.append(f"handoff {name}: pass-with-caveats requires a named caveat")

    finalisation = data.get("finalisation")
    if not isinstance(finalisation, dict):
        errors.append("finalisation must be an object")
        finalisation = {}
    render = finalisation.get("render")
    if not isinstance(render, dict) or not _state(render.get("state")):
        errors.append("finalisation render record is invalid")
        render = {}
    if not isinstance(render.get("required"), bool):
        errors.append("finalisation render: required must be boolean")
    _check_paths(bundle_path, render.get("evidence"), "finalisation render", errors)
    for name in ("reviewer_notes", "audit_log", "release_checklist"):
        _check_paths(bundle_path, finalisation.get(name), f"finalisation {name}", errors)

    authority = data.get("release_authority")
    if not isinstance(authority, dict) or not _state(authority.get("state")):
        errors.append("release_authority is invalid")
        authority = {}
    if not isinstance(authority.get("required"), bool):
        errors.append("release_authority: required must be boolean")
    if not _text(authority.get("role")):
        errors.append("release_authority: role is required")
    _check_paths(bundle_path, authority.get("evidence"), "release_authority", errors)
    if authority.get("state") == "pass" and not authority.get("evidence"):
        errors.append("release_authority: passing state requires evidence")
    if render.get("state") == "pass" and not render.get("evidence"):
        errors.append("finalisation render: passing state requires evidence")

    blocked = any(item.get("state") in ("fail", "not-assessed") for item in stages if isinstance(item, dict))
    blocked |= any(item.get("applicable") and item.get("state") in ("fail", "not-assessed")
                   for item in handoffs.values() if isinstance(item, dict))
    blocked |= bool(render.get("required") and render.get("state") != "pass")
    blocked |= any(not finalisation.get(name) for name in ("reviewer_notes", "audit_log", "release_checklist"))
    blocked |= bool(authority.get("required") and authority.get("state") != "pass")
    declared = data.get("release_state")
    if declared not in ("release", "blocked"):
        errors.append("release_state must be release or blocked")
    if blocked and declared != "blocked":
        errors.append("blocker precedence requires release_state=blocked")
    if not blocked and declared != "release":
        errors.append("all mandatory gates pass but release_state is not release")
    blockers = data.get("blockers")
    if not isinstance(blockers, list):
        errors.append("blockers must be a list")
    elif blocked and not blockers:
        errors.append("blocked bundle must name at least one blocker")
    elif not blocked and blockers:
        errors.append("release bundle cannot retain blockers")
    if isinstance(blockers, list):
        required = {"id", "owner", "finding", "recovery"}
        for index, blocker in enumerate(blockers):
            if not isinstance(blocker, dict) or not required <= set(blocker) or not all(blocker.get(key) for key in required):
                errors.append(f"blocker {index}: id, owner, finding and recovery are required")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", type=Path)
    args = parser.parse_args()
    failures = validate(args.bundle.resolve())
    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        return 1
    data = json.loads(args.bundle.read_text(encoding="utf-8"))
    print(f"PASS: release bundle is structurally valid; decision={data['release_state']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
