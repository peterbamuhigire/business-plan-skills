---
name: saas-ai-funding-stage-playbook
description: AI overlay on the SaaS funding stage ladder (pre-seed → seed → A → B → growth). Specifies AI-specific milestone breakpoints, what an AI plan must show at each stage, AI-specialist vs generalist-SaaS vs sovereign-AI vs DFI AI-for-good fund mapping, and Africa-specific funding pathways. Use whenever Section 11 of an AI-feature-led SaaS plan is being built or a fundraise is being planned.
---

# SaaS AI Funding Stage Playbook Skill

## Overview

The standard SaaS funding ladder (bootstrap → F&F → pre-seed → seed → A → B → growth) sits in `saas-valuation-and-fundraising-strategy` / `saas-funding-stage-playbook.md`. AI startups raise differently: AI-specialist funds set different bars, generalist SaaS funds discount or ignore the AI thesis, sovereign-AI funds (in select jurisdictions) have separate envelopes, AI-for-good DFIs / grantmakers run different rubrics. This skill installs the AI overlay.

## Use When

- Section 11 of an AI-feature-led SaaS plan is being built
- A fundraise is being planned and investor-archetype targeting must be intentional
- A founder is asking which funders fit and which don't
- DFI / grant pathway is being explored alongside commercial fundraise

## Do Not Use When

- AI is internal-efficiency only — use `11-funding-request` + `saas-funding-stage-playbook.md`
- Plan is bank-loan only (CAMPARI; AI is incidental)

## Required Inputs

- ARR / MRR + AI-attribution share (from `saas-ai-market-and-tam`)
- AI bankability scorecard
- AI moat score
- Valuation range with AI adjustments
- Use-of-proceeds plan (AI-specific spend)
- Geography / regulatory context

## Workflow

1. **Identify the stage** based on standard SaaS criteria (ARR, growth, team size, customer count, GM, NRR) **plus** AI-specific signals (eval coverage, model-mix maturity, AI revenue share, governance maturity).
2. **Apply the AI-specific milestone breakpoints** per `references/saas-ai-funding-stage-playbook.md`:
   - **Pre-seed**: AI prototype in production with ≥1 paying customer; eval suite started; cost-per-tenant directional
   - **Seed**: 10-30 AI-paying customers; AI Gross Margin >50%; eval coverage >40%; AI-cost-as-%-of-ARR <15%; governance policy drafted
   - **Series A**: $1-3M AI-ARR or $3-5M total ARR with AI driving net new; AI GM >65%; eval coverage >60%; cost engineering visible; moat thesis testable
   - **Series B**: $5-15M ARR; Rule-of-40-AI adjusted ≥35; AI GM trajectory positive; vendor concentration <70%; governance committee operating
   - **Growth**: $20M+ ARR; Rule of 40 ≥40; AI premium clearly priced into valuation; multi-region; AI compliance for enterprise
3. **Map to investor archetype** per `references/ai-investor-archetype-map.md`:
   - **AI-specialist funds**: a16z AI, Index AI, Bessemer AI, Cohere founders fund, Khosla AI, Lightspeed AI, AIX Ventures, AI Grant, Conviction, South Park Commons, Costanoa, Greylock AI track
   - **Generalist SaaS funds**: Sequoia, Accel, Benchmark, Iconiq, Battery, Insight, Tiger, Coatue — AI thesis must be defensible but not the primary pitch
   - **Sovereign-AI funds**: G42 / MGX (UAE), French sovereign-AI envelope, German / EU AI funds, Saudi Vision 2030 AI envelopes — usually for AI-platform / sovereign-AI archetype
   - **DFIs with AI envelopes**: IFC AI envelopes, AfDB AI-for-development, Norfund, BII (formerly CDC), FMO, Proparco, Swedfund
   - **AI-for-good grantmakers**: Mozilla African Innovation Mradi, GSMA AI for Impact, IDRC AI4D, Lacuna Fund (training-data grants), Google.org AI for Social Good, Microsoft AI for Good, Patrick J. McGovern Foundation, Gates AI envelopes
   - **Africa-focused funds with AI thesis**: Norrsken22, TLcom, Partech Africa, P1 Ventures, 4DX, Renew Capital, Future Africa, Catalyst Fund, Ventures Platform, Antler Africa
