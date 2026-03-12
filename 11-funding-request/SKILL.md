---
name: funding-request
description: Generate the funding request section for Uganda/East Africa context — bank loans, DFI funding, equity, grants, or combinations. Covers capital ask, use of funds, DSCR calculation, collateral statement, CAMPARI alignment, and investor/lender terms. Calibrated to Ugandan bank and development finance institution requirements.
---

# Funding Request & Use of Funds Skill

Generate the section that tells lenders or investors exactly what you need, what you will do with it, and why they should fund you.

## Funder Type Identification

Before drafting this section, identify the primary funder type — this determines the entire format and content:

| Funder Type | Primary Concern | What They Want to See |
|---|---|---|
| **Ugandan commercial bank** (Stanbic, ABSA, Centenary, Equity, dfcu, HFB) | Repayment security | DSCR ≥ 1.25x; collateral ≥ 125% of loan; CAMPARI compliance |
| **Development Finance Institution** (UDB, ACF) | Development impact + viability | Social/economic impact; jobs created; sector alignment; DSCR |
| **Microfinance / SACCO** | Cash flow; group character | Mobile money/bank statements; group guarantee; track record |
| **Equity investor** (angel, VC, PE) | Return on investment | Growth potential; exit route; valuation; traction |
| **Development partner grant** (USAID, EU, GIZ) | Programme objectives | LogFrame; beneficiaries; Theory of Change — use `11b-grant-proposal` skill |
| **Government programme** (YLP, PDM, Emyooga) | Youth/women/poverty | Eligibility criteria; sector; group membership |

**Most Uganda SME plans target commercial bank or DFI funding. The Uganda Bank Loan section below is the default.**

---

## Uganda Bank Loan Mode (Default for Uganda Plans)

### Required Elements

1. **Funding amount** — Exact amount in UGX (not a range)
2. **Loan type** — Term loan (for capital expenditure), overdraft/working capital facility, or LPO/invoice financing
3. **Use of funds** — Itemised to individual line items; must match §13 implementation budget exactly
4. **Loan term and repayment** — Proposed term in months; grace period request (if any); repayment source identified
5. **DSCR calculation** — Debt Service Coverage Ratio from §10 projections: EBITDA ÷ Annual Debt Service ≥ 1.25x
6. **Owner equity contribution** — The owner's co-investment; minimum 20% of total project cost
7. **Collateral** — Primary collateral with estimated market value; coverage ratio (collateral value ÷ loan amount ≥ 125%)
8. **Security documents** — What documents exist (land title, motor vehicle logbook, debenture, personal guarantee)
9. **Compensating factors** — If collateral is weak: UCGS (Uganda Credit Guarantee Scheme), group guarantee, strong character references

### Use of Funds Format (Bank Version)

| Line Item | Amount (UGX) | % of Loan | Purpose |
|---|---|---|---|
| [Equipment/Asset 1] | [X] | X% | [Specific item, supplier, quantity] |
| [Equipment/Asset 2] | [X] | X% | [Specific item] |
| [Civil works/renovation] | [X] | X% | [Location, scope] |
| [Working capital] | [X] | X% | [Months of operating costs covered] |
| [Other — specify] | [X] | X% | [Purpose] |
| **TOTAL LOAN REQUEST** | **[X]** | **100%** | |
| *Owner equity contribution* | *[X]* | — | *Own funds / existing assets* |
| **TOTAL PROJECT COST** | **[X]** | | |

*Note: Total loan + owner equity = total project cost. Loan amount must equal sum of line items. Verify via `meta-bankability-scoring/references/consistency-audit.md` before submitting.*

### DSCR Statement

