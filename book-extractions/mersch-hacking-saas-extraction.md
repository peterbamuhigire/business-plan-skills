# Book Extraction: Eric Mersch — Hacking SaaS

**Source:** Mersch, Eric. *Hacking SaaS* (FLG Partners, 2023). Author is a serial SaaS CFO (15+ years CFO experience, Bay Area FLG Partners) writing the definitive CFO-grade operating manual for SaaS.

**Why this matters:** Where Walling teaches the bootstrap mindset and Cotton teaches the marketing/operating frameworks, Mersch teaches the **finance operating model**. For a business plan to be bankable, equity-investable, or grant-fundable, the financial section must speak the language of SaaS CFOs: top-line metrics, unit economics, financial profile, GAAP/IFRS reporting, Working Capital Trough, the three customer-centric models (Enterprise / SMM / B2C), and the industry-centric split (Horizontal vs Vertical SaaS). This book is the CFO-grade guard rail for the financial-projections, valuation, and bankability skills.

---

## 1. SaaS is a Business Model, not a delivery mechanism

Mersch opens with the canonical CFO mistake (a peer CFO claiming "SaaS is just like newspapers — monthly subscription"). The differentiator: SaaS companies watch customer interaction in real-time and feed that data back into rapid product iteration. The implications cascade through the financial profile.

| Perpetual Software (1980–2000) | SaaS |
|---|---|
| One-time licence + maintenance | Recurring subscription |
| Capex for customer (hardware, install) | Opex for customer (subscription) |
| Customer support is overhead | Customer success is revenue protection |
| Multi-year innovation cycles | Continuous deployment |
| No customer behaviour data | Full real-time telemetry |

## 2. The Three Categories of SaaS Metrics

Mersch's canonical framework for any SaaS plan / report / board pack:

### A. Top-Line Metrics
- **ARR** (Annual Recurring Revenue) — contractual annualised subscription value
- **MRR** (Monthly Recurring Revenue)
- **New ARR** (sales from new logos)
- **Expansion ARR** (existing customer upgrades / cross-sells)
- **Contraction ARR** (downgrades)
- **Churn ARR** (cancellations)
- **Net New ARR** = New + Expansion − Contraction − Churn
- **Growth Rate** (Net New ARR ÷ starting ARR)
- **Bookings** (the dollar value of contracts signed in period, ≠ revenue)

### B. Unit Economics
- **CAC** — fully-loaded S&M cost ÷ new customers
- **LTV** — average revenue per customer × gross margin × average customer lifetime (1 ÷ churn)
- **LTV:CAC** — ≥3:1 healthy
- **CAC Payback Period** — months until cumulative gross profit = CAC. Target <12 months for SMB SaaS, <18 for mid-market, <24 for enterprise.
- **Gross Margin** — segmented by recurring SW vs services
- **Magic Number** — (Net New ARR × 4) ÷ prior-quarter S&M spend. >1.0 means sales are paying back within 1 year.

### C. Financial Metrics
- **Operating Income** / **EBITDA** / **Adjusted EBITDA** (excludes SBC, non-cash, non-operating)
- **Free Cash Flow** = Cash from Ops + Cash from Investing. This is the **single most important line item in SaaS finance**.
- **Burn / Burn Multiple** = Net Burn ÷ Net New ARR. <1 elite, <2 healthy, >3 unsustainable
- **Months of runway** = cash ÷ monthly net burn

## 3. The Three Financial Statements — Best-Practice Format

Mersch insists on **Multi-Step Income Statement** format for SaaS, segmenting:

**Revenue**:
- Recurring software revenue (the headline)
- Recurring service revenue (support contracts)
- Non-recurring revenue (implementation / professional services)

**Cost of Revenue** (separately disclosed):
- Hosting and infrastructure
- Customer support
- Cloud operations / platform support
- Third-party software / data fees

