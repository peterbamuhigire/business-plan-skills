---
name: saas-agent-deferred-revenue-and-credit-reserves
description: Liability-side mechanics for agent commercial commitments — deferred revenue for prepaid task credits with breakage policy under ASC 606 BC394 / IFRS 15.B46; SLA-credit accrued liability sized from trailing SLA-credit history; refund reserve; reserve true-up cadence; balance-sheet presentation. Use whenever an agent product has prepaid credits, SLA credits, outcome refunds, or any other commercial commitment that creates a contract liability.
---

# SaaS Agent Deferred Revenue and Credit / Refund Reserves Skill

## Overview

Investors and auditors increasingly diligence the **liability side** of agent commercial commitments because that is where overstated revenue, surprise credit accruals, and reserve inadequacy show up. Three liabilities matter:

1. **Deferred revenue** for prepaid agent task credits, annual prepaid SLA-tier subscriptions, and platform-fee components billed in advance — cash received but service not yet delivered
2. **SLA-credit accrued liability** — expected future SLA credits to be issued; sized off trailing SLA-credit-issued ÷ trailing agent revenue × forward agent revenue × adjustment factor
3. **Refund reserve** — expected future refunds on failed outcomes; sized off historical refund pattern

Each has a defined methodology, a balance-sheet line, a P&L counterpart, a true-up cadence, and a disclosure obligation. Each must be auditor-acceptable. Each must be visible in the 3yr / 5yr projection.

This skill installs the discipline.

## Use When

- The agent product accepts prepaid task credits, prepaid annual SLA subscriptions, or any pre-payment
- The agent product has a contractual SLA with credits for breach
- The agent product has outcome pricing with a refund policy
- An audit firm or DD team has asked for the reserve methodology
- The 3yr / 5yr projection must show balance-sheet liabilities credibly
- The bankability scorecard checks reserve adequacy
- Cross-loaded with `saas-agent-revenue-recognition` and `saas-agent-sla-cogs-treatment`

## Do Not Use When

- The agent product is post-paid only with no SLA credits or refund commitments
- The contract has no commercial commitment that creates a liability
- The plan is pre-revenue and the liability shape is not yet committed (use directional treatment)

## Required Inputs

- Pricing primitive(s) (from `saas-agent-pricing-strategy` and `saas-agent-revenue-recognition`)
- Prepaid-credit terms (term, expiry, transferability, non-refundability)
- SLA schedule (uptime, response, accuracy thresholds; credit % per breach; credit cap; credit currency; credit expiry)
- Refund policy (when refunds apply, %, currency, processing time)
- Trailing 12-month SLA credit issued (gross) — actuals
- Trailing 12-month agent revenue (gross) — actuals
- Trailing 12-month refunds issued — actuals
- Forward 12-month agent revenue projection
- Customer-cohort behaviour on prepaid credit consumption (historical pattern of % used over months 1, 2, 3, ...)
- Credit-expiry triggers (typically 12 or 24 months)
- Audit framework (US GAAP / IFRS / local GAAP)

## Workflow

### 1. Build the prepaid-credit liability schedule

Per `references/saas-agent-deferred-revenue-template.md`:

- For each prepaid-credit contract: amount paid, credits issued, credit consumption to date, expected consumption pattern (months 1, 2, ..., N), breakage assumption
- Roll forward to each balance-sheet date: deferred revenue opening + new prepayments - credits consumed - breakage recognised = deferred revenue closing
- Each month, recognise consumed-credit revenue + proportional breakage
- Reassess breakage assumption quarterly

Worked sub-example: customer prepays $10,000 for 4,000 credits at $2.50/credit on Day 1.

| Month | Credits consumed | Revenue from consumption | Breakage recognised (proportional 8%) | DR closing |
|---|---|---|---|---|
| 0 | - | - | - | 10,000 |
| 1 | 800 | 2,000 | 174 | 7,826 |
| 2 | 600 | 1,500 | 130 | 6,196 |
| 3 | 500 | 1,250 | 109 | 4,837 |
| ... |  |  |  |  |
| 12 | 50 | 125 | 11 | 0 |

Total breakage recognised across consumption = 8% of original prepayment.

### 2. Build the SLA-credit reserve methodology

The reserve sizes the expected future SLA credits to be issued. It is an **accrued liability** on the balance sheet and a **reduction of revenue** in the P&L.

**Formula:**

```
SLA-credit reserve = (Trailing 12mo SLA credits issued ÷ Trailing 12mo gross agent revenue) × Forward agent revenue × Adjustment factor
```

Where the **adjustment factor** captures:
- Known SLA-tier mix shift (more gold-tier customers → higher accrual)
- Known SLA-tightening (contract renegotiation toward stricter SLAs)
- Known reliability improvements (engineering investment) → lower accrual
- Risk-margin (auditor-acceptable buffer for variability)

