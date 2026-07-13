---
name: saas-ai-product-strategy-and-roadmap
description: Use when producing or reviewing the saas ai product strategy and roadmap component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS AI Product Strategy & Roadmap Skill

## Overview

Generic product strategy can describe AI features but cannot reason about AI product specifics: when AI is the product vs an augmentation, the model-router architecture, eval-driven development, model-deprecation as a planning constraint, build-vs-buy-vs-host-vs-orchestrate, and AI roadmap pacing against ARR milestones with cost gating. This skill installs the discipline.

## Use When

- Section 03 of an AI-feature-led plan is being built
- Product strategy needs to decide AI-native vs AI-augmented
- Roadmap needs to pace AI features against ARR milestones and AI cost trajectory
- Build-vs-buy decisions on AI components need to be made
- Investors are asking how the product strategy survives foundation-model commoditisation

## Do Not Use When

- AI is internal-efficiency only — use `14-ai-integration` + `03-products-services` standard
- Product is pre-architecture — use `saas-mvp-and-product-market-fit-strategy` first

## Required Inputs

- Customer-job-to-be-done (specifically where AI changes the job)
- Current architecture or MVP architecture
- Provider landscape (which foundation models, embedding models, vector stores)
- Eval-pipeline maturity
- ARR plan from `saas-mrr-arr-financial-modeling`
- Cost per feature (from `saas-ai-cost-of-tenant-calculator`)

## Workflow

1. **Decide AI-native vs AI-augmented** — is the product the AI orchestration (Devin-class) or a workflow that uses AI as a feature? Many plans fudge this; investors push hard for clarity.
2. **Decide feature vs platform** — selling AI features to end-users vs selling AI infrastructure to developers — different GTM, different unit economics, different moats.
3. **Apply the build-vs-buy-vs-host-vs-orchestrate matrix** per `references/ai-build-buy-host-orchestrate-matrix.md`:
   - **Foundation model**: buy (almost always; build only for proprietary-data moat at >$100M ARR)
   - **Embedding model**: buy
   - **Vector DB**: buy / self-host
   - **RAG orchestration**: build (this is your product)
   - **Fine-tuning pipeline**: buy / hybrid
   - **Eval / observability**: buy (Langfuse, Helicone, Arize)
4. **Design the model-router architecture** — premium models for high-stakes / complex queries; cheap models for routine; local models for cost-sensitive routine. Router policy is a strategic asset, not a tactical implementation detail.
5. **Install eval-driven development** — every AI feature ships with an eval suite. Coverage % is a plan KPI. Production sampling rate is set. Eval drift triggers replan.
6. **Define the model-deprecation strategy** — providers deprecate models on 12-24 month cycles. Plan the migration buffer, the eval-comparison protocol, and the rollback path.
7. **Build the AI roadmap by ARR milestone** with explicit cost gating per `references/saas-ai-feature-roadmap-in-business-plan.md` (already in `14-ai-integration/references/`):
   - Pre-PMF: 1-2 generic LLM-wrapper features
   - $0-$1M ARR: 3-5 domain-tuned RAG features
   - $1-$5M ARR: fine-tuning starts; per-tenant cost modelling installed
   - $5-$20M ARR: multi-model orchestration; AI-native workflows
   - $20M+ ARR: proprietary model option; enterprise AI compliance
8. **Apply the cost-gating discipline** — no AI feature ships without a per-tenant cost estimate and a tier-pricing decision. This stops the AI-features-as-margin-thieves problem.
9. **Wire to risk, moat, and pricing skills** — outputs feed `saas-ai-risk-and-stress-test`, `saas-ai-moat-and-defensibility`, `saas-ai-pricing-strategy`.
10. **Wire to living plan** — eval coverage weekly, roadmap quarterly, model-deprecation watch monthly, AI moat reassessment quarterly.

## Quality Bar

- AI-native vs AI-augmented declared
- Feature vs platform declared
- Build / buy / host / orchestrate decision per component, with reasoning
- Model-router architecture documented
- Eval-driven development installed; eval coverage stated
- Model-deprecation strategy documented
- AI roadmap by ARR milestone with cost gating
- No "ship and figure out cost later" features
- Cross-references to risk, moat, pricing, financial sections

## Anti-Patterns

- "AI features will be a tab in the UI" — feature-list product strategy
- Building foundation models pre-$100M ARR
- Single-model architecture when query mix is heterogeneous
- No eval-pipeline plan
- "We'll migrate to GPT-5 when it's out" — model deprecation not in the plan
- Roadmap not tied to ARR / cost milestones
- Build-vs-buy decided by engineering preference, not commercial logic

## Outputs