**Operating Expense** in three buckets:
- R&D (engineering + product)
- S&M (sales, marketing, customer success, sales commissions)
- G&A (finance, legal, HR, facilities)

**Plan implication:** the engine's financial-projections template must produce this exact multi-step format, not a generic P&L. This is what investors and banks expect for SaaS.

## 4. The Working Capital Trough

Mersch's most important conceptual contribution: in SMB and B2C SaaS where customers pay monthly, **faster growth means deeper cash burn before profitability**. The CAC is spent up-front; the LTV is collected over many months. Until the LTV crosses CAC (CAC payback period), each new customer destroys near-term cash.

Diagram (verbal):
- Month 1: spend $X on CAC. Customer pays $Y/mo.
- Cumulative cash flow goes negative immediately by ($X − $Y × GM%).
- Cumulative cash flow turns positive after CAC payback period.
- During growth, you're always adding new customers in their pre-payback months.
- Net effect: the faster you grow, the deeper the cash trough.

**Plan implication:** Section 10 must explicitly model the Working Capital Trough — the worst cash month is usually 12–24 months from launch, NOT month 1. Plans that don't model this run out of cash unexpectedly.

## 5. Enterprise SaaS — The Up-Front Cash Model

Enterprise SaaS has **annual or multi-year prepayment**, which creates **deferred revenue** liability on the balance sheet but creates **positive working capital** because customers fund operations.

Mersch's Enterprise SaaS financial profile:
- Gross Margin: 75–80%
- S&M as % of revenue: 40–60% (high-touch sales)
- R&D as % of revenue: 20–30%
- G&A as % of revenue: 10–15%
- CAC payback: 12–24 months
- Rule of 40: target ≥40 by year 3–5
- ARR growth: best-in-class doubles annually until $50M ARR

## 6. SMB / Mid-Market SaaS

Different profile because customers are monthly-pay, lower ACV:
- Gross Margin: 70–80%
- S&M: 40–50% (lower-touch, more inbound)
- R&D: 20–25%
- G&A: 8–15%
- CAC payback: <12 months mandatory
- Churn: 1–3% monthly typical (12–36% annual gross)
- Working Capital Trough is real and deep

## 7. B2C SaaS

Highest customer volume, lowest ACV:
- Gross margin similar
- Heavy reliance on freemium + PLG
- Working capital trough most severe
- Cohort retention curves are the central analytical tool
- Marketing dominates S&M (paid ads, content, SEO)

## 8. Industry-Centric: Horizontal vs Vertical SaaS

**Horizontal SaaS** (Salesforce, HubSpot, Slack, Zoom): one product across many industries. Pros: huge TAM. Cons: harder to differentiate, more competition, deeper feature lift to serve any single vertical well.

**Vertical SaaS** (Veeva for life sciences, Procore for construction, Toast for restaurants, ServiceTitan for trades): industry-specific platform. Pros: deep ICP, lower churn, stronger pricing power, less competition, often payments-and-services upsell. Cons: smaller TAM ceiling, requires sector expertise to build.

**Plan implication for African ICT/SaaS:** Vertical SaaS is the most natural African opportunity because:
- Local-context expertise IS the moat (knowing M-Pesa flow, KRA/URA tax integration, local-language SMS dialects).
- Smaller TAM is less of a constraint at the ARR ranges African plans realistically target.
- Sector-specific consortia and DFIs fund vertical-SaaS plays (agritech, fintech-for-MSMEs, healthtech, edutech, logistics, energy).

## 9. The CFO-Grade Five-Year Financial Model

