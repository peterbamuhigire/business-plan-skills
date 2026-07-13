---
name: meta-pitch-preparation
description: Use when preparing for an investor, lender, donor, client, or board pitch. Use pitch-deck for end-to-end deck orchestration.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Pitch Preparation Meta-Skill

## Overview

Use this meta-skill to prepare the spoken strategy for a live pitch. It helps the presenter decide what the audience must believe, how the argument should be framed, and how likely objections should be handled.

## Use When

- Use when preparing for an investor, lender, donor, client, or board pitch.
- Use when coaching a client through a live presentation or defence.
- Use when a deck exists or will exist, but the message strategy still needs work.

## Do Not Use When

- Do not use as a substitute for fixing weak economics, weak evidence, or weak strategy.
- Do not jump straight to slide design if the spoken frame is still unclear.
- Do not use for written-only proposals with no live presentation component.


- Route to `pitch-deck` instead when the task requires end-to-end deck orchestration.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Pitch Preparation brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Audience type, decision context, and time available
- Core business case, funding ask, and key supporting evidence
- Known objections, sensitivities, and presentation constraints
- Any existing deck, notes, or related plan sections

## Workflow

1. Identify the pitch type and the audience's primary question.
2. Build the persuasive frame, governing thought, and sequencing logic.
3. Prepare the opening, evidence flow, ask, and likely Q&A.
4. Reconcile the spoken case with the underlying plan and numbers.
5. Tighten the pitch for brevity, clarity, and psychological impact.
6. Flag any weakness that will fail in a live setting.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the pitch delivery brief and that the decision concerns which hook, proof, and ask the speaker must own.
- **Stop condition:** halt the affected conclusion if required evidence is missing (audience decision, approved story, timing, and likely objections) or if the work could lead to this identified risk: coaching performance around an unsupported story.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The presenter can state the case clearly, quickly, and convincingly.
- Framing matches the audience's incentives and objections.
- The spoken logic is consistent with the written plan.
- Q&A preparation addresses real pressure points.

## Anti-Patterns

- Presenting information without controlling the frame.
- Memorising lines instead of understanding the argument structure.
- Using one pitch style for investors, lenders, donors, and buyers alike.
- Letting the live story drift away from the actual evidence.
- Treating a generic pitch preparation template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to meta pitch preparation. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pitch Preparation deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A prepared pitch frame, message strategy, and rehearsal plan
- Anticipated Q&A and objection-handling notes
- Open issues to resolve before presenting


## When to Use

**Mode A  Prepare Your Own Pitch:** You are pitching to investors, a bank, a client, or a grant committee. Use this skill to build, structure, and rehearse your pitch.

**Mode B  Coach a Client's Pitch:** Your client has a pitch coming up. Use this skill to audit their materials, rebuild their pitch frame, and prepare them for delivery and Q&A.

**Mode C  Pitch Audit:** Review an existing pitch deck or presentation script for structural and psychological weaknesses before the pitch day.

---

## Pitch Type Identification

Before preparing any pitch, identify the type  this determines frame, structure, and delivery style:

| Pitch Type | Primary Audience | Their Core Question | Win Condition |
|---|---|---|---|
| **Equity investor** (angel, VC, PE, impact) | Return on capital | Will this make me money at acceptable risk? | Intrigue + traction + credible exit |
| **Bank / DFI loan** | Repayment security | Can and will they repay? | DSCR + collateral + character |
| **Client proposal** | Value delivery | Will this solve my problem better than alternatives? | Fit + competence + price confidence |
| **Grant / donor** | Programme objectives | Does this advance our mission? | Theory of Change + impact + accountability |
| **Board / management** | Strategic fit | Is this the right use of our resources? | Logic + data + risk mitigation |
| **Government / public tender** | Compliance + value | Do they meet our criteria at best price? | Specification compliance + track record |

---

## Mode A: Prepare Your Own Pitch

### Phase 1  Frame Architecture (Klaff)

Before building slides or a script, establish the frame. Klaff's STRONG method provides the sequence:

