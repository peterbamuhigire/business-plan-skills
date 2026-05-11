---
source: Agent-products business-plan audit (2026); 2024-2026 agent ops practice; engine synthesis
frameworks: [Agent operations runbook; Kill-switch; Audit cadence; Drill cadence; Incident runbook]
skill: 08-operations-plan
cross-reference: [saas-agent-risk-and-stress-test, saas-agent-product-strategy-and-roadmap, meta-agent-bankability-and-investor-readiness]
---

# Agent Operations Runbook — Summary

For Section 08 of any agent-product plan. Full operations covered in the agent product / risk / safety skills; this summary anchors Section 08 to the agent operating discipline.

## 1. Kill-Switch

- **Design**: per-agent and global kill-switch reachable within 60 seconds; multiple authorised triggers (AI Safety Lead, CTO, CEO, on-call)
- **Drill**: monthly; record outcome; participants signed
- **Customer-visible kill**: customer can pause agent in own tenant within 60s
- **Cascade**: kill-switch suspends new tasks; in-flight tasks complete or hand off to HITL (configurable per action class)

## 2. Audit-Log

- **Immutability**: append-only store; cryptographic hash chain or equivalent
- **Retention**: 3-7+ years for regulated; longer if sectorally required
- **Queryability**: regulator-on-demand within agreed SLA (typically <72h)
- **Review cadence**: monthly review by Compliance + AI Safety Lead
- **Findings log**: any finding logged with severity and remediation owner

## 3. Drill Cadence

- **Monthly safety drill**: kill-switch, audit-log query, HITL escalation, incident response
- **Quarterly tabletop exercise**: one scenario rotated (provider 5x; tool outage; intervention 2x; irreversibility incident; foundation-model deprecation; regulator freeze; prompt-injection mass)
- **Annual full simulation**: end-to-end with customer-impacting drill (with customer notification)
- **Attendance**: signed; missed drills logged as governance failure

## 4. Incident Runbook

- **Detection**: monitoring alerts; eval-suite regression; customer report; audit-log anomaly; tool-vendor outage
- **Triage**: sev-1 / sev-2 / sev-3 classification within 30 minutes of detection
- **Containment**: kill-switch if sev-1; isolate affected tenants if sev-2
- **Communication**: customers affected notified within agreed SLA; investors notified within 48h of sev-1 confirmation
- **Resolution**: root-cause + fix + rollback verification
- **Postmortem**: blameless; within 14 days for sev-1; within 30 days for sev-2
- **Remediation**: tracked in decision log; ownership and deadline
- **Customer-credit / indemnity**: SLA credits + indemnity per contract; reserve drawn from irreversibility reserve if Class D

## 5. Eval-Loop Operations

- **Offline eval**: daily on golden set
- **Online eval / sampling**: continuous on production traffic at agreed sample rate
- **Human-correction signal**: reviewer corrections feed eval set
- **Regression detection**: any -3pp on any metric triggers alert; -5pp triggers freeze of promotion
- **Versioning**: eval suite versioned with agent versions

## 6. HITL Operations

- **Reviewer training**: onboarding programme + monthly calibration sessions
- **Reviewer workbench**: purpose-built tool with audit-log integration
- **Reviewer-load capacity planning**: per agent / per tenant / per shift; redeploy as autonomy expands
- **Quality discipline**: reviewer-correction sampling cross-reviewed; reviewer-agreement metric tracked
- **Reviewer wellbeing**: especially for high-stake / distressing content; mental-health support

## 7. Provider Watch

- **LLM provider pricing**: weekly scan
- **LLM provider deprecation notices**: continuous monitoring
- **Tool vendor changelogs**: continuous monitoring
- **Channel aggregator status**: continuous monitoring
- **Vendor concentration**: quarterly review; alert if >60% on single vendor in any layer

## 8. Regulator Engagement Operations

- **Engagement calendar**: scheduled touchpoints with each regulator
- **Submissions log**: tracked; deadlines monitored
- **Inquiry response**: dedicated owner; SLA per regulator type
- **New-guidance watch**: monthly scan
- **Sectoral approval renewals**: tracked

## 9. Reporting Operations

- Monthly investor update agent block (see `meta-agent-board-and-investor-reporting`)
- Quarterly board pack agent section
- Continuous decision log
- Quarterly bankability rescore
- Quarterly stress-test refresh

## 10. Anti-Patterns

- Kill-switch designed but never drilled
- Audit-log only for engineering debugging
- Drills skipped due to capacity
- Sev-1 communicated at next board meeting (too late)
- Reviewer wellbeing ignored
- Provider watch only when provider sends notice (passive)
- Regulator engagement only when summoned (reactive)
- Decision log not maintained

## 11. Cross-References

- Risk register: `saas-agent-risk-and-stress-test/references/saas-agent-risk-register-template.md`
- Stress: `saas-agent-stress-test-scenarios.md`
- Reporting: `meta-agent-board-and-investor-reporting`
- Bankability: `meta-agent-bankability-and-investor-readiness`
