---
source: Agent-products business-plan audit (2026); 2024-2026 agent-VC diligence practice
frameworks: [Per-task cost calculator; Sensitivity worksheet; Stress worksheet]
skill: saas-agent-unit-economics-and-cogs
cross-reference: [saas-agent-unit-economics-template, saas-agent-pricing-strategy]
---

# Agent Cost-Per-Task Calculator — Specification

A specification for building (in Excel / Google Sheets / Notion calculator / Python notebook) the cost-per-task and cost-per-resolved-task calculator that every agent-product plan must produce.

## Worksheets

### Worksheet 1 — Inputs

Single-cell inputs (with sensible defaults; investor-readable):

**Provider pricing**
- Frontier model input rate (USD per 1M tokens)
- Frontier model output rate (USD per 1M tokens)
- Cheap-router input rate (USD per 1M tokens)
- Cheap-router output rate (USD per 1M tokens)
- Specialist / fine-tuned model rates (input / output)
- Embedding rate (USD per 1M tokens)

**Agent architecture**
- Avg planner step input tokens
- Avg planner step output tokens
- Number of worker steps per task (mean)
- Avg worker step input tokens
- Avg worker step output tokens
- Worker step model-mix (% frontier / % cheap / % specialist)
- Critic step present? (Y/N) + tokens + model
- HITL-prep step present? (Y/N) + tokens + model

**Tools**
- Tool 1 name + per-invocation cost + invocations per task
- ...up to N tools
- Channel cost (WhatsApp / SMS / USSD / IVR) per task

**Behaviour**
- Retry rate (%)
- Avg retry depth (number of repeated steps)
- Branch fan-out (parallel branches per task; 1 if single-agent)
- Branch proportion of tasks (% with branches)
- HITL escalation rate (%)
- HITL minutes per escalated task (mean)
- HITL fully-loaded rate (local currency / hour)
- FX rate (local / USD)

**Task taxonomy**
- Resolved rate (%)
- Escalated-to-HITL rate (%) — resolved with help
- Escalated-to-human-final rate (%) — escalated and not resolved by agent
- Failed rate (%)
- Abandoned rate (%)
- Looped-killed rate (%)
- (sum = 100%)

**Indirect & overhead (monthly amounts to allocate)**
- Eval-loop spend / month
- Observability / tracing / month
- Sandbox + staging / month
- Audit-log retention / month
- Supervision UX runtime / month
- Agent team payroll (Architect + Tool + Eval + Safety + HITL Designer) / month (loaded)
- % of team payroll allocated to COGS vs OpEx (default 60% COGS, 40% OpEx)

**Reserves**
- Irreversibility-incident reserve (bp of revenue or USD / task)
- Model-migration reserve (% of period AI spend)
- Regulator-engagement reserve (USD / month accrual)

**Volume**
- Tasks per month (mean)
- Tasks per month (P95 stress)

### Worksheet 2 — Per-Task Computation

Computed cells:

```
llm_planner_cost = (planner_in_tokens x frontier_in_rate + planner_out_tokens x frontier_out_rate) / 1e6
llm_worker_cost  = N_workers x [ mix_frontier x (in x frontier_in + out x frontier_out)
                                + mix_cheap   x (in x cheap_in    + out x cheap_out)
                                + mix_special x (in x special_in  + out x special_out) ] / 1e6
llm_critic_cost  = (critic_in x rate_in + critic_out x rate_out) / 1e6  (if present)
llm_hitlprep_cost = ... (if present)
llm_total = sum of above

tool_total = sum over tools of (tool_cost_per_invocation x invocations_per_task)
channel_total = channel_cost_per_task

retry_overhead = (llm_total + tool_total) x retry_rate x avg_retry_depth
branch_overhead = (llm_total + tool_total + channel_total) x (branch_fan_out - 1) x branch_proportion

hitl_loaded_per_min = hitl_loaded_per_hour / 60 / fx_rate    (to USD)
hitl_cost_per_escalated = hitl_minutes_per_escalated x hitl_loaded_per_min
hitl_cost_per_task = hitl_cost_per_escalated x hitl_escalation_rate

direct_per_task = llm_total + tool_total + channel_total + retry_overhead + branch_overhead + hitl_cost_per_task

indirect_per_task = (eval_loop + observability + sandbox + audit_log + supervision_ux) / tasks_per_month
overhead_per_task = (team_payroll x cogs_allocation_pct) / tasks_per_month
reserve_per_task  = (irreversibility_reserve_per_task) + (migration_reserve_pct x llm_total) + (regulator_reserve / tasks_per_month)

total_cost_per_task = direct_per_task + indirect_per_task + overhead_per_task + reserve_per_task
cost_per_resolved_task = total_cost_per_task x (1 / resolved_rate)
```

### Worksheet 3 — Sensitivity

A two-axis grid:
- Rows: dimensions (provider price, intervention rate, failure rate, FX, cache-hit, volume)
- Columns: -30% / -15% / base / +15% / +30%
- Cells: cost-per-resolved-task and agent gross margin

Identify the **two most sensitive dimensions** — those are the binding margin levers. Document mitigation per lever.

### Worksheet 4 — Stress

Pre-coded scenarios:
- Provider 2x
- Provider 5x
- Tool-vendor outage 1 week (alternate-path cost)
- Intervention rate 2x
- Failure rate 2x
- Foundation model deprecation (one-time migration cost)
- Irreversibility incident (reserve drawdown)
- FX shock -20% local
- Branch explosion (uncapped multi-agent)

Each scenario shows: cost-per-resolved-task, agent gross margin, runway impact, mitigation, time-to-mitigate.

### Worksheet 5 — Pricing Floor

Inputs: target agent gross margin (e.g. 65%) and total cost per resolved task.
Output: minimum per-resolution price (or per-outcome / per-step equivalent).
Cross-check: price-corridor analysis from `saas-agent-pricing-strategy`.

### Worksheet 6 — Diagnostics Dashboard

Headline outputs:
- Cost per resolved task (USD + local)
- Agent gross margin (%)
- Intervention rate (%)
- HITL cost share (%)
- Tool cost share (%)
- Retry overhead share (%)
- Cache-hit ratio (%)
- Sensitivity ranking of dimensions
- Stress red flags

## Building Order

1. Inputs first (no calculations); validate ranges and units.
2. Per-task computation; validate against a known reference task.
3. Sensitivity (use data-table or Python loop).
4. Stress (manual scenario overrides).
5. Pricing floor (derived).
6. Dashboard.

## Validation Checks

- All currency consistent (display in both USD and local; compute in USD)
- Task taxonomy sums to 100%
- Model-mix sums to 100%
- Cost per resolved task >= cost per task (always; sanity check)
- HITL cost share within plausible range (0-40%; alarm if outside)
- Tool cost share within plausible range (5-50%)
- Retry overhead share within plausible range (0-20% of LLM cost; alarm if >20%)
- Branch overhead == 0 if single-agent (sanity)
- Reserve adequacy = months of coverage at expected incident rate (>=12 months target)

## Owner & Cadence

- Owner: CFO with Head of Agent
- Build cadence: weekly cost-per-resolved-task; monthly full refresh; quarterly stress refresh
- Sign-off: monthly review by CEO; quarterly board review
