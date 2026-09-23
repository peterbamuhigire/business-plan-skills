---
name: competitive-platform-analysis
description: Use when scoping a sourced, tiered competitor set for a standalone competitive-intelligence report before benchmark-methodology.
metadata:
  portable: true
  origin: ECC (skills/competitive-platform-analysis/SKILL.md), adapted for
    Uganda/East Africa business-plan engagements
  compatible_with:
    - claude-code
    - codex
---

# Competitive Platform Analysis

Use this skill to decide **who to benchmark** and **where to find them** before
any scoring begins. A competitive analysis is only as good as its frame: the
wrong set makes the client look either unbeatable or doomed. The goal is a
defensible, decision-relevant set — not an exhaustive census.

## Use When

- Starting a competitive-intelligence engagement that needs a defensible,
  pruned competitor set before benchmarking.
- Unsure which companies belong in the Direct / Adjacent / Aspirational tiers.
- A client positioning brief exists (or can be quickly elicited) and the task
  is to identify who genuinely contests that position.
- First step before running `benchmark-methodology`.

## Do Not Use When

- The competitor discussion is a subsection of a business-plan document, not
  a standalone competitive-intelligence deliverable — use
  `pipeline/06-competitive-analysis` instead (it produces Section 06 of the
  plan directly, with its own Porter's Five Forces, moat, and market-share
  treatment).
- The competitor set is already tiered and sourced — go straight to
  `benchmark-methodology`.

## Client positioning brief (establish first — do not skip)

Before scoping the set, establish the client's positioning brief. If it does
not already exist, run a short discovery pass to elicit it — do **not**
invent one and do **not** scope the set blind. The brief supplies:

- **Identity / register** — what kind of company this is and how it presents
  itself to the market.
- **Offer** — what products or services it delivers.
- **Target clients** — who it sells to.
- **Differentiator** — the moat or positioning argument the client believes
  in.
- **Scoping consequence** — the implication for how to weight competitors
  (e.g., prioritise by distinctiveness vs. capability overlap vs. price).
- **Strategic tension** — the paired axes that define the client's
  white-space (e.g., innovation × bankability, premium × accessibility).

