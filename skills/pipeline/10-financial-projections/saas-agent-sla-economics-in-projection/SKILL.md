---
name: saas-agent-sla-economics-in-projection
description: Wire SLA performance into the 3yr / 5yr financial projection — SLA-breach scenarios feed revenue (credit cost), risk register (reputational), churn (SLA performance as leading indicator of churn), and funding need (reserve drawdown). Model SLA-tier mix evolution, cost-of-quality assumptions, and SLA performance as an integrated projection driver, not a one-time risk event.
---

# SaaS Agent SLA Economics in Projection Skill

## Overview

Standard SaaS projections treat SLA breach as a one-time risk event in Section 12. For agent businesses with measurable, breachable SLAs that drive material revenue exposure, **SLA performance is an integrated projection driver**, not a risk-page footnote.

The 3yr / 5yr plan must model:

1. **SLA-credit accrual** as a revenue-reduction line tied to credit ratio × revenue (per `saas-agent-credit-reserve-methodology.md`)
2. **Refund accrual** as a revenue-reduction line tied to refund ratio × revenue
3. **SLA-tier mix evolution** (bronze / silver / gold mix shifts over the projection horizon)
4. **Cost-of-quality investment** (engineering reliability investment expected to drive credit ratio down; eval-loop investment expected to drive refund ratio down)
5. **SLA performance as leading indicator of churn** (poor SLA → churn risk increase one quarter forward)
6. **Reserve drawdown scenarios** and their funding implications
7. **Catastrophic SLA breach** scenarios where credit accrual exceeds reserve and the cash impact is direct

A plan that does not model these lines is operationally blind to a material risk and a material lever.

## Use When

- A 3yr / 5yr projection for an agent product with SLA commitments is being built
- The projection is for investor / lender / DFI submission and must reconcile to operational reality
- An agent business is reporting to a board and the SLA economics question recurs
- Cross-loaded with `saas-agent-revenue-recognition`, `saas-agent-deferred-revenue-and-credit-reserves`, `saas-agent-sla-cogs-treatment`, and `meta-financial-stress-test`

## Do Not Use When

- The agent product has no SLA commitments (use standard `10-financial-projections`)
- The plan is pre-PMF and the SLA shape is not yet committed (use directional treatment with assumption flag)

## Required Inputs

- Pricing primitives (from `saas-agent-pricing-strategy`)
- SLA tier structure if applicable (bronze / silver / gold thresholds + prices + credit terms)
- Historical SLA performance (uptime %, response time, accuracy, DoD compliance) if any
- Trailing SLA-credit ratio and refund ratio (per `saas-agent-credit-reserve-methodology.md`)
- Reliability engineering roadmap (planned investments and expected impact)
- Eval-loop investment roadmap
- Customer-mix trajectory (SLA-tier mix evolution)
- Churn data segmented by SLA performance (where available)
- Reserve balances and methodology

## Workflow

### 1. Build the SLA-line projection in the P&L

For each forward year, populate:

| Line | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Gross agent revenue | (driver-based) | (driver-based) | etc. |  |  |
| SLA credit ratio (% of gross) | 2.0% | 1.8% | 1.6% | 1.5% | 1.4% |
| SLA credits (revenue reduction) | (computed) | (computed) | etc. |  |  |
| Refund ratio (% of gross) | 1.2% | 1.0% | 0.9% | 0.8% | 0.8% |
| Refunds (revenue reduction) | (computed) | etc. |  |  |  |
| Net agent revenue | (computed) | etc. |  |  |  |

The ratios must reconcile to the engineering and eval-loop investment plan — improving credit ratio assumes the investment lands.

### 2. Build the SLA-tier mix projection

For tiered offerings:

| Tier | Year 1 mix | Year 2 mix | Year 3 mix | Notes |
|---|---|---|---|---|
| Bronze (80% uptime / standard accuracy) | 60% | 50% | 40% | Eroding as customers upgrade |
| Silver (99% uptime / improved accuracy) | 30% | 35% | 40% | Growing |
| Gold (99.9% uptime / 95% accuracy / 1-hour response) | 10% | 15% | 20% | Premium expansion |

