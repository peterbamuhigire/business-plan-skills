---
name: anti-ai-slop
description: Use when producing any human-facing business-plan artefact; applies live specificity, verification, authored-intent, hard-case, and language controls, while `ai-slop-audit` independently grades completed work.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Anti AI Slop

<!-- dual-compat-start -->

## Overview

This is the production-side quality gate every output in this suite passes before it ships. Detection and scoring live in the companion `ai-slop-audit` skill; this skill governs **production** — writing, modelling, and designing so slop never appears in the first place. It sits on top of `writing-quality`, `language-standards`, and `meta-critical-thinking-business-logic`, and it overrides stylistic preferences when they conflict.

## Real-time application (this is a LIVE constraint, not only a final gate)

Apply these rules **continuously, as you write and model** — to every section, paragraph, slide, and projection at the moment it is drafted, not only in one pass at the end. The moment you reach for a banned word, a generic placeholder, an unverified market size or figure, or a template default, stop and correct it in place. The ship-gate checklist at the end is the final confirmation, not the first time these rules are consulted. If you are mid-draft and notice slop accumulating — a TAM with no derivation, a value proposition that would fit any competitor, a hockey-stick line with no stated driver — fix it then; do not defer to a cleanup pass.

## Use When

- Use before delivering any generated business plan, plan section, executive summary, pitch deck, investment case, funding request, GTM/pricing narrative, financial-narrative paragraph, grant proposal, or blog post.
- Use as the final pass after `writing-quality` and the section skill have done their work.
- Use whenever you are about to call an output bankable, investor-ready, or submission-ready.

## Do Not Use When

- Do not use to invent evidence, market sizes, or strategy that the plan does not have — that creates slop, it does not remove it.
- Do not use to strip precise technical terms that are genuinely the right word.
- Do not use as a substitute for the commercial-logic gate (`meta-critical-thinking-business-logic`) — weak thinking is not a wording problem.

## Required Inputs

- The draft output to be shipped (section, deck, narrative, or document)
- The audience mode (bank, DFI, equity investor, grant funder, strategic partner, client)
- The verified facts, figures, and citations the output is allowed to use
- Adjacent sections it must reconcile with

## Workflow

1. Confirm what the reader must decide from this output.
2. Run the seven universal guardrails (U1–U7) over every section.
3. Apply the business-plan domain block below to the output type.
4. Scan for banned vocabulary used as filler.
5. Verify every statistic, market size, citation, and named entity against source before it ships.
6. Run the ship gate. If any box is unticked, the output is not ready.
7. When in doubt, hand the draft to `ai-slop-audit` for a graded verdict.

## Quality Standards

- Every section carries a concrete, named, business-specific element a template could not produce.
- No financial or market claim ships unverified.
- The output states an authored strategy and point of view, not relentless positivity.
- Rhythm and structure vary; the banned-vocabulary list is absent as default register.

## Anti-Patterns

- Padding a section to length instead of cutting hollow paragraphs.
- "Studies show" or "the market is growing rapidly" with no named source.
- A value proposition that would fit any company in the sector.
- Hockey-stick projections with no stated driver or assumption.

## Outputs

- A ship-ready output that passes the gate, or
- A list of unticked gate items with the specific fix each one needs.

---

## What "AI slop" is (so you know what you are preventing)

**AI slop** is low-quality content produced in quantity by generative AI and pushed at people who did not ask for it (Merriam-Webster 2025 Word of the Year, verified). Its three diagnostic properties (Kommers et al., *"Why Slop Matters"*, arXiv 2601.06060, verified):

1. **Superficial competence** — looks fine on the surface, no substance underneath.
2. **Asymmetric effort** — cheap to produce, costly for a human (a credit officer, an investment committee) to read, review, and fix.
3. **Mass producibility** — generated at volume.

The human tell named in every domain studied: **absence of intent** — the sense that no one *meant* anything by it. A business plan with this tell reads as if no founder stood behind it. Your job is to re-internalise effort (specificity, verification, authored choices) before the artefact reaches a lender or investor.

## The seven universal guardrails (apply to EVERY output)

| # | Marker to prevent | Avoidance rule you MUST follow |
|---|---|---|
| **U1** | Genericness / averaging | Every section carries ≥1 concrete, named, business-specific element (a real customer, a named competitor, a UGX figure with a source, a dated milestone, an authored decision) a generic template could not produce. Forbid boilerplate copy. |
| **U2** | Superficial competence | Enforce a substance floor: include a claim, number, or decision the section could not exist without. A "market overview" that asserts nothing measurable is filler — cut or replace it. |
| **U3** | Confident wrongness / hallucination | Verify every statistic, market size, citation, quote, and named entity before emit. Cite at the point of claim. Flag uncertainty rather than inventing a TAM. **Financial and market claims especially must pass verify-before-emit — never invent a market size, growth rate, or benchmark.** |
| **U4** | Volume over substance | Prefer one substantive paragraph over three hollow ones. Do not pad to fill a section heading. |
| **U5** | Absence of authored voice / intent | State a strategy, a rationale, a named trade-off the founder made. Ban relentless positivity and sycophancy. A plan with no downside discussion reads as slop. |
| **U6** | Skipping the hard parts | Cover the risks, the do-nothing case, the competitor response, the downside scenario — not just the happy path. |
| **U7** | Mechanical uniformity | Vary sentence length and structure. Break the template. No rule-of-three reflex, no "it's not X, it's Y" formula, no em-dash flood. |

