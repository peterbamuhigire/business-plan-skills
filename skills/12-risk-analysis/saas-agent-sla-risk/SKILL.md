---
name: saas-agent-sla-risk
description: SLA-specific risk register for agent products — catastrophic SLA breach event (sev-1 mass-credit); model-cost shock making SLA-tier pricing unviable; customer-side SLA gaming (false intervention reports, false outcome rejections); regulator-mandated SLA standard; SLA-credit accrual blowing reserve; dispute backlog. Stress scenarios. Sits on top of `saas-agent-risk-and-stress-test`.
---

# SaaS Agent SLA Risk Skill

## Overview

Agent risk registers (in `saas-agent-risk-and-stress-test`) cover autonomy incidents, irreversibility incidents, tool outages, talent flight, and model deprecation. **SLA risk** is a distinct category because:

1. The risks are financial-reporting events (credits, refunds, reserves) not operational incidents
2. The risks are commercial-policy events (gaming, dispute, regulator-mandated standards) not technical events
3. The risks compound with autonomy and irreversibility risks (sev-1 SLA breach is often correlated with sev-1 autonomy incident)
4. The risks have specific reserve, control, and disclosure implications

This skill encodes the SLA risk discipline. It does not replace the agent risk register; it extends it.

## Use When

- An agent product has contractual SLA commitments
- The 3yr / 5yr plan must show SLA-risk-quantified stress scenarios
- A board / DD team has asked specifically about SLA risk
- A regulator is engaged on SLA matters
- A dispute or near-dispute has occurred and the register must be refreshed
- Cross-loaded with `saas-agent-risk-and-stress-test`, `meta-financial-stress-test`, `meta-agent-sla-financial-controls`

## Do Not Use When

- The agent product has no SLA commitments
- The plan is pre-PMF and SLA is not yet committed

## Required Inputs

- SLA schedule (uptime, response, accuracy, DoD per tier)
- Trailing SLA performance (where available)
- Reserve methodology (per `saas-agent-credit-reserve-methodology.md`)
- Refund methodology (per `saas-agent-refund-reserve-methodology.md`)
- Dispute history (where available)
- Regulator engagement record
- Insurance coverage of SLA exposure

## Workflow

### 1. Build the SLA risk register

Per `references/saas-agent-sla-risk-register.md`, populate:

| Risk | Severity | Likelihood | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|
| **Catastrophic SLA breach event** (sev-1 affecting >5% of customers) | 5 | 2 | AI Safety Lead + CTO | Eng investment in reliability; drill cadence; comms plan | Uptime trend; sev-1 incident rate | Any sev-1 affecting >5% of customers |
| **Model-cost shock breaking SLA economics** (provider raises >50% making SLA-tier unprofitable) | 4 | 3 | CFO + CTO | Vendor-cost-pass-through clauses; multi-vendor; cache; pricing adjustment | Provider pricing watch | Provider raises >25% |
| **Customer-side SLA gaming** (false intervention reports; false outcome rejections; false breach claims) | 3 | 3 | CFO + Head of CS + Legal | Audit-log evidence; dispute discipline; reserve | Dispute volume / customer | Gaming detected systemically |
| **Regulator-mandated SLA standard** (sector regulator imposes SLA terms incompatible with current pricing) | 4 | 2 | Compliance + CEO | Regulator engagement; sector dialogue | Regulator consultation publication | Mandatory standard published |
| **SLA-credit accrual blowing reserve** (actual credits >150% of reserve) | 4 | 3 | CFO + Head of Agent | Reserve methodology; quarterly true-up; adjustment factor | Monthly accrual rate | Accrual >120% reserve |
| **Refund-claim flood** (catastrophic refund wave on outcome pricing) | 4 | 2 | CFO + Head of Agent | Refund reserve; eval-loop investment; dispute mechanism | Refund rate trend | Refund rate >2x |
| **Dispute backlog** (open disputes >30, aged >14 days) | 3 | 3 | Head of CS + Legal | Dispute mechanism; response SLA; legal capacity | Open-dispute count | Backlog persistent |
| **SLA dispute → legal escalation** (single customer escalates to litigation) | 4 | 2 | Legal + CEO + CFO | Contract language; insurance; legal reserve | Pre-litigation correspondence | Demand letter |
| **Counter-party verification failure** (outcome pricing: counter-party process fails to verify outcomes) | 4 | 2 | Head of Agent + Operations | Counter-party process redundancy; verification alternatives | Verification lag trend | Verification fails |
| **SLA-tier mix collapse** (premium tiers churn while base tier stays) | 4 | 3 | Head of GTM + CFO | Premium-tier value reinforcement; CS investment | Premium-tier churn | Mix shift >10pp |
| **Foundation-model migration breaks SLA quality** (forced migration causes accuracy regression) | 4 | 3 | CTO + Head of Agent | Multi-model architecture; eval coverage; migration drills | Eval scores post-migration | Quality regression |
| **Audit-log integrity question** (audit log challenged in dispute or audit) | 4 | 2 | CTO + AI Safety Lead | Immutable audit-log; periodic integrity verification | Audit findings | Integrity challenge |
| **Insurance exclusion materialises** (SLA-related claim falls under exclusion) | 4 | 2 | CFO + Legal | Coverage review; self-insurance reserve | Insurance review findings | Claim falling under exclusion |
| **Communication failure during breach** (customer not informed; learns from outage) | 3 | 3 | Head of CS + CEO | Incident-comms plan; status-page; PR plan | Past incident comms quality | Public outcry |

