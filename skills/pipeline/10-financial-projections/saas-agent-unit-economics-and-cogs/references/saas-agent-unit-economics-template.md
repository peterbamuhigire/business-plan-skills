---
source: Agent-products business-plan audit (2026); Mersch CFO discipline; 2024-2026 agent-VC diligence practice
frameworks: [Agent COGS waterfall; Cost per task; Cost per resolved task; Agent gross margin; Sensitivity; Stress]
skill: saas-agent-unit-economics-and-cogs
cross-reference: [saas-agent-pricing-strategy, saas-agent-risk-and-stress-test, meta-agent-bankability-and-investor-readiness, meta-agent-valuation-adjustments]
---

# SaaS Agent Unit Economics Template

This template specifies the formulas, the waterfall, a worked example, and the diagnostics for agent cost-of-revenue. It is the canonical model for any agent-product plan in this engine.

## 1. The Agent COGS Waterfall

```
Agent Direct COGS (per task class)
  LLM token cost (planner step)
+ LLM token cost (worker steps, summed; weighted by model mix)
+ LLM token cost (critic / supervisor step)
+ LLM token cost (HITL-prep step if any)
+ Tool invocation cost (sum of per-tool tariffs)
+ External API cost (separate from tool registry)
+ Channel cost (WhatsApp / USSD / SMS / IVR / voice where applicable)
+ Retry overhead = (LLM+tool) cost x retry_rate x avg_retry_depth
+ Branch overhead = (LLM+tool) cost x (branch_fan_out - 1) x branch_proportion_of_tasks
+ HITL escalation cost = HITL_minutes_per_escalated_task x HITL_loaded_rate_per_minute x HITL_escalation_rate
= Agent Direct COGS per task

Agent Indirect COGS (period costs allocated per task)
+ Eval-loop spend (monthly) / task volume (monthly)
+ Observability / tracing spend / task volume
+ Sandbox + staging compute / task volume
+ Audit-log retention cost / task volume
+ Supervision UX runtime / task volume

Agent Reserves (accrued; expensed periodically)
+ Irreversibility-incident reserve (basis-point of revenue or per-task)
+ Model-migration reserve (% of period AI spend)
+ Regulator-engagement reserve (period accrual)

Agent Overhead Allocation (% of fully-loaded payroll allocated to COGS)
+ Agent Architect (allocated share)
+ Tool Engineer (allocated share)
+ Eval Engineer (allocated share)
+ AI Safety Lead (allocated share)
+ HITL Designer (allocated share)
+ Forward Deployed Engineer (allocated share, if customer-specific agent builds)
= Total Agent COGS per task
```

## 2. Cost-Per-Task vs Cost-Per-Resolved-Task

**Cost per task (weighted)** = sum over task classes of (cost per task in class x proportion of class in task volume).

**Cost per resolved task** = total agent COGS (all classes) / number of **resolved** tasks (excluding escalated-to-human-final, failed, abandoned, looped-killed).

The gap between these two metrics tells you how much unresolved-task drag your model carries. A well-tuned agent has cost-per-resolved-task within 15-30% of cost-per-task. A poorly-tuned agent can have cost-per-resolved-task 2-3x cost-per-task because too many failed / abandoned / escalated tasks amortise across too few resolved outcomes.

**Investors will quote cost-per-resolved-task as the headline.** Plan accordingly.

## 3. Agent Gross Margin

```
Agent-attributable revenue (per period)
  - per-resolution price x resolved tasks
  - per-outcome price x outcomes
  - per-step price x billable steps
  - per-agent / per-seat price x agents-deployed
  - bundled-tier AI revenue attributed (honest fraction)
- Agent COGS (per period)
= Agent Gross Profit
Agent Gross Margin = Agent Gross Profit / Agent-attributable revenue
```

Target benchmarks (2026 agent-product market):
- **<50% agent GM** — margin-strained; likely wrapper; expect valuation discount
- **50-65% agent GM** — viable; typical at A; needs trajectory
- **65-75% agent GM** — strong; defensible; premium territory
- **>75% agent GM** — exceptional; likely vertical agent with proprietary tools and pricing power

## 4. Worked Example — Vertical Agentic SaaS (East Africa)

**Business:** AI agent for cooperative-society loan-arrears collection. Vertical agentic SaaS. Customer = SACCO or microfinance. Agent takes case files, contacts borrower via WhatsApp / SMS / voice IVR / call, negotiates rescheduling within policy, escalates irrecoverable cases. Pricing: per-resolved-case (USD 1.20 / UGX 4,400 in 2025/26 planning rate).

**Architecture:**
- Planner step (GPT-4o-class, USD 2.50/1M in + USD 10/1M out)
- 2-4 worker steps (Claude Haiku / Llama-3 70B on Cassava: USD 0.25/1M in + USD 1.25/1M out)
- Critic step (Claude Sonnet-class for policy compliance check)
- Tools: SACCO core-banking API (USD 0.005/call); WhatsApp Business API (USD 0.005/conversation); SMS aggregator (UGX 25/SMS ~ USD 0.0067); IVR voice (UGX 80/min ~ USD 0.022); KYC re-check (USD 0.04/call)

**Per resolved-case typical:**