4. **Set the use-of-proceeds AI lines** — AI infra (compute, model APIs, vector DBs); AI hiring; eval pipeline build-out; AI governance / compliance build; training-data acquisition; AI sales / marketing.
5. **Set the milestones the round funds** in AI-specific terms — eval coverage target, AI GM target, AI-revenue target, AI moat-evidence target, governance maturity target.
6. **Decide grant + commercial blend** — AI-for-good grants can fund training-data, eval pipeline, ethics infrastructure, local-language coverage without dilution; commercial rounds fund growth.
7. **Address foundation-model platform risk** explicitly in the pitch — investors will ask. Best practice: name it, show the moat that survives it, show the multi-provider strategy.
8. **Wire to bankability and valuation** — outputs of `meta-ai-bankability-and-investor-readiness` and `meta-ai-valuation-adjustments` feed this skill.
9. **Wire to living plan** — round-readiness reviewed quarterly; investor-pipeline maintained; data-room kept continuously DD-ready.

## Stage Readiness Table (indicative)

| Stage | AI ARR | AI GM | Eval coverage | Governance | Moat evidence |
|---|---|---|---|---|---|
| Pre-seed | $0-$50k | n/a / >40% | >40% on top features | policy in draft | thesis only |
| Seed | $50k-$500k | >50% | >50% | policy + decision log | first proprietary-data signal |
| A | $1-$5M | >65% | >60% | committee operating | data accrual + workflow moat |
| B | $5-$20M | >70% | >75% | full RACI + eval program | proven moat + 1-2 dimensions |
| Growth | $20M+ | >75% | >85% | external audit / SOC2 + AI | 3+ moat dimensions defensible |

## Quality Bar

- Stage declared with AI-specific evidence
- Investor archetype targeted; not "all VCs"
- Use-of-proceeds has AI-specific lines, not "team + product + sales"
- Milestones the round funds stated in AI-specific terms
- Foundation-model platform-risk addressed
- Grant + commercial blend considered for Africa-context plans
- Cross-references to bankability and valuation

## Anti-Patterns

- One pitch deck for all investor archetypes
- "Raising $5M" with no AI-specific use-of-proceeds breakdown
- Targeting generalist SaaS funds with an AI pitch and getting AI-discount valuations
- Ignoring AI-for-good DFI / grant pathways in Africa-context plans
- No moat-survives-platform-risk story
- Round milestones in generic SaaS terms, not AI terms

## Outputs

- Stage declaration with AI evidence
- Investor archetype map (who fits, who doesn't, in priority order)
- Use-of-proceeds with AI-specific lines
- Round-fund milestones in AI terms
- Foundation-model platform-risk response
- Grant + commercial blend plan
- Investor-pipeline list

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Stage readiness review | quarterly | CEO + CFO | round-not-ready signal |
| Investor pipeline | monthly | CEO | conversion stall |
| Use-of-proceeds vs spend | monthly | CFO | overspend on AI infra |
| Round-fund milestones | monthly | CEO + CFO | slip >45 days |
| Investor archetype map | semi-annual | CEO | new fund category emerges |
| Grant pipeline | quarterly | CEO + Grants lead | grant cycle slip |

## References

- `references/saas-ai-funding-stage-playbook.md` — full stage ladder + investor-archetype detail
- `references/ai-investor-archetype-map.md` — named funds per archetype with thesis notes
- `skills/saas-valuation-and-fundraising-strategy/SKILL.md` — base SaaS funding skill
- `skills/meta-ai-bankability-and-investor-readiness/SKILL.md` — bankability that supports stage
- `skills/meta-ai-valuation-adjustments/SKILL.md` — valuation overlay
- `skills/11b-grant-proposal/saas-ai-for-good-grant-proposal/SKILL.md` — grant pathway
- `country-context/africa-regional/africa-ict-saas-market-context.md` — Section 7 funding ecosystem

## Africa / Uganda Application Notes

- **Blended-finance approach** is often optimal: commercial seed + AI-for-good grant funding training-data + ethics + local-language coverage.
- **DFI cycles** are slower (6-18 months) than commercial VC; plan runway accordingly.
- **Sovereign-AI tender pre-funding** is emerging in select African jurisdictions (RW, KE, NG, ZA, EG) — tender wins can be quasi-funding events.
- **Diaspora capital + African-roots funds** (Norrsken22, P1, TLcom, Partech Africa, 4DX, Future Africa) increasingly comfortable with AI thesis; international AI-specialist funds still rare in African deals.
- **Use-of-proceeds in DFI plans** should include training-data acquisition, local-language curation, local AI-team hiring, governance build-out — these are often DFI / grant priorities.
- **FX exposure** on USD-funded plans must be modelled as a runway risk.
