---
name: benchmark-methodology
description: >-
  Use when competitive-platform-analysis has produced a tiered competitor
  set. Score nine dimensions and both strategic-tension poles with explicit
  1-5 rubrics and source trails before competitive-report-structure. Preserve
  a separate, no-blended-total matrix by design.
metadata:
  portable: true
  origin: ECC (skills/benchmark-methodology/SKILL.md), adapted for
    Uganda/East Africa business-plan engagements
  compatible_with:
    - claude-code
    - codex
---

# Benchmark Methodology

Use this skill to turn a scoped competitor set into **comparable, defensible
scores**. Each competitor is assessed on the same nine dimensions, with
explicit 1–5 rubrics, then captured in a uniform profile card. Consistency is
the point: scores are only useful if the same evidence would earn the same
number for any competitor.

## Use When

- A scoped, tiered competitor set from `competitive-platform-analysis` is
  ready to score.
- Comparable, evidence-anchored scores are needed across competitors — not
  gut-feel rankings.
- The client's strategic tension (the paired axes defining their target
  white-space) has already been established.
- Preparing to produce profile cards for assembly in
  `competitive-report-structure`.

## Do Not Use When

- For an unscoped set, use `competitive-platform-analysis` instead.
- No tiered competitor set exists yet — run `competitive-platform-analysis`
  first.
- No positioning brief / strategic tension has been established — this
  skill's dimension 9 depends on it; do not substitute a generic tension.

## Client positioning brief (establish first)

Before scoring, confirm the client's positioning brief. It supplies:

- **Strategic tension** — the two axes (e.g., innovation × bankability,
  premium × accessibility) whose intersection marks the client's target
  white-space. Dimension 9 is always the client's named tension; report both
  poles separately, never averaged.
- **Differentiator** — what makes the client's moat. This informs which
  dimensions matter most for the client's positioning argument.
- **Brand balance** — the intended mix of distinct strategic emphases (e.g.
  60% evidence/bankability, 25% distinctiveness, 15% craft/presentation).
  Strategic recommendations must not break this balance without flagging it.

## Why these dimensions

The client competes on a **specific tension held across two poles**, not on
offer breadth alone. The dimensions are weighted to reflect that moat. Two
dimensions — the tension poles — are scored **separately and never averaged
together**, because the client's strategic question is precisely whether a
rival achieves both simultaneously.

## The nine dimensions (with weights)

Weights guide synthesis emphasis, not a single blended score (avoid a false
composite — see Bias controls). Sum = 100%.

1. **Positioning clarity & distinctiveness** (18%) — Is the business's
   position sharp, ownable, and instantly legible? Or generic?
2. **Brand voice / customer-facing communication** (15%) — Does the
   messaging (site, signage, sales pitch) have an ownable register, or is it
   interchangeable boilerplate?
3. **Visual/operational presentation & craft** (15%) — Quality and ownership
   of the visual and physical presentation (branding, premises, packaging,
   site); presentation as proof-of-craft.
4. **Offer & packaging** (12%) — Products/services are clearly defined and
   legible (named packages, tiers, SKUs) vs. vague. Packaging maturity.
5. **Evidence & credibility** (12%) — Named clients, quantified outcomes,
   certifications, case depth. Proof beyond assertion.
6. **Enterprise/institutional-readiness / commercial maturity** (10%) —
   Signals they can land and hold larger institutional, corporate, or
   export-grade contracts (process, compliance marks, references, scale).
7. **Thought leadership / market presence** (8%) — Owned point of view:
   media presence, association leadership, trade-fair participation,
   published expertise. Depth over volume.
8. **Pricing transparency & engagement model** (5%) — Is pricing/engagement
   legible? Published vs. negotiated vs. opaque.
9. **[Client's strategic tension]** (5% as a flag; **score BOTH poles,
   report separately**) — Read the tension name and axis descriptions from
   the client's positioning brief. Plot both; the gap is the insight. The
   client's target quadrant is the single most important finding: who else
   is already there?

## Scoring rubric (1–5, applies to dimensions 1–8)

Anchor every score to observable evidence. Generic descriptors below; adapt
the specifics per dimension but keep the level meaning constant.

- **1 — Absent / generic.** No discernible position or craft;
  indistinguishable from any informal competitor. Active liability.
- **2 — Below par.** Some intent but inconsistent, derivative, or
  unconvincing. Wouldn't survive a side-by-side.
- **3 — Competent / table-stakes.** Solid, professional, unremarkable.
  Meets expectation, ownable by nobody.
- **4 — Strong / distinctive.** Clearly above peers; a real strength a
  customer or funder would notice and cite.
- **5 — Category-defining.** Best-in-class, ownable, hard to imitate. Sets
  the bar others react to.

### Tension axes (dimension 9) — score each 1–5

Read the axis labels and their 1/3/5 anchors from the client's positioning
brief. Example anchors for an innovation × bankability tension:

- **Innovation** — 1: copies existing offers with no differentiation ·
  3: incremental improvement on the standard offer · 5: a genuinely new
  approach the market has not seen locally.
