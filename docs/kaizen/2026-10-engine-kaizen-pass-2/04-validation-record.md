# Validation record (pass 2)

Validation date: 2026-10-31, after the last committed change (`015c68b`). Commands ran from the repository root on `python3` 3.14.8 with `PYTHONDONTWRITEBYTECODE=1`. `pytest` is not installed, so the suite ran with `unittest`, which it supports. No package was installed, no host configuration was changed and no paid model call was made. LibreOffice 26.2.6.3 was run headless with a throwaway profile in a temporary directory; originals were never opened in place.

## Registered validators and gates

| Command | Exit | Result |
|---|---:|---|
| `python3 -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json` | 0 | 137 active skills, 3 templates, 137 compliant, no failure counts; now also runs the text-integrity check and the package file budget |
| `python3 -X utf8 scripts/routing_smoke_test.py --threshold 1.0 --report --min-precision-at-1 0.80` | 0 | 80/80 top-three; precision@1 64/80 (80.0%); 46 of 137 skills with a fixture; 5 skills with 3 positives and 2 owned negatives |
| `python3 -X utf8 scripts/routing_link_check.py` | 0 | 7 surfaces, 0 failures |
| `python3 -B -X utf8 tools/evidence-register/refresh_evidence_register.py --check` | **1** | 4 of 24 rows overdue: `UG-UBOS-STATISTICAL-PUBLICATIONS`, `KE-KNBS-STATISTICAL-ABSTRACT`, `UG-UNBS-STANDARDS`, `UG-BOU-SUPERVISION`. Deliberately not a pass: the issuer pages could not be read (see below). The Markdown table agrees with the JSON |
| `python3 -X utf8 tools/sector-gates/validate_sector_gates.py` | 0 | 12 sector families, 24 gates (structure only) |
| `python3 -X utf8 tools/exemplar-packs/validate_exemplar_packs.py` | 0 | 4 packs, 32 artefacts |
| `python3 -X utf8 tools/release-gate/validate_release_bundle.py examples/full-plan-packages/<pack>/release-bundle.json` for `dfi-loan-uganda`, `grant-east-africa`, `owner-manager-uganda`, `vc-east-africa` | 0 each | structurally valid; `decision=blocked` for all four (not a release) |
| `python3 -X utf8 scripts/build-financial-models/verify_workbooks.py` | 0 | 7 workbooks verified (ZIP and sheet names only) |
| `python3 -X utf8 scripts/check_package_file_budget.py` | 0 | 1,590 checkout entries, 1,163 package-oriented entries, cap 5,000 (not a built archive) |
| `python3 -B -X utf8 scripts/check_text_integrity.py` | 0 | no control characters, glued numeric ranges, host paths or known stripped lines |
| `python3 -B -X utf8 -m unittest discover -s tests -p "test_*.py"` | 0 | 130 tests, OK (80 at baseline; 50 added) |
| `python3 -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py <dir>` on every skill directory changed since the baseline | 0 | 35 directories, 0 failures |
| `python3 -m compileall -q scripts tools skills/meta-utility/skill-writing/scripts` | 0 | compiles |
| `git diff --check 0d1eb51 HEAD` | 0 | no whitespace errors |
| `docs/kaizen/2026-10-engine-kaizen-pass-2/labs/restore_stripped_operators.py --commit e1a9aa1` (dry run) | 0 | 0 whole-line and 0 single-operator restorations left (idempotent) |

## New checks and what each was shown to catch

| Check | Negative control (built to fail) | Result |
|---|---|---|
| `scripts/check_text_integrity.py` | The pre-fix tree extracted from commit `0d1eb51` into a scratch directory | 296 findings, exit 1; fixed tree passes |
| `tools/workbook-audit/recalc_check.py` | `labs/three-statement-mismatch.xlsx` (assets 100 against equity and liabilities 75, both sides formulas); the retained 29 October literal mismatch | Both fail with `recalc-values-differ`; `labs/three-statement-matched.xlsx` passes; typed-zero check cell over a mismatch fails; an error cell fails; a nonexistent engine gives exit 2 `NOT_ASSESSED` |
| `formula_map.py --require-wired-inputs` | Projection template | 10 findings, the same 10 inputs found by an independent hand scan |
| `formula_map.py --require-balance-checks` | A workbook with only "Opening balance" and "Ending balance" labels | Fails (`missing-balance-checks`); a formula on a "Balance sheet check" row passes |
| Register Markdown check | A table with one `stale` changed to `verified-current` | Fails with "table differs"; missing markers fail |
| `tests/test_generator_paths.py` | The pre-fix tree | Fails for all 7 generators; fixed tree passes |
| `routing_smoke_test.py` | A skill with unparseable frontmatter | Fails and names the file (before: silently skipped) |

