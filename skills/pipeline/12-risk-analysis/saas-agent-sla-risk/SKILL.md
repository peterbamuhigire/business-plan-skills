---
name: saas-agent-sla-risk
description: Use when producing or reviewing the saas agent sla risk component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

Apply the ordered stages below; stop and recover when a stage lacks its required evidence.

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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| SLA definitions, monitoring evidence, exclusions, incident history, credit terms, dispute records, control owners, and risk appetite for saas agent sla risk | Contracts, monitoring and incident systems, customer-success records, risk owner, and finance reviewer | Yes | If absent, an SLA clock, exclusion, incident record, credit term, or control test is unavailable, mark the affected risk unassessed and withhold the claimed mitigation. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| SLA risk register with measurement, credit, dispute, concentration, control, trigger, and stress-test fields | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent sla risk exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent sla risk release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| SLA clause-to-monitor trace, incident and credit evidence, control test, residual-risk decision, and finance-review state | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent sla risk decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent sla risk review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent sla risk, the controlling focus is SLA definitions, measurement clocks, exclusions, service credits, dispute exposure, and control ownership. This skill may inspect SLA, incident, monitoring, credit, and dispute evidence in read-only mode; it may not change contracts, accept risk, issue credits, alter monitoring, or approve accounting treatment. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent sla risk, loss of evidence about SLA definitions, measurement clocks, exclusions, service credits, dispute exposure, and control ownership activates degraded mode. If the controlling saas agent sla risk evidence is unavailable, the same boundary applies. When an SLA clock, exclusion, incident record, credit term, or control test is unavailable, mark the affected risk unassessed and withhold the claimed mitigation. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent sla risk, the contractual SLA clock, monitoring clock, and customer-notification clock do not agree| reconcile the definitions, quantify credit and dispute exposure under each interpretation, and escalate the contract ambiguity | Misaligned clocks conceal liability and make control evidence unreliable |
| For saas agent sla risk, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent sla risk decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent sla risk, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete sla risk register with measurement, credit, dispute, concentration, control, trigger, and stress-test fields, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent sla risk decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect sla definitions, monitoring evidence, exclusions, incident history, credit terms, dispute records, control owners, and risk appetite and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce sla risk register with measurement, credit, dispute, concentration, control, trigger, and stress-test fields with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- SLA risk register with measurement, credit, dispute, concentration, control, trigger, and stress-test fields must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- SLA clause-to-monitor trace, incident and credit evidence, control test, residual-risk decision, and finance-review state must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent sla risk, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent sla risk, treating an unavailable sla definitions, monitoring evidence, exclusions, incident history, credit terms, dispute records, control owners, and risk appetite as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing sla risk register with measurement, credit, dispute, concentration, control, trigger, and stress-test fields that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

The SLA starts its outage clock from customer notification while monitoring detects incidents earlier. Resolve the clock, evidence source, exclusions, and credit calculation before accepting the liability estimate.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent sla risk; no local deep-dive reference is declared.
- For saas agent sla risk claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