## Banned / high-risk vocabulary (the lexical tells)

These words and constructions are statistically over-produced by LLMs (FSU/COLING-2025; PubMed "delve" +400%). **Do not use them as default register.** A word here is allowed only when it is the genuinely precise term, never as filler. This list merges the canonical anti-slop list with the suite's existing `writing-quality` anti-AI checklist.

- **Words:** delve, tapestry, realm, landscape (as metaphor), navigate (as metaphor), leverage, foster, harness, synergy, embark, robust, vibrant, holistic, seamless, intricate, commendable, meticulous, pivotal, underscore, testament, resonate, elevate, paramount, unwavering, multifaceted, game-changing, innovative solution, unlock, dive into.
- **Phrases:** "in today's fast-paced world", "in today's competitive landscape", "in the ever-evolving landscape of", "it is important to note that", "it should be noted that", "it's worth mentioning", "let's dive in", "here's the kicker", "at the end of the day", "in conclusion", "studies show" (without a named study), "the market is growing rapidly" (without a sourced rate).
- **Constructions:** the "it's not just X, it's Y" antithesis; reflexive rule-of-three lists; em-dash used to manufacture drama; relentless triplet adjectives ("robust, scalable, and reliable"); any paragraph that announces what the next paragraph will say instead of saying it.
- **French equivalents** (for Francophone output): "plongeons dans", "il est important de noter que", "force est de constater", "dans un monde en constante évolution", "par ailleurs/de plus/en outre" as filler connectors, "au cœur de", "pierre angulaire".

## Drop-in guardrail block (inherit in dependent skills)

```text
ANTI-SLOP GUARDRAIL (inherit in every output):
1. SPECIFICITY FLOOR — every section carries ≥1 concrete, named, business-specific
   element. No boilerplate, no placeholder copy.
2. VERIFY-BEFORE-EMIT — no statistic, market size, citation, quote, or named entity
   ships unverified; cite at point of claim; flag uncertainty. Never invent a TAM.
3. AUTHORED VOICE — state a strategy / rationale / trade-off; no relentless
   positivity, no sycophancy.
4. COVER THE HARD PARTS — risks, do-nothing case, competitor response, downside.
5. BREAK THE TEMPLATE — vary rhythm and structure; forbid the banned-vocabulary
   list above.
```

## Business-plan domain block (apply to plans, decks, narratives)

This is the primary domain for this suite. Apply every item before shipping a plan, a section, or a deck.

- **Market sizing:** every TAM/SAM/SOM figure has a named source and a stated method (top-down or bottom-up). No round-number TAM with no derivation. No "the market is growing rapidly" without a sourced growth rate. Generic TAM/SAM filler that would fit any sector is slop — cut it.
- **Evidence:** no "studies show", "research indicates", or "industry experts agree" without a named study, report, or institution and a year. Use the suite's source-referencing format (Author, Year).
- **Strategy:** the plan states an authored strategy — a named choice of segment, position, and basis of competition — not a generic ambition to "become the leading provider". A value proposition that would describe any competitor in the sector has not been authored.
- **Differentiation:** the moat or differentiator is specific and testable (a named asset, contract, cost position, or capability), not an adjective stack.
- **Projections:** every hockey-stick line has a stated driver and assumption (customers × price × conversion, with a source for each). Projections with no basis fail U3 and U6. Reconcile the funding ask with the implementation plan.
- **Risk:** the risks section names decision-relevant risks and the do-nothing case, not a generic list of "market, operational, and financial risks".
- **Pitch deck:** one assertion per slide backed by one piece of evidence; no slide that could appear in any pitch unchanged.

## Adjacent domain blocks (load the relevant one when the output type applies)

- **Written content (blog, article, marketing copy):** no focal-word clusters; vary sentence length (mix 3–10 with 25–40 words); ≤1 em-dash per paragraph; no "in conclusion"; specific examples over generic claims; a stated point of view.
- **Proposal / EoI / client proposal:** no inflated superlatives or hollow analogies; every claim is verifiable; the logic chain (evidence → warrant → implication) is visible; route through `proposal-architect`.
- **Code / financial-model formulas:** verify every dependency exists; no placeholder stubs or TODOs in shipped work; no hardcoded secrets; real assumptions, not `assert true` cells.

