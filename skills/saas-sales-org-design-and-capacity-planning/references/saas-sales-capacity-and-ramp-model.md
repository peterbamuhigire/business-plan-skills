---
source: van der Kooij (WBD), Mersch (Hacking SaaS), Skok forentrepreneurs.com, KeyBanc SaaS Survey
frameworks: [Sales capacity formula, Ramp curve, OTE structure, Pod design, Hiring sequence by ARR milestone]
skill: saas-sales-org-design-and-capacity-planning
cross-reference: [saas-gtm-motion-design, 09-management-team, 10-financial-projections]
---

# SaaS Sales Capacity & Ramp Model — Reference Template

## 1. The Master Capacity Formula

```
Bookings (annual) = Σ (over all AEs) [ Quota × Attainment % × (1 − Ramp Discount) ]
```

Where for each AE:
- **Quota** = annualised new-ARR target
- **Attainment %** = expected % of quota actually achieved (60–70% healthy)
- **Ramp Discount** = reduced productivity in the first N months (declines over time)

The ramp discount applied:
```
Month in role    Productivity %    Ramp discount
1-3              25%               75%
4-6              50%               50%
7-9              75%               25%
10+              100%              0%
```

(Faster for transactional sales; slower for enterprise.)

## 2. AE Archetype to Quota Mapping

| AE archetype | ACV Range | Annual quota (US) | Annual quota (Africa local) | Deal velocity |
|---|---|---|---|---|
| SMB AE | $1-10k | $500k-$1M ARR | $250-500k ARR | 5-15 deals/month |
| Mid-market AE | $10-50k | $1-1.5M ARR | $500k-$1M ARR | 1-3 deals/month |
| Enterprise AE | $50-250k+ | $1-2M ARR | $750k-$1.5M ARR | 4-8 deals/year |
| Strategic AE | $250k+ | $2-3M ARR | $1-2M ARR | 2-4 deals/year |

## 3. The OTE Structure (US baseline, African adjustment)

OTE = On-Target Earnings = total comp if 100% attainment.

| Role | US OTE | Africa OTE | Base / Variable split |
|---|---|---|---|
| SDR | $60-80k | $15-25k | 70/30 |
| SMB AE | $80-120k | $20-35k | 50/50 |
| Mid-market AE | $130-180k | $30-55k | 50/50 |
| Enterprise AE | $200-300k | $50-100k | 50/50 |
| Strategic AE | $300-500k | $80-150k | 50/50 or 40/60 |
| Sales Manager | $200-300k | $50-100k | 60/40 |
| VP Sales | $350-500k | $100-200k | 60/40 |
| CSM (mid-touch) | $80-120k | $20-35k | 80/20 |
| Senior CSM | $120-180k | $35-60k | 70/30 |
| Head of CS | $200-300k | $60-100k | 70/30 |

**Fully loaded cost** = OTE × 1.3 (benefits, payroll tax, tools, allocated overhead).

## 4. Pod Structure

Modern SaaS often uses "pods" — small cross-functional units:

**SMB Pod** (~$2M ARR responsibility):
- 1 SDR + 2 AEs + 1 CSM + shared marketing-ops

**Mid-Market Pod** (~$5M ARR responsibility):
- 1 BDR + 2 AEs + 1 SE (solutions engineer) + 1 CSM

**Enterprise Pod** (~$10M ARR responsibility):
- 1 BDR + 1 AE + 1 SE + 1 CSM (high-touch) + executive sponsor

## 5. The Hiring Sequence by ARR Milestone

| ARR Milestone | Total HC | Engineering | Sales+CS | G&A | Trigger |
|---|---|---|---|---|---|
| $0 (pre-PMF) | 2-4 | 2-3 | 0 (founder sales) | 0 | n/a |
| $100k | 5-7 | 3-5 | 1 (founder + first AE) | 0-1 | first non-founder sale |
| $500k | 10-15 | 5-8 | 3-5 (1 lead + 2 AEs + 1 CSM) | 1-2 | repeatable channel |
| $1M | 15-25 | 7-12 | 5-10 (sales manager hired) | 2-3 | Rule of 3 broken |
| $3M | 25-50 | 12-20 | 10-20 (Head of GTM / VP Sales) | 4-6 | Rule of 10 broken |
| $10M | 50-100 | 20-40 | 25-50 (multiple managers, RevOps) | 8-15 | Rule of 30 broken |
| $30M | 150-300 | 50-100 | 80-150 (regions, verticals) | 20-40 | Rule of 100 broken |