Mix shifts drive:
- ARPU (higher tier = higher price)
- Credit-ratio exposure (gold tier has stricter SLAs and higher credit cap)
- Margin (gold tier needs more reliable infrastructure)

### 3. Build the cost-of-quality investment line

Capital and operating investment in reliability:

| Investment | Year 1 | Year 2 | Year 3 | Expected impact |
|---|---|---|---|---|
| Reliability engineering FTEs | $200k | $400k | $500k | Credit ratio -0.3pp by Y2 |
| Eval-loop platform | $80k | $120k | $150k | Refund ratio -0.4pp by Y2 |
| Audit-log infrastructure | $30k | $40k | $50k | Sustains SLA-monitoring |
| SLA-monitoring tooling | $40k | $50k | $60k | Detection + alerting |
| Total cost-of-quality | $350k | $610k | $760k |  |

These flow through COGS or R&D per the SLA-COGS policy.

### 4. Wire SLA performance to churn

SLA performance is a **leading indicator of churn** — customers experiencing repeated SLA breaches churn at materially higher rates 1-2 quarters forward. Model:

- Customers with 0 SLA breaches in trailing quarter: base churn rate (e.g. 1.5%)
- Customers with 1-2 SLA breaches: +1pp churn (2.5%)
- Customers with 3+ SLA breaches: +3pp churn (4.5%)
- Customers with sev-1 SLA breach: +5pp churn (6.5%)

Project the SLA-breach distribution over the horizon. Compute the SLA-driven churn premium and add to base churn.

This makes SLA performance a driver of NRR, not a side-effect.

### 5. Build the reserve drawdown sensitivity

For each year:
- Forward 12mo expected credits (per credit-reserve methodology)
- Reserve balance projected
- Cumulative reserve drawdown
- Cash impact of reserve drawdown (where credits paid out vs accrued)

If reserve drawdown projected to exceed reserve balance in any year, document the funding gap and the mitigation.

### 6. Build the catastrophic-SLA-breach scenario

A single-quarter sev-1 SLA breach affecting >5% of customers:

- Credit accrual spikes to 5-15% of quarterly revenue
- Refund spike if affected customers also fail outcomes
- Reserve depleted; cash impact direct
- Customer-success cost spike (dispute handling)
- Legal cost spike
- Reputational impact: 6-month customer-acquisition slowdown
- Churn spike following quarter

Quantify each line. This is the stress scenario the DD and board pack will reference.

### 7. Build the SLA-driven funding need

If reserve depletion and catastrophic scenario combined create a funding need, that need flows into:
- Section 11 funding request
- Use-of-proceeds (reserve replenishment)
- Risk register
- Investor narrative

### 8. Model the SLA-quality flywheel

Strong SLA performance → premium positioning → win rate up → SLA-tier mix shifts toward gold → margin pressure but ARPU up → reliability investment funded → SLA performance further strengthens → defensible moat element.

Project the flywheel KPIs:
- Win rate on SLA-bearing deals
- Gold-tier attach rate among new logos
- SLA performance trend (uptime, accuracy)
- Customer references quoting SLA performance

### 9. Wire to bankability, valuation, and investor reporting

- Bankability: SLA performance is a scorecard item (`saas-agent-sla-bankability-checklist.md`)
- Valuation: SLA quality is a valuation overlay (`saas-agent-sla-valuation-adjustments.md`)
- Reporting: SLA is a monthly investor update + board pack item (`saas-agent-sla-board-block.md`)

### 10. Wire to living-plan governance

Per cadence below.

## Quality Bar

- SLA-credit and refund lines explicit in P&L projection
- SLA-tier mix evolution projected
- Cost-of-quality investment line projected with expected impact
- SLA-driven churn premium modelled
- Reserve drawdown sensitivity shown
- Catastrophic-SLA-breach scenario quantified
- SLA-quality flywheel KPIs defined
- Cross-references to bankability / valuation / reporting consistent
- A sceptical board chair would accept the model as operationally honest

