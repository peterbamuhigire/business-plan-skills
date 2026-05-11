---
name: meta-agent-sla-financial-controls
description: Financial controls for SLA economics — SLA-credit approval workflow with threshold-based authority; reserve methodology governance with quarterly true-up and auditor concurrence; dispute escalation with documented escalation chain; SOC1 financial-controls cross-link; audit trail of credits issued; segregation of duties between credit issuance and reserve accounting. Use when SLA economics are material and bankability / DD expects control maturity.
---

# Meta — Agent SLA Financial Controls Skill

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

## Required Inputs

- SLA terms and credit policy
- Refund policy
- Prepaid-credit terms
- Dispute history (where available)
- Reserve methodology (per `saas-agent-credit-reserve-methodology.md`)
- Org chart and role inventory (CFO, Controller, Head of CS, Legal, Customer Success Managers)
- ERP / billing-system capability (does it enforce approvals?)
- Auditor / internal-audit appointment status

## Workflow

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

## Outputs

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
