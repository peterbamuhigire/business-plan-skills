---
name: meta-agent-valuation-overlay-for-sla
description: Valuation overlay for SLA quality. Premium when SLA performance is strong, published, audited, disclosed; discount when SLA performance is hidden, weak, or contested. Effect on ARR multiple. Composes with `meta-agent-valuation-adjustments` (which handles moat-vs-wrapper, intervention rate, governance, regulator). Use whenever an agent business with SLA commitments is being valued.
---

# Meta — Agent Valuation Overlay for SLA Skill

## Overview

SaaS valuation (handled by `meta-valuation`) uses Rule-of-40-adjusted ARR multiples. AI valuation (`meta-ai-valuation-adjustments`) layers AI defensibility premium/discount. Agent valuation (`meta-agent-valuation-adjustments`) layers moat-vs-wrapper, intervention-rate trajectory, governance, regulator, foundation-model platform risk.

**SLA quality is a distinct valuation dimension** that sits within or alongside agent valuation. Two agent businesses with identical ARR, identical moat-vs-wrapper score, and identical intervention-rate trajectories trade at different multiples if their SLA disciplines diverge:

- **Strong SLA discipline** (measurable, published, audited, low credit ratio, disciplined reserve) → premium signalling operational maturity and revenue-volatility floor
- **Weak SLA discipline** (hidden performance, ad hoc reserves, undisclosed disputes, credit ratio drift) → discount signalling unmanaged revenue volatility and governance immaturity

The dispersion can be 10-30% of the multiple. This is material.

## Use When

- An agent business with SLA commitments is being valued
- A funding round is being planned and pre-money expectation set
- An exit comparable analysis is being run
- A board pack includes a valuation update
- The plan must declare its expected multiple range with reasoning
- Cross-loaded with `meta-valuation`, `meta-ai-valuation-adjustments`, `meta-agent-valuation-adjustments`

## Do Not Use When

- The agent business has no SLA commitments — use agent valuation alone
- The plan is too early for valuation discipline

## Required Inputs

- SaaS / AI / agent valuation base (from prior valuation skills)
- SLA performance trailing 4-quarter trend (uptime, accuracy, DoD compliance, credit ratio)
- SLA disclosure posture (published / audited / private / undisclosed)
- Reserve methodology maturity
- Dispute history
- Customer testimonials referencing SLA performance
- Comparable transactions noting SLA quality
- Regulator engagement on SLA (where sector regulator is active)

## Workflow

### 1. Score the SLA quality dimension

Per `references/saas-agent-sla-valuation-adjustments.md`, score across:

| Dimension | Weight | Score 0-4 |
|---|---|---|
| SLA performance trend (4-quarter trailing) | 25% | 0=worsening; 4=strong improving |
| SLA disclosure posture | 20% | 0=undisclosed; 4=audited and published |
| Reserve methodology maturity | 15% | 0=ad hoc; 4=auditor-concurrent quarterly |
| Dispute discipline | 15% | 0=backlog growing; 4=disputes <1% of revenue, resolved in 7 days |
| Customer reference quality on SLA | 10% | 0=none; 4=multiple enterprise references quoting SLA |
| Regulator alignment on SLA | 10% | 0=at odds; 4=pre-cleared / sector-aligned |
| Cost-of-quality investment | 5% | 0=none; 4=substantial and increasing |
| Total | 100% |  |

Compute weighted score (out of 4). Map to overlay:

| SLA score | Overlay |
|---|---|
| 3.5 - 4.0 | +15-25% premium |
| 2.5 - 3.4 | +5-15% premium |
| 1.5 - 2.4 | 0% (neutral) |
| 0.5 - 1.4 | -10-20% discount |
| 0 - 0.4 | -20-40% discount |

### 2. Apply the overlay

Adjusted multiple = SaaS base × AI adjustment × agent adjustment × **SLA overlay** × geographic adjustment.

### 3. Show the adjustment trail

