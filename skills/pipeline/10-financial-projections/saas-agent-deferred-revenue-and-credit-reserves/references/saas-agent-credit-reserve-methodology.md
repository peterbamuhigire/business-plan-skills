---
source: ASC 606 / IFRS 15 transaction-price-reduction guidance; Big-4 SaaS interpretive practice 2024-2026; engine synthesis from agent-SLA-commercial audit (2026)
frameworks: [Trailing-ratio + forward-revenue × adjustment factor methodology; Quarterly true-up; Balance-sheet liability vs forward expected exposure; Cumulative catch-up; Sensitivity matrix]
skill: saas-agent-deferred-revenue-and-credit-reserves
cross-reference: [saas-agent-refund-reserve-methodology, saas-agent-deferred-revenue-template, saas-agent-revenue-recognition-policy-template, saas-agent-sla-cogs-policy]
---

# SLA-Credit Reserve Methodology — Formula, Worked Example, and Audit Pack

This is the methodology that auditors and DD teams will request when an agent product has contractual SLA credits.

## 1. Conceptual frame

A contractual SLA credit (a price reduction triggered by SLA breach) is **variable consideration** under ASC 606 / IFRS 15. The vendor must:

1. Estimate the variable consideration (expected SLA credits) at contract inception and reassess each reporting date
2. Apply the **constraint** — include only the amount for which it is probable / highly probable no significant reversal will occur
3. Recognise revenue **net** of the constrained expected SLA credits
4. Maintain a balance-sheet liability for SLA credits earned but not yet processed

The reserve serves both ASC 606 / IFRS 15 compliance and operational forecasting (how much margin is exposed to SLA risk).

## 2. The formula

```
Forward 12mo SLA-credit reserve estimate =
    (Trailing 12mo SLA credits issued ÷ Trailing 12mo gross agent revenue) × Forward 12mo agent revenue × Adjustment factor
```

This produces the **forward-looking exposure** the business expects to accrue over the next 12 months. It is used:

- For 3yr / 5yr projection visibility (a line in the P&L plan showing expected credits as transaction-price reduction)
- For valuation / stress sensitivity
- As the anchor for the actual **balance-sheet accrued liability** computed at each reporting date

The **balance-sheet accrued liability** at any given measurement date is:

```
Accrued liability (balance sheet) =
    SLA credits already earned in the current SLA measurement period (typically week or month) but not yet processed / issued
    + any portion of forward-12mo expected credits that have probably been triggered but not yet billed against
```

In practice for most agent businesses with weekly or monthly SLA measurement, the balance-sheet liability is small (1-2 weeks of expected credits), while the forward-12mo estimate is a much larger informational figure used for revenue-net-of-credits in the P&L plan.

## 3. The adjustment factor

The adjustment factor (typically 1.05 to 1.25) captures known forward-looking changes that the trailing ratio does not reflect:

| Driver | Direction | Typical magnitude |
|---|---|---|
| SLA-tier mix shifting toward gold | Up | +5 to +15% |
| Contract renegotiation toward tighter SLAs | Up | +5 to +20% |
| New customer cohort with weaker reliability history | Up | +5 to +25% |
| Engineering reliability investment landing | Down | -5 to -15% |
| Foundation-model upgrade improving accuracy | Down | -5 to -10% |
| Auditor-required risk margin | Up | +5 to +10% |

Combine multiplicatively. Document each driver. The auditor will challenge the factor; the documentation defends it.

## 4. Worked example

**Inputs:**
- Trailing 12mo SLA credits issued: $84,000
- Trailing 12mo gross agent revenue: $4,200,000
- Forward 12mo agent revenue projection: $6,000,000
- Adjustment factor drivers:
  - SLA-tier mix shift toward gold: +10%
  - Two new enterprise customers with stricter SLAs: +5%
  - Reliability engineering investment expected by Q3: -5%
  - Risk margin: +5%
- Combined adjustment factor: 1.10 × 1.05 × 0.95 × 1.05 = 1.151

**Computation:**
- Credit ratio = 84,000 ÷ 4,200,000 = 2.00%
- Expected forward credits (raw) = 2.00% × 6,000,000 = $120,000
- Adjusted forward credits = $120,000 × 1.151 = $138,120
- **Forward 12mo SLA-credit reserve estimate = $138,120**

**P&L treatment in the projection:**
- Gross agent revenue (year): $6,000,000
- Less expected SLA credits: ($138,120)
- Net agent revenue: $5,861,880

**Balance-sheet treatment:**
- At each month-end, calculate credits earned in the prior SLA measurement period but not yet processed: typically 1-4 weeks of credits at the run-rate.
- Run-rate = $138,120 ÷ 12 = $11,510 per month average
- Two weeks earned-not-processed = ~$5,755 accrued liability at month-end

## 5. Roll-forward template

Monthly:

| Line | Calculation | Example ($) |
|---|---|---|
| Opening accrued liability | From prior period | 5,755 |
| Add: credits earned this month | From SLA telemetry | 12,200 |
| Less: credits processed / issued | Approved credits processed | (11,800) |
| Less: credits expired / lapsed | If SLA credit expiry applies | (0) |
| Closing accrued liability | Sum | 6,155 |

