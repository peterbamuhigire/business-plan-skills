---
source: Agent SLA + commercial business-plan audit (2026); 2024-2026 board / investor reporting practice; engine synthesis
frameworks: [Board-pack SLA section template; quarterly / annual structure]
skill: meta-agent-board-and-investor-reporting
cross-reference: [saas-agent-investor-narrative-on-sla, meta-agent-sla-financial-controls, saas-agent-sla-bankability-checklist]
---

# SaaS Agent SLA Board Block — Template

Standard SLA section for board packs and investor reporting. Adopt as a recurring block (quarterly) and expand annually for strategy review.

---

## Quarterly Board-Pack SLA Block (3-5 pages)

### Page 1 — Headline Metrics

```
## SLA — Q{n} {year}

**Performance vs commitment**
| Metric | Commit | Actual | Trend (4-qtr) | Status |
|---|---|---|---|---|
| Uptime | 99.5% | 99.82% | ↑ from 99.71% | ✅ |
| Response time p95 | 5s | 3.2s | → stable | ✅ |
| Accuracy / DoD | 95% | 97.2% | ↑ from 96.4% | ✅ |
| MTTR sev-1 | 4h | 2.8h | ↓ from 3.5h | ✅ |
| Sev-1 incidents | ≤2 | 1 | → | ✅ |

**Reserve adequacy**
- SLA-credit accrual: {x%} of agent revenue
- Reserve provisioned: {y%}
- Adequacy ratio: {z%} (target ≥110%)
- Quarterly true-up: completed {date}; auditor concurrence ✅

**Disputes**
- Open: {n}; avg aging {d} days
- Resolved in quarter: {m}
- Escalations to legal: {p}
- Customer-gaming flags investigated: {q}

**Customer impact**
- Customers with SLA-credit issued: {n} of {m} ({x%})
- Concentration: top-3 credit-receiving customers = {y%} of credit issued
- Churn correlated with SLA misses: {n} customers ({m%} of quarter churn)
```

### Page 2 — Performance Detail & Cohort Disaggregation

```
**Per SLA tier** (Bronze / Silver / Gold)
| Tier | Customer count | Trailing uptime | Credit ratio | Tier ARR |

**Per sector**
| Sector | Customer count | Trailing performance | Credit ratio |

**Per pricing primitive**
| Primitive | Trailing performance | Credit / refund ratio |
```

### Page 3 — Reserve, Controls & Auditor

```
**Reserve walkforward**
| Item | USD k |
|---|---|
| Opening reserve | |
| Provisions during quarter | |
| Credits paid out | |
| True-up adjustment | |
| Closing reserve | |

**Refund-reserve walkforward (if outcome pricing)**
[same structure]

**Controls evidence**
- Approval workflow audit-log: {n} credits approved, all within threshold
- Segregation-of-duties review: {date}; no exceptions
- SOC1 / SOC2 control testing: status {current / lapsed}
- Catastrophic-scenario tabletop: completed {date}; lessons captured

**Auditor engagement**
- Firm: {name}
- Methodology concurrence: ✅
- Quarter-end procedures: {scope}
- Next review: {date}
```

### Page 4 — Risk Register Update

```
**Top-3 SLA risks (this quarter)**
1. {Risk row from sla-risk-register}: trigger indicators {x, y, z}; mitigation action {a}; owner {b}
2. {...}
3. {...}

**Risk trend signals**
- Catastrophic-event indicator: {green/amber/red}
- Foundation-model cost: {indicator}
- Customer-gaming indicator: {indicator}
- Regulator engagement: {indicator}

**New / changed risks**
- {Describe}
```

### Page 5 — Forward Signal, Strategy & Investor Comms

```
**Forward signal Q{n+1}**
- Expected performance: {commitments + drivers}
- Reserve assumption: {hold / change}
- Policy changes proposed: {none / describe with rationale}
- Catastrophic-event drill calendar: next {date}

**Strategy items for Board decision**
- {SLA-tier mix shift proposal / Policy refresh / Insurance renewal / Auditor change / Regulator engagement step / etc.}

**Investor communications**
- Quarterly update SLA block: drafted {date}; published {date}
- DD-room SLA section: refreshed {date}
- Major-investor SLA queries during quarter: {n} (responses logged)
- Sovereign / DFI / strategic engagement: {summary}
```