## Ship gate (run before delivering ANY output)

- [ ] Every section has ≥1 concrete, named, business-specific element (U1/U2).
- [ ] Every stat, market size, citation, quote, and named entity verified against source (U3).
- [ ] No banned vocabulary used as filler; scanned the output for the list above.
- [ ] The output states an authored strategy / point of view; no sycophancy (U5).
- [ ] Risks, do-nothing case, competitor response, and downside addressed (U6).
- [ ] Sentence length and structure varied; no rule-of-three reflex, no antithesis formula, no em-dash flood (U7).
- [ ] The business-plan domain block (or the relevant adjacent block) applied.
- [ ] When in doubt, run the `ai-slop-audit` skill on the draft.

If any box is unticked, the output is not ready to ship.

## References

- `ai-slop-audit` supplies the independent checkpoint and release grade.
- `writing-quality` governs business-plan prose mechanics beneath this gate.
- `meta-critical-thinking-business-logic` tests claim, evidence, warrant, countercase, and implication.
- `../../../book-extractions/human-english-craft-synthesis-2026.md` governs reader-fit register, grammar, collocation, rhythm, and proof alongside this gate.

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when missing |
| --- | --- | ---: | --- |
| Human-facing draft and intended decision | Parent workflow or requester | Yes | Stop the release gate until the output and audience are named. |
| Verifiable claims, citations, dependencies, and figures | Supplied evidence or authoritative sources | Conditional | Remove or qualify unsupported specificity. |

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Guarded human-facing output | Requester and decision-maker | Specificity, verification, intent, hard-case, and language checks pass without fabricated evidence. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Anti-slop gate record | Completed checklist with verified, qualified, and blocked items | No fabricated statistic, citation, benchmark, market size, dependency, or professional claim remains. |
| Authored-content trace | Named decisions, countercases, examples, and risk notes | Each section earns its place through business-specific evidence or judgement. |

## Capability Contract

Apply within the parent task's authority. Read and search supplied evidence; execute checks or use network verification only when available and authorised. Do not publish, spend, delete, certify, or alter source records merely to satisfy this gate. Current finance, legal, tax, regulatory, and market claims require the governing source and review boundary.

## Degraded Mode

Fallback: if a source, network, renderer, model, font, dependency registry, or execution capability is unavailable, remove unsupported specificity or mark the check `not assessed`. Return the narrowest useful qualified artefact and the evidence needed to finish; never convert the missing check into a pass.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A claim, citation, number, named entity, or dependency cannot be verified | Remove it, qualify it, or stop for evidence | Confident wrongness and fabricated authority. |
| A paragraph contains no decision, example, evidence, or necessary instruction | Cut it or add real substance | Superficial competence and review burden. |
| A hard case, counterargument, or failure path could change the recommendation | Cover it before release | Happy-path strategy that fails under scrutiny. |
| Content is specific, verified, concise, and purposeful | Preserve it | Mechanical rewriting that erases authored voice. |

## Anti-Patterns

- Adding a precise number to make a section look researched. Correction: verify and cite it or remove it.
- Keeping a polished paragraph that makes no decision. Correction: add business-specific evidence or cut the paragraph.
- Applying the gate only after the full draft. Correction: check each section while it is produced and audit each major iteration.
- Replacing an intentional phrase merely because it is unusual. Correction: preserve purposeful voice unless it harms clarity or accuracy.
- Ignoring downside, rejection, error, or empty states. Correction: add the hard case that could change the decision.
- Claiming an unavailable verification passed. Correction: mark it `not assessed` and narrow the output.

## Worked Example

Draft text says "the market is rapidly growing" without a source or decision implication. Remove the claim until dated evidence exists, or state the verified market observation and explain how it changes capacity, pricing, or entry timing. A decorative adjective is not a substitute for evidence.

## Workflow

1. Name the reader's decision and inspect the evidence supporting each load-bearing claim.
2. Apply the seven controls while drafting; stop when a fact, citation, dependency, or professional claim cannot be verified.
3. Cover countercases, risks, and failure paths, then run the output-specific gate.
4. Recover a blocked draft by removing unsupported claims or obtaining evidence, and send the completed artefact to `ai-slop-audit`.

<!-- dual-compat-end -->

- `../../meta-utility/ai-slop-audit/SKILL.md` — the detection, evaluation, and audit companion (grade any artefact for slop).
- `../../language/writing-quality/SKILL.md` — the suite's language-quality layer; apply before this gate.
- `../../language/language-standards/SKILL.md` — multilingual tone and grammar standard; apply on top.
- `../../meta-strategy/meta-critical-thinking-business-logic/SKILL.md` — commercial-logic gate; weak thinking is not fixed by wording.
