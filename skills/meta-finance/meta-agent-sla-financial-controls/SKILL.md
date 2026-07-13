---
name: meta-agent-sla-financial-controls
description: Use when the agent business has SLA-credit, refund, prepaid-credit, or outcome-pricing variable revenue. Use financial projections for model construction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->


# Meta — Agent SLA Financial Controls Skill

## Workflow

1. Confirm the decision audience, scope, current evidence, and applicable finance doctrine.
2. Apply the ordered domain analysis below and reconcile every calculation to its source.
3. Record the decision, exceptions, reviewer, and next evidence action before release.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the SLA financial-control matrix and that the decision concerns which credit and reserve controls are mandatory.
- **Stop condition:** halt the affected conclusion if required evidence is missing (SLA credit terms, reserve method, and approver roles) or if the work could lead to this identified risk: unapproved credits or an unsupported reserve reaching the ledger.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Overview

Bankability scorecards (DFI, institutional) increasingly check **financial-control maturity around variable revenue**. SLA credits, outcome refunds, prepaid breakage, and dispute resolution are all variable-revenue mechanisms that without controls expose the business to:

- Unapproved credits drain revenue
- Inconsistent credit decisions invite gaming
- Reserve methodology drift without governance produces audit findings
- Dispute backlog accumulates quietly
- SOC1 / SOC2 attestation fails for financial reporting controls

This meta-skill installs the SLA financial-control discipline as a documented, named, owned, auditable system.

## Use When

- The agent business has SLA-credit, refund, prepaid-credit, or outcome-pricing variable revenue
- A SOC1 / SOC2 attestation is being pursued
- Institutional / DFI DD has asked about financial controls
- Bankability scorecard checks control maturity
- An auditor / internal-audit function is being installed
- Cross-loaded with `meta-agent-revenue-recognition-policy`, `saas-agent-deferred-revenue-and-credit-reserves`, `meta-accounting-finance-review`

## Do Not Use When

- The agent business has no variable revenue (all flat subscription)
- The plan is pre-revenue and controls are premature (use directional treatment)


- Route to `10-financial-projections` instead when the task is to construct the underlying model.
## Required Inputs

| Input artefact | Source / provider | Required? | If missing |
|---|---|---:|---|
| SLA, refund, prepaid-credit, and reserve terms | Signed contracts, billing owner, finance controller | Yes | Stop control design and request the governing terms. |
| Approval roles and system capabilities | Approved org chart, ERP or billing administrator | Yes | Return a qualified control-gap assessment only. |
| Dispute and credit history | Finance records and customer-success register | Conditional | Mark trend and reserve calibration not assessed. |

- SLA terms and credit policy
- Refund policy
- Prepaid-credit terms
- Dispute history (where available)
- Reserve methodology (per `saas-agent-credit-reserve-methodology.md`)
- Org chart and role inventory (CFO, Controller, Head of CS, Legal, Customer Success Managers)
- ERP / billing-system capability (does it enforce approvals?)
- Auditor / internal-audit appointment status

### 1. Design the SLA-credit approval workflow

Per `references/saas-agent-sla-financial-controls-policy.md`:

| Credit size | Approver | Documentation required |
|---|---|---|
| <$500 | Customer Success Manager (with audit trail) | Credit reason code; affected customer; breach evidence |
| $500-$5,000 | Head of CS | Above + customer comms; cause analysis |
| $5,000-$25,000 | CFO + Head of CS | Above + reserve impact; cause analysis |
| >$25,000 or material to a customer's annual fee | CEO + CFO + Legal | Above + remediation plan |
| Pattern / multiple sev-1 affecting many customers | Board / audit committee notification | Above + plan for board pack |

Document:
- Authorities matrix
- Approval system (ERP / billing workflow)
- Evidence requirements per level
- Approval-cycle SLA (response time)

### 2. Design refund approval workflow

Similar to credits:

