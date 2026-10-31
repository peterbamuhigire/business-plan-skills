# Scope and evidence (pass 2)

- **Cycle:** Business Plan Skills, kaizen pass 2, October 2026 (prompt 9 of 12).
- **Continues:** the 29 October cycle in [`../2026-10-engine-kaizen/`](../2026-10-engine-kaizen/05-final-report.md). Its open items in `06-next-cycle.md` were the primary backlog input; each was re-confirmed before use.
- **Assessment date and source access date:** 2026-10-31.
- **Starting branch and HEAD:** `main` at `50d50f937e58ef2cd476c8a0c15b4b1d0305f3e9`. The earlier branch `kaizen/2026-10` (`50d50f9`) is an ancestor of `main`.
- **Working branch:** `kaizen/2026-10-pass2`, created from that HEAD. Nothing is pushed, tagged or released.
- **Working tree at start:** `git status --porcelain` printed no lines (0). No foreign uncommitted files were present, so nothing needed preserving.
- **Runtime:** Claude. The Codex-only model-pin section of `AGENTS.md` does not apply. No model-policy change is proposed, so the model-currentness comparison is `NOT_ASSESSED` for this pass and no Codex pin was touched.

This pass used the engine's own shipped templates with their default inputs, a scratch copy of the earlier mismatch workbook, and read-only git history. No client, borrower, lender or investor file was supplied. Every figure below that comes from the projection template is a template default, not an observation about a company or about Uganda. No paid model call, host configuration change, deletion of user content, canonical-doctrine edit or sibling-engine edit is part of this work.

## What was read

Router `AGENTS.md`; `business-plan-orchestrator` and its stage-gate map; `10-financial-projections` and the SaaS projection reference; `kaizen-improvement-system`; the Portfolio Kaizen Standard and currentness gate (in the research engine); the September audit and readiness review; the full 29 October evidence folder including `labs/`; `CONTRIBUTING.md`; `tools/workbook-audit/formula_map.py`; `tools/release-gate/validate_release_bundle.py`; `scripts/routing_smoke_test.py`; `docs/source-registers/`.

## Step 0.5: registered validators, run once before any change

All were run from the repository root with `PYTHONDONTWRITEBYTECODE=1` on `python3` 3.14.8. `pytest` is not installed, so the suite was run with `unittest`, which it supports.

| Command | Exit | Result |
|---|---:|---|
| `python3 -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json` | 0 | 137 active skills, 3 templates, 137 compliant, no failure counts |
| `python3 -X utf8 scripts/routing_smoke_test.py --threshold 1.0` | 0 | 61/61 top-three matches |
| `python3 -X utf8 scripts/routing_link_check.py` | 0 | 7 surfaces, 0 failures |
| `python3 -B -X utf8 tools/evidence-register/refresh_evidence_register.py --check` | 1 | 10 entries overdue (recheck dates 2026-10-13 and 2026-10-24) |
| `python3 -X utf8 tools/sector-gates/validate_sector_gates.py` | 0 | 12 sector families, 24 gates |
| `python3 -X utf8 tools/exemplar-packs/validate_exemplar_packs.py` | 0 | 4 packs, 32 artefacts |
| `tools/release-gate/validate_release_bundle.py` on each of the 4 example bundles | 0 each | structurally valid; `decision=blocked` for all four |
| `python3 -X utf8 scripts/build-financial-models/verify_workbooks.py` | 0 | 7 workbooks verified (ZIP and sheet names only) |
| `python3 -X utf8 scripts/check_package_file_budget.py` | 0 | 1,343 full-checkout entries, 1,142 package-oriented entries, cap 5,000 |
| `python3 -B -X utf8 -m unittest discover -s tests -p "test_*.py"` | 0 | 80 tests, OK |
| `python3 -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py skills/meta-strategy/business-plan-orchestrator` | 0 | Skill is valid |
| Research-engine `scripts/skill_contract_validator.py --root skills` (the "canonical scanner") | 1 | `NOT_ASSESSED` as a conformance result: it requires research-engine mandatory resources under `--root` (six `missing_mandatory_resource` findings, 0 active skills read), so it cannot scan this repository by path |
| `soffice --version` | 0 | LibreOffice 26.2.6.3 is installed, so workbook recalculation is assessable this pass |

