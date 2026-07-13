---
name: meta-critical-thinking-business-logic
description: Use when use before drafting serious business-plan sections where the business model, market, operations, financials, funding ask, risk, sustainability, or implementation logic matters. Use the relevant plan-section skill for section drafting.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Critical Thinking and Business Logic Meta-Skill

## Overview

Use this meta-skill as the business-plan suite's thinking and achievability gate. It turns critical thinking, essential questions, mental models, design thinking, and strategic reasoning into practical tests for market logic, revenue logic, cost logic, operating reality, funding fit, risk, and implementation feasibility.

## Use When

- Use before drafting serious business-plan sections where the business model, market, operations, financials, funding ask, risk, sustainability, or implementation logic matters.
- Use after section drafts exist but before `meta-consulting-synthesis`, `meta-financial-stress-test`, `meta-bankability-scoring`, `meta-due-diligence`, or `00-plan-assembly`.
- Use when a plan sounds polished but may not yet make logical, commercial, operational, or financing sense.
- Use when assumptions are thin, numbers feel optimistic, or recommendations need stronger evidence and reasoning.

## Do Not Use When

- Do not use as a substitute for market research, financial modelling, due diligence, or country-context verification.
- Do not use to make weak evidence sound stronger than it is.
- Do not call a plan bankable, investor-ready, or achievable just because this review has been run; fix the gaps it finds.


- For `meta-critical-thinking-business-logic`, route to the relevant plan-section skill instead when the request is section drafting rather than cross-section analysis.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Critical Thinking Business Logic brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Business concept, country context, target audience, and funding mode.
- Draft sections or working notes where available.
- Market evidence, customer evidence, competitor evidence, operations assumptions, financial assumptions, implementation plan, risks, and funding ask.

## Workflow

1. Define the reader's real decision: lend, invest, grant, partner, approve, or operate.
2. Map the plan's load-bearing claims into claim, evidence, warrant, assumption, countercase, and implication.
3. Use `references/reasoning-achievability-gate.md` to apply essential questions, mental models, design-thinking checks, strategic logic, and business-sense tests.
4. Separate facts from assumptions, projections, targets, hopes, and recommendations.
5. Test whether the market, operations, team, financials, funding ask, risk, and implementation plan mutually support each other.
6. Produce a fix list ranked by decision impact: fatal gap, major weakness, evidence gap, modelling gap, or wording issue.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the business-logic review and that the decision concerns which contradictions or evidence gaps block achievability.
- **Stop condition:** halt the affected conclusion if required evidence is missing (load-bearing claims, assumptions, and operating-finance links) or if the work could lead to this identified risk: calling a plan feasible because its prose is coherent.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Every major claim is evidence-backed or clearly labelled as an assumption.
- The business has a visible route from customer need to revenue, margin, cash flow, and repayment or investor return.
- Financial projections follow operational capacity, market access, pricing, and implementation timing.
- Risks include downside scenarios and practical mitigations.
- The plan is achievable with the stated people, money, assets, systems, licences, suppliers, and timeline.

## Anti-Patterns

- Treating market size as proof of sales.
- Treating enthusiasm, social need, or founder passion as proof of demand.
- Forecasting revenue without customer acquisition, conversion, capacity, pricing, and working-capital logic.
- Copying an industry profile into a plan without adapting it to the specific business.
- Hiding weak assumptions inside confident prose.
- Presenting a funding ask that does not match implementation priorities or cash-flow timing.
- Calling risks manageable without triggers, owners, mitigations, and fallback actions.


- Applying the wrong neighbouring route to meta critical thinking business logic. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Critical Thinking Business Logic deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Reasoning map for the business case.
- Assumption and evidence register.
- Achievability and feasibility findings.
- Cross-section contradiction list.
- Prioritised fixes before synthesis, scoring, or assembly.

## References

- `references/reasoning-achievability-gate.md` - essential questions, mental-model checks, design-thinking pass, strategic reasoning, business-sense tests, and final achievability gate.
- `../meta-consulting-synthesis/SKILL.md` - use after this skill to turn corrected analysis into one decision-grade storyline.
- `../meta-financial-stress-test/SKILL.md` - use after financial assumptions are explicit.
- `../meta-bankability-scoring/SKILL.md` - use after contradictions and evidence gaps have been addressed.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Business-logic review decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to calling a plan feasible because its prose is coherent. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the business-logic review; annotating claims and fixes in the review copy is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If load-bearing claims, assumptions, and operating-finance links cannot be obtained, return a qualified business-logic review covering only the checks that remain supportable. Leave this decision unresolved: which contradictions or evidence gaps block achievability. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which contradictions or evidence gaps block achievability | Record the conclusion, source trail, owner, and review trigger in the business-logic review. | Risk of calling a plan feasible because its prose is coherent |
| Material evidence conflicts or remains uncertain | Trace each competing claim through customer, operating, cash, and funding consequences; leave any broken chain as a blocking finding. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: load-bearing claims, assumptions, and operating-finance links | Mark the decision on which contradictions or evidence gaps block achievability `not assessed` in the business-logic review, and send it to the plan owner and executive sponsor. | Otherwise, the work risks calling a plan feasible because its prose is coherent |

## Quality Standards


Accept the business-logic review only when evidence is sufficient for this decision: which contradictions or evidence gaps block achievability. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of calling a plan feasible because its prose is coherent.

## Worked Example


A plan converts national demand directly into first-year revenue. The review exposes missing reach, conversion, capacity, and cash links, then blocks the achievability claim until those assumptions reconcile.

<!-- dual-compat-end -->
