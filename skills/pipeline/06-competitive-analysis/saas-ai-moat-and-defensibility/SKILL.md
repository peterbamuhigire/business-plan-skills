---
name: saas-ai-moat-and-defensibility
description: Use when producing or reviewing the saas ai moat and defensibility component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Named competitors and substitutes, customer decision criteria, observed offers, and defensibility evidence for saas ai moat and defensibility | Customer research, competitor primary sources, product data, and technical records | Yes | If absent, competitor or moat evidence is unavailable, state the untested claim and design a verification step rather than awarding a score. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Scored AI moat and defensibility thesis with downgraded or rejected claims | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai moat and defensibility exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai moat and defensibility release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Rubric score, proprietary-asset proof, commoditisation test, and claim downgrade log | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai moat and defensibility decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai moat and defensibility review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai moat and defensibility, the controlling focus is proprietary data, workflow embedding, distribution, learning loops, switching costs, and replicability. This skill may inspect public and supplied competitive evidence in read-only mode; it may not misrepresent a competitor, scrape outside authorised terms, or assert proprietary advantage without proof. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai moat and defensibility, loss of evidence about proprietary data, workflow embedding, distribution, learning loops, switching costs, and replicability activates degraded mode. If the controlling saas ai moat and defensibility evidence is unavailable, the same boundary applies. When competitor or moat evidence is unavailable, state the untested claim and design a verification step rather than awarding a score. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai moat and defensibility, the claimed advantage is readily copied or depends only on a third-party model or framework| downgrade the claim, test what survives commoditisation, and reposition around evidenced assets or distribution | Promotional differentiation collapses under customer or investor diligence |
| For saas ai moat and defensibility, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai moat and defensibility decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai moat and defensibility, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete scored ai moat and defensibility thesis with downgraded or rejected claims, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai moat and defensibility decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect named competitors and substitutes, customer decision criteria, observed offers, and defensibility evidence and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce scored ai moat and defensibility thesis with downgraded or rejected claims with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Scored AI moat and defensibility thesis with downgraded or rejected claims must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Rubric score, proprietary-asset proof, commoditisation test, and claim downgrade log must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas ai moat and defensibility, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai moat and defensibility, treating an unavailable named competitors and substitutes, customer decision criteria, observed offers, and defensibility evidence as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing scored ai moat and defensibility thesis with downgraded or rejected claims that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A SaaS feature uses a fine-tuned public model but lacks exclusive data, embedded workflow, distribution, or learning-loop evidence. Score each moat claim separately and withhold a defensibility premium until durable assets exist.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai moat and defensibility; no local deep-dive reference is declared.
- For saas ai moat and defensibility claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