```
DEBT SERVICE COVERAGE RATIO (DSCR)

Annual EBITDA (from §10 financial projections, Year 1): UGX ___________
Annual loan repayment (principal + interest):           UGX ___________
DSCR = EBITDA ÷ Annual Debt Service = ___ / ___ = X.Xx

Bank minimum requirement: 1.25x
[Our DSCR of X.Xx exceeds / falls below] the minimum.

[If below 1.25x: Explain the mitigation — e.g., "Owner will inject UGX X additional equity in Q2
to strengthen debt service coverage" or "Revenue ramps in Q3 once equipment is fully deployed;
Year 2 DSCR projects at 1.45x"]
```

### Collateral Statement

```
PRIMARY COLLATERAL

Asset type:          [Land / Building / Vehicle / Machinery / Debenture / Personal guarantee]
Description:         [LRV/Block/Plot; vehicle reg; machinery model and serial no.]
Estimated value:     UGX ___________
Valuation basis:     [Market comparison / Professional valuation by [Firm], [Date]]
Coverage ratio:      [Collateral value] / [Loan amount] = ___% (minimum required: 125%)
Documentation:       [Land title / Logbook / Valuation report — available for inspection]

[If applicable] SECONDARY COLLATERAL / COMPENSATING FACTORS:
[List additional security or mitigants: personal guarantee of directors, UCGS application,
group guarantee, crop/produce as security, invoice discounting arrangement]
```

---

## Equity Investor Mode

### Required Elements

1. **Funding amount** — Exact amount being raised
2. **Funding type** — Equity, convertible note, SAFE, or combination
3. **Use of funds** — Detailed allocation with percentages
4. **Current capitalisation table** — Existing ownership and investment history
5. **Valuation basis** — How the company is valued and methodology used
6. **Investment terms** — What the investor receives (equity %, interest rate, conversion terms)
7. **Milestones funded** — What this capital will achieve (tied to section 13)
8. **Runway** — How long the funding lasts at projected burn rate
9. **Future funding needs** — Anticipated subsequent rounds
10. **Exit strategy** — How investors realise returns (acquisition, IPO, buyback, dividends)

### Exit Strategy Options

- **Acquisition** — Sale to strategic buyer or PE firm
- **IPO** — Public listing (typically for larger ventures)
- **Management buyout** — Founders buy back investor shares
- **Dividend/profit sharing** — Ongoing returns from profits
- **Secondary sale** — Investor sells stake to another investor

### Use of Funds Breakdown Format

| Category | Amount | % of Total | Purpose |
|---|---|---|---|
| Product development | $X | X% | [Specific deliverables] |
| Marketing & sales | $X | X% | [Specific campaigns/hires] |
| Operations | $X | X% | [Equipment, facilities] |
| Working capital | $X | X% | [Cash reserve for operations] |
| Team/hiring | $X | X% | [Specific roles] |

### Exit Strategy Options

- **Acquisition** — Sale to strategic buyer or PE firm
- **IPO** — Public listing (typically for larger ventures)
- **Management buyout** — Founders buy back investor shares
- **Dividend/profit sharing** — Ongoing returns from profits
- **Secondary sale** — Investor sells stake to another investor

## Generation Process

1. Identify funder type — this determines the format (see table above)
2. **For bank loans:** Ask for loan amount, purpose, collateral available, owner equity contribution, proposed term
3. **For equity:** Ask for amount, funding type, current valuation (if any), existing investors
4. Build detailed use-of-funds table itemised to individual line items; cross-reference §13 budget
5. **For bank loans:** Calculate DSCR from §10 projections; calculate collateral coverage ratio; run consistency check
6. **For equity:** Calculate runway at projected burn rate; define investment terms; present exit strategy
7. Before finalising, verify numbers against `meta-bankability-scoring/references/consistency-audit.md`

## Quality Criteria

- Ask is specific — single amount, not a range
- Every item in the use-of-funds table is a line item (not "working capital: 30%")
- Use of funds total = loan amount (consistency check)
- Use of funds aligns with implementation timeline (section 13)
- **For bank loans:** DSCR ≥ 1.25x; collateral coverage ≥ 125%; repayment source identified
- **For bank loans:** Run `meta-bankability-scoring` Bank Loan Readiness Mode before submitting
- **For equity:** Runway extends beyond next major milestone; exit strategy is realistic for sector and size
- Valuation methodology is defensible

