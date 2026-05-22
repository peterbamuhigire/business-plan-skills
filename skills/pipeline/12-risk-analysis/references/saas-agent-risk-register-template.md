---
source: Agent-products business-plan audit (2026); engine synthesis
frameworks: [Agent risk register at Section 12 level — pointer to full template]
skill: 12-risk-analysis
cross-reference: [saas-agent-risk-and-stress-test, saas-agent-risk-register-template (deep)]
---

# Agent Risk Register Template — Section 12 Reference

When the plan is an agent business, use the full agent risk register template at:

`skills/12-risk-analysis/saas-agent-risk-and-stress-test/references/saas-agent-risk-register-template.md`

That template covers:

- Action taxonomy with irreversibility classes A/B/C/D
- 12 risk categories (cost, model, autonomy, irreversibility, safety / red-team, multi-agent, tool / vendor, data, talent, regulatory, customer, operational)
- ~50 specific risks populated with severity x likelihood x owner x mitigation x leading indicator x trigger-replan
- Top-5 risks by composite score (for a typical agent business)

## Quick reference: top categories agent plans must cover

1. Cost / margin (LLM spike; tool spike; intervention spike; FX; branch / loop)
2. Model (deprecation; version drift; quality regression; foundation provider absorption)
3. **Autonomy** (action beyond authority; misinterpreted goal; misuse; multi-agent goal cascading)
4. **Irreversibility** (Class D taken incorrectly; Class C without retraction window; regulator exposure)
5. Safety / red-team (prompt injection; jailbreak; tool-call exfiltration; action-auth bypass)
6. Multi-agent (loop; collusion; branch explosion; goal-drift)
7. Tool / vendor (API outage; contract change; lock-in; channel outage)
8. Data (training-data lawsuit; leakage; residency breach; accrual loss)
9. Talent (AI Safety Lead; Eval Engineer; Agent Architect; Tool Engineer departures)
10. Regulatory (sector regulator freeze; data-protection enforcement; AI Act; sovereign-AI disqualification)
11. Customer (misuse; downstream-harm allegation; jobs-impact backlash; contestability)
12. Operational (eval-coverage gap; audit-log gap; kill-switch failure; drill skipped; reserve depletion)

## Use with

- `saas-agent-risk-and-stress-test/SKILL.md` — workflow and detail
- `saas-agent-stress-test-scenarios.md` — quantified scenarios
- Standard Section 12 workflow

## Notes

- Generic Section 12 risk register is insufficient for agent businesses
- Skip nothing; the categories that look "small" are often where catastrophic incidents emerge
- Refresh quarterly; not annually
