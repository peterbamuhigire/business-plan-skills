# Grants Management Manual — Document Blueprint

The reusable architecture for a standalone Grants / Donor-Funds Management Manual, synthesised from real Ugandan NGO grant-management practice and the deferred-income (fund-accounting) model. The **grant lifecycle is the spine**: every chapter hangs off it. Use the chapter→skill map so accounting substance always comes from the finance engine, never improvised; layer each donor's stricter rules on top per grant.

Finance-engine root: `C:\wamp64\www\chwezi-accounting-doctrine` (paths below are relative to it). Donor-rule packs live in `proposal-skills` (`C:\wamp64\www\proposal-skills`).

## One document, one spine

A single *procedures* document (typically 50–120 pages) governing how received grants are managed end-to-end. It is **not** a proposal (`pipeline/11b-grant-proposal` writes those) and **not** the grants chapter of a finance manual — it is the full standalone manual. Restricted vs unrestricted fund accounting is its backbone; the deferred-income model is non-negotiable.

## The grant lifecycle (the spine)

Draft every chapter against this sequence; each stage is a chapter:

1. **Pre-award due diligence** — donor and (for sub-grants) sub-grantee assessment; capacity, compliance history, conflict screening; go/no-go.
2. **Agreement review** — read the grant agreement before signing; capture restrictions, eligible-cost rules, reporting calendar, audit clauses, currency, retention, branding, asset-disposition terms; record the **original-budget rate (rate at agreement signing)**.
3. **Budgeting & set-up** — dual-currency budget (donor currency + UGX); open a **separate bank account and cost centre per donor**; build a chart of accounts that **mirrors each grant budget line**; register the donor.
4. **Disbursement** — record receipt (and any deduction at source / in-kind fair value); recognise as **deferred income**, not revenue; acknowledge with a receipt.
5. **Accounting & fund control** — restricted/unrestricted segregation; release deferred income to revenue as eligible expenditure is incurred; multi-currency flexing; cost-eligibility testing.
6. **Monitoring & reporting** — budget-vs-actual-vs-variance against the **flexed** budget, with narrative; donor financial reports quarterly or per donor terms; sub-grantee retirement.
7. **Audit & close-out** — donor audits; ineligible-cost recovery; final report and reconciliation; grant close-out and asset disposition per donor consent.

## Chapter map (and where the substance comes from)

| # | Chapter (lifecycle stage) | Substance from finance-engine skill / reference |
|---|---|---|
| 1 | Introduction, scope, fund-accounting basis (restricted vs unrestricted), definitions | `skills/11-sector-and-fund-accounting/ngo-and-fund-accounting`; `doctrine/references/uganda-ngo-financial-management-patterns.md` |
| 2 | Governance & roles (Board, Finance/Audit committee, grants officer, donor relations) | `skills/10-controls-governance-and-fraud/internal-controls-library` |
| 3 | Pre-award due diligence (donor & sub-grantee assessment, go/no-go) | `skills/12-public-sector-and-ipsas/donor-funded-project-fiscal-compliance` |
| 4 | Grant agreement review (restrictions, audit clauses, branding, retention, asset terms) | `skills/12-.../donor-funded-project-fiscal-compliance`; donor packs (`proposal-skills`) |
| 5 | Donor register & acknowledgement (capture, deductions at source, in-kind fair value, receipt) | `skills/11-.../ngo-and-fund-accounting`; NGO patterns reference |
| 6 | Grant recognition & deferred income (IAS 20 / Section 24; asset- vs income-related; in-kind at fair value) | `skills/03-ifrs-specialised-standards/ias-government-grants` |
| 7 | Chart of accounts & coding (mirrors each grant budget line; cost centre per donor) | `skills/11-.../ngo-and-fund-accounting`; `doctrine/references/chart-of-accounts.md` |
| 8 | Budgeting (dual-currency budget, original-budget rate, virement within donor rules) | `skills/09-budgeting-fpa-and-costing/budgeting-and-rolling-forecasts` |
| 9 | Multi-currency management & flexing (weighted-average rate, exchange differences) | `skills/01-foundations/functional-and-presentation-currency`; `skills/05-receivables-payables-and-treasury/fx-management-and-hedging` |
| 10 | Cost eligibility (Reasonable / Allocable / Allowable; unallowable-cost list; questionable costs) | `skills/12-.../donor-funded-project-fiscal-compliance` |
| 11 | Sub-granting (assessment, sub-grant agreement, advances, monthly retirement) | `skills/12-.../donor-funded-project-fiscal-compliance`; `internal-controls-library` |
| 12 | Monitoring & donor reporting (budget-vs-actual-vs-variance against flexed budget, narrative) | `skills/09-.../variance-analysis-and-kpi-reporting` |
| 13 | Audit & close-out (donor audits, ineligible-cost recovery, close-out, asset disposition) | `skills/06-close-consolidation-and-reporting/audit-pbc-and-evidence-management` |
| 14 | Records management & retention (per donor terms; may exceed the 5–7 year default) | `skills/15-security-privacy-and-continuity/finance-data-privacy-and-retention` |
| 15 | Appendices: forms pack, Statutory Schedule, version control | this blueprint + `doctrine/references/uganda-compliance-caveats.md` |

