---
name: competitive-report-structure
description: >-
  Use when benchmark-methodology has produced scored competitor profile
  cards. Assemble a sourced report with maps, tiers, a no-blended-total
  matrix, instructive deep dives, white-space, threats, and recommendations
  checked against the client's brand balance.
metadata:
  portable: true
  origin: ECC (skills/competitive-report-structure/SKILL.md), adapted for
    Uganda/East Africa business-plan engagements
  compatible_with:
    - claude-code
    - codex
---

# Competitive Report Structure

Use this skill to assemble scored competitor cards into a decision-grade
report. The report must answer three questions for the client: **who do we
compete with, how do we compete, and where is our defensible white-space?**
Every section earns its place by moving toward those answers — cut anything
that doesn't.

## Use When

- All competitor profile cards from `benchmark-methodology` are complete and
  ready to assemble.
- Presenting competitive findings to a founder, leadership team, board, or
  investor as a standalone deliverable.
- The report must drive decisions (who to compete with, how, where the moat
  is) — not just document the landscape.
- Preparing a client deliverable that must be auditable and defensible
  (sourced, dated, verification noted).

## Do Not Use When

- For incomplete cards, use `benchmark-methodology` before assembly.
- Profile cards from `benchmark-methodology` are incomplete — finish scoring
  first; partial data undermines the heatmap and white-space sections.
- The output is a plan section, not a standalone report — use
  `pipeline/06-competitive-analysis` for that and, if a pitch deck follows,
  `meta-pitch/pitch-deck` Slide 7 draws its "we win on 2-3 dimensions" claim
  from that section, not from this report's separately-reported matrix.

## Client positioning brief (establish first)

Before assembling the report, confirm the client's positioning brief. It
supplies:

- **Strategic tension** — the paired axes (e.g., innovation × bankability)
  that define the client's target white-space. All maps and synthesis
  resolve back to this tension.
- **Brand balance** — the intended proportional mix of the client's
  strategic emphases (e.g., 60% evidence/bankability, 25% distinctiveness,
  15% craft/presentation). Every recommendation must be checked against this
  balance; flag any that would shift it.
- **Differentiator** — the framing principle for the executive summary and
  white-space section.
- **Target quadrant** — where the client intends to sit in the tension map;
  confirming whether that quadrant is genuinely open is the report's central
  empirical question.

## Framing principle

The whole report is organised around the client's strategic tension, and
recommendations resolve back to the client's deliberate brand balance.
Recommendations that would break that balance must be flagged against it
explicitly — "this move shifts the balance from X/Y/Z toward A/B/C; confirm
intent."

## Report sections

### 1. Executive summary
3–5 takeaways, decision-first. State the most important findings in plain
language: where the client is strong, where it's exposed, who occupies its
target white-space, and the top 2–3 moves. Written so a founder or director
reads only this and knows what to do. No methodology here.

### 2. Market landscape & category framing
Define the category and map it. Use a **multi-axis map** — at minimum a 2×2
(e.g., *value-led ↔ premium-led* × *micro/SME ↔ enterprise-scale*), and
ideally the **client's tension plot** from `benchmark-methodology` as the
headline map. Place every profiled competitor and the client. The map should
make the client's intended position visually obvious and show how crowded
(or empty) it is.

### 3. Competitor tiers
Organise the set into **Direct / Adjacent / Aspirational** (from
`competitive-platform-analysis`). One short paragraph per tier explaining
who's in it and why it matters to the client. This sets reader expectations
before the detail.

### 4. Benchmarking matrix
The full **competitors × dimensions** table — the quantitative spine. Rows =
competitors (grouped by tier), columns = the nine benchmark dimensions
(dimension 9 — strategic tension — has two poles; represent them as two
separate sub-columns rather than averaging them). Include the client's own
honest self-assessment as a row for contrast. Use a **heatmap** (colour or
symbol scale) so strength/weakness patterns are scannable. Do **not** add a
blended total column — report dimensions separately (per the bias controls
in `benchmark-methodology`). Call out the columns where the client leads and
where it trails.

### 5. Deep dives
3–5 most instructive competitors in narrative form (from their profile
cards). Choose for instruction, not ranking: the best exemplar of the target
tension (high on both poles), the cautionary "one pole only" case, the
"competent but forgettable" archetype the client defines against, plus any
direct threat. Each deep dive: what they do, what the client should learn,
what the client should avoid.

