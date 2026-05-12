---
source: Agent SLA + commercial business-plan audit (2026); 2024-2026 valuation / comparable-transaction practice; engine synthesis
frameworks: [SLA valuation overlay; scoring rubric; adjustment trail]
skill: meta-valuation
cross-reference: [meta-agent-valuation-adjustments, meta-agent-valuation-overlay-for-sla, meta-bankability-scoring]
---

# SaaS Agent SLA Valuation Adjustments — Reference Table

This reference defines the SLA-quality overlay applied on top of the SaaS / AI / agent valuation base. The overlay is invoked by `meta-agent-valuation-overlay-for-sla` and feeds the adjustment trail in `meta-valuation`.

---

## Adjustment trail position

```
Adjusted ARR multiple =
    SaaS Rule-of-40-adjusted base
  × AI defensibility adjustment (meta-ai-valuation-adjustments)
  × Agent moat / governance / talent adjustment (meta-agent-valuation-adjustments)
  × SLA overlay (this reference)
  × Geographic / sovereign adjustment
```

SLA overlay can move the final multiple **+25% to −40%** in the empirically observed range from 2024-2026 agent transactions and DD outcomes.

---

## Scoring Rubric — 7 dimensions

| # | Dimension | Weight | 0 | 2 | 4 |
|---|---|---|---|---|---|
| 1 | SLA performance trend (4-quarter trailing) | 25% | Worsening; misses commitment | Stable; mostly meeting | Trending up; exceeding |
| 2 | SLA disclosure posture | 20% | Undisclosed | Customer-shared | Publicly published + audited |
| 3 | Reserve methodology maturity | 15% | Ad hoc / none | Documented internal | Auditor-concurrent quarterly |
| 4 | Dispute discipline | 15% | Backlog growing; >30 day aging | Resolved <14 days | <1% rev in dispute; <7 day aging |
| 5 | Customer reference quality on SLA | 10% | None | One reference | Multiple enterprise references |
| 6 | Regulator alignment on SLA | 10% | None / at odds | Engaged informally | Pre-cleared / sector-aligned |
| 7 | Cost-of-quality investment | 5% | None | Modest line-item | Substantial + ROI shown |

Compute weighted score (out of 4).

---

## Overlay Mapping

| Weighted SLA score | Overlay applied | Investor read |
|---|---|---|
| 3.5 - 4.0 | **+15 to +25%** | Operational maturity at scale; SLA is a moat |
| 2.5 - 3.4 | **+5 to +15%** | Disciplined; trajectory positive |
| 1.5 - 2.4 | **0% (neutral)** | Build mode; honest narrative; size round for SLA-discipline build |
| 0.5 - 1.4 | **−10 to −20%** | Unpriced revenue volatility; governance immaturity |
| 0 - 0.4 | **−20 to −40%** | Material risk; investor pass likely; rebuild required |

---

## Worked Example

**Company A** — agent business at USD 12M ARR; Per-resolution under uptime + accuracy SLA archetype; Series B opening.

Scoring:
- Dim 1 (perf): 3.0 (4 quarters of 99.85% uptime against 99.5% commit; DoD 97.4% vs 95%)
- Dim 2 (disclosure): 4.0 (public status page; audited quarterly)
- Dim 3 (reserve): 4.0 (Big-4 auditor concurrence; quarterly true-up; variance <8%)
- Dim 4 (dispute): 3.0 (avg aging 9 days; 0.6% of rev in dispute)
- Dim 5 (customer ref): 3.0 (3 enterprise references citing SLA)
- Dim 6 (regulator): 2.0 (engaged but not pre-cleared)
- Dim 7 (cost of quality): 3.0 (line-item growing; ROI shown)

Weighted score = (3.0×0.25) + (4.0×0.20) + (4.0×0.15) + (3.0×0.15) + (3.0×0.10) + (2.0×0.10) + (3.0×0.05) = 0.75 + 0.80 + 0.60 + 0.45 + 0.30 + 0.20 + 0.15 = **3.25 / 4.0**.

