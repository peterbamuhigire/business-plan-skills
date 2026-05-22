---
source: SOC1 / SOC2 control practice; COSO ICFR; Big-4 SaaS controls practice; engine synthesis from agent-SLA-commercial audit (2026)
frameworks: [Approval-authority matrix; Segregation of duties; Audit trail; Dispute-escalation chain; Reserve governance; SOC1 mapping]
skill: meta-agent-sla-financial-controls
cross-reference: [meta-agent-revenue-recognition-policy, saas-agent-credit-reserve-methodology, saas-agent-sla-cogs-policy]
---

# SLA Financial Controls Policy — Full Document

## 1. Purpose

This policy establishes financial controls over variable-revenue mechanisms in the agent business: SLA credits, outcome refunds, prepaid-credit breakage, and dispute resolution. Controls are designed to:

- Prevent unapproved revenue reductions
- Ensure consistent credit / refund decisions
- Govern reserve methodology
- Maintain audit-quality evidence
- Enable SOC1 / SOC2 attestation
- Satisfy ICFR where applicable

## 2. Approval authority matrix — SLA credits

| Credit size (USD) | Approver | Evidence required | Cycle SLA |
|---|---|---|---|
| <$500 | Customer Success Manager | Reason code; customer ID; breach evidence (telemetry / log) | 24 hours |
| $500 - $5,000 | Head of Customer Success | Above + customer comms log; cause analysis | 48 hours |
| $5,001 - $25,000 | CFO + Head of CS | Above + reserve impact note; cause analysis with engineering input | 5 working days |
| >$25,000 OR >25% of customer's annual fee | CEO + CFO + Legal | Above + remediation plan; insurance notification | 10 working days |
| Multi-customer pattern (>5 customers, >$10k aggregate) | CEO + CFO + Board (notification) | Above + board pack item; PR plan | 14 working days |

Decisions logged in the billing / ticketing system. Approval cannot be retroactive without secondary review.

## 3. Approval authority matrix — refunds

| Refund size (USD) | Approver | Evidence required |
|---|---|---|
| <$500 | Customer Success Manager | Reason code; outcome attempt log |
| $500 - $5,000 | Head of CS | Above + cause analysis |
| $5,001 - $25,000 | CFO | Above + reserve impact |
| >$25,000 | CEO + CFO + Legal | Above + remediation |

## 4. Approval authority matrix — concession credits

(Goodwill / commercial concessions not tied to SLA breach)

| Size | Approver |
|---|---|
| <$1,000 | Head of CS |
| $1,000 - $10,000 | CFO + Head of CS |
| >$10,000 | CEO + CFO |

Concession credits classified separately for disclosure (G&A or contra-revenue, per `saas-agent-sla-cogs-policy.md`).

## 5. Reserve methodology governance

| Element | Owner | Review |
|---|---|---|
| Methodology document | CFO + Controller | CFO sign-off; auditor review (annually) |
| Quarterly true-up | Controller | CFO approval; audit committee notification on material change |
| Reserve roll-forward | Controller | Monthly close discipline; reconciled to ledger |
| Reserve sensitivity | CFO + Controller | Quarterly + on trigger |
| Methodology change | CFO | Audit committee notification; auditor concurrence if material |
| Adjustment factor | CFO + Controller | Quarterly review with documented reasoning |
| Trailing-period actuals | Controller | Monthly refresh |

Changes documented with reasoning. Cumulative-catch-up entries booked through revenue.

## 6. Dispute escalation chain

| Stage | Owner | Timeline | Evidence |
|---|---|---|---|
| Receipt of claim | Customer Success Manager | Acknowledge within 24 hours | Customer comm; claim summary |
| Investigation | CSM + Head of Agent | 5 working days | Audit log; telemetry; eval result |
| Resolution offer | Head of CS | 7 working days | Settlement proposal; approval |
| Escalation if rejected | CFO + Legal | 14 working days | Counter-proposal; legal review |
| Mediation / arbitration | CEO + Legal | 30 working days | Mediation request; legal pack |
| Litigation | Legal + CEO + Board (notified) | As triggered | Legal pack; insurance notification |

Each dispute logged with stage tracking; aged disputes escalated automatically.

## 7. Segregation of duties matrix

