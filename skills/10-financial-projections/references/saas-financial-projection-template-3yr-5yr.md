---
source: Mersch (Hacking SaaS) ch. 5–6; Cotton; OpenView Benchmarks; KeyBanc SaaS Survey
frameworks: [Multi-Step SaaS P&L, ARR Waterfall, Working Capital Trough, Headcount-driven cost build, Sensitivity & Scenario]
skill: 10-financial-projections (and saas-mrr-arr-financial-modeling)
cross-reference: [saas-unit-economics-model-template, saas-cohort-and-retention-model-template, saas-sales-capacity-and-ramp-model]
---

# SaaS 3-Year / 5-Year Financial Projection Template

The canonical SaaS-specific financial model structure for any plan in this engine. Built around Mersch's Multi-Step Income Statement and the ARR-waterfall discipline. This template is mandatory; the engine's previous generic `financial-model-templates.md` is for non-SaaS businesses.

## 1. Worksheet / Tab Architecture (mandatory minimum)

A SaaS financial model should have these tabs (whether built in Excel, Google Sheets, or modelled in narrative form for early plans):

1. **Cover & Assumptions** — every input lives here; everything else flows from it
2. **ARR Waterfall** — monthly for Year 1, quarterly for Years 2–5
3. **Customer Build** — new customer adds, churn, expansion by month
4. **Headcount Plan** — by function, by quarter, tied to ARR milestones
5. **Multi-Step P&L** — monthly Y1, quarterly Y2–Y5
6. **Cash Flow** — operating, investing, financing
7. **Balance Sheet** — quarterly snapshots, with deferred revenue
8. **Unit Economics Dashboard** — LTV, CAC, Payback, Magic Number, Rule of 40, Burn Multiple, Quick Ratio
9. **Cohort Retention** — see `saas-cohort-and-retention-model-template.md`
10. **Sensitivity** — one-variable-at-a-time + multivariable scenarios
11. **Scenario** — Base / Bear / Bull / Stress (with explicit assumption deltas)

## 2. The Cover & Assumptions Tab (canonical fields)

### Customer & Revenue Assumptions
- Starting customer count
- New customer adds per month (by quarter, ramping)
- Sales-cycle length (for pipeline modelling)
- Win rate (qualified opportunities to closed-won)
- ARPU starting + annual price escalator
- Monthly gross logo churn (split SMB / Mid / Enterprise if tiered)
- Monthly expansion revenue rate
- Annual prepayment % of new contracts
- Annual prepayment discount %
- Mix by tier (Tier1/2/3 %)

### Cost Assumptions (segmented per Mersch Multi-Step)
**COGS / Cost of Revenue:**
- Hosting / infrastructure cost per customer per month (with growth scaling — careful with AI costs)
- Customer support cost per customer
- Third-party software / data fees (e.g., payment gateways, SMS, AI APIs)
- Customer-success cost per customer (CS team allocation)

**Operating Expense:**
- R&D headcount × loaded cost
- S&M headcount × loaded cost
- S&M non-headcount (paid media, content, events, tools)
- G&A headcount × loaded cost
- G&A non-headcount (legal, audit, office, insurance)

### FX / Localisation Assumptions (Africa)
- Reporting currency (e.g., UGX)
- USD/local FX rate (e.g., UGX 3,700)
- FX depreciation expected per year
- USD-denominated cost categories (cloud, AI, USD-priced SaaS tools)
- Local-currency cost categories (labour, rent, local services)
- Currency in which contracts are denominated (mix)

### Capital Structure
- Starting cash
- Funding to be raised, when, at what valuation, with what terms
- Debt (DFI, working capital, lease finance) with terms
- Convertible notes / SAFEs if any

## 3. The ARR Waterfall Tab

For each month (Y1) or quarter (Y2–5), produce:

```
Starting ARR
+ New Logo ARR
+ Expansion ARR (existing customer upgrades / new modules / additional seats)
- Contraction ARR (downgrades)
- Churn ARR (cancellations)
= Ending ARR

Net New ARR = New + Expansion - Contraction - Churn

Growth Rate (YoY) = (Ending ARR / Ending ARR same period prior year) - 1
```

This waterfall feeds: (a) the revenue line of the P&L (after billings-to-revenue conversion), (b) the cohort retention model, (c) the unit-economics dashboard.

## 4. The Customer Build Tab

Bottom-up customer growth model:

```
For each month:
  Beginning Customer Count
  + New customers (from sales capacity model: pipeline × conversion × win rate)
  - Churned customers (churn rate × beginning count)
  = Ending Customer Count

ARPU schedule:
  Y1 starting ARPU = X
  Annual price escalator = +5–8% per year
  Expansion: per-customer-month expansion revenue average

Revenue computation:
  MRR = Ending Customers × ARPU + expansion stock
  ARR = MRR × 12
```