## 6. Worked Example — Ugandan SaaS, Year 1 → Year 3

**Plan target:** Year 3 ARR = UGX 3 billion (~$810k). ACV = UGX 9M ($2,500). So target customer count = 333.

**Sales motion:** Solution sales, cycle 60-90 days, 5 deals/month/AE at full ramp.

**AE archetype:** SMB AE (African). Annual quota = $300k ARR = UGX 1.11 billion.

**Year 1:**
- Founder-led sales + 1 AE hired mid-year
- AE Year 1 bookings: quota $300k × attainment 50% (year 1 reality) × ramp discount average 50% = $75k = UGX 277M
- Plus founder sales: target UGX 200M
- Total Year 1 bookings: UGX 477M
- Year 1 ARR: UGX 477M

**Year 2:**
- 1 AE ramped + 2 new AEs hired at Q1 (ramped by Q4) + 1 SDR
- Ramped AE bookings: $300k × 70% attainment × 100% productivity = $210k = UGX 777M
- 2 ramping AEs: 2 × $300k × 50% × 60% (avg productivity) = $180k = UGX 666M
- Founder: tapering to UGX 100M
- Year 2 new bookings: UGX 1.54 billion
- Year 2 ending ARR: UGX 477M − Year 1 churn + UGX 1.54B = ~UGX 1.85B

**Year 3:**
- 3 ramped AEs + 2 new AEs + 1 SDR + 1 sales manager hired
- Ramped AEs: 3 × $300k × 70% = $630k = UGX 2.33B
- Ramping AEs: 2 × $300k × 50% × 50% = $150k = UGX 555M
- Year 3 new bookings: UGX 2.88B
- Plus expansion: UGX 200M
- Minus churn (15%): -UGX 277M
- Year 3 ending ARR: UGX 1.85B + UGX 2.88B + UGX 200M − UGX 277M = ~UGX 4.65B ✓ exceeds target

**Headcount end Year 3:** 5 AEs + 1 SDR + 1 manager + 2 CSMs + ~10 engineering + ~3 G&A = ~22 people.

**Fully loaded sales cost Year 3:** 5 AEs × $40k × 1.3 + 1 SDR × $25k × 1.3 + 1 manager × $80k × 1.3 + 2 CSMs × $25k × 1.3 ≈ $432k ≈ UGX 1.6B. Plus marketing, tools. Total S&M ≈ UGX 2B → ~43% of revenue. In range for Year 3 SaaS.

## 7. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Pipeline coverage (target 3-4× quota) | Weekly | Sales Manager |
| Win-rate by source / segment | Monthly | RevOps / Manager |
| Ramp progress (per new hire) | Monthly | Sales Manager + HR |
| Attainment vs plan | Monthly | VP Sales + CFO |
| Quota refresh | Annually (and at major motion change) | VP Sales + CEO + Board |
| Comp plan refresh | Annually | VP Sales + CFO + Board comp committee |
| Capacity model refresh | Quarterly | RevOps + CFO |

## 8. Africa / Uganda Application Notes

- Quotas in African markets typically 50–70% of US quotas at the same ACV due to longer sales cycles.
- Attainment realistic range: 50–65% Year 1, 60–70% Year 2+.
- Ramp time longer for African enterprise: 9–12 months for full productivity vs 6–9 in US.
- SDR economics are favourable: 1 SDR can cover 1–2 AEs sustainably; US ratio of 0.5 SDR per AE doesn't apply.
- VP Sales should not be the first sales hire in African contexts — start with a player-coach Senior AE / Sales Lead and elevate to VP at $3-5M ARR.
- Comp plans should be local-currency denominated to remove FX risk from sellers; company absorbs FX risk on USD revenues.
- Public-sector / NGO segment requires dedicated specialist AE (different sales process, procurement, contracting).
