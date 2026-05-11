---
source: Agent-products business-plan audit (2026); EU AI Act; NIST AI RMF; African AI policy; engine synthesis
frameworks: [Agent risk register; Irreversibility taxonomy; HITL policy matrix; Severity x Likelihood; Trigger-replan]
skill: saas-agent-risk-and-stress-test
cross-reference: [saas-agent-unit-economics-and-cogs, meta-financial-stress-test, meta-agent-bankability-and-investor-readiness]
---

# Agent Risk Register — Template

A populated agent risk register that a board / DFI / regulator-acceptable diligence would not call performative. Customise to the specific agent business; do not delete categories.

## 0. Action taxonomy and irreversibility classes

| Class | Definition | Examples | HITL policy |
|---|---|---|---|
| A — reversible information | output is information; no action taken | summary, recommendation, draft | Audit only |
| B — reversible transaction | action takeable but reversible without harm | open ticket, schedule, draft email saved | Agent autonomous within policy; HITL on escalation |
| C — soft-irreversible | action takes effect but can be retracted with effort | message sent and not yet read; transaction queued and not settled | HITL approval above threshold |
| D — hard-irreversible | action cannot be undone | financial transfer settled; legal document filed; medication ordered; permit issued; ledger committed | Human-final required; pre-action confirmation; double-signing |

## 1. Cost / margin risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| C1 | LLM provider price hike >25% | 4 | 3 | 12 | CFO + CTO | Multi-vendor; cache; model-mix; pricing pass-through clause | Provider price watch | Provider announces >25% |
| C2 | Tool cost spike (vendor change) | 3 | 3 | 9 | Tool Engineer + CFO | Multi-vendor; alternate path | Vendor invoice variance | >50% spike sustained |
| C3 | Intervention rate doubles | 4 | 3 | 12 | HITL Designer + Eval Engineer | Triage tuning; planner improvement | Intervention rate trend | +5pp sustained 2 weeks |
| C4 | FX shock 20% local depreciation | 3 | 3 | 9 | CFO | FX corridor in pricing; USD-equivalent contracts | FX volatility | -10% in 30 days |
| C5 | Branch / loop explosion (multi-agent) | 4 | 2 | 8 | Eval Engineer | Hard branch + loop caps; kill-switch | Branch / loop breach | any breach |

## 2. Model risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| M1 | Foundation model deprecation breaks agent tool-calls | 4 | 3 | 12 | CTO | Reserve; migration plan; eval before swap | Provider deprecation notice | Notice issued |
| M2 | Version-drift quality regression | 3 | 3 | 9 | Eval Engineer | Versioned eval suite; canary roll | Eval score variance | -5pp single version |
| M3 | Foundation provider absorbs orchestration | 5 | 3 | 15 | CEO + CTO | Moat deepening; vertical depth; tool registry | Provider product roadmap | Provider ships analogue |
| M4 | Local-language / specialist model regression | 3 | 2 | 6 | Head of AI | Specialist model fallback; eval cover | Eval score on local-language | -5pp |

## 3. Autonomy risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| A1 | Agent takes action beyond authority | 5 | 2 | 10 | AI Safety Lead | Action-class policy; tool-permission scoping; double-signing on Class C/D | Audit-log anomalies | Any sev-1 |
| A2 | Misinterpreted customer goal -> wrong outcome | 4 | 3 | 12 | AI Safety Lead + Eval Engineer | Goal-confirmation step; clarifying-question policy | Customer-correction rate | +3pp |
| A3 | Misuse by customer end-user | 3 | 3 | 9 | Compliance + AI Safety | Acceptable-use policy; rate-limit; abuse detection | Abuse signal | Spike |
| A4 | Goal-mis-specification cascading across multi-agent | 4 | 2 | 8 | Agent Architect | Critic step; sanity-check gate | Critic-failure rate | +3pp |

