---
name: meta-agent-valuation-adjustments
description: Agent premium (when defensible) vs wrapper discount (when not), layered on top of SaaS and AI valuation logic. Models per-resolution-economics premium, intervention-rate-tied valuation, comparable transactions in agent space, foundation-model-platform-risk overlay, multi-agent governance discount. Use whenever an agent business is being valued or pricing-implied multiples set.
---

# Meta — Agent Valuation Adjustments Skill

## Overview

SaaS valuation (handled by `meta-valuation` + `saas-valuation-and-fundraising-strategy`) uses Rule-of-40-adjusted ARR multiples + cohort discipline. AI valuation (handled by `meta-ai-valuation-adjustments`) layers premium / discount for AI defensibility. **Agent valuation** must add a separate adjustment because agent businesses span a much wider range — from "genuinely defensible vertical agent" earning a substantial premium to "GPT prompt wrapper" earning a wrapper discount of 40-70% on the headline ARR multiple.

The dispersion of agent-business multiples in 2025-2026 is wider than any other AI category. Investors are explicit about premium and discount; the model must be too.

## Use When

- An agent-product plan is being valued
- A funding round is being planned and pre-money expectation set
- An exit comparable analysis is being run
- A board pack includes valuation update
- The plan must declare its expected multiple range with reasoning
- Cross-loaded with `meta-valuation` and `meta-ai-valuation-adjustments`

## Do Not Use When

- The product is not an agent — use SaaS / AI valuation alone
- The business is too early for valuation discipline (pre-revenue with no operating evidence) — use directional range only

## Required Inputs

- SaaS valuation base (from `meta-valuation` and `saas-valuation-and-fundraising-strategy`)
- AI valuation adjustment (from `meta-ai-valuation-adjustments`)
- Agent moat-vs-wrapper score (from `saas-agent-moat-and-wrapper-risk`)
- Agent unit economics (cost-per-resolved-task, agent GM)
- Intervention rate trajectory
- Task success rate trajectory
- Irreversibility-incident log
- Regulator engagement evidence
- Comparable transactions in agent space (recent rounds, recent exits)
- Foundation-model-provider trajectory in your category

## Workflow

1. **Compute the SaaS base multiple** — Rule-of-40-adjusted ARR multiple from `meta-valuation`.
2. **Apply the AI adjustment** — premium or discount from `meta-ai-valuation-adjustments`.
3. **Apply the agent adjustment** per `references/saas-agent-valuation-adjustments.md`:
   - **Moat-vs-wrapper score** (0-24 from `saas-agent-moat-and-wrapper-risk`):
     - 0-8 (wrapper): apply 40-70% discount on AI-adjusted multiple
     - 9-14 (real but incomplete): apply 0-20% discount or 0% premium depending on trajectory
     - 15-19 (strong moat): apply 20-50% premium
     - 20-24 (rare strong): apply 50-100%+ premium
   - **Per-resolution-economics premium** (if cost-per-resolved-task < competitive anchor with sustained GM >65%): +10-25%
   - **Intervention-rate trajectory** (if declining over 4+ quarters): +5-15%; (if rising): -10-25%
   - **Irreversibility governance**: clean log + drilled kill-switch + audit-log accepted = +5-10%; recent sev-1 = -15-40%
   - **Regulator engagement evidence**: pre-clearance / sectoral approval = +5-15%; pending regulatory action = -20-60%
   - **Foundation-model platform risk**: high (provider actively shipping in your category) = -15-40%; low (your moat survives provider commoditisation) = neutral
   - **Multi-agent governance discount**: if multi-agent product without branch / loop caps + kill-switch + governance evidence = -20-40%
