#!/usr/bin/env python3
"""Inspect XLSX formula structure using only the Python standard library."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import math
import re
import sys
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
      "p": "http://schemas.openxmlformats.org/package/2006/relationships"}
ERROR_VALUES = {"#NULL!", "#DIV/0!", "#VALUE!", "#REF!", "#NAME?", "#NUM!", "#N/A"}
SCENARIO_RE = re.compile(r"\b(base|bull|bear|downside|upside|stress|scenario)\b", re.I)
BALANCE_RE = re.compile(r"balance|tie[- ]?out|reconcil|opening|closing|ending|dscr|check", re.I)
SHEET_REF_RE = re.compile(r"(?<![A-Za-z0-9_.])(?:'([^']+)'|([A-Za-z_][A-Za-z0-9_. ]*))!")


@dataclass
class Finding:
    severity: str
    code: str
    location: str
    message: str


def _xml(zf: zipfile.ZipFile, name: str) -> ET.Element:
    return ET.fromstring(zf.read(name))


def _shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = _xml(zf, "xl/sharedStrings.xml")
    return ["".join(t.text or "" for t in si.findall(".//m:t", NS))
            for si in root.findall("m:si", NS)]


def _cell_text(cell: ET.Element, shared: list[str]) -> str:
    value = cell.findtext("m:v", default="", namespaces=NS)
    if cell.get("t") == "s" and value.isdigit() and int(value) < len(shared):
        return shared[int(value)]
    inline = cell.find("m:is", NS)
    if inline is not None:
        return "".join(t.text or "" for t in inline.findall(".//m:t", NS))
    return value


CELL_REF_RE = re.compile(r"^\$?([A-Z]{1,3})\$?(\d+)$", re.I)


def _parse_location(value: object) -> tuple[str, str] | None:
    if not isinstance(value, str) or value.count("!") != 1:
        return None
    sheet, cell = value.rsplit("!", 1)
    if not sheet or not CELL_REF_RE.fullmatch(cell):
        return None
    return sheet, cell.replace("$", "").upper()


def _number(value: object) -> float | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = float(value)
    except ValueError:
        return None
    return parsed if math.isfinite(parsed) else None


def _reconcile_checks(checks_path: str | Path | None, cell_values: dict[str, dict],
                      formulas: list[dict], required: bool) -> dict:
    result = {"status": "not-assessed", "checks": [], "findings": [],
              "contract_sha256": None}
    if checks_path is None:
        if required:
            result["status"] = "fail"
            result["findings"].append({"code": "missing-reconciliation-contract",
                                       "message": "A reconciliation-checks JSON file is required"})
        return result

    contract_path = Path(checks_path)
    try:
        contract_bytes = contract_path.read_bytes()
        contract = json.loads(contract_bytes.decode("utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        result["status"] = "fail"
        result["findings"].append({"code": "invalid-reconciliation-contract",
                                   "message": str(exc)})
        return result
    result["contract_sha256"] = hashlib.sha256(contract_bytes).hexdigest()
    if not isinstance(contract, dict) or contract.get("schema_version") != "1.0.0" or not isinstance(contract.get("checks"), list) or not contract["checks"]:
        result["status"] = "fail"
        result["findings"].append({"code": "invalid-reconciliation-contract",
                                   "message": "Expected schema_version 1.0.0 and a non-empty checks list"})
        return result

    formula_by_location = {item["location"]: item for item in formulas}
    seen_ids: set[str] = set()
    for item in contract["checks"]:
        check_result = {"id": "", "status": "fail", "findings": []}
        result["checks"].append(check_result)
        if not isinstance(item, dict):
            check_result["findings"].append({"code": "invalid-reconciliation-check",
                                             "message": "Each check must be an object"})
            continue
        check_id = item.get("id")
        check_result["id"] = check_id if isinstance(check_id, str) else ""
        if not isinstance(check_id, str) or not check_id.strip() or check_id in seen_ids:
            check_result["findings"].append({"code": "invalid-reconciliation-check-id",
                                             "message": "Check IDs must be unique non-empty strings"})
            continue
        seen_ids.add(check_id)
        left_loc, right_loc, check_loc = (item.get("left_cell"), item.get("right_cell"), item.get("check_cell"))
        parsed = [_parse_location(v) for v in (left_loc, right_loc, check_loc)]
        if any(v is None for v in parsed) or len({v[0] for v in parsed if v}) != 1:
            check_result["findings"].append({"code": "invalid-reconciliation-location",
                                             "message": "All cells must be valid references on the same worksheet"})
            continue
        tolerance = item.get("tolerance")
        try:
            tolerance_value = float(tolerance)
        except (TypeError, ValueError, OverflowError):
            tolerance_value = math.nan
        if isinstance(tolerance, bool) or not isinstance(tolerance, (int, float)) or not math.isfinite(tolerance_value) or tolerance_value < 0:
            check_result["findings"].append({"code": "invalid-reconciliation-tolerance",
                                             "message": "Tolerance must be a finite non-negative number"})
            continue
        left, right, check_cell = (cell_values.get(left_loc), cell_values.get(right_loc),
                                   cell_values.get(check_loc))
        if left is None or right is None or check_cell is None:
            check_result["findings"].append({"code": "reconciliation-cell-missing",
                                             "message": "One or more declared reconciliation cells are missing"})
            continue
        if left["formula"] or right["formula"]:
            check_result["findings"].append({"code": "reconciliation-source-not-literal",
                                             "message": "Source cells must be literal numeric inputs; formula-source recalculation is not assessed"})
            continue
        left_value, right_value = _number(left["value"]), _number(right["value"])
        if left_value is None or right_value is None:
            check_result["findings"].append({"code": "reconciliation-source-not-numeric",
                                             "message": "Both source cells must contain finite numeric values"})
            continue
        formula_item = formula_by_location.get(check_loc)
        expected_formula = f"{parsed[0][1]}-{parsed[1][1]}"
        actual_formula = formula_item["formula"].replace("$", "").replace(" ", "").upper() if formula_item else ""
        if actual_formula != expected_formula.upper():
            check_result["findings"].append({"code": "reconciliation-formula-mismatch",
                                             "message": f"Check formula must be {expected_formula}; found {actual_formula or 'no formula'}"})
            continue
        expected_difference = left_value - right_value
        if not math.isfinite(expected_difference):
            check_result["findings"].append({"code": "reconciliation-difference-not-finite",
                                             "message": "The independently calculated difference is not finite"})
            continue
        check_result.update({"left_cell": left_loc, "right_cell": right_loc,
                             "check_cell": check_loc, "left_value": left_value,
                             "right_value": right_value,
                             "expected_difference": expected_difference,
                             "tolerance": tolerance_value})
        if abs(expected_difference) > tolerance_value:
            check_result["findings"].append({"code": "reconciliation-values-differ",
                                             "message": f"Declared values differ by {expected_difference}; tolerance is {tolerance_value}"})
        cached_value = _number(check_cell["value"])
        if cached_value is None:
            check_result["findings"].append({"code": "reconciliation-cache-missing",
                                             "message": "The check formula must have a finite numeric cached result"})
            continue
        check_result["cached_check_value"] = cached_value
        if abs(cached_value - expected_difference) > tolerance_value:
            check_result["findings"].append({"code": "reconciliation-cache-does-not-match-inputs",
                                             "message": f"Cached check result {cached_value} differs from independently calculated {expected_difference}"})
        check_result["status"] = "pass" if not check_result["findings"] else "fail"

    all_pass = bool(result["checks"]) and all(item["status"] == "pass" for item in result["checks"])
    result["status"] = "pass" if all_pass and not result["findings"] else "fail"
    return result


def audit_workbook(path: str | Path, require_scenarios: bool = False,
                   require_balance_checks: bool = False,
                   reconciliation_checks: str | Path | None = None,
                   require_reconciliation: bool = False) -> dict:
    workbook = Path(path)
    findings: list[Finding] = []
    formulas: list[dict] = []
    assumptions: list[dict] = []
    scenario_hits: list[dict] = []
    balance_hits: list[dict] = []
    external_links: list[dict] = []
    cell_values: dict[str, dict] = {}
    workbook_bytes = workbook.read_bytes()
    workbook_hash = hashlib.sha256(workbook_bytes).hexdigest()

    with zipfile.ZipFile(io.BytesIO(workbook_bytes)) as zf:
        shared = _shared_strings(zf)
        wb = _xml(zf, "xl/workbook.xml")
        rels = _xml(zf, "xl/_rels/workbook.xml.rels")
        targets = {r.get("Id"): r.get("Target") for r in rels.findall("p:Relationship", NS)}
        sheets: list[tuple[str, str]] = []
        for sheet in wb.findall("m:sheets/m:sheet", NS):
            target = targets.get(sheet.get(f"{{{NS['r']}}}id"), "")
            if target.startswith("/"):
                part = target.lstrip("/")
            else:
                part = str(Path("xl") / target).replace("\\", "/")
            sheets.append((sheet.get("name", ""), part))
        sheet_names = {name for name, _ in sheets}

        defined_names = []
        for node in wb.findall("m:definedNames/m:definedName", NS):
            item = {"name": node.get("name", ""), "formula": node.text or ""}
            defined_names.append(item)
            combined = f"{item['name']} {item['formula']}"
            if SCENARIO_RE.search(combined):
                scenario_hits.append({"location": "defined-name", "value": combined})
            if BALANCE_RE.search(combined):
                balance_hits.append({"location": "defined-name", "value": combined})

        for sheet_name, part in sheets:
            if part not in zf.namelist():
                findings.append(Finding("error", "missing-sheet-part", sheet_name, part))
                continue
            root = _xml(zf, part)
            assumption_sheet = bool(re.search(r"input|assumption", sheet_name, re.I))
            if SCENARIO_RE.search(sheet_name):
                scenario_hits.append({"location": sheet_name, "value": "sheet-name"})
            if BALANCE_RE.search(sheet_name):
                balance_hits.append({"location": sheet_name, "value": "sheet-name"})
            for cell in root.findall(".//m:c", NS):
                ref = cell.get("r", "?")
                location = f"{sheet_name}!{ref}"
                formula = cell.findtext("m:f", default="", namespaces=NS)
                value = _cell_text(cell, shared)
                cell_values[location] = {"formula": formula, "value": value}
                if assumption_sheet and not formula and value:
                    assumptions.append({"location": location, "value": value})
                combined = f"{formula} {value}"
                if SCENARIO_RE.search(combined):
                    scenario_hits.append({"location": location, "value": combined[:160]})
                if BALANCE_RE.search(combined):
                    balance_hits.append({"location": location, "value": combined[:160]})
                if not formula:
                    continue
                formulas.append({"location": location, "formula": formula, "cached_value": value})
                if "#REF!" in formula:
                    findings.append(Finding("error", "broken-reference", location, formula))
                if value in ERROR_VALUES:
                    findings.append(Finding("error", "cached-formula-error", location, value))
                if re.search(r"\[[^\]]+\]", formula):
                    external_links.append({"location": location, "formula": formula})
                    findings.append(Finding("error", "external-workbook-link", location, formula))
                for match in SHEET_REF_RE.finditer(formula):
                    referenced = (match.group(1) or match.group(2) or "").strip()
                    if referenced and referenced not in sheet_names:
                        findings.append(Finding("error", "missing-sheet-reference", location, referenced))

    if require_scenarios and not scenario_hits:
        findings.append(Finding("error", "missing-scenario-checks", str(workbook),
                                "No base, downside, stress, or scenario evidence found"))
    if require_balance_checks and not balance_hits:
        findings.append(Finding("error", "missing-balance-checks", str(workbook),
                                "No balance, reconciliation, tie-out, or check evidence found"))
    reconciliation = _reconcile_checks(reconciliation_checks, cell_values, formulas,
                                       require_reconciliation)
    for item in reconciliation["findings"]:
        findings.append(Finding("error", item["code"], "workbook-reconciliation", item["message"]))
    for check in reconciliation["checks"]:
        for item in check.get("findings", []):
            findings.append(Finding("error", item["code"], check.get("id", ""), item["message"]))
    failures = [asdict(f) for f in findings if f.severity == "error"]
    return {
        "workbook": workbook.as_posix(),
        "workbook_sha256": workbook_hash,
        "status": "pass" if not failures else "fail",
        "sheet_count": len(sheets),
        "formula_count": len(formulas),
        "assumption_cell_count": len(assumptions),
        "scenario_check_count": len(scenario_hits),
        "balance_check_count": len(balance_hits),
        "external_link_count": len(external_links),
        "formulas": formulas,
        "assumptions": assumptions,
        "scenario_checks": scenario_hits,
        "balance_checks": balance_hits,
        "external_links": external_links,
        "reconciliation": reconciliation,
        "findings": [asdict(f) for f in findings],
    }


def markdown_report(report: dict) -> str:
    lines = [f"# Formula map: {Path(report['workbook']).name}", "",
             f"- Status: **{report['status'].upper()}**",
             f"- Sheets: {report['sheet_count']}", f"- Formulae: {report['formula_count']}",
             f"- Assumption cells: {report['assumption_cell_count']}",
             f"- Scenario checks: {report['scenario_check_count']}",
             f"- Balance/reconciliation checks: {report['balance_check_count']}",
             f"- External links: {report['external_link_count']}", "", "## Findings", ""]
    if report["findings"]:
        lines += [f"- `{f['severity']}` `{f['code']}` at `{f['location']}`: {f['message']}"
                  for f in report["findings"]]
    else:
        lines.append("No structural formula findings.")
    lines += ["", "## Formulae", "", "| Cell | Formula | Cached value |", "| --- | --- | --- |"]
    for item in report["formulas"]:
        formula = item["formula"].replace("|", "\\|")
        lines.append(f"| `{item['location']}` | `{formula}` | `{item['cached_value']}` |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbooks", nargs="+", type=Path)
    parser.add_argument("--require-scenarios", action="store_true")
    parser.add_argument("--require-balance-checks", action="store_true")
    parser.add_argument("--reconciliation-checks", type=Path,
                        help="JSON contract for a literal-input difference check")
    parser.add_argument("--require-reconciliation", action="store_true",
                        help="Fail unless numeric reconciliation checks pass")
    parser.add_argument("--json-out", "--output", dest="json_out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    args = parser.parse_args(argv)
    reports = []
    for workbook in args.workbooks:
        try:
            reports.append(audit_workbook(workbook, args.require_scenarios,
                                          args.require_balance_checks,
                                          args.reconciliation_checks,
                                          args.require_reconciliation))
        except (OSError, zipfile.BadZipFile, ET.ParseError) as exc:
            reports.append({"workbook": workbook.as_posix(), "status": "fail", "findings": [
                asdict(Finding("error", "unreadable-workbook", str(workbook), str(exc)))
            ]})
    payload = reports[0] if len(reports) == 1 else {"workbooks": reports}
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.markdown_out:
        if len(reports) != 1:
            parser.error("--markdown-out requires exactly one workbook")
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(markdown_report(reports[0]), encoding="utf-8")
    for report in reports:
        print(f"{report['status'].upper()}: {report['workbook']} "
              f"({len(report.get('findings', []))} findings)")
    return 1 if any(r["status"] != "pass" for r in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