Tests that need a spreadsheet engine are guarded with `skipUnless` on the engine being installed. In this run none was skipped (7 engine tests ran). On a host without LibreOffice they would be skipped and must be recorded `NOT_ASSESSED`, not as passes; the GitHub workflow has not been changed to install an engine (see `06-next-cycle.md`).

## NOT_ASSESSED

| Item | Reason |
|---|---|
| Research-engine `scripts/skill_contract_validator.py` as a conformance scan of this repository | It requires research-engine mandatory resources under `--root`; run against `skills/` it reports 6 `missing_mandatory_resource` findings and reads 0 skills. It also mis-reads the orchestrator's degraded-mode wording (pattern at its line 226); recorded for the research engine |
| Model currentness | Claude runtime; no model-policy change proposed; no official release or catalogue comparison performed this pass |
| UBOS, KNBS, UNBS and Bank of Uganda supervision pages | Retrieval failed (certificate chain not verifiable for UBOS and KNBS; HTTP 403 for UNBS; no body text for the Bank of Uganda page). Rows remain `stale` |
| Kenya and Tanzania policy rates and exchange rates | Not re-fetched; their rows carry 2024 and 2025 dates and are unchanged. The 29 October snapshot (Kenya CBR 8.75%, Tanzania CBR 6.25%) was not re-verified |
| Tax rates for Uganda, Kenya and Tanzania | Accounting register entries are draft (see below); no rate is verified |
| Tier 3 behavioural runs, live-agent routing, independent semantic review of skills, rendered plan, accessibility review, real lender or investor model | Out of scope or not permitted; no paid model call |
| Public marketplace acceptance, account-level availability | Not touched |
| A Linux CI run of the GitHub workflow | Not run; no push |
| Full census of backticked cross-engine skill names | Only path-form references were resolved |

## Step 5: currency record

Gate read: the research engine's `kaizen-currentness-gate.md` and Portfolio Kaizen Standard. Source-evaluation and source-verification disciplines applied by recording scope, access date, support state and review date per row. Page content was treated as data. The reviewer in every record below is this pass-2 agent run on behalf of Peter Bamuhigire; there was no human reviewer.

| Source (issuer URL) | Access date | What the page showed | Support state | Review date |
|---|---|---|---|---|
| Bank of Uganda, Monetary Policy Statement for October 2026 (`bou.or.ug/uploads/MPS_October_2026_cdc1de720f.pdf`) | 2026-10-31 | Special meeting 14 October 2026 raised the Central Bank Rate by 225 basis points from 9.75% to 12.0%; headline inflation 4.6% (September 2026), core 3.7%; headline inflation projected at 7.0-7.5% over 12 months; depreciation pressure on the shilling; no exchange-rate level on the pages read | Verified for the stated figures (first two PDF pages read) | 2026-11-30 (register `UG-BOU-MPS-OCT-2026`) |
| National Bureau of Statistics Tanzania, Statistical Abstract Reports | 2026-10-31 | Abstracts 2025 (dated 20 September 2026) back to 2016; titles and dates only | Verified with caveat: topics not shown | 2027-01-29 |
| Uganda Revenue Authority, Domestic Taxes FAQs | 2026-10-31 | TIN and agent registration, provisional and final return dates, payment registration; customs only in passing; no page date; a waiver deadline of 31 December 2024 still shown | Verified with caveat; claim families narrowed; no rate used | 2027-01-29 |
| Uganda Registration Services Bureau, Business Registration | 2026-10-31 | Company and legal-document registration, legal identity as a benefit, online system; no annual returns | Verified with caveat; annual filings dropped | 2027-01-29 |
| National Environment Management Authority, Regulations | 2026-10-31 | Environmental and Social Assessment Regulations S.I. 143 of 2020, Waste Management S.I. 49 of 2020, Air Quality Standards S.I. 22 of 2024, effluent discharge 2020 and others; no page date | Verified with caveat; amendment status not checked | 2027-01-29 |
| Uganda Communications Commission, Telecommunication Licensing | 2026-10-31 | Sections 5(1)(b) and 22 of the Uganda Communications Act 2013; licence PDFs; list of licensed telecoms at 31 January 2026; spectrum, postal, broadcasting only as menu items | Verified with caveat; claim families narrowed | 2027-01-29 |
| World Bank, World Development Indicators home page | 2026-10-31 | Loaded; no last-updated date; DataBank source page returned an error | Verified with caveat; URL changed with the reason recorded in the row | 2027-01-29 |
| UBOS, KNBS | 2026-10-31 | "unable to verify the first certificate" | NOT_ASSESSED; row stays stale | not renewed |
| UNBS | 2026-10-31 | HTTP 403 | NOT_ASSESSED; row stays stale | not renewed |
| Bank of Uganda supervision page | 2026-10-31 | Heading and help-desk link, no body | NOT_ASSESSED; row stays stale | not renewed |

