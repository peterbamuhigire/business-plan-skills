---
name: 01-executive-summary
description: Use when producing or reviewing the 01 executive summary component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Executive Summary Skill

## Use When

- Use after the core plan sections are complete and the final numbers are known.
- Use when a reader must understand the whole opportunity in 2-3 pages or less.
- Use when a plan, proposal, or funding document needs a decision-ready front section.

## Do Not Use When

- Do not draft this first and hope the rest of the plan catches up later.
- Do not use it to introduce new claims that are not supported elsewhere in the plan.
- Do not use it as a generic company description; it must function as a compressed investment case.

## Required Inputs

- Final or near-final outputs from Sections 02-15
- Audience type: bank, investor, DFI, grant committee, partner, or board
- Final funding ask, use of funds, and financial highlights
- The governing thesis or key investment case if `meta-consulting-synthesis` has been run

## Workflow

1. Extract the strongest claims, numbers, and reader-specific priorities from the completed plan.
2. Identify the one governing thought and strongest hook.
3. Draft using the Context -> Approach -> Results -> Ask structure.
4. Compress the plan into a short, high-signal summary without losing financial and decision logic.
5. Apply `premium-commercial-writing` for investor/lender polish, proof calibration, premium credibility, and decision-ready language.
6. Reconcile every claim and number against the underlying sections.
7. Revise for clarity, persuasion, and scanability.

## Quality Bar

- A busy decision-maker can understand the business and the ask in under two minutes.
- The opening lands immediately and states the core conclusion early.
- The summary is numerically consistent with the final plan.
- The ask is specific and the next step is clear.

## Anti-Patterns

- Writing this before the rest of the plan is stable.
- Leading with company history instead of the decision case.
- Burying the ask or the economics at the end.
- Repeating section headings without synthesising them.

## Outputs

- A 2-3 page executive summary
- A reader-specific hook and governing thought
- Financial and ask highlights that match the plan
- Any unresolved inconsistencies blocking finalisation



Generate the executive summary  the single most important section of a bankable business plan. Investors decide within 60 seconds whether to keep reading.

**Core principle:** The executive summary is not an introduction. It is a standalone document that enables a busy decision-maker to understand the entire business, assess its viability, and decide whether to invest  without reading anything else (Jewinski).

## Invoke AFTER all other plan sections (02-15) are complete.

## The Four-Step Formula

Every executive summary follows this structure (Jewinski):

1. **Context**  Set the stage: who, what, when, why this matters now
2. **Approach**  How the business addresses the opportunity (model, strategy)
3. **Results**  Traction, projections, evidence of viability
4. **Recommendation/Ask**  The funding request and expected returns

## Required Elements

1. **The Hook**  Opening sentence that captures the single most compelling aspect. Lead with your strongest point. Start at the ending  state the conclusion first (NIBM: "Don't start at the beginning. Start at the ending.")
2. **Business concept**  What the company does, in one paragraph
3. **Problem & opportunity**  The market gap, stated with urgency
4. **Solution**  Products/services and unique value proposition
5. **Target market**  Who buys and market size (TAM/SAM/SOM)
6. **Business model**  How revenue is generated
7. **Competitive advantage**  Defensible moat, not generic claims
8. **Traction & milestones**  Evidence of market validation, product usage, retention, or repeatable sales motion
9. **Financial highlights**  Revenue projections, margins, break-even
10. **Team snapshot**  Key leaders and relevant track record
11. **Funding request**  Amount, use of funds, expected ROI/exit
12. **Call to action**  Clear next step for the reader
13. **Growth engine**  The repeatable mechanism that turns customer signal into revenue: channel, conversion path, retention loop, referral/expansion trigger, and operating owner

## Writing Standards

### Lead with Impact

The opening sentence is the "lead"  the lure that grabs the reader. If it is clear and dynamic, the reader forges on. If muddled or dull, they stop (NIBM).

