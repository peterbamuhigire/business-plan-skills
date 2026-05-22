---
name: saas-agent-integration-deep
description: Agent layer atop AI integration — how the plan treats agents as a distinct product class within Section 14. Cross-references all agent-specific skills. Use whenever Section 14 is being built for a plan with an agent or multi-agent product, in conjunction with the standard `14-ai-integration` SKILL.
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

- Treating agent as "AI feature" in Section 14
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