### 2. Quantify the catastrophic-SLA-breach scenario

This is the headline stress scenario. Per `references/saas-agent-sla-stress-test-scenarios.md`:

**Scenario:** Single-quarter sev-1 SLA breach affecting 10% of customers.

Quantified impact:
- Credit accrual spike: 8-15% of quarterly revenue (vs 2% baseline)
- Refund spike (if outcome customers affected): 5-15% of outcome revenue
- Reserve depletion: full draw + funding need for top-up
- Customer-success cost spike: 2-3x normal CS spend in the quarter
- Legal cost spike: $50k-$200k depending on jurisdiction
- Insurance claim filing
- Reputation impact: 6-month CAC inflation (10-20% higher)
- Churn spike: +3-5pp churn following quarter
- Sales-cycle elongation: +30-50% on new logos for 2 quarters
- Investor confidence impact: monthly investor update flag; possible round delay

### 3. Quantify the model-cost-shock scenario

**Scenario:** Foundation-model provider raises pricing 50% with 30 days notice. SLA-tier pricing locked for 12 months.

Quantified impact:
- Cost-per-resolved-task rises 35-50%
- Gold-tier margin compresses from 60% to 20%
- Silver-tier margin compresses from 50% to 5%
- Bronze-tier becomes unprofitable
- Mitigation: vendor-cost-pass-through clauses (60-day notice typically)
- Bridge: cache-hit improvement; model-mix shift to cheaper models on lower-stakes steps
- Reserve drawdown if pricing renegotiation lags

### 4. Quantify the gaming scenario

**Scenario:** Customer systematically reports 30% of resolutions as failed to avoid paying.

Quantified impact:
- Revenue reduction: 30% of attributable revenue
- Dispute cost: 30 disputes / month at $200/dispute = $6,000/month legal + CS
- Reserve drawdown: refund reserve depleted
- Mitigation: audit-log evidence; dispute mechanism; contract clauses; counter-claim if egregious

### 5. Quantify the regulator-mandated-SLA scenario

**Scenario:** Sector regulator (e.g. KE financial-services AI guidance) mandates 99.95% uptime + audit-log retention 7 years + breach-disclosure within 24 hours.

Quantified impact:
- Infrastructure investment to meet uptime: $150-500k
- Audit-log retention cost increase: $30-80k / year
- Compliance staff: $80-150k / year
- Customer comms / disclosure SOP: $30-50k setup
- Customer renegotiation: SLA tightening with credit-cap renegotiation
- Time-to-comply: 6-12 months
- Implication on competitor positioning: differential compliance cost

### 6. Stress matrix combining scenarios

Per `references/saas-agent-sla-stress-test-scenarios.md`:

| Scenario | Probability (12mo) | Revenue impact | Cost impact | Reserve impact | Margin impact | Time to mitigate |
|---|---|---|---|---|---|---|
| Catastrophic SLA breach | 5-10% | -15-25% Q1; -5% Q2-Q3 | +50-100% in Q1 | Full draw + top-up | -25-40pp | 6 months |
| Model-cost shock (provider +50%) | 15-25% | 0 short-term | +35-50% | Reserve growth | -25-35pp until pass-through | 90 days |
| Customer gaming (one large customer) | 10-15% | -15-30% of that customer | +5% CS cost | Refund reserve draw | -3-5pp | 3-6 months |
| Regulator-mandated SLA | 20-40% over 24mo | 0 (mandatory) | +$200-500k | Reserve adjustment | -3-5pp | 6-12 months |
| SLA-credit reserve breach | 10-15% | 0 | 0 | Methodology revision | -2pp | 3 months |
| Dispute → litigation | 5-10% | 0 | +$50-200k | Legal reserve | -2-4pp | 12-24 months |
| Counter-party verification failure | 5-10% (per-outcome) | -30-100% on outcome stream | +$20-50k | Refund reserve draw | -10-20pp on outcome line | 3-6 months |

### 7. Wire reserves to scenarios

