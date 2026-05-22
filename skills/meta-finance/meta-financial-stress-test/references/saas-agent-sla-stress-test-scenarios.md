---
source: Agent SLA + commercial business-plan audit (2026); engine synthesis
frameworks: [SLA stress-test scenario set; financial impact ledger; reserve adequacy under stress]
skill: meta-financial-stress-test
cross-reference: [saas-agent-sla-risk, saas-agent-deferred-revenue-and-credit-reserves, saas-agent-sla-economics-in-projection, meta-agent-sla-financial-controls]
---

# SaaS Agent SLA Stress-Test Scenarios

Eight standardised SLA-stress scenarios for agent businesses with SLA commitments. Each scenario specifies trigger, mechanic, financial impact, reserve adequacy, control trigger, and recovery path. Use in `meta-financial-stress-test`-driven projection and DD prep.

Scoring conventions: severity (1-5), recovery horizon (months), pre-money valuation hit (% of base multiple).

---

## Scenario A — Catastrophic SLA Breach (sev-1 mass-credit)

**Trigger.** Foundation-model outage or tool-partner outage or sovereign-AI provider outage lasting >6 hours during business window; >5% of customers experience SLA breach simultaneously.

**Mechanic.** SLA-credit accrual spikes 5-15x trailing-quarter baseline in one month. Customer-success queue saturates. Dispute backlog forms. Reputational signal in industry press.

**Financial impact.**
- SLA-credit cost: 8-25% of monthly agent revenue (event month)
- Refund cost (if outcome pricing): additional 3-10%
- Customer-success overhead: +30-50% short-term
- Churn signal: 1-3% trailing-quarter churn lift attributable to event
- Reserve depletion: 60-120% of provisioned SLA-credit reserve

**Reserve adequacy.** Reserve sized at trailing 4-quarter credit ratio × 1.5 (catastrophic factor) typically covers one event; second event in same year exceeds reserve.

**Control trigger.** CFO + CEO + Board notification within 24 hours of event; auditor notification if event-month credits >120% reserve; insurance carrier notification per policy.

**Recovery horizon.** 2-4 months for reserve replenishment + 6-12 months for churn signal to clear.

**Pre-money valuation hit.** -5 to -15% if isolated event with strong RCA; -15 to -30% if pattern.

**Severity.** 5.

---

## Scenario B — Foundation-Model Cost Shock at Provider 2x

**Trigger.** Blended foundation-model cost rises 100% (provider repricing; model deprecation forcing migration; usage-mix shift to more expensive model).

**Mechanic.** Cost-per-resolved-task doubles in the affected cost component. Margin compresses or inverts on contracts lacking vendor-cost pass-through clause.

**Financial impact.**
- Agent gross margin: -10 to -25pp on affected revenue
- Contract repricing fights with 30-60% of customer base
- Customer churn signal: 2-5% if repricing demand is steep
- Vendor-cost pass-through trigger fires on contracts that have the clause

**Reserve adequacy.** Margin reserve where contracts lack pass-through; SLA-credit reserve unaffected directly but indirect impact if cost-of-quality investment is cut to defend margin.

**Control trigger.** Provider-cost watch fires at >25% YoY; CFO + CTO joint review; renewable-contract repricing trigger executed.

**Recovery horizon.** 3-9 months for contract repricing cycle to complete.

**Pre-money valuation hit.** -10 to -25% depending on contract-coverage of pass-through clauses.

**Severity.** 4.

---

## Scenario C — Customer-Side SLA Gaming (revenue leakage 10%)

**Trigger.** Customer staff or vendor-management function inflate intervention reports or reject outcomes systematically; trailing-quarter intervention rate or rejection rate at a customer cohort drifts +5pp vs other cohorts.

**Mechanic.** Effective billing falls; SLA-credit accrual rises; gross revenue overstated if not investigated.

**Financial impact.**
- Revenue leakage: 5-15% of affected customers' billing
- Dispute / investigation overhead: 0.5-1 FTE per dispute cluster
- Customer-relationship cost: variable
- Audit-firm comment if pattern undetected: material control deficiency

**Reserve adequacy.** Refund reserve absorbs initial leakage; pattern-detection control should fire before reserve depletes.

**Control trigger.** Gaming-detection metric (deviation from cohort) flags monthly; CFO + Head of CS investigation; dispute-escalation path.

