---
name: pitch-deck
description: Use when the user asks for a pitch deck, investor deck, bank presentation, or live proposal deck. Use pitch-deck for end-to-end deck orchestration.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Pitch Deck Skill

## Overview

Use this skill as the orchestration layer for live presentation work. It sequences `meta-pitch-preparation` and `meta-presentation-design` so the deck, spoken frame, and Q&A preparation stay aligned.

## Use When

- Use when the user asks for a pitch deck, investor deck, bank presentation, or live proposal deck.
- Use when both deck structure and spoken delivery matter.
- Use when a completed or near-complete plan must be converted into a persuasive presentation workflow.

## Do Not Use When

- Do not use if the task is only deck design polish or only speaking rehearsal; call the more specific meta-skill directly.
- Do not use before the core business case is stable enough to present.
- Do not treat this as a substitute for fixing weak underlying strategy or numbers.


- Route to `pitch-deck` instead when the task requires end-to-end deck orchestration.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Pitch Deck brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Audience type and presentation context
- Core business-plan sections or equivalent business-case material
- Funding ask, commercial logic, and key supporting evidence
- Any time, slide-count, or format constraints

## Workflow

1. Confirm the pitch type and the decision the audience must make.
2. Run the framing and message strategy through `meta-pitch-preparation`.
3. Translate that frame into slides and delivery structure through `meta-presentation-design`.
4. Reconcile the deck with the written plan and the final ask.
5. Stress-test likely objections and Q&A gaps.
6. Flag any weakness in the underlying case that presentation work cannot solve.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the presentation-ready deck package and that the decision concerns which plan claims earn space in the deck and delivery programme.
- **Stop condition:** halt the affected conclusion if required evidence is missing (completed plan, evidence register, pitch audience, and time limit) or if the work could lead to this identified risk: losing the funding decision between slide design and speaker coaching.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The deck and spoken narrative reinforce the same core argument.
- Slide structure matches audience psychology and time constraints.
- The ask is clear, credible, and easy to repeat.
- Presentation polish does not outrun the quality of the business case.

## Anti-Patterns

- Designing slides before deciding what the audience needs to believe.
- Treating the deck as a condensed business plan.
- Hiding weak economics behind visual polish.
- Mixing investor, lender, and donor logic in the same presentation without intent.
- Treating a generic pitch deck template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to pitch deck. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pitch Deck deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A coordinated pitch-deck workflow and output path
- Clear handoffs to the two underlying meta-skills
- Open questions and presentation risks to address before pitch day


The pitch deck is the bridge between a written business plan and a live investment or lending decision. This skill runs two meta-skills in sequence:

1. **`meta-pitch-preparation`**  establishes *what to say and how to frame it* (psychology, structure, Q&A)
2. **`meta-presentation-design`**  builds *the deck and trains delivery* (slides, narrative, rehearsal)

Neither skill alone is sufficient. A psychologically sharp pitch delivered from a weak deck loses. A beautiful deck presented by someone who has not prepared the frame loses worse.

---

## When to Use This Skill

Invoke `pitch-deck` when:
- A client has a completed (or substantially complete) business plan and needs a pitch deck for investors, a bank, or a client
- You are preparing someone for a live funding presentation or sales pitch
- You have been asked to "create a pitch deck" without further specification  this skill handles the full workflow
- The business plan has a funding request section (Section 11) that must be presented live

Do NOT invoke this skill if:
- The client only wants to improve their speaking skills (use `meta-presentation-design` Mode B directly)
- The client only wants to stress-test their investor Q&A (use `meta-pitch-preparation` Mode A directly)
- The client is preparing a written proposal with no live presentation (use `proposal-architect`)

---

## Workflow: Four-Phase Execution

### Phase 1  Briefing (5 minutes)

Before any deck work, confirm three things:

~~~text
1. What is the pitch type?
   [ ] Equity investor (angel / VC / PE / impact)
   [ ] Bank / DFI loan presentation
   [ ] Client proposal presentation
   [ ] Grant committee
   [ ] Board / management
   [ ] Government / public tender

2. What is the deadline?
   [ ] Same day / urgent
   [ ] Within 1 week
   [ ] 24 weeks (full preparation possible)

3. What materials exist?
   [ ] Complete business plan (all 15 sections)
   [ ] Partial plan (specify sections available)
   [ ] Financial model only
   [ ] Rough notes / verbal brief only
~~~

The pitch type determines slide count, structure, and tone. The deadline determines how much preparation depth is realistic. The materials determine what must be synthesised vs. what can be drawn directly.

---

### Phase 2  Pitch Strategy (invoke `meta-pitch-preparation`)

**Run `meta-pitch-preparation` Mode A (self-prep) or Mode B (client coaching) before opening any slide tool.**

Key outputs required from Phase 2:
- **The One Ask**  exact amount (UGX/USD), exact terms, exact use of funds
- **The Frame**  is this pitched from prize frame or status frame? Who has the power and why?
- **The Hook**  the 60-second opening that creates urgency and curiosity
- **The STRONG skeleton**  the six narrative stages mapped to this specific pitch type
- **The 10 hardest Q&A**  written out with bridge scripts
- **Financial claims verified**  DSCR, collateral coverage, valuation, revenue projections cross-checked against the plan

