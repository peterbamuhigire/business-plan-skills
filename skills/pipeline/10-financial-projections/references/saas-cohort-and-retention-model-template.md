---
source: Mersch (Hacking SaaS) ch. 11; Garbugli; Skok forentrepreneurs.com
frameworks: [Logo cohort retention, Revenue cohort retention, Smile curve, Involuntary-churn cohort]
skill: 10-financial-projections (and saas-cohort-retention-modeling)
cross-reference: [saas-unit-economics-model-template, saas-customer-success-operating-model]
---

# SaaS Cohort & Retention Model — Reference Template

## 1. Why Cohort Retention is the Single Most Diagnostic SaaS Exhibit

Aggregate churn hides the truth. A 3% monthly aggregate churn might be:
- 1% for old customers + 6% for new customers → onboarding is broken
- 6% for SMB + 0.5% for Enterprise → SMB unit economics may fail
- 2% voluntary + 1% involuntary → payment-rail fix would dramatically improve

Cohort retention curves expose all of these. They are the standard SaaS analytical artefact, expected in every investor data room.

## 2. The Two Cohort Views

### Logo (Customer) Cohort Retention

For each cohort = customers acquired in Month X, plot: % of original cohort still customers in Month X+0, X+1, X+2, ... X+24.

Typical healthy SaaS curves:
- **Enterprise**: month-0 100% → month-12 90% → month-24 80% → flat
- **Mid-market**: 100 → 85 → 70 → 60
- **SMB**: 100 → 75 → 55 → 40

The curve should **flatten** over time (logo churn rate decreases as the cohort matures). A curve that stays linear means the product isn't sticky.

### Revenue (Net Revenue Retention) Cohort

For each cohort, plot: revenue from the cohort in month X+N divided by revenue from the cohort in month X+0.

The crucial difference from logo cohort: this includes expansion. Healthy SaaS shows:
- Initial decline (some logos churn early)
- Curve bottoms out
- Curve turns **upward** as expansion from retained customers exceeds revenue lost to churned ones
- This is the **"smile curve"** — the signature of net-negative-churn SaaS

If the revenue cohort never turns upward, the business is leaking value over time, no matter how fast new customer acquisition is.

## 3. The Cohort Matrix (canonical exhibit)

```
              Months since acquisition
Cohort        M0    M1    M2    M3    M6    M12    M18   M24
2024-01      100%  93%   89%   86%   78%   72%    68%   65%
2024-02      100%  92%   88%   85%   77%   71%    67%   64%
2024-03      100%  94%   91%   88%   80%   74%    70%
2024-04      100%  95%   92%   89%   82%   75%
...
2025-12      100%  96%   93%
```

(Recent cohorts have fewer columns because not enough time has passed.)

## 4. Computing the Curves

### Logo Cohort Retention
```
For each cohort (acquisition month X):
  Cohort_Size_M0 = customers acquired in month X
  For each subsequent month Y:
    Retained(Y) = cohort customers still active at end of month Y
    Logo_Retention(Y) = Retained(Y) / Cohort_Size_M0
```

### Revenue Cohort Retention (NRR per cohort)
```
For each cohort:
  Cohort_Revenue_M0 = sum of MRR from cohort customers at start
  For each subsequent month:
    Cohort_Revenue(Y) = current MRR from those who remain
                        + expansion MRR from those who remain
    NRR_Cohort(Y) = Cohort_Revenue(Y) / Cohort_Revenue_M0
```

## 5. The Involuntary-Churn Cohort (Africa-specific discipline)

Separate cohort tracking for involuntary churn (payment failures, card declines, mobile-money timeouts). Why: voluntary churn signals product/value-fit issues; involuntary churn signals payment-infrastructure issues. They require completely different remediation:

- High voluntary churn → product, onboarding, value-delivery investment
- High involuntary churn → dunning automation, payment-retry, alternative payment-rail integration

Best-in-class involuntary-churn rate: <1% annually. Africa average: 3–6% annually due to mobile-money and card-rail friction.

