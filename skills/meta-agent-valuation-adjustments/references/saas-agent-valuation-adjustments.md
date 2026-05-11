---
source: Agent-products business-plan audit (2026); 2024-2026 agent-VC and SaaS multiples research; Damodaran AI/agent commentary; Bessemer / OpenView / ICONIQ SaaS reports
frameworks: [Agent premium / wrapper discount; Adjustment trail; Investor-archetype multiples; Stress on multiple]
skill: meta-agent-valuation-adjustments
cross-reference: [meta-valuation, meta-ai-valuation-adjustments, saas-agent-moat-and-wrapper-risk]
---

# Agent Valuation Adjustments — Reference

## 1. The Adjustment Trail

```
SaaS base multiple (Rule-of-40-adjusted ARR multiple)
  +/- AI adjustment (from meta-ai-valuation-adjustments)
  +/- Agent adjustment (this document)
  -  Geographic / market discount
  =  Adjusted multiple range (low / base / high)
```

## 2. Agent Adjustment Components

### a) Moat-vs-wrapper score (primary driver)
| Score | Category | Adjustment |
|---|---|---|
| 0-8 | Wrapper | -40 to -70% |
| 9-14 | Real but incomplete | -20 to +0% |
| 15-19 | Strong moat | +20 to +50% |
| 20-24 | Rare strong defensibility | +50 to +100%+ |

### b) Per-resolution-economics premium
| Condition | Adjustment |
|---|---|
| Cost-per-resolved-task < competitive anchor with sustained agent GM >65% | +10 to +25% |
| Cost-per-resolved-task at parity with anchor; agent GM 50-65% | 0% |
| Cost-per-resolved-task > anchor; agent GM <50% | -10 to -30% |

### c) Intervention-rate trajectory
| Condition | Adjustment |
|---|---|
| Intervention rate declining 4+ quarters | +5 to +15% |
| Intervention rate flat | 0% |
| Intervention rate rising | -10 to -25% |

### d) Irreversibility governance
| Condition | Adjustment |
|---|---|
| Clean log + drilled kill-switch + regulator-accepted audit-log | +5 to +10% |
| Standard governance | 0% |
| Recent sev-1 irreversibility incident in last 12 months | -15 to -40% |
| Ongoing unresolved incident | -30 to -60% |

### e) Regulator engagement evidence
| Condition | Adjustment |
|---|---|
| Pre-clearance / sectoral approval in target market | +5 to +15% |
| Documented engagement; no approvals yet | 0% |
| Pending regulatory action or notice | -20 to -60% |
| Active enforcement | -50 to -90% |

### f) Foundation-model platform risk
| Condition | Adjustment |
|---|---|
| Your moat survives provider commoditisation (proprietary tools / data / integration / regulatory) | 0% |
| Provider plausibly shipping in your category in 12-24 months | -15 to -30% |
| Provider actively shipping in your exact category now | -30 to -50% |
| You ARE the orchestration / agent-platform layer that provider will absorb | -40 to -70% |

### g) Multi-agent governance discount
| Condition | Adjustment |
|---|---|
| Multi-agent with branch + loop caps + kill-switch + drilled governance | 0% |
| Multi-agent with branch / loop caps only | -10 to -15% |
| Multi-agent without governance evidence | -20 to -40% |
| Multi-agent with documented runaway incidents | -30 to -60% |

### h) Eval-loop maturity
| Condition | Adjustment |
|---|---|
| Proprietary eval suite + improving trajectory + human-correction feeds product | +5 to +15% |
| Standard offline + online eval | 0% |
| No eval-loop | -15 to -30% |

### i) Talent depth (AI Safety Lead, Eval Engineer, Agent Architect)
| Condition | Adjustment |
|---|---|
| All key roles full-time + retention strong | +5% |
| Key roles filled but with retention risk | 0% |
| AI Safety Lead vacant or recently departed | -10 to -25% |
| Multiple key roles vacant | -20 to -40% |

## 3. Composite Adjustment Range (typical)

| Profile | Composite adjustment range |
|---|---|
| Wrapper (low score across dimensions) | -60 to -80% (i.e. multiple is 20-40% of SaaS / AI baseline) |
| Average agent (real but incomplete) | -15 to +10% |
| Strong vertical agent (high moat, strong governance) | +25 to +75% |
| Exceptional agent (rare top-quartile across all dimensions) | +75 to +200% |

## 4. Comparable Transactions Worksheet (2024-2026)

(Note: agent-comparable data is sparse and noisy. Examples below are illustrative reference points; verify with current sources before quoting in a plan.)

Investors will typically reference clusters such as:

