---
name: saas-lifecycle-email-and-retention
description: Design the SaaS lifecycle email and retention programme — the seven sequences (cold, welcome/onboarding, behavioural, upgrade/expansion, retention, referral, reactivation), data infrastructure, deliverability discipline, and integration with WhatsApp / messaging. Lifecycle email is the highest under-valued ARR lever in African SaaS.
---

# SaaS Lifecycle Email & Retention Skill

## Overview

40-60% of SaaS first-time users check out the product and never come back without lifecycle email (Garbugli). Lifecycle email is the lowest-cost, highest-leverage retention and expansion mechanism. This skill installs the canonical seven-sequence architecture, the data infrastructure that powers it, and the multi-channel orchestration with WhatsApp / SMS that African SaaS needs.

## Use When

- Section 07 of a SaaS plan
- Plan has signups but low activation or low trial-to-paid conversion
- NRR is below 100% and there's no systematic retention engine
- The team is sending email manually rather than through automation

## Required Inputs

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

## Outputs

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
