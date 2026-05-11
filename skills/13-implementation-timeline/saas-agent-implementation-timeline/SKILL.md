---
name: saas-agent-implementation-timeline
description: Agent rollout discipline tied to plan — shadow, supervised, agentic gates; eval-coverage gates; cost-gated launches; human-in-the-loop ramp-down; irreversibility-class-by-class autonomy expansion. Sits on top of `13-implementation-timeline` generic skill.
---

# SaaS Agent Implementation Timeline Skill

## Overview

Generic implementation timeline (handled by `13-implementation-timeline`) covers milestones, dependencies, critical path. **Agent implementation** must additionally encode the **shadow -> supervised -> agentic** progression as the dominant scaffolding, with eval-coverage gates, cost gates, drill gates, and AI Safety Lead sign-off at each transition.

## Use When

- Section 13 is being built for an agent-product plan
- A new agent capability is being launched
- An autonomy promotion is being planned
- A vertical / customer-specific rollout is being scheduled
- The plan must pass `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- The product is AI-feature only without agentic action — use generic `13-implementation-timeline`
- The agent is internal-efficiency only with no customer-facing action class progression — use generic implementation timeline
- The plan is pre-PMF with no operational evidence — use directional ladder and milestones, but do not over-engineer the gate model

## Required Inputs

- Agent capability scope
- Customer segment(s)
- Action class taxonomy (A/B/C/D)
- Eval-coverage baseline
- HITL capacity
- Drill cadence
- Reserve adequacy

## Workflow

1. **Define the rollout phases per agent capability:**
   - **Phase 0 — Shadow** — agent runs in parallel with human; human acts; agent output recorded but not used; eval data accrued
   - **Phase 1 — Supervised (Class A/B)** — agent acts on Class A / B actions; human reviews before commit on B
   - **Phase 2 — Supervised (Class C)** — agent acts on Class C; human approves above threshold; audit-log mandatory
   - **Phase 3 — Agentic within policy** — agent acts within policy on B/C; human reviews exceptionally; Class D requires human-final
   - **Phase 4 — Expanded autonomy** — additional Class C / D action types promoted

2. **Set gates between phases:**
   - Eval-coverage on the action class >=95%
   - Sample size in current phase (typically 5k-20k actions)
   - Incident-free duration (typically 90 days no sev-1)
   - AI Safety Lead sign-off
   - Drill executed for the new phase
   - Reserve adequacy confirmed
   - Customer notification / consent

3. **Cost-gated launch** — each phase has target cost-per-resolved-task; do not promote if cost trending above target.

4. **HITL ramp-down** — as supervised -> agentic, HITL reviewer capacity required falls; redeploy reviewers to higher-stake action classes or to eval / quality.

5. **Customer-by-customer rollout** — typically pilot with 1-3 design partners through Phase 1; expand through Phase 2; broaden through Phase 3.

6. **Multi-country / multi-language rollout** — sequence by regulatory readiness and language coverage; do not skip countries' regulator engagement.

7. **Build the implementation Gantt** — phases x customer segments x time; identify the critical path.

8. **Risk-tag the critical path** — which gates are most likely to slip; what's the contingency?

9. **Wire to living-plan governance** — monthly review of phase progress; quarterly autonomy expansion review with AI Safety Lead sign-off.

## Quality Bar

- Shadow -> supervised -> agentic phases declared per capability
- Eval-coverage / sample-size / incident-free / drill / reserve / consent gates explicit
- Cost-per-resolved-task target per phase
- HITL ramp-down schedule
- Customer rollout sequence
- Multi-country sequence by regulator readiness
- Critical path identified with risk tags
- Living-plan cadence assigned

## Anti-Patterns

- Skipping shadow phase
- Going from supervised to agentic without sample-size threshold
- Cost-target not part of gate
- Customer notification skipped on Class C/D promotion
- AI Safety Lead sign-off implicit not explicit
- HITL ramp-down without redeployment plan
- Multi-country rollout without per-country regulator engagement

## Outputs

- Phased rollout per capability
- Gates with criteria per phase
- Cost-target per phase
- HITL ramp-down schedule
- Customer rollout sequence
- Implementation Gantt
- Critical path with risk tags

## Living-Plan Cadence Defaults

| Element | Cadence | Owner |
|---|---|---|
| Phase progress review | monthly | Head of Agent + AI Safety Lead |
| Eval-coverage by phase | monthly | Eval Engineer |
| Cost-per-resolved by phase | weekly | CFO + Head of Agent |
| Drill cadence by phase | monthly | AI Safety Lead |
| Autonomy expansion review | quarterly | AI Safety Lead + Head of Agent + CEO |
| Customer rollout review | monthly | Head of CS |
| Regulator engagement per country | quarterly | Compliance |

## References

- `skills/13-implementation-timeline/SKILL.md` — parent
- `skills/03-products-services/saas-agent-product-strategy-and-roadmap/SKILL.md` — roadmap input
- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — risk input
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — cost gate
- `book-extractions/agent-products-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Multi-country sequencing** in Africa: each country has its own regulator (ODPC / NDPC / NITA-U / Info Reg / NCSA / PDPC / NTRA) plus sectoral regulators; sequence countries by regulator-engagement maturity, not by market size
- **Channel rollout** — WhatsApp / USSD / SMS / IVR per country; rollout per channel has its own ramp
- **Local-language rollout** — sequence languages by user volume and eval-coverage readiness
- **Public-sector pilots** — typically slower than commercial; budget 6-18 months from MoU to first production
- **Sovereign-AI procurement** — adds 3-12 months for residency / local-entity / local-citizen evidence
