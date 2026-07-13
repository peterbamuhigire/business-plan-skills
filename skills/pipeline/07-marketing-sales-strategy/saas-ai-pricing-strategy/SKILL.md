---
name: saas-ai-pricing-strategy
description: Use when producing or reviewing the saas ai pricing strategy component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS AI Pricing Strategy Skill

## Overview

Generic SaaS pricing skills (Kennedy/Marrs premium positioning; `saas-pricing-and-packaging-strategy` for tier/freemium/usage architecture) cannot answer questions specific to AI feature pricing: how to include AI in a tier without margin disaster, when to meter, when to charge by outcome, how to design allowance × overage, how to price across FX corridors when AI cost is USD-denominated and ARPU is in UGX / KES / NGN / ZAR / GHS. This skill specifies the AI pricing architecture and the discipline behind it.

The output is a pricing architecture document with: tier × included-AI-allowance × model-mix policy × overage rate × add-on tier × FX corridor × margin-protection mechanic. It feeds Section 07 and reconciles back to `saas-ai-cost-of-tenant-calculator`.

## Use When

- AI features are customer-facing and material to value proposition
- Tier design needs to defend AI margin
- Existing pricing is causing margin compression from heavy-AI tenants
- Investor or DFI has asked "how does your pricing protect AI margin?"
- A pricing experiment is being designed
- Multi-currency / cross-border pricing requires FX-aware architecture

## Do Not Use When

- AI is internal-efficiency only (no customer-facing AI) — use `meta-pricing-strategy`
- Plan is pre-PMF and pricing is still notional — produce a hypothesis architecture but don't over-engineer
- Pricing is mandated externally (regulated, government tender, RFP-bound)

## Required Inputs

- Tier list with current pricing and AI features
- Output from `saas-ai-cost-of-tenant-calculator` (per-tenant AI cost by tier)
- Customer-willingness-to-pay evidence (interviews, win-rate data, competitor pricing)
- FX exposure (cost currency vs revenue currency)
- Competitive pricing snapshot (especially "AI included" claims)
- Buyer persona — SMB / mid-market / enterprise / public-sector / consumer

## Workflow

1. **Decide the pricing model** per `references/saas-ai-pricing-architecture.md`:
   - **Included-with-tier** (AI cost absorbed; usage capped via fair-use) — works for low-AI-cost-share products
   - **Metered (per-query / per-1k-token / per-document / per-seat)** — works for high-variance usage; commodity perception risk
   - **Hybrid (included allowance + overage rate)** — usually the right answer; predictable + margin-protected
   - **AI-as-add-on (separate AI tier or upgrade)** — works when AI is differentiated value, not table stakes
   - **Outcome-based ("pay only when AI succeeds")** — premium positioning; requires success-definition rigour
2. **Set the allowance per tier** using `saas-ai-cost-of-tenant-calculator` data — allowance should cover median tenant usage at target margin, with overage rate covering high-decile usage at cost+markup.
3. **Set the overage rate** — typical: 1.5-3× marginal AI cost. The overage rate is the margin lever; it should not feel punitive to mid-decile users (they should never hit it).
4. **Map model-mix to pricing tier** — premium tiers route to premium models (more accurate, slower-deprecated); lower tiers route to cheap models with quality SLAs. Be honest with customers about model-mix differences.
5. **Apply the FX corridor** — when ARPU is in local currency and AI cost is USD, set tier prices with FX headroom. Re-price quarterly or on >7% FX move.
6. **Apply the competitive overlay** — if competitors include AI "free," design positioning (quality, transparency, vertical-specificity, governance) rather than match price. Cost-plus + competitor-match are the two failure modes of SaaS AI pricing (Kennedy 9 Failures discipline).
7. **Apply the customer-segment lens** — SMB / mid-market / enterprise / public-sector have different AI-price-tolerance and different procurement cycles; align packaging.
8. **Design the AI-only upgrade path** — for customers without AI today, the upgrade ladder (no-AI → AI-light → AI-full) is an expansion-revenue lever.
9. **Stress-test the pricing** — what happens to margin if usage doubles? if provider doubles pricing? if FX depreciates 20%? if hallucination event forces capacity reduction?
10. **Wire to living plan** — pricing cadence (quarterly review default), AI cost-as-%-of-ARPU monthly, AI overage realisation monthly.

## Pricing Decision Matrix

| Customer profile | AI cost share of ARPU | Recommended model |
|---|---|---|
| SMB / high-volume / commodity | <5% | Included; tier-gated; fair-use cap |
| SMB / heavy AI usage | 5-15% | Hybrid (included allowance + overage) |
| Mid-market | 5-15% | Hybrid + premium-AI add-on |
| Enterprise | <5% (large ARPU absorbs) | Included; SLA-backed; custom model option |
| Public-sector / NGO | 5-25% (often heavy use, sensitive pricing) | AI-as-add-on; usage-based with floor |
| Consumer / freemium | 0-5% (free), 5-20% (paid) | Strict allowance + overage; premium AI tier |
| Outcome-priced (legal, sales, recruiting) | n/a (priced on outcome) | Outcome-based with floor |

## Quality Bar

- Pricing model decision explicit and defended
- Allowance × overage architecture defined per tier
- Model-mix mapped to tier with honest disclosure
- FX corridor and re-pricing rule defined
- Competitive overlay analysed; differentiation thesis stated
- Customer-segment alignment explicit
- Pricing stress-tested across cost, usage, FX, provider-pricing scenarios
- AI Gross Margin protected at planned utilisation
- Margin trajectory positive across 3-year plan
- Living-plan cadence assigned

