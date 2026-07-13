---
name: saas-ai-unit-economics-and-cogs
description: Use when producing or reviewing the saas ai unit economics and cogs component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS AI Unit Economics & COGS Skill

## Overview

Generic SaaS unit economics treats AI as one cost line. AI-aware investors in 2026 require the AI cost line decomposed into its constituent waterfall, separately modelled, separately sensitised, and separately reported. This skill installs that discipline.

The output is a four-layer view of the AI cost-of-revenue:

1. **Direct AI COGS** — tokens, embeddings, fine-tuning amortisation, vector store, GPU reservation.
2. **Indirect AI COGS** — eval pipeline cost, observability / safety infra, model-router infra, caching infra.
3. **AI reserves** — hallucination-liability reserve, retraining-cycle reserve, model-migration reserve.
4. **AI overhead allocation** — share of AI-team payroll, share of AI tooling, share of governance.

Together these produce the AI Gross Margin, AI Contribution Margin per tier, blended-GM impact, AI-cost-as-%-of-ARR, and the diagnostics investors and DFIs look for.

## Use When

- AI is a material cost in a SaaS / ICT plan (typically >2% of ARR or load-bearing to product)
- Section 10 (Financial Projections) is being built for an AI-feature-led plan
- Investors or DFIs have asked for AI gross margin specifically
- A plan claims AI-native or AI-first and needs to defend the cost economics
- Pricing or packaging decisions need AI-cost sensitivity
- The plan must pass `meta-ai-bankability-and-investor-readiness`

## Do Not Use When

- AI is incidental (internal-efficiency only, no customer-facing AI cost) — use `14-ai-integration` plus generic `saas-unit-economics-and-cohort-model`
- The plan is pre-PMF and no real AI usage data exists — use directional inputs with explicit sensitivity ranges, and pair with `saas-mvp-and-product-market-fit-strategy`
- The business is not SaaS / subscription / recurring revenue

## Required Inputs

- AI architecture description (which models, which providers, RAG / fine-tuning / agentic / multi-model router)
- Provider pricing snapshot (per-1k-token, per-embedding, per-fine-tune-token, per-GPU-hour, per-vector-store-row)
- Per-tenant usage profile by tier (queries/month, tokens/query, embeddings/month, document volume)
- Cache-hit ratio (or assumed range)
- Model-mix policy (which queries route to which model)
- Eval pipeline cost (eval-runs/month × tokens-per-run × model-cost)
- Retraining cadence (quarterly / annual / triggered)
- Hallucination-liability exposure (high-stakes vs low-stakes feature mix)
- Currency exposure (USD-denominated AI cost vs local-currency ARPU)

## Workflow

1. **Document the AI architecture** in one paragraph + one diagram (or text-based component list). Without this, the cost model is fiction.
2. **Build the per-tenant AI cost** per `references/saas-ai-cost-of-tenant-calculator.md` — token COGS + embeddings + amortised fine-tune + eval share + reserve + overhead share.
3. **Build the AI COGS waterfall** — direct + indirect + reserves + overhead allocation, monthly Year 1, quarterly Years 2–5.
4. **Compute AI Gross Margin** = (AI-attributable revenue − AI COGS) / AI-attributable revenue. AI-attributable revenue uses the AI-TAM attribution discipline (`ai-tam-attribution.md`) — usually a fraction of total ARPU, not all of it, unless the product is AI-native.
5. **Compute AI Contribution Margin per tier** — for each tier: (tier ARPU × AI-attribution %) − tier AI cost. Identify tiers where AI is margin-eating.
6. **Compute blended-GM impact** — AI COGS as a share of total COGS; impact of AI on company-level GM trajectory over the 5-year plan.
7. **Compute AI-cost-as-%-of-ARR** — the headline diagnostic investors quote. Set targets: <5% (excellent), 5–10% (typical), 10–15% (margin-strained), >15% (alarm).
8. **Apply mitigation levers** in scenarios — cache-hit increase, model-mix downshift (route routine queries to cheaper models), usage caps, AI-as-add-on tier, prompt-token optimisation, response-token truncation, semantic compression.
9. **Sensitivity-test** — ±30% token usage, ±50% provider pricing, ±20pp cache-hit ratio, ±20% FX, model-deprecation forced migration cost.
10. **Stress-test** — provider doubles pricing; foundation model deprecates; hallucination event triggers reserve drawdown; GPU scarcity raises hosting cost 2×.
11. **Wire into living-plan governance** — assign cadence, owners, variance thresholds per the AI Living-Plan Cadence below.
12. **Diagnose the binding AI-cost constraint** — which lever (cache, model-mix, prompt design, tier design, pricing) most improves AI margin?

