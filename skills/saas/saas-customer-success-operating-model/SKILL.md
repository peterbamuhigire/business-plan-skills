---
name: saas-customer-success-operating-model
description: Design the customer success operating model for a SaaS plan — high-touch vs mid-touch vs tech-touch segmentation, CSM ratios, customer health score, onboarding-to-renewal lifecycle, expansion playbook, save-the-customer protocol. CS is the NRR engine; this skill makes it a designed operating model, not a support afterthought.
---

# SaaS Customer Success Operating Model Skill

## Overview

Customer success is not support. CS is the revenue-protection and expansion engine that produces NRR (net revenue retention). For SaaS plans projecting NRR ≥ 100%, the CS operating model must be specified explicitly — touch model by segment, CSM ratios, health-score logic, onboarding pipeline, expansion playbook, save-protocol on cancellation.

## Use When

- Section 08 (Operations) or Section 07 (Marketing/Sales) for any SaaS plan
- Plan projects NRR > 100% (needs an expansion engine)
- Existing CS organisation is reactive (support tickets only, no proactive engagement)
- Onboarding is unstructured (high CAC + low activation)

## Required Inputs

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

## Outputs

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