## Anti-Patterns

- "AI included, no usage cap" with no margin model behind it
- Cost-plus AI pricing (this is the Kennedy Failure #1)
- Competitor-match AI pricing ("they're charging $X so we charge $X")
- Metered-only pricing for a small-ACV SMB segment (causes bill-shock churn)
- Outcome-based pricing without rigorous success-definition (becomes dispute-machine)
- Hiding model-mix from customers (eroded trust when they discover)
- One global price across currencies that ignores FX
- No mechanism to re-price when provider raises rates
- Pricing decided by Finance alone or Sales alone — must reconcile

## Outputs

- Pricing architecture document (tier × allowance × overage × add-on × model-mix × FX)
- Pricing decision rationale per tier
- Margin sensitivity analysis
- Competitive pricing overlay
- Customer-segment alignment notes
- Re-pricing trigger rules
- Pricing experiment backlog (3-5 tests)

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| AI cost-as-%-of-ARPU by tier | monthly | CFO + Head of GTM | >planned by 3pp |
| Overage revenue / overage events | monthly | CFO + Head of CS | overage events <5% or >25% of tenants |
| FX corridor | monthly | CFO | move >5% |
| Provider pricing | as-published + monthly | Head of AI | any change |
| Pricing experiment outcomes | per-experiment + quarterly | Head of GTM | as designed |
| Full pricing review | quarterly | CEO + CFO + Head of GTM | strategic |

## References

- `references/saas-ai-pricing-architecture.md` — full architecture spec with worked example
- `references/ai-feature-pricing-and-positioning.md` — positioning discipline (in `07-marketing-sales-strategy/references/`)
- `skills/saas-pricing-and-packaging-strategy/SKILL.md` — sister skill (generic SaaS pricing)
- `skills/meta-pricing-strategy/SKILL.md` — Kennedy/Marrs discipline (anti cost-plus, anti competitor-match)
- `skills/10-financial-projections/saas-ai-cost-of-tenant-calculator/SKILL.md` — cost input
- `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md` — margin output
- `book-extractions/walling-saas-playbook-extraction.md` — pricing chapters
- `book-extractions/mersch-hacking-saas-extraction.md` — pricing-as-CFO-discipline
- `book-extractions/kennedy-no-bs-price-strategy-extraction.md` — anti-cost-plus discipline

## Africa / Uganda Application Notes

- FX corridor is the binding pricing constraint. Set local-currency tier prices with 10-15% FX headroom; re-price on >7% FX move or quarterly, whichever comes first.
- Mobile-money fees (1.5-2.5%) eat margin alongside AI cost; model both.
- Public-sector and NGO customers procure on annual cycles with USD-pegged budgets — USD pricing for these segments is often easier than local.
- Donor-funded customers (NGOs, programmes) are AI-heavy users (analysis, reporting); design AI-as-add-on rather than included.
- Local-language inference is more expensive per task; charge premium for local-language AI tiers, not less.
- Sovereign-AI / data-residency requirements drive a separate enterprise tier (in-country hosting + dedicated model + governance) that supports premium pricing.
- WhatsApp-channel AI (chatbots, voice notes) is the highest-tolerance, lowest-friction AI usage profile in Africa — design pricing that captures this.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| ICP, buying process, channel evidence, price tests, unit economics, and sales capacity for saas ai pricing strategy | Customer research, CRM records, approved financial model, and sales owner | Yes | If absent, price, margin, conversion, or capacity evidence is unavailable, return a testable commercial hypothesis and cap the recommendation at pilot scale. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Pricing or packaging decision with margin and adoption guardrails | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai pricing strategy exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai pricing strategy release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Price metric rationale, willingness-to-pay evidence, margin bridge, and failure thresholds | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai pricing strategy decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai pricing strategy review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai pricing strategy, the controlling focus is AI feature packaging, inference-cost exposure, value metric, adoption friction, and price testing. This skill may analyse commercial options and draft tests; it may not launch prices, purchase media, contact prospects, alter contracts, or promise outcomes without explicit authority. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai pricing strategy, loss of evidence about AI feature packaging, inference-cost exposure, value metric, adoption friction, and price testing activates degraded mode. If the controlling saas ai pricing strategy evidence is unavailable, the same boundary applies. When price, margin, conversion, or capacity evidence is unavailable, return a testable commercial hypothesis and cap the recommendation at pilot scale. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai pricing strategy, a package or channel grows headline demand while weakening gross margin, trust, or delivery capacity| reject or constrain it, quantify the guardrail, and test the next credible option | Growth recommendations can consume cash or create obligations the business cannot fulfil |
| For saas ai pricing strategy, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai pricing strategy decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai pricing strategy, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete pricing or packaging decision with margin and adoption guardrails, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai pricing strategy decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect icp, buying process, channel evidence, price tests, unit economics, and sales capacity and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce pricing or packaging decision with margin and adoption guardrails with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Pricing or packaging decision with margin and adoption guardrails must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Price metric rationale, willingness-to-pay evidence, margin bridge, and failure thresholds must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas ai pricing strategy, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai pricing strategy, treating an unavailable icp, buying process, channel evidence, price tests, unit economics, and sales capacity as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing pricing or packaging decision with margin and adoption guardrails that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

An AI drafting feature saves time but its inference cost varies little by seat. Test a tiered feature price against willingness to pay and set a usage guardrail rather than passing raw token charges to customers.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai pricing strategy; no local deep-dive reference is declared.
- For saas ai pricing strategy claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
