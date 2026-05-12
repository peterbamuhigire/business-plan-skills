---
source: Agent SLA + commercial business-plan audit (2026); engine synthesis
frameworks: [SLA-specific risk register; likelihood × impact × velocity scoring; reserve and control mapping]
skill: 12-risk-analysis/saas-agent-sla-risk
cross-reference: [saas-agent-risk-and-stress-test, meta-financial-stress-test, meta-agent-sla-financial-controls]
---

# SaaS Agent SLA Risk Register — Populated Template

Use this register in the risk-analysis section of any agent-product plan that carries SLA commitments. Each row covers the SLA-specific risks distinct from the broader agent risk register.

Scoring: **Likelihood** (1=rare, 5=near-certain); **Impact** (1=immaterial, 5=existential); **Velocity** (1=slow, 5=overnight). Treat the sum of likelihood × impact as risk score; velocity governs mitigation pace.

---

## 1. Catastrophic SLA breach event (sev-1 mass-credit)

**Description.** A single incident (model outage; tool partner outage; regional cloud incident; data-poisoning; cascading agent failure; sovereign-AI provider outage) triggers SLA breach across >5% of customers simultaneously, generating credit accrual that exceeds reserve.

**Likelihood.** 2-3 (annual probability material for any agent business at scale).
**Impact.** 4-5 (reserve depletion + reputational + dispute risk + churn signal).
**Velocity.** 5 (overnight financial impact).

**Mitigation.**
- Reserve sized for catastrophic scenario per `meta-financial-stress-test` SLA scenario set
- Per-event SLA-credit caps in contract (typically 30-50% of monthly fee)
- Insurance (E&O / cyber / business-interruption) covering residual where carriers permit
- Quarterly tabletop drill simulating catastrophic event
- Communications-ready customer template; legal-ready dispute template
- Provider-diversification where feasible (multi-LLM, multi-region)
- Post-event RCA + reserve adequacy true-up

**Reserve / control mapping.** SLA-credit reserve methodology must explicitly contemplate this scenario; financial controls must include CFO + CEO + Board notification triggers (typically credit accrual >120% of reserve drawn in any month).

**Cross-reference.** `saas-agent-risk-and-stress-test` covers operational sev-1; this row covers the financial-reporting and SLA-commercial dimension.

---

## 2. Foundation-model cost shock making SLA-tier pricing unviable

**Description.** Foundation-model provider raises blended pricing by >25% in a quarter (or deprecates a cheaper model forcing migration to a more expensive one); cost-floor for SLA-tier pricing rises above the contracted price; tier becomes unprofitable for the remainder of contract term.

**Likelihood.** 2-3 (observed multiple times 2023-2025).
**Impact.** 3-5 (margin compression; potential loss-making contracts; contract-repricing fights).
**Velocity.** 3-4 (60-90 day forward signal usually visible).

**Mitigation.**
- Vendor-cost pass-through clause in all contracts >12 months (with 60-day notice and defined trigger threshold)
- Multi-vendor / multi-model architecture allowing routing to cheaper provider
- Quarterly cost-floor stress test at provider 2x
- Forward-buy / committed-spend agreements with provider where available
- Renegotiation calendar tied to provider-pricing-change watch

**Reserve / control mapping.** Margin reserve where contracts lack pass-through clause; CFO watch on blended-cost metric.

---

## 3. Customer-side SLA gaming — false intervention reports / false outcome rejections

**Description.** Customer staff (or their procurement / vendor-management function) inflate intervention reports or reject outcomes to trigger SLA credits or refunds, reducing effective billing.

**Likelihood.** 2-3 (rising as outcome pricing spreads; correlates with poorly-defined outcome criteria).
**Impact.** 2-4 (revenue leakage 5-15% in worst cases; margin compression).
**Velocity.** 2 (gradual; quarter-on-quarter pattern).

**Mitigation.**
- Outcome-definition rigour at contract; counter-party verification clauses (third-party process / digital receipt / regulator confirmation)
- Per-customer intervention-rate and rejection-rate monitoring; deviation from cohort triggers investigation
- Dispute-escalation path with named owner on both sides
- Audit-log of intervention triggers; segregation between agent telemetry and customer-reported intervention
- Customer-success engagement before gaming hardens into dispute

**Reserve / control mapping.** Gaming-detection sits in `meta-agent-sla-financial-controls`; control includes monthly variance review.

---

## 4. Regulator-mandated SLA standard tightening

