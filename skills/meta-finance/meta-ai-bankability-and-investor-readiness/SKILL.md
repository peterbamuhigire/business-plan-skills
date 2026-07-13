---
name: meta-ai-bankability-and-investor-readiness
description: Use when aI-feature-led SaaS plan is preparing for fundraise, DFI submission, or AI-for-good grant. Use financial projections for model construction.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Meta — AI Bankability & Investor Readiness Skill

## Overview

SaaS bankability scrutiny (Rule of 40, LTV:CAC, NRR, burn multiple) is necessary but no longer sufficient for AI-feature-led plans. AI-specialist funds (a16z AI, Index AI, Bessemer AI, Cohere founders fund) and AI-aware DFIs (IFC AI envelopes, AfDB AI-for-development) apply an additional bankability lens: are you running AI like a CFO, or like a feature team?

This skill installs the AI bankability scorecard that sits on top of the SaaS bankability scorecard and the CAMPARI lending lens. It is the discipline behind the AI-specific investor diligence partner's first session.

## Use When

- AI-feature-led SaaS plan is preparing for fundraise, DFI submission, or AI-for-good grant
- AI is material to revenue or product thesis
- Existing bankability score is "good SaaS" but the AI dimensions are unmeasured
- Plan is pricing in an AI valuation premium (`meta-ai-valuation-adjustments`) and must justify it
- Investor diligence has flagged AI economics or governance gaps

## Do Not Use When

- AI is internal-efficiency only — use `meta-bankability-scoring` standard SaaS layer
- Plan is bank-loan only (CAMPARI is the binding lens; AI bankability is supplementary)

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Bankability And Investor Readiness brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
| Current accounting, tax, valuation, or pricing basis | Finance owner, accounting records, signed contracts, and current authoritative sources | Conditional | Mark the treatment unresolved and require qualified professional review. |
- Output of `saas-ai-unit-economics-and-cogs` (AI margin trajectory)
- Output of `saas-ai-cost-of-tenant-calculator` (per-tenant cost)
- Output of `saas-ai-risk-and-stress-test` (risk register + stress scenarios)
- Output of `saas-ai-moat-and-defensibility` (moat score)
- Eval-pipeline maturity evidence
- AI-governance documentation (committee, policy, decision log on AI changes)
- AI data-room contents (model cards, training-data provenance, EULA exposures, incident log)

## Workflow

1. **Score the AI economics dimensions** — produce values + ratings:
   - **AI-cost-as-%-of-ARR** — <5% excellent / 5-10% typical / 10-15% strained / >15% alarm
   - **AI Gross Margin trajectory** — improving QoQ / stable / declining
   - **AI Contribution Margin per tier** — positive across all tiers / mixed / negative tiers exist
   - **AI-revenue % of total ARR** — declared AI-attributable share
   - **Per-tenant AI cost (median + top decile)** — gap between median and top decile shows tail-risk
2. **Score the AI discipline dimensions**:
   - **Eval coverage** — % of production AI behaviour covered by automated evals
   - **Hallucination-rate trajectory** — measured? declining?
   - **Production sampling rate** — % of production calls sampled for human review
   - **Model-deprecation-watch** — process in place; documented; last review date
   - **Cost-engineering rituals** — cache-hit, model-mix, prompt-token discipline
3. **Score the AI governance dimensions**:
   - **AI policy** — written and current
   - **AI committee / RACI** — who decides on model changes, data uses, risk acceptances
   - **Incident log + runbook** — existence and quality
   - **Training-data provenance audit** — done, in progress, or absent
   - **EULA / data-rights exposure** — documented exposures to provider EULAs
4. **Score the AI moat dimensions** — pull from `saas-ai-moat-and-defensibility` 0-21 score
5. **Score the AI risk dimensions** — pull from `saas-ai-risk-and-stress-test`:
   - Vendor concentration
   - Regulatory exposure by jurisdiction
   - FX exposure on USD AI cost
   - Hallucination-liability reserve adequacy
6. **Compile the AI bankability scorecard** per `references/saas-ai-bankability-checklist.md` — five sections (economics, discipline, governance, moat, risk) × multiple line items, each 0-3, total out of ~50.
7. **Apply the bankability threshold** — <20 weak / 20-30 typical / 30-40 strong / 40+ exceptional.
8. **Identify the binding constraints** — which dimensions are dragging the score and which would most improve fundability.
9. **Map to investor archetype** — AI-specialist VC, generalist SaaS VC, sovereign-AI fund, AI-for-good DFI / grantmaker each weight differently.
10. **Wire to living plan** — scorecard refresh quarterly; binding-constraint review monthly; investor-update AI block monthly.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the AI bankability scorecard and that the decision concerns whether AI-specific evidence clears funder diligence.
- **Stop condition:** halt the affected conclusion if required evidence is missing (AI cost, evaluation, incident, and governance records) or if the work could lead to this identified risk: rating an unevaluated AI feature as investable differentiation.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- All five dimensions scored with explicit numbers, not narrative
- AI-cost-as-%-of-ARR stated as headline diagnostic
- Eval coverage stated as a number
- Vendor concentration stated as a percentage
- Investor archetype declared; scorecard mapped to that lens
- Binding constraints named; remediation plan stated
- Scorecard arithmetic transparent; no aggregate-only summary
- Reconciliation with SaaS-bankability score (the two must compose, not contradict)