**S  Set the Frame**
Establish your frame before the audience can impose theirs. Identify which frame the room will attempt to use (power frame, time frame, analyst frame) and prepare your counter-frame. Never enter someone else's frame  reframe immediately and with confidence.

- Power frame counter: Arrive with a prize frame. You are selective about who you work with.
- Time frame counter: Acknowledge the constraint, then control the sequence. "We have 20 minutes  I'll cover the three things that matter most."
- Analyst frame counter: "I'll send the detailed model. Right now I want to show you the opportunity."

**T  Tell the Story**
Open with a story that establishes novelty and context. The crocodile brain (the oldest, most primitive decision-making layer) filters everything first: is this dangerous? Is this novel? Is this relevant? Only novelty and emotional relevance pass through. Facts do not.

- The story must be: brief (under 2 minutes), personal or firsthand, and lead to a "and that's when I saw the opportunity" moment.
- Do NOT open with company history, founder credentials, or slide 1 of a deck. Open with the story.

**R  Reveal the Intrigue**
After the story, create a genuine knowledge gap  something the audience does not yet know but wants to know. The gap must be real and resolvable within the pitch.

- "Most people don't know that [counterintuitive insight about the market / problem]."
- The intrigue frame keeps attention without generating anxiety.

**O  Offer the Prize**
You are not chasing this deal. You are offering a limited opportunity that the right partner will qualify for. The prize frame reverses the typical power dynamic  the pitcher becomes the prize, not the supplicant.

- Push/pull mechanics: advance with enthusiasm, then briefly pull back. "This is exactly the kind of project we want to be doing  though we are selective about who we partner with."
- Eradicate neediness entirely. Never say "we really need this" or "I hope you'll consider."

**N  Nail the Hookpoint**
The hookpoint is the moment of peak interest  when the audience leans forward, commits attention, and wants to know more. It typically arrives 10-15 minutes in. Structure your material so the highest-intrigue element lands at the hookpoint, not at the start.

- Signs you've hit the hookpoint: questions become specific (not sceptical), the audience references the future ("so once you've done X, would you then..."), body language shifts toward you.
- If the hookpoint never arrives, the frame has not been established.

**G  Get the Deal**
Close while momentum is high. Never let the pitch end without a clear next step. The close should not feel like a close  it should feel like a natural next action that both parties are already leaning toward.

- Time constraint close: "We're moving forward with our core partners by [date]  are you in?"
- The "no" close: offer the audience permission to say no. This reduces anxiety and paradoxically increases yes rates.

---

### Phase 2  Message Architecture (McGowan)

Once the frame is set, structure the message for maximum clarity and retention.

**Hook  Meat  Payoff**

Every pitch, every answer, every section of a pitch follows this three-part structure:

- **Hook:** A single, compelling, counterintuitive, or visual opening statement. Not a question. Not "let me tell you about..." The hook arrests attention in the first 8 seconds.
  - Formula: [Startling fact / Vivid image / Bold assertion] + [So what it means for this audience]
  - Test: Would someone repeat this hook at dinner tonight?

- **Meat:** The three most important points that support your hook. Exactly three  not two, not six. Each point must be: distinct, memorable, and independently valuable.
  - Use the "Scalpel not a Shovel" rule: cut everything that isn't essential to the three points. No tangential data. No qualifications that can go in the appendix.
  - Flag your structure: "There are three things that make this business uniquely positioned: first... second... third..."

- **Payoff:** What you want the audience to do, feel, or remember. Explicit and specific. A payoff is not a summary  it is a call to action or a crystallising statement that makes the ask feel inevitable.
  - For investor pitches: "We are raising [amount] at [terms]. The right investor gets in now before [milestone]."
  - For bank presentations: "We are requesting [amount] over [term]. The numbers show we can service this debt from day one."

---

### Phase 3  Pitch Structure by Type

#### Investor Pitch (20-Minute Format  Klaff standard)