- **Bankability** — 1: no verifiable financial or operational evidence ·
  3: plausible, some evidence, unproven at scale · 5: audited/verifiable
  track record a lender or investor would accept without discount.

Plot competitors on the tension 2×2. The client's target quadrant is named
in the positioning brief. Who else occupies that quadrant is the single most
important finding of the benchmark.

## How to collect the data

For each competitor, work the dimensions in this order (cheapest signal
first):

1. **Competitor's own site / social / signage** — positioning, offer
   packaging, pricing posture, named clients.
2. **Case studies / references / visible work** — evidence depth, quantified
   outcomes, client names. Distinguish *asserted* ("we supply X clients")
   from *proven* (verifiable, named, corroborated).
3. **Reviews, directories, trade/sector associations** — corroborate
   clients, scale, engagement model → credibility & institutional readiness.
4. **Site visit / market survey** — physical presentation, stock, footfall,
   staffing → craft/presentation and offer.
5. **Supplier/distributor conversations** — the strongest signal for scale
   and market share in low-data EA markets
   (`meta-due-diligence/references/osint-business-intelligence.md`).
6. **Media / trade-fair / association presence** — thought-leadership depth.

**What to record per dimension:** the score, one-line justification, and the
source (link, document, or named contact) that earned it. No score without
evidence — this is the same discipline as the engine's
never-fabricate-a-number rule (`rules/common/core.md`), applied to scores
rather than financial figures: an unsupported score is as misleading as an
unsupported number.

## Bias controls

- **No single composite score.** Report dimension scores and the tension
  plot separately. A weighted average hides the asymmetry that matters. This
  is the deliberate correction to the blended "Total" row that appears in
  generic competitive matrices (including simpler comparison tables) — do
  not add one here.
- **Asserted vs proven.** Downgrade credibility/evidence scores for
  self-reported claims with no corroboration. A claim on a competitor's own
  site or WhatsApp status is marketing, not fact.
- **Aesthetic/register affinity bias.** Reviewers may over-score competitors
  whose presentation style they personally prefer and under-score rivals'
  commercial strength. Score craft and credibility independently; a plain,
  unglamorous operator may be winning the bigger contracts.
- **Recency / flashiness bias.** A newly renovated shopfront or a recent
  award dazzles but may lack commercial depth — verify with directories,
  references, or supplier conversations before scoring credibility.
- **Survivorship.** The visible, well-marketed competitors aren't the whole
  market; note strong-but-quiet operators found via directories, referrals,
  or supplier conversations.
- **Calibrate across the set, not in isolation.** Before finalising, re-read
  scores side-by-side — a "4" must mean the same thing for every competitor.
  Adjust outliers.

## Competitor profile card (output format)

Produce one card per profiled competitor — the atomic unit the report
assembles from:

```text
## <Competitor name>
- **Profile / Tier:** <positioning stance · specialisation · size band> / <Direct | Adjacent | Aspirational>
- **One-liner:** <how they position themselves, in their words>
- **Model / size / geography:** <micro|SME|mid-size> · <region> · <pricing/engagement model>
- **Notable clients / evidence:** <named, with proven/asserted tag>

### Dimension scores
| Dimension | Score (1-5) | Justification (1 line) | Source |
|---|---|---|---|
| Positioning clarity & distinctiveness | | | |
| Brand voice / customer-facing communication | | | |
| Visual/operational presentation & craft | | | |
| Offer & packaging | | | |
| Evidence & credibility | | | |
| Enterprise/institutional-readiness | | | |
| Thought leadership / market presence | | | |
| Pricing transparency & engagement model | | | |

### Tension plot
- **[Axis 1 from positioning brief]:** <1-5> - <why>
- **[Axis 2 from positioning brief]:** <1-5> - <why>
- **Quadrant:** <high/high | high-1/low-2 | low-1/high-2 | low/low>

### Read for [client]
- **Strength to learn from:** <...>
- **Weakness to exploit / white-space it exposes:** <...>
- **Threat to [client]:** <...>
```

Hand the completed cards plus the tension plot to
`competitive-report-structure`.

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Tiered competitor set and inclusion rationale | `competitive-platform-analysis` output | Yes | Stop scoring; return the unscoped or disputed candidates for resolution. |
| Client positioning brief with named strategic tension and brand balance | Client or authorised engagement lead | Yes | Mark dimension 9 and any affected recommendation `NOT_ASSESSED`; request the missing brief. |
| Evidence register for competitor attributes and scores | Research notes, links, documents, or named contacts | Yes | Qualify the score and retain the evidence gap; never fill it with a plausible number. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Competitor profile cards and dimension score matrix | Competitive-report-structure author | Every scored dimension has a 1-5 value, one-line rationale, source, and asserted/proven status. |
| Tension plot and scoring exceptions | Client decision-maker and report assembler | Both poles are plotted separately and every exception or missing signal is visible. |
| Benchmark handoff note | `competitive-report-structure` | Names the completed cards, unresolved evidence, and the decision implication for the client. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Dimension score trail | Matrix row with rationale and source | A reviewer can reproduce why the same evidence earned that score. |
| Tension-axis evidence | Plot annotation and source note | Each pole has its own anchor, score, uncertainty, and target-quadrant implication. |
| Calibration and bias log | Short review note | Outliers, self-reported claims, recency effects, and survivorship gaps are recorded before handoff. |

