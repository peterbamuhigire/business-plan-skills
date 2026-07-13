---
name: meta-agent-revenue-recognition-policy
description: Use when a plan is being prepared for audit, DFI / institutional DD, or institutional fundraising. Use financial projections for model construction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Meta — Agent Revenue Recognition Policy Skill

## Overview

The operational rev-rec skill (`saas-agent-revenue-recognition`) installs the analysis discipline. This meta-skill installs the **policy declaration discipline** — the practice of producing an auditor-ready policy memo as a first-class artefact of the plan, refreshing it annually, and making it traceable to the contract templates, financial model, and disclosure language.

Why a separate meta-skill: audit firms (Big-4 and regional) expect an explicit policy memo as a documented artefact. DD teams quote from it. Investors lean on it. Treating policy as an emergent property of the financial model is not enough — the policy must be a named, owned, dated artefact.

## Use When

- A plan is being prepared for audit, DFI / institutional DD, or institutional fundraising
- An auditor has been appointed and the policy memo is a deliverable
- A pricing primitive is being changed or added (modification triggers policy refresh)
- The plan involves outcome pricing, hybrid pricing, prepaid credits, SLA tiers, or any non-ratable revenue
- The annual planning cycle requires policy-memo refresh
- Cross-loaded with `saas-agent-revenue-recognition`, `saas-agent-deferred-revenue-and-credit-reserves`, `meta-accounting-finance-review`

## Do Not Use When

- The plan has flat monthly subscription only with a single deliverable (use `meta-accounting-finance-review`)
- The plan is pre-revenue and no pricing primitive is committed

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Revenue Recognition Policy brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
| Current accounting, tax, valuation, or pricing basis | Finance owner, accounting records, signed contracts, and current authoritative sources | Conditional | Mark the treatment unresolved and require qualified professional review. |
- Pricing primitives in scope (from `saas-agent-pricing-strategy`)
- Contract templates (from proposal session)
- Standalone selling price evidence (where available)
- Variable-consideration components inventory
- Principal-vs-agent indicators per service flow
- Audit firm (if appointed)
- Prior-period policy memo (if updating)
- Reporting framework (ASC 606 / IFRS 15 / both)

## Workflow

1. Inventory contract types, pricing primitives, performance obligations, and source evidence.
2. Draft the policy analysis under the current reporting framework and obtain auditor or qualified professional review where material.
3. Reconcile the approved policy to contracts, billing, ledger treatment, disclosures, and the financial model.

Follow the ordered policy analysis below; unresolved recognition questions stop release pending current-source and professional review.

### 1. Inventory pricing primitives + contract types

For each revenue-bearing contract type:
- Pricing primitive(s) involved
- Performance obligations (named)
- Transaction price components (fixed + variable)
- Allocation method
- Recognition trigger
- Principal-vs-agent posture (where applicable)
- Refund / breakage / SLA-credit terms

### 2. Draft the policy memo

Using `references/saas-agent-revenue-recognition-policy-template.md` (in the operational skill) as the template, produce:
- Scope (which pricing primitives are covered)
- Framework (ASC 606 / IFRS 15)
- Per-primitive 5-step analysis
- Variable-consideration estimation method per component
- Constraint methodology
- Principal-vs-agent conclusions
- Contract-modification policy
- Examples and edge cases
- Disclosure language

### 3. Auditor pre-review

Where an auditor is appointed:
- Provide the draft memo
- Schedule a policy review session
- Capture auditor feedback
- Revise

Where no auditor is appointed yet but a Series A / institutional round is in scope:
- Self-test against Big-4 published interpretive guidance
- Engage a fractional CFO or auditor consultant for a single review
- Document the review

### 4. Wire to financial model

- Each revenue line traces to a recognition trigger per the memo
- Variable consideration shown net of constraint
- Deferred revenue and reserves consistent with the memo
- VAT-vs-recognition timing reconciled

### 5. Wire to contract templates

Cross-load with proposal session:
- Contract language matches the memo's treatment
- Performance-obligation language consistent
- Outcome definitions consistent
- SLA terms consistent
- Refund / credit terms consistent

If contract language and memo treatment diverge, fix one or the other.

### 6. Wire to disclosure language

Draft the disclosure for the audited financial statements:
- Revenue recognition note (per primitive)
- Significant judgments note (variable-consideration estimation; constraint; SSP; principal-vs-agent)
- Contract balances note (receivable, contract asset, contract liability)
- Performance obligations note

### 7. Set the refresh cadence

- Annual policy refresh + auditor review
- Quarterly check on variable-consideration estimates
- Trigger refresh on:
  - New pricing primitive
  - Contract-modification volume spike
  - Principal-vs-agent service-flow change
  - Auditor / regulator feedback
  - Material change in business mix

### 8. Wire to living-plan governance

Per cadence below.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the agent revenue-recognition memo and that the decision concerns the recognition trigger for each performance obligation.
- **Stop condition:** halt the affected conclusion if required evidence is missing (executed contracts and pricing primitives) or if the work could lead to this identified risk: recognising outcome, credit, or SLA revenue before the obligation is satisfied.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Policy memo exists as a named, dated, owned artefact
- Covers every pricing primitive in scope
- 5-step analysis per primitive
- Variable-consideration estimation method per component
- Constraint applied with reasoning
- Principal-vs-agent analysis where applicable
- Contract-modification policy stated
- Disclosure language drafted
- Auditor pre-review obtained (where auditor appointed)
- Cross-references consistent (contract templates, financial model, disclosure)
- Memo passes Big-4 interpretive standard