| Segment | Duration | Content |
|---|---|---|
| Frame open + story | 3 min | Personal story that reveals the opportunity; establish prize frame |
| The Big Idea | 2 min | One sentence: what it is, who it's for, why now |
| Market opportunity | 3 min | TAM/SAM/SOM; bottom-up sizing; growth driver |
| Solution and business model | 3 min | How it works; how you make money; why this model |
| Traction and proof | 3 min | Revenue, users, pilots, LOIs, strategic partnerships |
| Team | 2 min | Unfair advantage only — not CVs. Why are YOU the team to do this? |
| The ask | 2 min | Amount, use of funds (4 items max), what milestones it funds, next step |
| Intrigue close | 2 min | Reveal the hook  the thing they don't know that changes everything |

**Frame management throughout:** Reframe every sceptical question using the "Yes, and" bridge  acknowledge, reframe, advance. Never become defensive.

#### Bank / DFI Loan Presentation

The bank pitch is fundamentally different from the investor pitch. Banks are not buying upside  they are managing downside. Their crocodile brain asks: "What could go wrong?" Frame accordingly.

| Segment | Duration | Content |
|---|---|---|
| Context + credibility hook | 2 min | Hook: "Our business has operated for X years and has never missed a supplier payment." Establish character first. |
| Business overview | 3 min | What we do, how long, key clients/customers, track record |
| The opportunity | 3 min | Why now; what the loan enables; how it grows the business |
| Financial proof | 5 min | Revenue trend, profitability, cash flow  show the numbers tell a story |
| Loan request + use of funds | 3 min | Exact amount; 4-5 line items; DSCR calculation stated clearly |
| Collateral and security | 2 min | Primary collateral; valuation basis; coverage ratio |
| Repayment plan | 2 min | Source of repayment; schedule; what happens if revenue dips |

**Key frame for bank pitches:** You are not seeking charity. You are offering the bank a well-secured, income-generating asset. They are lucky to have you as a client. Prize frame still applies  delivered with professional restraint.

**Cross-reference:** See `11-funding-request/SKILL.md` for DSCR calculation, collateral statement, and CAMPARI compliance. Ensure these are complete before the presentation.

#### Client Proposal Pitch

| Segment | Content |
|---|---|
| Hook | The client's problem  stated more precisely than they stated it |
| Diagnosis | Show you understand the root cause (not just the symptom) |
| Solution | How your approach specifically addresses the root cause |
| Proof | Case study, testimonial, or comparable result  social proof |
| Investment | Price positioned as ROI, not cost |
| Next step | Specific and low-friction: "Can we schedule a site visit for Tuesday?" |

---

### Phase 4  Delivery Preparation (McGowan)

Delivery quality determines whether good content is received or rejected.

**The Three Ps:**
1. **Presence**  Be fully engaged with the room, not your slides. The audience watches you, not your deck.
2. **Passion**  Not performance. Genuine belief in what you are pitching. If you do not believe it, the crocodile brain of your audience will detect the incongruence.
3. **Preparation**  Knowing your content so completely that you can abandon the script when needed and return without loss.

**Vocal delivery:**
- Pace: Slow down at key points. Speed signals nerves; deliberate pace signals confidence.
- Pauses: Use them. A 2-second pause after a major statement creates emphasis better than any word.
- Avoid: vocal fry, upward inflection at the end of statements (makes assertions sound like questions), filler words (um, so, like, basically, you know).

**The Adrenaline Protocol:**
Adrenaline before a pitch is not a problem  it is fuel. Redirect it:
- Breathe slowly (4 counts in, 4 hold, 6 out) for 3-4 minutes before entering
- Adopt a strong physical posture 5 minutes before (not during)
- Arrive early enough that you are the most comfortable person in the room, not the last to arrive

**Q&A preparation:**
- Anticipate the 10 hardest questions. Write full answers. Practice delivering each in under 60 seconds.
- Bridging technique: Acknowledge the question, bridge to your frame, answer from your territory. "That's an important concern. What I can tell you is..." (then answer from strength).
- Flagging: Signal what is important. "The key thing to understand here is..."  this anchors attention.

---

