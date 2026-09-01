import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCE = (
    ROOT
    / "skills/meta-strategy/references/marketing-plan-handbook-operating-loop.md"
)
KAIZEN_SKILL = ROOT / "skills/meta-strategy/kaizen-improvement-system/SKILL.md"


class WoodMarketingPlanKaizenContractTests(unittest.TestCase):
    def test_independent_synthesis_contains_operating_loop_and_currentness_gate(self):
        self.assertTrue(REFERENCE.is_file())
        content = REFERENCE.read_text(encoding="utf-8").lower()
        for phrase in (
            "adaptive customer-first marketing plan",
            "current situation",
            "potential market",
            "qualified available",
            "segment evaluation",
            "strategy pyramid",
            "forecast",
            "budget",
            "leading and lagging",
            "corrective action",
            "marketing audit",
            "digital-research-skills",
            "not_assessed",
        ):
            self.assertIn(phrase, content, phrase)

    def test_kaizen_owner_links_the_synthesis(self):
        content = KAIZEN_SKILL.read_text(encoding="utf-8").lower()
        self.assertIn("marketing-plan-handbook-operating-loop.md", content)


if __name__ == "__main__":
    unittest.main()
