# Final report (pass 2)

Cycle: Business Plan Skills, kaizen pass 2, 31 October 2026. It continues [the 29 October cycle](../2026-10-engine-kaizen/05-final-report.md). Scope and observations: [`00-scope-and-evidence.md`](00-scope-and-evidence.md). Frozen baseline: [`01-baseline-scorecard.md`](01-baseline-scorecard.md). Backlog and Five Whys: [`02-improvement-backlog.md`](02-improvement-backlog.md). Experiments: [`03-experiment-log.md`](03-experiment-log.md). Validators and currency: [`04-validation-record.md`](04-validation-record.md). Open work: [`06-next-cycle.md`](06-next-cycle.md).

- **Branches.** Started on `main` at `50d50f937e58ef2cd476c8a0c15b4b1d0305f3e9` with a clean tree. Work is on `kaizen/2026-10-pass2` (16 commits ahead of `main` with this report). Nothing was pushed, tagged or released. The checkout was returned to `main` after the last commit.
- **Foreign files.** None were present.

## Scores

Scores are practitioner judgements (inference), not validator pass rates. The fresh baseline is lower than the 29 October final on five dimensions because it measured things that cycle left `NOT_ASSESSED`; it is a wider measurement, not a regression, since no engine content changed between the two dates.

| Dimension | 29 Oct final | Fresh baseline | Final | Basis for the final score |
|---|---:|---:|---:|---|
| Doctrine | 50 | 50 | 55 | The reference and the workbook no longer contradict each other (a scope table states what the workbook lacks); the router no longer names nonexistent host paths. No new principle |
| Taxonomy and routing | 55 | 50 | 55 | Precision@1 78.7% to 80.0%; 5 skills with full fixture coverage (was 0); silent skipping of unreadable skills fixed. 46 of 137 skills still share a template description |
| Skill depth | 50 | 50 | 50 | Two skills gained a decision row, an anti-pattern or a specific description; 75 skills still carry duplicate headings |
| Applied proof | 40 | 40 | 50 | A formula-driven tie-out can now be proved or failed on recalculated values, with 7 engine tests and a built-to-fail three-statement fixture. The shipped model is still defective and no real model was reviewed |
| Standards currency | 35 | 30 | 40 | Six rows renewed at claim level, one primary-source row added, register table now generated and checked, Uganda rows dated. Four rows still stale; tax rates unverified; Kenya and Tanzania rates not refreshed |
| Output readiness | 60 | 55 | 55 | Unchanged: the template cannot produce a lender model and no complete plan was rendered. Honest scope statements prevent mis-selling it |
| Accessibility and inclusion | 25 | 25 | 25 | Not worked on |
| Production and handoff | 55 | 50 | 55 | A recalculation route exists and is named in the orchestrator, delivery contract and router; generator output paths fixed. It is not yet part of the release gate |
| Hygiene | 60 | 40 | 60 | 256 numeric lines restored and guarded; host paths out of Markdown; register table synced; generator paths fixed. 1,370 stripped em-dash and symbol lines and 75 duplicate-heading files remain |
| Safety and integrity | 55 | 50 | 55 | Wrong numbers in country context removed and guarded; recalculation catches mismatches. The shipped model's D1 and D2 defects are documented, not fixed, so they remain a blocker for lender use |

| Measure | 29 Oct final | Fresh baseline | Final |
|---|---:|---:|---:|
| Raw arithmetic mean | 49.0 | 44.0 | 50.0 |
| Published, `min(raw, 65)` | 49.0 | 44.0 | 50.0 |

Arithmetic for the final: `(55 + 55 + 50 + 50 + 40 + 55 + 25 + 55 + 60 + 55) / 10 = 50.0`. The 95/100 target is not achieved. No measure is worse than its frozen baseline (table in `04-validation-record.md`). The final score is 1.0 above the 29 October figure and 6.0 above the fresh baseline.

## Kept changes (all committed, none reverted after commit)

