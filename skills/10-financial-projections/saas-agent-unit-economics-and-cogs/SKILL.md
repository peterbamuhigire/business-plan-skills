---
name: saas-agent-unit-economics-and-cogs
description: Decompose AI-agent cost-of-revenue into a multi-step COGS waterfall (LLM tokens x steps x parallel branches + tool invocations x tool cost + external API + retry overhead + supervision overhead) and produce agent gross margin, cost-per-task, and cost-per-resolved-task (the true unit) diagnostics that investors in agent businesses require. Sits on top of `saas-ai-unit-economics-and-cogs`. Use whenever an agentic / multi-agent product is a material part of the plan.
---

# SaaS Agent Unit Economics & COGS Skill

## Overview

Generic AI unit economics treats one user query as one LLM call. **Agent unit economics is fundamentally different**: one user request triggers a planner step, N worker steps, M tool invocations, possible retries, possible parallel branches, possible critic / supervisor calls, possible human-in-the-loop (HITL) escalations. A single resolved customer-service ticket can be 15-40 LLM calls and 5-15 tool invocations. A single "deep research" outcome can be hundreds of LLM calls. The cost waterfall is **multiplicative**, not additive, and investors will not accept generic AI cost models for agent products.

This skill installs the agent COGS discipline:

1. **Agent direct COGS** — LLM tokens at each step (planner + workers + critic), tool invocations, external API cost, retry overhead, branch cost, HITL escalation cost.
2. **Agent indirect COGS** — eval-loop cost, observability / tracing infrastructure, audit-log retention, sandbox / staging cost, supervision UX runtime.
3. **Agent reserves** — irreversibility-incident reserve, regulator-engagement reserve, model-migration reserve.
4. **Agent overhead allocation** — share of Agent Architect / Tool Engineer / Eval Engineer / AI Safety Lead / HITL Designer payroll.

Together these produce **cost-per-task**, **cost-per-resolved-task** (the true unit because unresolved tasks still cost money), **agent gross margin**, **intervention-cost overhead**, and the **agent-cost-as-%-of-agent-revenue** diagnostic.

## Use When