**Recovery horizon.** 2-6 months for investigation + customer-engagement + contract clarification.

**Pre-money valuation hit.** -5 to -15% depending on gaming-detection control maturity.

**Severity.** 3.

---

## Scenario D — Regulator-Mandated SLA Tightening

**Trigger.** Sector regulator publishes SLA standard tighter than current commitments (e.g. CBK / CBN / SARB / FCA / OCC / SEC mandate uptime ≥99.9% for AI in regulated workflows).

**Mechanic.** Cost-of-quality investment required (additional monitoring; redundancy; HITL coverage). Renewable contracts upgrade at renewal; non-renewable contracts subsidise gap until renewal.

**Financial impact.**
- Cost-of-quality investment: 2-8% of agent revenue (one-time) + 0.5-2% (recurring)
- Margin compression: 2-5pp on non-renewable contract subsidy
- Regulatory penalty risk if non-compliant: variable, potentially material

**Reserve adequacy.** Forward cost-of-quality reserve in projection; existing reserves unaffected unless penalty risk crystallises.

**Control trigger.** Regulator-engagement quarterly review flags consultation; General Counsel + CFO assess impact; forward budget set.

**Recovery horizon.** 6-18 months for upgrade rollout and contract repricing.

**Pre-money valuation hit.** -5 to -15% if engagement weak; neutral to +5% if engagement strong (signals operational maturity).

**Severity.** 3.

---

## Scenario E — SLA-Credit Accrual Blowing Reserve

**Trigger.** Trailing 3-month SLA credits >120% of reserve drawn; reserve methodology stale; trend deteriorating.

**Mechanic.** P&L surprise at quarter close; auditor concern; reserve methodology must be re-cut; pre-money valuation question.

**Financial impact.**
- P&L variance: 2-8% of agent revenue (quarter)
- Auditor-engagement overhead
- Investor-narrative damage; valuation overlay shift

**Reserve adequacy.** Methodology re-cut with auditor concurrence; new reserve level provisioned; backstop from operating cash if needed.

**Control trigger.** Monthly reserve-adequacy review fires at >110%; quarterly true-up scheduled at >115%; Board notification at >120%.

**Recovery horizon.** 1-3 months for reserve re-cut; 6-12 months for methodology credibility to rebuild with investors.

**Pre-money valuation hit.** -10 to -25%.

**Severity.** 4.

---

## Scenario F — Outcome-Pricing Refund Cascade

**Trigger.** Per-outcome agent product faces systematic downstream-verification rejection; refund accrual spikes; refund reserve depletes.

**Mechanic.** Outcome-definition ambiguity or counter-party-verification weakness drives cascade; revenue recognised in prior quarters becomes refundable.

**Financial impact.**
- Refund cost: 5-20% of outcome-priced revenue
- Revenue restatement risk if material
- Customer-relationship damage; potential litigation if disputes harden

**Reserve adequacy.** Refund reserve sized to handle one quarter of normal refund rate × 2; cascade typically exceeds.

**Control trigger.** Outcome-rejection-rate monthly variance fires; CFO + Head of GTM + General Counsel review; outcome-definition emergency clarification.

**Recovery horizon.** 3-9 months for outcome-definition correction + refund-reserve replenishment.

**Pre-money valuation hit.** -10 to -30% (rev-rec credibility hit is severe).

**Severity.** 4-5.

---

## Scenario G — Insurance Carrier Exclusion Expansion

**Trigger.** AI E&O / cyber / business-interruption carrier expands exclusions at renewal to remove SLA-credit / refund coverage; previously-covered risk becomes uncovered.

**Mechanic.** Self-insurance reserve must absorb previously-transferred risk; either reserve provisioning rises or risk appetite contracts.

**Financial impact.**
- Self-insurance reserve uplift: 1-4% of agent revenue
- Premium re-negotiation; potentially carrier change
- Reduced risk-transfer capacity

**Reserve adequacy.** Self-insurance reserve typically sub-scale at early stage; uplift can absorb 1-3 months of operating cash.

**Control trigger.** Annual carrier review with broker; semi-annual review of exclusion landscape.

**Recovery horizon.** Renewal cycle (12 months) for alternative carrier; reserve uplift immediate.

**Pre-money valuation hit.** -2 to -10%.