## 5. The Headcount Plan Tab

Per Cotton's Rule of 3 and 10 + Mersch's S&M / R&D / G&A discipline.

Headcount tied to ARR milestones (not calendar):

| ARR milestone | Eng + Product | Sales + CS | G&A | Total |
|---|---|---|---|---|
| Pre-PMF ($0) | 2–4 | 1 | 0 (founders cover) | 3–5 |
| Early-PMF ($100k ARR) | 4–6 | 2–3 | 1 | 7–10 |
| PMF ($500k ARR) | 6–10 | 4–6 | 1–2 | 11–18 |
| Escape Velocity ($1M ARR) | 8–15 | 6–10 | 2–3 | 16–28 |
| Scale ($3M ARR) | 15–25 | 12–20 | 3–5 | 30–50 |
| Mid-scale ($10M ARR) | 30–50 | 30–50 | 8–12 | 70–110 |

Sales capacity feeds back into customer-build:
```
Sales bookings (year) = (#AEs ramped × quota) + (#AEs in ramp × ramp-adjusted quota)
                                 × Attainment %
```
Use the `saas-sales-capacity-and-ramp-model.md` reference.

## 6. The Multi-Step P&L Tab (Mersch format)

```
                                                   Y1     Y2     Y3     Y4     Y5
RECURRING SOFTWARE REVENUE                         ___    ___    ___    ___    ___
RECURRING SERVICE REVENUE                          ___    ___    ___    ___    ___
NON-RECURRING REVENUE (services, setup)            ___    ___    ___    ___    ___
TOTAL REVENUE                                      ___    ___    ___    ___    ___

COST OF REVENUE
  Hosting & infrastructure                         ___    ___    ___    ___    ___
  Customer support                                 ___    ___    ___    ___    ___
  Cloud operations / platform                      ___    ___    ___    ___    ___
  Third-party software & data fees                 ___    ___    ___    ___    ___
TOTAL COST OF REVENUE                              ___    ___    ___    ___    ___

GROSS PROFIT                                       ___    ___    ___    ___    ___
GROSS MARGIN %                                     ___    ___    ___    ___    ___

OPERATING EXPENSE
  Research & Development                           ___    ___    ___    ___    ___
  Sales & Marketing                                ___    ___    ___    ___    ___
  General & Administrative                         ___    ___    ___    ___    ___
TOTAL OPERATING EXPENSE                            ___    ___    ___    ___    ___

OPERATING INCOME (LOSS)                            ___    ___    ___    ___    ___
OPERATING MARGIN %                                 ___    ___    ___    ___    ___

  + D&A                                            ___    ___    ___    ___    ___
  + Stock-based compensation                       ___    ___    ___    ___    ___
ADJUSTED EBITDA                                    ___    ___    ___    ___    ___

Net Interest                                       ___    ___    ___    ___    ___
Tax                                                ___    ___    ___    ___    ___
NET INCOME                                         ___    ___    ___    ___    ___
```

## 7. The Cash Flow Tab — Including the Working-Capital Trough

```
                                                   Y1     Y2     Y3     Y4     Y5
Operating Cash Flow
  Cash from customers (billings collected)         ___    ___    ___    ___    ___
  Cash to suppliers/COGS                           ___    ___    ___    ___    ___
  Cash to OpEx                                     ___    ___    ___    ___    ___
  Net Operating Cash Flow                          ___    ___    ___    ___    ___

Investing Cash Flow
  Capex (laptops, equipment)                       ___    ___    ___    ___    ___
  Software dev capitalisation (if applicable)      ___    ___    ___    ___    ___
  Net Investing Cash Flow                          ___    ___    ___    ___    ___

Financing Cash Flow
  Equity raised                                    ___    ___    ___    ___    ___
  Debt drawdown / repayment                        ___    ___    ___    ___    ___
  Net Financing Cash Flow                          ___    ___    ___    ___    ___

Beginning Cash                                     ___    ___    ___    ___    ___
+ Net Cash from all activities                     ___    ___    ___    ___    ___
= Ending Cash                                      ___    ___    ___    ___    ___

Free Cash Flow (Operating + Investing)             ___    ___    ___    ___    ___
Burn (negative FCF)                                ___    ___    ___    ___    ___
Months of Runway at current burn                   ___    ___    ___    ___    ___
```

**Working Capital Trough discipline (Mersch):**
- Plot cumulative FCF month-by-month for Year 1 and 2
- Identify the trough month (typically month 12–24)
- Confirm cash + funding covers the trough plus 6 months buffer
- If not, either (a) raise more, (b) slow growth, (c) move to annual prepayment

## 8. The Balance Sheet (quarterly snapshots)