| Refund size | Approver |
|---|---|
| <$500 | Customer Success Manager |
| $500-$5,000 | Head of CS |
| $5,000-$25,000 | CFO |
| >$25,000 | CEO + CFO + Legal |

### 3. Document the reserve methodology governance

- Methodology document signed by CFO
- Quarterly true-up by Controller + CFO
- Annual review by external auditor
- Reserve roll-forward reconciled at month-end close
- Variances documented and explained
- Methodology change requires CFO approval + auditor concurrence

### 4. Design the dispute escalation chain

| Dispute stage | Owner | Timeline |
|---|---|---|
| Initial customer claim | Customer Success Manager | Respond within 48 hours |
| Investigation | Customer Success Manager + Head of Agent | 5 working days |
| Resolution / settlement | Head of CS | 7 working days from claim |
| Escalation if unresolved | CFO + Legal | 14 working days |
| Escalation to mediation / arbitration | CEO + Legal | 30 working days |
| Litigation | Legal + CEO + Board notification | As required |

Each stage:
- Documented evidence requirements
- Decision authority
- Settlement-authority threshold
- Audit-log evidence captured

### 5. Implement segregation of duties

- Credit / refund approval: customer-facing (CS / Head of CS / CFO / CEO)
- Credit / refund accounting entry: Controller / Accounts
- Reserve calculation: Controller
- Reserve approval: CFO
- Reserve audit: external auditor + audit committee

No single role both approves and books. Document the segregation.

### 6. Implement audit trail

- Every credit / refund logged in the ticketing / billing system
- Log captures: customer, amount, currency, reason code, breach evidence, approver, approval date, processing date, ERP entry reference
- Audit log is immutable
- Periodic integrity verification

### 7. Wire to SOC1 / SOC2

Map controls to SOC1 / SOC2 control categories:
- Control environment (org structure, segregation)
- Risk assessment (variable-revenue risk register)
- Control activities (approvals, reconciliations, segregation)
- Information and communication (audit trail, reporting)
- Monitoring (variance review, quarterly true-up)

Document control mapping for attestation pack.

### 8. Wire to financial reporting controls (ICFR)

For companies pursuing IPO or institutional rounds requiring ICFR-equivalent discipline:
- Document control narratives for each SLA-related process
- Test controls quarterly
- Remediate exceptions
- Annual management assertion

### 9. Wire to insurance and indemnity

- Insurance coverage scope tested against control posture
- Self-insurance reserve sized for coverage gaps
- Indemnity caps in contracts cross-checked

### 10. Wire to living-plan governance

Per cadence below.

## Quality Bar

- SLA-credit approval workflow documented with thresholds and evidence requirements
- Refund approval workflow documented
- Reserve methodology governance documented (CFO sign-off; auditor review)
- Dispute escalation chain documented with timelines
- Segregation of duties documented
- Audit trail captured and immutable
- SOC1 / SOC2 control mapping (where applicable)
- ICFR readiness (where applicable)
- Insurance scope tested
- A sceptical audit committee chair would accept the controls

## Anti-Patterns

- Credits approved verbally without audit trail
- Credit approval threshold absent (all credits informally approved)
- Reserve methodology in a spreadsheet without governance
- Dispute backlog without escalation discipline
- Segregation of duties violated (CS approves AND books)
- No SOC1 mapping when institutional round in scope
- Audit trail mutable
- Insurance scope assumed without testing
- "We trust each other" as the control framework — fails first DD


- Applying the wrong neighbouring route to meta agent sla financial controls. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Sla Financial Controls deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- SLA-credit approval workflow document
- Refund approval workflow document
- Reserve methodology governance document
- Dispute escalation chain document
- Segregation-of-duties matrix
- Audit-trail design
- SOC1 / SOC2 mapping (where applicable)
- ICFR readiness assessment (where applicable)
- Insurance / indemnity cross-check
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Credit / refund audit-trail review | weekly | Controller | missing evidence |
| Reserve roll-forward reconciliation | monthly | Controller + CFO | unexplained variance |
| Reserve methodology true-up | quarterly | CFO + Controller + Auditor | methodology change |
| Dispute backlog review | weekly | Head of CS + Legal | >5 disputes aged >7 days |
| Segregation-of-duties test | quarterly | Internal audit / Controller | exception |
| Control narrative refresh | annually | CFO + Internal audit | process change |
| SOC1 / SOC2 attestation | annually | CFO + SOC auditor | gap |
| Insurance coverage review | semi-annually | CFO + Legal | exclusion |
| Audit committee report | quarterly | CFO + Audit Committee | findings |