- AI-native vs AI-augmented declaration
- Feature vs platform declaration
- Build/buy/host/orchestrate decision matrix
- Model-router architecture description
- Eval-driven development plan
- Model-deprecation strategy
- AI roadmap by ARR milestone with cost gating
- Cross-references to risk, moat, pricing, financial sections

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| AI roadmap status | quarterly | Head of Product + Head of AI | milestone slip >30 days |
| Eval coverage | weekly | Head of AI / QA | -5pp |
| Model-deprecation watch | monthly | Head of AI / CTO | provider notice |
| Cost-gate before feature ship | per-feature | Head of Product + CFO | feature exceeds tier cost-of-tenant budget |
| Build-vs-buy reassessment | annual | CTO + CFO | provider trajectory change |
| AI-native vs augmented thesis | annual | CEO + Head of Product | strategic shift |

## References

- `references/ai-build-buy-host-orchestrate-matrix.md` — full decision matrix
- `skills/14-ai-integration/references/saas-ai-feature-roadmap-in-business-plan.md` — feature roadmap with ARR milestones
- `skills/03-products-services/SKILL.md` — generic product strategy
- `skills/saas-mvp-and-product-market-fit-strategy/SKILL.md` — pre-PMF product discipline
- `skills/06-competitive-analysis/saas-ai-moat-and-defensibility/SKILL.md`
- `skills/10-financial-projections/saas-ai-cost-of-tenant-calculator/SKILL.md`
- `book-extractions/walling-saas-playbook-extraction.md` — PMF and product strategy
- `book-extractions/tod-building-multi-tenant-saas-architectures-extraction.md` — architecture decisions

## Africa / Uganda Application Notes

- Mobile-first / WhatsApp-channel AI products have different architecture (short-prompt, multi-turn) and different cost profile.
- Local-language AI features should be in roadmap from day one for vertical SaaS in Africa; English-only AI for African SMB is a self-imposed ceiling.
- Build-vs-host should explicitly consider local providers (Liquid, Cassava, Raxio, MainOne) for sovereign-AI tenders.
- Offline / low-bandwidth AI design — pre-process server-side; cache aggressively; design for intermittent connectivity.
- Eval discipline in regulated African verticals (health, finance, public-sector) is more onerous; plan eval-pipeline cost accordingly.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Validated AI or agent use cases, customer evidence, architecture constraints, and roadmap economics for saas ai product strategy and roadmap | Product owner, customer research, technical lead, and approved model | Yes | If absent, customer outcome evidence, cost data, or safety constraints are unavailable, hold the affected roadmap item at discovery and return the missing validation test. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| AI product roadmap with use-case, model, data, evaluation, safety, economics, and build/buy/host gates | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai product strategy and roadmap exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai product strategy and roadmap release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Use-case scorecard, roadmap gate decisions, and dependency register | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai product strategy and roadmap decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai product strategy and roadmap review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai product strategy and roadmap, the controlling focus is AI use-case value, model choice, data readiness, evaluation, safety, and staged roadmap investment. This skill may analyse product and architecture options; it may not approve model spend, production deployment, autonomous actions, or unsupported AI capability claims. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai product strategy and roadmap, loss of evidence about AI use-case value, model choice, data readiness, evaluation, safety, and staged roadmap investment activates degraded mode. If the controlling saas ai product strategy and roadmap evidence is unavailable, the same boundary applies. When customer outcome evidence, cost data, or safety constraints are unavailable, hold the affected roadmap item at discovery and return the missing validation test. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai product strategy and roadmap, an AI or agent feature has novelty but no measurable customer outcome or affordable operating path| defer it, define the experiment and exit criterion, and keep it out of the funded roadmap | Roadmap theatre commits capital before value, cost, and safety are known |
| For saas ai product strategy and roadmap, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai product strategy and roadmap decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai product strategy and roadmap, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete ai product roadmap with use-case, model, data, evaluation, safety, economics, and build/buy/host gates, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai product strategy and roadmap decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect validated ai or agent use cases, customer evidence, architecture constraints, and roadmap economics and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce ai product roadmap with use-case, model, data, evaluation, safety, economics, and build/buy/host gates with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- AI product roadmap with use-case, model, data, evaluation, safety, economics, and build/buy/host gates must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Use-case scorecard, roadmap gate decisions, and dependency register must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas ai product strategy and roadmap, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai product strategy and roadmap, treating an unavailable validated ai or agent use cases, customer evidence, architecture constraints, and roadmap economics as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing ai product roadmap with use-case, model, data, evaluation, safety, economics, and build/buy/host gates that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

An AI demand forecast looks accurate on one historic month but has no baseline comparison or retraining plan. Keep it in discovery, define forecast-error and commercial-use gates, and stage investment only after out-of-sample evidence.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai product strategy and roadmap; no local deep-dive reference is declared.
- For saas ai product strategy and roadmap claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
