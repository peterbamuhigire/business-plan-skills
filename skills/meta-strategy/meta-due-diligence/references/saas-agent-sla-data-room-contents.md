---
source: Agent SLA + commercial business-plan audit (2026); 2024-2026 institutional / DFI / auditor DD practice; engine synthesis
frameworks: [SLA data-room section index; evidence completeness checklist; DD response timing]
skill: meta-due-diligence
cross-reference: [saas-agent-data-room-contents, saas-agent-sla-bankability-checklist, saas-agent-investor-narrative-on-sla, meta-agent-sla-financial-controls]
---

# SaaS Agent SLA Data-Room Contents — Reference Index

The SLA section sits inside the broader agent data room (`saas-agent-data-room-contents.md`). It is a distinct evidence cluster that institutional, DFI, strategic, and auditor DD teams expect populated for any agent business carrying SLA commitments.

---

## Section Index (12 evidence clusters)

### 1. SLA Policy Memo

- Auditor-ready policy declaration (per pricing primitive)
- Revenue-recognition treatment (per ASC 606 / IFRS 15 5-step)
- SLA-credit accrual policy
- Refund-reserve policy (if outcome pricing)
- Deferred-revenue policy (if prepaid credits)
- Cross-reference to `meta-agent-revenue-recognition-policy`

**Document.** `sla-policy-memo-v{n}.pdf` + redline history.

---

### 2. Trailing 12-Quarter SLA Performance Dashboard

- Per dimension: uptime, accuracy, response time p50 / p95 / p99, DoD compliance, MTTR, sev-1 incident count
- Per customer / per SLA tier / per sector disaggregation
- Trend chart against commitment line
- Variance-from-plan explanatory notes

**Document.** `sla-performance-dashboard.xlsx` + monthly board-pack screenshots.

---

### 3. Reserve Methodology + True-Up History

- SLA-credit reserve methodology memo
- Refund-reserve methodology memo
- Formula (trailing credit ratio × forward agent revenue × adjustment factor) with worked example
- Quarterly true-up history (actuals vs reserve drawn)
- Auditor concurrence letter
- Methodology change-log

**Documents.** `sla-credit-reserve-methodology.pdf`, `refund-reserve-methodology.pdf`, `reserve-true-up-history.xlsx`, `auditor-concurrence-letter.pdf`.

---

### 4. Dispute Log + Resolution History

- Dispute register (count, customer, amount, age, status)
- Resolution timeline per dispute
- Escalation history (CS → Legal → Court)
- Gaming-detection flags + investigation outcomes
- Counter-party verification log

**Document.** `dispute-log.xlsx` (redacted where contractually required).

---

### 5. Audit-Firm Engagement Letter + Reports

- Auditor engagement letter
- SOC1 / SOC2 reports covering SLA-credit and reserve controls
- Internal controls report (ICFR)
- Audit-firm comment letters

**Documents.** Audit firm correspondence, SOC reports.

---

### 6. Customer SLA Contracts (Redacted)

- Minimum 5 representative contracts (mix of customer size / sector / SLA tier)
- SLA schedule excerpts highlighted
- SLA-credit cap clauses highlighted
- Vendor-cost pass-through clauses highlighted
- FX-corridor clauses highlighted (where applicable)
- Outcome-definition language (if outcome pricing)
- Counter-party verification language (if outcome pricing)
- Dispute-resolution clauses

**Documents.** `contract-{customer-id}-redacted.pdf` x N.

---

### 7. Regulator Correspondence on SLA

(Where sector regulator engaged)

- Consultation responses filed
- Regulator-engagement correspondence
- Pre-clearance letters (where granted)
- Sector body submissions
- Industry working-group participation evidence

**Documents.** `regulator-{name}-correspondence.pdf` x N.

---

### 8. Insurance Certificates Covering SLA Exposure

- E&O / professional indemnity certificate
- Cyber-insurance certificate
- Business-interruption certificate
- AI-specific policy where carrier offers (Munich Re, Beazley, Tokio Marine, AIG, Allianz, Chubb, AXA-XL)
- Self-insurance reserve memo (where insurance unavailable or insufficient)
- Carrier-exclusion summary

**Documents.** `insurance-certificate-{policy}.pdf` x N, `self-insurance-reserve-memo.pdf`.

---

### 9. SLA Stress-Test Scenarios + Financial Impact

- Catastrophic SLA breach scenario impact
- Foundation-model cost shock scenario impact
- Customer-gaming scenario impact
- Regulator-mandated SLA tightening scenario impact
- Reserve depletion scenario impact
- Outcome-pricing refund cascade scenario impact
- Insurance-carrier exclusion scenario impact
- Sovereign-AI provider pass-through scenario impact

Cross-reference: `meta-financial-stress-test/references/saas-agent-sla-stress-test-scenarios.md`.

