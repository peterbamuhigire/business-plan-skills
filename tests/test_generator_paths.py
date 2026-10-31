"""Workbook generators must write to the files that actually ship."""

from __future__ import annotations

import ast
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GENERATORS = sorted((ROOT / "scripts" / "build-financial-models").glob("build_*.py"))


def output_path(script: Path) -> Path:
    """Evaluate `OUT = normpath(join(HERE, '..', '..', ...))` statically, without importing xlsxwriter."""
    tree = ast.parse(script.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", "") == "OUT" for t in node.targets):
            call = node.value
            while isinstance(call, ast.Call) and call.args and isinstance(call.args[0], ast.Call):
                call = call.args[0]
            parts = [a.value for a in call.args[1:] if isinstance(a, ast.Constant)]
            return (script.parent.joinpath(*parts)).resolve()
    raise AssertionError(f"{script.name}: no OUT assignment found")


class GeneratorPathTests(unittest.TestCase):
    def test_there_are_seven_generators(self):
        self.assertEqual(7, len(GENERATORS))

    def test_every_generator_targets_a_shipped_workbook(self):
        shipped = {path.resolve() for path in (ROOT / "skills").glob("**/templates/*.xlsx")}
        for script in GENERATORS:
            with self.subTest(script=script.name):
                target = output_path(script)
                self.assertTrue(target.is_relative_to(ROOT), target)
                self.assertIn(target, shipped, f"{script.name} would write {target}, which is not a shipped workbook")

    def test_generators_cover_every_shipped_workbook_exactly_once(self):
        shipped = sorted((ROOT / "skills").glob("**/templates/*.xlsx"))
        targets = sorted(output_path(script) for script in GENERATORS)
        self.assertEqual([path.resolve() for path in shipped], targets)


if __name__ == "__main__":
    unittest.main()