Typical adjustment factor: 1.05 to 1.25 (5-25% conservative add).

**Reassessment cadence:**
- Monthly: trailing-12mo update + ratio recomputation
- Quarterly: full true-up against actuals; adjustment-factor review
- Annually: methodology review with auditor

**Balance-sheet presentation:**
- Current-portion accrued liability (expected to be settled within 12 months)
- Long-term portion if SLA credits can roll forward beyond 12 months (uncommon)

**P&L treatment:**
- Expected SLA credits reduce revenue (transaction-price reduction under ASC 606 / IFRS 15)
- Actual SLA credits issued in the period reverse the corresponding accrual
- Variance between expected and actual flows through revenue as cumulative catch-up

**Worked example:**

Trailing 12mo SLA credits issued = $84,000
Trailing 12mo gross agent revenue = $4,200,000
Credit ratio = 2.0%
Forward 12mo agent revenue projection = $6,000,000
Expected forward credits = 2.0% × $6,000,000 = $120,000
Adjustment factor = 1.15 (SLA tightening on renewals; SLA-tier mix shifting toward gold)
SLA-credit reserve at period-end = $120,000 × 1.15 = $138,000

But this is the **forward 12mo** expected credits. The **balance-sheet liability** at period-end is the credits earned but not yet issued at the date of measurement — typically a smaller number, reflecting credits accrued in the most recent SLA measurement period (week / month). Use:

```
Balance-sheet SLA-credit liability = Credits earned in current SLA measurement period but not yet processed
```

The annual reserve concept is informational (forward-looking expected credit exposure used in valuation and stress testing); the balance-sheet liability is the unprocessed already-earned credits at the measurement date.

Document both. Auditors will ask for both.

### 3. Build the refund reserve methodology

Distinct from SLA credits because refunds typically apply to failed outcomes, not to SLA breaches on successful service.

**Formula:**

```
Refund reserve = (Trailing 12mo refunds issued ÷ Trailing 12mo gross agent revenue) × Forward agent revenue × Adjustment factor
```

With adjustment factor capturing outcome-variance and customer-acceptance trends.

**Typical refund ratios:**
- Per-resolution agent: 0.5-2% of resolved-ticket revenue
- Per-outcome agent (binary outcomes): higher variance, can be 5-15% on outcomes that fail counter-party verification
- Subscription + success: lower on subscription, similar to per-outcome on success

Reassess quarterly per `references/saas-agent-refund-reserve-methodology.md`.

### 4. Disclose the reserves transparently

The DD pack and annual financial statements should disclose:
- Methodology (formula + adjustment factor + reassessment cadence)
- Reserve balance opening + additions + utilisations - reversals = closing
- Variance between expected and actual
- Sensitivity (what reserve looks like at +/-1pp credit ratio)

### 5. Reconcile reserves to the projection

In the 3yr / 5yr projection:
- Deferred revenue line on the balance sheet rolls forward
- SLA-credit reserve grows with agent revenue at the credit-ratio + adjustment factor
- Refund reserve grows with agent revenue at the refund-ratio + adjustment factor
- The P&L line "SLA credits" and "refunds" reduce revenue contemporaneously
- The cash-flow statement shows reserve true-ups as working-capital movements

### 6. Stress-test the reserves

Per `references/saas-agent-sla-stress-test-scenarios.md` (cross-skill):
- SLA-credit ratio doubles for 1 quarter (catastrophic breach)
- Refund ratio doubles for 1 quarter (outcome regression)
- Breakage rate halves (customers consume more than expected; reserve depleted)
- Foundation-model cost spike forces SLA-tier price reduction → narrower margin → larger reserve needed
- Customer-cohort dispute pattern shifts

For each: how much does the reserve need to scale? Is the engineering / GTM response timed?

### 7. Wire to financial controls

Per `meta-agent-sla-financial-controls`:
- Credit-issuance approval workflow (who approves what level)
- Reserve methodology documentation reviewed by auditor
- Audit trail of credits issued
- Segregation of duties on credit issuance vs reserve true-up
- SOC1-style control evidence

### 8. Wire to living-plan governance

Per cadence table below.

## Quality Bar

- Each liability (deferred revenue, SLA-credit reserve, refund reserve) has a documented methodology
- Methodology formula is explicit with named variables
- Adjustment factor is justified (not arbitrary)
- Trailing-12mo actuals support the ratio (12 months minimum; auditor may require longer)
- Reassessment cadence is named with owner
- Balance-sheet presentation is correct (current vs long-term)
- P&L impact is named (transaction-price reduction; not opex)
- Disclosure draft language is in the policy memo
- Reserves reconcile to the projection
- Stress-tested under shock scenarios
- Auditor pre-review obtained where possible
- A sceptical CFO at a Series B agent business would accept the methodology

