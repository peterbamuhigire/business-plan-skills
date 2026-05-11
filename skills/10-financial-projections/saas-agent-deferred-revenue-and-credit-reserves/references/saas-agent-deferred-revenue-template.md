---
source: ASC 606 BC394 / IFRS 15.B46 (breakage); ASC 606-10-32-25 to -27 (significant financing component); Big-4 SaaS practice 2024-2026; engine synthesis from agent-SLA-commercial audit (2026)
frameworks: [Deferred revenue (contract liability) under ASC 606 / IFRS 15; Breakage proportional method; Significant financing component; Prepaid task-credit roll-forward]
skill: saas-agent-deferred-revenue-and-credit-reserves
cross-reference: [saas-agent-credit-reserve-methodology, saas-agent-refund-reserve-methodology, saas-agent-revenue-recognition-policy-template]
---

# Deferred Revenue Template — Prepaid Agent Task Credits and Prepaid Subscriptions

## 1. Scope

Three patterns of prepayment create deferred revenue (contract liability) for agent businesses:

1. **Prepaid task credits** — customer pays for N task credits redeemable over a defined term (e.g. 12 or 24 months)
2. **Prepaid annual SLA-tier subscription** — customer pays upfront for an annual subscription with SLA terms
3. **Prepaid platform-fee + variable success-fee hybrid** — customer prepays the platform-fee component; success-fee billed in arrears

This template covers all three.

## 2. Pattern 1 — Prepaid task credits

### Concept
Customer prepays $X for Y credits at $X/Y per credit. Credits are consumed as the customer uses the agent. Unused credits at expiry are subject to **breakage** policy.

### Day-1 entries
- Dr Cash $X
- Cr Deferred revenue (contract liability) $X

### Per period (monthly / weekly) — credit consumption
- Dr Deferred revenue (consumption × per-credit rate)
- Cr Revenue

### Breakage
Under ASC 606 BC394 and IFRS 15.B46, two methods are acceptable:

1. **Proportional method** (preferred) — recognise breakage in proportion to the consumption pattern, based on historical breakage estimate. This is the method most agent businesses adopt because credits are consumed over time, not in a single event.
2. **Remote method** — wait until exercise of the customer's remaining rights becomes remote (typically expiry). Less common; produces lumpy revenue.

**Proportional method formula:**
```
Per period breakage revenue = (Credits consumed this period × Per-credit rate) × (Breakage % / (1 - Breakage %))
```

This recognises breakage as a proportional add-on to consumption-based revenue.

### Worked example
- Customer prepays $10,000 for 4,000 credits at $2.50/credit
- Historical breakage = 8% of prepaid credits go unused
- Day 0: $10,000 deferred revenue booked

| Month | Credits consumed | Consumption revenue | Breakage revenue (proportional) | Total recognised | DR closing |
|---|---|---|---|---|---|
| 0 | - | - | - | - | 10,000 |
| 1 | 800 | 2,000.00 | 173.91 | 2,173.91 | 7,826.09 |
| 2 | 600 | 1,500.00 | 130.43 | 1,630.43 | 6,195.65 |
| 3 | 500 | 1,250.00 | 108.70 | 1,358.70 | 4,836.96 |
| 4 | 400 | 1,000.00 | 86.96 | 1,086.96 | 3,750.00 |
| 5 | 350 | 875.00 | 76.09 | 951.09 | 2,798.91 |
| 6 | 300 | 750.00 | 65.22 | 815.22 | 1,983.70 |
| 7 | 250 | 625.00 | 54.35 | 679.35 | 1,304.35 |
| 8 | 200 | 500.00 | 43.48 | 543.48 | 760.87 |
| 9 | 150 | 375.00 | 32.61 | 407.61 | 353.26 |
| 10 | 100 | 250.00 | 21.74 | 271.74 | 81.52 |
| 11 | 30 | 75.00 | 6.52 | 81.52 | 0.00 |
| Total | 3,680 (92%) | 9,200.00 | 800.00 | 10,000.00 | - |

Of the original $10,000 prepayment, $9,200 is recognised through consumption (3,680 credits × $2.50) and $800 is recognised as breakage (8% × $10,000). Total recognised reconciles to the full prepayment.

If breakage assumption proves wrong at quarter-end (e.g. actual unused turns out to be 12%), book a cumulative catch-up.

