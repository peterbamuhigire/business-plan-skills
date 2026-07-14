#!/usr/bin/env python3
"""Validate blocker-first business-plan release evidence bundles."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STAGES = {"intake", "evidence", "business-logic", "sections", "model-finance",
          "challenge", "assembly", "finalisation"}
HANDOFFS = {"research", "finance", "spreadsheet", "design", "document", "security"}
STATES = {"pass", "pass-with-caveats", "fail", "not-assessed", "not-applicable"}


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


def validate(bundle_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(bundle_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"bundle cannot be read: {exc}"]
    if data.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    for key in ("artefact", "audience"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"{key} is required")

    stages = data.get("stages")
    if not isinstance(stages, list):
        errors.append("stages must be a list")
        stages = []
    stage_ids = {item.get("id") for item in stages if isinstance(item, dict)}
    if stage_ids != STAGES or len(stages) != len(STAGES):
        errors.append(f"stages must contain exactly {sorted(STAGES)}")
    for item in stages:
        if not isinstance(item, dict):
            errors.append("stage entries must be objects")
            continue
        state = item.get("state")
        if state not in STATES - {"not-applicable"}:
            errors.append(f"stage {item.get('id')}: invalid state {state}")
        if not item.get("owner"):
            errors.append(f"stage {item.get('id')}: owner is required")
        _check_paths(bundle_path, item.get("evidence"), f"stage {item.get('id')}", errors)
        if state in {"pass", "pass-with-caveats"} and not item.get("evidence"):
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
        if not isinstance(applicable, bool) or state not in STATES:
            errors.append(f"handoff {name}: applicability and state are invalid")
        if applicable and state == "not-applicable":
            errors.append(f"handoff {name}: applicable handoff cannot be not-applicable")
        if not applicable and (state != "not-applicable" or not item.get("reason")):
            errors.append(f"handoff {name}: non-applicable handoff needs reason and not-applicable state")
        if not item.get("receiver"):
            errors.append(f"handoff {name}: receiver is required")
        if not isinstance(item.get("requested_decision"), str) or not item["requested_decision"].strip():
            errors.append(f"handoff {name}: requested_decision is required")
        _check_paths(bundle_path, item.get("input_versions"), f"handoff {name} input_versions", errors)
        if applicable and not item.get("input_versions"):
            errors.append(f"handoff {name}: applicable handoff requires input_versions")
        _check_paths(bundle_path, item.get("evidence"), f"handoff {name}", errors)
        if applicable and state in {"pass", "pass-with-caveats"} and not item.get("evidence"):
            errors.append(f"handoff {name}: passing state requires evidence")
        if state == "pass-with-caveats" and not item.get("caveats"):
            errors.append(f"handoff {name}: pass-with-caveats requires a named caveat")

    finalisation = data.get("finalisation")
    if not isinstance(finalisation, dict):
        errors.append("finalisation must be an object")
        finalisation = {}
    render = finalisation.get("render")
    if not isinstance(render, dict) or render.get("state") not in STATES:
        errors.append("finalisation render record is invalid")
        render = {}
    _check_paths(bundle_path, render.get("evidence"), "finalisation render", errors)
    for name in ("reviewer_notes", "audit_log", "release_checklist"):
        _check_paths(bundle_path, finalisation.get(name), f"finalisation {name}", errors)

    authority = data.get("release_authority")
    if not isinstance(authority, dict) or authority.get("state") not in STATES:
        errors.append("release_authority is invalid")
        authority = {}
    _check_paths(bundle_path, authority.get("evidence"), "release_authority", errors)
    if authority.get("state") == "pass" and not authority.get("evidence"):
        errors.append("release_authority: passing state requires evidence")
    if render.get("state") == "pass" and not render.get("evidence"):
        errors.append("finalisation render: passing state requires evidence")

    blocked = any(item.get("state") in {"fail", "not-assessed"} for item in stages if isinstance(item, dict))
    blocked |= any(item.get("applicable") and item.get("state") in {"fail", "not-assessed"}
                   for item in handoffs.values() if isinstance(item, dict))
    blocked |= bool(render.get("required") and render.get("state") != "pass")
    blocked |= any(not finalisation.get(name) for name in ("reviewer_notes", "audit_log", "release_checklist"))
    blocked |= bool(authority.get("required") and authority.get("state") != "pass")
    declared = data.get("release_state")
    if declared not in {"release", "blocked"}:
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
