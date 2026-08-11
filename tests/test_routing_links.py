import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "routing_link_check", ROOT / "scripts/routing_link_check.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RoutingLinkTests(unittest.TestCase):
    def test_high_use_surfaces_resolve_route_references(self):
        self.assertEqual([], MODULE.scan(ROOT))

    def test_bounded_ai_skill_has_one_contract_heading_each(self):
        skill = ROOT / "skills/pipeline/14-ai-integration/SKILL.md"
        lines = skill.read_text(encoding="utf-8").splitlines()
        for heading in ("Required Inputs", "Workflow", "Anti-Patterns", "Outputs", "References"):
            self.assertEqual(
                1,
                sum(line.strip().lower() == f"## {heading}".lower() for line in lines),
                heading,
            )
        self.assertEqual(
            1,
            sum(line.strip().lower() == "## capability contract" for line in lines),
        )

    def test_route_link_cannot_escape_repository_root(self):
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary)
            root = parent / "repo"
            root.mkdir()
            outside = parent / "outside.md"
            outside.write_text("outside fixture\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[outside](../outside.md)\n",
                encoding="utf-8",
            )

            failures = MODULE.scan(root, ("README.md",))

            self.assertEqual(1, len(failures))
            self.assertIn("resolves outside repository", failures[0])


if __name__ == "__main__":
    unittest.main()
