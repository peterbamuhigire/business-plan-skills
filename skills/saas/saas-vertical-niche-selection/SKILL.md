---
name: saas-vertical-niche-selection
description: Use when a new SaaS / ICT plan is being built (run BEFORE Section 03 and 04). Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS Vertical & Niche Selection Skill

## Overview

Choosing the wrong vertical is the most common cause of SaaS plan failure (Walling foreword, Cohen). Choosing the right vertical / niche is the single most leveraged strategic decision. This skill produces the explicit choice — with named criteria, scoring, and a defensible niche-by-geography intersection.

## Use When

- A new SaaS / ICT plan is being built (run BEFORE Section 03 and 04)
- An existing horizontal plan is failing and considering verticalisation
- A vertical plan is considering expanding to adjacent verticals
- A multi-country plan is considering which geographies to enter first

## Do Not Use When

- The request belongs to the neighbouring route. Use the cross-sector meta skill when the decision is not specific to recurring-revenue SaaS economics or operations.
- The available evidence cannot support a responsible vertical niche selection conclusion; return the evidence gap instead of inventing one.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Vertical Niche Selection brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Founder domain expertise / network
- Target ACV range
- Capital availability (vertical SaaS needs less; horizontal needs more)
- Geographic focus
- Existing customer / pilot data (if any)

## Workflow

1. **List candidate verticals** — based on founder domain knowledge + market opportunity + capital. Cap at 5-7 candidates.
2. **Score each on the Vertical Fit Scorecard** (see references):
   - Founder domain knowledge (5)
   - TAM (5)
   - Customer pain intensity (5)
   - Willingness-to-pay (5)
   - Competition / category-density (5; lower is better)
   - Cycle-length tolerance (5)
   - Network effects within vertical (5)
   - Channel access (5)
   - Geography fit (5)
   - Regulatory complexity (5; lower is better — sometimes higher = moat)
   - Total: out of 50
3. **For top 2-3 verticals, define the niche within the vertical** — geography × sub-segment × use-case. Specificity unlocks pricing power (Kennedy: "specifically-for" pricing lift typically 100-500%).
4. **Compute niche-pricing-lift potential** — how much pricing premium does deep niche specialisation enable vs horizontal alternatives?
5. **Decide horizontal vs vertical positioning** explicitly:
   - **Horizontal**: huge TAM, generic product, high competition. Salesforce, Slack, Notion.
   - **Vertical**: smaller TAM, sector-specific product, deep moat. Veeva, Procore, Toast, ServiceTitan.
   - **Africa default: VERTICAL** because local-context expertise (M-Pesa flow, KRA/URA tax, sector regulation, language) IS the moat.
6. **Articulate the ICP** within the chosen niche — firmographic + technographic + behavioural + psychographic.
7. **Define expansion path** — once dominant in niche A, what's niche B, C? (Walling: don't expand verticals too early.)
8. **Cross-reference**: Section 04 (Market Analysis), Section 05 (Target Market), Section 06 (Competitive Analysis), Section 07 (Marketing/Sales).

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the vertical-niche decision matrix and that the decision concerns which sector-by-geography niche earns focused investment.
- **Stop condition:** halt the affected conclusion if required evidence is missing (buyer pain, workflow depth, reachable accounts, regulation, competition, and pricing lift) or if the work could lead to this identified risk: choosing a broad market that prevents product depth and efficient distribution.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Vertical scored explicitly (not asserted)
- Niche defined as geography × sub-segment × use-case intersection
- Pricing lift quantified
- ICP definition has 4 dimensions
- Expansion path named (with do-not-expand-too-early discipline)
- Africa default of vertical-first applied where relevant

## Anti-Patterns

- "We'll serve any industry" — pricing collapses
- "We'll start broad and narrow later" — usually opposite is right
- Vertical chosen by founder enthusiasm without scoring
- Expanding to adjacent vertical before dominating the first
- Horizontal play with sub-$5M capital (capital insufficient)


- Applying the wrong neighbouring route to saas vertical niche selection. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Vertical Niche Selection deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Vertical fit scorecard with top 1-3 verticals chosen
- Defined niche within chosen vertical (geography × sub-segment × use-case)
- ICP definition (firmographic / technographic / behavioural / psychographic)
- Niche-pricing-lift estimate
- Vertical-expansion path
- Cross-reference updates to Sections 04, 05, 06, 07

## References

- `book-extractions/walling-saas-playbook-extraction.md` — niche selection, vertical discipline, expansion timing
- `book-extractions/mersch-hacking-saas-extraction.md` — vertical vs horizontal SaaS financial profile (chapters 15-16)
- `book-extractions/kennedy-no-bs-price-strategy-extraction.md` — niche pricing lift
- `skills/04-market-analysis/SKILL.md` — sister skill for TAM/SAM/SOM
- `skills/05-target-market/SKILL.md` — sister skill for ICP detail
- `country-context/africa-regional/africa-ict-saas-market-context.md` — Africa vertical opportunities

## Africa / Uganda Application Notes

- **African vertical SaaS sweet spots:** fintech-for-MSMEs, agritech (cooperative / smallholder), healthtech (insurance / supply-chain), logistics, edtech, energy (PAYG solar), public-sector / GovTech, HR (gig-worker platforms).
- **Geography × vertical intersection** is often where the moat lives — "the M-Pesa-integrated dairy-cooperative platform for Western Kenya" beats "agritech for Africa."
- **Niche-pricing lift in Africa** can be even higher than US benchmarks because incumbent alternatives are usually generic ERP / spreadsheets — switching to a niche-specific tool delivers obvious value.
- **Regulatory complexity** is sometimes the moat (fintech licensing, healthcare data, public-sector tax-clearance) — depth into these creates barriers.
- **Multi-country expansion** within Africa is non-trivial — different payment rails, regulators, languages. Plan vertical-deep before geographic-broad.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Vertical-niche decision matrix decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to choosing a broad market that prevents product depth and efficient distribution. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the vertical-niche decision matrix; recording the niche decision without entering commercial commitments is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If buyer pain, workflow depth, reachable accounts, regulation, competition, and pricing lift cannot be obtained, return a qualified vertical-niche decision matrix covering only the checks that remain supportable. Leave this decision unresolved: which sector-by-geography niche earns focused investment. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which sector-by-geography niche earns focused investment | Record the conclusion, source trail, owner, and review trigger in the vertical-niche decision matrix. | Risk of choosing a broad market that prevents product depth and efficient distribution |
| Material evidence conflicts or remains uncertain | Score the tied niches with primary buyer evidence and a sector-by-geography reachability test, then choose only if the lead survives sensitivity. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: buyer pain, workflow depth, reachable accounts, regulation, competition, and pricing lift | Mark the decision on which sector-by-geography niche earns focused investment `not assessed` in the vertical-niche decision matrix, and send it to the strategy owner and commercial lead. | Otherwise, the work risks choosing a broad market that prevents product depth and efficient distribution |

## Quality Standards


Accept the vertical-niche decision matrix only when evidence is sufficient for this decision: which sector-by-geography niche earns focused investment. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of choosing a broad market that prevents product depth and efficient distribution.

## Worked Example


Healthcare and logistics tie on a broad score. Add buyer access, workflow depth, regulation, and reachable-account evidence for the target geography; select a niche only if the lead survives sensitivity.

<!-- dual-compat-end -->
