---
name: saas-lifecycle-email-and-retention
description: Use when section 07 of a SaaS plan. Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS Lifecycle Email & Retention Skill

## Overview

40-60% of SaaS first-time users check out the product and never come back without lifecycle email (Garbugli). Lifecycle email is the lowest-cost, highest-leverage retention and expansion mechanism. This skill installs the canonical seven-sequence architecture, the data infrastructure that powers it, and the multi-channel orchestration with WhatsApp / SMS that African SaaS needs.

## Use When

- Section 07 of a SaaS plan
- Plan has signups but low activation or low trial-to-paid conversion
- NRR is below 100% and there's no systematic retention engine
- The team is sending email manually rather than through automation

## Do Not Use When

- The request belongs to the neighbouring route. Use the cross-sector meta skill when the decision is not specific to recurring-revenue SaaS economics or operations.
- The available evidence cannot support a responsible lifecycle email and retention conclusion; return the evidence gap instead of inventing one.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Lifecycle Email And Retention brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Customer lifecycle stages
- Current email programme (sequences, frequency, performance)
- Email service provider (ESP) currently in use
- CRM / event-tracking infrastructure
- Customer segmentation

## Workflow

1. **Audit current email programme** against the seven sequence families (Garbugli):
   - Cold (prospects)
   - Welcome / onboarding (new signups / new paid)
   - Behavioural / lifecycle (active users — feature adoption)
   - Upgrade / upsell / expansion (existing paid)
   - Retention (at-risk customers)
   - Referral (happy customers)
   - Reactivation (churned customers)
2. **Identify gaps** — which sequences are missing or under-developed?
3. **Build the data implementation plan:**
   - Customer journey map
   - Custom fields / properties needed
   - Event tracking (signup-source, plan, last-login, feature flags, MRR, NPS)
   - User segments (Power Users, At-Risk, Trial-Day-3, Cancelled-30-Days)
   - Operating rules (frequency caps, exclusions, time-of-day, A/B framework)
4. **Prioritise sequence build order** — welcome/onboarding first (biggest single ROI), then retention save, then expansion, then referral, then cold, then reactivation.
5. **Design ESP architecture** — single ESP (Customer.io, HubSpot, Mailchimp+Mautic, Iterable) or separation (Postmark for transactional + Customer.io for lifecycle).
6. **Set up deliverability infrastructure**:
   - SPF, DKIM, DMARC for sending domain
   - Subdomain segregation (transactional, marketing, sales)
   - List hygiene (suppress bounces, 6-month-inactive)
   - Warm-up plan for new sending IPs
7. **Integrate with WhatsApp / SMS** — orchestrate channel-by-stage (email for content/long-form, WhatsApp for real-time/urgent/relational).
8. **Specify the 5-minute rule** — qualified-lead first-touch within 5 minutes of trigger.
9. **Design A/B testing cadence** — subject lines, send times, CTA copy.
10. **Define team composition** by ARR stage (Garbugli):
    - $0-$1M ARR: founder + freelancer
    - $1-5M: 1 dedicated lifecycle marketer
    - $5-20M: team of 3
    - $20M+: full lifecycle function

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the lifecycle retention programme and that the decision concerns which sequence fires for each lifecycle state.
- **Stop condition:** halt the affected conclusion if required evidence is missing (consent basis, product events, segments, deliverability, and churn signals) or if the work could lead to this identified risk: automating irrelevant or non-compliant messages that damage retention.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- All seven sequence families addressed (or explicit reason for skip)
- Data infrastructure (events, properties, segments) specified
- ESP architecture defined
- Deliverability infrastructure (SPF/DKIM/DMARC/subdomain/warm-up) set up
- WhatsApp / SMS orchestration where Africa-relevant
- Team composition scales with ARR
- A/B testing cadence installed

## Anti-Patterns

- Send-and-pray bulk emails without segmentation
- No event-driven triggers
- Mailchimp campaign-style emails for behavioural triggers
- Ignoring deliverability (sending from main domain)
- Internal benchmark obsession ("industry-average open rate")
- WhatsApp / SMS not in the orchestration for Africa plans
- Sales asking for "leads" without lifecycle nurture


- Applying the wrong neighbouring route to saas lifecycle email and retention. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Lifecycle Email And Retention deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Sequence-by-sequence design (welcome, behavioural, etc.) with goals, triggers, structure, KPIs
- Data implementation plan (events, properties, segments)
- ESP architecture
- Deliverability setup checklist
- WhatsApp / SMS orchestration plan
- A/B testing cadence
- Team composition by ARR stage

## References

- `book-extractions/garbugli-saas-email-marketing-playbook-extraction.md` — full source
- `book-extractions/kennedy-magnetic-marketing-extraction.md` — attraction / conversion / retention
- `skills/digital-marketing-strategy/SKILL.md` — sister skill for broader digital marketing
- `skills/saas-customer-success-operating-model/SKILL.md` — CS sister skill (CSM + email orchestration)

## Africa / Uganda Application Notes

- **WhatsApp Business** is often more effective than email for African B2B engagement — use WhatsApp for real-time, urgent, relational; email for content, transactional, long-form.
- **SMS** remains powerful for OTP, payment confirmations, urgent retention (Africa's Talking, Twilio).
- **Mobile-first design** — most opens are on mobile; lightweight HTML or plain-text outperforms designed templates.
- **Code-switching subject lines** (English + one local-language phrase) often outperforms pure English for African markets.
- **POPIA / NDPR / Kenya DPA / Uganda DPPA** require explicit consent and data-handling — build opt-in mechanics into signup, maintain suppression lists.
- **Deliverability from African IPs** to global inboxes is harder — use ESP providers with US/EU sending infrastructure rather than self-hosting in African datacentres.
- **Public-sector / NGO** customers often have stricter email-permission controls — design separate segment with appropriate handling.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Lifecycle retention programme decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to automating irrelevant or non-compliant messages that damage retention. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the lifecycle retention programme; drafting sequences; sending or platform changes require approval is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If consent basis, product events, segments, deliverability, and churn signals cannot be obtained, return a qualified lifecycle retention programme covering only the checks that remain supportable. Leave this decision unresolved: which sequence fires for each lifecycle state. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which sequence fires for each lifecycle state | Record the conclusion, source trail, owner, and review trigger in the lifecycle retention programme. | Risk of automating irrelevant or non-compliant messages that damage retention |
| Material evidence conflicts or remains uncertain | Test the disputed sequence on an eligible segment with a holdout and agreed retention event; do not infer impact from opens alone. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: consent basis, product events, segments, deliverability, and churn signals | Mark the decision on which sequence fires for each lifecycle state `not assessed` in the lifecycle retention programme, and send it to the lifecycle owner and privacy or compliance reviewer. | Otherwise, the work risks automating irrelevant or non-compliant messages that damage retention |

## Quality Standards


Accept the lifecycle retention programme only when evidence is sufficient for this decision: which sequence fires for each lifecycle state. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of automating irrelevant or non-compliant messages that damage retention.

## Worked Example


New users receive the same messages after activation and after inactivity. Split the lifecycle states, define the triggering events and consent basis, and measure retention rather than opens alone.

<!-- dual-compat-end -->
