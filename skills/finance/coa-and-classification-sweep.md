# Business-Plan Classification Sweep

Canonical IFRS-for-SMEs-aligned classification for the line items that appear in business-plan financial projections. Use this file as the single source of truth when writing or reviewing a Chwezi business plan.

## Why this exists

Business-plan financial projections frequently mix classifications across templates (cost of sales in operating expenses; depreciation in COGS sometimes and overhead other times; tax in interest; deferred revenue in revenue). This sweep file fixes the canonical position so every business plan we ship lines up with how the system will actually report.

## Revenue (SOCI: Revenue)

Items belonging here:

- Sale of goods.
- Rendering of services.
- Subscription fees.
- Membership / access fees recognised under the relevant pattern.
- Royalties and licence fees.
- Other operating revenue tied to the principal activity.

**Not here:** customer deposits (these are liabilities until performance), grant income (Section 24), interest income (finance income), gain on disposal (other income).

## Cost of sales / Cost of services (SOCI: Cost of sales)

- Direct materials.
- Direct labour.
- Variable production overhead.
- Production / service depreciation directly assignable.
- Inventory write-downs to NRV (Section 13).
- Carriage inwards.
- Direct subcontract.

**Not here:** marketing, distribution, central admin, finance costs, depreciation of admin assets.

## Other operating income

- Government grant income recognised under Section 24.
- Sundry rental income (when not the principal activity).
- Insurance recoveries.

## Distribution costs

- Sales commissions.
- Outbound freight.
- Marketing and advertising.
- Customer service costs.

## Administrative expenses

- Salaries and benefits of admin / management.
- Office rent (admin portion).
- Office utilities, internet, communications.
- Office supplies.
- Professional fees (legal, accounting, audit).
- Insurance (admin).
- Bank charges and commissions.
- Depreciation of admin assets.
- Allowance for doubtful debts movement.

## Other operating expenses

- Loss on disposal of assets.
- Impairment losses other than goodwill in some presentations.

## Finance income (SOCI: Finance income)

- Interest income.
- Other returns on basic financial assets (Section 11).

## Finance costs (SOCI: Finance costs)

- Interest expense.
- Unwinding of discount on provisions (Section 21).
- Bank loan arrangement fees amortised through effective interest.
- Borrowing costs — **expensed** under IFRS for SMEs (Section 25). Not capitalised.

## Income tax expense

- Current income tax.
- Deferred tax movement (Section 29).

**Not here:** payroll-related taxes (those are operating costs / liabilities, not income tax expense).

## Working capital

- Trade receivables (current asset).
- Inventories (current asset).
- Trade payables (current liability).
- Prepayments and accruals.

## Inventory

- FIFO or weighted average. **LIFO is not permitted under IFRS or IFRS for SMEs.** Any business plan that references LIFO is non-compliant and must be revised.
- Inventory valuation includes cost of purchase, conversion costs, and other costs incurred to bring the inventory to its present location and condition.
- Write-downs to net realisable value where applicable.

## Cash flow

Choose direct OR indirect method per entity policy and apply consistently across periods. Standard categories:

- Operating activities.
- Investing activities (including PPE additions, asset disposals, acquisitions).
- Financing activities (borrowings drawdown / repayment, equity issuance, dividends paid).

Free cash flow = Operating cash flow − Capital expenditure (PPE additions).

## Depreciation and amortisation

- Depreciation of operating / production assets → Cost of sales or operating expenses by function.
- Depreciation of admin assets → Administrative expenses.
- Amortisation of intangibles → in the same function as the related activity.
- Internally generated intangibles (other than capitalised development costs under full IFRS — not permitted under IFRS for SMEs) → expensed.

## Tax in projections

- VAT, PAYE, WHT, NSSF are **not** P&L items; they are cash-flow and balance-sheet items. Show them as receipts and payments in cash-flow.
- Income tax expense **is** a P&L item; show it separately under income tax expense.
- Statutory contributions paid by employer → operating expense (salaries / benefits).

## Forbidden in Chwezi business plans

- LIFO appearing as an IFRS / IFRS-for-SMEs option.
- US-GAAP-only language (extraordinary items as a line; FAS-13-style lease classifications without explicit US-GAAP overlay).
- Hardcoded statutory rates without source-register reference (planning defaults must be flagged "verify before final output").
- Stale FX rates without an effective date and source.
- "Always use rate X" language without a verification trigger.
- Cash-basis revenue presented as IFRS-aligned without a stated accrual reconciliation.

## Cleanup queue (existing industry guides to align)

The following existing business-plan-skills industry guides should be reviewed against this sweep:

- `skills/industry-guides/restaurant/references/cost-controls-advanced.md` — contains LIFO references; reclassify under the doctrine cleanup backlog.
- All other industry-guides — sweep for COGS vs operating-expense placement, depreciation classification, finance costs vs interest, tax handling.

(Cleanup is governed by `doctrine/governance/cleanup-backlog.md`; do not auto-apply changes.)

Last reviewed: 2026-05-12. Next review due: 2026-11-12.
