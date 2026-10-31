# Improvement backlog and Five Whys (pass 2)

Assessment date: 2026-10-31. Root causes are inferences from repository history, code and the command results in [`00-scope-and-evidence.md`](00-scope-and-evidence.md). Owners are roles. The 95/100 target is a plan figure only; the published score stays capped at 65.

## Five Whys for the critical and repeated defects

### D11 (critical): numeric ranges collapsed into other numbers

1. **Why does Uganda's context say inflation is 35%?** The source line was "3-5%" with an en dash and the dash is gone.
2. **Why is the dash gone?** Commit `e1a9aa1` (13 April 2026, "Make the skills dual boot") removed every non-ASCII character from 47 files (2,719 characters); `git show` of the line before and after proves it.
3. **Why did a bulk rewrite delete characters instead of failing?** The migration pass re-encoded text through a path that silently drops what it cannot represent. The diff was reviewed as a structural migration, not for character loss.
4. **Why did no gate catch it, then or since?** Every validator checks structure (headings, frontmatter, links). The 29 October fix checked control bytes in one file. Nothing compares text content to its history or looks for glued numbers.
5. **Why was it not noticed by readers?** "35%" and "9.7510.5%" are grammatical text. Only a reader who already knows the right value sees the fault, which is exactly the lender or investor who then loses trust.

**Root cause (inference):** process and tooling. A mass text rewrite had no loss-detection step, and the validators have no content-integrity check.

### D7 and Task 3 (critical for any lender case): formula-driven models cannot be proven

1. **Why can a three-statement model not pass the spreadsheet handoff?** The 29 October contract accepts only literal numeric source cells.
2. **Why only literals?** The check reads cached values from the XLSX XML and has no calculation engine, so a formula source has no trustworthy value.
3. **Why are cached values untrustworthy?** All six generators write formulas without a value, so the file stores `0` (4,046 of 4,385 formula cells differ from a recalculation).
4. **Why was no engine used?** The 29 October environment had none; this machine has LibreOffice, so the limit was environmental and never recorded as a capability to look for.
5. **Why does the router not ask for recalculation?** `AGENTS.md` says to run `formula_map.py`, which is documented as structural; no skill or gate names a recalculation step.

**Root cause (inference):** tooling and process. The proof strategy was built around what could be done in the standard library alone, and the gap was recorded but not given a route.

### D1 to D6 (critical and major): the shipped lender model does not model a lender case

1. **Why can the template not model a loan?** `Cash` has no debt line and `Inputs!B91:B92` feed nothing.
2. **Why are inputs unwired?** The generator was written against a spec that lists debt, working capital and a balance sheet, but only some tabs were implemented (`build_financial_projection.py` builds ARR, P&L and a cash sheet).
3. **Why did the gap survive?** `verify_workbooks.py` checks sheet names only and `formula_map.py` checks formula text; neither asks whether an input is used or whether the spec's tabs exist.
4. **Why does EBITDA exceed operating income?** The P&L adds back D&A and stock-based pay that its opex lines never expensed, so the add-back double counts.
5. **Why was that not seen?** No check compares a subtotal's components, and the template was accepted on structure.

**Root cause (inference):** proof and reference. The reference promises more than the workbook delivers and no check compares them.

## Prioritised backlog

Selected for this cycle: 9 items (maximum ten). Each lists gap, root cause, exact change, hypothesis, owner and due date, acceptance evidence, risk and rollback, and target contribution.