**Lead format options:**
- State the problem being solved with a revealing detail
- Open with a dramatic but substantiated forecast
- Summarise the core value proposition in one sentence
- Use a concrete metric that demonstrates scale or traction

**Never** open with "The purpose of this document is..." or generic platitudes.

### Force and Clarity

- **Active voice always.** "We generated UGX 8.9B in Year 1 revenue" not "Revenue of UGX 8.9B was generated." Passive verbs drain energy and sound evasive (NIBM).
- **Positive language.** State what IS, not what ISN'T. "We reduced costs by 40%" not "We did not fail to reduce costs."
- **Be specific.** Replace vague qualifiers with concrete data. "A significant market" becomes "UGX 15.5T addressable market growing at 12% CAGR."
- **Average sentence length: 17-20 words.** Comprehension drops sharply beyond 25 words per sentence (NIBM research).
- **Prune ruthlessly.** Every word must pull its weight. Eliminate zero-words, needless intensifiers, and pompous phrasing.

### Audience Awareness

Before writing, establish (Jewinski):
- **Who** will read this summary? (Investors, lenders, board, partners)
- **What** do they already know about this industry?
- **What decisions** will they make based on this document?
- **What are their priorities?** (ROI, risk, social impact, scalability)

Write for the least-informed decision-maker in the audience. Define technical terms on first use with brief appositives.

### Presentation Structure

Structure the summary for both reading and presenting (Bradbury):

- **Chunk information**  Group related points into clear sections with visual breaks
- **One idea per paragraph**  Never bury multiple arguments in a single block
- **Signpost transitions**  Guide the reader: "The market validates this approach..." / "With this team in place..."
- **Close with an echo**  Repeat a key phrase or metric from the opening to bring the reader full circle

## Format Guidelines

- Maximum 2-3 pages (800-1,200 words)
- Use bullet points for financial highlights and milestones  they aid scanning (Jewinski: "The Case for Bullets")
- Include one small table for financial snapshot if appropriate
- White space matters  avoid dense walls of text
- Write in present tense for current state, future tense for projections

## Generation Process

1. Review all completed sections (02-15) and extract key data points
2. Identify the single strongest selling point  this becomes the lead
3. Draft using the four-step formula: Context  Approach  Results  Ask
4. Weave in all 12 required elements
5. Apply the revision process (see references/writing-quality.md) and the premium investor-document gate (see `../premium-commercial-writing/references/document-investor-polish.md`)
6. Verify financial figures match section 10 exactly
7. Run the six-question verification test

## Six-Question Verification Test

After drafting, confirm the reader can answer (Jewinski):

1. What does this business do and for whom?
2. What is the market opportunity and how large is it?
3. How does the business make money?
4. What evidence exists that this will succeed?
5. How much funding is needed and what will it achieve?
6. What is the expected return for the investor?

If any question cannot be answered clearly from the summary alone, revise.

## Quality Criteria (Bankability Check)

- Can a reader understand the entire business in under 2 minutes?
- Does the opening sentence create immediate interest?
- Are all financial claims specific and traceable to projections?
- Is the funding ask clear with defined use of funds?
- Does it create urgency without being pushy?
- Would an investor want to read the rest of the plan?
- Is every sentence in active voice with concrete language?
- Has the summary been revised at least once for clarity and brevity?
- Does it state the growth engine and primary profit lever, not only the market opportunity?

### Elevator Pitch Integration

For investor-facing summaries, structure the core proposition using these proven templates:

**60-Second Pitch** (Nager et al, 2011): 4 timed segments
- 5-10 sec: Who are you?
- 10-20 sec: What problem does your product solve?
- 10-20 sec: What is your solution?
- 5-10 sec: What do you need? (team/funding)

**Short Elevator Pitch** (Alam): "For [customer], we provide [solution], to [need + insight]. Currently [alternatives] lack [advantage]. Without this, [impact of inaction]."

**Long Elevator Pitch** (Alam, adds investor-facing elements): short version + TAM, initial target segment, go-to-market channel, growth rate, pricing, USP, team, traction, funding ask with equity stake.