Do not move to Phase 3 until the pitch strategy is clear. A deck built on an unclear frame will be redesigned after Phase 3  double the work.

---

### Phase 3  Deck Construction (invoke `meta-presentation-design`)

**Run `meta-presentation-design` Mode A (deck design) using the Phase 2 outputs as input.**

#### Master Slide Template (13 slides  equity/bank default)

| Slide | Assertion Headline Format | Source in Plan |
|---|---|---|
| 1  Title | `[Business Name]  [One-line value proposition]` | 01 Executive Summary |
| 2  The Problem | `[X% of target customers] face [specific pain] with no adequate solution` | 04 Market Analysis / 05 Target Market |
| 3  The Solution | `[Business Name] solves this by [mechanism]  delivering [measurable outcome]` | 03 Products & Services |
| 4  Market Size | `The [addressable market] is [UGX/USD X] and growing at [X%] per year` | 04 Market Analysis |
| 5  Business Model | `We earn [UGX X] per [unit/customer] through [revenue mechanism]` | 03 / 07 Marketing |
| 6  Traction | `In [period], we achieved [metric]: [customers / revenue / units / pilots]` | 02 Company Overview |
| 7  Competition | `We win against [competitors] on [23 specific dimensions]` | 06 Competitive Analysis |
| 8  Go-to-Market | `We reach [target customer] through [channel] at [CAC]  [conversion rate] close rate` | 07 Marketing & Sales |
| 9  Team | `[Name] brings [X years] of [relevant experience]  this team has done this before` | 09 Management Team |
| 10  Financials | `Revenue reaches [UGX X] by Year 3; EBITDA margin [X%]; break-even Month [X]` | 10 Financial Projections |
| 11  The Ask | `We are raising [UGX X] as a [loan / equity / grant] to [specific use]` | 11 Funding Request |
| 12  Use of Funds | `[Visual: 45 line items with % breakdown matching 11 exactly]` | 11 Funding Request |
| 13  The Close | `[Investor/lender name] + [Business Name] = [specific shared outcome]. Here is the next step.` | 01 Executive Summary |

**Slide count adjustments by pitch type:**
- Equity investor: 1012 slides (drop Slide 12; integrate use of funds into Slide 11)
- Bank / DFI: 1315 slides (add DSCR slide; add collateral slide)
- Grant committee: 1214 slides (replace Traction with Theory of Change; add beneficiary slide)
- Client proposal: 1520 slides (expand Solution and Go-to-Market; add delivery timeline)

#### Slide Design Rules (non-negotiable)

1. **Assertion headlines**  every slide title is a complete sentence stating a conclusion, not a label ("Revenue"  "Revenue grows 3 in 24 months")
2. **One message per slide**  if there are two messages, there are two slides
3. **No bullet forests**  maximum 3 bullets; prefer visuals, charts, or single statements
4. **Chart titles are conclusions**  "Monthly Revenue (UGX)"  "Revenue crosses break-even in Month 14"
5. **The 3-second test**  the key message of every slide must be readable in 3 seconds without reading the body
6. **Financial consistency**  every number on every slide must match the business plan exactly (see `meta-due-diligence` Mode C)

---

### Phase 4  Delivery Preparation (invoke `meta-presentation-design` Mode B)

**Run delivery coaching after the deck is complete, not before.**

Minimum preparation standard before any live pitch:

| Run | Format | Purpose |
|---|---|---|
| Run 1 | Read aloud, alone, with deck | Hear the words for the first time |
| Run 2 | Present standing, deck on screen | Full physical simulation |
| Run 3 | Full run with coach/colleague | External feedback on pacing, frame, confidence |
| Run 4 | Q&A simulation only | Drill the 10 hardest questions with bridges |
| Run 5 | Full dress rehearsal | Timed, complete, no stops |
| Run 6 (day of) | Opening + Close + Q&A warm-up | Activate the material; remove nerves |

**Critical delivery checkpoints:**
- Can the presenter state the ask (amount, terms, next step) without looking at the slides? If not, more rehearsal.
- Does the opening create a question in the audience's mind within 30 seconds? If not, rewrite the hook.
- Does the close make the next step feel inevitable  not a request, but a logical conclusion? If not, rewrite the close.

---

## Pitch Deck by Audience  Quick-Reference

### Equity Investor Deck

**Frame:** Prize frame  you are selective about investors, not desperate for capital. The investor earns the right to participate.

**Opening hook:** A striking statistic about the problem, a customer story, or a counterintuitive claim that makes the investor lean forward.

**The ask slide must include:** Amount  pre-money valuation  % equity offered  use of funds (3 lines)  runway achieved  key milestone unlocked.

**Hardest Q&A to prepare:** "Why you?" / "Why now?" / "What's your exit?" / "What happens if revenue is 50% below plan?" / "Who else is in the round?"

### Bank / DFI Loan Deck