```
ASSETS
  Cash & cash equivalents
  Accounts receivable
  Prepaid expenses (incl. annual SaaS prepayments)
  PP&E (laptops, equipment)
  Total Assets

LIABILITIES
  Accounts payable
  Deferred revenue (large for annual prepayments) ←  KEY SaaS LINE
  Short-term debt
  Long-term debt
  Total Liabilities

EQUITY
  Paid-in capital
  Retained earnings / (accumulated deficit)
  Total Equity

Total Liabilities + Equity = Total Assets
```

Deferred revenue is the canonical SaaS balance-sheet item; for enterprise SaaS with annual prepayment, it can be larger than ARR.

## 9. The Unit Economics Dashboard Tab

Pull from the upstream tabs:
- ARPU, CAC, LTV, LTV:CAC, CAC Payback
- Gross Margin, NRR, GRR
- Rule of 40, Burn Multiple, Magic Number, Quick Ratio
- Monthly trend graphs for each

Each metric: actual vs plan vs benchmark.

## 10. The Sensitivity Tab

One-variable-at-a-time impact on Year 3 ARR, Year 3 EBITDA, end-Y3 cash:

| Variable | Base | -20% | -10% | +10% | +20% |
|---|---|---|---|---|---|
| Churn rate | ___ | ___ | ___ | ___ | ___ |
| Win rate | ___ | ___ | ___ | ___ | ___ |
| ARPU | ___ | ___ | ___ | ___ | ___ |
| CAC | ___ | ___ | ___ | ___ | ___ |
| Sales ramp | ___ | ___ | ___ | ___ | ___ |
| FX (UGX/USD) | ___ | ___ | ___ | ___ | ___ |
| AI cost per tenant | ___ | ___ | ___ | ___ | ___ |
| Payment-rail fee | ___ | ___ | ___ | ___ | ___ |

## 11. The Scenario Tab

| | Base | Bear | Bull | Stress |
|---|---|---|---|---|
| Churn (annual) | 12% | 18% | 8% | 25% |
| Win rate | 22% | 15% | 30% | 12% |
| ARPU | UGX 750k | UGX 600k | UGX 900k | UGX 500k |
| Sales capacity | full plan | -25% | +25% | -40% |
| FX | UGX 3,700/$ | UGX 4,200/$ | UGX 3,600/$ | UGX 4,500/$ |
| **Year 3 ARR** | ___ | ___ | ___ | ___ |
| **Year 3 EBITDA** | ___ | ___ | ___ | ___ |
| **Cash position** | ___ | ___ | ___ | ___ |
| **Runway months** | ___ | ___ | ___ | ___ |

The Stress scenario is mandatory and must be survivable with available capital, or the plan must show how it would be survived (cost cuts, additional capital, divestiture).

## 12. Reconciliation Checks (the model is not done until these pass)

- Revenue ↔ ARR waterfall ↔ Customer build are arithmetically consistent
- Headcount × loaded cost ↔ OpEx total reconciles
- Cash ending each period = previous cash + net cash flow
- Balance sheet balances every period
- Deferred revenue moves match billings-revenue timing
- Sensitivity and scenario tabs use the same model engine (no parallel sheets)

## 13. Living-Plan Discipline

Every quarter:
- Update actuals into the model alongside plan
- Recompute the dashboard
- Identify variance from plan; if >threshold, run the variance protocol
- Re-forecast the next 4 quarters
- Decision-log any model changes

Annually:
- Roll forward by one year (Y2 becomes Y1; Y6 is added)
- Re-baseline assumptions
- Re-run sensitivity and scenarios
- Refresh the MSPOT linked to this model

## 14. Africa / Uganda Application Notes

- Build the model in **UGX (or local currency) as reporting currency** even if USD pricing is used externally — DFIs and Uganda banks expect local-currency presentation.
- Maintain a parallel USD view (sensitivity tab) for international investors.
- FX sensitivity scenarios should include realistic depreciation paths (UGX has averaged 3–6% annual depreciation against USD).
- Cost stack must separately disclose: (a) USD-denominated cloud/tooling, (b) local-currency labour, (c) FX-exposed payment-rail fees, (d) USD-priced AI/API costs.
- Working-capital trough is deeper in Africa due to longer sales cycles + monthly billing preference. Plan trough buffer at 9 months (vs 6 months US standard).
- Annual prepayment uptake is typically 20–40% in African SaaS (vs 60–80% in US enterprise SaaS). Model accordingly; don't assume US prepayment rates.
- Mobile-money transaction fees (1–2% per transaction) are a real per-tenant cost; ensure they're in COGS.
- AI cost per tenant is FX-exposed (LLM APIs are USD-priced). The plan must show how this is hedged: USD-priced AI tier, usage caps, or local LLM alternatives.
