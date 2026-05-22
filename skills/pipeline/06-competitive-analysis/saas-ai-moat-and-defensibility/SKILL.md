---
name: saas-ai-moat-and-defensibility
description: Test AI-moat claims honestly — data moat, workflow moat, distribution moat, cost moat, brand/trust moat, regulatory moat, switching-cost moat — against the "false moat" taxonomy (LLM wrapper, "we use AI," fine-tuned-once, API resale). Output a defensibility scorecard and a Wardley-map placement of AI components. Use whenever a SaaS plan claims AI as competitive differentiation.
---

# SaaS AI Moat & Defensibility Skill

## Overview

"AI moat" is the most over-claimed line in 2025–2026 business plans. Most claims dissolve under three questions: *what proprietary data?, what proprietary workflow?, what's stopping a foundation-model provider from doing this themselves?* This skill installs the discipline to test AI-moat claims, name the false moats, and produce a defensibility scorecard that an investor's technical diligence partner will accept.

## Use When

- A SaaS plan claims AI as competitive differentiation
- Section 06 of an AI-feature-led plan is being built
- An investor's technical diligence is upcoming
- A founder is making a build-vs-buy / fine-tune-vs-RAG decision and needs the moat lens
- The plan asks for a valuation premium that implicitly assumes AI moat

## Do Not Use When

- AI is internal-efficiency only — no customer-facing AI moat to defend
- Plan is at pre-seed with no customers — moat claims are forward-looking, but discipline still applies

## Required Inputs

- AI architecture (model, embedding, RAG vs fine-tune, training data sources, eval discipline)
- Customer data inventory (what's proprietary, what's accruing, what's leaving when customer leaves)
- Distribution channels (who you reach, how, with what scale)
- Pricing position
- Competitor AI claims
- Foundation-model provider trajectory (are they moving into your category?)

## Workflow

1. **List the AI moat claims** — every place in the plan where AI is presented as competitive differentiation.
2. **Run the 7-question moat test** per `references/saas-ai-moats-and-defensibility-checklist.md`:
   - **Data moat** — proprietary training data competitors cannot access?
   - **Workflow moat** — AI deeply embedded in workflow that's hard to recreate?
   - **Distribution moat** — customer reach hard to replicate?
   - **Cost moat** — running AI more cheaply than competitors?
   - **Brand / trust moat** — the trusted AI expert in this vertical?
   - **Regulatory moat** — compliance / certification / data-residency competitors lack?
   - **Switching-cost moat** — AI tied to data, integrations, training that locks customer in?
3. **Apply the false-moat detector** per `references/ai-moats-vs-false-moats.md`:
   - **LLM wrapper** — "we use GPT" with no data, workflow, distribution, or cost edge → not a moat
   - **"We fine-tuned a model"** — one-off fine-tune with no ongoing data accrual → not a moat
   - **API resale** — value-add layer is thin → not a moat
   - **Generic RAG** — RAG over public docs → not a moat
   - **AI partnership claim** — "we partner with OpenAI" → not a moat (everyone has API access)
   - **AI roadmap** — "we'll have AI" → not a moat until shipped + adopted
4. **Wardley-map the AI components** — place each component (foundation model, embedding, vector DB, RAG, eval, observability, fine-tune, data pipeline) on the Wardley evolution axis (Genesis → Custom → Product → Commodity). Components in Commodity or moving to Commodity cannot be your moat. Your moat must be in Custom or Product layers with explicit "stay defensible" logic.
5. **Foundation-model provider risk** — explicitly map what OpenAI / Anthropic / Google / Meta / Amazon doing in your category would mean. If the answer is "they'd kill us," declare it as a risk and a moat-strategy implication.
6. **Score the defensibility** — 0-3 per dimension, total out of 21. Below 8 = weak; 8-14 = real but not unique; 15+ = strong.
7. **State the moat thesis in one paragraph** that an experienced operator would not call marketing language.
8. **Wire to risk** (`saas-ai-risk-and-stress-test`) and valuation (`meta-ai-valuation-adjustments`).

## Quality Bar

- Every AI-moat claim tested through the 7-question rubric
- False-moat detector applied; weak claims explicitly retracted from the plan
- Wardley-map placement done for each AI component
- Foundation-model platform risk explicitly named
- Defensibility score honestly computed; not gamed
- Moat thesis stated in plain language without marketing
- Anti-marketing language: "we have a moat because…" with evidence, not assertion

## Anti-Patterns

- "AI is our moat" without specifying which of the 7 dimensions
- One-time fine-tune as the moat (without ongoing data accrual)
- API access as the moat ("we partner with OpenAI")
- Mentioning fine-tune / RAG / embedding without data-source provenance
- Failing to name foundation-model platform risk
- Wardley-map placing your moat in Commodity layer

## Outputs

- Moat-claim inventory
- Defensibility score (0-21) per moat dimension
- False-moat detection list (claims rejected or downgraded)
- Wardley-map AI-component placement
- Foundation-model platform risk statement
- Moat thesis paragraph (the one-sentence answer to "why are you defensible?")
- Cross-reference to risk register and valuation premium/discount

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Competitor AI claim scan | monthly | Head of Strategy | new entrant with similar moat claim |
| Foundation-model commoditisation watch | monthly | Head of AI / CTO | provider releases competing capability |
| Data accrual evidence | monthly | Head of Product | accrual rate <plan |
| Moat score reassessment | quarterly | CEO + Head of Strategy | -3 points on any dimension |
| Wardley-map refresh | annual | Head of Strategy | structural shift |

## References

- `references/saas-ai-moats-and-defensibility-checklist.md` — full 7-question rubric + false-moat catalogue + Wardley placement guide
- `references/ai-moats-vs-false-moats.md` — in `06-competitive-analysis/references/`
- `skills/06-competitive-analysis/SKILL.md` — generic competitive analysis
- `book-extractions/walling-saas-playbook-extraction.md` — moats chapter
- `skills/14-ai-integration/references/saas-ai-feature-roadmap-in-business-plan.md` — feature roadmap discipline
- `skills/meta-ai-valuation-adjustments/SKILL.md` — valuation logic that consumes the moat score

## Africa / Uganda Application Notes

- **Local-language data moat** is the most under-utilised real moat available to African AI startups (Swahili, Hausa, Yoruba, Amharic, Luganda, Lingala, Wolof, Tigrinya). Lelapa AI, Masakhane, Awarri, EqualyzAI are precedents.
- **Sovereign-AI / data-residency moat** — if you can run AI on in-country compute with in-country data, you have a moat against US/EU competitors who can't legally serve regulated African verticals.
- **Distribution moat in African verticals** — 200 deployed cooperatives, 50 deployed clinics, 30 deployed schools are real moats that an offshore AI competitor cannot replicate quickly.
- **Workflow moat** in African business processes (mobile-money-driven workflows, USSD-channel workflows, WhatsApp-channel workflows) is genuine; foundation-model providers don't understand these.
- **Trust / brand moat** — being the local AI expert with local accountability matters more in Africa than in saturated markets; in regulated sectors, foreign AI is often a procurement disqualifier.
- **Cost moat** — running local Mistral / Llama 3 / Gemma on Liquid / Cassava infra can be cheaper than OpenAI for high-volume routine queries; this is a real defensibility.