## 4. Irreversibility risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| I1 | Class D action taken incorrectly (financial / legal / medical / regulatory) | 5 | 2 | 10 | AI Safety Lead + CEO | Human-final on Class D; double-signing; immutable audit; pre-action confirmation; reserve | Pre-action confirmation drop-out | Any sev-1 |
| I2 | Class C action sent without retraction window | 4 | 2 | 8 | AI Safety Lead | Hold-and-confirm window; retraction tooling | Send-without-window count | Any |
| I3 | Class D action with regulator exposure | 5 | 2 | 10 | Compliance | Regulator-pre-clearance; sectoral approval | Regulator inquiry | Any inquiry |

## 5. Safety / red-team risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| S1 | Prompt injection bypasses safety | 4 | 3 | 12 | AI Safety Lead | Input filtering; tool-call sandboxing; eval on injection vectors | Injection-scan flags | New vector detected |
| S2 | Jailbreak / model-policy bypass | 4 | 3 | 12 | AI Safety Lead | Multi-layer policy; refusal evals; logging | Refusal-rate variance | -5pp |
| S3 | Tool-call exfiltration of sensitive data | 5 | 2 | 10 | AI Safety + Tool Engineer | Tool-permission scoping; data classification; egress filtering | Egress-volume anomaly | Spike |
| S4 | Action-authentication bypass | 5 | 2 | 10 | AI Safety + CTO | Per-action auth; mTLS; signed tool envelopes; rotation | Auth-anomaly | Any |

## 6. Multi-agent risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| MA1 | Planner / worker / critic loop | 4 | 3 | 12 | Eval Engineer | Loop cap; circuit-breaker; kill-switch | Loop count | Any breach |
| MA2 | Agents collude to satisfy critic falsely | 4 | 2 | 8 | Eval Engineer | Independent eval; cross-validation; ground-truth sampling | Critic-score / eval gap | Gap >5pp |
| MA3 | Branch explosion | 4 | 3 | 12 | Eval Engineer | Branch cap; budget cap; kill-switch | Branch count | Any breach |
| MA4 | Goal-drift across agents | 3 | 3 | 9 | Agent Architect | Shared goal frame; periodic re-anchor | Goal-anchor drift | Detected drift |

## 7. Tool / vendor risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| T1 | Critical tool API outage | 4 | 3 | 12 | Tool Engineer | Multi-vendor; alternate path; degrade gracefully | 5xx / timeout rate | Outage >1h |
| T2 | Tool API contract change | 3 | 3 | 9 | Tool Engineer | Versioned adapters; deprecation watch | Vendor changelog | Major change |
| T3 | Vendor lock-in (single-tool dependency) | 4 | 2 | 8 | CTO | Alternate-vendor evaluation; abstraction layer | Vendor concentration | >60% on one tool |
| T4 | Channel-vendor outage (WhatsApp / SMS / USSD / IVR) | 4 | 2 | 8 | Tool Engineer | Multi-aggregator; SMS / voice fallback | Aggregator status | Outage >30 min |

## 8. Data risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| D1 | Training-data lawsuit | 4 | 2 | 8 | Legal + Head of AI | Provenance audit; licence registry; non-training-customer-data policy | Provider EULA change | EULA shift |
| D2 | Customer-data leakage via agent | 5 | 2 | 10 | AI Safety + CTO | Data classification; egress filtering; tenant isolation | Egress anomalies | Any leakage |
| D3 | Data-residency breach | 4 | 2 | 8 | Compliance + CTO | In-region inference for residency-sensitive; routing rules | Routing audit | Mis-routed |
| D4 | Action-data accrual loss | 3 | 2 | 6 | Head of AI | Replication; backup; lineage | Backup verification | Loss event |

