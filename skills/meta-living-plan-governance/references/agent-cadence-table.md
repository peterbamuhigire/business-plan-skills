---
source: Agent-products business-plan audit (2026); engine synthesis
frameworks: [Living-plan agent cadence; Weekly / monthly / quarterly cadence; Owners; Variance thresholds; Trigger-replan conditions]
skill: meta-living-plan-governance
cross-reference: [saas-agent-unit-economics-and-cogs, saas-agent-risk-and-stress-test, saas-agent-moat-and-wrapper-risk, saas-agent-pricing-strategy, meta-agent-bankability-and-investor-readiness, meta-agent-board-and-investor-reporting]
---

# Living-Plan Agent Cadence Table

The agent-specific cadence that every agent-product plan must encode, in addition to the standard living-plan and AI-living-plan cadence. Append to `meta-living-plan-governance/SKILL.md` workflow when the plan is agent-product.

## Weekly cadence

| Element | Owner | Variance threshold | Trigger-replan |
|---|---|---|---|
| Task success rate | Eval Engineer + Head of Agent | -3pp | -5pp in single week |
| Intervention rate | HITL Designer + Head of Agent | +3pp | +5pp sustained 2 weeks |
| Cost per resolved task | CFO + Head of Agent | +15% WoW | +30% WoW |
| Cost per task (weighted) | CFO + Head of Agent | +10% WoW | +20% WoW |
| Tool-invocation reliability per tool | Tool Engineer | error rate >2% | tool outage / 5xx surge |
| Branch / loop ceiling breaches | Eval Engineer | any breach | runaway loop |
| Eval-suite scores (accuracy / hallucination / refusal / latency) | Eval Engineer | -3pp any metric | -5pp |
| Cache-hit ratio | Head of AI | -10pp from baseline | -20pp |
| Token usage per query | Head of AI | +25% WoW | +50% |
| Provider pricing scan | Head of AI / CTO | any change | major change >30% |
| Prompt-injection scan | AI Safety Lead | new vector | active exploitation |

## Monthly cadence

| Element | Owner | Variance threshold | Trigger-replan |
|---|---|---|---|
| Agent gross margin | CFO | -3pp MoM | -5pp QoQ |
| HITL cost share | CFO | >25% of agent COGS | >35% |
| Tool cost share | Tool Engineer | >30% of agent COGS | >45% |
| Retry overhead share | Tool Engineer | >15% of LLM cost | >25% |
| Agent revenue attribution | CFO | -10% of attributable | -20% |
| Irreversibility-class incidents | AI Safety Lead | any sev-1 | sev-1 = immediate re-plan |
| Autonomy incidents (action beyond authority) | AI Safety Lead | any sev-1 | sev-1 = immediate |
| Audit-log review | Compliance + AI Safety Lead | findings | sev-1 finding |
| Kill-switch drill | Tool Engineer + AI Safety Lead | drill failure | drill failure = immediate |
| Red-team / safety drill | AI Safety Lead | missed drill | drill exposes critical gap |
| Eval coverage by action class | Eval Engineer | gap on Class C/D | any gap on Class D |
| Model-deprecation watch | Head of AI / CTO | provider notice | deprecation announced |
| Customer-contestability requests | Compliance | rate trend | rate spike |
| Channel reliability (WhatsApp / SMS / USSD / IVR) | Tool Engineer | provider outage >30min | provider outage >2h |
| AI Safety Lead retention signal | Head of People + CEO | flight signal | departure |
| Sustainability KPIs (energy per resolved task) | Sustainability + CTO | regression | structural shift |
| Misuse / abuse detection | AI Safety + Compliance | trend up | event |

## Quarterly cadence

| Element | Owner | Variance threshold | Trigger-replan |
|---|---|---|---|
| Moat-vs-wrapper rescore | CEO + Head of Strategy | -3 points | foundation provider commoditises |
| Autonomy expansion review | AI Safety Lead + Head of Agent + CEO | proposed level-up | irreversibility class added |
| Regulator engagement / watch | Compliance + Legal | new rule | active enforcement vs analogue |
| Stress-test refresh | AI Safety Lead + CFO + CEO | new tail scenario | structural shift |
| Tabletop incident exercise | AI Safety Lead + CEO | missed exercise | drill exposes gap |
| Reserve adequacy review (irreversibility / migration / regulator) | CFO + AI Safety Lead | <12 months coverage | reserve drawdown event |
| Bankability rescore | CEO + CFO + AI Safety Lead | -5 points QoQ | foundation provider commoditises |
| Valuation / multiple range refresh | CFO + CEO | drift >20% | new comparable |
| Foundation-model platform risk | CTO + CEO | provider ships in category | provider ships product |
| Comparable-transactions scan | Head of Strategy | new comparable moves range | new round / exit |
| Insurance coverage review | CFO | exclusion identified | new exclusion |
| Tool registry proprietary share | Tool Engineer | share falling | structural shift |
| AI Safety Lead succession review | CEO + Head of People | unfilled succession | departure imminent |
| Talent retention scan | Head of People | >15% attrition | >25% in agent team |
| Customer-rollout phase review | Head of CS + Head of Agent | phase slip >30 days | structural |
| Training-data provenance audit | Head of AI / Data | new data source | data-rights challenge |
| Jobs-impact tracking | CEO + HR | shift | regulatory / political event |

## Annual cadence

| Element | Owner | Notes |
|---|---|---|
| Full simulation (end-to-end with customer-impacting drill) | AI Safety Lead + CEO | with customer notification |
| External AI ethics / safety review | CEO + Compliance | third-party where applicable |
| Wardley-map refresh | Head of Strategy | structural |
| Compensation market scan | Head of People | salary band adjustment |
| Sustainability KPI full review | Sustainability + CTO | annual targets |
| Multi-country expansion review | CEO + Head of GTM | regulator readiness per country |

## Trigger-replan events (force immediate re-plan)

In addition to standard SaaS triggers:

- Sev-1 irreversibility incident
- Sev-1 autonomy incident
- Foundation-model provider ships competing capability
- Regulator action freezing deployment
- AI Safety Lead departure without succession
- Provider 5x pricing event
- Tool-vendor major outage / contract suspension
- Multi-agent runaway loop / branch event affecting production
- Prompt-injection mass exploitation
- Audit-log integrity breach
- Reserve drawdown threshold (irreversibility / migration / regulator)

## Integration with standard living-plan cadence

This agent cadence sits on top of:
- Standard SaaS living-plan cadence (`meta-living-plan-governance/SKILL.md` core)
- AI living-plan cadence (`meta-living-plan-governance/SKILL.md` AI section)

All three layers must run in parallel for an agent business.

## Cross-References

- Living plan: `meta-living-plan-governance/SKILL.md`
- Unit economics cadence: `saas-agent-unit-economics-and-cogs`
- Risk cadence: `saas-agent-risk-and-stress-test`
- Moat cadence: `saas-agent-moat-and-wrapper-risk`
- Pricing cadence: `saas-agent-pricing-strategy`
- Reporting: `meta-agent-board-and-investor-reporting`
- Bankability: `meta-agent-bankability-and-investor-readiness`
