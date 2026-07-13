---
name: saas-agent-integration-deep
description: Use when producing or reviewing the saas agent integration deep component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS Agent Integration Deep Skill

## Overview

Section 14 (AI Integration) treats AI homogeneously by default. **Agent businesses require a distinct treatment**: the AI is not a feature inside a product — the agent IS the product (single-agent vertical) or the agent IS the platform (multi-agent orchestration). This skill installs the agent overlay on Section 14 so that the plan reads correctly as an agent-product plan rather than a SaaS-with-AI-feature plan.

## Use When

- Section 14 is being built for an agent-product plan
- The plan is being rewritten from "SaaS with AI" to "agent-product"
- Investor diligence on the agent layer specifically is upcoming
- The plan must compose with all the agent-specific skills

## Do Not Use When

- The product is AI-feature only without agentic action — use `14-ai-integration` standard SKILL alone
- The agent is internal-efficiency only (no customer-facing agent action) — generic Section 14 plus internal-tooling commentary is sufficient
- The plan is too early (pre-PMF) for full agent-layer commitment — note the agent direction without bolting on the full overlay

## Required Inputs

- Agent archetype declared
- Agent architecture
- Cross-references to all agent-specific skill outputs

## Workflow

1. **Declare the agent archetype** on the first page of Section 14:
   - Single-agent customer-service / resolution agent
   - Single-agent operations agent
   - Multi-agent orchestrated workflow
   - Vertical agentic SaaS
   - Agent platform / agent-as-infrastructure
2. **Compose the agent layer** as a distinct sub-section within Section 14:
   - Agent architecture (planner / workers / critic; tool registry; channels)
   - Autonomy ladder per customer job
   - Tool-registry strategy
   - Eval-loop and drill cadence
   - HITL design and policy
   - Audit-log design
   - Kill-switch design
   - Foundation-model platform-risk posture
   - Multi-channel UX (WhatsApp / USSD / SMS / IVR / web / voice / mobile-money)
3. **Cross-reference every agent skill output:**
   - Unit economics: `saas-agent-unit-economics-and-cogs`
   - Pricing: `saas-agent-pricing-strategy`
   - Moat: `saas-agent-moat-and-wrapper-risk`
   - Risk: `saas-agent-risk-and-stress-test`
   - Talent: `saas-agent-talent-strategy`
   - Product strategy: `saas-agent-product-strategy-and-roadmap`
   - Funding: `saas-agent-funding-stage-playbook`
   - Implementation: `saas-agent-implementation-timeline`
   - Sustainability / ethics: `saas-agent-sustainability-and-ethics`
   - Bankability: `meta-agent-bankability-and-investor-readiness`
   - Valuation: `meta-agent-valuation-adjustments`
   - Reporting: `meta-agent-board-and-investor-reporting`
4. **Reconcile with the standard AI Integration narrative** — agent layer extends, does not replace, the AI-as-feature narrative; if there is AI-as-feature in addition to agent, both must be addressed cleanly
5. **Reconcile with Section 10 unit economics** — agent cost lives in agent UE, not generic AI UE
6. **Reconcile with Section 12 risk** — agent risks live in agent risk register, not generic risk
7. **Reconcile with Section 16 sustainability / ethics** — agent ethics is a distinct sub-section

## Quality Bar

- Archetype declared
- Agent layer treated as distinct product class
- Cross-references to every agent skill present
- Reconciliation with Sections 10 / 12 / 16 visible
- No "AI feature" language where the product is actually agentic
- AI-as-feature and agent-layer clearly separated if both present

## Anti-Patterns

- In saas agent integration deep, treating agent as "AI feature" in Section 14
- Cost / risk / ethics in generic AI sub-sections only (must be agent-specific)
- Skipping archetype declaration
- "We use AI" language where "we are an agent business" is the truth
- Cross-references absent
- Implementation timeline in Section 13 not reconciled to autonomy ladder

## Outputs

- Section 14 agent sub-section
- Archetype declaration
- Agent architecture description
- Cross-reference table to all agent skills
- Reconciliation notes for Sections 10 / 12 / 16

## References

- `skills/14-ai-integration/SKILL.md` — parent
- All agent-specific skills (listed above)
- `book-extractions/agent-products-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- Multi-channel agent UX is mandatory in African plans (see africa-agent-context-extension)
- Local-language coverage is a Section 14 dimension
- Sovereign-AI / data-residency posture is a Section 14 dimension
- In-region inference posture is a Section 14 dimension where applicable

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Prioritised use cases, process baseline, data rights, architecture, vendor options, safety controls, capability evidence, and economics for saas agent integration deep | Process owners, technical lead, legal/privacy review, vendors, and approved model | Yes | If absent, data rights, baseline performance, evaluation evidence, or human fallback is unavailable, hold the use case at discovery and return the control or test needed. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Staged AI or agent integration plan with use-case gates, controls, costs, and fallback operations | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent integration deep exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent integration deep release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Use-case readiness score, build/buy decision, data/control review, cost model, evaluation plan, and rollback path | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent integration deep decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent integration deep review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent integration deep, the controlling focus is agent use-case readiness, tool registry, action permissions, evaluation, observability, rollback, and operating cost. This skill may analyse and prototype within authorised data and tools; it may not expose client data, purchase services, deploy to production, grant autonomous permissions, or claim model capability without testing. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent integration deep, loss of evidence about agent use-case readiness, tool registry, action permissions, evaluation, observability, rollback, and operating cost activates degraded mode. If the controlling saas agent integration deep evidence is unavailable, the same boundary applies. When data rights, baseline performance, evaluation evidence, or human fallback is unavailable, hold the use case at discovery and return the control or test needed. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent integration deep, automation value is plausible but error cost or action authority exceeds the tested control boundary| reduce autonomy, add human approval, narrow scope, or reject the use case | AI theatre or unsafe automation adds cost and operational liability without customer value |
| For saas agent integration deep, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent integration deep decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent integration deep, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete staged ai or agent integration plan with use-case gates, controls, costs, and fallback operations, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent integration deep decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect prioritised use cases, process baseline, data rights, architecture, vendor options, safety controls, capability evidence, and economics and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce staged ai or agent integration plan with use-case gates, controls, costs, and fallback operations with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Staged AI or agent integration plan with use-case gates, controls, costs, and fallback operations must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Use-case readiness score, build/buy decision, data/control review, cost model, evaluation plan, and rollback path must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent integration deep, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- Treating an unavailable prioritised use cases, process baseline, data rights, architecture, vendor options, safety controls, capability evidence, and economics as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing staged ai or agent integration plan with use-case gates, controls, costs, and fallback operations that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A procurement agent can draft purchase orders but its tool can also submit them. Restrict the tool to draft mode, evaluate policy and supplier errors, rehearse approval and rollback, and enable submission only with explicit human authority.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent integration deep; no local deep-dive reference is declared.
- For saas agent integration deep claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