## Anti-Patterns

- Policy memo is an emergent property of the financial model rather than a named artefact
- Memo not refreshed when pricing primitives change
- Memo says "we follow ASC 606" without 5-step analysis
- Contract templates and memo diverge
- Disclosure language not drafted; left to year-end audit
- No auditor pre-review
- Variable consideration without constraint
- Principal-vs-agent not analysed for orchestration revenue
- Breakage method not stated


- Applying the wrong neighbouring route to meta agent revenue recognition policy. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Revenue Recognition Policy deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Auditor-ready revenue recognition policy memo
- Per-primitive 5-step analysis
- Variable-consideration estimation methodology
- Principal-vs-agent conclusions
- Contract-modification policy
- Disclosure language for audited financial statements
- Cross-reference map (contract templates, financial model, disclosure)
- Refresh-cadence calendar
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Policy memo refresh | annually | CFO + Controller + Auditor | new primitive |
| Variable-consideration estimates reassessment | quarterly | Controller + CFO | estimate change >10% |
| Constraint reassessment | quarterly | Controller + CFO | constraint change |
| Principal-vs-agent reassessment | quarterly | Controller + CFO | service flow change |
| Breakage estimate reassessment | quarterly | Controller | historical pattern change |
| Contract-template / memo divergence audit | annually | Legal + Controller | divergence found |
| Disclosure language refresh | annually | Controller + Auditor | year-end |

## References

- `references/saas-agent-rev-rec-policy-memo-template.md` — meta template (extends operational skill template)
- `skills/10-financial-projections/saas-agent-revenue-recognition/SKILL.md` — operational rev-rec
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — liability side
- `skills/10-financial-projections/saas-agent-sla-cogs-treatment/SKILL.md` — COGS / contra-revenue
- `skills/meta-accounting-finance-review/SKILL.md` — accounting review gate
- `skills/meta-agent-sla-financial-controls/SKILL.md` — financial controls
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit
- `book-extractions/accounting-bookkeeping-finance-controls-extraction.md` — controls

## Africa / Uganda Application Notes

- **IFRS in African markets** — KE, NG, ZA, UG, TZ, RW, GH use IFRS; EG uses EAS with IFRS convergence; the policy memo should be written under IFRS 15 unless the company also reports under US GAAP
- **Local audit firm coaching** — where Big-4 not appointed, mid-tier (BDO, RSM, Mazars, Grant Thornton) firms may need the memo template; provide it
- **VAT / recognition timing reconciliation** — must be explicit in the memo (VAT on prepayment under most African VAT regimes; revenue on consumption)
- **WHT treatment** — Uganda 6% (Sched 6), Kenya variable, Nigeria 5%, South Africa none, Rwanda variable — receivable shown net; revenue gross-up
- **Public-sector receivables collectability** — collectability constraint may defer recognition where DSO >120 days
- **DFI / multilateral DD review** — IFC / AfDB / FMO will request the memo specifically
- **Sovereign-AI procurement** — local-currency pricing with USD index; treat USD adjustment as variable consideration; constrain
- **FX revaluation** — IAS 21 / ASC 830; non-operating; not part of revenue recognition itself

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Agent revenue-recognition memo decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to recognising outcome, credit, or SLA revenue before the obligation is satisfied. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the agent revenue-recognition memo; drafting a policy memo for controller and auditor review is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If executed contracts and pricing primitives cannot be obtained, return a qualified agent revenue-recognition memo covering only the checks that remain supportable. Leave this decision unresolved: the recognition trigger for each performance obligation. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: the recognition trigger for each performance obligation | Record the conclusion, source trail, owner, and review trigger in the agent revenue-recognition memo. | Risk of recognising outcome, credit, or SLA revenue before the obligation is satisfied |
| Material evidence conflicts or remains uncertain | Compare the contract wording against each plausible recognition treatment and send the unresolved conclusion to the controller or auditor. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: executed contracts and pricing primitives | Mark the decision on the recognition trigger for each performance obligation `not assessed` in the agent revenue-recognition memo, and send it to the controller and appointed auditor. | Otherwise, the work risks recognising outcome, credit, or SLA revenue before the obligation is satisfied |

## Quality Standards


Accept the agent revenue-recognition memo only when evidence is sufficient for this decision: the recognition trigger for each performance obligation. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of recognising outcome, credit, or SLA revenue before the obligation is satisfied.

## Worked Example


A contract bills prepaid credits that expire and also promises outcome refunds. Map the obligations and variable consideration separately; do not approve the memo until contract wording, billing events, and ledger entries agree.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the agent revenue-recognition memo, using the reporting basis and effective date supported by executed contracts and pricing primitives. Reconcile the treatment to the model and narrative, and have the controller and appointed auditor review the treatment, reconciliation, and exposure to this risk: recognising outcome, credit, or SLA revenue before the obligation is satisfied.

<!-- dual-compat-end -->