Layer donor-specific rules from `proposal-skills` packs (`sectors/world-bank`, `sectors/undp`, `sectors/afdb`, `domain-delivery/giz-eu-local-procurement-response`) over every chapter: where a donor's rule is stricter than the organisation's baseline, the donor rule wins for that grant. Also reference `country-context/uganda` and `language/east-african-english`.

## Fund-control core (every manual must state these)

- **Restricted vs unrestricted.** Restricted grants may be spent only on their stated purpose; unspent restricted balances are carried as **deferred income (a liability)**, released to revenue only as eligible expenditure is incurred. Unrestricted funds support general operations.
- **Separation per donor.** A separate bank account and a separate cost centre for each donor/grant; no commingling.
- **Budget-mirrored coding.** The chart of accounts maps line-for-line to each grant budget, so actuals report directly against budget lines.
- **In-kind donations** recognised at fair value.

## Multi-currency flexing — worked logic

1. **Original budget rate** = the exchange rate at **agreement signing**. The dual-currency budget fixes the donor-currency total and its UGX equivalent at this rate.
2. **Disbursements** arrive over the grant life at varying rates. Record each at its actual rate.
3. **Flexing** restates the budget using a **weighted-average rate computed from actual disbursements** (each tranche weighted by its donor-currency amount). This produces the **flexed budget** in UGX.
4. **Variance** is measured as actual UGX expenditure against the **flexed budget** — never against the original budget — so a currency move is not mistaken for over/under-spend.
5. **Exchange differences** (between original-budget rate, flexed rate, and settlement rates) are accumulated, tracked, and **explained in the quarterly narrative**, distinguishing genuine variance from FX effect.

> Worked illustration: grant of USD 100,000 signed at UGX 3,700/USD → original budget UGX 370,000,000. Disbursed USD 40,000 @ 3,750 and USD 60,000 @ 3,800 → weighted-average rate (40,000×3,750 + 60,000×3,800) / 100,000 = **UGX 3,780/USD** → flexed budget UGX 378,000,000. Measure spend against UGX 378m; the UGX 8m uplift is an FX effect, not over-budget room.

## Parameterisation rule

Everything the entity must choose is a **parameter with an owner and a review date**, presented as a default-to-be-approved, not a hardcoded fact:

> "Sub-grantee advance retirement: within **[____] days** of month-end (recommended default 5 days); maximum outstanding advance per sub-grantee **UGX [____]** — set by the Board, reviewed annually."

Statutory rates are NOT parameters — WHT-at-source on grant payments, VAT treatment, and PAYE on grant-funded staff live in the dated **Statutory Schedule** appendix and are verified against the live source register at issue (see `uganda-compliance-caveats.md`). The body references "the current rate per the Statutory Schedule", never a number.

**Retention** is per donor terms and may exceed the 5–7 year default — record the longest applicable period as a parameter per grant.

## Standard forms / templates pack (appendix)

Donor register; grant agreement review checklist; grant acknowledgement / receipt; deferred-income / fund-movement schedule; dual-currency budget & flexed-budget statement; budget-monitoring statement (budget-vs-actual-vs-variance with narrative); cost-eligibility checklist (Reasonable / Allocable / Allowable) and unallowable-cost list; sub-grantee assessment form; sub-grant agreement; advance request form; advance accountability / retirement form; in-kind donation valuation form; donor financial report template; ineligible-cost recovery schedule; grant close-out checklist; asset-disposition (donor consent) form. Tailor the list to the entity's actual processes — do not ship forms for processes it does not run (e.g. omit sub-grant forms where the entity does not sub-grant).
