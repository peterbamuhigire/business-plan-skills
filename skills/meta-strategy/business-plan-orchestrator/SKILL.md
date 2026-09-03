---
name: business-plan-orchestrator
description: Use when governing a serious business-plan engagement end to end, from intake and evidence design through sections, model, challenge, assembly, rendering, and release; use 00-plan-assembly only for final packaging and proposal-architect for bids or tenders.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Business Plan Orchestrator

<!-- dual-compat-start -->

## Use When

- Governing a full bank, DFI, investor, grant, owner-board, feasibility, or strategic-partner business-plan engagement.
- Resuming a multi-stage plan where evidence, section, model, review, and release states must remain traceable.
- Deciding whether a completed-looking plan may progress to assembly, rendering, committee rehearsal, or external release.

## Do Not Use When

- For final document ordering alone, use `00-plan-assembly` instead.
- For a single section with no cross-plan dependencies, route to the owning pipeline skill.
- For bids, tenders, EOIs, or RFP responses, use `proposal-architect`; for a pitch-only engagement, use `pitch-deck`.

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Engagement brief, decision, audience, jurisdiction, scope, and authority | `00-client-intake` and engagement owner | Yes | Stop drafting and return the missing intake questions. |
| Evidence plan and claim register | Digital research engine and section owners | Yes | Block each load-bearing unsupported claim; do not replace it with plausible filler. |
| Section, model, risk, regulatory, and funding work products | Pipeline and specialist skills | Conditional | Mark the dependent stage blocked and return it to the named owner. |
| Release bundle and cross-engine handoff evidence | Release owner and external engines | Yes for release | Produce a blocked bundle from the template; never infer a pass. |

## Workflow

1. Freeze the decision brief: audience, funding instrument, jurisdiction, reporting framework, business stage, deliverable family, permissions, and release authority. Stop if the decision or audience is unresolved; recover through `00-client-intake`.
2. Build the claim-and-evidence plan before prose. Apply the digital research engine's source evaluation, evidence discipline, verification, and synthesis controls. Block unsupported load-bearing claims and assign gaps to owners.
3. Select the smallest section stack using the audience route in [the stage-gate map](references/end-to-end-stage-gates.md). Add country, sector, finance, valuation, sustainability, digital, website, and execution overlays only when triggered.
4. Draft and review one decision-bearing section or model assumption at a time. Inspect the existing evidence and dependency chain before changing it, exercise its base and downside case, make one deliberate refinement, then run business-logic review, writing quality, and the anti-slop audit. Return contradictions to the owning section instead of reconciling them silently.
5. Build the integrated model and funding logic. Apply the Chwezi finance doctrine, identify the reporting basis, reconcile narrative and workbook assumptions, run formula-map and stress tests, and stop on a finance blocker.
6. Run synthesis, regulatory screens, due diligence, bankability or valuation, and audience-specific red-team review. Preserve dissent, conditions, countercases, and unresolved checks.
7. Assemble only approved versions through `00-plan-assembly`, then execute every applicable handoff in [the cross-engine delivery contract](../../../references/cross-engine-delivery-contract.md). Missing render, reviewer, security, spreadsheet, research, finance, or document evidence remains `not-assessed`, never passed.
8. Populate the release-evidence bundle, validate it with `tools/release-gate/validate_release_bundle.py`, and release only when the gate returns `release`. Recover a blocked bundle by closing the named finding and rerunning all affected upstream gates.

## Decision Rules

| Condition or evidence | Action | Failure or risk avoided |
|---|---|---|
| Decision, audience, jurisdiction, or authority is missing | Stop at intake and request the exact missing field | A generic plan optimised for no real decision |
| A load-bearing claim lacks verified claim-level evidence | Block the claim and section; record a gap and owner | Fabricated market, legal, or commercial certainty |
| Narrative, model, funding ask, and implementation plan disagree | Return the conflict to the owning skills and retain no preferred value until reconciled | Polished but internally impossible plans |
| A mandatory finance, regulatory, workbook, security, or professional review fails | Keep release state `blocked` regardless of narrative score | Score averaging conceals a knockout risk |
| All applicable stages and handoffs pass with evidence and release authority is recorded | Validate the bundle, assemble the final package, and release | Untraceable or premature publication |