| ID | Change | Evidence | Commit |
|---|---|---|---|
| B1 | Restored numeric operators stripped by commit `e1a9aa1` on 256 lines in 33 files; added `scripts/check_text_integrity.py` with 298 known-line hashes | Uganda inflation "35%" read 3-5% again; pre-fix tree gives 296 findings, fixed tree 0; script idempotent | `e762dbc`, `423214c` |
| B2 | `tools/workbook-audit/recalc_check.py`: recalculation in LibreOffice, stale-cache and error-cell reporting, formula-sourced tie-outs | Mismatched three-statement fixture fails, matched passes, the 29 October check cannot separate them; 19 tests, 7 on the real engine | `1350d4a` |
| B3 | `formula_map.py`: unwired-input report and flag, balance evidence must be on a formula row | Reports exactly the 10 dead inputs found by hand; prose labels no longer satisfy `--require-balance-checks` | `9c044f2` |
| B4 | Six of ten overdue rows renewed with narrowed claim families, four left stale, Bank of Uganda October 2026 row added, Markdown table generated from JSON and checked | Overdue 10 to 4; table drift 10 rows to a failing check; per-row evidence in `04-validation-record.md` | `d4f9943` |
| B5 | Host paths removed from router, skill pointer, template README and gitignore; 7 generator output paths corrected; host-path signature and static generator test | Pre-fix tree fails the generator test for all 7; Markdown host-path lines 10 to 0 | `5fc69b9` |
| B6 | Uganda macro rows dated; CBR 12.0% from 14 October 2026 with source; planning rate labelled a 2025 assumption | Primary-source PDF read; see the currency table | `c392a40` |
| B7 | Two specific descriptions, 19 fixtures, `--report` and `--min-precision-at-1`, silent-skip fix, CI ratchet at 80.0% | Top-three 80/80; precision@1 80.0%; coverage 0 to 5 skills | `c7d956a`, `33617d4`, `015c68b` |
| B8 | Scope table of what the shipped workbook does not model, lender-case procedure, decision row, anti-pattern, recalculation routing | 116 tests and validators pass | `01997bd` |
| B9 | Corrected sibling path to the PPDA profile | Path exists in the sibling checkout | `02395c1` |
| B10 | Dated callouts that restated tax rates are unverified against the accounting register | Register lookups in `04-validation-record.md` | `24bd64b` |

The evidence commits are `0d1eb51` (frozen baseline) and `00afcec` (backlog); the final evidence commit carries this report.

## Reverted

Nothing was reverted after commit. Three attempts at the `00-plan-assembly` description were tried before the kept one; the first regressed an existing fixture and the second made the skill unreadable and exposed the silent-skip defect (details in `03-experiment-log.md`).

## Critical defects

| Defect | Status |
|---|---|
| D11 numeric ranges collapsed into other numbers | Fixed and verified for numeric operators; guarded. Residual stripped em dashes and symbols (1,370 lines) are stylistic and need Peter's decision |
| D1 no balance sheet, no loan, no DSCR in the shipped lender model | Escalated. Mitigated by the scope table and a decision row; rebuilding needs the generator's dependency (`xlsxwriter`, not installed and not installable here) and an accounting review |
| D2 Adjusted EBITDA adds back items never expensed | Escalated for the same reason; the reference now says to quote operating income instead |
| D7 stored values in all shipped workbooks are placeholders | Detected and reported by the new tool; fixing the stored values needs the same rebuild |

## Residual risk

- A plan built on the shipped projection workbook can still present a positive Year 3 EBITDA over a negative operating income. The guidance now warns against it, but no gate blocks it.
- The recalculation report is not yet required by the release gate, so a bundle can still be marked passing on the literal-input contract alone.
- Four register rows are stale and CI's evidence step still exits 1; this is honest, not a regression.
- No complete plan, rendered output, accessibility review or independent human review was produced. Scores are judgement.
