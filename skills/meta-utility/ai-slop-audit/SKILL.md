---
name: ai-slop-audit
description: Analyse, evaluate, audit, critique, score, or "de-slop" any business plan, plan section, pitch deck, investment case, financial model or narrative, GTM/pricing narrative, proposal/EoI, blog post, document, or codebase for AI slop. AUTO-RUNS whenever the user asks to analyse, review, evaluate, audit, critique, or score such an artefact for AI slop, or asks "does this look AI-generated?". Produces a graded slop report — per-marker findings with severity, evidence, and a concrete fix, plus a 0–100 genericness score. Pairs with anti-ai-slop, which prevents slop during production.
---

# AI Slop Audit

## Overview

This is the detector. Given any artefact, it decides how strongly it reads as AI slop, names exactly why with evidence, scores it, and says how to fix each finding. Production-side prevention is the companion `anti-ai-slop` skill. It runs as the final gate before any plan, deck, or narrative leaves the suite, and on demand whenever a user asks for a slop review.

## Cadence — run after each major iteration

This is the default mode: run this audit after **each major iteration of work on the plan** — each drafted plan section, each completed deck, each financial-narrative module, each significant revision, each milestone — before moving to the next. Log the verdict each time. If the verdict is **F (Blocked)**, do not progress to the next section or iteration until the blocking findings are fixed. Treat it like a test suite that runs at every checkpoint, not a one-time final review. This is in addition to running on request and as the final pre-submission gate; the companion `anti-ai-slop` skill runs continuously *during* drafting, and this audit runs *at each checkpoint* to catch what slipped through.

## Use When

- Use when the user asks to analyse, review, evaluate, audit, critique, score, or de-slop a business plan, plan section, pitch deck, investment case, financial model or narrative, GTM/pricing narrative, proposal/EoI, blog post, document, or codebase.
- Use when the user asks "is this AI slop / does this look AI-generated / why does this feel off?".
- Use as the final gate before publishing or submitting any suite output.

## Do Not Use When

- Do not use to invent a flaw to pad the report — "this artefact is clean" is a wanted verdict.
- Do not use as a substitute for the commercial-logic gate; a slop-clean plan can still be a bad plan.
- Do not use to rewrite — this skill grades and prescribes; `anti-ai-slop` and the section skills do the fixing.

## Required Inputs

- The artefact to audit (text, plan, deck, model, document, or code)
- The artefact type and intended audience
- Any source list the artefact's claims are supposed to rest on

## Workflow

1. Identify the artefact type(s) and load the right checklist (Step 1 below).
2. Run the automated gates — any hit on a blocking (✗) marker fails the artefact (Step 2).
3. Compute the 0–100 genericness score and name its drivers (Step 3).
4. Run the human-judgement review, including the business-plan domain checks (Step 4).
5. Grade A/B/C/F and write the report in the fixed output format.
6. Hand blocking and high-severity findings to `anti-ai-slop` and the relevant section skill for fixing.

## Quality Bar

- Every finding cites concrete evidence from the artefact (a quote, a line, a figure, a slide).
- The verdict, the score, and the score drivers are all stated.
- Blocking findings (hallucinated stat, fabricated citation, missing assumption behind a projection) are separated from minor ones.
- "What's good" is listed so the fix does not strip substance.

## Anti-Patterns

- A finding with no evidence from the artefact.
- Inventing flaws to make the report look thorough.
- Presenting an inference as a measured fact.
- Grading on tone alone while ignoring fabricated market data.

## Outputs

- A graded slop audit report (A/B/C/F) with a genericness score, per-marker findings, evidence, fixes, and a recommended next step.

---

## What slop is (the yardstick)

Low-quality content produced in quantity by AI and pushed at people who did not ask for it (Merriam-Webster 2025 WOTY, verified). Three diagnostic properties (Kommers et al., arXiv 2601.06060): **superficial competence, asymmetric effort, mass producibility**. The human tell: **absence of intent**. You are measuring how strongly an artefact exhibits these.

## Audit method — layered, cheapest first

### Step 1 — Identify artefact type and load the right checklist

Map the artefact to one or more domains: written content (EN/FR), business plan / pitch deck / financial narrative, proposal/EoI, code. A full plan usually spans several (prose + market data + financial model) — audit each layer.

### Step 2 — Automated gates (🤖, machine-checkable) — any hit is hard evidence

Run every applicable check; a hit on a **blocking** marker (✗) fails the artefact outright.

**Written content / plan prose**
- 🤖 Focal-word density — delve/tapestry/realm/navigate/underscore/pivotal/intricate/leverage/robust/seamless etc. >2 per 500 words.
- 🤖 Em-dash density >1 per paragraph; reflexive rule-of-three; "it's not X, it's Y" repetition; uniform 15–25-word sentences (low burstiness).
- 🤖 Transition clichés ("in today's fast-paced world", "in today's competitive landscape", "let's dive in", "in conclusion").
- 🤖 Mechanical formatting: Title-Case headers, excess bold, decorative emoji, leftover tool markup ("oaicite", "contentReference").
- ✗ 🤖 Broken/fake citations: dead URLs, invalid DOI/ISBN, fabricated stats, utm_source params copied in.
- French: "plongeons dans", "il est important de noter que", "force est de constater", filler connectors.