4. **Compute comparable transactions** — recent agent rounds and exits, multiple ranges, adjusted for stage / geography / vertical. Note: agent-comparable data is sparse and noisy in 2026; use carefully.
5. **Apply geographic / market adjustments** — African / emerging-market discount per `meta-valuation` (typically -10 to -30% on SaaS / AI; can be narrower for sovereign-AI-positioned plays).
6. **Output the adjusted multiple range** — low / base / high with reasoning per adjustment.
7. **Map to pre-money** — adjusted multiple x current ARR (or forward ARR with discount).
8. **Stress the valuation** — under provider 5x, irreversibility incident, regulator action, foundation-model commoditisation, AI Safety Lead departure: what does the multiple compress to?
9. **State the investor-archetype-specific multiple** — agent-specialist fund / vertical AI fund / generalist SaaS fund / sovereign-AI / DFI all anchor differently.
10. **Wire to the funding ask** (`11-funding-request`) and exit thesis (`saas-valuation-and-fundraising-strategy`).

## Quality Bar

- All three layers (SaaS / AI / Agent) adjustments visible and computed transparently
- Moat-vs-wrapper score directly drives the adjustment, not a vibe
- Comparable transactions cited with date and source
- Foundation-model platform risk explicitly priced
- Geographic adjustment applied
- Range stated (low / base / high) with reasoning per adjustment
- Stress on valuation under tail risks
- Investor-archetype-specific multiples differentiated

## Anti-Patterns

- Quoting headline ARR multiple without adjustments
- Ignoring wrapper discount because "we use AI"
- Cherry-picking comparable transactions
- Ignoring foundation-model platform risk
- Single-point multiple with no range
- Mixing SaaS / AI / Agent adjustments without showing each
- Ignoring geographic discount in emerging markets
- Pricing on TAM rather than on operating evidence

## Outputs

- Adjusted multiple range (low / base / high)
- Adjustment trail (SaaS base -> AI adjustment -> Agent adjustment with each component)
- Comparable transactions table
- Pre-money valuation range
- Stress on valuation under tail risks
- Investor-archetype-specific multiples
- Sensitivity to key drivers

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Comparable-transactions scan | quarterly | Head of Strategy | new comparable that moves range |
| Moat-vs-wrapper rescore | quarterly | (per `saas-agent-moat-and-wrapper-risk`) | -3 points |
| Foundation-model platform risk | quarterly | CTO + CEO | provider ships in category |
| Multiple range refresh | quarterly | CFO + CEO | multiple drifts >20% |
| Pre-round valuation set | per-round | CEO + Board | round opens |

## References

- `references/saas-agent-valuation-adjustments.md` — adjustment table by archetype and dimension
- `skills/meta-valuation/SKILL.md` — SaaS valuation parent
- `skills/meta-ai-valuation-adjustments/SKILL.md` — AI valuation parent
- `skills/saas-valuation-and-fundraising-strategy/SKILL.md` — SaaS fundraising
- `skills/06-competitive-analysis/saas-agent-moat-and-wrapper-risk/SKILL.md` — moat score input
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — UE input
- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — stress input
- `skills/11-funding-request/saas-agent-funding-stage-playbook/SKILL.md` — funding consumer
- `book-extractions/agent-products-business-plan-audit-2026.md` — agent audit

## Africa / Uganda Application Notes

- **African discount on agent valuations** is typically -15 to -35% on US / EU baseline; partly market-discovery, partly liquidity, partly DFI-co-investment-norms
- **Sovereign-AI positioning premium** — agents with credible in-country compute / data residency / regulator engagement in KE / NG / ZA / RW / EG can earn 10-25% premium versus offshore competitors for the same vertical (public-sector procurement preference)
- **African DFI / multilateral co-investment** can lower required institutional multiple (DFI patient capital tolerates longer payback); document DFI co-investment intent in the valuation thesis
- **Agent comparable-transactions in Africa** are sparse in 2025-2026; rely on global comparables adjusted; document the adjustment explicitly
- **Currency-of-record** matters — institutional rounds price in USD; report multiples in USD; report local-currency-equivalent for DFI / strategic
- **Sovereign-AI envelopes** (RW innovation envelope; KE Talanta; NG NITDA implementation; ZA Presidential 4IR; EG infrastructure) can be valuation-supportive if executed; document trajectory
- **Liquidity discount** — African secondary markets thin; expect 10-15% liquidity discount in pre-money compared to US comparables; reduces at growth-round and trade-sale-eligible stages