The valuation memo must show each adjustment with reasoning. The SLA overlay is explicit and traceable.

### 4. Stress under SLA scenarios

- Catastrophic SLA breach scenario: what does the multiple compress to?
- Reserve depletion + funding need: pre-money discount applied
- Regulator-mandated SLA: cost compression flowing through margin → multiple change

### 5. Cross-load with comparable transactions

Where comparable agent transactions are available, note whether the comparable had visible SLA discipline. Premium-priced exits (e.g. enterprise agent acquisitions 2024-2026) frequently quote SLA performance as a buying criterion. Document the comparable SLA pattern.

### 6. Wire to investor narrative

The investor narrative on SLA (`saas-agent-investor-narrative-on-sla`) carries the story; the valuation overlay quantifies it. Cross-load.

### 7. Wire to bankability

The SLA bankability checklist (`saas-agent-sla-bankability-checklist.md`) checks the same dimensions; valuation overlay should reconcile.

### 8. Wire to living-plan governance

Per cadence below.

## Quality Bar

- SLA quality scored across 7 dimensions with reasoning
- Overlay applied transparently in the adjustment trail
- Stress under SLA scenarios shown
- Comparable transactions reviewed for SLA pattern
- Cross-loaded with bankability and investor narrative
- A sceptical investor would accept the SLA overlay as honest

## Anti-Patterns

- "Our SLA is great" without scoring evidence
- Overlay claimed without methodology
- Premium claimed when SLA performance is undisclosed
- Comparable transactions cherry-picked
- Overlay ignored under stress scenarios
- No reconciliation with bankability
- SLA discipline asserted without reserve evidence

## Outputs

- SLA quality score with dimension breakdown
- Valuation overlay with reasoning
- Adjustment trail update
- SLA stress impact on multiple
- Comparable transactions analysis
- Cross-reference to bankability and investor narrative
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| SLA quality score refresh | quarterly | CFO + Head of GTM | -0.5 point quarterly |
| Overlay reassessment | quarterly | CFO + CEO | overlay shift |
| Comparable-transactions SLA scan | quarterly | Head of Strategy | new comparable noting SLA |
| Pre-round overlay set | per-round | CEO + CFO + Board | round opens |
| Disclosure posture review | annually | CEO + CFO + Comms | shift in posture |

## References

- `references/saas-agent-sla-valuation-adjustments.md` — overlay table and worked example
- `skills/meta-valuation/SKILL.md` — SaaS valuation parent
- `skills/meta-ai-valuation-adjustments/SKILL.md` — AI valuation parent
- `skills/meta-agent-valuation-adjustments/SKILL.md` — agent valuation parent
- `skills/11-funding-request/saas-agent-investor-narrative-on-sla/SKILL.md` — narrative
- `skills/meta-bankability-scoring/references/saas-agent-sla-bankability-checklist.md` — bankability
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **African agent valuations** — already discounted -15 to -35% vs US/EU baselines; SLA overlay applies on top of geographic discount
- **Sovereign-AI premium** — strong SLA discipline + sovereign-AI positioning compounds (sovereign + SLA both signal local-fit + operational maturity)
- **DFI co-investment** — strong SLA discipline often opens DFI co-investment, narrowing the institutional vs DFI multiple gap
- **Insurance scarcity affects discount** — when insurance is thin (Africa), self-insurance reserve adequacy is the SLA-overlay evidence; document the reserve transparently
- **Public-sector SLA performance** — public-sector contracts with strong SLA delivery are reference-worthy and can lift overlay materially
- **Mobile-money settlement reliability** — for per-resolution agents, settlement reliability is part of SLA performance; document
- **FX-corridor SLA risk** — overlay should reflect FX-corridor exposure on local-currency SLA-credit liabilities
- **Local audit firm coverage** — where Big-4 audited financials are unavailable, audit-acceptable methodology + mid-tier auditor can still earn the overlay