**Frame:** Evidence frame  you are the safe, qualified choice. Every claim is verifiable. Every risk is identified and mitigated.

**Opening hook:** The business in one sentence, followed immediately by DSCR and collateral coverage. Credit officers form their view in the first 60 seconds.

**The ask slide must include:** Loan amount  loan type  proposed term  grace period  repayment source  DSCR (Year 1, 2, 3)  collateral value + coverage ratio.

**Hardest Q&A to prepare:** "What if sales are 30% lower?" / "What is your fallback repayment source?" / "Who guarantees if the business fails?" / "Why this loan amount and not less?" / "What experience do you have in this sector?"

### Grant / Donor Deck

**Frame:** Impact frame  you are the most credible implementer of their programme objectives. Every slide answers "will this advance our mission?"

**Opening hook:** A human story (beneficiary profile) that makes the problem concrete and personal.

**The ask slide must include:** Grant amount  project period  beneficiary count  Theory of Change (one sentence)  M&E framework (one line)  reporting obligations accepted.

**Hardest Q&A to prepare:** "How will you measure impact?" / "What happens after the grant period?" / "Why not use an established NGO?" / "Have you implemented a similar programme before?"

---

## Consistency Check Before Submission

Before the pitch deck is declared final, verify:

- [ ] Every financial figure on slides matches the business plan exactly
- [ ] The ask on Slide 11 matches 11 of the plan exactly (amount, terms, use of funds)
- [ ] Revenue projections on Slide 10 match 10 exactly (Year 1, 2, 3)
- [ ] Market size on Slide 4 matches 04 exactly (TAM/SAM/SOM)
- [ ] Team bios on Slide 9 are consistent with 09
- [ ] Risk acknowledgement is present (investors distrust plans with no risks)
- [ ] Slide count is appropriate for pitch type (see table above)
- [ ] All slides pass the 3-second test
- [ ] Delivery has been rehearsed minimum 5 times

Run `meta-bankability-scoring` (Bank Loan Readiness Mode) before any bank or DFI pitch to verify the deck does not contradict CAMPARI criteria.

---

## Generation Process

1. **Confirm pitch type, deadline, and available materials** (Phase 1  5 minutes)
2. **Run `meta-pitch-preparation`** to establish frame, hook, STRONG narrative, and Q&A prep (Phase 2)
3. **Build deck using the master template** adjusted for pitch type; apply slide design rules throughout (Phase 3)
4. **Run `meta-presentation-design` Mode B** delivery coaching; execute minimum 5-run rehearsal protocol (Phase 4)
5. **Apply consistency check** before declaring the pitch deck final

## References

- **Pitch strategy and frame control**: See `meta-pitch-preparation/SKILL.md` for STRONG method, Klaff frame control, McGowan Hook-Meat-Payoff, Q&A preparation, and the six-run rehearsal protocol
- **Deck design and delivery**: See `meta-presentation-design/SKILL.md` for the full 13-slide master template, assertion-evidence standard, Duarte Sparkline, visual design rules, and the four-dimension deck audit checklist
- **Financial verification**: See `11-funding-request/SKILL.md` for DSCR calculation, collateral coverage, and use-of-funds table that must be reflected exactly on the pitch slides
- **Consistency audit**: See `meta-bankability-scoring/references/consistency-audit.md` to verify pitch figures against the business plan before any live presentation
- **DD readiness**: See `meta-due-diligence/SKILL.md` Mode C for pre-pitch data room audit  if an investor asks for due diligence materials, the data room must be ready before the pitch, not after
- **Pyramid structure for the narrative**: See `01-executive-summary/references/pyramid-principle.md` for the SCQA framework that governs the overall pitch storyline

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Presentation-ready deck package decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to losing the funding decision between slide design and speaker coaching. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the presentation-ready deck package; assembling the authorised deck and rehearsal pack is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If completed plan, evidence register, pitch audience, and time limit cannot be obtained, return a qualified presentation-ready deck package covering only the checks that remain supportable. Leave this decision unresolved: which plan claims earn space in the deck and delivery programme. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which plan claims earn space in the deck and delivery programme | Record the conclusion, source trail, owner, and review trigger in the presentation-ready deck package. | Risk of losing the funding decision between slide design and speaker coaching |
| Material evidence conflicts or remains uncertain | Build a short and full narrative sequence from the same approved claims, then choose the version that fits the meeting time without dropping the ask. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: completed plan, evidence register, pitch audience, and time limit | Mark the decision on which plan claims earn space in the deck and delivery programme `not assessed` in the presentation-ready deck package, and send it to the presentation owner and intended speaker. | Otherwise, the work risks losing the funding decision between slide design and speaker coaching |

## Quality Standards


Accept the presentation-ready deck package only when evidence is sufficient for this decision: which plan claims earn space in the deck and delivery programme. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of losing the funding decision between slide design and speaker coaching.

## Worked Example


A 40-page plan must become a 12-minute DFI presentation. Keep the development outcome, operating proof, financing need, and repayment logic in the core deck; move diligence schedules to the appendix and rehearse the handoff.

<!-- dual-compat-end -->
