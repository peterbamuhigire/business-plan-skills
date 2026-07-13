import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("committee", ROOT / "tools/investment-committee/simulate_committee.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def manifest(score=4):
    return {"audience": "dfi", "artefacts": {key: f"evidence/{key}" for key in MODULE.MANDATORY_ARTEFACTS},
            "criteria": {key: {"score": score, "status": "assessed", "evidence": f"pack#{key}"}
                         for key in MODULE.CRITERIA}, "blockers": [], "conditions": [], "dissent": []}


class CommitteeTests(unittest.TestCase):
    def test_complete_pack_progresses_to_real_review(self):
        result = MODULE.simulate(manifest())
        self.assertEqual("pass", result["status"])
        self.assertEqual("progress-for-real-review", result["recommendation"])

    def test_blocker_precedes_score(self):
        data = manifest()
        data["blockers"] = [{"severity": "remediable", "message": "ESIA screen not assessed"}]
        self.assertEqual("defer", MODULE.simulate(data)["recommendation"])

    def test_missing_evidence_is_invalid(self):
        data = manifest()
        data["criteria"]["market_evidence"]["evidence"] = ""
        result = MODULE.simulate(data)
        self.assertEqual("fail", result["status"])
        self.assertEqual("invalid-manifest", result["recommendation"])


if __name__ == "__main__":
    unittest.main()
