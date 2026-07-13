---
name: meta-presentation-design
description: Use when designing or auditing a presentation deck tied to a business plan or proposal. Use pitch-deck for end-to-end deck orchestration.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Business Plan Presentation Design Skill

## Overview

Use this meta-skill to turn a business case into an effective presentation artifact and delivery plan. It covers slide structure, narrative pacing, visual standards, rehearsal, and presentation-audit logic.

## Use When

- Use when designing or auditing a presentation deck tied to a business plan or proposal.
- Use when coaching delivery, slide flow, or executive presentation quality.
- Use after the pitch frame is stable enough to visualise.

## Do Not Use When

- Do not use before the core story and ask are clear.
- Do not use visual polish to hide weak strategic thinking.
- Do not treat deck design as independent from the presenter's delivery.


- Route to `pitch-deck` instead when the task requires end-to-end deck orchestration.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Presentation Design brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Presentation objective, audience, and time limit
- Core business case, pitch frame, and final ask
- Any existing deck, brand constraints, or design preferences
- Evidence, visuals, and numbers that must appear on slides

## Workflow

1. Confirm the presentation context, duration, and audience expectations.
2. Translate the core argument into a slide-level narrative sequence.
3. Design or audit slides for clarity, emphasis, and evidence density.
4. Align delivery coaching with the final slide structure.
5. Reconcile visuals, spoken cues, and numbers with the underlying plan.
6. Flag slides or delivery habits that weaken persuasion.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the deck design and audit record and that the decision concerns which slide sequence and visual treatment support the decision.
- **Stop condition:** halt the affected conclusion if required evidence is missing (approved narrative, audience, brand assets, and display constraints) or if the work could lead to this identified risk: using visual polish to conceal missing evidence.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Slides make the argument easier to understand, not harder.
- The deck supports the presenter's narrative and timing constraints.
- Evidence appears where it matters most.
- Visual and verbal delivery stay aligned.

## Anti-Patterns

- Overcrowded slides that force the presenter to read.
- Decorative design with weak message hierarchy.
- Mismatched deck tone for the audience type.
- Slide claims that do not match the plan or pitch script.
- Treating a generic presentation design template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to meta presentation design. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Presentation Design deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A presentation deck structure, design direction, or audit result
- Delivery and rehearsal guidance tied to the deck
- Any unresolved presentation weaknesses to fix


## Relationship to Other Skills

This skill works in sequence with:
- **`meta-pitch-preparation`**  builds the psychological frame and pitch strategy (Klaff/McGowan). Run that first to establish what to say and how to frame it.
- **`meta-presentation-design`** (this skill)  builds the deck itself and trains the client to deliver it. Run after the pitch strategy is set.
- **`00-plan-assembly`**  the business plan document that the deck accompanies. Slides must align with plan sections.

The deck is not a condensed business plan. It is a visual argument that makes the audience want to read the plan and commit to the ask.

---

## Presentation Type Identification

Before designing any deck, confirm the audience and context  this determines every design decision:

| Context | Audience | Time | Slides | Dominant Mode |
|---|---|---|---|---|
| **Investor pitch** | Angel / VC / impact investor | 1520 min | 1012 | Narrative + aspiration |
| **Bank / DFI presentation** | Credit officer / loan committee | 2030 min | 1215 | Evidence + security |
| **Client proposal** | Procurement / decision-maker | 3045 min | 1520 | Problem-solution-ROI |
| **Grant committee** | Programme officers | 2030 min | 1215 | Impact + accountability |
| **Board / management** | Directors / senior management | 3060 min | 1525 | Strategy + data |
| **Public / community** | Stakeholders / partners | 2040 min | 1015 | Story + benefit |

---

## Mode A: Design the Deck

### Phase 1  Narrative Architecture (Before Opening PowerPoint)

**The cardinal rule:** Design the story before the slides. A deck is a visual translation of a narrative  not a filing system for information.

#### Step 1: Define the One Thing

Every presentation has one governing idea  the single thought you want the audience to carry out of the room. Everything in the deck either supports this idea or is cut.

