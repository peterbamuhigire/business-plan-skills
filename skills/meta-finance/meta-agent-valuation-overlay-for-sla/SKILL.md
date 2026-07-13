---
name: meta-agent-valuation-overlay-for-sla
description: Use when an agent business with SLA commitments is being valued. Use financial projections for model construction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->


# Meta — Agent Valuation Overlay for SLA Skill

## Workflow

1. Confirm the decision audience, scope, current evidence, and applicable finance doctrine.
2. Apply the ordered domain analysis below and reconcile every calculation to its source.
3. Record the decision, exceptions, reviewer, and next evidence action before release.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the SLA valuation overlay and that the decision concerns whether SLA performance earns a multiple premium or discount.
- **Stop condition:** halt the affected conclusion if required evidence is missing (four-quarter SLA, credit, reserve, and dispute evidence) or if the work could lead to this identified risk: pricing hidden service volatility as durable ARR.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

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


- Route to `10-financial-projections` instead when the task is to construct the underlying model.
## Required Inputs

- SaaS / AI / agent valuation base (from prior valuation skills)
- SLA performance trailing 4-quarter trend (uptime, accuracy, DoD compliance, credit ratio)
- SLA disclosure posture (published / audited / private / undisclosed)
- Reserve methodology maturity
- Dispute history
- Customer testimonials referencing SLA performance
- Comparable transactions noting SLA quality
- Regulator engagement on SLA (where sector regulator is active)

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


- Applying the wrong neighbouring route to meta agent valuation overlay for sla. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Valuation Overlay For Sla deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
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

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| SLA valuation overlay decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to pricing hidden service volatility as durable ARR. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the SLA valuation overlay; adding the SLA adjustment to a supplied valuation analysis is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If four-quarter SLA, credit, reserve, and dispute evidence cannot be obtained, return a qualified SLA valuation overlay covering only the checks that remain supportable. Leave this decision unresolved: whether SLA performance earns a multiple premium or discount. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: whether SLA performance earns a multiple premium or discount | Record the conclusion, source trail, owner, and review trigger in the SLA valuation overlay. | Risk of pricing hidden service volatility as durable ARR |
| Material evidence conflicts or remains uncertain | Calculate the multiple effect under strong, weak, and unverified SLA evidence, then retain the unverified case as the base until records arrive. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: four-quarter SLA, credit, reserve, and dispute evidence | Mark the decision on whether SLA performance earns a multiple premium or discount `not assessed` in the SLA valuation overlay, and send it to the valuation lead and transaction adviser. | Otherwise, the work risks pricing hidden service volatility as durable ARR |

## Quality Standards


Accept the SLA valuation overlay only when evidence is sufficient for this decision: whether SLA performance earns a multiple premium or discount. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of pricing hidden service volatility as durable ARR.

## Worked Example


An agent company claims premium uptime while its credit ratio and dispute log are unavailable. Use the unverified SLA case in the valuation and assign the premium only after four-quarter evidence reconciles.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the SLA valuation overlay, using the reporting basis and effective date supported by four-quarter SLA, credit, reserve, and dispute evidence. Reconcile the treatment to the model and narrative, and have the valuation lead and transaction adviser review the treatment, reconciliation, and exposure to this risk: pricing hidden service volatility as durable ARR.

<!-- dual-compat-end -->
