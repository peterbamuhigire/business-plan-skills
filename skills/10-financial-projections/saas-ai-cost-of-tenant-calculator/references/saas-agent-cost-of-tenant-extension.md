---
source: Agent-products business-plan audit (2026); engine synthesis
frameworks: [Agent extension to AI cost-of-tenant calculator; Steps x tools dimension; Multi-step inflation]
skill: saas-ai-cost-of-tenant-calculator
cross-reference: [saas-agent-unit-economics-and-cogs, saas-agent-cost-per-task-calculator-spec]
---

# Agent Extension to Cost-of-Tenant Calculator

When the SaaS product is an agent or includes agentic capability, the AI cost-of-tenant calculator (`saas-ai-cost-of-tenant-calculator.md`) must be extended with a steps-x-tools dimension. This file specifies the extension.

## 1. Why the AI cost-of-tenant calculator is insufficient on its own

Generic AI cost-of-tenant treats one user query as one LLM call. Agent products generate many LLM calls per user request (planner + workers + critic + retries + branches) plus tool calls. Without the steps-x-tools dimension, per-tenant cost is materially understated.

## 2. Additional input fields (extend the AI calculator)

- Average steps per tenant user request (planner + worker count + critic)
- Average tool invocations per tenant user request
- Average branch fan-out (if multi-agent)
- Retry rate and depth
- HITL escalation rate per tenant
- Channel cost per tenant (WhatsApp / SMS / USSD / IVR)
- Action-class mix per tenant (% Class A / B / C / D)

## 3. Modified per-tenant cost formula

```
per_tenant_AI_cost (agent) =
   per_tenant_token_cost x avg_steps x model_mix_weight
 + per_tenant_tool_cost x avg_tool_invocations
 + per_tenant_channel_cost x avg_channel_interactions
 + retry_overhead
 + branch_overhead
 + HITL_cost_per_tenant
 + per_tenant_eval_share
 + per_tenant_reserve_share
 + per_tenant_overhead_share
```

Full breakdown in `saas-agent-unit-economics-and-cogs/references/saas-agent-unit-economics-template.md`.

## 4. Cross-link to the agent calculator spec

Use the full agent calculator spec at:

`skills/10-financial-projections/saas-agent-unit-economics-and-cogs/references/saas-agent-cost-per-task-calculator-spec.md`

That spec covers:
- 6 worksheets (Inputs, Per-Task Computation, Sensitivity, Stress, Pricing Floor, Diagnostics)
- Cost-per-task and cost-per-resolved-task formulae
- Validation checks

## 5. When to use which calculator

- AI feature only (no agent) -> use AI cost-of-tenant calculator
- Agent or multi-agent product -> use agent calculator (which subsumes the AI calculator)
- AI feature + agent in same product -> use both, allocate revenue and cost separately to AI feature vs agent

## 6. Cross-references

- AI calculator parent: `saas-ai-cost-of-tenant-calculator.md`
- Agent calculator: `saas-agent-cost-per-task-calculator-spec.md`
- Agent unit economics: `saas-agent-unit-economics-and-cogs/SKILL.md`
- Pricing: `saas-agent-pricing-strategy/SKILL.md`