Mersch builds a worked example of a five-year model with:
- Quarterly ARR build (New + Expansion − Contraction − Churn)
- Headcount plan tied to bookings capacity (sales capacity formula: bookings = #reps × quota × attainment %)
- Cohort-based revenue recognition
- Cash conversion (bookings → billings → revenue → cash)
- Deferred revenue waterfall
- S&M / R&D / G&A as % of revenue benchmarked against public SaaS
- Sensitivity to churn, win-rate, expansion, ramp time

**Plan implication:** the engine's `saas-financial-projection-template` must produce this CFO-grade artefact, not a generic small-business P&L.

## 10. Benchmarking Discipline

Mersch's CFO posture: every line item in the model should be benchmarked against:
- Public-company SaaS (Salesforce, HubSpot, Workday, Veeva, ServiceNow, etc.)
- Private market data (OpenView SaaS Benchmarks, KeyBanc SaaS Survey, ChartMogul, ProfitWell)
- Peer companies at the same stage

When a projection deviates from benchmark materially, the plan must explain why — a CFO red flag if unjustified.

## 11. The Burn Multiple — the new VC obsession

Burn Multiple = Net Burn ÷ Net New ARR.
- < 1.0 = elite (Klaviyo, Wiz, Datadog scale early)
- 1.0 – 1.5 = healthy
- 1.5 – 2.0 = acceptable
- 2.0 – 3.0 = concerning
- > 3.0 = unsustainable, fix-or-die

Plans should target burn multiple <2 by year 2, <1.5 by year 3.

## 12. SaaS Cohort Modelling

Cohort retention curves answer: "of the customers we acquired in Month X, what % were still customers in Month X+12?" Two views:
- **Logo cohort** — % of customers retained
- **Revenue cohort** — % of original cohort revenue retained (can exceed 100% with expansion)

Healthy SaaS cohorts flatten and then turn upward as expansion exceeds churn (the "smile curve" cohort).

**Plan implication:** cohort retention model is a mandatory exhibit in Section 10. Even projections (without actuals) can show projected cohort curves with the assumptions stated.

## 13. The CFO's role in strategy

Mersch's final thesis: SaaS CFOs are not bookkeepers, they are strategic partners. They translate operational metrics into financial outcomes and back. Every operating decision (pricing, packaging, geography, vertical, hiring) flows through to the financial profile.

## 14. Hardening Rules for the Business-Plan Engine

- Section 10 must use Multi-Step Income Statement format with SaaS-specific COGS / OpEx categories.
- Section 10 must include ARR waterfall (new + expansion − contraction − churn).
- Section 10 must model the Working Capital Trough explicitly.
- Section 10 must show CAC payback, LTV:CAC, Magic Number, Burn Multiple, Rule of 40 — not just gross margin and net income.
- Cohort retention curves mandatory.
- Sensitivity to churn, win-rate, expansion-rate, CAC, gross-margin mandatory.
- Plans must declare whether they are Enterprise / SMM / B2C and Horizontal / Vertical, and adopt the corresponding financial profile benchmarks.
- Deferred revenue (for prepaid annual contracts) must appear on projected balance sheet.

## 15. Uganda / East Africa / Africa Application Notes

- Vertical SaaS is the strategic sweet-spot for African plans because local-context expertise is the moat (agritech, fintech-for-MSMEs, healthtech, logistics, energy access, public-sector procurement).
- Enterprise SaaS with annual prepayment is harder in Africa because customers prefer monthly billing and FX volatility makes USD-denominated annual contracts politically sensitive. Plan to offer multi-year contracts in local currency with annual price-escalator clauses.
- Working Capital Trough is more severe in African SaaS because FX-hedged USD costs (cloud, software) sit against UGX/KES/NGN revenues. Plan must model FX-pass-through or USD-pricing strategy.
- Magic Number and Burn Multiple benchmarks should be adjusted by 0.2–0.5 unfavourably for African SaaS due to higher S&M cost per customer (longer education cycle, lower category awareness).
- Cohort modelling matters more because African SaaS churn drivers include payment failure (Stripe unavailability, card decline, mobile-money timeout). Separate involuntary-churn cohort from voluntary-churn cohort.
- CFO-grade reporting is rare in African SaaS — adopting it early is a powerful signal to DFIs and international VCs (TLcom, Partech, P1, Future Africa, Catalyst Fund).