**Description.** Sector regulator (FCA, OCC, SEC, FDA, FFIEC, ICO, CBK, CMA, CBN, SEC-NG, SARB, FSCA, BoU, NDPC, EU AI Act technical standards bodies) mandates an SLA standard that exceeds current commitments; cost-of-quality investment required; existing contracts must be renegotiated or upgraded.

**Likelihood.** 2-3 (rising 2025-2027 in finance, healthcare, public-sector).
**Impact.** 3-4 (operating-margin compression; upgrade cost; non-compliance penalty risk).
**Velocity.** 2-3 (consultation usually 6-18 months forward).

**Mitigation.**
- Active regulator engagement (consultations, working groups, sector-body membership)
- Forward cost-of-quality budget for regulatory-driven upgrades
- Renewable-contract pricing triggers tied to regulator-mandated changes
- Investor communication of regulator-engagement progress (signals discipline)

**Reserve / control mapping.** Forward-cost-of-quality reserve in projection; CFO + General Counsel quarterly review.

---

## 5. SLA-credit accrual exceeding reserve

**Description.** Actual SLA credits issued exceed the provisioned reserve. Drivers: under-reserving; performance trend deteriorating; catastrophic event without reserve adjustment; reserve methodology stale.

**Likelihood.** 2-3 (common at early scaling; rare at maturity).
**Impact.** 2-3 (P&L surprise; auditor concern; investor question).
**Velocity.** 3 (quarter-on-quarter signal visible).

**Mitigation.**
- Reserve methodology documented and audited per `saas-agent-credit-reserve-methodology.md`
- Quarterly true-up cadence
- Monthly variance monitoring (actuals vs reserve drawn)
- Trigger thresholds: actuals >110% of reserve drawn → CFO review; >120% → Board notification
- Reserve adjustment with auditor concurrence before quarter close

**Reserve / control mapping.** `meta-agent-sla-financial-controls` — reserve true-up workflow.

---

## 6. Dispute backlog risk

**Description.** Dispute queue grows beyond service capacity; aged disputes escalate to legal; reputational and cash-tied-up impact.

**Likelihood.** 2-3 (correlates with contract growth + ambiguous outcome definitions).
**Impact.** 2-3 (cash conversion delay; legal cost; reputational).
**Velocity.** 2 (gradual).

**Mitigation.**
- Dispute-resolution SLA in contracts (e.g. respond within 7 days; resolve within 30)
- Customer-success staffing scaled to ARR growth + dispute-volume ratio
- Standard dispute-escalation playbook
- Legal-bench-strength sized to dispute volume

**Reserve / control mapping.** Customer-Success queue depth metric + aging-dispute metric in weekly cadence; legal-cost line in projection.

---

## 7. Outcome-pricing refund cascade

**Description.** Per-outcome agent product faces refund cascade where downstream verification systematically rejects outcomes after they were operationally executed; refund accrual exceeds refund reserve.

**Likelihood.** 2-3 (when outcome definitions weak or counter-party verification lags).
**Impact.** 3-4 (refund-reserve depletion; revenue restatement risk).
**Velocity.** 2-3.

**Mitigation.**
- Outcome-definition rigour at contract level
- Counter-party verification clauses (objective process; digital receipt; regulator-validated)
- Refund-reserve methodology per `saas-agent-refund-reserve-methodology.md`
- Quarterly outcome-attribution audit

**Reserve / control mapping.** Refund-reserve provision; CFO monthly review; auditor concurrence quarterly.

---

## 8. Insurance carrier exclusion expansion

**Description.** AI E&O / cyber / business-interruption carriers expand exclusions to remove SLA-credit / refund coverage; previously-covered risk becomes uncovered.

**Likelihood.** 2-3 (observed in 2024-2026 as carriers price emerging AI risk).
**Impact.** 2-4 (residual risk uncovered; reserve must absorb).
**Velocity.** 3 (typically at renewal).

**Mitigation.**
- Annual carrier review with broker
- Self-insurance reserve sized to anticipated exclusion
- Reinsurance / captive structures at scale
- Diversification of carriers if available

**Reserve / control mapping.** Self-insurance reserve adjustment if carrier exclusion expanded; semi-annual review.

---

## 9. Sovereign-AI provider SLA pass-through breach

**Description.** Vendor's SLA depends on mandated in-region compute provider's SLA (af-south-1, africa-south1, Cassava, Liquid, Raxio, MTN AI Factories, Ethiopian AI Institute, EITC, G42, Saudi Aramco-affiliated, etc.); provider breaches; vendor's SLA breaches by pass-through.

