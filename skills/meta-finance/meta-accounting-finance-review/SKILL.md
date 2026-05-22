---
name: meta-accounting-finance-review
description: Review business plans, financial projections, funding requests, investor decks, and proposals through accounting, IFRS-aware, management-accounting, financial-model, and controls discipline. Use before bankability scoring, stress testing, valuation, due diligence, or final assembly to make numbers realistic and internally consistent.
---

# Accounting Finance Review Meta-Skill

## Use When

- A business plan contains financial projections, funding requests, valuation, investor terms, budgets, cost structures, or management controls.
- The plan involves POS, ERP, bookkeeping, inventory, payroll, tax, mobile money, school fees, healthcare billing, grants, manufacturing, logistics, subscriptions, or project accounting.
- The user wants the financial logic to withstand accountants, lenders, investors, CEOs, partners, or due-diligence reviewers.

## Do Not Use When

- The business model is still too vague to build assumptions.
- The task is only copyediting and does not involve numbers, controls, or financial decisions.

## Required Inputs

- Draft plan sections, financial projections, assumptions, funding request, tax/country context, and industry guide where available.
- Historical financials, bank/mobile money statements, inventory records, payroll, tax records, contracts, or reconstructed records where available.

## Workflow

1. Reconcile the business model to financial statements: revenue, COGS, operating expenses, capex, working capital, tax, debt, equity, and cash.
2. Review accounting basis: cash/accrual, local GAAP/IFRS/IFRS for SMEs, revenue timing, inventory costing, depreciation, leases, provisions, taxes, and reporting cadence.
3. Review management accounting: cost behavior, contribution margin, break-even, cost centers, profit centers, budgets, standard costs, variance analysis, and responsibility reporting.
4. Audit the model: driver logic, formula checks, balance sheet integrity, cash roll-forward, debt schedule, tax schedule, working capital, and no hidden balancing figures.
5. Stress the assumptions qualitatively before numerical stress testing: capacity, market demand, pricing power, collection days, supplier terms, input inflation, FX, staffing, and control maturity.
6. Produce a fix list ranked by funding impact: fatal contradictions, lender/investor trust issues, projection weaknesses, control gaps, and appendix evidence gaps.

## Quality Bar

- Numbers reconcile across narrative, assumptions, statements, funding request, ratios, and appendices.
- Projections are bottom-up, operationally feasible, and not dependent on unexplained hockey-stick growth.
- Cash flow is distinct from profit, with working-capital timing made explicit.
- The plan shows how the business will keep reliable books after launch.

## Outputs

- Accounting and financial quality review.
- Reconciled issue list with severity and section references.
- Assumption corrections and model-control recommendations.
- Handoff notes for `meta-financial-stress-test`, `meta-bankability-scoring`, `meta-valuation`, and `meta-due-diligence`.

## References

- `references/accounting-finance-quality-gate.md` - detailed review checks for projections, IFRS-aware accounting, management accounting, controls, and investor/lender readiness.
- `../10-financial-projections/SKILL.md` - core financial statement and assumption structure.
- `../meta-financial-stress-test/SKILL.md` - numerical downside testing after accounting review.
- `../meta-bankability-scoring/SKILL.md` - fundability scoring after numbers reconcile.