## Anti-Patterns

- "We'll reserve when we have to" — ASC 606 / IFRS 15 require accrual when expected
- Treating SLA credits as a marketing expense — wrong; they are a transaction-price reduction
- Treating refunds as a contra-COGS item — wrong; transaction-price reduction
- Reserve held at flat 2% with no methodology — auditors and DD will challenge
- No adjustment factor — over-reliance on historical run-rate when future is structurally different
- Breakage recognised at expiry only (lump) — wrong under ASC 606 / IFRS 15; proportional method required (in most cases)
- Reserve methodology in a footnote, not in the policy memo — fails disclosure quality
- Reserve reassessment annual only — too slow; quarterly minimum
- No segregation of duties between credit issuance and reserve accounting — control weakness
- Long-term prepaid credits booked as current deferred revenue — balance-sheet misclassification
- Reserve ignored in stress test — overstates resilience

## Outputs

- Deferred revenue schedule with breakage policy
- SLA-credit reserve methodology + worked example + roll-forward
- Refund reserve methodology + worked example
- Reassessment cadence calendar
- Balance-sheet presentation + P&L reconciliation
- Stress-test of reserves
- Cross-reference to rev-rec policy memo
- Cross-reference to SLA-COGS policy
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| SLA-credit accrual rate (% of agent MRR) | weekly | CFO + Customer Success | >2% accrual rate |
| SLA-credit reserve adequacy (actual vs reserve drawn) | monthly | CFO | actual >110% of reserve drawn |
| Refund reserve adequacy | monthly | CFO | actual >110% of reserve drawn |
| Breakage assumption | quarterly | Controller | shift in historical pattern |
| Reserve methodology true-up | quarterly | CFO + Controller + Auditor | methodology assumption change |
| Reserve roll-forward | monthly | Controller | unexplained variance |
| Deferred-revenue waterfall (aging) | monthly | Controller | aging anomaly |
| Credit-issuance audit trail | weekly | Controller | missing approval |
| Reserve full methodology review | annually | CFO + Auditor | always |

## References

- `references/saas-agent-deferred-revenue-template.md` — prepaid task-credit template
- `references/saas-agent-credit-reserve-methodology.md` — SLA-credit reserve formula and worked example
- `references/saas-agent-refund-reserve-methodology.md` — refund reserve formula
- `skills/10-financial-projections/saas-agent-revenue-recognition/SKILL.md` — recognition side
- `skills/10-financial-projections/saas-agent-sla-cogs-treatment/SKILL.md` — COGS / contra-revenue split
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — cost waterfall
- `skills/meta-agent-revenue-recognition-policy/SKILL.md` — policy discipline
- `skills/meta-agent-sla-financial-controls/SKILL.md` — controls
- `skills/meta-living-plan-governance/SKILL.md` — governance parent
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit
- `book-extractions/accounting-bookkeeping-finance-controls-extraction.md` — controls reference

## Africa / Uganda Application Notes

- **Currency-of-record on reserves** — SLA-credit reserves and refund reserves in agent contracts denominated in local currency must be revalued at each closing date under IAS 21 / ASC 830 when reporting currency differs (USD reporting common in African agent businesses with US / EU investors).
- **Mobile-money settlement** — for per-resolution micro-billing, the cash arrives T+0 to T+2; deferred revenue concept generally does not apply (services delivered before settlement); but prepaid task-credit packages purchased via MoMo / M-Pesa create deferred revenue immediately at settlement.
- **VAT on prepaid credits** — Uganda VAT (18%) treats prepayment as taxable supply on receipt; VAT-output booked on prepayment, not on credit consumption; reconcile VAT-output with deferred-revenue recognition.
- **Public-sector contracts** — often pay in advance (annual lump) creating large deferred-revenue balances; consumption pattern is uneven; breakage rare (public-sector usually consumes); methodology reassessment necessary.
- **DFI / multilateral funded customers** — sometimes prepay multi-year; long-term deferred revenue line; auditor will reclassify current vs long-term annually.
- **Local audit firms** — may need methodology coaching; provide the worked example.
- **Reserve currency** — USD-denominated cost with local-currency revenue creates asymmetric reserves; if SLA credits are in local currency but the cost saved by reserve depletion is in USD, reserve adequacy in real terms is FX-sensitive. Document FX-stress scenarios on reserve adequacy.
- **Mobile-money refund cost** — refunding via MoMo / M-Pesa carries 1-2.5% transaction fee; refund reserve methodology should include the refund-cost line.
- **Sovereign-AI contracts** — may include indemnity / penalty clauses that effectively act like SLA credits; classify and reserve accordingly.
