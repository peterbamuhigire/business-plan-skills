---
source: Agent-products business-plan audit (2026); engine synthesis
frameworks: [Agent stress scenarios; Quantified impact; Time-to-mitigate]
skill: saas-agent-risk-and-stress-test
cross-reference: [saas-agent-unit-economics-and-cogs, saas-agent-pricing-strategy, meta-financial-stress-test]
---

# Agent Stress-Test Scenarios — Reference

The mandatory stress scenarios that every agent-product plan must run, each with mechanism, quantified impact, mitigation, and time-to-mitigate. Customise magnitudes to the specific business; do not skip scenarios.

## Scenario 1 — LLM Provider 2x Pricing

- **Mechanism:** OpenAI / Anthropic / Google raises blended token pricing 100%.
- **Impact:**
  - Cost per resolved task: +30 to +50% (LLM share is typically 30-60% of agent COGS)
  - Agent GM: -10 to -20pp
  - Runway: -2 to -5 months if absorbed
- **Mitigation:** Model-mix downshift; cache aggressive; switch provider for routine steps; activate vendor-cost pass-through clause after 90-day sustained
- **Time-to-mitigate:** 30-60 days for model-mix + cache; 60-90 days for provider switch
- **Probability:** medium (frontier model price has been deflationary 2023-2025 but specific provider pricing moves are volatile)

## Scenario 2 — LLM Provider 5x Pricing

- **Mechanism:** Severe provider pricing shock (regulatory cost; supply shock; provider strategic shift)
- **Impact:**
  - Cost per resolved task: +120 to +180%
  - Agent GM: likely <0
  - Runway: catastrophic if absorbed; reserve depletion
- **Mitigation:** Immediate vendor-cost pass-through invocation; emergency provider switch; degraded-mode operation; customer communication
- **Time-to-mitigate:** 60-120 days; potential customer attrition
- **Probability:** low but tail-significant

## Scenario 3 — Tool-Vendor Outage 1 Week

- **Mechanism:** Critical tool (CRM / ERP / payment / KYC / WhatsApp / SMS aggregator) outage or contract suspension
- **Impact:**
  - During outage: tasks routed to alternate path or degrade to HITL
  - Cost per resolved task: +40 to +100% during outage (alternate path cost + HITL surge)
  - Agent GM during outage: -15 to -25pp
  - SLA credits: 5-20% of period fee
- **Mitigation:** Multi-vendor architecture pre-built; alternate-path tested; degrade-gracefully UX; customer communication
- **Time-to-mitigate:** Hours-to-days to switch path; days-to-weeks to restore primary
- **Probability:** medium-high (annual occurrence likely)

## Scenario 4 — Intervention Rate Doubles

- **Mechanism:** Eval regression; new customer segment with different distribution; model version change reducing autonomy
- **Impact:**
  - Cost per resolved task: +20 to +40% (HITL surge)
  - Agent GM: -8 to -15pp
  - Customer NPS: -5 to -15 points (intervention is friction)
  - Customer churn risk: +20% on usage-based contracts
- **Mitigation:** Triage re-tuning; planner improvement; eval-set refresh; HITL UX optimisation
- **Time-to-mitigate:** 30-90 days
- **Probability:** medium (typical occurrence during product evolution)

## Scenario 5 — Irreversibility Incident at Scale

- **Mechanism:** Class D action taken incorrectly affecting >1% of customers (financial transfer to wrong account at scale; legal filing with wrong content; medication ordering anomaly; permit issuance anomaly)
- **Impact:**
  - One-time customer-credit / indemnity: 5-25% of annual ARR (severity dependent)
  - Reserve drawdown: full irreversibility reserve
  - Insurance claim: where covered
  - Regulator engagement / investigation cost: USD 50k-500k+
  - Customer-trust damage: 10-30% churn risk at next renewal
  - Press / political exposure
  - Possible service freeze pending investigation
- **Mitigation (preventive):** Class D human-final mandatory; pre-action confirmation; double-signing; immutable audit; rigorous eval coverage on Class D
- **Mitigation (responsive):** Crisis playbook; customer communication; legal / PR / regulator engagement; postmortem and public remediation
- **Time-to-recover:** 3-12 months for trust restoration
- **Probability:** tail event but plausible; **must be reserved for**

## Scenario 6 — Foundation Model Deprecation

- **Mechanism:** Provider announces sunset of model variant the agent depends on; 6-12 month sunset window
- **Impact:**
  - One-time migration spike: +25% on AI spend for one quarter
  - Eval-run cost: 2-5x normal during migration
  - Risk of quality regression on switch
  - Customer SLA risk during transition
  - GM impact -5 to -10pp for the migration quarter
- **Mitigation:** Migration reserve; model-router architecture; canary roll; versioned eval suite
- **Time-to-mitigate:** Migration window (6-12 months); execute in 3-6 months ideally
- **Probability:** high (occurs every 12-24 months for at least one provider)

## Scenario 7 — FX Shock 20% Local Depreciation

