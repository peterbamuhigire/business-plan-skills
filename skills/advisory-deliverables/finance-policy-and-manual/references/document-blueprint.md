# Finance Policy & Manual — Document Blueprint

The reusable architecture for two related deliverables, synthesised from real Ugandan manuals (UCOBAC, MCLD Uganda, IMAU) and the LG (Financial & Accounting) Regulations 2007 / MOFPED Financial Reporting Guide 2024 framework. Use the chapter→skill map so accounting substance always comes from the finance engine, never improvised.

Finance-engine root: `C:\wamp64\www\chwezi-accounting-doctrine` (paths below are relative to it).

## Two documents, one source

- **Financial Management Policy** — the short, board-owned *policy* document (principles, authority, controls, thresholds). 15–30 pages.
- **Finance & Accounting Manual** — the long *procedures* document (how each process is executed, with forms). 60–150 pages.

The Policy is the apex; the Manual operationalises it. Draft the Policy first, then expand each policy statement into Manual procedures.

## Manual chapter map (and where the substance comes from)

| # | Chapter | Substance from finance-engine skill / reference |
|---|---|---|
| 1 | Introduction, scope, definitions, accounting basis, financial year, currency | `doctrine/references/uganda-ngo-financial-management-patterns.md` (NGO) or `uganda-public-sector-pfm.md` (public); `ifrs-for-smes-default.md` |
| 2 | Governance & oversight (Board, Finance/Procurement/Audit committees, roles) | `10-controls-governance-and-fraud/internal-controls-library`; `engagement-quality-and-plain-language-output` |
| 3 | Chart of accounts & coding (per budget line / per fund) | `01-foundations/chart-of-accounts-design-and-governance`; `doctrine/references/chart-of-accounts.md` |
| 4 | Budgeting & planning (cycle, committee, virement, monitoring) | `09-budgeting-fpa-and-costing/budgeting-and-rolling-forecasts`, `variance-analysis-and-kpi-reporting` |
| 5 | Income & receipting (banking-intact, receipts, deferred income) | `04-subledgers-and-operations/bank-and-mobile-money-reconciliation`; `03-ifrs-specialised-standards/ias-government-grants` |
| 6 | Cash & bank management (mandate, signatories, reconciliation) | `04-.../bank-and-mobile-money-reconciliation`; `05-.../cash-flow-forecasting-and-treasury` |
| 7 | Petty cash & imprest (float, single-txn cap, replenishment state machine) | `04-subledgers-and-operations/petty-cash-and-imprest-management` |
| 8 | Advances & accountability (retirement days, one-at-a-time, salary recovery) | `04-.../expense-management-and-staff-claims`; NGO patterns reference |
| 9 | Expenditure & payments (authorisation matrix, vouchers, cheque/EFT controls) | `05-.../accounts-payable-and-supplier-management`; `internal-controls-library` |
| 10 | Procurement & contracts (thresholds, ≥3 quotations, committee, LPO, records) | `05-.../accounts-payable-and-supplier-management`; `12-public-sector-and-ipsas/government-procurement-and-fiscal-controls` (public); proposal-skills `sectors/ppda-uganda` if PPDA applies |
| 11 | Payroll & statutory deductions | `04-subledgers-and-operations/payroll-and-statutory-postings-east-africa`; rates via Statutory Schedule only |
| 12 | Fixed assets & inventory (capitalisation threshold, depreciation policy, registers) | `04-.../fixed-assets-and-depreciation`, `inventory-costing-and-stock-accounting`; `02-.../ifrs-property-plant-equipment-ias16` |
| 13 | Grants & donor funds (restricted/unrestricted, multi-currency flexing, donor reporting) | `11-sector-and-fund-accounting/ngo-and-fund-accounting`; `12-.../donor-funded-project-fiscal-compliance` |
| 14 | Period-end close & financial reporting (statements, frequency, approval) | `06-close-consolidation-and-reporting/month-end-and-year-end-close-playbook`; `07-financial-statements-and-disclosures/financial-statements-preparation` |
| 15 | Internal control & risk (SoD, fraud, whistleblowing) | `internal-controls-library`; `forensic-accounting-and-anti-fraud`; `whistleblowing-and-finance-ethics` |
| 16 | Audit (internal & external, tenure, audit committee) | `06-.../audit-pbc-and-evidence-management`, `audit-ready-reporting-pack` |
| 17 | Records management & retention | `15-security-privacy-and-continuity/finance-data-privacy-and-retention` |
| 18 | Appendices: forms pack, Statutory Schedule, version control | this blueprint + `doctrine/references/uganda-compliance-caveats.md` |

For a public/local-government body, also layer: reporting calendar, commitment control, vote book, surcharge/liability, board of survey — all in `uganda-public-sector-pfm.md`.

## Control set (every manual must define these as named client parameters)

- **Authorisation matrix** — tiers keyed to amount: operational → management → board, with the board owning the top threshold. Parameters: the threshold figures (client/board set).
- **Segregation of duties** — the chain *request → check → approve → disburse → account → review → approve accountability*; no person in two adjacent roles; nobody approves or signs in their own favour.
- **Bank-signatory mandate** — N named signatories, any 2 transacting; principal signatory; high-value board/treasurer threshold.
- **Reconciliation & close calendar** — bank monthly; cash month-end; petty cash monthly + surprise counts; stock semi-annual; asset register annual; statements within ~3 months of year-end.
- **Procurement thresholds** — quotation trigger (≥3 quotations above the client threshold), committee composition, LPO rule, records retained.
- **Advance rules** — retirement days, one-advance-at-a-time, salary recovery on default.
- **Capitalisation & depreciation policy** — threshold (dual-currency anchor) and chosen method/rates (client-set, stated explicitly).

Render the first two as tables (an authorisation-matrix table and an SoD matrix) in every manual.

## Standard forms / templates pack (appendix)

Funds requisition; payment voucher; journal voucher; petty-cash book/sheet; advance request; advance accountability/reconciliation; local purchase order; goods received note; goods issued / stores requisition; stores ledger card; receipt / cash-acknowledgement; cheque requisition & cheque register; bank reconciliation statement; cash-count certificate; payroll sheet & pay slip; fixed-assets register (purchased and donated); asset verification report; quotations request & bid-analysis form; budget-monitoring statement; vehicle log / fuel ledger; staff clearance form. Tailor the list to the entity's actual processes — do not ship forms for processes it does not run.

## Parameterisation rule

Everything the entity must choose is a **parameter with an owner and a review date**, presented as a default-to-be-approved, not a hardcoded fact:

> "Petty cash float: **UGX [____]** (recommended default UGX 1,000,000; single-transaction cap UGX [____], recommended 100,000) — set by the Board, reviewed annually."

Statutory rates are NOT parameters — they live in the dated **Statutory Schedule** appendix and are verified against the live source register at issue (see `uganda-compliance-caveats.md`). The manual body references "the current rate per the Statutory Schedule", never a number.