Quarterly true-up:

| Line | Calculation | Example ($) |
|---|---|---|
| Trailing 12mo credit ratio (refreshed) | New trailing data | 2.05% |
| Forward 12mo revenue (refreshed) | New plan revenue | $6,250,000 |
| Forward expected credits (raw) | 2.05% × $6.25M | $128,125 |
| Adjustment factor (refreshed) | Reassessed | 1.18 |
| Forward 12mo reserve estimate | $128,125 × 1.18 | $151,188 |
| Change from prior estimate | + or - | +$13,068 |
| P&L impact (cumulative catch-up) | Catch-up via revenue line | -$13,068 to revenue |

## 6. Sensitivity matrix

Mandatory for the audit pack and the DD pack:

| Credit ratio scenario | Forward revenue | Adjustment factor | Reserve estimate |
|---|---|---|---|
| Base 2.0% | $6.0M | 1.15 | $138,000 |
| Stress: 3.0% | $6.0M | 1.20 | $216,000 |
| Catastrophic 5.0% | $6.0M | 1.30 | $390,000 |
| Improved 1.0% | $6.0M | 1.10 | $66,000 |
| Revenue stress (-20%) | $4.8M | 1.15 | $110,400 |
| Revenue upside (+20%) | $7.2M | 1.15 | $165,600 |

Each scenario maps to a specific risk: catastrophic SLA breach event; foundation-model cost shock; reliability engineering payoff; customer-mix shift.

## 7. Balance-sheet presentation

**Current liability** (settled within 12 months):
- "SLA credits accrued and unprocessed" or "Customer credit liability" line
- Typically materially smaller than the forward 12mo estimate

**Disclosure** (in audited financial statements):
- Methodology (formula + adjustment factor + reassessment cadence)
- Reserve balance opening + additions + utilisations - reversals = closing
- Variance between expected and actual in prior period
- Sensitivity at +/-1pp credit ratio
- Cumulative catch-up amounts

## 8. P&L presentation

- SLA credits are a **reduction of revenue** under ASC 606 / IFRS 15, not an operating expense
- Show as a separate line below gross revenue ("Less: SLA credits issued") and roll into net revenue
- Comparison to prior period must be visible

This is the **single most common mistake** — treating SLA credits as opex / SG&A. Auditors will require the reclassification.

## 9. Reassessment triggers (beyond the cadence)

Trigger immediate reassessment when:
- A sev-1 SLA breach event occurs
- A foundation-model cost spike shifts unit economics
- A new pricing tier with materially different SLA is launched
- A new customer cohort with materially different reliability requirements joins
- Engineering reliability changes materially (incident rate up or down)
- Contract renegotiations change SLA terms materially
- A regulator-mandated SLA standard is published

## 10. Reserve in the 3yr / 5yr projection

For each forward year:

| Year | Forward revenue | Credit ratio | Adjustment factor | Reserve estimate |
|---|---|---|---|---|
| Y1 | $6.0M | 2.0% | 1.15 | $138,000 |
| Y2 | $10.5M | 1.8% | 1.10 | $207,900 |
| Y3 | $18.0M | 1.6% | 1.10 | $316,800 |
| Y4 | $28.0M | 1.5% | 1.05 | $441,000 |
| Y5 | $42.0M | 1.4% | 1.05 | $617,400 |

Assumptions:
- Credit ratio declining as reliability matures
- Adjustment factor moderating as data improves
- Reserve growing in absolute terms with revenue

Document each assumption.

## 11. Cross-references

- Refund reserve methodology: `saas-agent-refund-reserve-methodology.md` (this directory)
- Prepaid-credit deferred revenue: `saas-agent-deferred-revenue-template.md` (this directory)
- Rev-rec policy memo: `saas-agent-revenue-recognition-policy-template.md` (this directory's sibling)
- COGS / contra-revenue policy: `saas-agent-sla-cogs-policy.md` (sibling skill)
- Stress tests: `saas-agent-sla-stress-test-scenarios.md` (meta-financial-stress-test)
- Controls: `meta-agent-sla-financial-controls/SKILL.md`

## 12. Africa / Uganda overlay

- **Local-currency reserves with USD reporting** — reserve revalues at each closing date; FX gain/loss on reserve is non-operating; document policy
- **Mobile-money settlement** — credits issued via MoMo / M-Pesa to customer carry transaction-cost; the cost reduces the value of the credit issued (and increases COGS) but does not change the SLA-credit-as-transaction-price-reduction policy
- **Public-sector customers** — credit processing through public-procurement systems can lag 60-90 days; balance-sheet liability accordingly larger
- **Reserve documentation for DFI DD** — IFC / AfDB / FMO / BII expect methodology disclosure equivalent to Big-4 standard
- **Sovereign-AI penalty clauses** — treat as SLA credits if they reduce future payments; treat as warranty if they trigger a separate cash payment; the classification matters
