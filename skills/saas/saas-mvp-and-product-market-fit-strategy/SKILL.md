---
name: saas-mvp-and-product-market-fit-strategy
description: Use when a SaaS or ICT plan is pre-PMF, with no clear retention signal, repeatable channel, or ARR above $200k. Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS MVP & Product-Market-Fit Strategy Skill

## Overview

Pre-PMF SaaS plans need a different discipline than scale-stage plans. The product is unproven, the market is hypothesised, and the founder is the operating system. This skill installs the MVP-to-PMF strategy: define what PMF means, what tests it, what cadences feed it, and what gates the company passes through (Walling: MVP → PMF → Escape Velocity).

## Use When

- A SaaS / ICT plan is pre-PMF (no clear retention signal; no repeatable channel; ARR <$200k)
- A plan claims PMF but lacks the evidence
- A founder is deciding what to build in the next 90 days
- An accelerator / pre-seed investor is asking what milestones unlock the next round

## Do Not Use When

- ARR > $500k with sustained retention — the plan is past PMF; use scale-stage skills
- The company is in a paid pilot with one customer — that's pre-MVP


- For `saas-mvp-and-product-market-fit-strategy`, route to the corresponding cross-sector meta skill instead when recurring-revenue SaaS logic is not material.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Mvp And Product Market Fit Strategy brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Current customer count, ARR, MRR
- Retention data (if any cohort visibility exists)
- Customer-interview log
- Current feature roadmap
- Founder time allocation

## Workflow

1. **Define PMF for this specific plan** — what's the measurable signal?
   - Sean Ellis 40% test: ≥40% of users say they'd be "very disappointed" without the product
   - Retention curve flattening: after month 3, monthly retention rate is stable (not decreasing)
   - Organic referral: ≥25% of new users come from word-of-mouth without paid acquisition
   - Walling shortcut: $10-20k MRR with stable retention
2. **Define MVP scope** — the minimum feature set required to deliver value to the ICP. Resist scope creep. Vertical-first beats horizontal at MVP stage.
3. **Install the customer-conversation cadence** — 10+ customer interviews per month (Walling discipline). Owner: founder. Log: shared doc. Quarterly synthesis.
4. **Triage features** using Walling's three buckets:
   - **Crackpot** (10-15%): outside use case, vision, capability — say no
   - **No-Brainer** (15-25%): obvious value, build now
   - **In-Between** (60-75%): apply three filter questions: (1) what's the use case? (2) what % will use it? (3) does it fit product vision?
5. **Plan the path to PMF** with explicit milestones:
   - Month 1-3: MVP build, first 10 customers
   - Month 4-6: Iteration on usage; second 20 customers
   - Month 7-9: Retention curve diagnosis; Sean Ellis test
   - Month 10-12: PMF signal achieved or pivot decision
6. **Plan the path to Escape Velocity** (Walling) — at least one repeatable channel with payback <18 months.
7. **Define the pivot framework** — what failures trigger which pivots:
   - Customer pull but wrong segment → segment pivot
   - Segment right but feature mismatch → feature pivot
   - Segment + feature right but unit economics fail → pricing / packaging pivot
   - Nothing working → category pivot or stop
8. **Cross-reference**: Section 03 (Products), Section 04 (Market), Section 13 (Implementation Timeline) — milestones in this skill drive milestones there.
9. **Living-plan cadence** — weekly customer-conversation digest; monthly PMF-signal review; quarterly pivot-vs-persevere decision.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the MVP-to-PMF learning plan and that the decision concerns whether the product remains at MVP, reaches PMF, pivots, or stops.
- **Stop condition:** halt the affected conclusion if required evidence is missing (target user, retention cohorts, interviews, and referral evidence) or if the work could lead to this identified risk: declaring PMF from acquisition or founder enthusiasm.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Explicit PMF definition for this plan (not generic)
- Customer-conversation cadence installed with named owner
- MVP scope is narrow and defensible
- Feature triage applied to current backlog
- Path to PMF has named milestones and metrics
- Pivot framework explicit before pivots are needed
- Plan honest about pre-PMF status (vs claiming PMF without evidence)

## Anti-Patterns