## References

- `references/saas-agent-sla-financial-controls-policy.md` — full controls policy
- `skills/meta-agent-revenue-recognition-policy/SKILL.md` — policy declaration
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — reserves
- `skills/10-financial-projections/saas-agent-sla-cogs-treatment/SKILL.md` — classification
- `skills/meta-accounting-finance-review/SKILL.md` — accounting review parent
- `skills/12-risk-analysis/saas-agent-sla-risk/SKILL.md` — risk register
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit
- `book-extractions/accounting-bookkeeping-finance-controls-extraction.md` — controls reference

## Africa / Uganda Application Notes

- **Local audit firm acceptance** — KPMG, PwC, Deloitte, EY accept SOC1-style controls directly; mid-tier firms may benefit from policy walk-through
- **DFI DD on controls** — IFC / AfDB / FMO / BII expect control narratives + segregation-of-duties evidence
- **ERP / billing system capability** — local accounting software (Sage, QuickBooks, Tally, Pastel) may not enforce approval workflow natively; use ticketing-system + manual reconciliation
- **Mobile-money settlement audit-trail** — MoMo / M-Pesa transaction logs are immutable and auditor-acceptable; useful for refund-trail evidence
- **Public-sector dispute escalation** — disputes with public-sector customers go through procurement / accounting general; legal capacity required; reserve appropriately
- **Sovereign-AI compliance overlap** — sovereign-AI tenders often require local-citizen-headcount audit; SLA control system should map to local compliance discipline
- **Insurance availability** — AI E&O thin in Africa; self-insurance reserve essential; document the gap transparently
- **Currency-of-record** — controls must address local-currency credit issuance vs USD reporting reconciliation

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| SLA financial-control matrix decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to unapproved credits or an unsupported reserve reaching the ledger. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the SLA financial-control matrix; drafting control narratives and approval thresholds is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If SLA credit terms, reserve method, and approver roles cannot be obtained, return a qualified SLA financial-control matrix covering only the checks that remain supportable. Leave this decision unresolved: which credit and reserve controls are mandatory. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which credit and reserve controls are mandatory | Record the conclusion, source trail, owner, and review trigger in the SLA financial-control matrix. | Risk of unapproved credits or an unsupported reserve reaching the ledger |
| Material evidence conflicts or remains uncertain | Walk one credit, refund, and reserve true-up through the proposed approvals before accepting the control design. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: SLA credit terms, reserve method, and approver roles | Mark the decision on which credit and reserve controls are mandatory `not assessed` in the SLA financial-control matrix, and send it to the controller and SLA control owner. | Otherwise, the work risks unapproved credits or an unsupported reserve reaching the ledger |

## Quality Standards


Accept the SLA financial-control matrix only when evidence is sufficient for this decision: which credit and reserve controls are mandatory. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of unapproved credits or an unsupported reserve reaching the ledger.

## Worked Example


A customer-success manager can issue large SLA credits directly in billing. The control matrix introduces evidence, approval, and reserve true-up steps, then tests them on a sample credit before release.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the SLA financial-control matrix, using the reporting basis and effective date supported by SLA credit terms, reserve method, and approver roles. Reconcile the treatment to the model and narrative, and have the controller, control owner, and appointed auditor review the treatment, reconciliation, and exposure to this risk: unapproved credits or an unsupported reserve reaching the ledger.

<!-- dual-compat-end -->