## Anti-Patterns

- "AI is going well" with no measured eval / cost / margin data
- Eval coverage missing; production sampling absent
- AI governance "policy is in draft" with no committee operating
- Vendor concentration ignored
- Scorecard gamed (eval coverage 95% on a 5-test eval suite)
- Investor archetype undeclared; same pitch for all funders


- Applying the wrong neighbouring route to meta ai bankability and investor readiness. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Bankability And Investor Readiness deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- AI bankability scorecard (table of dimensions × items × score)
- Binding-constraint list
- Investor-archetype map (which funders fit; which don't)
- Remediation backlog (what to improve before round)
- AI section for the investor data room
- Cross-reference to SaaS-bankability scorecard

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| AI bankability scorecard | quarterly | CFO + CEO | -5 points from prior |
| AI-cost-as-%-of-ARR | monthly | CFO | >planned by 2pp |
| Eval coverage | monthly | Head of AI / QA | -5pp |
| Hallucination rate | monthly | Head of AI | +1pp |
| Governance committee meeting | monthly | AI committee chair | missed meeting |
| Investor archetype map | semi-annual | CEO | new fund category emerges |

## References

- `references/saas-ai-bankability-checklist.md` — full scorecard
- `references/saas-ai-data-room-contents.md` — what goes in AI data room (cross-listed in `meta-due-diligence`)
- `skills/saas-bankability-and-investor-readiness/SKILL.md` — sister skill (SaaS layer)
- `skills/meta-bankability-scoring/SKILL.md` — CAMPARI + SaaS layer
- `skills/meta-ai-valuation-adjustments/SKILL.md` — what the scorecard supports / undermines
- `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md`
- `skills/06-competitive-analysis/saas-ai-moat-and-defensibility/SKILL.md`
- `skills/12-risk-analysis/saas-ai-risk-and-stress-test/SKILL.md`

## Africa / Uganda Application Notes

- **DFI lens** (IFC AI, AfDB, Norfund, Proparco, BII) weights ethics, sustainability, data sovereignty, local-language coverage, and impact KPIs alongside commercial AI bankability. Plans should produce a separate DFI-lens scorecard.
- **AI-for-good grantmaker lens** (Mozilla Mradi, GSMA AI for Impact, IDRC AI4D, Lacuna Fund) weights theory-of-change, training-data provenance, community benefit, and explainability higher than commercial economics.
- **Local AI ecosystem credit** — partnerships with Lelapa AI, Masakhane, AIMS, Carnegie Mellon Africa, Deep Learning Indaba alumni are evidence of credible AI talent strategy in Africa.
- **Sovereign-AI tender readiness** — public-sector procurement scoring in KE, NG, ZA, RW, EG, UG increasingly weights in-country data residency, local capacity-building, and local-language coverage. Tender-readiness is a bankability dimension for plans selling to African public sector.
- **FX hedge / corridor evidence** — DFI bankability for AI plans includes FX management posture given USD AI cost vs local-currency revenue.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| AI bankability scorecard decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to rating an unevaluated AI feature as investable differentiation. |

## Capability and Permission Boundaries


Default to read-only inspection while producing the AI bankability scorecard. Read supplied records and run non-mutating checks; recording AI findings in the plan's scorecard is permitted only when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If AI cost, evaluation, incident, and governance records cannot be obtained, return a qualified AI bankability scorecard covering only the checks that remain supportable. Leave this decision unresolved: whether AI-specific evidence clears funder diligence. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: whether AI-specific evidence clears funder diligence | Record the conclusion, source trail, owner, and review trigger in the AI bankability scorecard. | Risk of rating an unevaluated AI feature as investable differentiation |
| Material evidence conflicts or remains uncertain | Rescore AI readiness after removing any unevaluated capability, unallocated model cost, or undocumented governance claim. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: AI cost, evaluation, incident, and governance records | Mark the decision on whether AI-specific evidence clears funder diligence `not assessed` in the AI bankability scorecard, and send it to the finance owner and funder reviewer. | Otherwise, the work risks rating an unevaluated AI feature as investable differentiation |

## Quality Standards


Accept the AI bankability scorecard only when evidence is sufficient for this decision: whether AI-specific evidence clears funder diligence. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of rating an unevaluated AI feature as investable differentiation.

## Worked Example


An AI SaaS plan reports rapid ARR growth but omits inference cost and evaluation coverage. Remove the unsupported margin and quality claims from the readiness score until cost attribution and evaluation records are supplied.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the AI bankability scorecard, using the reporting basis and effective date supported by AI cost, evaluation, incident, and governance records. Reconcile the treatment to the model and narrative, and have the finance owner and lender or investment reviewer review the treatment, reconciliation, and exposure to this risk: rating an unevaluated AI feature as investable differentiation.

<!-- dual-compat-end -->
