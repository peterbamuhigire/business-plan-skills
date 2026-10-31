"""Routing smoke test: first-place precision, coverage report and silently skipped skills."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "routing_smoke_test.py"


def skill(root: Path, name: str, description: str) -> None:
    folder = root / "skills" / "group" / name
    folder.mkdir(parents=True)
    (folder / "SKILL.md").write_text(
        f"---\nname: {name}\ndescription: {description}\n---\n\n## Use When\n\n- {description}\n", encoding="utf-8")


def run(root: Path, fixtures: list[dict], *extra: str) -> subprocess.CompletedProcess:
    path = root / "fixtures.json"
    path.write_text(json.dumps(fixtures), encoding="utf-8")
    return subprocess.run([sys.executable, "-B", "-X", "utf8", str(SCRIPT), "--root", str(root),
                           "--fixtures", str(path), *extra], capture_output=True, text=True,
                          encoding="utf-8", check=False)


class RoutingReportTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        skill(self.root, "alpha-budget", "Use when drafting an operating budget with monthly cash lines")
        skill(self.root, "beta-hiring", "Use when planning recruitment, interviews and offer letters")

    def tearDown(self):
        self._tmp.cleanup()

    def fixtures(self):
        return [
            {"id": "p1", "class": "positive", "prompt": "draft the operating budget with monthly cash lines", "expected": "alpha-budget"},
            {"id": "p2", "class": "positive", "prompt": "plan recruitment and interviews", "expected": "beta-hiring"},
            {"id": "n1", "class": "negative", "prompt": "plan recruitment and offer letters", "expected": "beta-hiring", "excluded": ["alpha-budget"]},
        ]

    def test_report_prints_first_place_precision_and_coverage(self):
        result = run(self.root, self.fixtures(), "--report")
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("precision@1: 3/3 (100.0%)", result.stdout)
        self.assertIn("skills with at least one fixture: 2/2", result.stdout)
        self.assertIn("skills with 3 positives and 2 owned negatives: 0/2", result.stdout)

    def test_report_is_opt_in(self):
        self.assertNotIn("precision@1", run(self.root, self.fixtures()).stdout)

    def test_first_place_floor_fails_when_missed(self):
        fixtures = self.fixtures() + [
            {"id": "weak", "class": "positive", "prompt": "plan recruitment and interviews and a budget with cash lines", "expected": "beta-hiring"}]
        result = run(self.root, fixtures, "--min-precision-at-1", "1.0")
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("below the required", result.stdout)

    def test_skill_with_unparseable_frontmatter_is_reported_not_silently_dropped(self):
        folder = self.root / "skills" / "group" / "gamma-broken"
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(
            "---\nname: gamma-broken\ndescription: Use for gamma work: it breaks YAML\n---\n\n## Use When\n\n- x\n",
            encoding="utf-8")
        result = run(self.root, self.fixtures())
        self.assertEqual(1, result.returncode, result.stdout)
        self.assertIn("skill skipped, so it cannot be routed to", result.stdout)
        self.assertIn("gamma-broken", result.stdout)

    def test_repository_has_no_skipped_skills_and_keeps_its_coverage_floor(self):
        result = subprocess.run([sys.executable, "-B", "-X", "utf8", str(SCRIPT), "--threshold", "1.0", "--report"],
                                capture_output=True, text=True, encoding="utf-8", check=False, cwd=ROOT)
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertNotIn("skipped", result.stdout)
        covered = int(result.stdout.split("skills with 3 positives and 2 owned negatives: ")[1].split("/")[0])
        self.assertGreaterEqual(covered, 5)


if __name__ == "__main__":
    unittest.main()
