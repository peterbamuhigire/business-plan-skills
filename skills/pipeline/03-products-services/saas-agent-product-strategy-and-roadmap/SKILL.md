---
name: saas-agent-product-strategy-and-roadmap
description: Agent product strategy — capability ladder (assist, suggest, supervise, agentic), autonomy progression with gates, build/buy/host of orchestration framework, vertical agent libraries, tool-registry strategy, eval-driven product development for agents. Sits on top of `saas-ai-product-strategy-and-roadmap`.
---

# SaaS Agent Product Strategy & Roadmap Skill

## Overview

AI product strategy covers feature-vs-platform, AI-native vs AI-augmented, build-buy-host-orchestrate, model-router architecture, eval-driven development, feature roadmap by ARR. **Agent product strategy** adds the **autonomy ladder** as a first-class plan element and forces gating between rungs, plus tool-registry strategy and vertical-agent-library posture.

## Use When

- Section 03 is being built for an agent-product plan
- An AI feature roadmap is being upgraded to an agent roadmap
- An autonomy expansion decision is on the table
- A build / buy / host of orchestration framework is being decided
- The plan must pass `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- Product is AI-feature only — use `saas-ai-product-strategy-and-roadmap`
- Product is internal-efficiency only

## Required Inputs

- Agent archetype (single-agent, multi-agent, vertical, platform)
- Customer-job-to-be-done with action class taxonomy
- Eval-coverage snapshot
- Tool registry inventory
- Customer-success / deployment evidence

## Workflow

1. **Declare the autonomy ladder** for each customer job:
   - **Assist** — agent provides information; human acts
   - **Suggest** — agent proposes action; human approves and acts
   - **Supervise** — agent acts; human reviews each action before commit
   - **Agentic** — agent acts within policy; human reviews exceptionally
2. **Define gates** between rungs:
   - Eval coverage threshold (e.g. >=95% on action class)
   - Sample-size threshold (e.g. >=10,000 actions in supervised mode)
   - Incident-free duration (e.g. >=90 days no sev-1)
   - AI Safety Lead sign-off
   - Customer notification / consent
3. **Tool-registry strategy** — which tools proprietary; which third-party; abstraction layer; vendor strategy.
4. **Build / buy / host / orchestrate** decisions per `references/saas-agent-product-strategy-template.md`:
   - Orchestration framework: typically buy (LangGraph / CrewAI / Semantic Kernel) and build proprietary on top
   - Foundation models: typically buy (provider mix)
   - Specialist models: buy or fine-tune
   - Local-language models: buy or train (vertical play)
5. **Vertical agent libraries** — if vertical strategy, what reusable agent components / templates / starter packs accelerate deployment?
6. **Eval-driven roadmap** — every roadmap item ships with eval coverage; no shipping without eval.
7. **Cost-gated launches** — every roadmap item ships with a target cost-per-resolved-task and is held until margin holds.
8. **Roadmap by ARR milestone** — pre-PMF (one Class B agent); seed (one Class C agent); A (multiple Class C/D agents); B (vertical agent libraries + platform plays).
9. **Model-deprecation strategy** — model-router architecture; versioned eval; canary rollout; reserve.
10. **Wire to risk** (`saas-agent-risk-and-stress-test`) and unit economics (`saas-agent-unit-economics-and-cogs`).

## Quality Bar

- Autonomy ladder declared per customer job
- Gates between rungs specified
- Tool-registry strategy explicit (proprietary vs commodity)
- Build / buy / host decisions stated with reasoning
- Eval-driven roadmap — no item without eval coverage
- Cost-gated launches — target cost-per-resolved on roadmap
- Roadmap mapped to ARR milestones
- Model-deprecation strategy explicit

## Anti-Patterns

- Jumping to "agentic" without gates
- Ship-then-eval (instead of eval-then-ship)
- Building orchestration framework from scratch unless platform thesis requires
- Vertical agent without reusable library posture
- Roadmap items without target cost-per-resolved
- "We'll switch models if cheaper" without router architecture
- Customer notified after autonomy expansion, not before

## Outputs

- Autonomy ladder per customer job
- Gates between rungs
- Tool-registry strategy
- Build / buy / host decisions
- Roadmap by ARR milestone
- Model-router architecture
- Cost-gated launch criteria
- Cross-references to risk and unit economics

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Autonomy expansion review | quarterly | AI Safety Lead + Head of Agent + CEO | proposed level-up |
| Eval coverage by action class | monthly | Eval Engineer | gap on roadmap item |
| Cost-per-resolved target tracking | weekly | CFO + Head of Agent | off target |
| Tool registry proprietary share | quarterly | Tool Engineer | falling |
| Model-router policy | quarterly | Head of AI / CTO | new model class viable |
| Vertical agent library reuse rate | quarterly | Head of Product | falling |

## References

- `references/saas-agent-product-strategy-template.md` — build / buy decisions; ladder design
- `skills/03-products-services/saas-ai-product-strategy-and-roadmap/SKILL.md` — parent
- `skills/06-competitive-analysis/saas-agent-moat-and-wrapper-risk/SKILL.md` — moat input
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — cost gate
- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — risk
- `book-extractions/agent-products-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- Vertical agent library reuse is high in Africa (multi-country deployment of same vertical agent); plan for this
- Local-language coverage is a roadmap dimension on every customer-facing agent
- Channel-first design (WhatsApp / USSD / SMS / IVR) is a roadmap dimension
- Model-router should include local-language specialist models (Lelapa AI, Masakhane, Awarri) where relevant
- In-region inference roadmap item if sovereign-AI procurement targeted
