---
source: Mersch (Hacking SaaS) ch. 11; engine 4-scenario stress framework; African macro shock history
frameworks: [SaaS stress scenarios; African-context shocks; Survival diagnosis]
skill: meta-financial-stress-test (enhancement)
cross-reference: [saas-unit-economics-and-cohort-model, saas-risk-register-template, 12-risk-analysis]
---

# SaaS Stress-Test Scenarios — Enhancement

The engine's `meta-financial-stress-test` uses a 4-scenario stress framework with Uganda historical shocks. SaaS plans need additional SaaS-specific stress scenarios because the failure modes are different.

## 1. The Top 5 SaaS Stress Scenarios (always model)

### Scenario A: Churn Doubles
- Monthly gross churn 2× baseline (e.g., 2% → 4%)
- Cohort retention curve worsens
- LTV halves
- NRR drops from 105% to 70%
- Implications: Year 3 ARR halves; cash extends but customer count collapses
- Response plan: pause new acquisition; CS triage; pricing review; product fixes
- Survival test: does the company have 9+ months runway in this scenario?

### Scenario B: NRR Collapse
- Expansion mechanic fails; contraction increases
- NRR moves from 110% to 90%
- Net new ARR from existing customer base = negative
- Implications: net new ARR depends entirely on new logos; CAC efficiency must compensate
- Response plan: expansion investment; tier-mix shift to higher tiers; vertical doubling

### Scenario C: Top Customer Loss
- Customer representing >15% of ARR churns
- One-month visible loss
- Implications: ARR drops 15%+; future expansion gone; reference customer gone
- Response plan: concentration plan; diversification target; deal-replacement pipeline
- Customer-concentration policy: no customer >X% of ARR (typically 10-15% target)

### Scenario D: Funding Round Failure
- Targeted round closes 6-12 months late or at 50% target size
- Implications: must extend runway through cost cuts, debt, or RBF
- Response plan: 3 levels of cost cuts (mild / moderate / severe); revenue-finance options; bridge from existing investors
- Pre-emptive: maintain 9+ months runway minimum

### Scenario E: AI / Cloud Cost Spike
- LLM provider cost increases 3-5×; or cloud cost shifts up 40%
- Implications: gross margin drops 5-15pp; expansion-tier economics may break
- Response plan: usage caps; cheaper-model migration; cache; alternative providers; pass-through pricing
- Pre-emptive: per-tenant cost telemetry; multi-provider strategy

## 2. Africa-Specific Stress Scenarios (additional)

### Scenario F: FX Shock (25% local currency depreciation in 90 days)
- USD-denominated costs (cloud, AI, payment-rails) spike
- Local-currency revenue unchanged
- Implications: gross margin drops 5-15pp; cost base in real terms inflates
- Response plan: USD-priced tier; FX-pass-through clauses; hedging where available; cost rebasing
- Reality check: Nigerian Naira moved >70% in 2023-24; Egyptian Pound >60% in 2024

### Scenario G: Payment-Rail Outage
- Primary payment rail (M-Pesa / MoMo / Paystack) outage or policy change
- Involuntary churn spikes; transaction failure across customer base
- Implications: revenue suspended in primary rail; reputational damage
- Response plan: multi-rail architecture; aggregator backup; emergency cash collection
- Pre-emptive: never depend on one payment rail above 60%

### Scenario H: Regulatory Shock
- Central Bank circular; sector regulator change; tax/VAT change; data-residency law
- Implications: compliance cost spike; possibly business-model change required; possibly licence required
- Response plan: regulatory monitoring; legal counsel; sandbox engagement
- Recent examples: NG NIN-BVN consolidation; KE Data Protection Act 2019; EG e-invoicing mandate

### Scenario I: Public-sector / Donor Cycle Collapse
- For SaaS with significant public-sector or donor-funded customers
- Implications: large segment of ARR threatened by single political/donor event
- Response plan: private-sector diversification target; multi-donor mix; geographic diversification

## 3. The Compound Stress Scenario

The most realistic and dangerous scenario combines 2-3 of the above:

**African vertical SaaS compound stress** (illustrative):
- FX depreciation 15%
- AI cost increases 50%
- Churn increases 30%
- Top customer (10% of ARR) churns

Combined impact: 30-50% drop in next-12-month ARR; 25-35% gross-margin compression; 40-60% Year 3 plan miss.

The plan must show survivability of the compound stress (with capital plus cost cuts) — or the company is not adequately capitalised.

## 4. Stress-Test Output Format

For each scenario:
```
SCENARIO: [name]
ASSUMPTIONS:
- [variable 1: from X to Y]
- [variable 2: from X to Y]

IMPACT:
- Year 1 ARR: [base] → [stressed]
- Year 1 EBITDA: [base] → [stressed]
- Cash position end-Year-1: [base] → [stressed]
- Runway months: [base] → [stressed]

RESPONSE PLAN:
- Action 1: [specific cost cut / pricing change / hiring freeze]
- Action 2: [specific operational response]
- Action 3: [specific commercial response]
- Timeline: when each fires

SURVIVABILITY: [Yes — with X actions / No — would require additional capital of $Y]

TRIGGER SIGNAL: [what indicator tells us this scenario is starting]
```

## 5. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Stress-test refresh | Quarterly | CFO |
| Trigger-signal review (monitoring) | Monthly | CFO + COO |
| Response-plan exercise (tabletop) | Annually | Exec team |
| Capital cushion review | At each round | CFO + Board |
| Scenario library refresh | Annually | CFO |

## 6. The Capital Cushion Recommendation

Based on stress modelling, the plan should hold:
- Base operating runway: 9-12 months minimum
- + Cost of mitigating top 3 risks (cyber, FX hedging, payment-rail redundancy)
- + Recovery cost of compound stress scenario

This is the "operational cushion" DFI / patient-capital investors expect. Companies running on 3-month runway are operating without margin of safety.

## 7. Africa / Uganda Application Notes

- **FX volatility** is the most under-modelled risk in African SaaS plans — always stress >15% depreciation.
- **Payment-rail concentration** is the second most under-modelled — always model a primary-rail outage.
- **Political / election-cycle risk** in some markets (Nigeria, Kenya, Senegal, Ghana, South Africa, etc.) — election years often produce 1-2 month operational disruption; model for known election dates.
- **Power / connectivity reliability** — extended outages affect SLA-tier customers; model with revenue credits.
- **Talent flight** — senior engineers leaving for Western remote-work opportunities; budget retention investment.
- **Donor-cycle risk** for plans with >20% donor-funded customers — explicitly model the cycle.
- **Tax / regulatory** changes are frequent — quarterly regulatory scan into the cadence.
- **Compound stress** is more common in Africa than US benchmarks — model 2-3 stressors together as a likely scenario, not a tail risk.