The 29 October note that the suite needed an "externally prepared environment" no longer applies on this machine: `unittest` runs all 80 tests directly.

## Step 1: Observe (three practitioner tasks)

### Task 1: bankable plan and three-year model for an early-stage Ugandan SaaS company seeking a bank loan

**Request.** "Produce a bankable plan and three-year model for an early-stage Ugandan SaaS company seeking a bank loan, and run the release gate."

**Route chosen and whether it was right.** `AGENTS.md` sends a serious full-plan request to `business-plan-orchestrator`, which stops at `00-client-intake` when the decision, audience and facts are missing. No company facts exist, so the correct outcome is the intake stop, with the model built only as a labelled scratch exercise. For the model the router leads to `10-financial-projections`, which names `references/saas-financial-projection-template-3yr-5yr.md` and the workbook `templates/saas-financial-projection-3yr-5yr.xlsx` as the canonical SaaS model ("mandatory" in the reference). Routing was correct. The finance, country (`country-context/uganda`) and release-gate overlays were also correctly named.

**What was run.** The shipped workbook, unmodified, was recalculated headlessly with LibreOffice 26.2.6.3 in a scratch directory (always-recalculate profile, original untouched) and read cell by cell. The release gate was run on the closest packaged case, `examples/full-plan-packages/dfi-loan-uganda`: structurally valid, `decision=blocked`.

**What the template produced with its default inputs** (USD; template defaults, not evidence): revenue Year 1 183,224, Year 2 831,618, Year 3 2,160,891; operating income Year 1 (142,722), Year 2 (189,739), Year 3 (10,715); minimum monthly ending cash about 1.875 million in month 24.

**Defects found** (workbook cell references stand in for line numbers):

| ID | Severity | Defect | Location |
|---|---|---|---|
| D1 | Critical for a lender case | No balance sheet and no debt schedule exist. The reference requires a "Balance Sheet" tab (`references/saas-financial-projection-template-3yr-5yr.md`, tab list item 7 and section 8) and skill 10 requires a balance sheet and DSCR. The workbook has 11 sheets and none is a balance sheet, no row computes debt service or DSCR, and `Cash` has no debt, interest or tax line. | `Cash!A4:A13`; `Bankability-Dashboard!A4:A20` |
| D2 | Critical | Adjusted EBITDA adds back depreciation and stock-based compensation that were never deducted. `PnL!B14` = gross profit minus S&M, R&D and G&A; none of those lines includes D&A or share-based pay; `PnL!B18` = `B14+B16+B17`. Year 3 operating income is (10,715) but Year 3 "Adjusted EBITDA" is +102,300, flipping the sign. The dashboard's Year 3 EBITDA margin and Rule of 40 read from this. | `PnL!B14:F18`; `Bankability-Dashboard!B7`, `B17` |
| D3 | Major | Ten input cells on `Inputs` drive nothing (checked by an independent reference scan including ranges and defined names): price escalator `B17`, opex inflation `B59`, DSO `B78`, DPO `B79`, annual prepayment uptake `B80` and discount `B81`, debt drawdown `B91`, debt interest `B92`, FX rate `B99` and FX depreciation `B100`. A user who sets a loan, a collection period or an FX path sees no effect. The FX gap means the workbook labelled `Reporting currency UGX` (`Inputs!B98`) is USD throughout. | `Inputs!B17`, `B59`, `B78:B81`, `B91:B92`, `B99:B100` |
| D4 | Major | The 11-person headcount plan costs USD 623,000 loaded in Year 1 (`Inputs!D75`), but total P&L operating expense is USD 279,224 (`PnL!B13`). No formula outside the `Headcount` sheet references it; opex is driven by revenue percentages. | `Headcount!B15`; `PnL!B10:B13` |
| D5 | Major | "Operating cash flow" equals pre-tax operating income, so cash ignores the tax the P&L charges (Year 4 tax 61,760; Year 5 159,700) and any working-capital timing. The monthly cash sheet and the annual P&L do not reconcile to net income. | `Cash!A8`; `PnL!B20:F21` |
| D6 | Major | Tax is `MAX(0, operating income) x rate` each year: no loss carry-forward and no interest deduction. Year 4 tax is charged on a profit that follows about 343,000 of cumulative earlier losses. Accounting treatment belongs to the accounting engine. | `PnL!B20:F20` |
| D7 | Major | Cached formula values are placeholders: 1,852 of 1,852 formula cells in this workbook cache `0`. Across all seven shipped workbooks, 4,046 of 4,385 formula cells (92%) hold a cached value that differs from the recalculated value. `fullCalcOnLoad="1"` makes Excel and LibreOffice recompute on open, but any reader that trusts caches sees zeros, and `formula_map.py` reads caches only. | `labs/baseline-workbook-cache-census.txt` |
| D8 | Minor | Rates are hard-coded inside formulas: non-recurring revenue `B4*0.05*(1=1)+B4*0.03*(1=2)`, stock-based compensation `B6*0.05`, and year indices typed as `IF(1=1,...)` in every column. | `PnL!B5`, `B17` |
| D9 | Minor | The Dashboard's S&M and CAC are independent: S&M is a share of revenue (`PnL!B10`) while `LTV:CAC` uses a typed CAC (`Inputs!B96`). Magic Number (Year 2) reads 8.4 and "Burn multiple" 0.16 on defaults; the burn multiple divides by adjusted EBITDA (`PnL!C18`) rather than net cash burn. | `Bankability-Dashboard!B18:B19` |
| D10 | Major (guidance) | `formula_map.py --require-balance-checks` passes this workbook (20 hits) although it has no balance sheet: the pattern `BALANCE_RE` matches the words "Opening ARR", "Ending ARR" and "running balance" in prose labels. | `tools/workbook-audit/formula_map.py:23` (`BALANCE_RE`), `:269` |

