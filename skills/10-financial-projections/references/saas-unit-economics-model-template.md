---
source: Mersch (Hacking SaaS), Cotton (How to Run a SaaS Business), Walling (SaaS Playbook), Skok (forentrepreneurs.com benchmark library)
frameworks: [LTV, CAC, CAC Payback, LTV:CAC, Gross Margin, NRR, GRR, Rule of 40, Burn Multiple, Magic Number, Quick Ratio]
skill: 10-financial-projections (and saas-unit-economics-and-cohort-model)
cross-reference: [meta-bankability-scoring, meta-valuation, meta-financial-stress-test, saas-cohort-and-retention-model-template]
---

# SaaS Unit Economics Model — Reference Template

This file is the canonical SaaS unit-economics reference for every business plan in this engine. Every SaaS / ICT plan must produce all the metrics below, with explicit formulas, assumptions, and benchmark comparisons.

## 1. The Twelve Core SaaS Metrics

| Metric | Formula | Best-in-class | Healthy | Concerning |
|---|---|---|---|---|
| **MRR** | Sum of all monthly recurring contracts | n/a (size-dependent) | Growing | Flat / declining |
| **ARR** | MRR × 12 (or contractual annualised value) | n/a | Growing 2–3× YoY (early) / 40%+ (mid) | <20% YoY |
| **Net New ARR** | New + Expansion − Contraction − Churn | Positive and growing | Positive | Negative |
| **Gross Margin (Recurring)** | (Recurring Rev − COGS_recurring) / Recurring Rev | 80–90% | 70–80% | <65% |
| **CAC** | (S&M cost in period) / (New customers in period) | n/a (compare to LTV) | n/a | n/a |
| **CAC Payback** | CAC / (ARR per customer × Gross Margin %) months | <12 months (SMB) <18 (mid) <24 (ent) | <18 (SMB) <24 (mid) <30 (ent) | >24 (SMB) >36 (mid) |
| **LTV** | (ARPU × Gross Margin %) / (Monthly Gross Churn) | n/a | n/a | n/a |
| **LTV:CAC** | LTV / CAC | ≥5 | ≥3 | <3 |
| **Gross Revenue Retention (GRR)** | (Starting MRR − Churn − Contraction) / Starting MRR | >90% (ent) >85% (mid) >75% (SMB) | >85/80/70 | <80/70/65 |
| **Net Revenue Retention (NRR)** | (Starting MRR + Expansion − Contraction − Churn) / Starting MRR | >120% | >110% | <100% |
| **Magic Number** | (Net New ARR × 4) / Prior-quarter S&M | >1.5 | 1.0–1.5 | <0.75 |
| **Rule of 40** | YoY Growth % + Operating Margin % | ≥40 | ≥30 | <20 |
| **Burn Multiple** | Net Cash Burn / Net New ARR | <1.0 | <2.0 | >3.0 |
| **Quick Ratio** | (New MRR + Expansion MRR) / (Contraction + Churn MRR) | >4 | >2 | <1 |

## 2. Detailed Formulas

### LTV (Lifetime Value) — three increasingly precise formulations

**Simple:**
```
LTV = ARPU × Average Customer Lifetime (months)
    = ARPU / Monthly Gross Churn Rate
```

**Gross-margin-adjusted (Mersch / Skok standard):**
```
LTV = (ARPU × Gross Margin %) / Monthly Gross Churn Rate
```

**Expansion-adjusted (more accurate for healthy SaaS):**
```
LTV = (ARPU × Gross Margin %) / (Monthly Gross Churn Rate − Monthly Expansion Rate)
```
(If expansion > churn — i.e. NRR > 100% — LTV is mathematically infinite. In practice cap at a horizon like 5 years.)

### CAC (Customer Acquisition Cost) — fully loaded

```
CAC = (Sales costs + Marketing costs + Customer Success costs attributable to acquisition + Tools + Allocated overhead) / New customers acquired in period
```

Common mistake: CAC computed only from "marketing spend" — ignores the dominant cost, sales-team loaded comp.

### CAC Payback Period

```
CAC Payback (months) = CAC / (ARPU × Gross Margin %)
```

Equivalent: months until cumulative gross profit from a customer equals the CAC spent to acquire them.

### Magic Number (sales efficiency)

```
Magic Number = (Net New ARR for Quarter × 4) / S&M spend in Prior Quarter
```
- Magic Number > 1.0 → sales investment is paying back in <1 year → invest more
- Magic Number 0.75 – 1.0 → marginally efficient → optimise before scaling
- Magic Number < 0.75 → fix unit economics before more S&M

### Burn Multiple (Sutton / Crast)

```
Burn Multiple = Net Cash Burn / Net New ARR
```
"Net Cash Burn" = cash out − cash in for the period (operating + investing, not financing).

The current single best capital-efficiency metric. Replaces the older "growth at any cost" framing.

### Rule of 40

```
Rule of 40 = (YoY Revenue Growth % ) + (EBITDA Margin %)  [or FCF Margin %]
```

