---
source: Mersch ch. 1; 2024-2026 AI-investor pitch practice; engine synthesis
frameworks: [AI archetype declaration; AI metrics in exec summary; AI moat one-liner; AI risk one-liner; AI funding-use breakdown]
section: 01-executive-summary
cross-reference: [saas-ai-unit-economics-and-cogs, saas-ai-moat-and-defensibility, saas-ai-pricing-strategy, saas-ai-funding-stage-playbook]
---

# SaaS AI Executive-Summary Block

The AI block that should sit inside the executive summary of any AI-feature-led SaaS plan. ~150-300 words. Investors look here first.

## 1. Required elements

1. **AI archetype declaration** (one sentence) — which of the four:
   - AI-native vertical SaaS
   - SaaS-with-AI-features
   - AI-platform / AI-as-infrastructure
   - AI-services productising

2. **AI revenue share** (one number) — what % of ARR is AI-attributable

3. **AI Gross Margin** (one number with trajectory) — current and 3-year target

4. **AI-cost-as-%-of-ARR** (one number) — the headline cost diagnostic

5. **AI moat one-liner** — the moat-thesis paragraph from `saas-ai-moats-and-defensibility-checklist.md` Section 6, compressed to one sentence

6. **AI risk one-liner** — the top-3 AI risks and mitigation in one sentence (cost / model / regulatory)

7. **AI funding-use breakdown** — what % of the funding ask goes to AI infrastructure, AI hiring, AI eval / governance, training-data acquisition

8. **AI milestones** — the 3 AI-specific milestones this round of capital funds

## 2. Template

> **AI strategy.** [Company] is an [archetype declaration: e.g. "AI-native vertical SaaS for dairy cooperatives" / "SaaS-with-AI-features for retail SMBs" / "AI-platform for African-language NLP"]. AI-attributable revenue is [X]% of current ARR ([$Y] of [$Z] total), with AI Gross Margin at [A]% and on trajectory to [B]% by Year 3. AI cost is [C]% of ARR today, with [D]% target by Year 3 driven by [cache, model-mix, distillation, local-model fallback — name the levers]. Our AI moat is [moat-thesis one-sentence: e.g. "proprietary 3-year cooperative-management dataset embedded in a Luganda-first AI workflow that competitors can match only by acquiring our distribution"]. Foundation-model platform risk is [mitigated by multi-provider router + vertical workflow + local-language depth]. Top AI risks are [cost spike (mitigated by multi-provider + cache), model deprecation (mitigated by migration playbook + multi-provider), hallucination liability (mitigated by reserve + human-in-loop in high-stakes flows)]. Of the [$X] capital raise, [Y]% funds AI infrastructure, hiring, evals, and governance, targeting these milestones: (1) [first eval coverage milestone], (2) [first AI-revenue milestone], (3) [first AI moat-evidence milestone].

## 3. Anti-patterns

- "We use AI to [generic capability]" — gives no archetype
- AI mentioned only in feature list — investor will discount
- AI cost stated as "low" without a number
- Moat asserted without one-line evidence
- Risk omitted from exec summary (false confidence)
- Funding-use omitting AI line
- Milestones in generic SaaS terms

## 4. Worked example — Ugandan Dairy AI Platform

> **AI strategy.** AfyaCoop is an AI-native vertical SaaS for East African dairy cooperatives. AI-attributable revenue is 55% of $1.5M ARR ($825,000), with AI Gross Margin at 70% on trajectory to 78% by Year 3. AI cost is 11% of ARR today, targeting 6% by Year 3 driven by semantic cache, fine-tuned Mistral-Small Luganda model (replacing Cohere routing for routine queries), and local hosting on Liquid Intelligent Technologies for in-region compliance. Our AI moat is a proprietary 3-year cooperative-management dataset embedded in a Luganda-first farmer-extension workflow that competitors can match only by acquiring our 200-cooperative distribution. Foundation-model platform risk is mitigated by a multi-provider router (Cohere primary; Claude Haiku fallback; self-hosted Mistral for routine) and by workflow + local-language moats foundation-model providers will not serve directly. Top AI risks are cost spike (mitigated by multi-provider + 55% cache), model deprecation (mitigated by 90-day migration playbook), and Uganda DPPA AI compliance (mitigated by in-region hosting). Of the $4M Series A raise, 35% funds AI infrastructure ($800k), AI hiring (3 ML engineers), eval pipeline build, and governance committee implementation, targeting (1) eval coverage 75% by Q4, (2) AI-revenue $2.5M by month 18, (3) Luganda model deployment with quality eval beating GPT-4 on dairy-domain benchmarks.

This block sits in the executive summary at maximum ~280 words.

## 5. Living-plan link

This block is refreshed quarterly or on material AI event. It's pulled directly from the outputs of `saas-ai-unit-economics-and-cogs`, `saas-ai-moat-and-defensibility`, `saas-ai-risk-and-stress-test`, `saas-ai-funding-stage-playbook`.

## 6. Africa context cue

For African plans, the block should signal: local-language coverage, in-region compliance, local talent / partnerships, sovereign-AI posture if applicable. These are the differentiators that move investors past the geography discount.