## Quality Bar

- AI architecture stated explicitly; no "we use GPT" wave-of-hand
- All cost components computed with formulas and assumptions
- AI Gross Margin and AI Contribution Margin separately computed and stated
- AI-cost-as-%-of-ARR reported as headline metric
- Tier-by-tier AI contribution stated; margin-eating tiers flagged
- Sensitivity covers usage, pricing, cache-hit, FX
- Stress scenarios cover cost spike, model deprecation, hallucination event, GPU scarcity
- Mitigation playbook explicit, with expected impact per lever
- Living-plan cadence assigned; eval / cost / margin owners named
- A sceptical CFO at a Series A AI fund would not laugh

## Anti-Patterns

- "AI cost ~5% of revenue" with no calculation behind it
- Token cost without prompt-token vs completion-token split (completion tokens are 2–4× pricier on most providers)
- Ignoring embedding cost when RAG is core to the product
- Ignoring eval cost — evals can equal 10–30% of production AI spend
- No cache-hit ratio modelled (semantic caching typically saves 30–60%)
- Single-model assumption when product clearly needs router logic
- USD-only modelling when ARPU is in local currency (FX is real)
- No hallucination-liability reserve in a regulated vertical
- No reserve for forced model migrations (these happen every 12–24 months)
- "We'll switch to cheaper models" stated as cost-reduction without quality-impact modelling

## Outputs

- AI architecture description (one paragraph + component list)
- AI COGS waterfall (monthly Y1, quarterly Y2–5)
- Per-tenant AI cost by tier
- AI Gross Margin (recurring)
- AI Contribution Margin per tier
- AI-cost-as-%-of-ARR diagnostic
- Sensitivity + stress analyses
- Mitigation playbook with prioritised levers
- Living-plan cadence assignment

## Living-Plan AI Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Per-tenant AI cost | monthly | CFO + Head of AI | +20% MoM |
| AI Gross Margin | monthly | CFO | -3pp MoM |
| AI-cost-as-%-of-ARR | monthly | CFO | >15% alarm |
| Token usage / tenant | weekly | Head of AI | +30% week-over-week |
| Cache-hit ratio | weekly | Head of AI | -10pp from baseline |
| Provider pricing watch | monthly | Head of AI / CTO | any provider change |
| Eval cost share | monthly | Head of AI | >30% of AI COGS |
| Hallucination reserve | quarterly | CFO + Head of AI | reserve drawdown event |
| Retraining-cost line | per-cycle + quarterly review | Head of AI | actual >150% planned |
| Model-mix policy | quarterly | Head of AI | competitor parity at cheaper cost |

## References

- `references/saas-ai-unit-economics-template.md` — formulas, worked example, AI COGS waterfall
- `references/saas-ai-cost-of-tenant-calculator.md` — calculator spec, sensitivity matrix
- `references/saas-ai-pricing-architecture.md` — pricing levers that protect AI margin
- `references/saas-ai-stress-test-scenarios.md` — stress scenarios with quantified impact
- `skills/saas-unit-economics-and-cohort-model/SKILL.md` — sister skill (standard SaaS unit economics)
- `skills/14-ai-integration/references/saas-ai-feature-roadmap-in-business-plan.md` — AI roadmap discipline
- `skills/meta-living-plan-governance/SKILL.md` — living-plan governance
- `book-extractions/mersch-hacking-saas-extraction.md` — CFO-grade SaaS discipline
- `book-extractions/tod-building-multi-tenant-saas-architectures-extraction.md` — multi-tenant cost realities

