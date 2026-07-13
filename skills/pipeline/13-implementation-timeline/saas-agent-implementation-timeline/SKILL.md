---
name: saas-agent-implementation-timeline
description: Use when producing or reviewing the saas agent implementation timeline component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Approved initiatives, dependencies, procurement lead times, owners, costs, milestones, and funding availability for saas agent implementation timeline | Section owners, operations plan, financial model, and implementation lead | Yes | If absent, a dependency, owner, lead time, or funding release date is unavailable, keep the activity unscheduled or show a range and identify the decision date. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Dependency-aware implementation schedule with gates, owners, costs, and recovery actions | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent implementation timeline exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent implementation timeline release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Critical-path map, milestone acceptance tests, resource reconciliation, and delay scenario | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent implementation timeline decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent implementation timeline review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent implementation timeline, the controlling focus is agent prototype, evaluation, tool permissions, pilot, human fallback, production gate, and scale dependencies. This skill may plan and review delivery sequencing; it may not procure, assign people, change live operations, or declare milestones complete without owner evidence. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent implementation timeline, loss of evidence about agent prototype, evaluation, tool permissions, pilot, human fallback, production gate, and scale dependencies activates degraded mode. If the controlling saas agent implementation timeline evidence is unavailable, the same boundary applies. When a dependency, owner, lead time, or funding release date is unavailable, keep the activity unscheduled or show a range and identify the decision date. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent implementation timeline, a milestone begins before its prerequisite, funding, procurement, or acceptance evidence exists| resequence it, expose the critical-path impact, and define the recovery option | Calendar dates disguise infeasible dependencies and unfunded work |
| For saas agent implementation timeline, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent implementation timeline decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent implementation timeline, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete dependency-aware implementation schedule with gates, owners, costs, and recovery actions, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent implementation timeline decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect approved initiatives, dependencies, procurement lead times, owners, costs, milestones, and funding availability and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce dependency-aware implementation schedule with gates, owners, costs, and recovery actions with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Dependency-aware implementation schedule with gates, owners, costs, and recovery actions must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Critical-path map, milestone acceptance tests, resource reconciliation, and delay scenario must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent implementation timeline, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent implementation timeline, treating an unavailable approved initiatives, dependencies, procurement lead times, owners, costs, milestones, and funding availability as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing dependency-aware implementation schedule with gates, owners, costs, and recovery actions that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

An agent pilot is scheduled before tool-permission review and failure-set evaluation. Sequence sandbox integration, evaluation, human-approval rehearsal, limited pilot, and production gate; show rollback ownership if the evaluation slips.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent implementation timeline; no local deep-dive reference is declared.
- For saas agent implementation timeline claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
