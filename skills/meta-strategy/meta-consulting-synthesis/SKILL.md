---
name: meta-consulting-synthesis
description: Use when use after the analytical sections exist but before final assembly or presentation. Use the relevant plan-section skill for section drafting.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Consulting Synthesis Meta-Skill

## Use When

- Use after the analytical sections exist but before final assembly or presentation.
- Use when a plan feels sectionally strong but not yet thesis-driven.
- Use when the work needs McKinsey-style governing logic, issue trees, and decision framing.
- Use after `meta-critical-thinking-business-logic` has exposed assumptions, countercases, achievability gaps, and cross-section contradictions.

## Do Not Use When

- Do not use before the core sections contain enough substance to synthesise.
- Do not use as a substitute for fixing factual weaknesses in the underlying analysis.
- Do not use to polish prose before the governing argument is clear.


- For `meta-consulting-synthesis`, route to the relevant plan-section skill instead when the request is section drafting rather than cross-section analysis.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Consulting Synthesis brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Draft or final core plan sections
- Target audience and decision type
- Key numbers, risks, and ask
- Any known contradictions, objections, or weak evidence areas
- Findings from `meta-critical-thinking-business-logic` where available

## Workflow

1. Define the decision the document must help the reader make.
2. Write the top-line governing thesis.
3. Break the case into MECE branches and hypotheses.
4. Check that claim, evidence, warrant, assumption, countercase, and implication are explicit for the load-bearing branches.
5. Rebuild the storyline around evidence, implications, and remaining proof burdens.
6. Surface contradictions and gaps across sections.
7. Produce the rewrite priorities and audience-specific close.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the decision-grade investment storyline and that the decision concerns the governing thesis and evidence sequence.
- **Stop condition:** halt the affected conclusion if required evidence is missing (completed sections, governing question, and contradiction list) or if the work could lead to this identified risk: creating a polished narrative that leaves cross-section contradictions intact.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The document reads as one investment or decision case, not stitched sections.
- The top-line thesis is explicit and supportable.
- Headings and opening lines make conclusions clear.
- Contradictions are exposed and resolved rather than buried.
- The final storyline is achievable under the plan's market, operating, financial, funding, and risk constraints.

## Anti-Patterns

- Treating synthesis as copy-editing.
- Listing topics instead of building a key line of reasons.
- Carrying multiple competing theses through the same document.
- Hiding the hardest objections instead of addressing them.
- Synthesising around an attractive thesis before the business logic has survived the achievability gate.


- Applying the wrong neighbouring route to meta consulting synthesis. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Consulting Synthesis deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Governing thesis
- Key line or investment case
- Issue tree and contradiction list
- Rewrite priorities
- Audience-specific closing recommendation


Use this skill after the analytical sections are drafted and before final assembly, presentation design, or final executive-summary polishing.

## Objective

Turn a collection of good sections into one coherent decision document that reads like a top-tier advisory product rather than a stitched draft.

## What to Produce

1. A single governing thesis
2. A 3-5 point investment case
3. A MECE issue tree for the decision
4. A section-by-section storyline that reconciles all major claims
5. A contradiction list and rewrite priorities
6. A decision-ready closing recommendation by audience

## Core Method

### 1. Start with the answer

Write the top-line conclusion first:

`[Business] is a [bankable / investable / partnerable] opportunity because [reason 1], [reason 2], and [reason 3], provided [critical condition] is managed.`

If that sentence is weak, the plan is not ready. Fix the thinking before polishing prose.

### 2. Build the issue tree

Break the decision into mutually exclusive, collectively exhaustive branches:

- Market attractiveness
- Business model and economics
- Execution capability
- Financing and return profile
- Risk and mitigations

Use yes/no or pass/fail questions under each branch. Each branch must lead to a conclusion, not a topic summary.

### 3. Apply hypothesis-driven review

For each branch, state:

- Working hypothesis
- Evidence that supports it
- Evidence that weakens it
- What must still be proven

Do not leave unresolved claims hidden in narrative paragraphs.

### 4. Force a storyline

Use this progression:

1. Why this opportunity matters now
2. Why existing alternatives leave a gap
3. Why this business can win
4. Why the economics are credible
5. Why the risks are manageable
6. Why the ask is justified now

If any section does not move that sequence forward, cut it or move it to appendices.

### 5. Rewrite for assertion-evidence logic

Every major paragraph or slide should follow:

- Assertion: the conclusion sentence
- Evidence: the proof
- Implication: why it matters for the decision

Do not use topic headings that merely label content. Prefer conclusion headings.

### 6. Tailor to the decision-maker

Adjust the final framing by audience:

- Bank: repayment capacity, collateral, downside resilience, covenant safety
- Equity investor: scale path, valuation, return logic, exit path
- DFI: development impact plus viability, governance, safeguards, execution readiness
- Strategic partner: market access, capability fit, ROI, delivery reliability

## Required Checks

Before finalising, confirm:

- The executive summary states the same governing thesis as the full plan
- Section 04 market claims support Section 10 revenue assumptions
- Section 08 operating model supports staffing, capex, and timing assumptions
- Section 11 ask and use of funds match Section 13 implementation priorities
- Section 12 risks match the actual vulnerabilities in the model
- Section 15 contains evidence for every high-stakes claim

## Rewrite Output Format

Produce these artifacts in order:

### A. Governing Thesis

One sentence only.

### B. Key Line

Three to five bullets only. Each bullet must be a stand-alone reason to proceed.

### C. Contradictions and Gaps

List the top issues blocking a decision-grade draft.

### D. Recommended Rewrite Order

Use this sequence:

1. Executive summary
2. Market and competition
3. Business model and economics
4. Financials and funding ask
5. Risks and appendices

### E. Audience-Specific Close

Write the exact closing recommendation for the target reader.

## Quality Criteria

- One thesis, not several competing claims
- Key messages are MECE and ordered by importance
- Evidence is stronger than adjectives
- The document answers the reader's decision, not the writer's need to explain
- Headings and first sentences are conclusion-led
- Open issues are surfaced, not buried

## References

- `references/consulting-synthesis-framework.md` - issue trees, hypothesis-driven problem solving, key-line logic, storyline construction, and assertion-evidence rewriting distilled from *McKinsey Mind*, *The McKinsey Edge*, and *Strategic Storytelling*
- `../meta-critical-thinking-business-logic/references/reasoning-achievability-gate.md` - serious-analysis, mental-model, business-sense, and achievability checks that should precede synthesis
- `../01-executive-summary/references/pyramid-principle.md` - SCQA and top-down structure
- `../meta-presentation-design/references/data-storytelling.md` - visual and narrative rules for turning analytical output into decision-ready exhibits

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Decision-grade investment storyline decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to creating a polished narrative that leaves cross-section contradictions intact. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the decision-grade investment storyline; restructuring the supplied narrative without changing source facts is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If completed sections, governing question, and contradiction list cannot be obtained, return a qualified decision-grade investment storyline covering only the checks that remain supportable. Leave this decision unresolved: the governing thesis and evidence sequence. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: the governing thesis and evidence sequence | Record the conclusion, source trail, owner, and review trigger in the decision-grade investment storyline. | Risk of creating a polished narrative that leaves cross-section contradictions intact |
| Material evidence conflicts or remains uncertain | Draft competing theses against the same evidence and retain the one that explains the countercase and cross-section economics with fewer exceptions. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: completed sections, governing question, and contradiction list | Mark the decision on the governing thesis and evidence sequence `not assessed` in the decision-grade investment storyline, and send it to the plan owner and executive sponsor. | Otherwise, the work risks creating a polished narrative that leaves cross-section contradictions intact |

## Quality Standards


Accept the decision-grade investment storyline only when evidence is sufficient for this decision: the governing thesis and evidence sequence. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of creating a polished narrative that leaves cross-section contradictions intact.

## Worked Example


Market demand appears attractive, but capacity and working capital cap first-year sales. Build the thesis around the staged, financeable entry rather than repeating the market-size claim.

<!-- dual-compat-end -->