- A SaaS / ICT plan includes an agentic or multi-agent product (single agent, planner-worker-critic, or vertical agent)
- Section 10 is being built for an agent-product plan
- Pricing must be set on per-resolution / per-outcome / per-step basis and needs cost floor
- Investors / DFIs have asked for cost-per-resolved-task specifically
- An existing AI-SaaS is moving up the autonomy ladder (assist -> suggest -> supervise -> agentic) and per-query economics no longer model reality
- The plan must pass `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- The AI feature is a single-shot completion (translate, summarise, classify) with no multi-step planning or tool use — use `saas-ai-unit-economics-and-cogs`
- The product is internal-efficiency only with no customer-facing agent
- The business is not SaaS / subscription / usage-based recurring

## Required Inputs

- Agent architecture description: single-agent or multi-agent; planner / worker / critic decomposition; tool registry (which tools, which providers, per-invocation cost)
- Per-agent-step model assignment (which step uses which model — frontier vs cheap-router)
- Average step count per task by task class (resolved, escalated, failed, abandoned)
- Average parallel-branch fan-out where applicable
- Retry policy and observed retry rate
- HITL escalation rate (% of tasks escalated to human; cost per HITL minute)
- Tool-invocation rate and per-tool cost (ERP, CRM, payment, KYC, mapping, OCR, internal API)
- Eval-loop spend per month (offline + online evals)
- Observability / tracing spend (LangSmith, LangFuse, Arize, Helicone, Weights & Biases, internal)
- Sandbox / staging compute spend
- Audit-log retention cost (storage + retrieval)
- Currency exposure (USD-denominated LLM + tool cost vs local-currency revenue)

## Workflow

1. **Document the agent architecture** — one paragraph + a step-and-tool diagram (or text decomposition: planner step -> N worker steps -> tool calls -> critic -> finaliser). Without this, cost modelling is fiction.
2. **Define the task taxonomy** — by class (resolved, escalated-to-HITL, escalated-to-human-final, failed, abandoned, looped-and-killed). Each class has different cost.
3. **Build the per-task cost decomposition** using `references/saas-agent-unit-economics-template.md`:
   - LLM cost per task = sum over steps of (input tokens x input rate + output tokens x output rate) x model-mix factor
   - Tool cost per task = sum over tool invocations of per-invocation tariff (some tools are flat per call, some metered)
   - External API cost per task (separate from tools where vendor lock-in or auth differs)
   - Retry overhead = LLM cost x retry rate x average retry depth
   - Branch overhead = (parallel-branch factor - 1) x base step cost (where applicable; multi-agent products)
   - HITL escalation cost = (HITL minutes per escalated task x fully-loaded HITL hourly rate / 60) x HITL escalation rate
   - Supervision overhead = supervisor / critic call cost per task
4. **Cost per task** = sum of above. Compute weighted average across task classes.
5. **Cost per resolved task (the true unit)** = total agent operating spend / number of resolved tasks. This is materially higher than cost-per-task because unresolved / failed / abandoned tasks still consume cost and must be amortised across the resolved outcomes. Investors will quote this number.
6. **Agent gross margin** = (agent-attributable revenue - agent COGS) / agent-attributable revenue. Use revenue attribution discipline (per-resolution pricing tracks directly; tier-bundled agent revenue must be attributed honestly).
7. **Agent contribution margin per pricing model** — for per-resolution, per-outcome, per-step, per-agent, hybrid. Identify which pricing models leave thin or negative margin.
8. **Apply mitigation levers** in scenarios:
   - **Step compression** — collapse planner + worker into single-shot for routine tasks (saves 30-50%)
   - **Model downshift on routine steps** — route low-stakes steps to cheap-router model (saves 40-70% on those steps)
   - **Tool result caching** — cache deterministic tool outputs (saves 20-40% of tool cost)
   - **Branch caps** — hard-cap parallel branches and loop depth (prevents runaway; saves variable %)
   - **HITL escalation re-tuning** — better triage reduces unnecessary HITL escalations (saves HITL minutes)
   - **Retry-policy tuning** — reduce blind retries, add backoff and re-prompt logic
   - **Prompt compression** — shorten system prompts shared across steps
9. **Sensitivity-test** — +/- 30% task volume, +/- 50% provider pricing, +/- 5pp intervention rate, +/- 5pp failure rate, +/- 20% FX.
10. **Stress-test** — provider 5x pricing; tool-vendor outage forces alternative path; intervention rate doubles; irreversibility-incident reserve drawn; foundation model deprecates and migration required.
11. **Wire to living-plan governance** — assign cadence, owners, variance thresholds per Agent Living-Plan Cadence below.
12. **Diagnose binding constraint** — which lever (step compression, model mix, tool caching, branch cap, HITL tuning) most improves cost-per-resolved-task?

## Quality Bar

- Agent architecture stated explicitly; planner / worker / critic / HITL decomposed
- Task taxonomy enumerated (resolved / escalated / failed / abandoned / looped-killed) with proportions
- Cost-per-task and **cost-per-resolved-task** both computed; the latter quoted as headline
- Agent gross margin separately computed from blended AI / SaaS margin
- Tool-cost line distinct from LLM-cost line (auditors and investors expect both)
- HITL escalation cost included; not assumed zero
- Sensitivity covers volume, pricing, intervention rate, failure rate, FX
- Stress scenarios cover provider 5x, tool outage, intervention 2x, irreversibility reserve, model deprecation migration
- Mitigation playbook explicit with expected impact per lever
- Living-plan cadence assigned with owners
- A sceptical Series A AI-agent-fund partner would not laugh at the model

## Anti-Patterns

- "Agent cost is roughly the LLM cost" — ignores tools, retries, branches, HITL, supervision
- "We charge per-resolution so cost-per-task doesn't matter" — wrong; per-resolution requires knowing the cost floor or you set price below margin
- Cost computed on resolved tasks only — must amortise failed and abandoned across resolved
- "Tool calls are free" — most enterprise tools (CRM, ERP, payment, KYC) have per-call cost
- No retry-overhead line — production agents retry 10-30% of the time
- Single-model assumption when product needs router (frontier for plan, cheap for worker)
- "HITL is rare" — production agents typically escalate 5-25% depending on irreversibility class
- USD-only modelling when revenue is local currency
- No branch cap modelled — multi-agent products can blow cost budgets when uncapped
- "We'll optimise costs after launch" — optimisation is the business model in agents, not an afterthought
- Treating supervisor / critic calls as overhead, not COGS — they are COGS

## Outputs

- Agent architecture description (one paragraph + step decomposition)
- Task taxonomy with class proportions
- Per-task cost decomposition (LLM + tool + API + retry + branch + HITL + supervision)
- Cost per task (weighted)
- **Cost per resolved task** (headline diagnostic)
- Agent gross margin
- Agent contribution margin by pricing model
- Sensitivity + stress analyses
- Mitigation playbook with prioritised levers
- Living-plan cadence assignment

## Living-Plan Agent Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Cost per resolved task | weekly | CFO + Head of Agent | +15% WoW |
| Cost per task (weighted) | weekly | CFO + Head of Agent | +10% WoW |
| Intervention rate | weekly | HITL Designer + Head of Agent | +3pp absolute |
| Task success rate | weekly | Eval Engineer | -3pp absolute |
| Tool-invocation reliability per tool | weekly | Tool Engineer | tool error rate >2% |
| Branch / loop ceiling breaches | weekly | Eval Engineer | any breach |
| HITL escalation cost share | monthly | CFO | >25% of agent COGS |
| Agent gross margin | monthly | CFO | -3pp MoM |
| Provider pricing watch | monthly | Head of AI / CTO | any change |
| Retry-overhead share | monthly | Tool Engineer | >15% of LLM cost |
| Tool-cost share | monthly | Tool Engineer | >30% of agent COGS |
| Model-migration reserve | quarterly | CFO + Head of AI | reserve drawdown |
| Irreversibility-incident reserve | quarterly | CFO + AI Safety Lead | any drawdown |

## References

- `references/saas-agent-unit-economics-template.md` — formulas, worked example, COGS waterfall
- `references/saas-agent-cost-per-task-calculator-spec.md` — calculator spec
- `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md` — parent AI unit economics
- `skills/07-marketing-sales-strategy/saas-agent-pricing-strategy/SKILL.md` — pricing that protects agent margin
- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — stress-test consumer
- `skills/meta-agent-bankability-and-investor-readiness/SKILL.md` — bankability scorecard consumer
- `skills/meta-living-plan-governance/SKILL.md` — governance discipline
- `book-extractions/agent-products-business-plan-audit-2026.md` — agent audit
- `book-extractions/ai-on-saas-business-plan-audit-2026.md` — AI-on-SaaS audit
- `book-extractions/mersch-hacking-saas-extraction.md` — CFO-grade SaaS discipline

## Africa / Uganda Application Notes

- Agent LLM + tool cost is USD-denominated; revenue often local currency. Per-resolution pricing must include FX corridor; the agent unit economics must hold across +/-20% FX swing (UGX 3,500-3,900/$, NGN 1,500-1,800/$, KES 128-145/$ as 2025/26 ranges).
- HITL cost in Uganda / Kenya / Nigeria / Rwanda is materially lower than US benchmarks (UGX 4,000-8,000/hour fully-loaded vs USD 30-60/hour US); this **shifts the agent-vs-human economics** — agents in Africa must beat a much lower human cost floor, and HITL fallback is cheaper to operate. Model both directions.
- Tool integration costs in Africa skew higher because of fragmented enterprise SaaS adoption — many tools are not yet API-first, requiring custom connectors. Model integration build cost as part of agent product cost, not as overhead.
- For agents serving WhatsApp / USSD / SMS / IVR channels, **channel costs are real per-task line items** (WhatsApp Business API per-conversation tariff; USSD aggregator per-session fee; SMS per-message; IVR per-minute). Add channel-cost line to per-task decomposition.
- In-region GPU for fine-tuned worker models (af-south-1, africa-south1, Liquid, Cassava, Raxio, Ethiopian AI Institute) prices 1.5-3x US/EU; model in-region inference premium if data residency is required.
- Cache-hit ratios in African vertical agents tend to be higher than US benchmarks because user task distributions are more concentrated (e.g. agri-extension agents see top 30 questions account for 60% of volume); model 40-60% cache.
- Audit-log retention costs in Africa can become binding when regulators (KE ODPC, NG NDPC, UG NITA-U, ZA Information Regulator) require multi-year retention; cost the retention period explicitly.
- Sovereign-AI procurement (KE Talanta, RW innovation, NG NITDA, ZA Presidential 4IR, EG infra) may require local hosting that raises per-task cost 30-80%; reflect in pricing if applicable.