### Pyramid Structure Test (Minto)

Before finalising the executive summary, apply the Pyramid Principle test (Minto, 2010):

**The SCQA check:** Does the opening paragraph follow Situation  Complication  Question  Answer?
- *Situation*: What the reader already knows to be true about the industry/business
- *Complication*: What changed or what gap exists that creates urgency
- *Question*: What the reader needs answered (implicitly or explicitly)
- *Answer*: The governing thought  your main point, stated first

**The 30-second test:** Can a reader extract the governing thought and all Key Line points in under 30 seconds? If not, restructure. The executive summary is already the pyramid in compressed form  the opening paragraph IS the top box, the bullet headings ARE the Key Line.

**Blank assertion test:** Replace any "three reasons" or "five objectives" statements with the actual insight those points collectively imply. "We have three competitive advantages"  "Our cost structure is 40% below competitors because we own the supply chain."

See `references/pyramid-principle.md` for the full framework including MECE grouping rules, deductive vs. inductive structure, and the problem-definition framework (R1/R2) that maps directly onto the Situation/Complication logic.

### StoryBrand One-Liner Test (Miller)

Before finalising the executive summary, confirm that the business concept can be compressed into a StoryBrand one-liner (Miller, 2017):

> "We help [CHARACTER] who [PROBLEM] [ACHIEVE RESULT / TRANSFORMATION]."

**The test:** Read the one-liner aloud to someone unfamiliar with the business. Can they immediately explain who this is for, what problem it solves, and what transformation it delivers? If not, the executive summary's opening paragraph will also fail to land.

**Common failure pattern:** Executive summaries that lead with the company name, founding year, and product description  rather than the customer's problem and the transformation on offer. The one-liner forces customer-centric framing from the first sentence.

**Application to the executive summary hook:** The opening sentence of the executive summary should contain the essence of the one-liner  stated in narrative form rather than template form.

*Bad:* "KisaFarm Limited is a poultry processing company established in 2022 in Kampala, Uganda."
*Better:* "Every week, 40,000 Kampala households buy chicken from a street vendor because no affordable, safe, packaged option exists  KisaFarm is changing that."

See `../07-marketing-sales-strategy/references/storybrand-framework.md` for the full BrandScript template, three-level problem framework (external/internal/philosophical), guide positioning, and identity transformation arc.

### Brand Story Narrative Test (Brito)

Before finalising the business concept paragraph, apply the Hero Narrative test (Brito, 2013):

**The simplification test:** If you cannot explain the brand story in one sentence to someone who has never heard of the business, it is not yet clear enough.

The business concept paragraph should answer: *"What is the one story this brand tells, consistently, across every channel?"*  not the tagline, not the mission statement, but the narrative that demonstrates how the business relates to the lives of its customers.

**Four-step narrative construction:**
1. State the customer's world *before* the business existed (the problem state)
2. Describe the specific change the business creates (the transformation)
3. Quantify that transformation where possible (time saved, money kept, outcome achieved)
4. Name who this is for (the customer, as specifically as possible)

**Test:** Read your business concept paragraph aloud. If it could describe any business in the sector, it is not specific enough. It should be impossible to confuse this business with a competitor after reading two sentences.

### Venture Type Framing

Frame the executive summary appropriately for the venture type (Blank & Dorf, 2012):

| Type | Focus | Investor Expectation |
|---|---|---|
| Small business | Lifestyle, cash flow, local market | Steady returns, loan repayment |
| Scalable startup | Growth, market capture, exit | 10+ return, equity stake |
| Buyable startup | Build to sell (acquisition target) | Quick flip, modest return |
| Large company venture | New division, innovation lab | Strategic value, internal ROI |
| Social enterprise | Impact + sustainability | Blended return (social + financial) |

## Common Mistakes to Avoid