## Anti-Patterns

- "SLA breach is in Section 12" — yes, but it must also be in Section 10
- Flat SLA-credit ratio across all 5 years — implausible; either investment improves it or risk worsens it
- No SLA-tier mix evolution — leaves ARPU and margin static
- No cost-of-quality investment — implies the credit ratio improves by magic
- No SLA-driven churn premium — disconnects SLA performance from NRR
- Reserve depletion ignored in funding need — funding gap hidden
- Catastrophic scenario not quantified — stress test toothless
- SLA as a marketing claim, not a financial driver — misses the moat

## Outputs

- SLA-line projection (credit + refund + net revenue)
- SLA-tier mix projection
- Cost-of-quality investment plan
- SLA-driven churn premium model
- Reserve drawdown sensitivity
- Catastrophic-SLA-breach scenario
- SLA-quality flywheel KPIs
- Cross-reference to bankability / valuation / reporting
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| SLA-credit ratio (actual vs projected) | monthly | CFO + Head of Agent | >0.5pp variance |
| Refund ratio (actual vs projected) | monthly | CFO + Head of Agent | >0.5pp variance |
| SLA-tier mix (actual vs projected) | quarterly | Head of GTM + CFO | mix shift >5pp |
| Cost-of-quality investment vs plan | quarterly | CFO + CTO | >10% variance |
| SLA-driven churn premium calibration | quarterly | Head of CS + Data | premium drifts |
| Reserve drawdown vs plan | monthly | CFO | drawdown >110% projected |
| SLA-quality flywheel KPIs | quarterly | CEO + Head of GTM | flywheel reversing |
| Catastrophic-scenario refresh | annually + on trigger | CFO + CEO + AI Safety Lead | trigger |

## References

- `references/saas-agent-sla-projection-template.md` — worked 5-year projection extract
- `skills/10-financial-projections/saas-agent-revenue-recognition/SKILL.md` — rev-rec side
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — reserve side
- `skills/10-financial-projections/saas-agent-sla-cogs-treatment/SKILL.md` — COGS side
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — unit economics
- `skills/12-risk-analysis/saas-agent-sla-risk/SKILL.md` — risk register consumer
- `skills/meta-financial-stress-test/SKILL.md` — stress-test consumer
- `skills/meta-agent-valuation-overlay-for-sla/SKILL.md` — valuation
- `skills/meta-agent-board-and-investor-reporting/SKILL.md` — reporting
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **FX corridor impact on SLA economics** — USD-denominated cost meets local-currency revenue; +/-20% FX swing changes the breakeven SLA credit ratio; model FX scenarios on SLA economics, not just on cost
- **Mobile-money cash-vs-revenue** — per-resolution agent revenue collected via MoMo / M-Pesa settles T+0 to T+2; SLA credits issued in local currency depend on the same rail; reconcile daily
- **Sovereign-AI compute SLA chain** — if in-region compute (Cassava, Liquid, Raxio, MTN AI Factories) is mandated, the vendor's SLA depends on the provider's SLA; model provider-SLA-breach pass-through scenarios
- **Public-sector SLA expectations** — KE Huduma, NG NIMC, UG NITA-U increasingly include SLA schedules in tenders; project SLA-tier mix as more public-sector wins land
- **DFI / multilateral customer SLA** — milestone-paid often; SLA tied to milestone delivery; model milestone-failure scenario
- **African insurer / regulated-sector adoption** — SLA discipline is a buying criterion; project SLA-quality flywheel as enabling regulated-sector expansion
- **Local-talent reliability engineering** — Tool Engineer + Eval Engineer roles in Uganda / Kenya / Nigeria fully loaded USD 2,500-9,500 / month; cost-of-quality investment scales differently from US benchmarks
- **Regulator-mandated SLA risk** — emerging in KE / NG / ZA financial-services AI; project regulatory-SLA-imposition scenario