**Missing, contradictory or ignored guidance.** Contradictory: the reference calls the workbook "mandatory" and lists a balance sheet and debt flows that it does not contain; `AGENTS.md` requires DSCR of at least 1.25 times for lender work while the dashboard has no DSCR. Missing: no statement of what the shipped workbook does and does not model. The reference also prescribes `UGX 3,700` as an example FX figure (`references/saas-financial-projection-template-3yr-5yr.md`) while the workbook carries 3,800; neither is sourced.

### Task 2: investor version of the same plan, narrative and model reconciliation

**Route chosen.** Same baseline flow plus `meta-valuation` (equity audience, `end-to-end-stage-gates.md` audience table), then `meta-investment-committee-red-team` only after a complete pack exists. Correct: no pack exists, so the committee stage stays unreachable.

**Reconciliation test run.** The dashboard figures an investor narrative would quote (Year 3 revenue 2.16 million, Year 3 ending ARR 3.03 million, LTV:CAC 5.16, Rule of 40 1.37, Year 3 EBITDA margin 4.7%) were traced to their formulas. They reconcile arithmetically to the model (for example `Bankability-Dashboard!B15` = `(ARPA_P*GM_P/Logo_Churn_P)/CAC_P`), so a narrative copied from the dashboard would "tie" to the model. It would tie to a model with the defects D2 and D9: Year 3 EBITDA margin is positive only because of the D2 add-back, and an investor narrative built on it would claim operating profitability that the operating-income line does not support. This is the specific failure the orchestrator's decision table warns about ("polished but internally impossible plans"), and no shipped check detects it because the check is arithmetic, not semantic. Valuation, cap table, terms and traction evidence were not supplied, so no investor conclusion is supportable.

### Task 3: model whose cash flow does not tie to the balance sheet

**Re-run of the retained 29 October mismatch.** `python3 -X utf8 tools/workbook-audit/formula_map.py docs/kaizen/2026-10-engine-kaizen/labs/synthetic-mismatch.xlsx --require-reconciliation --reconciliation-checks .../synthetic-mismatch-reconciliation.json --require-scenarios --require-balance-checks`: exit 1, findings `reconciliation-values-differ` and `reconciliation-cache-missing`. The literal-input case still fails closed.