Tax rates were not restated. Read-only effective-date lookups against the accounting engine's register (`tools/source_register_lookup.py --jurisdiction <code> --register <name> --date 2026-10-31 --as-of 2026-10-31`, run from that checkout, nothing written):

| Lookup | Exit | State |
|---|---:|---|
| UG `vat` | 3 | `UG-VAT-STANDARD-RATE` draft, final use refused, effective date NOT_ASSESSED, recheck overdue |
| UG `paye` | 3 | `UG-PAYE-RATES` draft, final use refused |
| UG `income-tax` | 3 | `UG-INCOME-TAX-RULES` draft, final use refused |
| UG `wht` | 3 | `UG-WHT-RATES` draft, final use refused |
| UG `exchange-rates` | 3 | `UG-EXCHANGE-RATE-SOURCE-HIERARCHY` draft, final use refused |
| UG `nssf` | 0 | `UG-NSSF-MEMBERSHIP-CONTRIBUTIONS` verified-current, effective 2026-05-15 |
| KE `vat`, KE `etims` | 3 | skeleton entries, draft, final use refused |
| TZ `vat` | 2 | unknown jurisdiction (the register knows IF, KE, UG) |

## Measures: frozen baseline against now

| Measure | Frozen baseline (`50d50f9`) | Now |
|---|---|---|
| Skill contract | 137/137 compliant | 137/137 compliant |
| Routing, top three | 61/61 | 80/80 |
| Routing precision@1 | 48/61 (78.7%) | 64/80 (80.0%) |
| Skills with 3 positives and 2 owned negatives | 0 | 5 |
| Skills with 2 or more owned negatives | 0 | 5 |
| Lines with a lost numeric operator | 1,636 stripped lines in HEAD, 170 numeric-range lines | 0 operator lines (guard in the validator); 1,370 lines still carry a stripped em dash, arrow, section sign or box-drawing character |
| Host-specific paths in engine Markdown | 10 lines in 3 files (12 in 5 files including non-Markdown) | 0 in Markdown; 1 comment and the new check's own pattern in two Python files, which are deliberate |
| Broken relative links | 0 of 584 (586 including two quoted counter-examples) | 0 of 584 |
| Overdue register rows | 10 of 23 | 4 of 24 |
| Register table disagrees with JSON | 10 rows | 0, and a failing check |
| Formula cells whose stored value differs from a recalculation | 4,046 of 4,385 (92%) in the 7 shipped workbooks | unchanged (workbooks not rebuilt); now reported by `recalc_check.py` as a warning, an error with `--require-fresh-cache` |
| Error cells after recalculation | 0 | 0 |
| Dead inputs in the projection workbook | 10 of 104, unreported | 10 of 104, now reported and testable with `--require-wired-inputs` |
| Duplicate H2 headings in `SKILL.md` | 75 of 137 | 75 of 137 (deferred) |
| Generators writing to a shipped file | 0 of 7 | 7 of 7 |
| Unit tests | 80 | 130 |
