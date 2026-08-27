---
name: writing-quality
description: Use when drafting or editing plans, proposals, pitches, reports, summaries, or founder narratives for clarity, argument, persuasion, originality, and human voice; use `language-standards` for multilingual correctness and `anti-ai-slop` for the mandatory release gate.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Writing Quality

## Overview

Use this skill as the language-quality layer for the suite. It sharpens clarity, structure, persuasiveness, and narrative force across business-plan and proposal writing without changing the underlying commercial logic.

## Use When

- Use when drafting, revising, or polishing business-plan prose.
- Use when the content is directionally correct but the writing is weak, bloated, or unconvincing.
- Use alongside section skills when language quality materially affects credibility.

## Do Not Use When

- Do not use to invent missing evidence or strategy.
- Do not improve style in a way that softens necessary precision.
- Do not replace section-specific logic with generic polished wording.

## Required Inputs

- Draft text to improve
- Audience and document context
- Any non-negotiable facts, figures, or terminology
- Adjacent sections where tone or phrasing must stay consistent

## Workflow

1. Identify what the reader must understand and decide.
2. Tighten the prose around that purpose using the rules below.
3. Remove ambiguity, filler, and passive evasion.
4. Improve flow, emphasis, and narrative sequence without distorting meaning.
5. Reconcile language choices with the intended audience and document type.
6. For premium, investor-facing, sales-oriented, SEO, or client-facing deliverables, apply `premium-commercial-writing` before final polish.
7. Flag where the draft is weak because the underlying thinking is weak.

## Quality Bar

- The writing is clearer, tighter, and more persuasive.
- Meaning stays intact while readability improves.
- The prose supports decision-making rather than sounding merely polished.
- Tone matches the document and audience.

## Anti-Patterns

- Replacing precision with vague eloquence.
- Polishing unsupported claims instead of fixing them.
- Letting sentence craft overpower logic and structure.
- Applying one tone uniformly across all audiences.

## Outputs

- Improved draft language with stronger clarity and persuasion
- Notes on structural or evidence issues the prose cannot solve
- A sharper language baseline for adjacent section work

## Book-derived reader-craft overlay

Load [`human-english-craft-synthesis-2026.md`](../../../book-extractions/human-english-craft-synthesis-2026.md) before drafting or polishing. Apply the five passes—reader and purpose, genre and spine, meaning and evidence, sentence/paragraph craft, and proof/read-aloud. Use grammar and vocabulary references diagnostically; never replace a sound argument with ornament, and never simulate humanity with errors or slang.



Apply these principles to all business plan text. The goal: the reader forgets they are reading a document and simply finds themselves persuaded.

---

## The Four Quality Dimensions

| Dimension | Source | Core principle |
|---|---|---|
| **Plain and clear** | Hood  *Words at Work* | Write for the reader, not to impress. One idea per sentence. |
| **Logically structured** | Shiach  *How to Write Essays* | Every argument: key sentence  evidence  conclusion. |
| **Professionally styled** | Geffner  *Business English* | Active voice. Natural language. Concrete nouns. No stilted phrases. |
| **Narratively compelling** | Rubie & Provost  *How to Tell a Story* | Give the reader a person, a problem, and a resolution. |

---

## Plain English Rules (Hood)

1. **Reversed triangle**  state the conclusion first, then the supporting detail. Never build up to the answer.
2. **One idea per sentence**  if a sentence contains two ideas, split it.
3. **Two-line rule**  if a sentence is longer than two printed lines, break it.
4. **Active voice**  "The business generates UGX 24M/month" not "Revenue of UGX 24M/month is generated."
5. **You and we**  address the reader directly. "You will see from the projections..." not "It can be observed..."
6. **Jargon discipline**  use technical terms only when the reader knows them. Define on first use.
7. **One idea per paragraph**  open with the main point, support it, close or link it. Usually keep it to five sentences or fewer, but let the thought—not a template—set the length.
8. **Positive framing**  "Repayment begins in month 4" not "Repayment will not start before month 4."
9. **Concrete over abstract**  "The mill processes 800kg per hour" not "The mill has significant capacity."
10. **Cut the preamble**  delete the first sentence of any paragraph that merely announces what follows.

**Avoid these phrases (replace with plain alternatives):**

| Stilted phrase | Plain replacement |
|---|---|
| Please find enclosed herewith | I enclose / Please find enclosed |
| Pursuant to our earlier discussion | Following our discussion |
| In the event that | If |
| It is recommended that | We recommend |
| At this point in time | Now |
| In order to | To |
| Due to the fact that | Because |
| Utilise | Use |
| Commence | Start / Begin |
| Prior to | Before |