Overlay: **+10 to +15%** premium.

Applied to base multiple of 8x ARR → adjusted multiple 8.8 - 9.2x ARR → valuation USD 105-110M vs unadjusted USD 96M. Material.

---

## Stress Adjustments — when overlay compresses

| Stress event | Overlay compression |
|---|---|
| Catastrophic SLA breach in last 12 months without strong RCA | -10 to -25% on top of base score effect |
| Reserve inadequacy disclosed (actuals >120% reserve drawn ≥1 quarter) | -10 to -20% |
| Material outcome-pricing refund cascade | -15 to -30% |
| Regulator-mandated SLA tightening unresponded | -5 to -15% |
| Foundation-model cost shock without pass-through clause coverage | -10 to -20% |
| Customer SLA-gaming pattern undetected | -5 to -15% |
| Sovereign-AI provider pass-through breach without contractual coverage | -5 to -15% |

Stress compressions apply **on top of** the base overlay — score-implied premium can be erased and inverted by a single material event.

---

## Comparable-Transaction Patterns (2024-2026)

Where SLA quality was visibly cited in deal documentation:

- **Enterprise CX / collections agent acquisitions** — premium multiples (8-15x ARR) frequently cited SLA performance (published, audited) as a buying rationale; un-disclosed peers transacted at 4-7x ARR
- **Vertical legal / medical / financial agent rounds** — Series A / B premium pricing correlated with SLA discipline + auditor concurrence; non-disclosed companies struggled to close
- **Public-sector / sovereign-AI deals** — strong SLA delivery on prior contracts materially lifted comparable-transaction multiples in the sovereign-AI envelope
- **African / EM agent rounds** — geographic discount (-15 to -35%) **partially offset** by strong SLA discipline (+5 to +15%); net position better than no-SLA-discipline African peers

---

## Adjustment Trail Disclosure (for the valuation memo)

Format:

```
| Step | Factor | Multiple | Cumulative | Reasoning |
|------|--------|----------|------------|-----------|
| 1 | SaaS R40-adjusted base | 6.0x | 6.0x | R40 = 52% |
| 2 | AI defensibility | ×1.20 | 7.2x | AI moat dimension 7 |
| 3 | Agent moat / governance | ×1.15 | 8.3x | Wardley moat + Class C |
| 4 | SLA overlay | ×1.12 | 9.3x | SLA score 3.25 |
| 5 | Geographic adjustment | ×0.85 | 7.9x | Africa discount |
```

The SLA-overlay row should reference the scoring rubric and bankability checklist for traceability.

---

## Cross-References

- `skills/meta-valuation/SKILL.md` — valuation parent
- `skills/meta-agent-valuation-adjustments/SKILL.md` — agent valuation parent
- `skills/meta-agent-valuation-overlay-for-sla/SKILL.md` — overlay skill
- `skills/meta-bankability-scoring/references/saas-agent-sla-bankability-checklist.md` — bankability evidence
- `skills/11-funding-request/saas-agent-investor-narrative-on-sla/SKILL.md` — narrative
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Geographic discount of -15 to -35%** applies on top; SLA overlay applies on top of that and can partially recover
- **Sovereign-AI premium** — strong SLA + sovereign positioning compound; African plans with both can compress geographic discount by 5-10pp
- **DFI co-investment** — strong SLA score often opens DFI ticket alongside institutional ticket; narrows institutional-vs-DFI multiple gap
- **Mid-tier auditor concurrence** is acceptable for Dimensions 3 and 4 scoring in African markets; do not over-discount where Big-4 unavailable
- **Public-sector SLA delivery** — high-profile public-sector contracts (Huduma / NIMC / Irembo / NITA-U) with documented SLA performance lift Dimension 5 materially
- **Insurance-scarcity backstop** — self-insurance reserve adequacy is the SLA-overlay evidence; document transparently
- **FX-corridor disclosure** — clear FX-corridor / reserve-currency disclosure adds Dimension 6 / 7 weight in DFI / international-investor scoring