- "We have PMF because we have customers" — customers ≠ retention ≠ love
- Building horizontal at MVP stage (too much surface area)
- Founder not in 10+ customer conversations per month
- "We'll pivot if it doesn't work" without pivot framework
- Hiring sales before PMF (founder must be the seller pre-PMF)
- Optimising before validating


- Applying the wrong neighbouring route to saas mvp and product market fit strategy. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Mvp And Product Market Fit Strategy deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Defined PMF signal (specific metric and target)
- MVP scope document (in/out features)
- Customer-conversation cadence with owner / log location
- Feature triage of current backlog (Crackpots / No-Brainers / In-Betweens)
- Milestone roadmap to PMF
- Pivot framework
- Pre-PMF financial expectations (don't aim for unit economics; aim for retention signal)

## References

- `book-extractions/walling-saas-playbook-extraction.md` — PMF, Escape Velocity, feature triage
- `book-extractions/garbugli-saas-email-marketing-playbook-extraction.md` — onboarding-to-activation discipline
- `book-extractions/vanderkooij-saas-sales-method-fundamentals-extraction.md` — customer-centric questioning
- `skills/03-products-services/SKILL.md` — sister skill for product narrative
- `skills/idea-testing/SKILL.md` — pre-MVP idea validation

## Africa / Uganda Application Notes

- WhatsApp-based customer interviews are the dominant cadence (lower friction than scheduled Zoom calls).
- Vertical-first MVP is the strategic default for African SaaS (local-context expertise = moat).
- "PMF" in African SaaS is often reached at lower MRR ($5-10k) because TAM is smaller; adjust Walling's $10-20k benchmark.
- In-person customer visits remain disproportionately powerful in African business culture — budget for travel during the MVP stage.
- Founder must be multi-lingual in the buyer's language for high-touch customer interviews — pre-PMF research can't be outsourced.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| MVP-to-PMF learning plan decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to declaring PMF from acquisition or founder enthusiasm. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the MVP-to-PMF learning plan; updating the approved experiment backlog is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If target user, retention cohorts, interviews, and referral evidence cannot be obtained, return a qualified MVP-to-PMF learning plan covering only the checks that remain supportable. Leave this decision unresolved: whether the product remains at MVP, reaches PMF, pivots, or stops. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: whether the product remains at MVP, reaches PMF, pivots, or stops | Record the conclusion, source trail, owner, and review trigger in the MVP-to-PMF learning plan. | Risk of declaring PMF from acquisition or founder enthusiasm |
| Material evidence conflicts or remains uncertain | Run the next retention or behaviour experiment with a predeclared PMF signal and preserve the pivot option until cohorts repeat it. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: target user, retention cohorts, interviews, and referral evidence | Mark the decision on whether the product remains at MVP, reaches PMF, pivots, or stops `not assessed` in the MVP-to-PMF learning plan, and send it to the product lead and founder. | Otherwise, the work risks declaring PMF from acquisition or founder enthusiasm |

## Quality Standards


Accept the MVP-to-PMF learning plan only when evidence is sufficient for this decision: whether the product remains at MVP, reaches PMF, pivots, or stops. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of declaring PMF from acquisition or founder enthusiasm.

## Worked Example


Sign-ups rise after a promotion, but successive cohorts do not retain. Keep the product pre-PMF, interview the retained minority, and test the next behaviour change against a predeclared retention signal.

## Activation and scale discipline

Define PMF with product-specific evidence rather than a fixed universal
threshold. Track a named first-value event separately from signup, then inspect
repeat behaviour, retention, referrals or renewal, support burden, and delivery
capacity. A polished prototype, acquisition spike, or founder enthusiasm cannot
close the PMF gate.

Before recommending scale, confirm a repeatable value path, a maintainable
design/component system, onboarding that minimises nonessential setup, and an
operating/support capacity plan. If evidence is mixed, preserve a reversible
experiment and explicit pivot/stop rule.

Practitioner cross-checks: [Eleken SaaS launch](https://www.eleken.co/blog-posts/how-to-launch-a-saas-business), [startup scaling](https://www.eleken.co/blog-posts/scaling-your-startup-how-it-looks-from-the-product-design-perspective), and [mobile onboarding](https://www.eleken.co/blog-posts/mobile-app-onboarding-best-practices). Exclude their market statistics, time estimates, and case outcomes.

<!-- dual-compat-end -->