**Severity.** 2-3.

---

## Scenario H — Sovereign-AI Provider SLA Pass-Through Breach

**Trigger.** Mandated in-region compute provider (af-south-1, africa-south1, Cassava, Liquid, Raxio, MTN AI Factories, Ethiopian AI Institute, etc.) experiences outage; vendor's SLA breaches by pass-through.

**Mechanic.** Vendor liability accrues to customer despite provider being root cause; customer may demand credit irrespective of provider's SLA terms; recovery from provider is slow.

**Financial impact.**
- Pass-through credit cost: 5-15% of affected customer revenue
- Cash conversion delay (provider reimbursement lag)
- Customer relationship cost; reputational

**Reserve adequacy.** Provider-pass-through reserve typically thin; first event often exceeds.

**Control trigger.** Provider-outage monitoring 24/7; CFO + CTO + customer-comms within hours.

**Recovery horizon.** 1-6 months for credit settlement + provider reimbursement; longer if provider disputes.

**Pre-money valuation hit.** -5 to -15% (sovereign-AI dependency is a known investor concern).

**Severity.** 3-4.

---

## Financial-Impact Ledger Summary

| Scenario | Severity | Likelihood (annual) | Revenue impact | Reserve impact | Valuation hit | Recovery |
|---|---|---|---|---|---|---|
| A. Catastrophic SLA breach | 5 | 20-30% | 8-25% month | 60-120% reserve | -5 to -30% | 2-12 mo |
| B. Foundation-model cost shock 2x | 4 | 20-40% | margin -10-25pp | indirect | -10 to -25% | 3-9 mo |
| C. SLA gaming (10%) | 3 | 30-50% | -5-15% | refund reserve | -5 to -15% | 2-6 mo |
| D. Regulator-mandated SLA | 3 | 20-30% | cost +2-8% one-time | forward reserve | -5 to +5% | 6-18 mo |
| E. SLA-credit blowing reserve | 4 | 15-25% | P&L -2-8% qtr | re-cut required | -10 to -25% | 1-12 mo |
| F. Refund cascade | 4-5 | 10-20% | -5-20% outcome rev | refund reserve gone | -10 to -30% | 3-9 mo |
| G. Insurance exclusion | 2-3 | 30-50% | reserve uplift 1-4% | self-insurance up | -2 to -10% | 12 mo |
| H. Sovereign-AI pass-through | 3-4 | 20-40% (sovereign) | 5-15% affected | provider-reserve | -5 to -15% | 1-6 mo |

---

## Use of Scenarios

1. **Projection.** Top-3 scenarios feed into 3yr / 5yr stress case; reserve adequacy tested against each.
2. **Investor narrative.** FAQ rebuttals on catastrophic / gaming / model-cost / regulator questions reference these scenarios.
3. **Board pack.** Quarterly review of trailing-quarter signal against each scenario's trigger conditions.
4. **Insurance review.** Annual broker conversation cites scenarios A, F, H as primary coverage targets.
5. **Auditor engagement.** Methodology memo references scenarios E and F for reserve sizing rationale.
6. **Living plan cadence.** Weekly indicators of trigger conditions; monthly reserve review; quarterly scenario refresh.

## Cross-References

- `skills/12-risk-analysis/saas-agent-sla-risk/SKILL.md` — risk register parent
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — reserves
- `skills/10-financial-projections/saas-agent-sla-economics-in-projection/SKILL.md` — projection integration
- `skills/meta-agent-sla-financial-controls/SKILL.md` — controls
- `skills/meta-financial-stress-test/SKILL.md` — stress-test parent
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Scenario H (sovereign-AI pass-through)** materially elevated in African deployments where in-region compute is mandated
- **Scenario B (FX-coupled foundation-model cost shock)** compounds with FX-corridor breach; treat as combined stress in African context
- **Scenario D (regulator-mandated SLA)** rising in CBK / CMA / CBN / SEC / SARB / FSCA / BoU / NDPC consultations
- **Scenario G (insurance exclusion)** more severe — carrier capacity thin; self-insurance reserve typically primary mitigation
- **Mobile-money settlement failure** as overlay to Scenario A — settlement-rail failure can amplify SLA breach perception
- **Public-sector dispute lag (90-180 days)** lengthens recovery horizon in Scenario C and F where public-sector customer involved