### Reassessment cadence
- Monthly: track consumption pattern; flag deviations
- Quarterly: refresh breakage assumption from historical data; book cumulative catch-up if needed
- Annually: full review with auditor

### Disclosure
- Methodology (proportional method; breakage rate; reassessment cadence)
- DR opening + new prepayments - revenue recognised - breakage - refunds (if any) = DR closing
- Variance between expected breakage and actual

## 3. Pattern 2 — Prepaid annual SLA-tier subscription

### Concept
Customer pays $X upfront for 12 months of platform access at a given SLA tier.

### Day-1 entries
- Dr Cash $X
- Cr Deferred revenue $X

### Per period (monthly)
- Dr Deferred revenue $X/12
- Cr Subscription revenue $X/12

### SLA credits
- Reduce monthly revenue as earned (see credit-reserve methodology)

### Significant financing component
ASC 606-10-32-15 to -27 / IFRS 15.60-65 — if the period between payment and service delivery exceeds 1 year, evaluate whether the contract contains a significant financing component. Annual prepaid subscriptions typically do not (12-month window is acceptable under the practical expedient); multi-year prepaid does (must be assessed).

### Worked example (annual prepaid Gold tier)
- Customer prepays $60,000 for 12 months at $5,000/month Gold tier
- Day 0: $60,000 DR
- Month 1: $5,000 recognised; less expected SLA credits ($100 estimated at 2%); net $4,900 revenue; DR $55,000
- Etc.

## 4. Pattern 3 — Hybrid platform fee prepaid + success fee in arrears

### Concept
Customer prepays the platform-fee component; success-fee is billed (and recognised) as outcomes verify.

### Treatment
- Platform fee: as Pattern 2
- Success fee: not a prepayment; variable consideration recognised at outcome verification (see rev-rec policy memo)

## 5. Balance-sheet presentation

**Current** vs **long-term** deferred revenue:
- Current = portion expected to be recognised within 12 months
- Long-term = beyond 12 months (multi-year prepaid)

Disclose split annually.

## 6. Aging analysis

Monthly: by customer / cohort, show DR aging:
- Recognised within next 3 months
- 3-6 months
- 6-12 months
- 12-24 months
- >24 months

Aging anomalies (DR growing while consumption slowing) flag customer health issues — wire to Customer Success and to churn risk.

## 7. Refunds on prepayments

If contract permits refund on unused credits:
- Refund is a **transaction-price reversal** (right of return) under ASC 606-10-55-22 / IFRS 15.B20-B27
- Maintain a refund liability separate from DR
- Estimate expected refunds using historical pattern; book as refund liability rather than DR

## 8. FX considerations (Africa / multi-currency)

- DR is denominated in the currency of the contract
- Revalue at each closing date under IAS 21 / ASC 830 if functional currency differs
- FX gain/loss on DR is non-operating; not part of revenue

## 9. VAT and tax timing (Africa overlay)

- Uganda VAT (18%): VAT-output booked on receipt of prepayment, not on credit consumption
- Kenya VAT (16%): same
- Nigeria VAT (7.5%): same
- South Africa VAT (15%): same
- Rwanda VAT (18%): same
- Reconcile VAT-output (on prepayment) with revenue recognition (on consumption) — they will diverge

## 10. Cross-references

- SLA-credit reserve: `saas-agent-credit-reserve-methodology.md`
- Refund reserve: `saas-agent-refund-reserve-methodology.md`
- Rev-rec policy memo: `saas-agent-revenue-recognition-policy-template.md`
- Controls: `meta-agent-sla-financial-controls/SKILL.md`

## 11. Africa / Uganda overlay

- **Mobile-money prepayment** — customer prepays via MoMo / M-Pesa for credits; cash settles T+0 to T+2; DR booked at settlement
- **Public-sector prepayments** — annual or multi-year prepaid via single PO; DR roll-forward critical; aging analysis must include public-sector aging which can be uneven (delivery in batches around budget cycles)
- **DFI / multilateral prepaid pilots** — milestone-paid often; treat each milestone as performance obligation if distinct; if not, prepayment with DR
- **Currency-of-record on DR** — if contract is in local currency and reporting in USD, FX-revaluation at each closing date is unavoidable
- **VAT-vs-recognition timing** — Ugandan VAT on prepayment but revenue on consumption creates a tax/accounting timing difference that requires reconciliation
- **Withholding tax on prepayments** — does not apply on receipt typically (WHT applies to payments out, not in)