Articulate it as a complete sentence (not a topic):
- Weak: "Market opportunity"
- Strong: "Uganda's UGX 4.2 trillion poultry market is structurally undersupplied, and [Business Name] is the only vertically integrated producer within 80 km of the largest deficit zone."

Test: Can it be said in one breath? Would someone repeat it to a colleague? If not, refine it.

#### Step 2: Build the Sparkline (Duarte)

The Sparkline is the narrative skeleton of every persuasive presentation. It alternates between two states:

- **What Is**  the current, imperfect reality your audience recognises
- **What Could Be**  the transformed future your business creates

The contrast between these states creates the emotional tension that drives action. The presentation oscillates between them, each cycle deepening the gap, until the final call to action resolves the tension.

**Sparkline for a business plan presentation:**

~~~text
OPENING:    What Is (the problem/gap the audience already knows)

SECTION 1:  What Could Be (the opportunity  if someone solves it)

SECTION 2:  What Is (why existing solutions fail)

SECTION 3:  What Could Be (your solution  specifically)

SECTION 4:  What Is (the current market evidence for your claims)

SECTION 5:  What Could Be (the financial outcome  projections)

CLOSE:      New Bliss (the future state after the audience acts  i.e., funds you)
~~~

**The STAR moment** (Something They'll Always Remember): Plan one moment in the deck  typically at the midpoint  that is so striking it becomes the anchor memory of the entire presentation. For a bank pitch: the DSCR and collateral ratio stated with absolute confidence, followed by a pause. For an investor: the market sizing insight that reframes the opportunity.

#### Step 3: Apply the Three-Act Structure (Gallo/Jobs)

| Act | Content | Purpose |
|---|---|---|
| **Act 1: Set the Stage** | The problem, the villain (the current reality), the stakes | Create urgency and emotional engagement |
| **Act 2: Introduce the Hero** | Your business, your solution, your team | Build belief and credibility |
| **Act 3: Resolution** | Financial proof, the ask, the call to action | Make saying yes feel inevitable |

The villain is not a competitor  it is the problem. The hero is not you  it is what becomes possible for the audience (and their portfolio/loan book) when they act.

#### Step 4: Audience Resistance Map (Duarte)

Before building slides, map the resistance for your specific audience:

| Audience | Primary Resistance | Secondary Resistance | How to Address |
|---|---|---|---|
| Bank credit officer | Repayment risk | Collateral adequacy | Lead with DSCR + collateral early; let evidence accumulate |
| Angel investor | Market size credibility | Team capability | Open with market insight; close with team unfair advantage |
| DFI programme officer | Development impact | Financial viability | Lead with impact story; then prove financial sustainability |
| Client / procurement | Delivery capability | Price justification | Lead with case study proof; close with ROI calculation |
| Board | Strategic fit | Resource requirement | Lead with strategic imperative; close with resource/return trade-off |

---

### Phase 2  Slide Architecture

#### The Business Plan Presentation Master Deck (1215 Slides)

**Slide 1: Cover**
- Business name, logo, tagline (the One Thing as a short phrase)
- Presenter name and date
- No clutter  this slide buys 30 seconds of first-impression time
- Visual: one powerful image that represents the opportunity or the solution

**Slide 2: The Hook / Opening Problem**
- State the problem or opportunity in one headline sentence (assertion-evidence format)
- One striking statistic or image that makes the scale undeniable
- No bullet points. Maximum 20 words of text.
- This is "What Is"  the reality the audience already partly knows but will now feel urgently

**Slide 3: The Opportunity (Market)**
- Market size stated as TAM  SAM  SOM with a simple funnel visual
- One growth rate figure with source
- Headline: "[Business Name]'s addressable market is [SOM]  and it is growing at [X]% annually"
- Cross-reference: `04-market-analysis/SKILL.md`

**Slide 4: Why Now**
- Three converging forces that have opened this window right now (Klaff)
- Visual: three icons or timeline
- This slide makes the opportunity feel urgent, not speculative

**Slide 5: The Solution**
- What the business does  stated in plain language
- One image or diagram of the product/service in use
- The unique mechanism: why this works when others haven't
- Cross-reference: `03-products-services/SKILL.md`

**Slide 6: Business Model**
- How money flows: from whom, for what, at what price, at what margin
- Simple diagram: Customer  Product/Service  Revenue  Cost  Profit
- Key unit economics: price per unit, COGS per unit, gross margin
- Cross-reference: `03-products-services/references/business-models-innovation-teece.md`

**Slide 7: Traction / Proof**
- The most credible evidence that this works: revenue, customers, pilots, LOIs, partnerships
- For pre-revenue: validation evidence  interviews, presales, deposits taken
- Headline states the conclusion: "Revenue has grown 3 in 18 months" not "Revenue Chart"
- Cross-reference: `meta-market-validation/SKILL.md` for validation evidence

**Slide 8: Competitive Landscape**
- 22 matrix or simple positioning map (not a competitor comparison table)
- Where the business sits in the upper-right quadrant and why it belongs there
- One sentence on sustainable competitive advantage
- Cross-reference: `06-competitive-analysis/SKILL.md`

**Slide 9: Operations / Go-to-Market**
- How the business reaches customers and delivers the product/service
- Key milestones already achieved (not just planned)
- For bank pitches: operational proof that the plan is executable

**Slide 10: Financial Projections**
- 3-year revenue and EBITDA in a clean bar chart (not a table)
- Headline: "[Year 3] revenue of [X] at [Y]% EBITDA margin"
- One key assumption stated explicitly
- For bank pitches: DSCR prominently stated  this is the most important number
- Cross-reference: `10-financial-projections/SKILL.md`

**Slide 11: The Team**
- Photos + 2-line bios of the top 23 people only
- Lead with the unfair advantage: "Former Head of Agriculture at [Bank], 12 years"
- Not a CV — every word must answer "why are YOU the team to do this?"
- Cross-reference: `09-management-team/SKILL.md`

**Slide 12: The Ask**
- Exact amount requested
- Equity percentage / loan terms / grant size  specific
- Use of funds: 45 line items maximum as a simple bar or pie
- What this funding achieves (tied to milestones)
- Next step: explicit and low-friction
- Cross-reference: `11-funding-request/SKILL.md`

**Slide 13: The Vision (Closing)**
- The future state  what the world looks like when this works
- Emotional close: the "New Bliss" state (Duarte Sparkline)
- Returns to the One Thing from Slide 1  full circle
- One powerful image. Minimal text.

**Backup slides (not presented unless asked):**
- Full financial model summary
- Detailed market sizing calculation
- Individual competitor analysis
- Management CVs in full
- Technical/product details
- Regulatory compliance status
- References and data sources

---

### Phase 3  Slide Design Standards

#### The Assertion-Evidence Format (Duarte)

Every slide has two elements:
1. **The headline**: a complete sentence that states the conclusion  not a topic label
   - Wrong: "Market Size"
   - Right: "Uganda's poultry market is worth UGX 4.2 trillion and growing at 12% annually"
2. **The evidence**: one visual (chart, image, diagram, quote) that proves the headline

This format forces every slide to make a claim and prove it  exactly what investors and bankers need.

#### Signal-to-Noise Reduction

Remove everything that doesn't directly support the headline:
- [ ] No bullet-point lists of more than 3 items
- [ ] No full sentences in body text  headlines only
- [ ] No decorative clip art or stock photos unrelated to content
- [ ] No tables with more than 4 rows and 4 columns (move to backup)
- [ ] No animations that distract (simple appear/fade only)
- [ ] No slide numbers visible to audience (use only for navigation reference)
- [ ] No corporate boilerplate footer on every slide

#### Typography
- Title font: minimum 36pt, sans-serif (Calibri, Helvetica, Gill Sans)
- Body text: minimum 24pt
- Captions/labels: minimum 18pt
- Maximum 2 font families per deck
- Contrast ratio: dark text on light, or light text on dark  never grey on grey

#### Colour
- 23 colours maximum (brand colours if available; if not: one strong primary, one accent, white/black)
- Consistent use: primary for headlines, accent for emphasis, white/black for body
- Financial slides: use colour intentionally  green for positive, amber for watch, red for risk

#### Charts and Data (Financial Slides)
- Bar charts for comparisons and trends (preferred for financials)
- Line charts for growth over time
- Pie charts only for market share (and only when 5 or fewer segments)
- Never use 3D charts  they distort data perception
- Title every chart with the conclusion, not a description
- Label the most important data point directly on the chart
- Source every external data point (small text, bottom of slide)

#### Dress Up Numbers  Make Data Vivid (Gallo/Jobs)

Raw figures mean nothing without context. The presenter who translates numbers into vivid comparisons the audience already understands is the one remembered.

| Raw figure | Dressed up |
|---|---|
| "Year 3 EBITDA: UGX 840M" | "By Year 3, this business generates the equivalent of two management salaries every week  from operations alone." |
| "The market is worth UGX 4.2 trillion" | "Uganda's poultry market is larger than the national road maintenance budget  and growing faster." |
| "Collateral value: UGX 180M on a UGX 120M loan" | "Every UGX 100 we borrow is secured by UGX 150 in registered property." |
| "We create 23 direct jobs" | "We create 23 jobs  that is 23 families moved off subsistence income in the first 18 months." |

**Rule:** Find the comparison. Make the number specific. Connect it to a reference frame the audience already holds. This technique requires no design skill and can be deployed verbally even if the projector fails.

#### The "Glanceable Test" (Duarte)
Hold the slide at arm's length for 3 seconds. If the key message is not immediately clear, the slide has too much information or too little visual hierarchy. Redesign.

#### The Rule of Three (Gallo/Jobs)
Structure every multi-point section in threes:
- Three market forces driving opportunity
- Three competitive advantages
- Three milestones the funding will achieve
- Three reasons the team is uniquely qualified
The human brain clusters information in threes. More than three items and retention drops sharply.

---

## Mode B: Client Coaching Protocol

Prepare the client's delivery through message ownership, rehearsal, voice and body-language practice, timed runs, and hostile-question drills. Coaching must use the actual deck and record unresolved weaknesses.

See [`references/client-coaching-protocol.md`](references/client-coaching-protocol.md) for the detailed procedure.

## Mode C: Deck Audit

Use before any presentation. Score each dimension 15.

### Narrative Audit
- [ ] Is there a single governing idea (the One Thing)?
- [ ] Does the deck follow a Sparkline structure  contrast between What Is and What Could Be?
- [ ] Is there a STAR moment  one memorable, striking element?
- [ ] Does the opening create urgency in the first 60 seconds?
- [ ] Does the close make the ask feel inevitable?

### Slide Design Audit
- [ ] Every slide has an assertion headline (complete sentence stating a conclusion)?
- [ ] No slide has more than one key message?
- [ ] No bullet-point lists of more than 3 items?
- [ ] Every chart is titled with its conclusion, not its description?
- [ ] The "glanceable test" passes  key message clear in 3 seconds?
- [ ] Font sizes: minimum 24pt body, 36pt titles?
- [ ] No 3D charts, excessive animation, or decorative clutter?

### Financial Slides Audit
- [ ] DSCR stated prominently (for bank pitches)?
- [ ] Revenue chart headlined with conclusion ("Revenue grows 3 in 24 months")?
- [ ] Use-of-funds visual (not table) with 45 line items?
- [ ] Every data point sourced or traceable to business plan projections?
- [ ] Numbers consistent with the business plan document (see `meta-due-diligence/SKILL.md` Mode C)?

### Delivery Readiness Audit
- [ ] Client can speak to every slide without reading it?
- [ ] Client knows 5 key numbers cold?
- [ ] Q&A responses prepared for 10 hardest questions?
- [ ] STAR moment rehearsed and timed?
- [ ] Opening and close are word-perfect?
- [ ] Full dress rehearsal completed?

---

## Generation Process

1. Confirm presentation type and audience (use the Presentation Type table)
2. **Mode A:**
   - Articulate the One Thing
   - Build the Sparkline narrative
   - Map audience resistance
   - Design the slide architecture (1215 slides using the master deck template)
   - Apply design standards (assertion-evidence, signal-to-noise, rule of three)
3. **Mode B:**
   - Schedule and run the 6-session coaching programme
   - Deliver Q&A simulation with resistance-mapped questions
   - Conduct dress rehearsal and debrief
4. **Mode C:** Apply all four audit checklists; produce priority fix list

## Quality Criteria

- One Thing is articulated before slide 1 is built
- Sparkline contrast is present  the deck oscillates between What Is and What Could Be
- Every slide headline is a complete assertion, not a topic label
- No slide fails the 3-second glanceable test
- Financial numbers are consistent with the business plan document
- Client can present without slides if the projector fails
- Client has rehearsed a minimum of 6 times
- Q&A simulation covered the 10 hardest questions for this specific audience

## References

- `references/presentation-secrets-jobs-gallo.md` - Three-act structure; the One Thing; Rule of Three; STAR moments; Twitter-friendly headlines; making numbers meaningful; opening lines; Jobs rehearsal methodology; analogue-first design process; business plan deck application table - Source: Gallo (McGraw-Hill, 2010). **Read for narrative structure, memorable moments, and the overall presentation philosophy.**
- `references/persuasive-presentations-duarte.md` - Sparkline (What Is / What Could Be contrast); assertion-evidence slide format; STAR moment; audience resistance mapping; signal-to-noise reduction; visual grammar; data slides; financial chart standards; slide transformation guide (before/after) - Source: Duarte (HBR Press, 2012). **Read for slide design standards and narrative persuasion structure. Primary visual design reference.**
- `references/data-storytelling.md` - context-first visual selection, clutter reduction, focus cues, chart annotation, and executive-story sequencing distilled from *Storytelling with Data*, *Master Data Storytelling*, and *Strategic Storytelling*
- `references/innovative-presentations-anthony.md` - Audience engagement techniques; innovative opening strategies; non-linear presentation options; storyboarding methodology; presenting to sceptical/analytical audiences; audience type adaptation guide - Source: Anthony (Wiley, 2014). **Read for engagement techniques and how to adapt to different audience types.**
- `references/presentation-skills-edwards.md` - Voice and delivery fundamentals; managing nerves; body language; Q&A handling; self-assessment methodology; before/during/after checklists; coaching and development progression - Source: Edwards. **Read for delivery coaching - the client training protocol draws heavily from this reference.**
- `references/hbr-presentations-anthology.md` - Executive presentation standards; presenting data to boards; research-backed persuasion principles; virtual presentation techniques; financial data visualisation for executives - Source: Harvard Business Review. **Read for executive-level standards and evidence-based presentation design.**
- `meta-pitch-preparation/SKILL.md`  Pitch strategy and frame control (Klaff STRONG method, McGowan 7 Principles). Run before this skill to establish the psychological frame the deck must embody.
- `01-executive-summary/references/pyramid-principle.md`  SCQA structure. The deck narrative should mirror the executive summary SCQA logic.
- `meta-due-diligence/SKILL.md`  Mode C: every claim on every slide must pass the DD audit. Run alongside the deck audit.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Deck design and audit record decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to using visual polish to conceal missing evidence. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the deck design and audit record; editing the supplied deck when design authority is explicit is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If approved narrative, audience, brand assets, and display constraints cannot be obtained, return a qualified deck design and audit record covering only the checks that remain supportable. Leave this decision unresolved: which slide sequence and visual treatment support the decision. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which slide sequence and visual treatment support the decision | Record the conclusion, source trail, owner, and review trigger in the deck design and audit record. | Risk of using visual polish to conceal missing evidence |
| Material evidence conflicts or remains uncertain | Prototype the disputed slide as a visual and as a concise evidence slide, then test legibility and comprehension in the real display context. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: approved narrative, audience, brand assets, and display constraints | Mark the decision on which slide sequence and visual treatment support the decision `not assessed` in the deck design and audit record, and send it to the presentation owner and intended speaker. | Otherwise, the work risks using visual polish to conceal missing evidence |

## Quality Standards


Accept the deck design and audit record only when evidence is sufficient for this decision: which slide sequence and visual treatment support the decision. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of using visual polish to conceal missing evidence.

## Worked Example


A dense market slide is legible on a laptop but not in the meeting room. Replace the table with one sourced comparison and move supporting detail to the appendix after a projected-size check.

<!-- dual-compat-end -->