## Capability and Permission Boundaries

Read and search are required. The requested benchmark authorises public-source research, analysis and local working artefacts within scope. Preserve original evidence and distinguish self-report from corroboration. Contacting competitors, conducting interviews or site visits, purchasing data, changing external client records and publishing require engagement-owner authority; honour authority already supplied without asking again.

## Degraded Mode

If the tiered set, positioning brief, source, or scoring evidence is unavailable, mark the affected dimension `NOT_ASSESSED`, qualify the card, and state the smallest evidence request that permits recovery. If only one source is available, retain the claim as asserted and narrow the score; do not convert a missing corroboration into a proven attribute. A report may proceed with a clearly labelled partial set only when the client decision-maker accepts the limitation.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| A competitor has no tier rationale or source trail | Return it to scoping and stop its score from entering the matrix | False precision from an unbounded competitor set |
| Evidence is self-reported or single-source | Tag it asserted, seek corroboration, and qualify the score until checked | Marketing claims being presented as verified capability |
| The two tension poles point in different directions | Report both poles and the gap separately; never average them | Hiding the strategic trade-off in a blended total |
| A weighted result would obscure material asymmetry | Keep the dimensions and plot separate and explain the decision implication | A composite ranking substituting for judgement |

## Workflow

1. Confirm the tiered set, positioning brief, strategic tension, and evidence boundary; stop if a required input is missing.
2. Gather the cheapest observable signals first, then corroborate material attributes using the source hierarchy already defined in this skill.
3. Score dimensions 1-8 against the 1-5 anchors and score both tension poles separately, recording the rationale and source on each row.
4. Re-read the full matrix side by side, test bias controls and the countercase, and correct outliers before finalising the cards.
5. Package the cards, plot, evidence gaps, and decision implication for `competitive-report-structure`; if evidence remains incomplete, hand off a qualified result with the recovery request.

## Quality Standards

- No score is released without a one-line evidence rationale and a source or named contact; unsupported values remain `NOT_ASSESSED` or explicitly qualified.
- Dimension weights guide attention but never produce a blended total, and dimension 9 always preserves both tension poles.
- The matrix distinguishes asserted, corroborated, and proven claims and records the limitation of each source type.
- Calibration is performed across the competitor set, with recency, aesthetic affinity, and survivorship checks visible in the bias log.
- The handoff identifies the target quadrant, the strongest countercase, unresolved evidence, and the next decision the client must make.

## References

- [Business-plan core rules](../../../rules/common/core.md)
- [Competitive platform analysis](../competitive-platform-analysis/SKILL.md)
- [Competitive report structure](../competitive-report-structure/SKILL.md)
- [OSINT business-intelligence reference](../meta-due-diligence/references/osint-business-intelligence.md)

<!-- dual-compat-end -->

## Anti-Patterns

- Unsupported score presented as measured performance. Correction: retain `NOT_ASSESSED` and request the evidence that would earn a score.
- A single composite total used to rank competitors. Correction: show each dimension and both tension poles separately.
- A self-reported client list treated as corroborated evidence. Correction: label it asserted and seek an independent source.
- A generic tension substituted for the client's named strategic question. Correction: stop dimension 9 until the positioning brief is confirmed.
- A newly renovated or highly visible competitor over-scored without commercial proof. Correction: test recency and survivorship bias against references or operational evidence.

- **Averaging the tension axes.** The two poles of the client's strategic
  tension must be scored and reported separately. Averaging destroys the
  insight — the gap between poles is the finding.
- **Scoring without evidence.** Every score requires a one-line
  justification and a source. A score without evidence is an opinion, not a
  benchmark.
- **Creating a single composite score / blended total.** Report dimension
  scores individually. A weighted average or a "Total" column hides the
  asymmetric strengths that matter for positioning.
- **Applying generic rubric anchors without adapting.** The 1–5 anchors must
  be calibrated to the specific dimension, sector, and competitor set.
- **Running before the competitor set is scoped.** Use
  `competitive-platform-analysis` first to produce a tiered, pruned set.

## Related Skills

- `competitive-platform-analysis` — the prerequisite; produces the tiered
  competitor set this skill scores.
- `competitive-report-structure` — the next step; assembles the scored
  profile cards into a client-deliverable report.
- `pipeline/06-competitive-analysis` — the business-plan-section equivalent;
  its comparison matrix includes a blended "Total" row, which is acceptable
  there because it is a single-page plan exhibit, not a decision-grade
  benchmarking deliverable. Do not import that Total row into this skill's
  output.
