---
source: Agent SLA + commercial business-plan audit (2026); engine synthesis
frameworks: [SLA-quality valuation overlay; scoring rubric; adjustment trail]
skill: meta-agent-valuation-overlay-for-sla
cross-reference: [meta-valuation, meta-ai-valuation-adjustments, meta-agent-valuation-adjustments, meta-bankability-scoring]
---

# SLA Valuation Adjustments — Reference (local to meta-agent-valuation-overlay-for-sla)

This file is the working reference for the SLA-quality valuation overlay invoked by `meta-agent-valuation-overlay-for-sla/SKILL.md`. It mirrors `meta-valuation/references/saas-agent-sla-valuation-adjustments.md` (which is the cross-skill canonical) and is duplicated here for skill-local self-containment.

The canonical version with adjustment-trail templates, comparable-transaction patterns, and stress-adjustment tables lives at:

**`skills/meta-valuation/references/saas-agent-sla-valuation-adjustments.md`**

This local file summarises the scoring rubric and overlay mapping for skill-internal use.

---

## Scoring Rubric — 7 dimensions

| # | Dimension | Weight | 0 | 2 | 4 |
|---|---|---|---|---|---|
| 1 | SLA performance trend (4-quarter trailing) | 25% | Worsening; misses commit | Stable; mostly meeting | Trending up; exceeding |
| 2 | SLA disclosure posture | 20% | Undisclosed | Customer-shared | Public + audited |
| 3 | Reserve methodology maturity | 15% | Ad hoc / none | Documented internal | Auditor-concurrent quarterly |
| 4 | Dispute discipline | 15% | Backlog >30 day aging | Resolved <14 days | <1% rev in dispute; <7 day aging |
| 5 | Customer reference quality | 10% | None | One reference | Multiple enterprise refs |
| 6 | Regulator alignment | 10% | None / at odds | Engaged informally | Pre-cleared / aligned |
| 7 | Cost-of-quality investment | 5% | None | Modest line-item | Substantial + ROI shown |

Weighted score (out of 4):

| Weighted SLA score | Overlay applied | Investor read |
|---|---|---|
| 3.5 - 4.0 | +15 to +25% | Operational maturity at scale |
| 2.5 - 3.4 | +5 to +15% | Disciplined; trajectory positive |
| 1.5 - 2.4 | 0% (neutral) | Build mode; honest narrative |
| 0.5 - 1.4 | -10 to -20% | Unpriced volatility; governance immaturity |
| 0 - 0.4 | -20 to -40% | Material risk; rebuild required |

---

## Adjustment Trail Position

```
Adjusted multiple =
    SaaS R40-adjusted base
  × AI defensibility adjustment
  × Agent moat / governance adjustment
  × SLA overlay  ← THIS FILE
  × Geographic adjustment
```

---

## Cross-References (full content)

- **Canonical valuation overlay**: `skills/meta-valuation/references/saas-agent-sla-valuation-adjustments.md`
- Parent skill: `skills/meta-agent-valuation-overlay-for-sla/SKILL.md`
- Bankability evidence: `skills/meta-bankability-scoring/references/saas-agent-sla-bankability-checklist.md`
- Investor narrative: `skills/11-funding-request/saas-agent-investor-narrative-on-sla/SKILL.md`
- Stress overlay: `skills/meta-financial-stress-test/references/saas-agent-sla-stress-test-scenarios.md`
- Data-room evidence: `skills/meta-due-diligence/references/saas-agent-sla-data-room-contents.md`
- Audit: `book-extractions/agent-sla-commercial-business-plan-audit-2026.md`