## 6. Cohort Gross Margin

For each cohort, compute gross margin separately. Why: customer-success cost, support cost, and infrastructure cost are often disproportionately concentrated in newer cohorts (early-product-version customers need more support).

```
For each cohort:
  Cohort Gross Margin = (Cohort Revenue - Cohort COGS attributed) / Cohort Revenue
```

This often shows that the youngest cohorts have lower gross margin (40-60%) which gradually improves to mature-cohort levels (75-85%). Plans must model this.

## 7. Cohort-Driven LTV (more accurate than aggregate)

Rather than assume one churn rate for the entire customer base, compute LTV per cohort:

```
For each cohort:
  Expected lifetime = sum over months of (cumulative retention × ARPU × cohort gross margin %)
  Cohort LTV = expected lifetime revenue × gross margin
```

A young SaaS company with limited cohort data should still produce this table with the data it has, and explicit assumptions for projected future months.

## 8. Cohort Retention by Segment

For mid-stage SaaS, the cohort matrix should be split by:
- Customer segment (SMB / Mid / Enterprise)
- Acquisition source (paid / inbound / outbound / referral)
- ICP fit (in-ICP / out-of-ICP)
- Geography (country / region)
- Vertical (within vertical SaaS)
- Plan tier (Tier 1 / Tier 2 / Tier 3)

Each split surfaces a different lesson. Out-of-ICP customers usually have 2–3× the churn of in-ICP customers — proving the ICP is the single most leverageable input.

## 9. Worked Example (Ugandan Vertical SaaS)

**Plan:** dairy-cooperative SaaS, monthly billing, mobile-money payments.

**Year 1 Cohort Matrix (12 months in):**
```
Cohort    M0    M3    M6    M9    M12
Jan-25    100%  92%   85%   78%   72%
Feb-25    100%  93%   86%   79%   73%
Mar-25    100%  90%   82%   75%   68%   ← worse cohort (caused by competitor launch in March)
Apr-25    100%  94%   88%   82%   76%   ← better cohort (improved onboarding)
...
```

**Insights:**
- March cohort underperformed → diagnosis: a competitor launched aggressive pricing
- April cohort outperformed → diagnosis: new in-product onboarding tour deployed
- Both lessons feed back into Section 07 (marketing) and Section 03 (product)

**Smile-curve test (revenue cohort):**
- Jan-25 cohort revenue at M12 = 78% of M0 (in the trough)
- Forecast: expansion (new modules launching Q3) should turn this upward by M18

If the smile curve never appears, the plan must either (a) invest in expansion-revenue mechanics or (b) accept that LTV is bounded and the model is acquisition-treadmill.

## 10. Living-Plan Discipline

- **Data feed**: billing system (Stripe / Paystack / Chargebee / Maxio) export
- **Cadence**: monthly cohort refresh
- **Owner**: CFO / Head of CS
- **Decision triggers**: any cohort showing >2× the historical-average churn triggers a CS / product review
- **Variance threshold**: cohort retention curve declining vs prior cohort by >5pp at M6 triggers replan of retention strategy
- **Quarterly QBR**: cohort matrix is a standing slide

## 11. Africa / Uganda Application Notes

- Build the **involuntary-churn cohort** separately from day one. African payment rails (M-Pesa, MoMo, Paystack, Flutterwave) have higher failure rates than US card rails.
- Mobile-money timeouts produce false-positive churn — customers who didn't intend to cancel. Investing in retry / dunning automation (3 retry attempts over 7 days) typically recovers 30–50% of these "lost" customers.
- Cohort gross margin is more volatile in Africa due to FX exposure — track in USD as well as local currency to separate FX impact from operational impact.
- Vertical-SaaS African plans should split cohorts by **region** (Nairobi vs Mombasa vs Kisumu for Kenyan SaaS; Lagos vs Abuja vs Port Harcourt for Nigerian SaaS) because regional economic conditions drive different churn dynamics.
- Public-sector / NGO cohorts churn very differently from private-sector cohorts (funding-cycle dependence). Separate them.
