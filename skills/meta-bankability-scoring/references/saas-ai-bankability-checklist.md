---
source: Mersch CFO discipline; 2024-2026 AI-investor diligence; NIST AI RMF; engine synthesis
frameworks: [5-section AI bankability scorecard; Investor-archetype weighting; Remediation backlog]
skill: meta-ai-bankability-and-investor-readiness (also referenced by meta-bankability-scoring)
cross-reference: [meta-ai-valuation-adjustments, saas-ai-unit-economics-and-cogs, saas-ai-moat-and-defensibility, saas-ai-risk-and-stress-test, saas-ai-data-room-contents]
---

# SaaS AI Bankability Checklist

## 1. Five-section scorecard (max ~50 points)

Each line item: 0 = absent / aspirational, 1 = in progress, 2 = operating but improvable, 3 = mature.

### Section A — AI Economics (max 15)

| Line item | Score | Evidence required |
|---|---|---|
| AI-cost-as-%-of-ARR <10% | 0-3 | Headline number with trajectory |
| AI Gross Margin >65% with positive trajectory | 0-3 | 12-month GM history |
| AI Contribution Margin positive across all tiers | 0-3 | Per-tier exhibit |
| Per-tenant AI cost modelled (median + top decile) | 0-3 | Cost-of-tenant calculator output |
| AI-revenue share declared with attribution methodology | 0-3 | Attribution analysis |

### Section B — AI Discipline (max 12)

| Line item | Score | Evidence required |
|---|---|---|
| Eval coverage >60% with weekly cadence | 0-3 | Eval methodology document + history |
| Hallucination rate measured + declining trajectory | 0-3 | Measurement methodology + 12-month history |
| Production sampling rate stated | 0-3 | Sampling policy |
| Model-deprecation watch operating | 0-3 | Watch process + last review date |

### Section C — AI Governance (max 12)

| Line item | Score | Evidence required |
|---|---|---|
| AI policy current + version-controlled | 0-3 | Document + version history |
| AI committee operating + monthly meetings | 0-3 | Charter + minutes (last 6+ months) |
| AI-incident protocol + runbook | 0-3 | Runbook + log (or "no incidents" + sampling evidence) |
| Training-data provenance audit complete | 0-3 | Provenance log + audit |

### Section D — AI Moat (max 7; pulled from moat-and-defensibility 21-point score, rescaled)

| Line item | Score | Evidence required |
|---|---|---|
| Moat score 0-21 (rescaled to 0-7 = score × 7/21) | 0-7 | `saas-ai-moats-and-defensibility-checklist.md` output |

### Section E — AI Risk (max 9)

| Line item | Score | Evidence required |
|---|---|---|
| Vendor concentration <70% on single provider | 0-3 | Cost breakdown |
| Regulatory posture per jurisdiction stated | 0-3 | Compliance map |
| Hallucination-liability reserve adequate | 0-3 | Reserve sizing methodology |

## 2. Score interpretation

| Total score | Verdict | Investor implication |
|---|---|---|
| 0-20 | Weak — AI bankability not established | Cannot price AI premium; AI discount likely |
| 21-30 | Typical — AI is real but not differentiating | Neutral AI overlay; standard SaaS multiple applies |
| 31-40 | Strong — AI bankability evident | AI premium plausible (+0.5x to +1.5x) |
| 41-50 | Exceptional — institutional-grade AI | Substantial AI premium (+1.5x to +3x) |

## 3. Investor-archetype weighting (the scorecard is not one-size-fits-all)

| Investor type | Section A | B | C | D | E |
|---|---|---|---|---|---|
| **AI-specialist VC (a16z AI, Index AI, Bessemer AI)** | 3x | 2x | 2x | 3x | 2x |
| **Generalist SaaS VC (Sequoia, Accel, Benchmark)** | 3x | 1x | 1x | 2x | 2x |
| **Sovereign-AI fund (G42 / MGX, EU sovereign-AI, KSA Vision 2030)** | 2x | 2x | 3x | 3x | 3x |
| **DFI (IFC, AfDB, BII, FMO, Proparco, Norfund)** | 2x | 2x | 3x | 2x | 3x |
| **AI-for-good grantmaker (Mozilla, GSMA, IDRC, Lacuna)** | 1x | 2x | 3x | 1x | 3x |
| **Strategic acquirer** | 2x | 2x | 2x | 3x | 2x |

Apply the weighting to identify which section to prioritise improving for the target archetype.

## 4. Remediation backlog (the output)

After scoring, produce a prioritised backlog:

| Section / Item | Current score | Target | Action | Owner | Timeline |
|---|---|---|---|---|---|
| (e.g.) B — Eval coverage | 1 | 3 | Build evals for top 5 features by ARR | Head of AI / QA | 90 days |
| (e.g.) C — AI committee | 1 | 3 | Formalise charter; start monthly meetings | CEO | 60 days |
| (e.g.) E — Vendor concentration | 1 | 3 | Multi-provider router; secondary contract | CTO | 120 days |

Backlog is a deliverable to the board and investor.

## 5. Anti-patterns

- Aggregate-only score (no line-item breakdown)
- Eval coverage 95% on a 5-test eval suite (game-able)
- Hallucination "low" without a number
- AI policy in draft for >6 months
- AI committee aspirational
- Vendor concentration ignored
- Reserve "we set aside something" without methodology
- Same pitch / scorecard for all investor archetypes

## 6. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Full scorecard refresh | quarterly | CFO + CEO |
| Section A (economics) updates | monthly | CFO |
| Section B (discipline) updates | weekly (evals) + monthly (sampling) | Head of AI / QA |
| Section C (governance) updates | per meeting (monthly) | AI committee chair |
| Section D (moat) updates | quarterly | CEO + Head of Strategy |
| Section E (risk) updates | quarterly + per event | CFO + Head of AI |
| Investor archetype weighting | per round | CEO |
| Remediation backlog | monthly | CEO + CFO + Head of AI |

## 7. Africa / Uganda Specifics

- DFI weighting (above) tilts hard toward governance + risk + ethics — Section C and E are the binding constraints for DFI fundability
- AI-for-good grant weighting de-emphasises pure economics; emphasises training-data provenance, ethics, community benefit
- Sovereign-AI tender readiness is a special bankability layer (data residency, local-talent evidence, local-language coverage, governance) — score as add-on for plans targeting public sector
- AI talent retention in Africa is the binding scaling constraint and should be tracked as a bankability-adjacent metric