### 6. White-space & threats
The strategic heart. Two parts:

- **White-space:** the position the client can own that rivals don't —
  argued from the maps and matrix, not asserted. Confirm whether the target
  quadrant (from the positioning brief) is genuinely open.
- **Threats:** who/what pressures the client — a rival closing the gap,
  substitutes (informal/unregistered suppliers, imports, self-supply), or
  category shifts. Be honest about the client's own risks (e.g., a
  distinctive but unconventional offer reading as unproven to a
  risk-averse lender).

### 7. Strategic recommendations
Concrete, prioritised moves: who the client competes with, how it
differentiates, and where to invest (offer packaging, evidence/references,
market presence, presentation). **Tie every recommendation back to the
brand balance from the positioning brief** and flag any that would shift it.
Sequence by impact × effort.

### 8. Sources / methodology appendix
The dimensions, weights, rubrics, the scoped set with tiers, source links or
named contacts per competitor, and verification notes (asserted vs proven).
This is what makes the report auditable and defensible — carry the
adversarial-verification discipline through, consistent with this engine's
never-fabricate-a-number rule (`rules/common/core.md`).

## How to present data

- **2×2 / positioning maps** — for landscape and the tension plot. Lead with
  these; they carry the argument faster than prose.
- **Heatmap matrix** — for the competitors × dimensions comparison
  (section 4).
- **Profile cards** — the source unit feeding deep dives (section 5).
- **Quadrant callouts** — name who sits in each quadrant explicitly,
  especially the client's target one.
- Keep tables scannable; push raw evidence and links to the appendix.

## Decision framework (the report must resolve these)

- **Who do we compete with?** — Name the Direct tier specifically; that's
  the real fight.
- **How do we compete?** — State the client's differentiator in one
  sentence, grounded in the matrix (which dimensions the client owns).
- **Where are our differentiators defensible?** — Identify the
  dimensions/quadrant rivals can't easily copy (the moat), vs. the ones that
  are table-stakes.

## Trigger questions for the team alignment session

End with questions that force decisions, not admiration of the analysis:

- Is the target quadrant truly open, or is a rival already moving in?
- Which Direct competitor is the sharpest threat in the next 12 months, and
  what's the counter?
- Does the brand balance still hold given the landscape — should any
  emphasis shift?
- Which dimension where the client trails is worth closing, and which to
  deliberately concede?
- What's the one move that most widens distinctiveness *without* costing
  bankability / credibility?

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Completed competitor profile cards and tension plot | `benchmark-methodology` output | Yes | Stop assembly and return incomplete cards for scoring or evidence repair. |
| Client positioning brief, target quadrant, differentiator, and brand balance | Client or authorised engagement lead | Yes | Qualify the executive summary and recommendations; request the missing decision frame. |
| Source and verification notes for the scoped set | Benchmark working papers and approved research evidence | Yes | Keep affected findings `NOT_ASSESSED` and retain the evidence gap in the appendix. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Decision-grade competitive report | Founder, leadership team, board, or investor | Answers who to compete with, how to compete, and where the defensible white-space lies, with sourced maps and matrix. |
| Recommendation and team-alignment register | Client decision-maker | Each move names the dimension, impact-effort order, brand-balance effect, owner, and unresolved assumption. |
| Sources and methodology appendix | Reviewer and future plan author | Carries the scoped set, weights, rubrics, source links or named contacts, dates, and asserted/proven status. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Benchmark matrix and heatmap | Competitor-by-dimension table | All competitors and the client appear with separate tension poles and no blended total. |
| White-space and threat trace | Map annotations plus cited narrative | Each conclusion points to matrix or source evidence and states uncertainty where the evidence is partial. |
| Recommendation decision trace | Prioritised action table | The recommendation resolves the three decision questions and records the countercase and brand-balance check. |

## Capability and Permission Boundaries

Read and search are required. The requested report authorises public-source verification, local drafting, source-register maintenance and visual production within scope. Preserve source provenance and distinguish inference from fact. Contacting competitors, external circulation/publication, spending and binding client commitments require engagement-owner authority; honour authority already supplied without asking again.

## Degraded Mode