---

## Annual Board Review — SLA Strategy (1 board meeting)

Expanded annual review covering:

1. **Performance retrospective** — 4-quarter performance vs plan; root-cause of misses; lessons learned
2. **Reserve methodology revalidation** — assumption review; methodology-change proposals; auditor confirmation
3. **Stress-test refresh** — all 8 scenarios re-run with current data; new scenarios added; reserve impact re-calculated
4. **Policy refresh** — SLA-credit cap, vendor-cost pass-through, FX-corridor, outcome-definition, dispute-resolution — all reviewed for currency
5. **Insurance / self-insurance review** — carrier landscape; exclusion changes; reserve adequacy
6. **Regulator engagement review** — consultations responded; upcoming consultations; pre-clearance status
7. **Peer benchmarking** — peer SLA disclosures; competitive position
8. **Investor narrative refresh** — narrative position; FAQ rebuttal library; pitch-slide update
9. **Living-plan cadence refresh** — owners, thresholds, escalation paths
10. **Investment requests** — cost-of-quality budget; tooling; talent (SLA engineering; reserve-actuary)

---

## Investor-Update Block (Quarterly Letter — 1 paragraph + 1 table)

```
## SLA performance — Q{n} {year}

We met or exceeded all SLA commitments this quarter. Uptime {x%} (commit {y%}); DoD compliance {x%} (commit {y%}); response p95 {x}s (commit {y}s); {n} sev-1 incidents within commit. SLA-credit accrual {x%} of agent revenue (industry benchmark {y%}); reserve adequacy {z%}; quarterly true-up completed with auditor concurrence. Open disputes {n}, average aging {d} days; no legal escalations. Forward Q{n+1} expectations consistent with this quarter; no material policy changes. {Any catastrophic-event note / sovereign-AI / regulator engagement update if material.}
```

---

## Catastrophic-Event Special Report (within 72 hours of sev-1 mass-credit)

```
**Event date / window:** {date / window}
**Customers affected:** {n} ({x%} of base)
**Root cause:** {description}
**SLA-credit estimate:** {USD k} ({y%} of monthly agent revenue)
**Reserve impact:** {z%} of provisioned reserve drawn
**Customer-communications status:** {summary}
**Dispute / litigation risk:** {assessment}
**Insurance notification:** {status}
**Auditor notification:** {status}
**Recovery plan:** {summary}
**Next update:** {date}
```

---

## Cross-References

- `skills/meta-agent-board-and-investor-reporting/SKILL.md` — board reporting parent
- `skills/meta-agent-sla-financial-controls/SKILL.md` — controls
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — reserves
- `skills/12-risk-analysis/saas-agent-sla-risk/references/saas-agent-sla-risk-register.md` — risk register
- `skills/11-funding-request/saas-agent-investor-narrative-on-sla/SKILL.md` — narrative
- `skills/meta-bankability-scoring/references/saas-agent-sla-bankability-checklist.md` — scorecard
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Sovereign-AI provider performance** — explicit row in Page 1 metrics when in-region compute mandated; capture provider-SLA-pass-through credit separately
- **FX-corridor reserve** — Page 3 reserve walkforward should show FX impact line when local-currency reserve / USD cost exposure exists
- **Mobile-money settlement reliability** — adjacent metric on Page 1 for per-resolution / per-outcome agents
- **Public-sector reporting** — consider separate public-sector slice in Page 2 cohort disaggregation; public-sector SLA performance often a board KPI in African plans
- **DFI / multilateral investor block** — for DFI-funded businesses, add a development-outcome SLA tie (e.g. "SLA on advisory accuracy supports {ESMP / development outcome}")
- **Audit-firm engagement** — where mid-tier auditor is engaged, name explicitly and reference scope; do not imply Big-4
- **Insurance carrier scarcity** — self-insurance reserve adequacy should be the headline in Page 3 when carriers unavailable
- **Regulator monitoring** — BoU / CMA / NDPC / CBK / CMA / CBN / SEC / SARB / FSCA consultations should appear in Page 4 risk-trend signals quarterly
