"""Structural scan: dead inputs and label-only balance evidence must be reported."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("formula_map_wiring", ROOT / "tools/workbook-audit/formula_map.py")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
PROJECTION = ROOT / "skills/pipeline/10-financial-projections/templates/saas-financial-projection-3yr-5yr.xlsx"
# Inputs in the shipped projection workbook that drive nothing (verified 2026-10-31).
# When the generator wires them, delete the matching entry; the test must then fail loudly.
KNOWN_DEAD_PROJECTION_INPUTS = {
    "Inputs!B17", "Inputs!B59", "Inputs!B78", "Inputs!B79", "Inputs!B80",
    "Inputs!B81", "Inputs!B91", "Inputs!B92", "Inputs!B99", "Inputs!B100",
}


def num(ref: str, value: str) -> str:
    return f'<c r="{ref}"><v>{value}</v></c>'


def text(ref: str, value: str) -> str:
    return f'<c r="{ref}" t="inlineStr"><is><t>{value}</t></is></c>'


def formula(ref: str, expression: str, value: str = "0") -> str:
    return f'<c r="{ref}"><f>{expression}</f><v>{value}</v></c>'


def write(path: Path, sheets: dict[str, dict[int, list[str]]], names: dict[str, str] | None = None) -> None:
    listing = "".join(f'<sheet name="{name}" sheetId="{i}" r:id="rId{i}"/>' for i, name in enumerate(sheets, 1))
    defined = "".join(f'<definedName name="{n}">{t}</definedName>' for n, t in (names or {}).items())
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("xl/workbook.xml", f'<?xml version="1.0"?><workbook xmlns="{NS}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>{listing}</sheets><definedNames>{defined}</definedNames></workbook>')
        rels = "".join(f'<Relationship Id="rId{i}" Target="worksheets/sheet{i}.xml"/>' for i in range(1, len(sheets) + 1))
        zf.writestr("xl/_rels/workbook.xml.rels", f'<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{rels}</Relationships>')
        for i, (name, rows) in enumerate(sheets.items(), 1):
            body = "".join(f'<row r="{r}">{"".join(cells)}</row>' for r, cells in sorted(rows.items()))
            zf.writestr(f"xl/worksheets/sheet{i}.xml", f'<?xml version="1.0"?><worksheet xmlns="{NS}"><sheetData>{body}</sheetData></worksheet>')


class WiredInputTests(unittest.TestCase):
    def audit(self, sheets, names=None, **options):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "model.xlsx"
            write(path, sheets, names)
            return MODULE.audit_workbook(path, **options)

    @staticmethod
    def locations(report):
        return {item["location"] for item in report["unreferenced_inputs"]}

    def test_dead_input_is_reported_and_fails_when_required(self):
        sheets = {"Inputs": {1: [text("A1", "Rate"), num("B1", "5")], 2: [text("A2", "Loan"), num("B2", "7")]},
                  "Model": {1: [formula("A1", "Inputs!B1*2")]}}
        report = self.audit(sheets)
        self.assertEqual({"Inputs!B2"}, self.locations(report))
        self.assertEqual("pass", report["status"])
        required = self.audit(sheets, require_wired_inputs=True)
        self.assertEqual("fail", required["status"])
        self.assertIn("unreferenced-input", {f["code"] for f in required["findings"]})

    def test_defined_name_and_range_references_count_as_use(self):
        sheets = {"Inputs": {1: [num("B1", "5")], 2: [num("B2", "7")], 3: [num("B3", "9")]},
                  "Model": {1: [formula("A1", "Rate*2"), formula("B1", "SUM(Inputs!B3:B4)")]}}
        report = self.audit(sheets, names={"Rate": "Inputs!$B$2"})
        self.assertEqual({"Inputs!B1"}, self.locations(report))

    def test_same_sheet_and_quoted_sheet_references_count_as_use(self):
        sheets = {"Key Inputs": {1: [num("B1", "5"), formula("C1", "B1+1")], 2: [num("B2", "7")]},
                  "Model": {1: [formula("A1", "'Key Inputs'!B2*2")]}}
        self.assertEqual(set(), self.locations(self.audit(sheets)))

    def test_text_labels_and_function_names_are_not_mistaken_for_cells(self):
        sheets = {"Inputs": {1: [text("A1", "LOG10 label"), num("B1", "5")]},
                  "Model": {1: [formula("A1", 'LOG10(Inputs!B1)+LEN("B9")')]}}
        self.assertEqual(set(), self.locations(self.audit(sheets)))

    def test_projection_template_reports_exactly_the_known_dead_inputs(self):
        report = MODULE.audit_workbook(PROJECTION)
        self.assertEqual(KNOWN_DEAD_PROJECTION_INPUTS, self.locations(report))
        self.assertEqual(104, report["numeric_input_count"])


class BalanceEvidenceTests(unittest.TestCase):
    def audit(self, sheets):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "model.xlsx"
            write(path, sheets)
            return MODULE.audit_workbook(path, require_balance_checks=True)

    def test_labels_alone_do_not_satisfy_the_balance_requirement(self):
        report = self.audit({"Model": {1: [text("A1", "Opening balance"), num("B1", "10")],
                                       2: [text("A2", "Ending balance"), num("B2", "12")],
                                       3: [text("A3", "Revenue"), formula("B3", "B1+B2")]}})
        self.assertEqual("fail", report["status"])
        self.assertIn("missing-balance-checks", {f["code"] for f in report["findings"]})
        self.assertGreater(report["balance_check_count"], 0)
        self.assertEqual(0, report["balance_formula_check_count"])

    def test_a_formula_on_a_check_row_satisfies_it(self):
        report = self.audit({"Model": {1: [text("A1", "Cash"), num("B1", "10")],
                                       2: [text("A2", "Balance sheet check"), formula("B2", "B1-10")]}})
        self.assertEqual("pass", report["status"], report["findings"])
        self.assertEqual(1, report["balance_formula_check_count"])


if __name__ == "__main__":
    unittest.main()
