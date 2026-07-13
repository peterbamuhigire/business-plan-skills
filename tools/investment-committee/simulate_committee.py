#!/usr/bin/env python3
"""Validate and score an evidence-linked investment-committee manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AUDIENCES = {"lender", "dfi", "vc", "grant", "owner-board"}
CRITERIA = {"decision_funding": 15, "market_evidence": 15, "commercial_economics": 15,
            "model_integrity": 20, "delivery_management": 10, "risk_regulatory": 10,
            "evidence_governance": 10, "audience_specific": 5}
MANDATORY_ARTEFACTS = {"plan", "funding_ask", "model_formula_map", "evidence_register", "sector_gates"}


def simulate(manifest: dict) -> dict:
    errors = []
    audience = manifest.get("audience")
    if audience not in AUDIENCES:
        errors.append(f"unsupported audience: {audience!r}")
    artefacts = manifest.get("artefacts", {})
    missing = sorted(MANDATORY_ARTEFACTS - set(artefacts))
    if missing:
        errors.append(f"missing artefacts: {', '.join(missing)}")
    criteria = manifest.get("criteria", {})
    missing_criteria = sorted(set(CRITERIA) - set(criteria))
    if missing_criteria:
        errors.append(f"missing criteria: {', '.join(missing_criteria)}")
    blockers = list(manifest.get("blockers", []))
    weighted = 0.0
    scored = []
    for name, weight in CRITERIA.items():
        item = criteria.get(name, {})
        score = item.get("score")
        status = item.get("status")
        evidence = item.get("evidence")
        if status == "not-assessed":
            blockers.append(f"{name} not assessed")
            score = 0
        if not isinstance(score, (int, float)) or not 0 <= score <= 4:
            errors.append(f"{name}: score must be 0..4")
            score = 0
        if not evidence:
            errors.append(f"{name}: evidence pointer required")
        contribution = score / 4 * weight
        weighted += contribution
        scored.append({"criterion": name, "score": score, "weight": weight,
                       "contribution": round(contribution, 2), "evidence": evidence,
                       "status": status or "assessed"})
    fatal = [b for b in blockers if isinstance(b, dict) and b.get("severity") == "fatal"]
    blocker_text = [b.get("message", "unnamed blocker") if isinstance(b, dict) else str(b) for b in blockers]
    if errors:
        recommendation = "invalid-manifest"
    elif fatal:
        recommendation = "decline"
    elif blocker_text:
        recommendation = "defer"
    elif weighted >= 85 and not manifest.get("conditions"):
        recommendation = "progress-for-real-review"
    elif weighted >= 70:
        recommendation = "conditional-progress"
    else:
        recommendation = "defer"
    return {"status": "fail" if errors else "pass", "audience": audience,
            "weighted_score_percent": round(weighted, 2), "recommendation": recommendation,
            "blockers": blocker_text, "conditions": manifest.get("conditions", []),
            "dissent": manifest.get("dissent", []), "criteria": scored, "errors": errors}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    result = simulate(json.loads(args.manifest.read_text(encoding="utf-8")))
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 1 if result["status"] == "fail" else 0


if __name__ == "__main__":
    sys.exit(main())
