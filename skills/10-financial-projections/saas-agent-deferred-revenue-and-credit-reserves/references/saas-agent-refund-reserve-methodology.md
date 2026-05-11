---
source: ASC 606 / IFRS 15 right-of-return and refund-liability guidance; Big-4 SaaS practice 2024-2026; engine synthesis from agent-SLA-commercial audit (2026)
frameworks: [Right-of-return / refund liability under ASC 606-10-55-22 / IFRS 15.B20-B27; Refund-ratio + adjustment-factor methodology; Per-pricing-primitive refund reserves]
skill: saas-agent-deferred-revenue-and-credit-reserves
cross-reference: [saas-agent-credit-reserve-methodology, saas-agent-revenue-recognition-policy-template, saas-agent-sla-cogs-policy]
---

# Refund Reserve Methodology — Distinct from SLA Credits

## 1. Why refund reserve is a separate liability from SLA credits

SLA credits are price reductions triggered by **SLA-breach events on otherwise-successful services** (uptime, response-time, accuracy thresholds). Refunds are price reversals for **failed outcomes** (the agent did not deliver the promised resolution / outcome / task at all, or the counter-party rejected it).

The accounting treatment converges (both reduce transaction price under ASC 606 / IFRS 15) but the **operational drivers** and **risk profile** are different:

- SLA-credit ratios are largely engineering-driven (reliability, response, accuracy)
- Refund ratios are largely outcome-driven (binary success/fail; counter-party verification result)
- SLA credits are typically capped contractually (e.g. max 25% of monthly fee)
- Refunds can be uncapped on outcome pricing

Maintain the two reserves separately. Disclose them separately.

## 2. The formula

```
Forward 12mo refund reserve estimate =
    (Trailing 12mo refunds issued ÷ Trailing 12mo gross agent revenue) × Forward 12mo agent revenue × Adjustment factor
```

By **pricing primitive** because refund ratios diverge sharply:

| Primitive | Typical refund ratio | Notes |
|---|---|---|
| Per-resolution | 0.5-2.0% | Tickets rejected by customer within rejection window |
| Per-outcome (DoD verified) | 5-15% | Outcome variance; counter-party rejection |
| Subscription + success fee | <1% on subscription; per-outcome rate on success fee | Two components |
| Prepaid credits | Negligible (credits typically non-refundable) | Disclose policy |
| SLA-tier subscription | Typically not refundable; SLA credit instead | Disclose |

Compute by primitive and aggregate.

## 3. The adjustment factor for refunds

| Driver | Direction | Typical |
|---|---|---|
| Outcome variance trending up | Up | +5 to +20% |
| New, untested customer cohort | Up | +10 to +30% |
| Counter-party process change (e.g. payer reimbursement rules) | Up or down | ±10 to ±30% |
| Eval-loop improvements landing | Down | -5 to -15% |
| New action class with unverified DoD | Up | +20 to +50% |
| Risk margin | Up | +5 to +10% |

## 4. Worked example (per-outcome agent)

**Inputs:**
- Trailing 12mo refunds issued: $96,000
- Trailing 12mo gross per-outcome revenue: $1,200,000
- Forward 12mo per-outcome revenue: $1,800,000
- Adjustment factors:
  - Counter-party (payer) rule tightening: +15%
  - Eval improvements expected by Q2: -5%
  - Risk margin: +5%
- Combined: 1.15 × 0.95 × 1.05 = 1.147

**Computation:**
- Refund ratio = 96,000 ÷ 1,200,000 = 8.0%
- Expected forward refunds (raw) = 8.0% × 1,800,000 = $144,000
- Adjusted forward refunds = $144,000 × 1.147 = $165,168
- **Forward 12mo refund reserve estimate = $165,168**

**P&L treatment:**
- Per-outcome gross revenue: $1,800,000
- Less expected refunds: ($165,168)
- Per-outcome net revenue: $1,634,832

**Balance-sheet treatment:**
- "Customer refund liability" line
- Closing balance = refunds earned but not yet processed at measurement date

## 5. Reassessment cadence

| Cadence | Action | Owner |
|---|---|---|
| Weekly | Refund queue depth and dispute count | Customer Success |
| Monthly | Refund-ratio recompute (trailing) | Controller + CFO |
| Monthly | Reserve adequacy review | Controller + CFO |
| Quarterly | Methodology + adjustment-factor true-up | CFO + Controller + Auditor |
| Annually | Methodology review with auditor | CFO + Auditor |

## 6. Refund processing controls

- Approval thresholds: small refunds (e.g. <$500) by Customer Success Manager; medium ($500-$5,000) by Head of CS; large (>$5,000) by CFO
- Audit trail: every refund logged with reason code, customer, amount, currency, approval chain, processing date
- Segregation: refund issuance and reserve accounting are separate roles
- Aging: refunds requested but not processed are aged; backlog >7 days triggers escalation
- Reconciliation: refunds processed reconcile with reserve drawdowns and bank/mobile-money outflows

## 7. P&L presentation

- **Reduction of revenue** under ASC 606 / IFRS 15
- Show as a separate line below gross revenue ("Less: refunds issued")
- The refund line is distinct from the SLA-credit line; both visible

## 8. Stress sensitivity

| Refund-ratio scenario | Forward revenue | Adjustment | Reserve |
|---|---|---|---|
| Base 8% | $1.8M | 1.15 | $165,600 |
| Stress 12% | $1.8M | 1.20 | $259,200 |
| Catastrophic 20% | $1.8M | 1.30 | $468,000 |
| Improved 5% | $1.8M | 1.10 | $99,000 |
| Per-outcome volume +30% | $2.34M | 1.15 | $215,280 |

## 9. Cross-references

- SLA-credit reserve: `saas-agent-credit-reserve-methodology.md`
- Prepaid deferred revenue: `saas-agent-deferred-revenue-template.md`
- Rev-rec policy memo: `saas-agent-revenue-recognition-policy-template.md`
- COGS / contra-revenue policy: `saas-agent-sla-cogs-policy.md`

## 10. Africa / Uganda overlay

- **Mobile-money refund cost** — MoMo / M-Pesa / Airtel Money / Wave / Orange Money refund transactions cost 1-2.5%; the cost is COGS / opex (refund-processing cost), not a reduction of the refund amount itself
- **Refund timing under public-sector procurement** — public-sector refunds can take 60-180 days; balance-sheet refund liability accordingly larger
- **Currency** — refunds in local currency where revenue was local; in USD where revenue was USD; document policy
- **Counter-party verification in African contexts** — collections agents on per-outcome pricing depend on counter-party (debtor) payment confirmation; mobile-money settlement is the verification trigger; document the chain
- **DFI customer refund policy** — DFI / multilateral customers typically prefer SLA credits over refunds (auditing simpler); negotiate refund avoidance where possible
