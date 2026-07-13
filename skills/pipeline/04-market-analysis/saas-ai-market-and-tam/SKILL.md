---
name: saas-ai-market-and-tam
description: Use when producing or reviewing the saas ai market and tam component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Market definition, customer count or spend evidence, geography, time period, and source register for saas ai market and tam | Verified research, official statistics, client sales data, and named assumptions | Yes | If absent, a load-bearing market source or denominator is unavailable, provide the bounded known market and label the unmeasured remainder rather than extrapolating it. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Attributable SaaS AI TAM/SAM/SOM model with sensitivity cases | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai market and tam exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai market and tam release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Customer-count × attributable-spend workbook and adoption constraint log | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai market and tam decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai market and tam review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai market and tam, the controlling focus is attributable AI spend, serviceable users, adoption constraints, price basis, and bottom-up TAM sensitivity. This skill may search and analyse market evidence in read-only mode; it may not invent a TAM, extrapolate beyond a source's population, or present an undated estimate as current. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai market and tam, loss of evidence about attributable AI spend, serviceable users, adoption constraints, price basis, and bottom-up TAM sensitivity activates degraded mode. If the controlling saas ai market and tam evidence is unavailable, the same boundary applies. When a load-bearing market source or denominator is unavailable, provide the bounded known market and label the unmeasured remainder rather than extrapolating it. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai market and tam, top-down market revenue conflicts with bottom-up reachable-customer economics| show both methods, diagnose the boundary difference, and use the more decision-relevant conservative case | Inflated market sizing destroys the credibility of strategy and valuation |
| For saas ai market and tam, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai market and tam decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai market and tam, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete attributable saas ai tam/sam/som model with sensitivity cases, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai market and tam decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect market definition, customer count or spend evidence, geography, time period, and source register and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce attributable saas ai tam/sam/som model with sensitivity cases with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Attributable SaaS AI TAM/SAM/SOM model with sensitivity cases must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Customer-count × attributable-spend workbook and adoption constraint log must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas ai market and tam, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai market and tam, treating an unavailable market definition, customer count or spend evidence, geography, time period, and source register as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing attributable saas ai tam/sam/som model with sensitivity cases that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A vendor report prices a full software suite at USD 100 per user, but the proposed AI feature accounts for only part of value. Attribute only the evidenced AI spend share and show adoption and price sensitivity instead of calling the full suite revenue TAM.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai market and tam; no local deep-dive reference is declared.
- For saas ai market and tam claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