Cross-load with `saas-agent-deferred-revenue-and-credit-reserves`:
- SLA-credit reserve sized to cover stress scenarios
- Refund reserve sized similarly
- Reserve adequacy reassessed quarterly against stress

### 8. Wire to insurance

- AI E&O policy reviewed annually
- SLA-related coverage scope-tested
- Exclusions documented
- Self-insurance reserve sized for gap

### 9. Wire to drill cadence

Monthly SLA-defence drills:
- Simulate uptime breach + customer comms
- Simulate refund-claim handling
- Simulate dispute escalation
- Document drill outcomes

Quarterly SLA tabletop:
- Simulate catastrophic-breach scenario end-to-end
- Stakeholders: CFO, Head of CS, Legal, CTO, AI Safety Lead, CEO
- Document gaps and remediation

### 10. Wire to living-plan governance

Per cadence below.

## Quality Bar

- SLA risk register populated with all 14 standard risks
- Each risk has severity / likelihood / owner / mitigation / leading indicator / trigger
- Catastrophic-SLA-breach scenario quantified
- Model-cost-shock scenario quantified
- Gaming scenario quantified
- Regulator-mandated-SLA scenario quantified
- Stress matrix produced
- Reserve adequacy cross-referenced
- Insurance scope cross-referenced
- Drill cadence calendar
- A sceptical risk officer would accept the register

## Anti-Patterns

- "SLA breach is rare so we don't reserve" — ASC 606 / IFRS 15 require accrual on expected
- No catastrophic scenario — DD will request it
- No gaming scenario — first customer gamer catches the business unprepared
- Treating SLA risk as identical to general agent risk — different mitigations and reserves
- No drill cadence — drill exposes gaps that postmortems would otherwise expose
- Insurance assumed to cover everything — exclusions often material
- Regulator-mandated-SLA dismissed — emerging in 2026 across multiple jurisdictions
- Dispute backlog not tracked — backlog grows quietly until visible at QBR
- No connection between SLA performance and churn — operationally blind

## Outputs

- Populated SLA risk register
- Quantified stress scenarios
- Stress matrix
- Reserve cross-reference
- Insurance cross-reference
- Drill cadence calendar
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| SLA-breach incident log | continuous + weekly review | AI Safety Lead + Head of Agent | any sev-1 |
| SLA-credit accrual rate | weekly | CFO + Customer Success | >2% of agent MRR |
| Refund rate (per-outcome) | weekly | CFO + Head of Agent | +0.5pp from plan |
| Dispute open / aged | weekly | Head of CS + Legal | >5 aged >7 days |
| Reserve adequacy | monthly | CFO | actuals >110% reserve drawn |
| Provider pricing watch | monthly | Head of AI / CTO | provider raises >25% |
| Customer-gaming detection | monthly | CFO + Head of CS | gaming pattern detected |
| Regulator engagement / watch | quarterly | Compliance | new consultation |
| Insurance coverage review | semi-annually | CFO + Legal | exclusion identified |
| SLA tabletop drill | quarterly | AI Safety Lead + CEO | missed drill |
| Stress-scenario refresh | annually + trigger | CFO + AI Safety Lead | trigger |

## References

- `references/saas-agent-sla-risk-register.md` — populated risk register
- `references/saas-agent-sla-stress-test-scenarios.md` (lives under meta-financial-stress-test/references/) — stress scenarios
- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — agent risk parent
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — reserves
- `skills/10-financial-projections/saas-agent-sla-economics-in-projection/SKILL.md` — projection
- `skills/meta-agent-sla-financial-controls/SKILL.md` — controls
- `skills/meta-financial-stress-test/SKILL.md` — stress-test parent
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Mobile-money settlement-failure as SLA-breach proxy** — for per-resolution / per-outcome agents collecting through MoMo / M-Pesa, settlement failure looks like a payment-rail issue but the customer may experience it as service failure; map to SLA carefully
- **Sovereign-AI provider SLA pass-through** — if mandated in-region compute is used, the vendor's SLA depends on provider's SLA; provider-SLA-breach is an SLA-risk register item; reserve for pass-through
- **Public-sector dispute mechanism** — disputes with public-sector customers can age 90-180 days; reserve and legal capacity accordingly
- **DFI / multilateral SLA scrutiny** — IFC / AfDB / FMO / BII expect SLA register evidence in DD
- **African insurer scrutiny** — insurers vetting agent vendors as suppliers expect SLA register and reserve evidence
- **Regulator-mandated SLA emerging in Africa** — KE / NG / ZA sector regulators (CBK, CMA, CBN, SEC, SARB, FSCA) increasingly publishing AI guidance with SLA expectations
- **FX corridor in SLA-risk reserve** — local-currency reserves vs USD-cost mean reserve adequacy is FX-sensitive
- **Jobs-impact SLA risk** — public-sector deployments displacing workers carry SLA risk from political backlash; document