- Writing the executive summary first (it must be written last)
- Burying the conclusion or ask at the end instead of leading with it
- Using passive voice and vague language ("significant growth potential")
- Including jargon without explanation for the reader
- Exceeding 3 pages  brevity is the soul of bankability
- Making claims not supported by data in the detailed sections
- Introducing new information not covered elsewhere in the plan

## References

- **Writing quality and revision process**: See `references/writing-quality.md` for detailed writing standards, revision workflow, and word-economy rules
- **Premium investor and document polish**: See `../premium-commercial-writing/references/document-investor-polish.md` and `../premium-commercial-writing/references/premium-writing-quality-gate.md` for decision-ready summaries, claim calibration, proof, funding ask polish, and premium commercial texture
- **Persuasion and presentation techniques**: See `references/presentation-structure.md` for audience analysis, persuasive structuring, and visual communication principles
- **Proposal summarisation patterns**: See `references/proposal-patterns.md` for examples and templates of effective executive summaries for funding proposals
- **Brand story and Hero Narrative framework**: See `../07-marketing-sales-strategy/references/social-business-brand-strategy.md` for Brito's nine-input content narrative framework, Hero Narrative simplification test, converged media model (paid/earned/owned), and content governance principles  applicable when writing the business concept paragraph and brand positioning statement
- **Pyramid Principle  structure and logic**: See `references/pyramid-principle.md` for Minto's full framework: SCQA opening formula, pyramid rules (MECE groupings, three logical orders, deductive vs. inductive), the 30-second test, intellectually blank assertion errors, and the problem-definition framework (R1/R2  Q  A)  the structural backbone for executive summaries, proposals, and any document where the purpose is to present thinking clearly
- **Growth, profit, disruption, and transformation logic**: See `../../book-extractions/growth-profit-disruption-systems-extraction.md` when the executive summary must explain a repeatable growth engine, product-led growth, AI-enabled growth, disruption strategy, or profit improvement thesis.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Completed and reconciled plan sections plus target-reader decision criteria for 01 executive summary | Plan assembly workspace and engagement brief | Yes | If absent, the body plan or reconciled funding ask is unavailable, return a summary outline with blocked claims rather than drafting confident prose. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Decision-led executive summary | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 01 executive summary exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 01 executive summary release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Summary-to-section claim map and funding-ask reconciliation | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 01 executive summary decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 01 executive summary review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 01 executive summary, the controlling focus is governing thesis, decision-maker relevance, plan-body traceability, traction evidence, funding-ask reconciliation, and material risk disclosure. This skill may compress approved plan evidence and sharpen the governing thesis; it may not introduce a market size, traction claim, projection, or funding use absent from the body. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 01 executive summary, loss of evidence about 01 executive summary evidence, decisions, failure thresholds, ownership, and downstream handoffs activates degraded mode. If the controlling 01 executive summary evidence is unavailable, the same boundary applies. When the body plan or reconciled funding ask is unavailable, return a summary outline with blocked claims rather than drafting confident prose. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 01 executive summary, a detail is persuasive but unsupported or immaterial to the reader's decision| remove it from the summary or route it to the owning section for evidence | Headline claims that fail diligence damage trust in the entire plan |
| For 01 executive summary, A current legal, regulatory, tax, accounting, market, or platform claim controls the 01 executive summary decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 01 executive summary, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete decision-led executive summary, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 01 executive summary decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect completed and reconciled plan sections plus target-reader decision criteria and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce decision-led executive summary with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Decision-led executive summary must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Summary-to-section claim map and funding-ask reconciliation must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 01 executive summary, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 01 executive summary, treating an unavailable completed and reconciled plan sections plus target-reader decision criteria as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing decision-led executive summary that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A plan describes three pilot customers but provides no signed evidence. State that pilots are under validation and identify the evidence needed before claiming commercial traction.

## References

- Use the verified project evidence register and the owning upstream pipeline section for 01 executive summary; no local deep-dive reference is declared.
- For 01 executive summary claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
