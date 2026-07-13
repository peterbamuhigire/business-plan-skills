---
name: saas-customer-success-operating-model
description: Use when section 08 (Operations) or Section 07 (Marketing/Sales) for any SaaS plan. Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS Customer Success Operating Model Skill

## Overview

Customer success is not support. CS is the revenue-protection and expansion engine that produces NRR (net revenue retention). For SaaS plans projecting NRR ≥ 100%, the CS operating model must be specified explicitly — touch model by segment, CSM ratios, health-score logic, onboarding pipeline, expansion playbook, save-protocol on cancellation.

## Use When

- Section 08 (Operations) or Section 07 (Marketing/Sales) for any SaaS plan
- Plan projects NRR > 100% (needs an expansion engine)
- Existing CS organisation is reactive (support tickets only, no proactive engagement)
- Onboarding is unstructured (high CAC + low activation)

## Do Not Use When

- The request belongs to the neighbouring route. Use the cross-sector meta skill when the decision is not specific to recurring-revenue SaaS economics or operations.
- The available evidence cannot support a responsible customer success operating model conclusion; return the evidence gap instead of inventing one.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Customer Success Operating Model brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Customer segmentation by ACV
- Current activation, expansion, churn rates
- CS team headcount and role definitions (if any)
- Product complexity (drives onboarding intensity)

## Workflow

1. **Segment customers by touch model:**
   - High-touch (ACV > $50k): 1 CSM per 25-30 customers; named executive sponsor
   - Mid-touch ($10-50k): 1 CSM per 50-100 customers; quarterly business reviews
   - Tech-touch (<$10k): 1 CSM per 200-500; automation-driven; CSM as escalation
2. **Define customer health score** — composite of product usage frequency, depth (key features used), NPS, support tickets, payment health, executive-sponsor health. Scored 0-100.
3. **Map the lifecycle**: Sign-up → Kickoff → Onboarding → First Value → Activation → Adoption → Expansion → Renewal → (Churn? → Save) → Advocacy.
4. **Specify the onboarding pipeline** with explicit milestones, time-to-first-value SLA, and onboarding-complete criteria.
5. **Design QBR (quarterly business review)** for high-touch and mid-touch customers — reviewing usage, outcomes, expansion opportunities, renewal posture.
6. **Specify the expansion playbook** — when CSM raises the expansion conversation (usage hits 80% of seat allocation; module-fit signal from usage data; new use-case identified).
7. **Design the save-protocol** for cancellation — when a customer churns, who outreaches, in what window, with what offers (pause, downgrade, extended trial, account-rescue plan).
8. **Define escalation paths** — health-score amber/red triggers automated CSM action; account-team-led intervention; executive-sponsor escalation.
9. **Reconcile with financial plan** — CSM headcount × loaded cost must appear in COGS (recurring service revenue cost) or OpEx (S&M) consistently.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the customer-success operating model and that the decision concerns the touch model, escalation rule, and CSM capacity by segment.
- **Stop condition:** halt the affected conclusion if required evidence is missing (ACV segments, onboarding data, health signals, churn, and team capacity) or if the work could lead to this identified risk: promising NRR expansion without an owned customer lifecycle.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Touch model defined by segment with ratios
- Health score with named components and weights
- Onboarding pipeline with time-to-first-value SLA
- QBR cadence for high/mid-touch
- Expansion playbook with named triggers
- Save-protocol with cancellation outreach
- Living-plan cadence assigned

## Anti-Patterns

- "CS will handle support tickets" — that's support, not CS
- 1 CSM per 1,000 customers without automation
- No health score
- Onboarding measured only by signature date
- Expansion conversations only at renewal (12-month gap is too late)
- No save-protocol — churned customers gone forever


- Applying the wrong neighbouring route to saas customer success operating model. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Customer Success Operating Model deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Touch model + ratios
- Health score definition with weights
- Customer-lifecycle pipeline
- Onboarding milestones with SLA
- QBR template
- Expansion playbook
- Save protocol
- CSM headcount with cost roll-up

## References

- `references/saas-customer-success-operating-model.md` — full operating-model design and worked examples
- `book-extractions/cotton-run-a-saas-business-extraction.md` — churn discipline
- `book-extractions/mersch-hacking-saas-extraction.md` — CS cost in financial profile
- `book-extractions/garbugli-saas-email-marketing-playbook-extraction.md` — lifecycle email integration
- `skills/saas-unit-economics-and-cohort-model/SKILL.md` — NRR computation

## Africa / Uganda Application Notes

- High-touch CSM in Africa often doubles as field-implementation; budget travel.
- Mobile-first health-score dashboards because customers / executives use mobile primarily.
- WhatsApp is the dominant CS channel for real-time customer engagement — design WhatsApp groups per major customer.
- QBR can be conducted in person for high-touch / strategic accounts — disproportionately effective vs Zoom in African corporate culture.
- Renewal conversations must start 90+ days before contract end (vs 60 in US) due to procurement timelines.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Customer-success operating model decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to promising NRR expansion without an owned customer lifecycle. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the customer-success operating model; drafting playbooks without contacting customers or changing live workflows is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If ACV segments, onboarding data, health signals, churn, and team capacity cannot be obtained, return a qualified customer-success operating model covering only the checks that remain supportable. Leave this decision unresolved: the touch model, escalation rule, and CSM capacity by segment. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: the touch model, escalation rule, and CSM capacity by segment | Record the conclusion, source trail, owner, and review trigger in the customer-success operating model. | Risk of promising NRR expansion without an owned customer lifecycle |
| Material evidence conflicts or remains uncertain | Test the proposed touch model on one segment using onboarding load, health signals, and CSM capacity before fixing the service ratio. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: ACV segments, onboarding data, health signals, churn, and team capacity | Mark the decision on the touch model, escalation rule, and CSM capacity by segment `not assessed` in the customer-success operating model, and send it to the customer-success lead and finance owner. | Otherwise, the work risks promising NRR expansion without an owned customer lifecycle |

## Quality Standards


Accept the customer-success operating model only when evidence is sufficient for this decision: the touch model, escalation rule, and CSM capacity by segment. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of promising NRR expansion without an owned customer lifecycle.

## Worked Example


Enterprise customers need implementation visits while small accounts onboard in-product. Set separate touch models, health triggers, and CSM capacity; include travel and staffing costs in the financial plan.

<!-- dual-compat-end -->
