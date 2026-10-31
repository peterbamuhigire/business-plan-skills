"""Recalculation evidence: formula-sourced tie-outs are tested on recalculated values."""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("recalc_check", ROOT / "tools/workbook-audit/recalc_check.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

HAS_ENGINE = MODULE.find_engine() is not None
NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"


def cell(ref: str, formula: str | None = None, value: str = "0") -> str:
    inner = f"<f>{formula}</f><v>{value}</v>" if formula is not None else f"<v>{value}</v>"
    return f'<c r="{ref}">{inner}</c>'


def write_workbook(path: Path, cells: list[str]) -> None:
    sheet = f'<?xml version="1.0"?><worksheet xmlns="{NS}"><sheetData><row r="1">{"".join(cells)}</row></sheetData></worksheet>'
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("[Content_Types].xml", '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        zf.writestr("_rels/.rels", '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        zf.writestr("xl/workbook.xml", f'<?xml version="1.0"?><workbook xmlns="{NS}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Model" sheetId="1" r:id="rId1"/></sheets></workbook>')
        zf.writestr("xl/_rels/workbook.xml.rels", '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>')
        zf.writestr("xl/worksheets/sheet1.xml", sheet)


def write_contract(path: Path, tolerance: float = 0) -> None:
    path.write_text(json.dumps({"schema_version": "1.0.0", "checks": [
        {"id": "cash-to-balance", "left_cell": "Model!B1", "right_cell": "Model!B2",
         "check_cell": "Model!B3", "tolerance": tolerance}]}), encoding="utf-8")


class ContractLogicTests(unittest.TestCase):
    """No engine needed: the comparison logic runs on supplied recalculated values."""

    @staticmethod
    def values(left="100", right="100", check="0", check_formula="B1-B2"):
        return {"Model!B1": {"formula": "10*10", "value": left, "kind": "n"},
                "Model!B2": {"formula": "50+50", "value": right, "kind": "n"},
                "Model!B3": {"formula": check_formula, "value": check, "kind": "n"}}

    def evaluate(self, cells, tolerance=0):
        with tempfile.TemporaryDirectory() as tmp:
            contract = Path(tmp) / "contract.json"
            write_contract(contract, tolerance)
            return MODULE.evaluate_contract(contract, cells)

    def codes(self, result):
        return {item["code"] for check in result["checks"] for item in check["findings"]}

    def test_matching_formula_sides_pass(self):
        self.assertEqual("pass", self.evaluate(self.values())["status"])

    def test_mismatched_formula_sides_fail(self):
        result = self.evaluate(self.values(right="80", check="20"))
        self.assertEqual("fail", result["status"])
        self.assertIn("recalc-values-differ", self.codes(result))

    def test_typed_zero_check_cell_over_a_mismatch_fails_twice(self):
        result = self.evaluate(self.values(right="80", check="0", check_formula=""))
        self.assertIn("recalc-check-cell-not-formula", self.codes(result))
        self.assertIn("recalc-check-cell-disagrees", self.codes(result))

    def test_difference_inside_tolerance_passes(self):
        self.assertEqual("pass", self.evaluate(self.values(right="99.5", check="0.5"), tolerance=1)["status"])

    def test_missing_cell_fails(self):
        cells = self.values()
        del cells["Model!B2"]
        self.assertIn("recalc-cell-missing", self.codes(self.evaluate(cells)))

    def test_non_numeric_value_fails(self):
        self.assertIn("recalc-value-not-numeric", self.codes(self.evaluate(self.values(left="n/a"))))

    def test_cells_on_different_sheets_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            contract = Path(tmp) / "contract.json"
            contract.write_text(json.dumps({"schema_version": "1.0.0", "checks": [
                {"id": "x", "left_cell": "A!B1", "right_cell": "B!B2", "check_cell": "A!B3", "tolerance": 0}]}),
                encoding="utf-8")
            result = MODULE.evaluate_contract(contract, self.values())
        self.assertIn("invalid-reconciliation-location", self.codes(result))

    def test_negative_tolerance_is_rejected(self):
        self.assertIn("invalid-reconciliation-tolerance", self.codes(self.evaluate(self.values(), tolerance=-1)))

    def test_compare_flags_stale_cache_and_error_cells(self):
        original = {"A!A1": {"formula": "1+1", "value": "0", "kind": "n"},
                    "A!A2": {"formula": "1/0", "value": "0", "kind": "n"},
                    "A!A3": {"formula": "2*2", "value": "4", "kind": "n"}}
        recalculated = {"A!A1": {"formula": "1+1", "value": "2", "kind": "n"},
                        "A!A2": {"formula": "1/0", "value": "#DIV/0!", "kind": "e"},
                        "A!A3": {"formula": "2*2", "value": "4", "kind": "n"}}
        result = MODULE.compare(original, recalculated)
        self.assertEqual(3, result["formula_cells"])
        self.assertEqual(2, result["stale_cache_count"])
        self.assertEqual(1, result["error_count"])


class NoEngineTests(unittest.TestCase):
    def test_missing_engine_is_not_assessed_never_a_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            workbook = Path(tmp) / "model.xlsx"
            write_workbook(workbook, [cell("B1", "10*10"), cell("B2", "50+50"), cell("B3", "B1-B2")])
            report = MODULE.audit(workbook, engine="/nonexistent/soffice")
            self.assertEqual("not-assessed", report["status"])
            result = subprocess.run([sys.executable, "-B", "-X", "utf8", str(SPEC.origin), str(workbook),
                                     "--engine", "/nonexistent/soffice"],
                                    capture_output=True, text=True, encoding="utf-8", check=False)
            self.assertEqual(2, result.returncode, result.stdout + result.stderr)
            self.assertIn("NOT_ASSESSED", result.stdout)

    def test_non_xlsx_input_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "model.xlsm"
            path.write_bytes(b"x")
            self.assertEqual("fail", MODULE.audit(path)["status"])

    def test_required_contract_missing_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            workbook = Path(tmp) / "model.xlsx"
            write_workbook(workbook, [cell("B1", "1+1")])
            report = MODULE.audit(workbook, require_contract=True)
            self.assertEqual("fail", report["status"])


@unittest.skipUnless(HAS_ENGINE, "LibreOffice is not installed: engine tests are NOT_ASSESSED")
class EngineTests(unittest.TestCase):
    """Run the real engine against workbooks whose stored values are placeholder zeros."""

    def audit(self, cells, tolerance=0, **options):
        with tempfile.TemporaryDirectory() as tmp:
            workbook = Path(tmp) / "model.xlsx"
            contract = Path(tmp) / "contract.json"
            write_workbook(workbook, cells)
            write_contract(contract, tolerance)
            before = workbook.read_bytes()
            report = MODULE.audit(workbook, contract, **options)
            self.assertEqual(before, workbook.read_bytes(), "the original workbook must not be modified")
            return report

    @staticmethod
    def codes(report):
        return {item["code"] for item in report["findings"]}

    def test_formula_sides_that_agree_pass_despite_placeholder_caches(self):
        report = self.audit([cell("B1", "10*10"), cell("B2", "50+50"), cell("B3", "B1-B2")])
        self.assertEqual("pass", report["status"], report["findings"])
        self.assertEqual("pass", report["reconciliation"]["status"])
        self.assertGreaterEqual(report["stale_cache_count"], 2)
        self.assertIn("stale-formula-cache", {item["code"] for item in report["warnings"]})
        self.assertTrue(report["engine"]["version"])

    def test_formula_sides_that_disagree_fail(self):
        report = self.audit([cell("B1", "10*10"), cell("B2", "50+30"), cell("B3", "B1-B2")])
        self.assertEqual("fail", report["status"])
        self.assertIn("recalc-values-differ", self.codes(report))

    def test_typed_check_cell_cannot_hide_a_mismatch(self):
        report = self.audit([cell("B1", "10*10"), cell("B2", "50+30"), cell("B3", None, "0")])
        self.assertEqual("fail", report["status"])
        self.assertIn("recalc-check-cell-not-formula", self.codes(report))

    def test_error_cell_after_recalculation_fails(self):
        report = self.audit([cell("B1", "10*10"), cell("B2", "100"), cell("B3", "B1-B2"), cell("C1", "1/0")])
        self.assertEqual("fail", report["status"])
        self.assertIn("error-after-recalculation", self.codes(report))

    def test_require_fresh_cache_turns_the_warning_into_a_failure(self):
        report = self.audit([cell("B1", "10*10"), cell("B2", "50+50"), cell("B3", "B1-B2")],
                            require_fresh_cache=True)
        self.assertEqual("fail", report["status"])
        self.assertIn("stale-formula-cache", self.codes(report))

    def test_retained_mismatch_workbook_from_the_october_cycle_is_caught(self):
        base = ROOT / "docs/kaizen/2026-10-engine-kaizen/labs"
        report = MODULE.audit(base / "synthetic-mismatch.xlsx", base / "synthetic-mismatch-reconciliation.json")
        self.assertEqual("fail", report["status"])
        self.assertIn("recalc-values-differ", self.codes(report))

    def test_shipped_templates_recalculate_without_error_cells(self):
        for workbook in sorted((ROOT / "skills").glob("**/templates/*.xlsx")):
            with self.subTest(workbook=workbook.name):
                report = MODULE.audit(workbook)
                self.assertEqual("pass", report["status"], report["findings"])
                self.assertEqual(0, report["error_count"])


if __name__ == "__main__":
    unittest.main()
