from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from scripts.aqar_cash_timing_fixture import FIXTURE, run_fixture, validate_fixture


class AqarCashTimingFixtureTests(unittest.TestCase):
    def test_collection_timing_changes_liquidity_without_changing_billings(self) -> None:
        results = run_fixture()
        self.assertEqual({row["scenario"] for row in results}, {"upside", "base", "downside"})
        self.assertEqual({tuple(row["monthly_billings_scu"]) for row in results}, {(100, 100, 100, 100)})
        self.assertEqual(
            [row["required_funding_scu"] for row in results],
            [0, 60, 120],
        )
        self.assertEqual(
            [row["ending_receivables_scu"] for row in results],
            [0, 100, 200],
        )
        self.assertEqual(
            [row["unfunded_gap_scu"] for row in results],
            [0, 0, 45],
        )

    def test_collection_scenarios_change_the_milestone_action(self) -> None:
        results = run_fixture()
        self.assertEqual(results[0]["management_action"], "PROCEED_SYNTHETIC_BASELINE")
        self.assertEqual(
            results[1]["management_action"],
            "USE_BUFFER_AND_HOLD_NEXT_MILESTONE_UNTIL_COLLECTIONS_CONFIRM",
        )
        self.assertEqual(
            results[2]["management_action"],
            "DEFER_ROLLOUT_UNTIL_FUNDING_OWNER_APPROVES",
        )

    def test_missing_owner_source_or_effective_date_is_blocked(self) -> None:
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        broken = copy.deepcopy(data)
        del broken["assumptions"][0]["owner"]
        self.assertTrue(any("assumption missing fields" in e for e in validate_fixture(broken)))
        broken = copy.deepcopy(data)
        broken["scenarios"][0]["source_id"] = "UNKNOWN"
        self.assertTrue(any("source, date, and owner" in e for e in validate_fixture(broken)))

    def test_real_market_and_accounting_claims_remain_unassessed(self) -> None:
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(data["scope"]["market_denominator"], "NOT_ASSESSED")
        self.assertEqual(data["finance_boundary"]["revenue_recognition"], "NOT_ASSESSED")
        self.assertTrue(all("SCU" in item["unit"] for item in data["assumptions"]))

    def test_invalid_negative_and_boolean_collection_inputs_are_blocked(self) -> None:
        data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        broken = copy.deepcopy(data)
        broken["model"]["monthly_billings_scu"] = -1
        self.assertIn(
            "cash, billings, costs, and liquidity must be non-negative",
            validate_fixture(broken),
        )
        broken = copy.deepcopy(data)
        broken["scenarios"][0]["collection_lag_months"] = True
        self.assertTrue(
            any("integer collection lag" in error for error in validate_fixture(broken))
        )


if __name__ == "__main__":
    unittest.main()
