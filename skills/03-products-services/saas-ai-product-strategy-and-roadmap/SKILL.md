---
name: saas-ai-product-strategy-and-roadmap
description: AI product strategy and roadmap for a SaaS plan — feature-vs-platform, AI-native vs AI-augmented, build-vs-buy-vs-host-vs-orchestrate, model-router architecture, eval-driven product development, model-deprecation strategy, AI-feature roadmap by ARR milestone with explicit cost gating. Sits inside Section 03 (Products & Services); coordinates with Sections 06, 10, 12, and 14.
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