If profile cards, the positioning brief, source notes, or verification evidence are unavailable, stop the affected section, mark it `NOT_ASSESSED` or qualified, and state the smallest evidence request that permits recovery. A partial report may show a provisional map or finding only when the missing coverage is visible, the client accepts the limitation, and no recommendation depends on an unsupported comparison. Do not fill a missing score or source with a template default.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| Profile cards are incomplete | Return to `benchmark-methodology` before building the heatmap or deep dives | A polished report amplifying partial scoring |
| The target quadrant is occupied or evidence is inconclusive | Name the occupant or uncertainty and frame the strategic choice; do not call the space open | An unsupported white-space claim |
| A recommendation shifts the stated brand balance | Flag the shift, test the countercase, and obtain the client's decision | Strategy drifting away from the agreed position |
| A source or score cannot be verified | Qualify the finding in the appendix and narrow the recommendation | Citation laundering or false precision |

## Workflow

1. Confirm the profile cards, client frame, source boundary, and intended decision-maker; stop assembly if a required input is missing.
2. Build the landscape map, tiers, heatmap matrix, and client comparison with separate tension poles before drafting recommendations.
3. Select deep dives for instruction, test white-space and threat claims against the matrix, and record the countercase and uncertainty.
4. Draft prioritised recommendations against impact and effort, check each against brand balance, and route any unresolved choice to the client decision-maker.
5. Complete the appendix and team-alignment questions, then run the evidence and anti-slop checks; revise or issue a qualified handoff when a gate fails.

## Quality Standards

- The executive summary is decision-first and states where the client is strong, exposed, and challenged, with a trace to the report evidence.
- The matrix includes all scored competitors and the client, preserves the two tension poles, and contains no blended total column.
- White-space, threats, deep dives, and recommendations are argued from the map and matrix, with sources and uncertainty visible.
- Every recommendation names its impact-effort position, brand-balance effect, countercase, and next decision owner.
- The appendix is sufficient for another reviewer to reproduce the set, scoring basis, sources, and verification status without relying on the author’s memory.

## References

- [Business-plan core rules](../../../rules/common/core.md)
- [Competitive platform analysis](../competitive-platform-analysis/SKILL.md)
- [Benchmark methodology](../benchmark-methodology/SKILL.md)
- [Client intake](../../pipeline/00-client-intake/SKILL.md)
- [Competitive-analysis plan section](../../pipeline/06-competitive-analysis/SKILL.md)

<!-- dual-compat-end -->

## Anti-Patterns

- Leading with methodology instead of the decision. Correction: put the strongest finding and action in the executive summary.
- Presenting scores without a tension plot. Correction: map both poles and show the client's target quadrant.
- Calling white-space open without checking the matrix and sources. Correction: name occupants, uncertainty, and the evidence gap.
- Recommending a move without checking brand balance. Correction: state the intended shift and obtain the client's decision.
- Starting assembly before profile cards are complete. Correction: return to benchmarking and retain a qualified report state.

- **Leading with methodology.** The executive summary opens with the most
  important finding, not an explanation of how the benchmark was run.
  Methodology belongs in the appendix.
- **Presenting scores without the tension plot.** The 2×2 tension map is the
  headline artefact. A table of numbers without the map buries the
  strategic insight.
- **Omitting the decision framework.** The report must resolve the three
  questions (who to compete with, how, where the moat is). Leaving these
  unanswered turns the report into a literature review.
- **Starting before all profile cards are complete.** `benchmark-methodology`
  must finish before assembly begins.
- **Adding a blended total column to the matrix.** Explicitly excluded — it
  creates a false composite that obscures the asymmetry the client needs to
  act on.

## Related Skills

- `benchmark-methodology` — the prerequisite; produces the scored competitor
  profile cards this skill assembles.
- `competitive-platform-analysis` — provides the tier structure (Direct /
  Adjacent / Aspirational) used in Section 3.
- `pipeline/06-competitive-analysis` — the business-plan-section equivalent;
  hand this report's white-space finding and differentiator statement to it
  when the same engagement also needs a plan document.
- `meta-pitch/pitch-deck` — Slide 7 ("we win against [competitors] on
  2-3 dimensions") should draw directly from Section 4 of this report when a
  pitch follows the competitive-intelligence engagement.