| Component | Calculation | Cost (USD) |
|---|---|---|
| Planner step | 800 in + 300 out = USD 0.005 | 0.005 |
| Worker steps (3) | 3 x (1,200 in + 500 out) on cheap router = 3 x USD 0.0009 | 0.003 |
| Critic step | 600 in + 200 out = USD 0.0035 | 0.003 |
| WhatsApp tool | 2 conversations | 0.010 |
| SMS tool | 3 SMS | 0.020 |
| IVR call | 1 call avg 2 min | 0.044 |
| KYC re-check | 0.4 calls (40% of cases) | 0.016 |
| Core-banking API | 4 calls | 0.020 |
| Retry overhead | 15% on LLM+tool = ~ USD 0.018 x 0.15 | 0.003 |
| HITL escalation cost | 12% escalated x 8 min x UGX 8,000/hour HITL loaded | 0.026 |
| **Subtotal direct per case** | | **0.150** |
| Eval / observability / sandbox / audit-log allocation | 10% of direct (monthly accrual) | 0.015 |
| Reserves (irreversibility + migration + regulator) | 5% of direct | 0.008 |
| Overhead allocation (payroll share) | 12% of direct | 0.018 |
| **Total agent COGS per resolved case** | | **0.191** |

**Pricing:** USD 1.20 per resolved case
**Agent gross profit per case:** USD 1.009
**Agent gross margin:** 84% (this is a strong vertical agent profile — proprietary tools, deep workflow, regulator engagement, vertical pricing power)

**Cost per task (weighted across resolved + escalated + failed + abandoned):** USD 0.158 (lower than per-resolved because failed/abandoned use fewer steps; not always the case)

**Cost per resolved task (the true unit):** USD 0.191 (computed above) — used as headline.

**FX sensitivity:** at UGX 3,900/$ stress (vs 3,700 plan rate), USD per-resolved revenue holds (priced in USD-equivalent) but USD-denominated COGS unchanged; UGX-priced HITL cheaper in USD terms = small margin tailwind. At UGX 3,500/$ (UGX strengthens), HITL more expensive in USD = small margin headwind.

## 5. Sensitivity Matrix (template)

| Dimension | -30% | -15% | Base | +15% | +30% |
|---|---|---|---|---|---|
| Task volume | (cost spread thinner; GM up) | | base | | (cost spread thinner; GM up further) |
| Provider pricing | GM up materially | GM up | base | GM down | GM down materially |
| Intervention rate | GM up | GM up | base | GM down | GM down |
| Failure / abandonment rate | cost per resolved down | down | base | up | up |
| FX (local currency vs USD) | HITL cheaper in USD; GM up | up | base | down | down |
| Cache-hit ratio | GM down | down | base | up | up |
| Branch fan-out | GM up | up | base | down (runaway risk) | down (runaway risk) |

## 6. Stress Scenarios

| Scenario | Mechanism | Impact on cost per resolved | Impact on agent GM | Mitigation |
|---|---|---|---|---|
| Provider doubles pricing | LLM cost x2 | +30-50% | -10 to -20pp | Model-mix downshift; cache; switch provider |
| Provider 5x pricing | shock | +120-180% | likely <0 GM | Emergency price-pass-through; provider switch |
| Tool-vendor outage | retries + alternate path | +40-100% during outage | -15 to -25pp during outage | Multi-vendor failover; degrade gracefully |
| Intervention rate doubles | HITL cost share rises | +20-40% | -8 to -15pp | Re-train triage; tighten policy thresholds |
| Failure rate doubles | unresolved tasks consume cost | +30-60% | -10 to -20pp | Tighten eval; reduce overconfident attempts |
| Foundation model deprecation | migration spike | +25% one-time | -5 to -10pp quarter | Reserve drawdown; planned migration |
| Irreversibility incident | reserve drawdown + customer credits | one-time hit | period GM -20 to -50pp | Reserve was for this; tighten autonomy class |
| FX shock 20% local-currency depreciation | USD cost holds; local revenue down | unchanged USD; +20% local | -8 to -15pp on local-currency P&L | FX corridor in pricing; USD-equivalent contract |
| Branch explosion (multi-agent) | uncapped fan-out | +50-300% on affected tasks | catastrophic if uncapped | Hard branch + loop caps; kill-switch |

## 7. Diagnostics & Headline Metrics

State these in every agent business plan financial section:

- **Cost per resolved task** (currency + units)
- **Agent gross margin** (%)
- **Intervention rate** (%; lower is better up to a quality floor)
- **Task success rate** (%; eval-defined)
- **Cost as % of agent revenue**
- **Tool-cost share of agent COGS** (%)
- **HITL-cost share of agent COGS** (%)
- **Retry overhead share of LLM cost** (%)
- **Cache-hit ratio** (%)
- **Branch / loop ceiling breaches** (count per month)
- **Reserve adequacy** (months of coverage at expected incident rate)

## 8. Living-Plan Wiring

Cadence and owners defined in `skills/saas-agent-unit-economics-and-cogs/SKILL.md` and `meta-living-plan-governance`. Recap:

- **Weekly:** cost per resolved task; cost per task weighted; intervention rate; task success; tool reliability per tool; branch / loop breaches
- **Monthly:** agent gross margin; HITL cost share; retry overhead share; tool-cost share; provider pricing watch
- **Quarterly:** model-migration reserve; irreversibility reserve; regulator-engagement reserve; moat-vs-wrapper reassessment

## 9. Anti-Patterns (recap)

- "Agent cost ~= LLM cost" — wrong
- Single-model assumption — wrong
- Tool calls assumed free — wrong
- HITL assumed zero — wrong
- Failed / abandoned tasks not amortised — wrong
- USD-only modelling — wrong for local-currency markets
- No retry / branch / loop modelling — wrong
- Cost-per-resolved-task absent — investors will not accept
