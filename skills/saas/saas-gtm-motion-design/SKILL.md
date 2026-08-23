---
name: saas-gtm-motion-design
description: Use when a new SaaS plan is being built — run this before Section 07 detailing. Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS GTM Motion Design Skill

## Overview

The GTM motion is the master upstream decision in any SaaS plan. It determines pricing structure, sales-team design, marketing channel mix, customer-success operating model, and the entire financial profile. This skill forces an explicit, defended GTM-motion choice — not the lazy default of "we'll do sales and marketing."

## Use When

- A new SaaS plan is being built — run this before Section 07 detailing
- The current GTM is producing inconsistent results (suggests motion-mismatch)
- The plan combines incompatible motions (e.g. $50k ACV with 30-day cycle)
- Considering a motion expansion (PLG → enterprise; or sales-led → channel)

## Do Not Use When

- The plan has already secured PMF and a working channel, and the motion is established and producing healthy economics


- For `saas-gtm-motion-design`, route to the corresponding cross-sector meta skill instead when recurring-revenue SaaS logic is not material.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Gtm Motion Design brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Target ICP and ACV range
- Customer state (do they know they have the problem? do they know solutions exist?)
- Product self-serve capability (can a customer use it without onboarding help?)
- Sales-cycle assumption
- Team composition / capability
- Geography (African enterprise sales cycles are 50–100% longer than US benchmarks)

## Workflow

1. **Map customer state** to one of the five WBD methodologies (DIY / Transactional / Solution / Consultative / Provocative).
2. **Map ACV** to compatible motions (see decision matrix in references).
3. **Match cycle length** — methodologies have characteristic cycle lengths; the plan's projection must reconcile.
4. **Decide PLG vs sales-led vs hybrid:**
   - PLG: high-volume, low-touch, self-serve, low ACV. Atlassian, Slack, Calendly, Notion path.
   - Sales-led: high-touch, low-volume, high ACV, complex deal. Salesforce, Workday, ServiceNow path.
   - Hybrid: PLG generates leads, sales-led converts to enterprise. HubSpot, Slack, Atlassian dual funnel.
   - Marketplace: facilitating buyers and sellers; different economics (Shopify, Stripe).
   - Channel-partner: VARs, SIs, distributors carry the sale. Common for vertical SaaS in fragmented markets.
5. **Design the funnel** for the chosen motion: top (Educate), middle (Prospect / Visit), bottom (Win), retention (Grow).
6. **Specify the named sales plays** that operate in the motion.
7. **Compute the team composition** from `saas-sales-org-design-and-capacity-planning`.
8. **Reconcile with pricing** — PLG needs simple, transparent pricing; enterprise needs custom pricing.
9. **Africa-test** — does the motion work given African sales-cycle / channel realities?

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the SaaS go-to-market motion and that the decision concerns PLG, sales-led, channel, marketplace, or hybrid motion.
- **Stop condition:** halt the affected conclusion if required evidence is missing (ACV, buyer process, sales cycle, channel evidence, and team capacity) or if the work could lead to this identified risk: choosing a fashionable motion that cannot recover CAC or close the buyer.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Single GTM motion declared (or hybrid with explicit boundaries)
- Motion reconciles with ACV, sales-cycle, customer state
- Named sales plays (not generic "outbound")
- Team composition computed from motion
- Pricing architecture compatible with motion
- Africa-adjusted cycle and motion if relevant

## Anti-Patterns

- "We'll do both PLG and enterprise" without explicit boundaries
- $50k ACV with 30-day projected cycle (impossible)
- Provocative methodology in markets with no incumbent budget (no money to be unlocked)
- PLG without a product that delivers value in <10 minutes
- Channel-partner motion without channel-partner economics modelled


- Applying the wrong neighbouring route to saas gtm motion design. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Gtm Motion Design deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Declared GTM motion with justification
- Funnel design (Educate / Prospect / Win / Grow stages with conversion benchmarks)
- Named sales plays
- Team composition specification (feeds into Section 09)
- Pricing-architecture compatibility check
- Africa-adjustment commentary

## References

- `references/saas-gtm-motion-decision-template.md` — full decision matrix and worked examples
- `book-extractions/vanderkooij-saas-sales-method-ae-extraction.md` — five methodologies
- `book-extractions/walling-saas-playbook-extraction.md` — dual-funnel cheat code
- `book-extractions/cotton-run-a-saas-business-extraction.md` — sales engine essay
- `skills/saas-sales-org-design-and-capacity-planning/SKILL.md` — sister skill

## Africa / Uganda Application Notes

- Enterprise sales cycles in African markets run 12–24 months for $50k+ deals; plan accordingly.
- Outbound sales is more cost-effective than US benchmarks because SDR labour is cheaper; African SaaS often runs outbound-first.
- Channel-partner motion via local resellers, SI partners (TechnoBrain, IPMC, Computech), or industry consortia is underused in African B2B SaaS; consider seriously for vertical plays.
- PLG works for products with global appeal and English-language UX; harder for vertically focused African plays where in-language onboarding matters.
- WhatsApp Business is a primary B2B sales channel; design the motion with WhatsApp at every stage.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| SaaS go-to-market motion decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to choosing a fashionable motion that cannot recover CAC or close the buyer. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the SaaS go-to-market motion; drafting the motion and capacity assumptions is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If ACV, buyer process, sales cycle, channel evidence, and team capacity cannot be obtained, return a qualified SaaS go-to-market motion covering only the checks that remain supportable. Leave this decision unresolved: PLG, sales-led, channel, marketplace, or hybrid motion. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: PLG, sales-led, channel, marketplace, or hybrid motion | Record the conclusion, source trail, owner, and review trigger in the SaaS go-to-market motion. | Risk of choosing a fashionable motion that cannot recover CAC or close the buyer |
| Material evidence conflicts or remains uncertain | Model each viable motion against ACV, buying process, sales cycle, CAC recovery, and team capacity before selecting the primary route. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: ACV, buyer process, sales cycle, channel evidence, and team capacity | Mark the decision on PLG, sales-led, channel, marketplace, or hybrid motion `not assessed` in the SaaS go-to-market motion, and send it to the growth lead and finance owner. | Otherwise, the work risks choosing a fashionable motion that cannot recover CAC or close the buyer |

## Quality Standards


Accept the SaaS go-to-market motion only when evidence is sufficient for this decision: PLG, sales-led, channel, marketplace, or hybrid motion. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of choosing a fashionable motion that cannot recover CAC or close the buyer.

## Worked Example


A low-ACV product proposes field sales across three countries. Compare sales-led payback with product-led and partner routes, then select the motion that matches buyer behaviour and CAC recovery.

## Product-readiness gate for the chosen motion

Do not select PLG merely because it is fashionable. Require evidence that the
target user can reach first value with a self-serve path, that onboarding can
defer nonessential setup, and that activation, retention, support load, and
conversion events are instrumented. If the path needs education, integration,
trust-building, or buyer coordination, model a sales-assisted or hybrid motion
instead and state the boundary.

For a launch or scale recommendation, pair the motion with one reversible
learning cycle: hypothesis, audience, behaviour, threshold, guardrail, owner,
time box, and decision consequence. Keep design-system and service capacity in
the operating and financial model.

Practitioner cross-checks: [Eleken SaaS launch](https://www.eleken.co/blog-posts/how-to-launch-a-saas-business), [startup scaling](https://www.eleken.co/blog-posts/scaling-your-startup-how-it-looks-from-the-product-design-perspective), and [design-system checklist](https://www.eleken.co/blog-posts/design-system-checklist). Use for prompts only; verify current commercial claims separately.

<!-- dual-compat-end -->
