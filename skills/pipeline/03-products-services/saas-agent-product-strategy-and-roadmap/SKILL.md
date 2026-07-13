---
name: saas-agent-product-strategy-and-roadmap
description: Use when producing or reviewing the saas agent product strategy and roadmap component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Validated AI or agent use cases, customer evidence, architecture constraints, and roadmap economics for saas agent product strategy and roadmap | Product owner, customer research, technical lead, and approved model | Yes | If absent, customer outcome evidence, cost data, or safety constraints are unavailable, hold the affected roadmap item at discovery and return the missing validation test. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Evidence-gated product roadmap with build/buy/host/orchestrate decisions | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent product strategy and roadmap exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent product strategy and roadmap release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Use-case scorecard, roadmap gate decisions, and dependency register | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent product strategy and roadmap decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent product strategy and roadmap review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent product strategy and roadmap, the controlling focus is agent jobs, action authority, tool integrations, evaluation gates, human fallback, and roadmap economics. This skill may analyse product and architecture options; it may not approve model spend, production deployment, autonomous actions, or unsupported AI capability claims. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent product strategy and roadmap, loss of evidence about agent jobs, action authority, tool integrations, evaluation gates, human fallback, and roadmap economics activates degraded mode. If the controlling saas agent product strategy and roadmap evidence is unavailable, the same boundary applies. When customer outcome evidence, cost data, or safety constraints are unavailable, hold the affected roadmap item at discovery and return the missing validation test. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent product strategy and roadmap, an AI or agent feature has novelty but no measurable customer outcome or affordable operating path| defer it, define the experiment and exit criterion, and keep it out of the funded roadmap | Roadmap theatre commits capital before value, cost, and safety are known |
| For saas agent product strategy and roadmap, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent product strategy and roadmap decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent product strategy and roadmap, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete evidence-gated product roadmap with build/buy/host/orchestrate decisions, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent product strategy and roadmap decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect validated ai or agent use cases, customer evidence, architecture constraints, and roadmap economics and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce evidence-gated product roadmap with build/buy/host/orchestrate decisions with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Evidence-gated product roadmap with build/buy/host/orchestrate decisions must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Use-case scorecard, roadmap gate decisions, and dependency register must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent product strategy and roadmap, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent product strategy and roadmap, treating an unavailable validated ai or agent use cases, customer evidence, architecture constraints, and roadmap economics as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing evidence-gated product roadmap with build/buy/host/orchestrate decisions that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A support agent demo answers FAQs but has no resolution-rate baseline or escalation control. Hold it at pilot, define outcome, cost, and unsafe-action thresholds, and fund deployment only after the gates pass.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent product strategy and roadmap; no local deep-dive reference is declared.
- For saas agent product strategy and roadmap claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
