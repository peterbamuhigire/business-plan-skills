---
name: meta-agent-revenue-recognition-policy
description: Meta policy-declaration discipline for agent revenue recognition — auditor-ready policy memo template per pricing primitive (per-resolution, per-outcome, hybrid, prepaid credits, SLA tier). Per-primitive: performance obligation, transaction-price allocation, recognition trigger, variable-consideration treatment, principal-vs-agent, breakage, refund, contract modification. Use when the plan must declare its rev-rec policy at audit-ready standard.
---

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

- Pricing primitives in scope (from `saas-agent-pricing-strategy`)
- Contract templates (from proposal session)
- Standalone selling price evidence (where available)
- Variable-consideration components inventory
- Principal-vs-agent indicators per service flow
- Audit firm (if appointed)
- Prior-period policy memo (if updating)
- Reporting framework (ASC 606 / IFRS 15 / both)

## Workflow

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

## Outputs

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