- **Customer-service agent businesses** — multiples observed in 8x-25x ARR range at growth-stage; defensible vertical agents at premium end
- **Coding / developer agent businesses** — premium multiples observed at top end (proprietary action data + developer adoption)
- **Vertical agent businesses (legal, medical, finance)** — typically 12x-30x ARR at growth-stage if vertical moat is real
- **Agent platforms** — wide range; wrapper-of-LangChain at 4x-8x; defensible platform with developer adoption at 20x+
- **Multi-agent orchestration plays** — sparse; valued more on technical depth than pure ARR multiple
- **Wrapper agent businesses** — single-digit ARR multiples typical

Document the comparable's:
- Date
- Stage (seed / A / B / C / growth)
- Geography
- Vertical / archetype
- ARR (if disclosed)
- Pre-money valuation
- Implied multiple
- Notable adjustments (moat profile, AI vs agent classification)

## 5. Stress on Multiple

| Stress event | Multiple impact |
|---|---|
| Provider 5x pricing | -20 to -40% (margin compression assumed not fully passed-through) |
| Irreversibility sev-1 incident | -30 to -50% short-term; recovers with trust restoration |
| Regulator freeze in a market | -20 to -40% short-term; recovers with re-clearance |
| Foundation-model provider ships in your category | -25 to -60% structural |
| AI Safety Lead departs without succession | -15 to -25% short-term |
| Intervention rate spike + sustained | -15 to -30% structural |
| Multi-agent loop / branch incident in production | -10 to -25% short-term |
| Prompt-injection mass exploitation | -20 to -40% short-term |
| FX 20% (institutional rounds) | <5% (priced in USD); larger for local-currency thinking |

## 6. Investor-Archetype-Specific Multiples

| Investor archetype | Multiple anchor | Comments |
|---|---|---|
| Agent-specialist fund | Premium range if strong moat; sharp wrapper discount | Most sensitive to wrapper-vs-moat; rigorous diligence |
| Vertical AI fund | Sector-anchored; premium if vertical moat | Wants vertical references, regulator engagement |
| Generalist SaaS fund | SaaS Rule-of-40 anchor; modest agent premium for defensible | Less premium, more downside protection |
| Sovereign-AI / strategic | Strategic value > pure financial multiple | Procurement footprint, residency, local-language |
| DFI / multilateral | Patient capital; longer payback acceptable; mission-aligned | Lower required multiple; expects governance + impact evidence |
| Corporate strategic | Strategic-fit premium; possibly low financial multiple but high price for fit | Beware single-buyer risk in cap-table |
| Family office / individual | Wide variance | Often lighter diligence; price discovery noisier |

## 7. Worked Example

**Business:** Vertical collections agent (East Africa), USD 2M ARR, 65% ARR growth, agent GM 84%, Rule-of-40 = 149.

- SaaS base multiple (Rule-of-40 = 149 -> top-decile): 12-18x ARR (apply 60th percentile = 13x given geography)
- AI adjustment: +10% (real eval, real cost engineering, in-region inference): 14.3x
- Agent adjustment:
  - Moat score 18 (strong): +30%
  - Per-resolution economics premium (cost USD 0.19 vs anchor USD 2.50, agent GM 84%): +20%
  - Intervention rate declining: +10%
  - Clean irreversibility log + monthly drill: +5%
  - Documented regulator engagement: +10%
  - Foundation-model commoditisation risk (low; deep workflow + tools + regulator): 0%
  - Multi-agent governance: N/A (single-agent)
  - Eval-loop mature: +10%
  - Talent: AI Safety Lead in seat: +5%
  - Composite agent adjustment: ~+90% multiplicative
- Adjusted multiple: 14.3x * 1.90 = ~27x
- Geographic discount (East Africa): -20%
- Final multiple: ~22x ARR -> pre-money USD 44M

**Stress check:**
- Provider 5x: -30% -> 15x -> pre-money USD 30M
- Foundation-model commoditisation reassessment to high risk: -40% -> 13x -> pre-money USD 26M
- Sev-1 irreversibility incident: -40% -> 13x -> pre-money USD 26M

Range to communicate to round investors: pre-money USD 26-44M; base USD 36M.

## 8. Anti-Patterns

- Quoting raw SaaS ARR multiple without adjustments
- Hand-waving "AI is our moat" and claiming a 50% premium without rubric
- Ignoring wrapper discount because the agent has demo polish
- Single-point multiple with no range
- Comparable transactions cherry-picked
- Foundation-model platform risk omitted
- Geographic discount omitted in emerging markets
- Pricing on TAM not on operating evidence
- Bundling agent revenue into SaaS revenue when attribution would yield a clearer agent-multiple

## 9. Living-Plan Wiring

- Quarterly comparable scan
- Quarterly moat-vs-wrapper rescore
- Quarterly multiple range refresh
- Round opens -> set pre-money
- Stress refresh quarterly
