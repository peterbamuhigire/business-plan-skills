---
name: saas-agent-sla-economics-in-projection
description: Use when producing or reviewing the saas agent sla economics in projection component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

Apply the ordered stages below; stop and recover when a stage lacks its required evidence.

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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon for saas agent sla economics in projection | Client records, approved operating model, finance owner, and accounting doctrine | Yes | If absent, contract terms, usage evidence, framework, or cost drivers are unavailable, isolate the affected schedule, label it unassessed, and do not force the model to balance with a plug. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Integrated projections with SLA and scenario effects | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent sla economics in projection exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent sla economics in projection release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Formula trace, source/assumption register, three-statement or schedule reconciliation, and finance-gate record | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent sla economics in projection decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent sla economics in projection review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent sla economics in projection, the controlling focus is SLA credit frequency, downtime exposure, margin sensitivity, cash timing, and downside projections. This skill may inspect records and calculate planning scenarios in read-only mode; it may not post entries, change ledgers, set accounting policy, certify IFRS treatment, or release statutory values without authorised professional review. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent sla economics in projection, loss of evidence about SLA credit frequency, downtime exposure, margin sensitivity, cash timing, and downside projections activates degraded mode. If the controlling saas agent sla economics in projection evidence is unavailable, the same boundary applies. When contract terms, usage evidence, framework, or cost drivers are unavailable, isolate the affected schedule, label it unassessed, and do not force the model to balance with a plug. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent sla economics in projection, commercial billing, cash receipt, service delivery, and accounting recognition occur in different periods| model each event separately, reconcile the bridge, and route judgemental treatment to the finance reviewer | Cash, revenue, liability, and margin can be conflated into a misleading forecast |
| For saas agent sla economics in projection, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent sla economics in projection decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent sla economics in projection, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete integrated projections with sla and scenario effects, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent sla economics in projection decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce integrated projections with sla and scenario effects with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Integrated projections with SLA and scenario effects must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Formula trace, source/assumption register, three-statement or schedule reconciliation, and finance-gate record must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent sla economics in projection, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent sla economics in projection, treating an unavailable approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing integrated projections with sla and scenario effects that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A 99.9% SLA looks affordable in the base case, but one regional outage triggers credits across the largest cohort. Add frequency and concentration scenarios and show the effect on margin, cash, and funding runway.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent sla economics in projection; no local deep-dive reference is declared.
- For saas agent sla economics in projection claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
