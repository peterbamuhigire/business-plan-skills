---
name: meta-ai-valuation-adjustments
description: Use when aI-feature-led SaaS plan is being valued for a priced round, secondary, or strategic acquisition. Use financial projections for model construction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Meta — AI Valuation Adjustments Skill

## Overview

Standard SaaS valuation methods (ARR multiple, Rule-of-40-adjusted multiple, DCF, venture method, Berkus / Scorecard at early stage) give the SaaS base case. AI changes the multiple — sometimes up, sometimes down — and the engine should model both directions explicitly rather than assuming "AI premium." This skill installs the adjustment logic.

The output is a valuation range with: SaaS base multiple → AI premium / discount → adjusted multiple → adjusted enterprise value, with explicit reasoning for each adjustment.

## Use When

- AI-feature-led SaaS plan is being valued for a priced round, secondary, or strategic acquisition
- A term sheet is being negotiated and AI thesis affects the valuation
- A board-level discussion of valuation strategy needs an AI overlay
- A comparison set (precedent multiples) needs AI-adjustment to be applicable
- Strategic-buyer modelling needs AI-attribution discipline

## Do Not Use When

- AI is internal-efficiency only — use `meta-valuation` + `saas-valuation-and-fundraising-strategy`
- Plan is bank-loan only (asset / DSCR-based valuation; AI is incidental)
- Valuation is fixed by tender / regulatory mechanism

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Valuation Adjustments brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
| Current accounting, tax, valuation, or pricing basis | Finance owner, accounting records, signed contracts, and current authoritative sources | Conditional | Mark the treatment unresolved and require qualified professional review. |
- Standard SaaS valuation output (`saas-valuation-and-fundraising-strategy` + `meta-valuation`)
- AI bankability scorecard (`meta-ai-bankability-and-investor-readiness`)
- AI moat score (`saas-ai-moat-and-defensibility`)
- AI economics (`saas-ai-unit-economics-and-cogs`)
- Foundation-model platform-risk statement
- Comparable transactions and trading multiples (with AI-attribution)

## Workflow

1. **Establish the SaaS base multiple** from `saas-valuation-and-fundraising-strategy`. This is the starting point. AI premium/discount adjusts from here, not from a hypothetical "AI multiple."
2. **Declare the archetype** per Part 1 of `book-extractions/ai-on-saas-business-plan-audit-2026.md` (AI-native vertical SaaS / SaaS-with-AI-features / AI-platform / AI-services productising). Multiples differ by archetype.
3. **Apply the AI-premium drivers** — each adjustment with reasoning and magnitude:
   - **Real data moat** (proprietary data accruing, not buyable) → +0.5x to +2x
   - **Real workflow moat** (AI embedded in workflow with switching cost) → +0.25x to +1x
   - **AI-native product** (the product IS AI, not augmented) → +0.5x to +1.5x
   - **Demonstrated AI gross margin >70%** in regulated vertical → +0.25x to +0.75x
   - **Eval discipline + governance maturity** (reduces incident risk) → +0.1x to +0.5x
   - **Local-language / sovereign-AI moat** in regulated jurisdiction → +0.25x to +1x
   - **AI-revenue >40% of total ARR + growing** → +0.25x to +0.75x
4. **Apply the AI-discount drivers** — each adjustment with reasoning and magnitude:
   - **LLM-wrapper / commodity-feature exposure** → -0.5x to -1.5x
   - **Foundation-model platform risk** (provider could enter category) → -0.25x to -1.5x
   - **AI-cost-as-%-of-ARR >15%** → -0.25x to -0.75x
   - **Declining AI Gross Margin trajectory** → -0.25x to -1x
   - **Hallucination-liability exposure unreserved** in regulated vertical → -0.5x to -2x
   - **Eval coverage <30%** → -0.25x to -0.75x
   - **Vendor concentration >80% single provider** → -0.25x to -0.5x
   - **Training-data provenance gap** (lawsuit risk) → -0.5x to -2x
   - **No AI governance committee + AI policy** → -0.1x to -0.5x
5. **Apply the foundation-model platform-risk adjustment** explicitly. This is the most-asked diligence question in 2026 AI valuation. Magnitude scales with how vertical / how moated the company is — vertical specialists with workflow moat have less platform risk than horizontal LLM-wrappers.
6. **Apply the comparable-transaction overlay** — adjust the multiple toward observed AI premiums / discounts in recent transactions in the same vertical / stage.
7. **Run the sensitivity** — show valuation range across plausible adjustment combinations (Bull / Base / Bear).
8. **Apply the strategic-buyer overlay** — if the plan contemplates strategic acquisition, model how a buyer with foundation-model exposure (Microsoft, Google, Amazon) values you vs a buyer without (Salesforce, Oracle, ServiceNow, vertical incumbents).
9. **State the valuation thesis** in one paragraph that survives an experienced investor's first push-back.
10. **Wire to living plan** — adjustment factors are dynamic; reassess on major comparable transaction, major foundation-model release, regulatory shift.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the AI valuation overlay and that the decision concerns whether AI capability merits a premium or platform-risk discount.
- **Stop condition:** halt the affected conclusion if required evidence is missing (gross-margin trajectory, evaluation coverage, and moat evidence) or if the work could lead to this identified risk: paying for a provider dependency as if it were proprietary IP.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Archetype-Adjusted Multiple Bands (2026 indicative)

