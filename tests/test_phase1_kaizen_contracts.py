"""Deterministic checks for the Phase 1 Kaizen reference contracts."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "phase1-kaizen-contracts.json"


class Phase1KaizenContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_reference_surfaces_exist(self):
        paths = [
            "docs/kaizen/fpa-assumption-trace.md",
            "skills/pipeline/10-financial-projections/references/manager-financial-intelligence-brief.md",
            "skills/meta-strategy/meta-digital-transformation/references/business-agility-readiness-map.md",
            "skills/meta-strategy/meta-monitoring-evaluation/references/strategy-map-scorecard-trace.md",
            "references/healthcare-payer-assumptions-and-reconciliation.md",
            "references/healthcare-workforce-and-learning-loop.md",
            "references/healthcare-workforce-cost-and-capacity-scenarios.md",
        ]
        for path in paths:
            self.assertTrue((ROOT / path).is_file(), path)

    def test_profit_and_cash_bridges_reconcile(self):
        f = self.data["financial_intelligence"]
        self.assertEqual(f["revenue"] - f["direct_costs"] - f["operating_costs"], 30000)
        self.assertEqual(f["opening_cash"] + f["collected_receipts"] - f["paid_outflows"], f["closing_cash"])
        self.assertEqual(f["currency"], "SYN")
        self.assertEqual(f["reviewer_role"], "synthetic-finance-reviewer")

    def test_payer_volume_and_ar_reconcile(self):
        p = self.data["payer"]
        self.assertEqual(p["claims_submitted"], p["claims_accepted"] + p["claims_rejected"])
        self.assertEqual(p["opening_ar"] + p["accepted_claim_value"] - p["payer_remittances"], p["ending_ar"])
        self.assertEqual(p["ending_ar"], p["ledger_control_ar"])
        self.assertEqual(p["rate_status"], "synthetic-assumption")
        for field in ("source_id", "period", "currency", "basis", "reviewer_role"):
            self.assertTrue(p[field], field)

    def test_missing_payer_rate_is_not_a_pass(self):
        p = dict(self.data["payer"])
        p["rate_status"] = "missing"
        self.assertNotEqual(p["rate_status"], "verified")
        self.assertIn(p["rate_status"], {"missing", "not-assessed", "synthetic-assumption"})

    def test_workforce_capacity_and_cost_are_reproducible(self):
        w = self.data["workforce"]
        capacity = (
            w["fte"]
            * w["available_hours"]
            * (1 - w["absence_training_allowance"])
            * w["utilisation"]
            * w["competency_factor"]
        )
        people_cost = w["fte"] * w["monthly_pay"] + w["benefits"]
        self.assertEqual(capacity, 172.8)
        self.assertEqual(people_cost, 2200)
        self.assertEqual(w["statutory_status"], "not-assessed")
        for field in ("source_id", "period", "currency", "basis", "reviewer_role"):
            self.assertTrue(w[field], field)

    def test_readiness_requires_baseline_owner_oracle_and_rollback(self):
        readiness = self.data["readiness"]
        self.assertTrue(all(readiness.values()))
        incomplete = dict(readiness)
        incomplete["baseline_present"] = False
        self.assertFalse(all(incomplete.values()))

    def test_scorecard_trace_has_source_owner_threshold_and_decision(self):
        scorecard = self.data["scorecard"]
        for field in ("formula", "source_id", "owner", "threshold", "decision"):
            self.assertIn(field, scorecard)
            self.assertIsNotNone(scorecard[field])


if __name__ == "__main__":
    unittest.main()
