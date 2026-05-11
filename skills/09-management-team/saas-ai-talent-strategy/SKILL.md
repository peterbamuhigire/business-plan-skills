---
name: saas-ai-talent-strategy
description: AI talent strategy for a SaaS plan — ML / applied-ML engineer, AI product manager, prompt / RAG engineer, AI infra / MLOps, AI safety / eval lead, AI policy / compliance, domain-expert-as-AI-trainer roles. Maps roles to ARR milestones; specifies African talent pool (Lelapa AI, Masakhane, ALU, Andela AI tracks, Carnegie Mellon Africa, Deep Learning Indaba network); applies outsource-to-build-to-buy logic. Use whenever AI capability is load-bearing to the plan.
---

# SaaS AI Talent Strategy Skill

## Overview

Generic management-team plans say "we'll hire AI engineers." AI-aware investors and DFIs require specificity: which AI roles, at which ARR milestone, sourced from where, at what comp, with what tenure expectation, with what training-and-retention plan. This skill installs the discipline.

## Use When

- Section 09 of an AI-feature-led plan is being built
- Hiring plan is being designed
- A funder has asked specifically how AI capability will be built
- Plan is targeting public-sector / regulated-vertical AI procurement where local-talent requirements apply
- Plan needs to defend AI moat with team-as-moat evidence

## Do Not Use When

- AI is internal-efficiency only — use `09-management-team` standard
- Plan has no AI capability requirement

## Required Inputs

- AI roadmap with milestones (`saas-ai-product-strategy-and-roadmap`)
- ARR plan
- Geography of operation
- Comp budget envelope
- Current team composition

## Workflow

1. **Map AI roles to ARR milestones** per `references/saas-ai-talent-and-org-design-template.md`:
   - **Pre-PMF**: founding ML / applied-ML engineer (often founder); AI-aware product person
   - **$0-$1M**: + RAG engineer; + AI product manager
   - **$1-$5M**: + MLOps / AI infra; + eval / QA lead; + domain-expert-trainer
   - **$5-$20M**: + AI safety / governance lead; + AI policy / compliance; + 2-4 ML engineers
   - **$20M+**: Head of AI / VP AI; + research-engineering function (if proprietary models)
2. **Decide outsource-to-build-to-buy** for each role / function:
   - **Outsource**: fractional CTO / fractional Head of AI for pre-seed; specialist consultancies for one-off fine-tuning
   - **Build**: domain-aware roles (RAG engineers, AI PMs, eval leads) that learn the business
   - **Buy**: senior leadership (Head of AI) typically bought at series A or later; comp + equity matter
3. **Source from the African AI talent map** per `references/africa-ai-talent-map.md`:
   - **Lelapa AI** (Johannesburg) — local-language AI research / startup
   - **Masakhane** — pan-African NLP research network
   - **AIMS network** (South Africa, Senegal, Cameroon, Ghana, Tanzania, Rwanda) — Master's-level AI
   - **Carnegie Mellon Africa** (Rwanda) — top-tier AI / ML talent
   - **ALU AI track** (Rwanda / Mauritius)
   - **Andela AI talent pool**
   - **Deep Learning Indaba** alumni network — annual continental AI conference
   - **Black in AI Africa** chapter networks
   - **InstaDeep** alumni network (BioNTech subsidiary; African AI precedent)
   - **University CS departments** — Makerere AI Lab, Nairobi, Witwatersrand, Cape Town, Cairo, Pretoria, Cape Town, ABU Zaria, Lagos, Addis Ababa, Khartoum
4. **Set comp benchmarks** in local + USD:
   - Junior ML engineer: $1,500-3,500/mo (varies by country per Africa context Section 6)
   - Mid ML engineer: $3,000-5,500/mo
   - Senior ML engineer: $5,000-9,000/mo (in-country); $8,000-15,000/mo (remote-international)
   - Head of AI: $8,000-15,000/mo + equity
5. **Design the retention strategy** — equity ladder, technical leadership track, conference / paper / publishing budget, eval-and-research time, sabbatical policy. AI talent in Africa is recruited aggressively by US/EU companies; retention is a real problem.
6. **Design the training / upskilling plan** — internal AI literacy for non-AI roles; external training budgets; partnerships with AIMS, ALU, Lelapa.
7. **Map the diversity / inclusion targets** — gender, country, language, vertical-experience. DFIs require this; AI ethics requires this.
8. **Build the contingency plan** — what if Head of AI leaves? key-person dependency mitigation. (Trigger-replan event in `meta-living-plan-governance`.)
9. **Wire to risk** — talent risk in `saas-ai-risk-and-stress-test`.
10. **Wire to living plan** — hiring plan monthly review, retention quarterly, AI talent landscape semi-annual.

## Quality Bar

- AI roles mapped to ARR milestones with explicit titles and seniority
- Outsource-to-build-to-buy decision per role
- Sourcing strategy specifies African talent pool sources, not generic
- Comp benchmarks in local + USD
- Retention strategy explicit
- Training / upskilling plan
- Diversity / inclusion targets
- Key-person contingency
- Cross-reference to risk register

## Anti-Patterns

- "We'll hire AI talent" without role specification
- Generic LinkedIn-sourcing assumption when most African senior AI talent isn't on the public market
- Comp pegged to local SMB benchmarks (AI talent is paid at international tier)
- No retention plan when international competition is intense
- Diversity stated as aspiration without target
- Key AI personnel undefined / unprotected (no NDA, no IP assignment, no non-compete)

## Outputs

- AI org chart by ARR milestone
- Hiring plan with role × milestone × source × comp × seniority
- Sourcing strategy with named talent pools
- Retention plan
- Training / upskilling plan
- Diversity / inclusion targets
- Key-person contingency
- Cross-references to risk and operations

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Hiring plan status | monthly | Head of People + CTO | slip >30 days |
| AI team attrition | quarterly | Head of People | >20% annualised |
| Comp benchmark review | semi-annual | Head of People + CFO | market shift >15% |
| Retention plan effectiveness | quarterly | Head of People | departure of senior AI |
| Training / upskilling spend | quarterly | Head of People | underspend or no progress |
| AI talent landscape | semi-annual | CTO | new talent pool emerges or shrinks |
| Diversity targets | quarterly | Head of People | regression from target |

## References

- `references/saas-ai-talent-and-org-design-template.md` — role × ARR milestone matrix + comp + sourcing
- `references/africa-ai-talent-map.md` — sourcing detail per network
- `skills/09-management-team/SKILL.md` — generic management-team flow
- `skills/saas-sales-org-design-and-capacity-planning/SKILL.md` — GTM team plan (sister)
- `country-context/africa-regional/africa-ict-saas-market-context.md` — Section 6 talent context

## Africa / Uganda Application Notes

- **Remote-international competition** — top African ML talent earns US/EU comp working remotely; plan equity-and-mission as differentiators or accept higher cash comp.
- **Distributed-team-across-Africa** is now feasible (Nairobi, Lagos, Cape Town, Kigali, Cairo, Accra, Kampala) — design for it from day one if AI capability is load-bearing.
- **Local-context as moat** — hiring AI talent who understand cooperative governance, mobile-money rails, public-sector procurement is itself a moat that offshore talent cannot replicate quickly.
- **DFI requirements** often include local-talent-building, gender targets, training commitments — embed in talent plan from start.
- **Sovereign-AI tender requirements** often include local-citizen-engineer headcount minima — plan for compliance.
- **Visa / mobility constraints** between African countries can affect distributed-team viability; plan for it.