Target ≥ 40. Public-market SaaS benchmark. Below 30 is a warning.

### Quick Ratio (Mamoon Hamid / Social+Capital)

```
Quick Ratio = (New MRR + Expansion MRR) / (Contraction MRR + Churn MRR)
```
Measures how fast you're growing relative to how fast you're losing. >4 is healthy.

## 3. The ARR Waterfall (mandatory exhibit)

```
                                Starting ARR (Beginning of Period)
                            +   New ARR (new logos signed in period)
                            +   Expansion ARR (existing customer upgrades, additional seats, additional modules)
                            -   Contraction ARR (downgrades)
                            -   Churn ARR (cancellations)
                            =   Ending ARR
                            
Net New ARR = New + Expansion - Contraction - Churn
```

The waterfall should be reported monthly. Best-in-class SaaS public companies report this explicitly in earnings.

## 4. Worked Example — Ugandan SaaS Plan

**Scenario:** Vertical SaaS for Uganda dairy cooperatives. Targets 200 cooperatives at UGX 750k/month MRR each (≈ USD 200/month) by end of Year 3.

**Assumptions (Year 1 ending):**
- Customers: 35
- ARPU: UGX 750,000 / month
- ARR: 35 × 750,000 × 12 = UGX 315 million
- Gross margin (recurring): 72% (allows for AWS infra in USD, SMS gateway fees, payment-rail fees, customer-support cost)
- Monthly gross churn: 2.5% (high — early-stage, learning curve)
- Monthly expansion: 1.0% (modest — limited upsell modules in Y1)
- New customers in Y1: 35 (cold start)
- S&M spend in Y1: UGX 180 million (1 sales lead, 1 SDR, content, events)

**Computed metrics (Year 1):**
- LTV (gross-margin-adjusted) = (750,000 × 72%) / 2.5% = UGX 21.6 million per customer
- CAC = 180,000,000 / 35 = UGX 5.14 million
- LTV:CAC = 21.6 / 5.14 = **4.2** ✓ healthy
- CAC Payback = 5.14 / (0.75 × 72%) = **9.5 months** ✓ healthy
- GRR = 1 − (0.025 × 12) = 70% — concerning, indicates retention investment needed
- NRR = 70% + (0.01 × 12) × (some expansion logic) ≈ 82% — concerning
- Rule of 40 = (year-on-year growth, n/a year 1) + EBITDA margin
- Burn Multiple = (assumed UGX 220M net burn) / UGX 315M new ARR = 0.70 ✓ elite

**Diagnosis:** Unit economics on acquisition are strong (LTV:CAC, payback). Retention is the binding constraint (high churn). Year 2 plan must invest in customer success, not more S&M.

## 5. Benchmark Sources

- OpenView Partners SaaS Benchmarks (annual)
- KeyBanc Capital SaaS Survey (annual)
- ChartMogul SaaS Benchmarks
- ProfitWell Recurring Revenue Index
- Pacific Crest SaaS Survey
- For Entrepreneurs (David Skok) sales-efficiency benchmarks

Use these for comparison, but adjust for stage (early-stage benchmarks differ from $50M+ ARR benchmarks) and segment (SMB vs Mid vs Enterprise vs B2C).

## 6. Living-Plan Discipline

For each metric in this template, the plan must specify:

- **Data feed**: the source (Stripe, Paystack, billing system, manual entry)
- **Cadence**: weekly for top-line; monthly for unit economics; quarterly for Rule of 40 and Burn Multiple
- **Owner**: CFO / Finance Lead / Founder
- **Variance threshold**: ±15% on revenue metrics, ±5pp on churn/NRR triggers replan
- **Decision-log link**: every material pricing / packaging / churn-fix decision must reference the metric impact

## 7. Africa / Uganda Application Notes

- Gross margin benchmarks should be adjusted by 5–10pp downward for African SaaS because of:
  - FX-pass-through: USD-denominated cloud and tooling against UGX/KES/NGN revenues
  - Mobile-money transaction fees (1–2% per transaction on M-Pesa, MoMo, Paystack, Flutterwave)
  - Higher customer-support intensity (sales-cycle education, longer onboarding)
- CAC Payback benchmarks: African SaaS often runs 50–100% longer than US benchmarks because of slower sales cycles. Adjust targets to <18 months (SMB), <24 (mid), <36 (enterprise).
- LTV: involuntary-churn is higher in Africa (payment failures from card declines, mobile-money timeouts). Track involuntary-churn separately from voluntary-churn; invest in dunning automation.
- Rule of 40: adjusted target of 30 for African SaaS in years 1–3 is acceptable; 40 from year 4 onward.
- Burn Multiple: African SaaS often achieves better Burn Multiples than US-equivalent stage because S&M cost is lower; this is a strength to highlight in fundraising.
- The plan must disclose **all three layers** of the cost stack: (1) USD-denominated SaaS / cloud costs, (2) local-currency labour and overhead, (3) FX-exposed pass-through costs. FX volatility appears in Section 10 sensitivity analysis.