**Business plan / pitch deck / financial narrative (the suite's primary domain)**
- ✗ 🤖 Fabricated market stats: any TAM/SAM/SOM figure, growth rate, or benchmark with no named source — resolve each against its cited source.
- ✗ 🤖 "Studies show" / "research indicates" / "industry experts agree" with no named study, report, or institution and year.
- 🤖 Generic TAM/SAM filler that would fit any sector unchanged; round-number TAM with no stated method (top-down/bottom-up).
- 🤖 Undifferentiated value proposition — a moat or positioning statement that would describe any competitor in the sector.
- 🤖 Hockey-stick projections with no stated driver or assumption behind the curve (no customers × price × conversion, no source).
- 🤖 No authored strategy — generic ambition ("become the leading provider") in place of a named choice of segment, position, and basis of competition.
- 🤖 Funding ask that does not reconcile with the use of funds or the implementation timeline.
- 🤖 Deck slides that could appear in any pitch unchanged; more than one assertion per slide with no supporting evidence.

**Code / financial-model formulas**
- ✗ 🤖 Hallucinated/uninstallable imports & packages (slopsquatting) — resolve every dependency against its registry.
- ✗ 🤖 Hardcoded secrets; SQL built by string interpolation; insecure defaults.
- 🤖 Placeholder stubs/TODO/`NotImplementedError`/`...` in shipped work; dead code; duplication; tautological tests (`assert true`); model cells with no assumption behind them.

### Step 3 — Structural score (🤖) → 0–100 "genericness"

Combine burstiness, focal-word density, duplication, and template-similarity into a single genericness score. Higher = more slop-like. Report the score and its drivers.

### Step 4 — Human-judgement review (👁) — the checklist no tool replaces

- 👁 **Substance:** what does this assert or decide that required real work (a primary customer interview, a sourced market figure, a costed assumption)? If nothing — slop.
- 👁 **Intent / authored voice:** is there a strategy and a point of view, or is it relentlessly positive and viewpoint-free?
- 👁 **Specificity:** real named customers, competitors, institutions, and UGX figures, or generic placeholders?
- 👁 **Hard parts:** are risks, the do-nothing case, competitor response, and the downside scenario handled?
- 👁 **Domain-specific (per artefact):**
  - *Business plan / investment case:* fabricated market stats, generic TAM/SAM filler, undifferentiated value proposition, hockey-stick projections with no basis, no authored strategy, "studies show" without a named study, funding ask that does not reconcile with the plan.
  - *Pitch deck:* slides that fit any company, more than one claim per slide with no evidence, no clear ask.
  - *GTM / pricing narrative:* cost-plus or competitor-match pricing with no stated value logic; channel list with no economics behind it.
  - *Proposal / EoI:* inflated superlatives, hollow analogies, unverifiable claims, no visible logic (evidence → warrant → implication).
  - *Blog / social:* engagement-bait, no lived experience, clichés.

## Scoring & verdict

Aggregate into a grade:

| Grade | Meaning | Trigger |
|---|---|---|
| **A — Clean** | No blocking hits; genericness low; substance & intent present | ship |
| **B — Minor slop** | A few automated hits, no blockers; some genericness | fix listed items |
| **C — Slopy** | Multiple automated hits or weak substance/intent | rework before ship |
| **F — Blocked** | Any ✗ blocker (fabricated stat/citation, hallucinated package, secret) OR no substance at all | do not ship |

## Output format (the audit report)

```
# AI Slop Audit — <artefact name> — <date>
Verdict: <A/B/C/F>   Genericness score: <0–100>
Artefact type(s): <...>

## Blocking findings (✗) — must fix
- [marker] <what was found> · evidence: <quote/line/figure/slide ref> · fix: <concrete action>

## Slop findings (by severity)
- [marker] <finding> · evidence: <...> · fix: <...>

## What's good (so it isn't stripped in the fix)
- <substantive, specific, authored elements worth keeping>

## Recommended next step
- <rework / targeted fixes / ship>
```

## Discipline (anti-hallucination — applies to the audit itself)

- Every finding cites concrete evidence from the artefact (a quote, a line number, a figure, a slide reference, a URL). No finding without evidence.
- Do not invent a flaw to pad the report. "This artefact is clean" is a valid, wanted verdict.
- Mark inferences "(inference)"; never present a guess as a measured fact.

## References

- `../../meta-utility/anti-ai-slop/SKILL.md` — prevention companion (write/model/design so slop never appears).
- `../../meta-strategy/meta-critical-thinking-business-logic/SKILL.md` — commercial-logic gate; a slop-clean plan can still be a bad plan.
- `../../language/writing-quality/SKILL.md` — the suite's language-quality layer; apply domain tone on top.