- **Mechanism:** Local currency depreciates 20% vs USD (KE, NG, UG, ZA, RW all plausible)
- **Impact (where USD costs / local revenue):**
  - USD agent COGS unchanged
  - Local-currency revenue: -20% in USD terms (or +20% in local terms if priced in local)
  - Agent GM: -8 to -15pp depending on cost structure
- **Mitigation:** FX corridor in pricing; price in USD-equivalent; USD-equivalent contracts; FX hedging where available
- **Time-to-mitigate:** 30-90 days for contract repricing; ongoing for floating price
- **Probability:** medium-high in African markets

## Scenario 8 — Regulator Action Freezing Deployment

- **Mechanism:** Regulator (ODPC / NDPC / NITA-U / Info Reg / NCSA / sectoral) issues notice freezing agent deployment pending investigation or guidance
- **Impact:**
  - Service suspension in affected market
  - Revenue: -10 to -100% for affected market for duration
  - Legal / regulator-engagement cost
  - Customer-credit accruals during suspension
  - Reputational damage
- **Mitigation:** Pre-clearance; sectoral engagement; pause-switch architecture; documentation; HITL evidence on file
- **Time-to-mitigate:** 30 days to 12 months depending on scope
- **Probability:** low-medium per market; higher in regulated sectors

## Scenario 9 — Branch Explosion / Multi-Agent Loop

- **Mechanism:** Uncapped multi-agent planner spawns runaway branches or loops; cost spikes
- **Impact:**
  - Cost per affected task: +50 to +300%
  - If undetected: monthly cost can 2-5x normal
  - SLA breach
  - Customer-trust if observed
- **Mitigation:** Hard branch + loop caps; budget cap; circuit-breaker; kill-switch; observability with alerts
- **Time-to-mitigate:** Hours if detected; days if structural fix needed
- **Probability:** medium for multi-agent products without caps; near-zero with caps

## Scenario 10 — AI Safety Lead Departs Mid-Roadmap

- **Mechanism:** AI Safety Lead resigns / poached / illness; role unfilled for 90+ days
- **Impact:**
  - Safety drill cadence interrupted
  - Audit-log review interrupted
  - Regulator engagement delayed
  - Incident-response capacity reduced
  - Bankability scorecard impact: large
  - Fundraising impact: material at A and later
- **Mitigation:** Succession plan; fractional cover; external advisor on contract; documentation; redundancy in safety practices
- **Time-to-mitigate:** 60-120 days to replace; immediate fractional cover required
- **Probability:** medium (the role is scarce, especially in Africa)

## Scenario 11 — Prompt-Injection Mass Exploitation

- **Mechanism:** Newly-discovered injection vector exploits agent at scale; data exfiltration or unauthorised action
- **Impact:**
  - Sev-1 security incident
  - Possible customer-data breach -> regulator notification
  - Customer credits / churn
  - Insurance claim
  - Service suspension pending fix
- **Mitigation:** Input filtering; tool-call sandboxing; eval on known injection vectors; periodic red-team; kill-switch
- **Time-to-mitigate:** Days for emergency patch; 30-60 days for structural defence
- **Probability:** medium; injection is the OWASP-LLM #1 risk

## Stress-Test Matrix (composite view)

| Scenario | Cost per resolved | Agent GM | Runway impact | Reserve drawdown | Time-to-mitigate |
|---|---|---|---|---|---|
| Provider 2x | +30-50% | -10 to -20pp | -2 to -5 mo | partial migration | 30-60 days |
| Provider 5x | +120-180% | <0 | catastrophic | full | 60-120 days |
| Tool outage 1 wk | +40-100% | -15 to -25pp during | 0.5-1 mo | none | hours-days |
| Intervention 2x | +20-40% | -8 to -15pp | -1 to -3 mo | none | 30-90 days |
| Irreversibility incident at scale | one-time hit | -20 to -50pp period | -1 to -6 mo | full irreversibility | 3-12 mo |
| Model deprecation | +25% Q | -5 to -10pp Q | -0.5 to -1 mo | partial migration | 3-6 mo |
| FX -20% | unchanged USD | -8 to -15pp local | -1 to -3 mo | none | 30-90 days |
| Regulator freeze | revenue 0 affected mkt | catastrophic affected | -1 to -12 mo | regulator | 30-365 days |
| Branch explosion | +50-300% affected | -20-50pp affected | -1 to -2 mo | none | hours-days |
| AI Safety Lead departure | structural | governance regression | fundraise impact | none | 60-120 days |
| Prompt-injection mass | sev-1 cost | -10-25pp | -1 to -3 mo | partial | 30-60 days |

## Living-Plan Integration

- Stress-test refresh: quarterly
- Tabletop exercise: quarterly (one scenario rotated)
- Full simulation: annual
- Reserve adequacy review: quarterly
- Owner: AI Safety Lead + CFO + CEO sign-off

## Cross-References

- Risk register: `saas-agent-risk-register-template.md`
- Unit economics + reserves: `saas-agent-unit-economics-and-cogs`
- Pricing pass-through: `saas-agent-pricing-strategy`
- Financial stress: `meta-financial-stress-test`
- Bankability: `meta-agent-bankability-and-investor-readiness`