| Function | Approver | Booker | Reconciler | Reviewer |
|---|---|---|---|---|
| SLA credit issuance | CSM / Head of CS / CFO / CEO (per matrix) | Controller / Accounts | Controller | CFO |
| Refund issuance | CSM / Head of CS / CFO / CEO | Controller / Accounts | Controller | CFO |
| Reserve calculation | Controller | Controller | CFO | Auditor (annual) |
| Reserve approval | CFO | n/a | Auditor (annual) | Audit committee |
| Dispute settlement | Per dispute chain | Controller / Legal | Controller | CFO + Legal |
| Concession credit | Head of CS / CFO / CEO | Controller / Accounts | Controller | CFO |

**No single role both approves and books.** This is the bright line.

## 8. Audit trail design

Every credit, refund, concession, or dispute action logged with:
- Date and time
- Customer ID
- Amount and currency
- Reason code (controlled vocabulary)
- Breach / outcome evidence reference (telemetry / log / eval / counter-party)
- Approver(s) with approval date
- Booker with booking date
- ERP / billing reference
- Settlement / processing date

Log fields immutable after entry. Corrections by reversing entry with linkage. Periodic integrity verification (hash chain or equivalent).

## 9. SOC1 / SOC2 mapping (illustrative)

| SOC1 / SOC2 control category | This policy addresses |
|---|---|
| Control environment | Authority matrix; segregation matrix |
| Risk assessment | Variable-revenue risk register (cross-load) |
| Control activities | Approval workflow; segregation; reconciliation; dispute chain |
| Information and communication | Audit trail; reporting cadence; board notification |
| Monitoring | Monthly close discipline; quarterly true-up; annual audit |

## 10. ICFR readiness (where applicable)

- Control narratives per process (credit issuance, refund, reserve, dispute)
- Quarterly control testing
- Exception remediation
- Management assertion annually
- External audit attestation

## 11. Insurance and indemnity controls

- Annual insurance policy review (CFO + Legal)
- Coverage scope tested against control posture
- Self-insurance reserve sized for coverage gaps
- Indemnity caps in contracts cross-checked
- Sub-limits documented

## 12. Reporting

Monthly:
- Credit / refund activity summary (count, amount, by tier, by reason)
- Reserve roll-forward
- Dispute backlog
- Open exceptions

Quarterly:
- Audit committee pack (above + methodology review)
- SOC1 / SOC2 progress

Annually:
- External audit pack
- ICFR management assertion (where applicable)

## 13. Worked example — SLA credit issuance

Scenario: Customer X experiences a 99.5% uptime month (vs 99.9% Gold SLA); credit = 10% of monthly fee = $500.

| Step | Owner | Action |
|---|---|---|
| 1 | Customer Success Manager | Logs claim; gathers evidence (uptime telemetry) |
| 2 | CSM | Calculates credit per SLA: $500; reason code "uptime-breach" |
| 3 | CSM | Approves (within <$500 threshold... wait, $500 is the threshold; goes to Head of CS) |
| 4 | Head of CS | Reviews evidence; approves; signs off |
| 5 | Controller | Books credit: Dr Revenue $500; Cr Customer credit (a/r) $500 (or processes through billing) |
| 6 | Controller | Reconciles month-end: credit posted; reserve reduced; audit trail saved |
| 7 | CFO | Reviews monthly summary |

## 14. Africa / Uganda overlay

- **Local-currency credit issuance** — credit issued in local currency; reserve revalued in reporting currency (USD); FX gain/loss to non-operating
- **Mobile-money refund-issuance cost** — MoMo / M-Pesa transaction fee on refund (1-2.5%) booked as COGS
- **Public-sector dispute timelines** — public-sector disputes often exceed 30-day SLA in this policy; document the extension policy
- **VAT on credit issuance** — VAT-output adjusted for SLA credit (transaction-price reduction); reconcile monthly
- **Local audit firm coaching** — provide control walk-through; segregation of duties may be new concept for some firms
- **DFI / multilateral DD** — IFC / AfDB / FMO will request the policy document and a sample audit-trail extract
- **Sovereign-AI compliance overlap** — local-citizen / local-entity controls map alongside SLA controls
- **Insurance availability** — AI E&O thin; self-insurance reserve must reflect uncovered SLA exposure
