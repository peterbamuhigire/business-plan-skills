---
source: Agent-products business-plan audit (2026); 2024-2026 investor relations practice; engine synthesis
frameworks: [Monthly agent investor block]
skill: meta-agent-board-and-investor-reporting
cross-reference: [saas-agent-unit-economics-and-cogs, saas-agent-risk-and-stress-test, saas-agent-board-pack-section]
---

# Monthly Investor Update — Agent Block (Template)

Use this block in the monthly investor update for any agent-product business. Append after the standard SaaS / AI block.

```
## Agent product (month of {YYYY-MM})

### Headline metrics
- Resolved tasks: {n} (vs plan {n_plan}; vs prior {n_prior})
- Cost per resolved task: {USD x.xx} (vs plan; vs prior)
- Intervention rate: {x%} (vs plan; vs prior)
- Task success rate: {x%} (vs plan; vs prior)
- Agent gross margin: {x%} (vs plan; vs prior)
- Agent ARR attribution: {USD k} ({x% of total ARR})

### Eval suite (4-week trend)
- Accuracy: {x%} -> {x%}
- Hallucination: {x%} -> {x%}
- Refusal: {x%} -> {x%}
- Latency p95: {ms} -> {ms}

### Top 3 agent risks this month
1. {risk; mitigation in progress; owner}
2. {...}
3. {...}

### Provider / model changes
- {LLM provider change / pricing / deprecation notice}
- {Tool vendor change / API change}
- {Multi-vendor posture change}

### Incidents
- Sev-1 incidents: {n} (zero or list with status)
- Sev-2 incidents: {n}
- Drill executed this month: {yes / no}; outcome: {pass / gap}
- Audit-log review: {pass / findings}

### Reserves
- Irreversibility reserve: {USD k}; months of coverage: {n}
- Model-migration reserve: {USD k}
- Regulator-engagement reserve: {USD k}

### Regulator / policy
- Engagements this month: {list}
- New guidance / notice: {list}

### Talent
- AI Safety Lead in seat: {yes / no / fractional}
- Eval Engineer team size: {n}
- Agent team attrition this month: {n}

### Next month focus
- {focus 1}
- {focus 2}
- {focus 3}

### Trigger-replan events triggered
- {if any; with action taken or planned}
```

## Notes for the author

- Keep to one page max
- Use the same metric order each month so investors can compare
- Sev-1 incidents must already have been communicated within 48h; this block is for record
- Variance >threshold must include diagnosis (execution vs environment) and remediation
- Trigger-replan events must be flagged immediately
- Plain-English summary at the top if board members are non-technical