## Mode B: Coach a Client's Pitch

### Step 1  Intake Assessment

Before touching content, assess:
- What type of pitch is this? (Use the Pitch Type table above)
- What is the specific ask  exact amount, equity %, contract value?
- Who is the audience  do you know names, roles, their track record on similar deals?
- What is the client's current pitch? (Ask to see the deck/script)
- What is the date and format? (Room layout, time allowed, Q&A?)
- What is the client's biggest fear about the pitch?

### Step 2  Materials Audit

Review the client's existing materials against the Mode C audit framework below.

### Step 3  Frame Rebuild

Most clients pitch in a submissive frame by default. They apologise for taking the audience's time, overwhelm with data to prove they have done their homework, and wait for approval. Rebuild their posture:

- Replace: "We hope you'll consider investing..."  "We're selecting partners who understand this market."
- Replace: "Sorry, I know the numbers are complex..."  "Here's what matters in these numbers."
- Replace: "I just want to quickly mention..."  "The most important thing I want you to walk away with is..."

### Step 4  Rehearsal Protocol

Minimum rehearsal schedule for a high-stakes pitch:
1. **Full run-through (silent)**  client presents to themselves; record on phone
2. **Full run-through (coached)**  you observe, take notes, do not interrupt
3. **Debrief**  specific notes on frame breaks, filler words, pacing, hookpoint timing
4. **Targeted drill**  repeat only the weak sections 3 each
5. **Q&A simulation**  ask the 10 hardest questions without warning; evaluate bridging
6. **Final full run-through**  full dress rehearsal with all materials in final form

### Step 5  Day-of Briefing

One-page brief for the client on pitch day covering:
- The three things they must convey (not more than three)
- The one frame to hold throughout
- The two questions most likely to destabilise them  and their bridge for each
- The exact ask and exact next step to propose at close

---

## Mode C: Pitch Audit

Use this checklist to evaluate an existing pitch before it is delivered.

### Frame Audit

- [ ] Does the pitcher enter the room as a prize or as a supplicant?
- [ ] Is there a clear frame established in the first 90 seconds?
- [ ] Are there beta traps in the language? ("I hope you'll..." "Sorry to take your time..." "We just wanted to...")
- [ ] Does the pitch at any point communicate neediness?
- [ ] Is the close confident and specific  or apologetic and vague?

### Message Audit

- [ ] Is there a single, memorable hook in the first 60 seconds?
- [ ] Are there exactly three key messages (not five, not eight)?
- [ ] Does the content follow Hook  Meat  Payoff structure?
- [ ] Is the ask stated clearly, once, with exact amount and specific next step?
- [ ] Is the pitch free of unnecessary qualifications, disclaimers, and tangents?

### Financial Audit (for bank and investor pitches)

- [ ] Revenue/income numbers stated  are they supported by the business plan projections?
- [ ] DSCR stated for bank pitches  does it meet 1.25 minimum?
- [ ] Valuation stated for equity pitches  is the methodology defensible? (See `references/business-valuation-methods.md`)
- [ ] Use of funds: is it specific (4-6 items), not vague ("working capital: 40%")?
- [ ] Collateral mentioned for bank pitches  with value and coverage ratio?

### Delivery Audit

- [ ] Is the presenter fully off the slides  or reading from them?
- [ ] Is the pace under control, or do nerves compress it?
- [ ] Are there filler words, upward inflections, vocal fry?
- [ ] Has the presenter practised bridging from the 5 hardest questions?
- [ ] Is the opening story less than 2 minutes?

### Deck Audit

- [ ] Does each slide carry one message  not three?
- [ ] Is the executive summary slide (if any) written bottom-line-up-front? (See `references/pyramid-principle.md`)
- [ ] Are financial charts titled with the conclusion ("Revenue grows 3 in 24 months"), not the description ("Revenue Chart")?
- [ ] Is the deck readable at arm's length? (Font  24pt for headers,  18pt body)
- [ ] Does the deck have a clear narrative flow  or is it a data dump?

---

## Generation Process

