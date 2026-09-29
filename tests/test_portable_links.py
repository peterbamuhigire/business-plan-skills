"""Portable-link rule: sibling-engine and host-absolute links fail locally as they do in CI."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_skill_engine", ROOT / "scripts" / "validate_skill_engine.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(MODULE)


class PortableLinkTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        base = Path(self._tmp.name)
        self.repo = base / "business-plan-skills"
        self.skill = self.repo / "skills" / "group" / "skill" / "SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.skill.write_text("skill", encoding="utf-8")
        (self.skill.parent / "references").mkdir()
        (self.skill.parent / "references" / "local.md").write_text("local", encoding="utf-8")
        sibling = base / "chwezi-accounting-doctrine"
        sibling.mkdir()
        (sibling / "README.md").write_text("sibling", encoding="utf-8")
        self.outside = base / "outside.md"
        self.outside.write_text("outside", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def failures(self, target: str) -> list[str]:
        return MODULE.local_links(self.skill, f"- [link]({target})", self.repo)

    def test_in_repository_link_resolves(self):
        self.assertEqual([], self.failures("references/local.md"))

    def test_sibling_engine_link_fails_even_when_the_sibling_is_present(self):
        self.assertTrue(self.failures("../../../../chwezi-accounting-doctrine/README.md"))

    def test_host_absolute_link_fails_even_when_the_target_exists(self):
        resolved = self.outside.resolve()
        target = resolved.as_posix() if resolved.drive else "C:/wamp64/www/outside.md"
        self.assertTrue(self.failures(target))

    def test_github_url_is_accepted(self):
        self.assertEqual([], self.failures("https://github.com/peterbamuhigire/chwezi-accounting-doctrine/blob/main/README.md"))


if __name__ == "__main__":
    unittest.main()