## Quality Standards

- One governing thesis connects customer evidence, market choice, operating model, economics, implementation, risk, and funding.
- Every load-bearing claim exposes source, warrant, assumption, countercase, confidence, and decision implication.
- Model assumptions, plan prose, use of funds, milestones, and downside cases reconcile to named versions.
- A failed or unavailable gate has an owner, consequence, recovery action, and restart condition.
- Release evidence includes handoffs, reviewer notes, audit log, checklist, render state, and explicit authority; client submission remains a human-authorised action.

## Anti-Patterns

- Drafting all sections before evidence design. Correction: create the claim-and-evidence plan first.
- Treating section completion as plan completion. Correction: reconcile dependencies and run synthesis and audience gates.
- Averaging a blocker into a high readiness score. Correction: apply blocker precedence.
- Letting a downstream editor choose between conflicting figures. Correction: return the conflict to the owning model or section.
- Calling a Markdown script a rendered deliverable. Correction: retain renderer output and visual-review evidence.
- Treating an official portal as proof of a copied fact. Correction: verify the exact claim, effective date, jurisdiction, and source record.
- Publishing because the automated bundle passes. Correction: require recorded release authority and the applicable human or professional review.

## Outputs

| Output artefact | Consumer | Acceptance condition |
|---|---|---|
| Stage register and dependency map | Section owners and engagement lead | Every required stage has owner, status, evidence, blocker, and restart condition. |
| Cross-engine handoff register | Finance, research, design, document, spreadsheet, and security reviewers | Applicability, input version, output evidence, acceptance result, caveat, and receiver are explicit. |
| Release-evidence bundle | Release reviewer and `00-plan-assembly` | Schema validation passes and the release decision follows blocker precedence. |
| Blocked-release report | Engagement owner | Every failed or unassessed mandatory check names consequence, owner, and recovery action. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Stage and decision trace | Release-bundle JSON plus source-linked records | A reviewer can reproduce progression from intake to release. |
| Model and finance trace | Formula map, reconciliations, stress cases, doctrine gate | No broken reference, unexplained external link, missing required scenario, or finance blocker remains. |
| Finalisation trace | Render record, reviewer notes, audit log, checklist, and authority record | Files exist, statuses agree, and unavailable checks are not reported as passes. |

## Capability Contract

This skill may read authorised engagement artefacts, coordinate drafting, execute local validators, and write the requested plan assets. It may not invent evidence, alter approved management assumptions without traceable owner approval, certify legal or financial compliance, contact funders, spend money, submit applications, or publish externally without explicit authority. Committee simulation and automated validation are decision support, not approval.

## Degraded Mode

Without network evidence, finance tooling, a renderer, a specialist engine, or reviewer access, continue only with the verified subset. Mark the affected stage or handoff `not-assessed`, narrow the conclusion, issue the smallest recovery request, and keep release blocked where the missing check is mandatory. Do not convert tool absence into a pass.

## Worked Example

A DFI plan has complete prose and an audited workbook, but its environmental and social screen and PDF render review are unavailable. Record both handoffs as `not-assessed`, preserve the model result, and return a blocked release bundle even if the committee score is high.

## References

- [End-to-end stage gates](references/end-to-end-stage-gates.md) — load for audience routes, stage ownership, and restart rules.
- [Cross-engine delivery contract](../../../references/cross-engine-delivery-contract.md) — load before finance, research, design, document, spreadsheet, or security handoff.
- [Business-plan release gate](../../../docs/quality-gates/business-plan-release-gate.md) — load for blocker precedence and the final release decision.
- [Release-evidence bundle template](../../../templates/release-evidence-bundle.json) — copy and replace every placeholder before validation.

<!-- dual-compat-end -->
