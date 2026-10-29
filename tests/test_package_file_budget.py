import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "package_file_budget", ROOT / "scripts/check_package_file_budget.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PackageFileBudgetTests(unittest.TestCase):
    def test_hard_cap_rejects_either_count_over_5000(self):
        self.assertEqual([], MODULE.validate_counts({"checkout": 5000, "package": 4999}))
        for counts in ({"checkout": 5001, "package": 10},
                       {"checkout": 10, "package": 5001}):
            with self.subTest(counts=counts):
                self.assertTrue(MODULE.validate_counts(counts))

    def test_cli_does_not_accept_a_higher_cap_override(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check_package_file_budget.py"),
             str(ROOT), "--maximum-files", "9000"],
            capture_output=True, text=True, check=False)
        self.assertEqual(2, result.returncode)

    def test_small_fixture_counts_package_exclusions_and_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".git").mkdir()
            (root / ".git" / "object").write_text("hidden from package count")
            (root / "kept.txt").write_text("included")
            (root / "link.txt").symlink_to(root / "kept.txt")
            self.assertEqual(3, MODULE.count_entries(root))
            self.assertEqual(2, MODULE.count_entries(root, package_only=True))


if __name__ == "__main__":
    unittest.main()