## Africa / Uganda Application Notes

- AI cost is USD-denominated; ARPU is typically local-currency. FX is a real margin risk; model the FX corridor explicitly (UGX 3,500-3,900/$, NGN 1,500-1,800/$, KES 128-145/$ as 2025/26 ranges).
- Cache-hit ratios are higher than typical US benchmarks in African vertical SaaS because user queries are more repetitive within tightly-defined verticals (cooperatives, clinics, schools) — model 40-60% cache-hit, not 20-30%.
- Local-language inference (Swahili, Hausa, Yoruba, Amharic, Luganda) is often more expensive per task because it requires more tokens or fine-tuned models — separately line-item.
- Eval cost in regulated verticals (health, finance) is higher because production sampling rates must be higher to meet sectoral expectations.
- Hallucination-liability reserve should reflect the regulatory environment — Kenya DPC, Nigeria NITDA / NDPC, Uganda NITA-U, South Africa Information Regulator all have evolving AI-incident expectations.
- GPU-reservation cost: if hosting in Cape Town (af-south-1), Johannesburg (africa-south1), or Liquid / Cassava / MainOne, expect 1.5-3× US/EU pricing; model the premium explicitly.
- Track all AI cost in USD for international investors, local currency for DFI / bank submissions.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon for saas ai unit economics and cogs | Client records, approved operating model, finance owner, and accounting doctrine | Yes | If absent, contract terms, usage evidence, framework, or cost drivers are unavailable, isolate the affected schedule, label it unassessed, and do not force the model to balance with a plug. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Unit-economics model with task or tenant cost bridge | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai unit economics and cogs exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai unit economics and cogs release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Formula trace, source/assumption register, three-statement or schedule reconciliation, and finance-gate record | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai unit economics and cogs decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai unit economics and cogs review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai unit economics and cogs, the controlling focus is AI feature inference cost, gross margin, usage intensity, support cost, and cohort economics. This skill may inspect records and calculate planning scenarios in read-only mode; it may not post entries, change ledgers, set accounting policy, certify IFRS treatment, or release statutory values without authorised professional review. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai unit economics and cogs, loss of evidence about AI feature inference cost, gross margin, usage intensity, support cost, and cohort economics activates degraded mode. If the controlling saas ai unit economics and cogs evidence is unavailable, the same boundary applies. When contract terms, usage evidence, framework, or cost drivers are unavailable, isolate the affected schedule, label it unassessed, and do not force the model to balance with a plug. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai unit economics and cogs, commercial billing, cash receipt, service delivery, and accounting recognition occur in different periods| model each event separately, reconcile the bridge, and route judgemental treatment to the finance reviewer | Cash, revenue, liability, and margin can be conflated into a misleading forecast |
| For saas ai unit economics and cogs, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai unit economics and cogs decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai unit economics and cogs, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete unit-economics model with task or tenant cost bridge, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai unit economics and cogs decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce unit-economics model with task or tenant cost bridge with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Unit-economics model with task or tenant cost bridge must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Formula trace, source/assumption register, three-statement or schedule reconciliation, and finance-gate record must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas ai unit economics and cogs, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai unit economics and cogs, treating an unavailable approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing unit-economics model with task or tenant cost bridge that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A low-priced AI add-on has strong adoption but premium-model routing pushes its cohort margin below the SaaS base product. Test routing, allowance, and price changes before scaling it.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai unit economics and cogs; no local deep-dive reference is declared.
- For saas ai unit economics and cogs claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
