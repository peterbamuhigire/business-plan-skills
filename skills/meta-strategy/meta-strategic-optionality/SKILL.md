---
name: meta-strategic-optionality
description: Use when a SaaS plan has external capital (the cap-table holders need an exit thesis). Use the relevant plan-section skill for section drafting.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Strategic Optionality & Exit Planning Skill

## Overview

Most SaaS plans assume a single exit path (strategic acquisition or IPO). The discipline is **optionality**: keeping multiple paths open as long as possible. This skill maps the exit landscape, designs the optionality-preserving moves the company makes today, and produces the explicit thinking that boards and investors expect by Series B / DFI growth-equity stage.

## Use When

- A SaaS plan has external capital (the cap-table holders need an exit thesis)
- Founders are weighing fundraise vs profitability vs distribution
- A strategic-buyer approach has arrived (always evaluate; preserve negotiating leverage)
- The company is at $10M+ ARR and exit conversations become real

## Do Not Use When

- The request belongs to the neighbouring route. Use a section skill for drafting; use this family for testing, synthesis, governance, or cross-section decisions.
- The available evidence cannot support a responsible strategic optionality conclusion; return the evidence gap instead of inventing one.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Strategic Optionality brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Cap table + investor preferences (liquidation preferences, participation, drag-along)
- Founder economics (preferred outcome at various exit levels)
- Strategic-buyer universe (named potential acquirers)
- PE / secondary-buyer landscape
- IPO readiness signals

## Workflow

1. **Map exit paths:**
   - **Strategic acquisition** — sold to a larger company for strategic value (most common SaaS exit at $20M-$500M)
   - **PE rollup** — sold to a private-equity buyer aggregating a portfolio (mature SaaS $20M-$200M)
   - **PE growth equity** — minority sale to PE for liquidity + growth capital (often $20M-$100M with founder partial liquidity)
   - **IPO** — public-market exit ($100M+ ARR typically; rare in African contexts; JSE / NSE / GHX possible but thin)
   - **Secondary** — partial sale of founder / early-investor shares without company-level exit
   - **Founder dividend** — extracting profit while continuing to operate (only for profitable bootstrap-style SaaS)
   - **Hold forever** — Berkshire-style; no exit needed; reinvest profits
2. **Identify the strategic-buyer universe** — list named potential acquirers with rationale:
   - Adjacent SaaS companies that need your capability / customers / IP
   - Larger players in your vertical that need to add a feature / segment
   - Tech-conglomerates with M&A appetite (Microsoft, Salesforce, Atlassian, Workday, ServiceNow)
   - Africa-specific: telcos (Safaricom, MTN, Liquid), banks (Standard, Ecobank, Stanbic), fintech (Flutterwave, Interswitch, MFS Africa, Onafriq)
   - PE rollups in your sector
3. **Design optionality-preserving moves NOW:**
   - Build for multiple exit paths simultaneously
   - Avoid contracts that lock you to one strategic (no exclusive integrations with one big partner)
   - Keep cap table clean (avoid dirty preferences that scare acquirers)
   - Maintain audit-ready books (saves time at deal stage)
   - Build relationships with target acquirers before you need to sell (Cohen / Bessemer; "the deal you can do is the relationship you've built")
4. **Model exit economics** at different exit values:
   - Founder take-home at $20M / $50M / $100M / $200M / $500M exit
   - Investor returns to each class at each exit value
   - Tax implications by jurisdiction
   - ESOP economics
5. **Plan the timing** — when does optionality compound? Usually $10-30M ARR is the sweet spot for strategic-acquisition optionality.
6. **Design the founder-economic conversation with the board** — founders and investors don't always want the same exit; surface this explicitly before it becomes a conflict.
7. **Cross-reference Section 11 (Funding Request)** — the exit thesis should reconcile with how the funding is being deployed.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the strategic-options map and that the decision concerns which exit and ownership paths to preserve now.
- **Stop condition:** halt the affected conclusion if required evidence is missing (capital structure, founder objectives, buyer logic, and milestone economics) or if the work could lead to this identified risk: locking the business into an exit story that weakens current choices.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Multiple exit paths named and assessed (not just one)
- Named strategic-buyer universe (not "we'll be acquired by someone")
- Optionality-preserving moves identified for the current quarter
- Founder economics modelled at multiple exit values
- Cap table / preference structure understood
- IPO realistic / unrealistic explicitly assessed

