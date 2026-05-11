---
source: Agent-products business-plan audit (2026); engine synthesis
frameworks: [Agent stress scenarios for financial stress test; Quantified impact; Reserve consumption]
skill: meta-financial-stress-test
cross-reference: [saas-agent-risk-and-stress-test, saas-agent-unit-economics-and-cogs, meta-agent-bankability-and-investor-readiness]
---

# Agent Stress-Test Scenarios — Reference (financial-stress overlay)

The agent-specific stress scenarios to add to `meta-financial-stress-test` when the plan is an agent business. Full risk-side scenarios live in `saas-agent-risk-and-stress-test/references/saas-agent-stress-test-scenarios.md`; this file captures the **financial-stress-overlay** version (focus: P&L, balance sheet, runway, valuation).

## Mandatory scenarios (run in addition to standard financial stress)

1. **LLM provider pricing 2x and 5x**
2. **Tool-vendor outage 1 week** (and 1 month for severe)
3. **Intervention rate 2x sustained**
4. **Irreversibility incident at scale** (sev-1 customer-impact >1% of customers)
5. **Foundation-model deprecation forced migration**
6. **FX shock 20% local-currency depreciation**
7. **Regulator action freezing deployment in a market**
8. **Branch explosion / multi-agent loop**
9. **AI Safety Lead departure mid-roadmap**
10. **Prompt-injection mass exploitation**

## Quantified impact (typical ranges; customise to business)

| Scenario | Cost per resolved | Agent GM | Runway impact | Reserve drawdown | Valuation impact |
|---|---|---|---|---|---|
| Provider 2x | +30-50% | -10 to -20pp | -2 to -5 mo | partial migration | -10 to -20% multiple |
| Provider 5x | +120-180% | <0 | catastrophic | full | -20 to -40% multiple |
| Tool outage 1 wk | +40-100% | -15 to -25pp | -0.5 to -1 mo | none | -5 to -10% |
| Tool outage 1 mo | +40-100% sustained | -15 to -25pp sustained | -3 to -6 mo | partial | -15 to -25% |
| Intervention 2x | +20-40% | -8 to -15pp | -1 to -3 mo | none | -10 to -15% |
| Irreversibility incident at scale | one-time hit | -20 to -50pp period | -1 to -6 mo | full irreversibility | -30 to -50% |
| Model deprecation | +25% Q | -5 to -10pp Q | -0.5 to -1 mo | partial migration | -5 to -10% |
| FX -20% local | unchanged USD | -8 to -15pp local | -1 to -3 mo | none | <5% (USD pricing) |
| Regulator freeze | revenue 0 affected mkt | catastrophic affected mkt | -1 to -12 mo | regulator | -20 to -40% if material market |
| Branch explosion | +50-300% affected | -20-50pp affected | -1 to -2 mo | none | -10 to -25% |
| AI Safety Lead departure | structural | governance regression | fundraise impact | none | -15 to -25% |
| Prompt-injection mass | sev-1 cost | -10-25pp | -1 to -3 mo | partial | -20 to -40% |

## Composite scenarios

Investors and DFIs increasingly request composite scenarios (multiple stresses simultaneously):

- **Provider 2x + intervention 2x + FX -15%** (cumulative margin compression scenario)
- **Tool outage + intervention 2x** (operational stress)
- **Irreversibility incident + regulator freeze** (governance crisis)
- **AI Safety Lead departure + foundation-model deprecation** (capacity x technical stress)
- **Provider 2x + intervention 2x + AI Safety Lead departure** (worst-case strategic)

For each composite: cost per resolved, GM, runway, reserve, valuation, time-to-recover.

## Reserve adequacy

Reserves must cover:

- **Irreversibility reserve** — at least 12 months of expected sev-1 customer-credit / indemnity at modelled rate (typically 5-25% of annual ARR per incident at scale; reserve sized at lower-bound rate x months coverage)
- **Model-migration reserve** — at least 1 full migration cycle (~25% of one quarter's AI spend)
- **Regulator-engagement reserve** — at least 12 months of expected engagement cost (USD 50k-500k+ depending on jurisdiction and footprint)

## Runway protection

Plans must show runway under:
- Base case
- Provider 2x case
- Composite worst-case
- Recovery trajectory

If runway under composite worst-case is <6 months, escalate to board for funding action.

## Valuation stress

Run the multiple under each scenario (per `meta-agent-valuation-adjustments`):
- Base multiple range
- Multiple under provider 2x
- Multiple under irreversibility incident
- Multiple under foundation-model commoditisation
- Multiple under AI Safety Lead departure

Communicate stress on multiple to investors transparently.

## Living-plan integration

- Stress-test refresh: quarterly
- Tabletop exercise: quarterly
- Composite scenario run: semi-annually
- Reserve adequacy review: quarterly
- Owner: CFO + AI Safety Lead + CEO sign-off

## Cross-References

- Risk-side stress: `saas-agent-risk-and-stress-test/references/saas-agent-stress-test-scenarios.md`
- Unit economics: `saas-agent-unit-economics-and-cogs`
- Pricing pass-through: `saas-agent-pricing-strategy`
- Valuation: `meta-agent-valuation-adjustments`
- Bankability: `meta-agent-bankability-and-investor-readiness`