## 9. Talent risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| TL1 | AI Safety Lead departs | 5 | 3 | 15 | CEO + Head of People | Comp + retention; succession; fractional cover | Retention signal | Departure |
| TL2 | Eval Engineer departs | 4 | 3 | 12 | Head of People | Comp; succession; documentation | Retention signal | Departure |
| TL3 | Agent Architect departs | 4 | 2 | 8 | Head of People | Documentation; co-architect | Retention signal | Departure |
| TL4 | Tool Engineer departs | 3 | 3 | 9 | Head of People | Documentation; pairing | Retention signal | Departure |

## 10. Regulatory risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| R1 | Sector regulator action freezes deployment | 5 | 2 | 10 | Compliance + CEO | Pre-clearance; sectoral engagement; pause-switch | Regulator inquiry | Action issued |
| R2 | Data-protection enforcement (ODPC / NDPC / NITA-U / Info Reg / NCSA) | 4 | 2 | 8 | Compliance | DPIA; data-mapping; controller / processor clarity | Inquiry | Notice |
| R3 | AI Act-equivalent enforcement | 4 | 2 | 8 | Compliance + Legal | Risk-class self-assessment; documentation; HITL evidence | Inquiry | Notice |
| R4 | Sovereign-AI procurement disqualification | 3 | 3 | 9 | CEO + Compliance | In-country compute; local-language; local entity | Tender criteria | Disqualified |

## 11. Customer risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| CU1 | Customer-misuse of agent | 3 | 3 | 9 | Customer Success + Compliance | AUP; usage monitoring; abuse detection | Misuse signal | Spike |
| CU2 | Downstream-harm allegation | 4 | 2 | 8 | Legal + Compliance | Contractual indemnity; insurance; HITL evidence | Customer complaint | Any |
| CU3 | Jobs-impact backlash | 3 | 3 | 9 | CEO + Communications | Jobs-impact disclosure; re-skilling commitment | Public sentiment | Press / social |
| CU4 | Contestability / redress request | 2 | 3 | 6 | Compliance | Redress workflow; SLA on response | Request rate | Spike |

## 12. Operational risks

| ID | Risk | Severity | Likelihood | Score | Owner | Mitigation | Leading indicator | Trigger-replan |
|---|---|---|---|---|---|---|---|---|
| O1 | Eval-coverage gap on Class C/D actions | 5 | 2 | 10 | Eval Engineer + AI Safety | Coverage matrix; gap-fill sprints | Coverage report | Any gap |
| O2 | Audit-log gap | 5 | 2 | 10 | Compliance + CTO | Append-only log; review monthly | Audit-log review | Any gap |
| O3 | Kill-switch failure | 5 | 1 | 5 | Tool Engineer + AI Safety | Monthly drill; redundant switches | Drill report | Failure |
| O4 | Drill skipped | 3 | 3 | 9 | AI Safety Lead | Cadence enforcement; CEO sign-off | Drill calendar | Missed |
| O5 | Reserve depletion (irreversibility / migration / regulator) | 4 | 2 | 8 | CFO | Top-up cadence; reserve adequacy review | Reserve balance | <12 months |

## Summary table

- Number of risks: ~50
- Number of sev-5 risks: ~10 (catastrophic)
- Number of sev-4 risks: ~20
- Number of sev-3 risks: ~15
- Number of sev-2 risks: ~5

Top-5 by composite score in a typical agent business (varies by archetype):

1. M3 — Foundation provider absorbs orchestration (5x3=15)
2. TL1 — AI Safety Lead departs (5x3=15)
3. A1 — Agent takes action beyond authority (5x2=10)
4. I1 — Class D action taken incorrectly (5x2=10)
5. O1 — Eval-coverage gap on Class C/D (5x2=10)

## Cross-references

- Reserves consumer: `saas-agent-unit-economics-and-cogs`
- Stress scenarios: `saas-agent-stress-test-scenarios.md`
- Bankability consumer: `meta-agent-bankability-and-investor-readiness`
- Living-plan cadence: in `saas-agent-risk-and-stress-test/SKILL.md`