**Harder variant, the realistic one.** In a real three-statement model both sides of the tie are formulas. The 29 October contract rejects formula sources (`reconciliation-source-not-literal`, `tools/workbook-audit/formula_map.py:144`), so a formula-driven model can fail but can never pass, and `validate_release_bundle.py` requires that contract for a passing XLSX handoff (`tools/release-gate/validate_release_bundle.py:63`). Practically, a genuine three-statement model has no route to a passing spreadsheet handoff. Without a recalculation engine the gate cannot tell a correct model from a wrong one; with one, it can. LibreOffice is installed here, so this pass tests that route (see the backlog).

## Step 5 preview: country-context and source register defects found while observing

| ID | Severity | Defect | Location |
|---|---|---|---|
| D11 | Critical (content integrity) | Commit `e1a9aa1` (13 April 2026, "Make the skills dual boot") removed every non-ASCII character from 47 files (2,719 characters). Numeric ranges collapsed into other numbers: Uganda headline inflation "3-5%" became "35%", the policy rate "9.75-10.5%" became "9.7510.5%", wages "UGX 2,000,000-6,000,000" became "2,000,0006,000,000", "3-5 principles" became "35 principles", "2-50 shareholders" became "250 shareholders". 1,636 damaged lines still stand in HEAD, 170 of them numeric-range lines, across skills and the three country contexts. Neither the skill validator nor the 29 October byte test sees this. | `country-context/uganda/SKILL.md:95`, `:179`, `:208`; `skills/pipeline/02-company-overview/SKILL.md:184`, `:198`; full census in `labs/baseline-text-damage-census.txt` |
| D12 | Major | The human-readable register table still shows `verified-current` for the ten rows the JSON marks `stale`. | `docs/source-registers/country-market-data.md` table rows 1 to 10 vs `country-market-data.json` |
| D13 | Major | Router and notes contain Windows host paths: eight lines in `AGENTS.md` (for example `AGENTS.md:368` and `:430`), one in `.gitignore:4`, one in `templates/README-financial-models.md:214`. On this machine they resolve nowhere. | as listed |
| D14 | Major | `country-context/uganda/SKILL.md:81` labels `UGX 3,550 per USD (Q1 2025/26)` as "current"; `:179` gives the policy rate as a 2025 range of 9.75-10.5% while the Bank of Uganda raised it to 12.0% on 14 October 2026 (see source evidence in `04-validation-record.md`). | as listed |
| D15 | Minor | `skills/advisory-deliverables/procurement-policy-and-manual/SKILL.md:52` points to `proposal-skills/sectors/ppda-uganda`, a path that does not exist in the sibling checkout (the skill is `proposal-skills/skills/profiles-sectors/sectors/ppda-uganda`). | as listed |
| D17 | Minor | The generator for the projection workbook, `scripts/build-financial-models/build_financial_projection.py`, writes to `skills/10-financial-projections/templates/` (`OUT` path, line 22), a folder that no longer exists since the skills moved under `skills/pipeline/`. It depends on `xlsxwriter` (not installed here) and, like all six generators, writes formulas without cached values, which is the root cause of D7. The README tells users to regenerate with `cd C:/wamp64/www/business-plan-skills` (`templates/README-financial-models.md:214`). | as listed |
| D16 | Minor | 75 of 137 `SKILL.md` files carry duplicate `## Workflow`, `## Anti-Patterns` or `## Outputs` headings (a migration leftover). Deferred; see the backlog. | census command in `01-baseline-scorecard.md` |

The scanner finding from September stands as a cross-engine item. The research engine's contract validator checks the degraded-mode section with the pattern `unassessed|not assessed|qualified|gap|cannot|unavailable|narrowest` (`skill_contract_validator.py:226` in the research engine). The orchestrator's section says "Mark the affected stage or handoff `not-assessed`" and "narrow the conclusion". The hyphenated state token that this engine's release schema requires and the verb form "narrow" are not matched, so the finding is a false negative of the scanner. Per the brief it is recorded for the research engine's cycle and no boilerplate was added here.