**Likelihood.** 2-3 (in sovereign-AI deployments; less in commercial-cloud).
**Impact.** 3-4 (financial-reporting + reputational + regulator-engagement).
**Velocity.** 4-5 (provider outage is immediate).

**Mitigation.**
- Disclosed dependency in customer SLA contracts (provider-SLA-pass-through clause)
- Provider-SLA reserve provisioning
- Multi-region routing where mandated jurisdiction permits
- Provider-relationship management at executive level

**Reserve / control mapping.** Provider-SLA-pass-through reserve; CFO + CTO monitoring.

---

## 10. FX-corridor breach destroying SLA-tier economics

**Description.** Local-currency revenue with USD-denominated cost (foundation-model, tool partner, cloud); local currency depreciates beyond corridor; SLA-tier pricing slips into loss-making.

**Likelihood.** 3-4 in African / EM contexts; 1-2 in USD-pricing-tolerated contexts.
**Impact.** 3-4 (margin destruction; contract repricing fight; tier viability).
**Velocity.** 4 (currency moves can be overnight).

**Mitigation.**
- FX-corridor clauses in contracts (USD-indexed pricing; trigger thresholds)
- USD pricing where customer accepts
- FX hedging where treasury depth allows
- Multi-currency invoicing
- Reserve currency choice aligned to cost currency

**Reserve / control mapping.** FX-corridor watch in weekly CFO cadence; SLA-tier viability quarterly.

---

## 11. Customer concentration on SLA-credit history

**Description.** Single large customer's SLA-credit history dominates aggregate metric; investor narrative reads as "great SLA performance" but is masking poor performance with another customer cohort.

**Likelihood.** 2-3 (common at <USD 5M ARR).
**Impact.** 2-3 (narrative integrity; investor trust on closer DD).
**Velocity.** 1 (visible in disaggregation).

**Mitigation.**
- Disaggregated SLA reporting (by customer tier; by SLA tier; by sector)
- Cohort analysis in board pack
- Honest narrative when concentration exists

**Reserve / control mapping.** Reporting discipline in `meta-agent-board-and-investor-reporting`.

---

## 12. Contractual SLA-credit cap exceeded

**Description.** Customer claims SLA credits in excess of monthly-fee cap; dispute on enforceability; legal exposure if cap clause is challenged.

**Likelihood.** 1-2.
**Impact.** 2-4 (legal cost; precedent risk).
**Velocity.** 2.

**Mitigation.**
- SLA-credit cap clauses drafted to enforceable standard
- Counsel review at contract template stage
- Negotiation history captured; standard-form negotiation playbook

**Reserve / control mapping.** Legal reserve; General Counsel review.

---

## Risk-Register Workflow

1. Score each row for the specific business (likelihood × impact × velocity)
2. Identify top 5 (highest score × velocity)
3. Map each to existing controls (reserve, contract clause, telemetry, drill, communication)
4. Identify gaps (rows where mitigation is absent)
5. Wire to projection (stress scenarios reflect top-3 rows)
6. Wire to living plan (cadence: weekly review of top-3 indicators; monthly review of register)
7. Wire to board pack (top-5 reported quarterly)
8. Wire to investor narrative (FAQ rebuttals address top-3 with reserve / control evidence)

## Cross-References

- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — agent risk register parent
- `skills/meta-financial-stress-test/references/saas-agent-sla-stress-test-scenarios.md` — financial scenarios
- `skills/meta-agent-sla-financial-controls/references/saas-agent-sla-financial-controls-policy.md` — controls
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — reserves
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **FX-corridor risk is materially higher** in African contexts; promote row 10 to top-3 for any local-currency-revenue / USD-cost agent
- **Sovereign-AI pass-through risk** materially higher where in-region compute mandated; promote row 9
- **Mobile-money settlement failure** can manifest as SLA-credit eligibility; document the boundary between payment-rail failure and service failure
- **Public-sector dispute timing** — disputes with public-sector counter-parties can age 90-180 days; size dispute-backlog mitigation accordingly
- **Insurance market thin** — carrier exclusion expansion risk (row 8) more material when self-insurance is the primary backstop
- **Regulator-mandated SLA emerging** — KE / NG / ZA / EG / RW / UG / TZ sector regulators publishing AI / data guidance with SLA expectations; monitor consultations