## References

- `references/business-valuation-methods.md` — Three valuation approaches (intrinsic/DCF, relative/multiples, options-based); full DCF framework with WACC/CAPM formulas; terminal value mechanics (stable growth perpetuity, ROIC > WACC condition); worked DCF example in UGX for Uganda food processing company; revenue multiples (P/E, EV/EBITDA, EV/Revenue, P/Book, PEG) with comparable company analysis; pre-revenue startup valuation (survival-adjusted DCF, forward multiples, VC/angel method) with UGX worked examples; 10 valuation mistakes; 7 sanity checks; Damodaran's 10 Rules; Uganda/East Africa context (country risk premium 4–6%, illiquidity discount 25–35%, thin comparables workarounds); Valuation Method Selector table — Source: Damodaran (Wiley). **Read for any equity investor round, business sale, DFI funding request, or when a valuation figure must be defended.**
- `references/credit-assessment-frameworks.md` — 5 Cs of Credit (Character, Capacity, Capital, Conditions, Collateral) and CAMPARI framework detail
- `references/women-financing-uganda.md` — Gender-specific financing constraints and solutions: 50% capital gap vs male peers; 84% of rural land under unregistered customary tenure (no collateral); "missing middle" between microfinance and commercial bank; psychometric credit scoring as collateral alternative; Uganda-specific funding sources (UDB, aBi Finance, WEF, UNCDF, SACCOs); evidence that larger loans (+40% profits, +55% employment in Ethiopia) outperform microfinance; mobile savings for household/business separation; SACCO access pathways; sensitivity analysis on UDB concessional vs commercial rates — Source: World Bank/IFC (2022). **Read when the business owner is a woman, or when standard collateral requirements cannot be met.**
- `references/equity-term-sheets.md` — Complete equity term sheet reference: economics vs control, pre/post-money valuation, option pool shuffle, liquidation preference (worked examples with 4 scenarios), anti-dilution (full ratchet vs broad-based weighted average), cap table construction, founder vesting (4-year/1-year cliff, single vs double trigger), drag-along/tag-along/pro-rata rights, convertible notes and SAFEs (discount, valuation cap, conversion mechanics), board composition and protective provisions, negotiation priorities, Uganda/East Africa investor landscape — Source: Feld & Mendelson (2019). **Read for any equity investor round, angel funding, or impact investor engagement.**
- `meta-bankability-scoring/SKILL.md` — Bank Loan Readiness Mode with full CAMPARI checklist (28 items) and consistency audit
- `meta-bankability-scoring/references/consistency-audit.md` — 12-point cross-section consistency checker; run before submitting to any lender
- `references/esmp-template.md` — IFC/UDB-compliant Environmental and Social Management Plan template: risk tiering (Category A/B/C), environmental screening checklist, social screening (labour/community/gender), mitigation plan table, common mitigations by Uganda business type (agri-processing, poultry, hospitality, construction, healthcare, transport), monitoring indicators, NEMA/NSSF/Employment Act compliance references, grievance mechanism template, ESMS Lite for Category C businesses, and Uganda legal instrument reference table. **Complete before submitting to UDB, IFC, AfDB, or any DFI that applies IFC Performance Standards. Budget ESMP implementation costs in §10 and §11.**
- `meta-pitch-preparation/SKILL.md` — Prepare the live presentation of this section; STRONG method frame for bank meetings; DSCR and collateral coverage must be stated with confidence; Q&A preparation for the 10 hardest questions any credit officer will ask
- `meta-due-diligence/SKILL.md` — Mode A (DD readiness): every figure in this section must survive investor DD; build the data room before presenting to equity or DFI funders
- `meta-presentation-design/SKILL.md` — Slide 10 (financials), Slide 12 (the ask), and Slide 13 (use of funds) design standards; the ask slide must state exact amount, terms, and next step
