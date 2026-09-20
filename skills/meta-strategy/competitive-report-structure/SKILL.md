---
name: competitive-report-structure
description: >-
  Use after benchmark-methodology has produced scored competitor profile
  cards. Assembles findings into a decision-grade report: landscape map,
  competitor tiers, benchmarking matrix (heatmap, no blended total),
  deep dives chosen for instruction not ranking, white-space analysis,
  strategic recommendations checked against the client's brand balance, and
  team-alignment trigger questions. Final step in the three-skill
  competitive-intelligence pipeline.
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

## Anti-Patterns

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
