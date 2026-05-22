---
name: saas-valuation-and-fundraising-strategy
description: Produce the SaaS valuation and stage-by-stage fundraising strategy — ARR multiples, Rule-of-40-adjusted multiples, DCF for SaaS, Berkus / Scorecard / venture-method for early-stage, comparables, and the stage playbook from bootstrap → pre-seed → seed → A → growth. Complements meta-valuation (DCF/WACC/CAPM) with SaaS-specific methods and stage-appropriate fundraising plan.
---

# SaaS Valuation & Fundraising Strategy Skill

## Overview

Produce the valuation and fundraising-strategy layer of a SaaS plan using SaaS-specific methods. Generic DCF / WACC / CAPM (handled by `meta-valuation`) under-values growth-stage SaaS; SaaS investors use ARR multiples adjusted by Rule of 40 + NRR + Burn Multiple, plus venture-method working back from exit. The fundraising strategy then matches the company's stage to the right capital sources.

## Use When

- A SaaS plan needs a valuation (round, secondary, M&A, internal share scheme, ESOP refresh)
- A founder is deciding which round to raise next
- An advisor / VC is benchmarking a SaaS plan's ask vs comparables
- Africa-focused plans need to match readiness to the correct DFI / fund tier

## Required Inputs

- ARR (current + projected)
- Growth rate (T12M, T3M annualised)
- Gross margin, NRR, GRR, burn multiple, Rule of 40
- Comparables (public SaaS, private comparables, recent rounds in vertical)
- Founder equity, cap table, ESOP pool

## Workflow

1. **Compute SaaS multiples valuation:**
   - **Base ARR multiple** = function of growth rate (see references)
   - **Rule of 40 adjustment** = +/-1× per 5 points above/below 40
   - **NRR adjustment** = +/-0.5× per 10pp above/below 100%
   - **Burn Multiple adjustment** = +/-0.5× per 0.5 below/above 1.5
   - **Final multiple range** with low / base / high
2. **DCF for late-stage SaaS** (>$20M ARR, profitable or near-profitable):
   - 10-year FCF projection
   - Terminal value at exit multiple or perpetuity
   - WACC 12-15% for African private SaaS; 10-12% for international
3. **Early-stage methods** (pre-revenue / pre-PMF):
   - Berkus method (max $2-2.5M pre-money, +$500k per quality factor)
   - Scorecard method (compare to regional comparable median)
   - Venture method (work back from target exit at target IRR)
4. **Triangulate** — multiples, DCF, early-stage methods, comparables. Report a range, not a single number.
5. **Map to fundraising stage** using `references/saas-funding-stage-playbook.md`:
   - Bootstrap (no external capital)
   - Pre-seed ($50k-$500k from F&F + angels)
   - Seed ($500k-$3M from seed funds, TinySeed-style, accelerators)
   - Series A ($3M-$15M from VCs, growth-equity, DFIs)
   - Series B+ ($15M+ from growth funds, PE, strategics)
6. **Match to capital sources** suitable for the stage and the company's geography (African plans have a different stack: F&F → angels → African seed funds → DFIs / patient capital → international VCs).
7. **Compute dilution** for each scenario and assess founder economics post-raise.
8. **Cross-reference `meta-valuation`** for the deeper DCF discipline; cross-reference `saas-bankability-and-investor-readiness` for whether the company is at the right stage.

## Quality Bar

- Multiples-based valuation cited with growth, NRR, Rule of 40, burn multiple adjustments
- DCF only used where ARR justifies (>$20M with visibility); otherwise multiples + venture-method
- African-context multiples discounted vs US benchmarks (typically 30-50%)
- Stage matches capital source
- Dilution and founder economics modelled
- Plan articulates the *next* round, not just the current one

## Outputs

- Valuation range (low / base / high) with method-by-method triangulation
- Fundraising-stage playbook for the company
- Capital-source short-list with check sizes and typical terms
- Cap table model showing pre/post raise
- Founder economics scenario analysis
- Term-sheet expectations (preference, board, anti-dilution)

## AI Premium / Discount Module (mandatory for AI-feature-led plans)

When AI is material to the plan, apply the AI valuation overlay from `skills/meta-ai-valuation-adjustments/SKILL.md` and `skills/meta-valuation/references/saas-ai-valuation-adjustments.md`. The framework:

```
Adjusted multiple = SaaS base multiple
                  + Σ (AI premium drivers × magnitude)
                  − Σ (AI discount drivers × magnitude)
                  ± Foundation-model platform-risk adjustment
                  ± Comparable-transaction overlay
                  ± Strategic-buyer overlay
```

Premium drivers include real data moat (+0.5x to +2x), workflow moat (+0.25x to +1x), AI-native architecture (+0.5x to +1.5x), high AI GM in regulated vertical (+0.25x to +0.75x), local-language / sovereign-AI moat (+0.25x to +1x), eval discipline + governance maturity (+0.1x to +0.5x).

Discount drivers include LLM-wrapper / commodity exposure (-0.5x to -1.5x), foundation-model platform risk (-0.25x to -1.5x), AI-cost-as-%-of-ARR >15% (-0.25x to -0.75x), declining AI GM (-0.25x to -1x), unreserved hallucination liability (-0.5x to -2x), eval coverage <30% (-0.25x to -0.75x), training-data provenance gap (-0.5x to -2x).

Pair with the AI archetype declaration (AI-native vertical SaaS / SaaS-with-AI-features / AI-platform / AI-services productising), AI funding stage playbook (`saas-ai-funding-stage-playbook/SKILL.md`), and investor-archetype targeting (AI-specialist VC vs generalist SaaS VC vs sovereign-AI fund vs DFI vs AI-for-good grantmaker vs strategic acquirer).

## References

- `references/saas-valuation-frameworks-for-business-plans.md` — multiples tables, formulas, comparables
- `references/saas-funding-stage-playbook.md` — stage-by-stage capital sources and plan profile
- `skills/meta-valuation/references/saas-ai-valuation-adjustments.md` — AI premium / discount full framework
- `skills/meta-ai-valuation-adjustments/SKILL.md` — AI valuation overlay skill
- `skills/11-funding-request/saas-ai-funding-stage-playbook/SKILL.md` — AI funding stage playbook
- `skills/meta-ai-bankability-and-investor-readiness/SKILL.md` — AI bankability scorecard
- `skills/meta-valuation/SKILL.md` — deeper DCF / WACC / CAPM logic
- `book-extractions/ai-on-saas-business-plan-audit-2026.md` — AI-on-SaaS audit
- `book-extractions/cotton-run-a-saas-business-extraction.md` — recurring revenue valuation rationale
- `book-extractions/mersch-hacking-saas-extraction.md` — financial profile by SaaS segment
- `book-extractions/walling-saas-playbook-extraction.md` — funding taxonomy

## Africa / Uganda Application Notes

- African SaaS multiples typically 30-50% below US benchmarks at the same stage, reflecting illiquidity premium, FX risk, smaller TAM.
- DFI growth equity (IFC, FMO, BII, Norfund, Proparco, AfDB) is often the right capital for Series A-equivalent African SaaS — they value patient capital and ESG, accept lower-than-VC returns.
- Patient-capital funds (Acumen, Catalyst Fund, Renew Capital, Future Africa, P1, TLcom) sit between seed and growth.
- Local family offices and corporate venture (Safaricom Spark, MTN, Liquid Intelligent Technologies) are an under-utilised source.
- Convertible notes / SAFEs are common in African pre-seed / seed; structure to allow follow-on; African DFIs prefer priced rounds.
