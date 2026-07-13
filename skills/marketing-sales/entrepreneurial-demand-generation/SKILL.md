---
name: entrepreneurial-demand-generation
description: Use when a business or startup plan must prove how customers become aware, interested, converted, retained, and referred; use `digital-marketing-strategy` for detailed online channel execution and `demand-forecasting` for quantitative demand estimates from operating data.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Entrepreneurial Demand Generation

## Overview

Use this skill to turn marketing sections into a credible demand system. It focuses on the first winnable customer segment, the buying trigger, the offer, the channel path, conversion, retention, and learning loop.

## Use When

- Drafting or reviewing a business plan's marketing, sales, or market validation logic.
- A plan lists channels but does not explain how demand is created.
- A startup, SME, or new product needs an early customer acquisition path.
- Marketing assumptions must connect to revenue, CAC, retention, and proof.

## Do Not Use When

- The task is only copywriting or social captions.
- The offer and customer are completely undefined; run intake or market analysis first.
- The user only needs a broad digital channel plan; use `digital-marketing-strategy` first.

## Required Inputs

- Offer, customer segment, geography, price point, revenue model, and current traction.
- Competitors or substitutes customers already use.
- Available channels, budget, sales capacity, and follow-up process.
- Evidence from customers, pilots, enquiries, website/social data, or market research.

## Workflow

1. Select the beachhead customer and buying trigger.
2. Define the first offer or hand-raiser that earns permission to follow up.
3. Map awareness to consideration, purchase, post-purchase, retention, and advocacy.
4. Assign channels by role, not popularity.
5. Define conversion steps, owner, tools, and follow-up cadence.
6. Attach metrics and assumptions to the financial model.
7. Identify the first 3 experiments that will validate demand.

## Quality Bar

- The demand path is specific enough for an operator to execute.
- Every channel has a role, CTA, owner, budget, and metric.
- Metrics cover the customer journey, not only awareness.
- Assumptions are testable and tied to financial projections.

## Anti-Patterns

- "We will use social media" with no offer, content role, or conversion path.
- Awareness goals with no sales follow-up.
- Broad target markets that hide the first customer segment.
- Growth assumptions without CAC, conversion, or retention logic.

## Outputs

- Demand-generation section or review.
- Customer journey metric map.
- Channel-role table.
- First-experiment plan.
- Assumptions and evidence gaps for validation.

## References

- `../../pipeline/07-marketing-sales-strategy/references/entrepreneurial-demand-and-brand-metrics.md` - demand creation, brand journey metrics, owned audience, and anti-pattern corrections.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Target customer, problem, offer, price, proof, journey, and sales constraints | Client intake and primary research | Required | Return hypotheses and a validation plan, not asserted demand |
| Funnel, channel, cohort, referral, sales, and retention evidence | CRM, analytics, sales records, interviews, and experiments | Conditional | Label stages and conversion rates unproven |
| Acquisition, revenue, refund, and contribution definitions | Chwezi Accounting Doctrine and finance model | Required for economic claims | Keep CAC and payback conclusions conditional |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Demand-generation system | Marketing-sales plan, founder, and operating team | Awareness, interest, conversion, retention, referral, owners, handoffs, and measures form one coherent path |
| Assumption and experiment backlog | Founder and growth owners | Each weak link has a hypothesis, test, measure, cost cap, stop rule, and decision date |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Funnel evidence map | Stage, customer evidence, metric, source, confidence, and owner | No stage is described only as a channel list |
| Economics reconciliation | CAC, contribution, payback, refund, and retention definitions | Commercial measures reconcile to the finance model and doctrine |

## Capability Contract

Read or search access is required; editing or mutation is allowed only with authorised permission.

Planning and review default to read-only. Do not launch campaigns, contact customers, spend budget, change prices, publish claims, or alter CRM data without explicit authority. Customer research must respect consent, privacy, and brand approval.

## Degraded Mode

Without primary research, funnel data, channel access, or finance definitions, return a hypothesis-led system and prioritised tests. Mark conversion, CAC, retention, and payback `not assessed`; do not replace evidence with benchmark averages.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Customer problem and trigger are unverified | Test problem and message before scaling channels | Paying to amplify a weak offer |
| Conversion works but retention fails | Repair onboarding, value, or fit before acquisition growth | Buying churn |
| One stage is the binding constraint | Concentrate experiments there | Scattered activity |
| CAC or payback does not reconcile | Apply Chwezi doctrine and pause scale | Growth that destroys cash |

## Workflow

1. Define the customer, trigger, job, alternative, offer, proof, price, and desired decision.
2. Map awareness through referral with named behaviours, frictions, owners, handoffs, and evidence.
3. Identify the binding constraint and distinguish facts from hypotheses.
4. Design the smallest ethical experiments with measures, cost caps, stop rules, and learning goals.
5. Reconcile acquisition and retention economics with current Chwezi doctrine and the finance model.
6. Sequence channel, sales, onboarding, retention, and referral work around the proven constraint.
7. Review results and recover from failure by revising the hypothesis, offer, or stage logic before adding spend.

## Quality Standards

The strategy must explain customer behaviour and handoffs, not merely name channels. Metrics need sources and definitions; economic scale decisions require reconciled CAC, contribution, retention, refund, and payback evidence.

## Anti-Patterns

- Listing Facebook, radio, and referrals as a strategy. Fix: map the customer behaviour each channel must cause.
- Scaling awareness before testing the offer. Fix: validate problem, message, proof, and conversion first.
- Treating leads as customers. Fix: define qualified, converted, retained, and referred states separately.
- Using blended CAC across unlike channels. Fix: calculate by channel, segment, period, and conversion basis.
- Ignoring sales-to-onboarding handoff. Fix: assign owner, timing, promise, evidence, and failure route.
- Calling benchmarks proof of demand. Fix: run primary research or experiments and qualify the plan.

## Worked Example

A clinic receives many WhatsApp enquiries but few bookings. Treat enquiry-to-booking as the binding constraint, test response time, proof, price clarity, and booking friction before buying more reach, and reconcile paid acquisition with contribution per completed visit.
<!-- dual-compat-end -->