| ID | Pri | Gap and evidence | Root cause | Exact change | Hypothesis | Owner / due | Acceptance evidence | Risk and rollback | Target contribution |
|---|---|---|---|---|---|---|---|---|---|
| B1 | P0 | D11: 1,636 damaged lines, 170 numeric ranges, 47 files | Process and tooling | Restore numeric-operator characters (en dash, minus, multiplication, comparison, plus-minus, division, root, degree, euro) on every line proven to be an exact strip of a pre-damage line; leave em dashes, arrows, section signs, box drawing and emoji as they are. Add a text-integrity check to `scripts/validate_skill_engine.py` | Restoring operators removes the wrong-number risk without touching style | Content maintainer, 2026-10-31 | Before and after count of damaged numeric lines; `git diff --stat`; new check fails on a reintroduced glued range and passes on HEAD | Reversible by `git revert` of one commit; risk of restoring a stale fact is accepted because the facts keep their original date labels | Hygiene +15, Safety +5 |
| B2 | P0 | D7 and Task 3: stale caches; formula-driven models cannot pass | Tooling and process | Add `tools/workbook-audit/recalc_check.py`: recalculate a copy with LibreOffice in an isolated profile, report error cells and stale caches, and evaluate declared tie-outs on recalculated values; exit 2 `NOT_ASSESSED` when no engine exists | A recalculating check closes the false-negative class for formula-sourced tie-outs | Finance gate owner, 2026-10-31 | Tests: matching formula tie-out passes, mismatching fails, stale-cache workbook flagged, no-engine case returns `NOT_ASSESSED`; run on the 7 shipped workbooks | New file and tests only; remove to roll back. Risk: engine version drift, so the report records the version | Applied proof +10, Production +5, Safety +5 |
| B3 | P1 | D3 and D10: 10 dead inputs; balance evidence satisfied by prose | Tooling | In `formula_map.py`: report `unreferenced_inputs` (input-sheet literals no formula, range or defined name uses) and add `--require-wired-inputs`; require balance evidence on a formula-bearing row rather than any prose hit | A used-input test and a formula-row test close two structural false negatives | Finance gate owner, 2026-10-31 | Tests with a dead-input fixture and a prose-only fixture; the projection template reports exactly the 10 known dead inputs | Flags are opt-in (the default exit codes of existing calls do not change) | Applied proof +5 |
| B4 | P0 (carry) | Ten overdue country-register rows; D12 table drift | Process | Claim-level review of each row against the official issuer page; renew only what the page supports; regenerate the Markdown table from the JSON and add a check that they agree | A table generated from, and checked against, the JSON cannot contradict it | Country-context and finance gate owners, 2026-10-31 | Per-row source URL, access date, what was seen; `--check` result; new test | Rows the page cannot support stay `stale` or `NOT_ASSESSED`; revert the JSON edit | Currency +15 |
| B5 | P1 | D13: Windows host paths in the router and notes | Hygiene | Replace host paths with "resolve through the engine-routing table"; add a machine-path check to the validator for router, skills, templates, references and country context | A check prevents the paths returning | Router owner, 2026-10-31 | `git grep` count before and after; check fails on a planted `C:\` path | Wording only; revert to restore | Hygiene +5 |
| B6 | P1 | D14: a 2025 rate labelled "current" and a superseded policy range | Currency | Relabel the exchange-rate row as a dated snapshot, correct the policy-rate row to a dated, sourced statement that points to the Bank of Uganda; no new planning rule invented | A dated label cannot be mistaken for a live rate | Country-context owner, 2026-10-31 | Diff plus source record in `04-validation-record.md` | Wording only | Currency +5 |
| B7 | P1 | Routing precision@1 78.7%; 0 skills with 3 positives and 2 owned negatives | Proof | Add `--report` to `routing_smoke_test.py` (precision@1, coverage, owned negatives) and add fixtures for every skill touched this cycle | A measured denominator lets the ratchet move | Routing owner, 2026-10-31 | Report output before and after; fixtures pass | Fixtures are data; revert to restore | Routing +5 |
| B8 | P1 | D1 to D6, D8 to D9: reference promises more than the workbook models | Reference | Add "What the shipped workbook does and does not model" to the SaaS projection reference and an anti-pattern plus decision row to skill 10; route recalculation evidence from the orchestrator and delivery contract. Defer rebuilding the workbook (needs `xlsxwriter` and accounting review) to the next cycle | Honest scope statements stop the template being presented as lender-ready | Finance model owner, 2026-10-31 | Skill validators pass; text cites the exact defects | Docs only | Doctrine +5, Output +5 |
| B9 | P2 | D15: wrong sibling path | Reference | Correct the path to the proposal engine's PPDA profile | Correct pointer | Advisory owner, 2026-10-31 | Resolves against the sibling checkout | One line | Hygiene +1 |

## Deferred (moved to `06-next-cycle.md`)

- Rebuild the projection workbook with a balance sheet, debt schedule, DSCR, wired inputs, cash tax and recalculated caches (needs the generator dependency and an accounting review). Reason: structural and needs permission to install a package.
- Wire the recalculation report into `validate_release_bundle.py`. Reason: release-gate schema change; needs one cycle of use first.
- Duplicate H2 headings in 75 skills, em-dash, arrow and section-sign restoration, full skill-behaviour census. Reason: structural or stylistic and larger than one cycle.
