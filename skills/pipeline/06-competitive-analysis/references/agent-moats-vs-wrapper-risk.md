---
source: Agent-products business-plan audit (2026); 2024-2026 agent-VC diligence; Walling moats; Wardley
frameworks: [Compact moat-vs-wrapper rubric]
skill: 06-competitive-analysis
cross-reference: [saas-agent-moat-and-wrapper-risk, meta-agent-valuation-adjustments]
---

# Agent Moats vs Wrapper Risk — Compact Rubric

For Section 06 of any agent-product plan. Detailed checklist in `saas-agent-moat-and-wrapper-risk/references/saas-agent-moats-and-wrapper-risk-checklist.md`.

## The 8-Question Test (score 0-3 each; max 24)

1. **Proprietary tools** — your tools, your integrations, your data sources?
2. **Proprietary action data** — accruing per customer / interaction?
3. **Integration depth** — system-of-record, identity, audit, billing?
4. **Eval-loop** — proprietary suite + human-correction + improvement trajectory?
5. **Customer-trust / brand** — named references, regulator references?
6. **Regulatory clearance** — sectoral approval, audit-log accepted?
7. **Switching cost** — data + integration + retraining + audit-log lock-in?
8. **Distribution** — channel / partner / embedded reach competitors can't match?

## Interpretation

- 0-8: Wrapper — apply 40-70% valuation discount
- 9-14: Real but incomplete — neutral; deepen 2-3 dimensions
- 15-19: Strong moat — premium territory
- 20-24: Rare strong defensibility — substantial premium

## Wrapper Red Flags

- Pure prompt cleverness over GPT
- Public-tool-only
- Generic LangChain / CrewAI / AutoGen wrap
- "We partner with OpenAI" as moat
- Demo without deployment
- Single-customer custom build
- No eval-loop
- Vertical positioning without vertical depth
- One-time fine-tune
- Open-source-model wrapper without engineering / data edge
- Platform plug-in without independent defensibility

## The Foundation-Model Commoditisation Test

Ask: "If OpenAI / Anthropic / Google ships our category next quarter, what survives?"

Survives because:
- Customer action data accrued
- Proprietary tools / integrations
- Regulator-accepted audit log
- Vertical workflow embedding
- Customer-trust / vertical reputation
- Distribution channel
- Local-language / sovereign-AI advantage

If "what survives" is empty -> wrapper.

## Wardley-Map Check

A moat in Commodity layers (foundation model, generic orchestration, generic observability) is not a moat. Your moat must live in Custom / Genesis layers with explicit "stay defensible" logic.

## Moat Thesis Paragraph

One paragraph an experienced operator would not call marketing. Must answer:
- What is proprietary?
- What accrues?
- What survives provider commoditisation?
- What is the switching cost?

If you cannot write this paragraph without marketing language, the moat is not yet real.

## Cross-References

- Full checklist: `saas-agent-moat-and-wrapper-risk/references/saas-agent-moats-and-wrapper-risk-checklist.md`
- Valuation consumer: `meta-agent-valuation-adjustments`
- Executive summary: `saas-agent-executive-summary-block.md`