---

## Argument Structure (Shiach)

Every paragraph in a business plan should follow this formula:

```text
1. Key sentence     state the point directly (topic sentence)
2. Development      two to four sentences of evidence, example, or data as the thought requires
3. Link             one sentence drawing the conclusion or bridging to the next point
```

**Introduction structure** (executive summary, section openers):
1. Hook  a specific, surprising, or urgent opening statement
2. Context  one or two sentences orienting the reader
3. Thesis  the main claim or argument in one sentence
4. Signpost  briefly indicate what follows

**Conclusion structure** (executive summary close, funding request close):
1. Signal  "This plan demonstrates that..." / "The evidence shows..."
2. Summary  two or three sentences restating the strongest points
3. Rounding-off sentence  one final sentence the reader will not forget

**Transitions by function:** choose the connector that expresses the actual relationship. Do not add one merely to make the prose look organised.

| Purpose | Linking devices |
|---|---|
| Adding a point | Furthermore, In addition, Moreover, Equally |
| Contrasting | However, Nevertheless, On the other hand, Yet |
| Cause/result | Therefore, Consequently, As a result, Thus |
| Illustrating | For example, For instance, To illustrate, Specifically |
| Concluding | In conclusion, Overall, To summarise, Ultimately |
| Conceding | Although, While, Despite this, Even though |

---

## Business Writing Style (Geffner)

**The Four Cs  every document must be:**
1. **Complete**  all questions the reader will ask are answered
2. **Accurate**  every figure, date, and claim is verifiable
3. **Clear**  no ambiguity; the meaning cannot be misread
4. **Concise**  nothing that does not earn its place

**Document tone rules:**
- Match formality to the reader: bank credit officer (formal), business partner (semi-formal), WhatsApp update (informal)
- Write in the positive: state what is, not what is not
- Use "you approach": write from the reader's perspective, not the writer's
- Avoid hedging unless genuinely uncertain: "The business will generate" not "The business should hopefully generate"

**Strong verbs  replace weak constructions:**

| Weak | Strong |
|---|---|
| There is a need for | Requires |
| Make a decision | Decide |
| Give consideration to | Consider |
| Be in a position to | Can |
| Have an effect on | Affect |

**Parallelism**  all items in a list must follow the same grammatical form:

 `The business will: expand operations, hiring new staff, and we will enter new markets.`
 `The business will: expand operations, hire new staff, and enter new markets.`

**Report structure:**
1. Executive summary (conclusion first)
2. Introduction (scope and background)
3. Body (findings, analysis, evidence)
4. Conclusions
5. Recommendations
6. Appendices (supporting data)

---

## Narrative and Storytelling (Rubie & Provost)

**The Provost Paragraph**  the anatomy of a compelling story, applicable to any business narrative:

1. A character with a **want** (the founder, the customer, or the business itself)
2. A **problem** that stands in the way (conflict, gap, obstacle)
3. **Struggle**  the attempts to overcome the problem
4. **Deepening**  the stakes become clearer or higher
5. A moment of **resolution or revelation**
6. A **changed world**  how things are now different
7. An **emotional truth** the reader takes away
8. A **new question** that propels the reader forward

Apply to: executive summary, founder narrative, case study, market problem section.

**The high-concept hook**  open any document with one sentence that captures the entire proposition:

Formula: `[What the business does] + [for whom] + [in a way no one else does] + [producing what result]`

Uganda examples:
- *"A solar financing company that turns smallholder farmers in Northern Uganda into energy asset owners  without requiring collateral."*
- *"A Kampala cold chain operator that has cut post-harvest losses for 200 vegetable traders by 60% in 18 months."*

**Show, don't tell:**
-  "There is significant demand for this product."
-  "During our pilot, 47 traders in Owino Market placed repeat orders within two weeks  without being asked."

**The origin story**  the founder narrative should answer:
1. What problem did you personally encounter?
2. What did you try first (and why did it not work)?
3. What did you learn that nobody else knows?
4. What does success look like  for you and your community?

---

## Anti-AI Checklist (apply before finalising any section)

Remove every instance of:

- [ ] "In today's fast-paced world" / "In today's competitive landscape"
- [ ] "It is worth noting that" / "It should be noted that"
- [ ] "Robust" / "Leverage" / "Synergy" / "Seamless" / "Game-changing" / "Innovative solution"
- [ ] "Unlock" / "Dive into" / "Navigate" / "Harness" / "Delve"
- [ ] Sentences that start with "Furthermore, it is important to..."
- [ ] Lists of five bullet points each beginning with "Ensure that..."
- [ ] Any paragraph that describes what the next paragraph will say instead of saying it

