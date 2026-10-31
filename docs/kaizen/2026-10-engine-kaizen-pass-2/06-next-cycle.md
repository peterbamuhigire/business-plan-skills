# Next cycle (pass 2 hand-off)

Nothing here authorises external submission, client data processing or paid model calls. Items are ordered by priority; each names the acceptance evidence that closes it.

**Re-audit date:** 2026-11-30 (the Bank of Uganda policy-rate row falls due then). **Evidence owners:** finance gate owner for the workbook and rate rows, country-context maintainer for the register, routing owner for fixtures.

## Decisions needed from Peter

1. May `xlsxwriter` be installed (in a throwaway virtual environment or the repository's own, not system-wide) so the workbook generators can be re-run? Without it the shipped lender model cannot be fixed (D1 to D9).
2. Should the em dashes, arrows, section signs and box-drawing characters removed in April (1,370 lines) be restored? Em dashes may conflict with the engine's anti-slop style, so this was left alone.
3. Should the Uganda context keep a fixed UGX planning rate at all? It is now labelled a 2025 assumption to be confirmed, because the Bank of Uganda's October 2026 statement reports depreciation pressure and gives no level.

## Open findings

| Pri | Work item | Acceptance evidence | Status |
|---|---|---|---|
| P0 | Rebuild the projection workbook: balance sheet, debt schedule and DSCR, working capital from DSO, DPO and prepayment, cash tax with loss relief (accounting engine decides the treatment), D&A and share-based pay expensed or not added back, headcount-driven cost, FX path, cached values written. Fix `build_financial_projection.py` and regenerate | `formula_map.py --require-wired-inputs --require-balance-checks` returns 0 findings; `recalc_check.py --checks <contract> --require-checks --require-fresh-cache` exits 0 with tie-outs for cash to balance sheet and debt to schedule; Year 3 EBITDA equals operating income plus only items actually expensed; `04-validation-record.md` shows the dead-input count 10 to 0 and stale caches 1,772 to 0 | Open; needs decision 1 |
| P0 | Make a passing XLSX spreadsheet handoff require the recalculation report (hash-bound, engine version recorded) in `tools/release-gate/validate_release_bundle.py`; today only the literal-input contract can mark it passing | Matched, mismatched, forged-report and no-engine cases in `tests/test_release_bundle.py`; four example bundles stay blocked | Open |
| P1 | Four register rows stay stale: UBOS and KNBS (certificate chain not verifiable from the fetch tool), UNBS (HTTP 403), Bank of Uganda supervision (no body text). Find a readable issuer page for each or retrieve from a host with the issuer chains; do not renew from a search snippet | Dated page evidence per row; `refresh_evidence_register.py --check` exit 0 | Open |
| P1 | Refresh Kenya and Tanzania policy rate and exchange-rate rows (`country-context/kenya/SKILL.md:92,213`, `country-context/tanzania/SKILL.md:98-100,118`), and add a register row per rate | Primary-source page per figure with date; rows dated | Open |
| P1 | Other Uganda references still show the 2025 CBR of 9.75% as a dated figure: `skills/pipeline/02-company-overview/references/doing-business-uganda.md:384,490`, `skills/pipeline/11-funding-request/references/credit-assessment-frameworks.md:280`, `skills/pipeline/11-funding-request/references/uganda-banking-loan-framework.md:27`, `skills/pipeline/04-market-analysis/references/uganda-economic-outlook-worldbank-afdb.md:86,276`, `skills/pipeline/11-funding-request/references/uganda-banking-sector-2025.md` | Each states its date and points at register `UG-BOU-MPS-OCT-2026`; SME lending-spread arithmetic rebuilt from the current CBR | Open |
| P1 | 46 skills still share the template description ("Use when producing or reviewing the N X component of a business plan; applies its specialist evidence..."); routing between them rests on the slug | Specific, neighbour-aware descriptions; fixtures per skill; precision@1 ratchet raised from 80.0% | Open |
| P1 | Carried from 29 October: one complete synthetic plan package with narrative and model tie-outs, rendering and accessibility review | Rendered bundle, accessibility findings, release-gate record | Open |
| P2 | 75 of 137 `SKILL.md` files repeat `## Workflow`, `## Anti-Patterns` or `## Outputs`; add a ratchet so the count cannot grow, then merge the duplicates skill by skill | Count in the validator output; 75 to a lower number | Open |
| P2 | The GitHub workflow does not install LibreOffice, so engine tests are skipped or run depending on the runner image; its evidence step is red until the four rows above are renewed | A workflow step that installs or declares the engine; skipped tests recorded `NOT_ASSESSED` | Open |
| P2 | Carried: Claude plugin warnings and the Luna/high policy revisit | As recorded on 29 October | Conditional |

## Cross-engine mismatches (recorded, not edited)

| Engine | Mismatch | Files on both sides |
|---|---|---|
| Research engine | The "canonical scanner" cannot scan another engine by path: run with `--root skills` it reports six `missing_mandatory_resource` findings and reads no skill. Its degraded-mode pattern `unassessed\|not assessed\|qualified\|gap\|cannot\|unavailable\|narrowest` does not match the hyphenated state token `not-assessed` that this engine's release schema requires, nor "narrow the conclusion" | Research engine `scripts/skill_contract_validator.py:226`; this engine `skills/meta-strategy/business-plan-orchestrator/SKILL.md` (Degraded Mode) and `AGENTS.md` (Verification, "run the canonical scanner for both `skills/` and `country-context/`") |
| Accounting engine | Uganda income tax, VAT, PAYE, withholding and exchange-rate entries are `draft`; Kenya VAT and eTIMS are skeletons; Tanzania has no entries. This engine restates the rates as plain facts | Accounting `doctrine/source-register/uganda/{income-tax,vat,paye,wht,exchange-rates}.yaml`, `doctrine/source-register/kenya/{vat,etims}.yaml`, `doctrine/source-register/tanzania/README.md`; this engine `country-context/{uganda,kenya,tanzania}/SKILL.md` section 4 and `skills/pipeline/10-financial-projections/references/uganda-tax-framework.md` |
| Accounting engine (treatment review) | Loss relief, depreciation and share-based pay treatment behind the shipped P&L | This engine `skills/pipeline/10-financial-projections/templates/saas-financial-projection-3yr-5yr.xlsx` (`PnL!B16:B18`, `B20`); accounting skills `ifrs-share-based-payment-ifrs2`, `ias-income-tax-deferred-tax` |
| Portfolio | GitHub repository names for the dev, design, SDLC and research engines were renamed upstream. These links were not checked against the current names | `skills/meta-utility/skill-writing/SKILL.md:12` (`chwezi-dev-engine`), `skills/meta-strategy/kaizen-improvement-system/SKILL.md` (`digital-research-skills` currentness-gate link) |

No mismatch was found with the proposal or social-media engines in this pass beyond the corrected PPDA path (`skills/advisory-deliverables/procurement-policy-and-manual/SKILL.md:52` to `proposal-skills/skills/profiles-sectors/sectors/ppda-uganda`).

## One small experiment for next time

Rebuild only the `Cash` and `PnL` sheets of the projection generator so that DSO, DPO, tax and a debt line feed the cash flow, add a balance sheet with a `Balance sheet check` row, regenerate with cached values, and require `recalc_check.py --require-fresh-cache --checks` to pass. Measure: dead inputs on that workbook 10 to 0, stale cached cells 1,772 to 0, and the P&L-to-cash difference in Year 4 (currently 61,760 of tax) to 0. Stop if the accounting engine rejects the tax or EBITDA treatment; revert the generator commit.

## Carry-forward gates

- A check that could not run stays `NOT_ASSESSED`; a missing spreadsheet engine is exit 2, never a pass.
- Renew a source row only for the claim its page shows; URL retrieval alone renews nothing.
- Keep the text-integrity fixture and the generator-path test. Do not weaken either to make a future edit pass.
