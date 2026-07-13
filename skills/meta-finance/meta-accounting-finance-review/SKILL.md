---
name: meta-accounting-finance-review
description: Use when a business plan contains financial projections, funding requests, valuation, investor terms, budgets, cost structures, or management controls. Use financial projections for model construction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Accounting Finance Review Meta-Skill

## Anti-Patterns

- Treating a generic accounting finance review template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.
- Presenting assumptions as verified facts. **Correction:** label assumptions and assign an evidence action.
- Hiding a failed or unavailable check. **Correction:** record it as failed or `not assessed` with its consequence.
- Crossing the permission boundary during analysis. **Correction:** keep review read-only and obtain explicit authority before mutation or publication.
- Producing an artefact with no consumer or acceptance test. **Correction:** name who will use it and what observable condition makes it usable.


## Use When

- A business plan contains financial projections, funding requests, valuation, investor terms, budgets, cost structures, or management controls.
- The plan involves POS, ERP, bookkeeping, inventory, payroll, tax, mobile money, school fees, healthcare billing, grants, manufacturing, logistics, subscriptions, or project accounting.
- The user wants the financial logic to withstand accountants, lenders, investors, CEOs, partners, or due-diligence reviewers.

## Do Not Use When

- The business model is still too vague to build assumptions.
- The task is only copyediting and does not involve numbers, controls, or financial decisions.


- Route to `10-financial-projections` instead when the task is to construct the underlying model.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Accounting Finance Review brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
| Current accounting, tax, valuation, or pricing basis | Finance owner, accounting records, signed contracts, and current authoritative sources | Conditional | Mark the treatment unresolved and require qualified professional review. |
- Draft plan sections, financial projections, assumptions, funding request, tax/country context, and industry guide where available.
- Historical financials, bank/mobile money statements, inventory records, payroll, tax records, contracts, or reconstructed records where available.

## Workflow

1. Reconcile the business model to financial statements: revenue, COGS, operating expenses, capex, working capital, tax, debt, equity, and cash.
2. Review accounting basis: cash/accrual, local GAAP/IFRS/IFRS for SMEs, revenue timing, inventory costing, depreciation, leases, provisions, taxes, and reporting cadence.
3. Review management accounting: cost behavior, contribution margin, break-even, cost centers, profit centers, budgets, standard costs, variance analysis, and responsibility reporting.
4. Audit the model: driver logic, formula checks, balance sheet integrity, cash roll-forward, debt schedule, tax schedule, working capital, and no hidden balancing figures.
5. Stress the assumptions qualitatively before numerical stress testing: capacity, market demand, pricing power, collection days, supplier terms, input inflation, FX, staffing, and control maturity.
6. Produce a fix list ranked by funding impact: fatal contradictions, lender/investor trust issues, projection weaknesses, control gaps, and appendix evidence gaps.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the reconciled finance review and that the decision concerns whether the plan's numbers are fit for funding review.
- **Stop condition:** halt the affected conclusion if required evidence is missing (ledger basis and integrated model) or if the work could lead to this identified risk: a balanced-looking model with broken cash, tax, or working-capital logic.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Numbers reconcile across narrative, assumptions, statements, funding request, ratios, and appendices.
- Projections are bottom-up, operationally feasible, and not dependent on unexplained hockey-stick growth.
- Cash flow is distinct from profit, with working-capital timing made explicit.
- The plan shows how the business will keep reliable books after launch.

## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Accounting Finance Review deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Accounting and financial quality review.
- Reconciled issue list with severity and section references.
- Assumption corrections and model-control recommendations.
- Handoff notes for `meta-financial-stress-test`, `meta-bankability-scoring`, `meta-valuation`, and `meta-due-diligence`.

## References

- `references/accounting-finance-quality-gate.md` - detailed review checks for projections, IFRS-aware accounting, management accounting, controls, and investor/lender readiness.
- `../10-financial-projections/SKILL.md` - core financial statement and assumption structure.
- `../meta-financial-stress-test/SKILL.md` - numerical downside testing after accounting review.
- `../meta-bankability-scoring/SKILL.md` - fundability scoring after numbers reconcile.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Reconciled finance review decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to a balanced-looking model with broken cash, tax, or working-capital logic. |

## Capability and Permission Boundaries


Default to read-only inspection while producing the reconciled finance review. Read supplied records and run non-mutating checks; annotating the supplied review copy is permitted only when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If ledger basis and integrated model cannot be obtained, return a qualified reconciled finance review covering only the checks that remain supportable. Leave this decision unresolved: whether the plan's numbers are fit for funding review. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: whether the plan's numbers are fit for funding review | Record the conclusion, source trail, owner, and review trigger in the reconciled finance review. | Risk of a balanced-looking model with broken cash, tax, or working-capital logic |
| Material evidence conflicts or remains uncertain | Trace the disputed balance through the statements and cash roll-forward, then ask the model owner to resolve the break. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: ledger basis and integrated model | Mark the decision on whether the plan's numbers are fit for funding review `not assessed` in the reconciled finance review, and send it to the finance owner and external accountant. | Otherwise, the work risks a balanced-looking model with broken cash, tax, or working-capital logic |

## Quality Standards


Accept the reconciled finance review only when evidence is sufficient for this decision: whether the plan's numbers are fit for funding review. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of a balanced-looking model with broken cash, tax, or working-capital logic.

## Worked Example


A retail plan shows profit while cash turns negative because inventory days double. The review traces the working-capital gap, corrects the cash roll-forward, and blocks the funding conclusion until stock assumptions and statements reconcile.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the reconciled finance review, using the reporting basis and effective date supported by ledger basis and integrated model. Reconcile the treatment to the model and narrative, and have the controller or external accountant review the treatment, reconciliation, and exposure to this risk: a balanced-looking model with broken cash, tax, or working-capital logic.

<!-- dual-compat-end -->