**Document.** `sla-stress-test-scenarios.pdf` + supporting model.

---

### 10. SLA Telemetry Architecture Overview

- Telemetry system architecture diagram
- Data flow: from agent runtime → metrics → SLA computation → alerting → credit calculation
- Audit-log architecture
- Integrity controls (tamper-evident logging; hash-chained records)
- Telemetry uptime / availability metrics
- Vendor / open-source components used
- Cross-reference to engineering-side runbook (paired engineering session)

**Document.** `sla-telemetry-architecture.pdf`.

---

### 11. SLA Cadence + Governance Document

- Weekly SLA review cadence + owners
- Monthly reserve-adequacy review cadence + owners
- Quarterly SLA policy review + auditor true-up
- Annual SLA strategy review (Board)
- Trigger-replan thresholds
- Cross-reference to `meta-living-plan-governance/references/agent-cadence-table.md`

**Document.** `sla-governance-cadence.pdf`.

---

### 12. SLA Investor Communications History

- Pitch-deck SLA slide history (versions over rounds)
- Quarterly investor-update SLA block (last 4-8 quarters)
- Board-pack SLA section history
- Major-investor SLA-specific responses
- Catastrophic-event post-mortems shared with investors

**Documents.** `investor-comms-sla-history.pdf` + redacted update snippets.

---

## Evidence-Completeness Checklist

| Cluster | Critical for | Status (✅ / 🟡 / ❌) |
|---|---|---|
| 1. Policy memo | All rounds + auditor | |
| 2. Performance dashboard | All rounds | |
| 3. Reserve methodology | Series A+ / DFI | |
| 4. Dispute log | Series A+ / DFI | |
| 5. Audit-firm engagement | Series B+ / DFI / strategic | |
| 6. Customer contracts | All rounds | |
| 7. Regulator correspondence | Regulated-sector rounds | |
| 8. Insurance certificates | Series A+ / DFI | |
| 9. Stress scenarios | All rounds | |
| 10. Telemetry architecture | Series A+ technical DD | |
| 11. Cadence + governance | All rounds | |
| 12. Investor comms history | Series B+ |

---

## DD Response Timing Targets

| DD request | Response target |
|---|---|
| Trailing performance dashboard | <24 hours |
| Reserve methodology memo | <48 hours |
| Specific dispute query | <72 hours |
| Catastrophic-scenario walkthrough | <72 hours (with CFO availability) |
| Auditor concurrence letter | <48 hours |
| Insurance certificate | <24 hours |
| Customer-contract excerpt | <72 hours (legal redaction) |
| Regulator correspondence | <72 hours |

Slow response signals immaturity; data-room completeness is read as discipline evidence.

---

## Integration with broader DD

- The SLA section is a **subset** of the agent data room (`saas-agent-data-room-contents.md`)
- The SLA section is **scored** by the bankability checklist (`saas-agent-sla-bankability-checklist.md`)
- The SLA section **populates** the valuation overlay (`saas-agent-sla-valuation-adjustments.md`)
- The SLA section **evidences** the investor narrative (`saas-agent-investor-narrative-on-sla`)

---

## Cross-References

- `skills/meta-due-diligence/SKILL.md` — DD parent
- `skills/meta-due-diligence/references/saas-agent-data-room-contents.md` — agent data room parent
- `skills/meta-bankability-scoring/references/saas-agent-sla-bankability-checklist.md` — scorecard
- `skills/meta-valuation/references/saas-agent-sla-valuation-adjustments.md` — valuation overlay
- `skills/11-funding-request/saas-agent-investor-narrative-on-sla/SKILL.md` — narrative
- `skills/meta-agent-sla-financial-controls/SKILL.md` — controls evidence
- `skills/meta-financial-stress-test/references/saas-agent-sla-stress-test-scenarios.md` — stress scenarios
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Local audit firm engagement letters** acceptable for Cluster 5 where Big-4 unavailable; document scope and limitations
- **Sovereign-AI provider contracts** belong in Cluster 6 (mandated dependency disclosure) and Cluster 10 (telemetry coupling)
- **Mobile-money settlement diagnostics** in Cluster 10 — settlement-success rate as adjacent metric to SLA performance
- **Public-sector SLA history** in Cluster 12 — political-sensitivity considerations on disclosure; coordinate with public-sector customer
- **FX-corridor reserve disclosures** in Cluster 3 — explicit reserve currency vs cost currency table
- **DFI-specific DD list** — IFC / AfDB / FMO / BII / Proparco specific DD checklists frequently emphasise Cluster 1, 3, 7, 9, 11
- **Insurance carrier scarcity** — Cluster 8 self-insurance reserve memo is acceptable substitute where carriers unavailable, but reserve adequacy must be transparent