1. Identify pitch type and audience
2. **Mode A (self-prep):** Run through Phases 14 sequentially; produce the pitch script outline, Q&A prep sheet, and delivery checklist
3. **Mode B (client coaching):** Run intake  materials audit  frame rebuild  rehearsal schedule  day-of brief
4. **Mode C (audit):** Apply the four audit checklists; produce a scored audit with priority fixes
5. Cross-reference financial claims against the relevant business plan sections before any pitch

## Quality Criteria

- The pitch has a single, clearly articulated ask with an exact number
- Frame is prize-based, not submissive  check language throughout
- Hookpoint is identified and placed 10-15 minutes in (for 20-min pitches)
- Every section follows Hook-Meat-Payoff
- Q&A preparation includes the 10 hardest questions with bridge scripts
- For bank pitches: DSCR, collateral coverage ratio, and use-of-funds table are verified against plan
- For equity pitches: valuation methodology is defensible; cap table is accurate
- Delivery has been rehearsed minimum twice (ideally six runs per the protocol)

## References

- `references/pitch-anything-klaff.md`  STRONG method; frame control and frame types; neurofinance (three-part brain, hot cognition); prizing and prize frame; status dynamics; hookpoint mechanics; beta traps; the "no" close; deal momentum; full worked pitch narrative  Source: Klaff (McGraw-Hill, 2011). **Read for any pitch where frame control, investor psychology, or deal dynamics are relevant.**
- `references/pitch-perfect-mcgowan.md`  7 Principles of Persuasion; Hook-Meat-Payoff structure; brevity and clarity rules; vocal delivery (pace, pause, inflection); adrenaline management; bridging and flagging techniques; Q&A mastery; common communication mistakes with diagnosis and fixes  Source: McGowan (HarperBusiness, 2014). **Read for any pitch where delivery quality, message clarity, or high-stakes communication is the focus.**
- `11-funding-request/SKILL.md`  DSCR calculation, collateral statement, use-of-funds table, CAMPARI compliance. Cross-reference all financial claims in investor and bank pitches.
- `11-funding-request/references/business-valuation-methods.md`  DCF, multiples, pre-revenue valuation methods; Uganda CRP and illiquidity discounts. Read for any equity pitch where valuation must be defended.
- `11-funding-request/references/equity-term-sheets.md`  Term sheet mechanics, option pool shuffle, liquidation preference, cap table. Read when preparing for investor negotiation post-pitch.
- `01-executive-summary/references/pyramid-principle.md`  SCQA structure for pitch decks and written summaries. Read for deck structure and written executive summary alignment.
- `meta-bankability-scoring/SKILL.md`  CAMPARI 28-item checklist. Run this before any bank or DFI loan presentation to verify full compliance.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Pitch delivery brief decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to coaching performance around an unsupported story. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the pitch delivery brief; marking rehearsal notes in the supplied script is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If audience decision, approved story, timing, and likely objections cannot be obtained, return a qualified pitch delivery brief covering only the checks that remain supportable. Leave this decision unresolved: which hook, proof, and ask the speaker must own. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which hook, proof, and ask the speaker must own | Record the conclusion, source trail, owner, and review trigger in the pitch delivery brief. | Risk of coaching performance around an unsupported story |
| Material evidence conflicts or remains uncertain | Rehearse two openings against the actual audience and time limit, retaining the version that reaches the decision and proof fastest. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: audience decision, approved story, timing, and likely objections | Mark the decision on which hook, proof, and ask the speaker must own `not assessed` in the pitch delivery brief, and send it to the presentation owner and intended speaker. | Otherwise, the work risks coaching performance around an unsupported story |

## Quality Standards


Accept the pitch delivery brief only when evidence is sufficient for this decision: which hook, proof, and ask the speaker must own. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of coaching performance around an unsupported story.

## Worked Example


A founder spends four minutes on company history in a ten-minute lender pitch. Rehearsal moves the repayment case and funding ask forward, times the revised delivery, and records unanswered credit questions.

<!-- dual-compat-end -->