## Anti-Patterns

- "We'll IPO" without $100M+ ARR trajectory
- Single named acquirer (vendor risk on the exit side)
- Liquidation preferences that crush founders at modest exits
- "Hold forever" without operational discipline to sustain profitability
- Optionality discussion only at exit-conversation time (too late)


- Applying the wrong neighbouring route to meta strategic optionality. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Strategic Optionality deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Exit-path map with assessment per path
- Strategic-buyer universe (named, prioritised)
- Optionality-preserving moves for next 12 months
- Exit-economics waterfall at multiple exit values
- Founder-economic conversation framework
- Section 11 reconciliation notes

## References

- `references/saas-exit-strategy-and-strategic-optionality.md` — full reference with worked examples
- `book-extractions/walling-saas-playbook-extraction.md` — bootstrapper exit philosophy
- `book-extractions/haines-how-to-create-a-business-case-extraction.md` — options analysis discipline
- `skills/saas-valuation-and-fundraising-strategy/SKILL.md` — sister skill for valuation
- `skills/meta-valuation/SKILL.md` — DCF / WACC

## Africa / Uganda Application Notes

- **IPO is rare** in African SaaS — JSE, NSE, GHX have thin SaaS listings. Most exits are strategic acquisitions.
- **Strategic buyers in Africa**: telcos (Safaricom, MTN, Vodacom, Airtel, Liquid), banks (Standard, Stanbic, Ecobank, NMB, Equity, KCB), pan-African fintech (Flutterwave, Interswitch, MFS Africa / Onafriq, MoneyHash), global tech entering Africa (Visa, Mastercard, Stripe, Google, Microsoft, Meta).
- **PE rollups** are emerging (Helios, DPI, Adenia, AfricInvest, EXEO).
- **Patient-capital holders** (DFIs, Acumen) often accept longer holds — exit pressure is less aggressive than VC.
- **Founder secondary** at Series B-equivalent is increasingly possible — provides liquidity without forcing company exit.
- **Hold-forever** is realistic for profitable African SaaS — companies like SeamlessHR, Workpay, Yoco may opt for sustainable hold.
- **FX in exit**: USD-priced strategic offers are typical; local-currency cost base creates an interesting hedge.
- **Capital gains tax** by jurisdiction (Kenya, Nigeria, South Africa, Uganda each different); structure equity holding accordingly.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Strategic-options map decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to locking the business into an exit story that weakens current choices. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the strategic-options map; drafting scenarios without soliciting buyers or securities is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If capital structure, founder objectives, buyer logic, and milestone economics cannot be obtained, return a qualified strategic-options map covering only the checks that remain supportable. Leave this decision unresolved: which exit and ownership paths to preserve now. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which exit and ownership paths to preserve now | Record the conclusion, source trail, owner, and review trigger in the strategic-options map. | Risk of locking the business into an exit story that weakens current choices |
| Material evidence conflicts or remains uncertain | Model the competing ownership paths against the same milestones, cash needs, control preferences, and buyer assumptions without selecting an exit prematurely. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: capital structure, founder objectives, buyer logic, and milestone economics | Mark the decision on which exit and ownership paths to preserve now `not assessed` in the strategic-options map, and send it to the plan owner and executive sponsor. | Otherwise, the work risks locking the business into an exit story that weakens current choices |

## Quality Standards


Accept the strategic-options map only when evidence is sufficient for this decision: which exit and ownership paths to preserve now. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of locking the business into an exit story that weakens current choices.

## Worked Example


A founder assumes acquisition is the only credible outcome before product-market fit. Model dividend, strategic sale, and follow-on-growth paths against capital and control needs, preserving the options that current choices can support.

<!-- dual-compat-end -->