Replace passive-voice constructions. Replace hedging language. Replace abstract nouns with concrete ones. Add a specific number or named place to any claim that currently has neither.

---

## References

- `references/words-at-work-hood.md`  Plain English checklist, reversed triangle, document structure, common mistakes table, editing checklists (Hood, *Words at Work*)
- `references/essay-writing-shiach.md`  Argument structure, introduction/conclusion formulas, transitions master list, waffle diagnosis test (Shiach, *How to Write Essays*)
- `references/business-english-geffner.md`  Four Cs, parallelism rules, business document conventions, positive framing, expressions to avoid, report/proposal structure (Geffner, *Business English*)
- `references/storytelling-rubie-provost.md`  Provost Paragraph, high-concept hook, scene-writing, conflict mechanics, book proposal structure applicable to business proposals (Rubie & Provost, *How to Tell a Story*)
- `../premium-commercial-writing/SKILL.md`  Cross-cutting premium commercial writing layer for commercial purpose, differentiation, proof, SEO/AI-search visibility, investor polish, and premium-fee quality gates.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Draft or content brief, audience, decision, purpose, and required action | Requester and owning plan or proposal skill | Required | Return an outline or request the missing decision; do not invent substance |
| Claims, evidence, assumptions, countercases, and citations | Research, client records, and subject owners | Required for persuasive claims | Cut or qualify unsupported claims |
| Voice, language, terminology, and approval constraints | Client guide and language skills | Conditional | Preserve existing voice and flag review needs |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Revised persuasive draft | Lender, investor, funder, client, board, or public reader | Governing thesis, argument, evidence, warrants, assumptions, risks, and action are clear without inflated language |
| Editorial decision log | Author and reviewer | Material cuts, unresolved evidence, substantive edits, and preserved voice are visible |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Claim-evidence-warrant check | Annotated draft or issue table | Every load-bearing claim is evidenced, qualified, or removed |
| Anti-slop release result | A/B/C/F audit with concrete findings | No grade F ships; fixes preserve specific and authored material |

## Capability Contract

Read or search access is required; editing or mutation is allowed only with authorised permission.

Critique defaults to read-only. Edit only when requested. Do not invent evidence, change approved numbers, alter legal or financial meaning, manufacture testimonials, or publish externally. Substantive claims remain owned by the relevant domain expert.

## Degraded Mode

If sources, audience context, language review, or editing access is unavailable, return the narrowest useful critique, proposed wording, and unassessed checks. Do not polish an unsupported assertion into apparent fact.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Paragraph has no claim, decision, evidence, or necessary transition | Cut or replace it | Polished filler |
| Claim is important but evidence is incomplete | Qualify it and state the evidence need | Confident wrongness |
| Technical detail changes the reader's decision | Keep and explain it plainly | Oversimplification |
| Unusual wording carries authentic voice | Preserve it unless clarity suffers | Mechanical homogenisation |

## Workflow

1. Confirm audience, decision, purpose, genre, voice, source authority, and editing scope.
2. Identify the governing thesis and the action or conclusion the reader must reach.
3. Map each load-bearing claim to evidence, warrant, assumption, countercase, and implication; stop on fabricated or unverifiable support.
4. Reorder content around reader questions and decision logic before sentence editing.
5. Rewrite for plain English, precision, varied rhythm, concrete examples, and honest trade-offs.
6. Verify names, figures, quotations, citations, legal and financial meaning against source material.
7. Run language and anti-slop checks; recover by restoring useful authored detail or qualifying unresolved claims.
8. Release with material limitations and unresolved evidence visible.

## Quality Standards

Every section must earn its place. The writing must help a named reader decide, retain the author's real point of view, and distinguish evidence from assumption without hype or filler.

## Anti-Patterns

- Opening with generic economic importance. Fix: start with the decision, tension, evidence, or consequence.
- Adding a market number to sound specific. Fix: verify and cite it or remove it.
- Using long words where short ones are precise. Fix: choose the clearest accurate term.
- Making every paragraph the same length and shape. Fix: vary rhythm according to the argument.
- Removing all risk to sound convincing. Fix: state the material countercase and mitigation.
- Replacing a founder's specific phrasing with generic corporate prose. Fix: preserve authentic voice and edit only for clarity.

## Worked Example

Replace `The company is well positioned to capture this market` with the supported logic: `Three wholesalers have signed trial letters covering 1,200 units, but the plan still depends on the proposed line reaching the tested reject-rate ceiling. Commercial launch therefore follows the commissioning test, not the calendar date.`
<!-- dual-compat-end -->
