---
name: saas-ai-market-and-tam
description: Build AI-aware TAM / SAM / SOM for a SaaS plan — addressable-by-AI subset of the SaaS TAM, AI-attribution discipline (avoid double-counting generic SaaS TAM as AI TAM), sovereign-AI / local-language / regulated-vertical segmentation, and AI-skeptic-friendly market sizing. Use whenever Section 04 of an AI-feature-led plan is being built or reviewed.
---

# SaaS AI Market & TAM Skill

## Overview

AI plans routinely inflate TAM by claiming all SaaS spend in the target vertical as "AI-addressable." Sophisticated investors discount these claims aggressively. This skill installs the AI-attribution discipline: the portion of SaaS TAM that is genuinely AI-attributable, segmented by buyer AI-readiness, vertical AI-fit, and regional realities.

The output is a TAM / SAM / SOM stack with explicit AI-attribution percentages, segmented by AI-readiness tier, with bottom-up and top-down triangulation, and Africa-context sizing where relevant.

## Use When

- Section 04 of an AI-feature-led SaaS plan is being built
- A plan's claimed TAM is suspiciously large because all vertical SaaS spend was counted as AI
- Investors have asked for AI-attributable revenue, not just SaaS revenue
- TAM must defend a stage-appropriate ARR aspiration (Series A needs $10M+ SOM minimum for typical AI SaaS)
- Plan targets sovereign-AI, local-language, or regulated-vertical AI markets

## Do Not Use When

- AI is internal-efficiency only — use generic `04-market-analysis`
- Plan is grant-funded (the TAM lens is different; use `11b-grant-proposal` and theory-of-change)

## Required Inputs

- Vertical, geography, buyer persona, AI use case(s)
- Total SaaS TAM for the vertical/geography
- Evidence of AI-readiness (buyer interviews, surveys, analyst reports)
- Competitor AI-attribution evidence (their ARR breakdown, pricing of AI tiers)

## Workflow

1. **Compute the standard TAM/SAM/SOM** using bottom-up + top-down + benchmark triangulation per `04-market-analysis`.
2. **Apply AI-attribution percentages** per `references/ai-tam-attribution.md`:
   - **High-AI-attribution segments** (60-100%): AI-native workflows, where the AI capability IS the product
   - **Mid-AI-attribution segments** (20-60%): AI-augmented workflows where AI is a material feature
   - **Low-AI-attribution segments** (5-20%): AI is incremental value but customer would pay close to the same without it
3. **Segment by AI-readiness tier** — early adopter, fast-follower, mainstream, laggard. The SOM for the first 3 years is almost entirely in the early-adopter + fast-follower segments.
4. **Apply geography overlays** — for Africa-targeting plans, add the sovereign-AI / local-language / regulated-vertical lenses (see `africa-ai-context-extension.md`). These can be both expansive (specific local moats) and constraining (smaller addressable pool).
5. **Triangulate against competitor signals** — if a competitor's AI revenue is X% of total ARR, that's a real-world AI-attribution benchmark.
6. **Stress-test the TAM** — what if AI-readiness moves slower than projected? what if foundation-model commoditises the category? what if regulation slows enterprise AI adoption?
7. **Produce the AI-attribution table** for the plan: TAM × AI-attribution % = AI-TAM; SAM × AI-attribution % = AI-SAM; etc. Be honest about which segments are 100% AI-attributable and which are <50%.
8. **Wire into living plan** — TAM refresh annual; AI-attribution review quarterly; major-entrant trigger immediate.

## AI-Attribution Rubric

| Vertical / use case | AI-attribution % | Reasoning |
|---|---|---|
| AI coding assistants (Copilot-class) | 80-100% | Product IS AI |
| AI customer-service automation | 50-80% | AI replaces or augments human agent |
| AI-augmented CRM (e.g. lead scoring) | 15-30% | Buyer wants CRM; AI is bonus |
| AI in healthcare imaging | 70-100% | AI is the differentiator |
| AI in agricultural advisory (vertical SaaS) | 30-60% | Buyer wants advisory; AI deepens it |
| AI in legal contract analysis | 60-80% | AI is the differentiator |
| AI in payroll / HR (e.g. resume screening) | 10-25% | Buyer wants payroll; AI is bonus |
| AI in vertical workflow (custom RAG over operational data) | 40-70% | AI is meaningful upgrade |
| Pure LLM API resale | 100% AI-revenue / 0% defensible | High attribution, weak business |

## Quality Bar

- Standard TAM/SAM/SOM done first
- AI-attribution % stated per segment with reasoning
- AI-readiness tier segmentation applied
- Geography overlays applied
- Competitor AI-revenue benchmarks cited where available
- Stress scenarios applied
- AI-TAM, AI-SAM, AI-SOM stated explicitly alongside (not instead of) standard figures
- Discipline visible: an investor would say "this team is honest about AI-attribution"

## Anti-Patterns

- "AI market is $X trillion by 2030" — meaningless headline; not addressable
- All SaaS TAM counted as AI TAM
- AI-readiness assumed uniform across segments
- Single-source TAM (analyst report only)
- No competitor AI-revenue benchmark
- AI-attribution stated as 100% across all segments

## Outputs

- AI-aware TAM / SAM / SOM stack (table form)
- AI-attribution % per segment with reasoning
- AI-readiness tier segmentation
- Stress scenarios
- Geographic overlay (especially Africa-context)
- Reconciliation to standard TAM

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| AI-TAM refresh | annual | Head of Strategy | structural change |
| AI-attribution % per segment | quarterly | Head of Strategy + Head of Product | -10pp from plan |
| Competitor AI-revenue benchmarks | quarterly | Head of Strategy | major shift |
| AI-readiness tier shift | annual | Head of Strategy | accelerated adoption |
| Sovereign-AI / regulated-vertical addressable change | annual + on regulatory event | Head of Legal + Head of Strategy | new regulation |

## References

- `references/ai-tam-attribution.md` — full discipline + worked example (in `04-market-analysis/references/`)
- `skills/04-market-analysis/SKILL.md` — generic TAM/SAM/SOM
- `country-context/africa-regional/africa-ict-saas-market-context.md` — Africa-AI Section 14
- `book-extractions/cotton-run-a-saas-business-extraction.md` — TAM discipline

## Africa / Uganda Application Notes

- African AI TAM should be sized in local + USD; donor-funded segments are USD-anchored.
- Sovereign-AI / regulated-vertical TAM is a real and growing addressable pool — KE national AI strategy, NG NITDA AI roadmap, ZA AI framework, RW AI policy all create public-sector AI demand.
- Local-language AI TAM is a genuine niche moat — Swahili, Hausa, Yoruba, Amharic, Igbo, Zulu, Xhosa, Luganda. Companies that legitimately curate local-language data have defensible AI-TAM in those niches.
- Early-adopter AI-readiness in African enterprise is concentrated in fintech, telecom, large banks, multinational subsidiaries. Public-sector AI procurement is fast-evolving (often donor-funded).
- AI-readiness in African SMB is low; the SMB AI TAM ramps slowly. Plans should not over-claim near-term SMB AI demand.