**Do not proceed without the positioning brief.** A competitor list scoped
without the client's lens is noise, not intelligence. The scoping consequence
in particular determines which competitors are genuine rivals (those that
contest the client's moat) versus merely overlapping on offer.

This gate is a process addition on top of this engine's existing
`ask-for-business-name-industry-country-context-first` rule
(`rules/common/core.md`) — that rule establishes the *engagement* context
(who, what sector, what country); the positioning brief establishes the
*competitive* frame (what tension the client is trying to win) and must be
established before scoping, not merely before drafting.

## Selection criteria

For each candidate, capture these axes — they decide both inclusion and tier:

- **Size / model** — micro-enterprise, SME, mid-size, large/multinational.
  Match the client's own band; same-band players are the realistic
  head-to-head set.
- **Niche / specialisation** — how closely the candidate's focus overlaps
  with the client's offer. Tighter overlap = more direct.
- **Geography / market** — district/city, national, regional (East Africa),
  or international; note whether they win the same customers the client
  targets.
- **Pricing & engagement model** — transparent published pricing vs.
  quote-on-request; retail vs. wholesale vs. B2B contract. Signals
  positioning maturity.
- **Offer presentation** — generic vs. differentiated/branded vs. informal
  and unbranded. Closer to the client's register = more it contests the
  client's distinctiveness.
- **Operational/technical depth** — relevant if the client's credibility
  story includes certifications, process quality, or documented systems
  (e.g. UNBS marks, ISO, NEMA compliance).
- **Brand strength** — does the competitor have an ownable identity, or is it
  interchangeable/informal? Weight this per the client's scoping
  consequence.

## Player taxonomy — axes to populate across

Don't sort competitors into sector-specific buckets only; sort them along a
few generic axes so the landscape isn't skewed toward one archetype. These
axes apply to any sector this engine covers (agriculture, ICT, hospitality,
manufacturing, services, etc.):

1. **Positioning stance** — *brand-led* (competes on identity, trust, story)
   vs *capability-led* (competes on scale, throughput, price). Populate both
   poles; the client's closest mirror sits at its own end.
2. **Specialisation** — *specialist* (one tight product/vertical) vs
   *generalist* (broad offer). Tighter overlap with the client's focus =
   more direct.
3. **Size / model** — *micro/informal* vs *SME* vs *mid-size* vs
   *enterprise/multinational*. Same-band players are the realistic
   head-to-head; larger bands are the aspirational/commercial-maturity
   reference.
4. **Distribution / channel** — *direct/retail* vs *agent/distributor
   network* vs *online/digital*. Signals reach and go-to-market maturity.
5. **Distinctiveness posture** — *conventional/undifferentiated* vs
   *deliberately positioned* (a clear promise, brand, or process). The
   differentiated end is key for distinctiveness benchmarking in any sector.
6. **Evidence / credibility model** — *outcome-led* (verifiable volumes,
   named clients, certifications) vs *reputation-led* (word of mouth, local
   standing). Tells you how each player earns trust.
7. **Brand strength of the operator** — *interchangeable/informal* vs *known,
   trusted name* (including strong sole proprietors who prove the
   "trusted-name" model works at small scale).
8. **Market / reach** — *local/regional* vs *national* vs *cross-border
   (EAC)*; note whether they win the same customers the client targets.

Plot each candidate on the relevant axes; a competitor is *direct* when it
sits near the client on positioning, specialisation, size, and market at
once.

## Competitive tiers (how the set resolves)

Group the final set into three tiers — this structure carries through to the
report:

- **Direct** — same band, overlapping offer, same customer targets. The
  realistic head-to-head.
- **Adjacent** — partial overlap (one product line, or a different customer
  segment/size) that pressures at the edges.
- **Aspirational** — players the client is not competing with today but
  whose commercial maturity or brand sets the bar to aim at (e.g. a national
  or regional player, for a client currently operating locally).
- *(Watch also for substitutes: informal/unregistered suppliers, imports,
  DIY/self-supply, or a customer's "do nothing" option — note as a threat
  vector, not a profiled competitor, unless materially relevant.)*

## Data sources (where to look)

Match the source to the dimension needed. Verification in East African
markets is often thinner than in mature digital markets — plan for primary
and semi-formal sources, not just websites:

- **Competitor's own site / social pages / WhatsApp Business profile** —
  primary source for positioning, offer, pricing posture, named clients.
- **Physical site visit or market survey** — for informal/retail competitors
  with no digital footprint; price checks, stock levels, footfall.
- **Trade/business directories and registries** — URSB company search,
  sector associations, chamber of commerce listings.
- **Review platforms and social proof** — Google reviews, Facebook,
  marketplace ratings where present.
- **Supplier/distributor conversations** — often the strongest signal for
  volumes and market share in low-data markets (see
  `meta-due-diligence/references/osint-business-intelligence.md` for the
  5-layer OSINT method).
- **Regulatory/certification bodies** — UNBS, NEMA, sector regulators —
  confirms compliance-based credibility claims.
- **News, trade press, conference/association presence** — thought-leadership
  and market-standing signals.

Always **verify claims across at least two sources** before treating a
competitor attribute as fact (self-reported claims or a single site visit ≠
verified outcome). Carry the never-fabricate-a-number rule
(`rules/common/core.md`) into this stage: an estimated competitor market
share or revenue figure must be labelled as an estimate, not presented as
fact.

## Scoring matrix template (selection stage)

A lightweight pre-filter to decide who graduates into full benchmarking.
Score 1–5; keep candidates that score high on **either** distinctiveness
**or** credibility — the client's strategic tension means both poles are
instructive.

| Candidate | Positioning stance | Specialisation | Size band | Tier | Offer overlap (1–5) | Distinctiveness (1–5) | Commercial credibility (1–5) | Include? |
|-----------|--------------------|-----------------|-----------|------|----------------------|-------------------------|-------------------------------|----------|

Rules of thumb (apply per the client's scoping consequence in the positioning
brief):

- High distinctiveness **and** high credibility → must-profile (proves the
  client's target tension is achievable).
- High distinctiveness, low credibility → cautionary case (memorable but
  unproven — a potential failure mode to learn from).
- High credibility, low distinctiveness → "competent but forgettable" mass
  the client defines itself against.
- Low on both → drop unless needed for landscape breadth.

## Output of this stage

A scoped, tiered competitor set (typically 8–15 candidates → 5–10 profiled
given data availability in EA markets), each tagged with its axis positions,
tier, and source links, ready to hand to `benchmark-methodology`.

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Client positioning brief with offer, target customers, differentiator, and strategic tension | Client or authorised engagement lead | Yes | Stop scoping and elicit the missing brief; do not invent a competitive lens. |
| Engagement context: business, industry, country, size band, and target market | `00-client-intake` and client evidence | Yes | Return the missing context to intake and mark tier decisions `NOT_ASSESSED`. |
| Candidate evidence and source trail | Approved research notes, registries, site observations, and named contacts | Conditional | Keep the candidate qualified or exclude it pending evidence; do not infer market share or revenue. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Scoped candidate register | Benchmark-methodology author | Each candidate has inclusion rationale, source trail, axis positions, and an explicit Direct, Adjacent, Aspirational, or substitute treatment. |
| Tiered competitor set | Client decision-maker and benchmark author | The set is pruned, decision-relevant, and explains who is excluded and why. |
| Scoping handoff note | Downstream competitive-intelligence skills | States the positioning brief, evidence gaps, verification status, and the next scoring action. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Candidate inclusion record | Register row with source and rationale | Another reviewer can reproduce why the candidate contests the client's position. |
| Tier and axis assessment | Annotated matrix or decision note | Direct, Adjacent, Aspirational, and substitute distinctions are visible and tied to evidence. |
| Verification and uncertainty log | Source notes with dates and limitations | Two-source corroboration, asserted claims, and estimated values are clearly labelled. |

## Capability and Permission Boundaries

Read and search are required. The skill may analyse authorised public and engagement evidence and draft a scoped register; it may not contact competitors, represent itself as the client, purchase data, disclose confidential client information, or publish intelligence. Site visits, interviews, registry fees, or any external communication require explicit engagement-owner authority.

## Degraded Mode

If the positioning brief, country context, candidate source, or corroboration is unavailable, stop the affected inclusion or tier decision, mark it `NOT_ASSESSED` or qualified, and issue the smallest evidence request for recovery. A thin digital footprint may support a clearly labelled candidate hypothesis, but it cannot establish a verified attribute or market-share figure. Continue only with the verified subset and state the downstream consequence.

## Decision Rules

| Condition | Action | Failure or risk avoided |
|---|---|---|
| The client lens is missing or generic | Return to positioning discovery and do not build a flat competitor list | Scoping noise that cannot inform strategy |
| A candidate overlaps only on product but not customers, size, or market | Classify it as Adjacent or exclude it, with the rationale recorded | Treating every similar offer as a head-to-head rival |
| A candidate is a maturity reference outside the current market | Classify it Aspirational and keep the commercial distance visible | Comparing unlike operators as if they share the same fight |
| A market-share or revenue figure is estimated | Label it an estimate with method and uncertainty, or remove it | An unsupported number becoming plan fact |

## Workflow

1. Confirm the client positioning brief, business context, country, permission boundary, and decision the competitor set must support; stop if a required input is missing.
2. Gather candidates across the source types already specified, then record size, niche, geography, engagement model, presentation, operational depth, brand strength, and evidence model.
3. Plot each candidate against the generic axes and apply Direct, Adjacent, Aspirational, or substitute treatment using the client's scoping consequence.
4. Apply the pre-filter, test the countercase and exclusion rationale, and verify material attributes across at least two sources where feasible.
5. Hand off the pruned set, source links, uncertainty, and recovery requests to `benchmark-methodology`; if the set is not defensible, return to step 1 rather than scoring it.

## Quality Standards

- Every included candidate has a named reason for inclusion, a tier, axis positions, and a source trail; exclusions are explainable.
- The positioning brief remains the frame for inclusion, and the business-plan core rule on country and engagement context is honoured.
- Direct, Adjacent, Aspirational, and substitute categories remain distinct, with the client's realistic head-to-head set clearly identified.
- Self-reported claims, estimates, and single-source observations retain their uncertainty until corroborated; no market figure is silently promoted to fact.
- The handoff exposes the strongest countercase, the evidence gaps, and the condition required before benchmarking can begin.

## References

- [Business-plan core rules](../../../rules/common/core.md)
- [Client intake](../../pipeline/00-client-intake/SKILL.md)
- [Benchmark methodology](../benchmark-methodology/SKILL.md)
- [OSINT business-intelligence reference](../meta-due-diligence/references/osint-business-intelligence.md)
- [Competitive report structure](../competitive-report-structure/SKILL.md)

<!-- dual-compat-end -->

## Anti-Patterns

- Scoping without a positioning brief. Correction: stop and elicit the client's offer, audience, differentiator, and tension first.
- Listing every similar business as a competitor. Correction: retain only candidates with a decision-relevant inclusion rationale.
- Blurring Direct, Adjacent, and Aspirational tiers. Correction: state the customer, size, geography, and maturity distinction for each tier.
- Treating a single site visit or self-reported claim as verification. Correction: label the observation and seek a second source.
- Presenting estimated market share or revenue as fact. Correction: label the estimate with its method and uncertainty or remove it.

- **Scoping without a positioning brief.** A competitor list built without
  the client's lens is noise. The brief determines what counts as a real
  rival.
- **Listing every similar business.** The goal is a defensible, pruned
  candidate set, not a census. Breadth without pruning makes benchmarking
  unmanageable.
- **Blurring the Direct/Adjacent/Aspirational tiers.** These tiers serve
  different strategic purposes. Mixing them produces a flat list that can't
  drive decisions.
- **Relying on a single source per competitor.** A single site visit or
  self-reported claim is not verification. Confirm across at least two
  sources.
- **Jumping straight to scoring.** This skill scopes and tiers the set.
  `benchmark-methodology` handles scoring. Don't conflate the two steps.
- **Treating an estimated market share or revenue figure as fact.** Label it
  an estimate per `rules/common/core.md`.

## Related Skills

- `pipeline/00-client-intake` — establishes the business name, industry, and
  country context this skill assumes is already in place.
- `pipeline/06-competitive-analysis` — use instead when the deliverable is
  the competitive-analysis section of a business plan, not a standalone
  competitive-intelligence report.
- `benchmark-methodology` — the next step; takes the tiered set and scores
  each competitor across nine dimensions.
- `meta-due-diligence` — OSINT methodology reference for gathering competitor
  intelligence in low-data East African markets.