| Archetype | SaaS base | AI premium range | AI discount range | Net plausible band |
|---|---|---|---|---|
| **AI-native vertical SaaS (Rule-of-40 ≥40, ARR growth >50%)** | 10-15x ARR | +1x to +3x | -0.5x to -1.5x | 10x to 17x |
| **SaaS-with-AI-features (Rule-of-40 ≥30)** | 6-10x ARR | +0.25x to +1x | -0.5x to -1x | 6x to 11x |
| **AI-platform (Rule-of-40 ≥30, GM ≥50%)** | 8-12x ARR | +1x to +3x | -1x to -3x | 7x to 14x |
| **AI-services productising (mixed)** | 1.5-4x revenue | +0.5x to +1x | -0.5x to -1x | 1.5x to 5x |

(These bands are indicative; specific transactions and stage adjust them materially.)

## Quality Bar

- Archetype declared
- Each premium / discount adjustment named, sourced, and quantified
- Foundation-model platform-risk adjustment explicit
- Comparable-transaction overlay applied
- Bull / Base / Bear range produced
- Strategic-buyer overlay applied where relevant
- Thesis paragraph defensible against pushback
- Living-plan cadence on adjustment factors

## Anti-Patterns

- "AI is hot, multiply by 1.5x" without specifying which drivers
- AI premium claimed without moat evidence
- Foundation-model platform risk omitted
- Only premiums applied; discounts ignored
- No comparable-transaction reference
- No strategic-buyer overlay when exit-strategy contemplates strategic acquisition


- Applying the wrong neighbouring route to meta ai valuation adjustments. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Valuation Adjustments deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Adjusted valuation range (Bull / Base / Bear)
- Per-adjustment table (driver × magnitude × reasoning)
- Foundation-model platform-risk statement and adjustment
- Comparable-transaction overlay
- Strategic-buyer overlay (if relevant)
- Valuation thesis paragraph
- Cross-references to bankability scorecard, moat score, AI economics

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Adjustment-factor reassessment | quarterly | CFO + CEO | drift in any driver |
| Comparable-transaction watch | quarterly | CFO | major precedent |
| Foundation-model commoditisation watch | monthly | CTO / Head of AI | provider releases compete |
| Regulatory shift watch | quarterly | Head of Legal | enforcement / new rule |
| Strategic-buyer landscape | semi-annual | CEO | new acquirer emerges |

## References

- `references/saas-ai-valuation-adjustments.md` — full adjustment table + worked examples
- `skills/meta-valuation/SKILL.md` — base valuation discipline
- `skills/saas-valuation-and-fundraising-strategy/SKILL.md` — SaaS valuation
- `skills/meta-ai-bankability-and-investor-readiness/SKILL.md` — feeds adjustments
- `skills/06-competitive-analysis/saas-ai-moat-and-defensibility/SKILL.md` — moat feeds adjustments
- `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md`
- `book-extractions/mersch-hacking-saas-extraction.md` — SaaS valuation discipline
- `book-extractions/walling-saas-playbook-extraction.md` — exit discussion

## Africa / Uganda Application Notes

- **African AI startups carry geography discount** in generalist investor portfolios — net 10-30% multiple haircut typical. AI premium drivers must outweigh this baseline geography discount to net positive.
- **DFI / impact-buyer valuations** weight IRR-floor + impact KPIs alongside multiples; the AI adjustment logic also applies but the weights shift.
- **Strategic-buyer landscape in Africa** is thinner; few local strategic acquirers can pay tech-multiples; international acquirers (Visa-Network, Stripe / Paystack, SAP, Microsoft, Google, regional telcos like MTN, Safaricom, Vodacom, Liquid) are the realistic exit buyers.
- **Local-language and sovereign-AI moats** translate to real valuation premium with regional strategic buyers and DFIs but less so with US-based generalist VCs.
- **Currency convention** — most international valuations USD-denominated; track both USD and local-currency valuations and explain FX impact.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| AI valuation overlay decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to paying for a provider dependency as if it were proprietary IP. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the AI valuation overlay; adding a sourced AI adjustment to the valuation schedule is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If gross-margin trajectory, evaluation coverage, and moat evidence cannot be obtained, return a qualified AI valuation overlay covering only the checks that remain supportable. Leave this decision unresolved: whether AI capability merits a premium or platform-risk discount. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: whether AI capability merits a premium or platform-risk discount | Record the conclusion, source trail, owner, and review trigger in the AI valuation overlay. | Risk of paying for a provider dependency as if it were proprietary IP |
| Material evidence conflicts or remains uncertain | Compare a no-premium case with adjustments supported separately by margin, moat, evaluation, and platform-risk evidence. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: gross-margin trajectory, evaluation coverage, and moat evidence | Mark the decision on whether AI capability merits a premium or platform-risk discount `not assessed` in the AI valuation overlay, and send it to the valuation lead and transaction adviser. | Otherwise, the work risks paying for a provider dependency as if it were proprietary IP |

## Quality Standards


Accept the AI valuation overlay only when evidence is sufficient for this decision: whether AI capability merits a premium or platform-risk discount. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of paying for a provider dependency as if it were proprietary IP.

## Worked Example


A product calls a third-party model through a thin interface yet claims an AI moat. The overlay applies platform-risk and wrapper adjustments rather than a premium, pending proprietary data or workflow evidence.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the AI valuation overlay, using the reporting basis and effective date supported by gross-margin trajectory, evaluation coverage, and moat evidence. Reconcile the treatment to the model and narrative, and have the valuation lead and transaction adviser review the treatment, reconciliation, and exposure to this risk: paying for a provider dependency as if it were proprietary IP.

<!-- dual-compat-end -->
