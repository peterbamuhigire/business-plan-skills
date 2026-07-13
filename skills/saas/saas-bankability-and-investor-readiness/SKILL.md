---
name: saas-bankability-and-investor-readiness
description: Use when a SaaS plan is preparing for any equity round (pre-seed, seed, Series A, growth, DFI growth-equity). Use the corresponding meta skill for a non-SaaS case.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# SaaS Bankability & Investor Readiness Skill

## Overview

SaaS investors apply a different lens than commercial bank lenders. Where CAMPARI (`meta-bankability-scoring`) checks character / ability / margin / amount / repayment / insurance for a debt facility, SaaS-investor readiness checks unit economics, growth quality, retention, capital efficiency, and operating discipline for an equity / venture / DFI growth-equity round. Both can be relevant; this skill runs the SaaS-investor layer.

## Use When

- A SaaS plan is preparing for any equity round (pre-seed, seed, Series A, growth, DFI growth-equity)
- A DFI is considering an equity / quasi-equity instrument in a SaaS company
- An accelerator (Y Combinator, Techstars, TinySeed, MEST, Founders Factory Africa, Catalyst Fund) is reviewing
- Strategic acquirer is doing diligence

## Do Not Use When

- The request belongs to the neighbouring route. Use the cross-sector meta skill when the decision is not specific to recurring-revenue SaaS economics or operations.
- The available evidence cannot support a responsible bankability and investor readiness conclusion; return the evidence gap instead of inventing one.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Bankability And Investor Readiness brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
| Current accounting, tax, valuation, or pricing basis | Finance owner, accounting records, signed contracts, and current authoritative sources | Conditional | Mark the treatment unresolved and require qualified professional review. |
- Section 10 financial projections (with the SaaS unit-economics dashboard)
- Cohort retention model
- Sales capacity model
- Pricing architecture
- Customer-success operating model
- Founder bios + team
- Cap table
- Data-room status

## Workflow

1. **Score the SaaS Quality Scorecard** (see `references/saas-bankability-checklist.md`):
   - ARR growth rate (T3M annualised vs T12M)
   - Net Revenue Retention (>110% target)
   - Gross Revenue Retention (>85% target)
   - LTV:CAC (≥3:1)
   - CAC Payback (<18 months SMB / <24 months mid / <30 months enterprise)
   - Gross Margin (≥70%; ≥80% for software-only)
   - Rule of 40 (≥30 early-stage; ≥40 mid-stage)
   - Burn Multiple (<2.0)
   - Magic Number (>0.75)
   - Quick Ratio (>2)

2. **Score the Operating Quality Checklist:**
   - Customer-conversation cadence in place
   - Cohort retention model maintained monthly
   - Sales capacity model maintained quarterly
   - Pricing experiments documented
   - QBR cadence for high/mid-touch customers
   - Decision log maintained
   - MSPOT (or equivalent) annual artefact
   - Board pack quality

3. **Score the Risk Posture:**
   - Customer concentration (no single customer >15% of ARR)
   - Channel concentration (no single channel >50%)
   - Key-person risk (named succession; bus-factor disclosed)
   - Compliance status (SOC2, ISO27001, data-residency)
   - FX exposure (for African plans)
   - Platform / API dependency risk

4. **Score the Data-Room Standard:**
   - Cap table
   - Financial statements (audited or accountant-prepared)
   - Customer contracts (top 20)
   - Cohort export from billing system
   - Pipeline export
   - Org chart + key bios
   - IP register
   - Material agreements
   - Tax compliance

5. **Aggregate into overall readiness score** (0-100 with named bands):
   - 80-100: Investor-ready; outreach now
   - 65-79: Near-ready; specific gaps to close
   - 50-64: 6-12 months from readiness; install operating discipline
   - <50: Not investor-ready; focus on fundamentals

6. **Produce the gap-closure plan** — specific actions, owners, timelines.

7. **Cross-reference with `meta-bankability-scoring`** if debt is also in scope.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the SaaS investor-readiness scorecard and that the decision concerns which SaaS metrics block or support fundraising.
- **Stop condition:** halt the affected conclusion if required evidence is missing (ARR quality, retention, unit economics, burn, governance, and data room) or if the work could lead to this identified risk: rewarding growth that destroys retention or cash efficiency.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Every score item is computed from actual data or marked as missing
- Benchmarks cited and adjusted for stage / segment / geography
- Gap-closure plan is specific (not "improve retention")
- The plan is honest about deficiencies — investors will discover them anyway

## Anti-Patterns

- "We'll improve our metrics later" — investors invest in trajectory + discipline, not promises
- Self-scoring high on items without evidence
- Hiding customer concentration
- Reporting in the most favourable cut without showing full data
- Treating a generic bankability and investor readiness template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to saas bankability and investor readiness. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Bankability And Investor Readiness deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- SaaS Quality Scorecard (with each metric, target, actual, gap)
- Operating Quality checklist
- Risk Posture assessment
- Data-Room readiness checklist
- Overall readiness score (0-100) with band
- Gap-closure plan
- Recommended investor / DFI tier matching the readiness score

## AI Scorecard Module (mandatory for AI-feature-led plans)

When AI is material to the plan, the SaaS bankability score is necessary but not sufficient. Add the AI bankability scorecard from `skills/meta-ai-bankability-and-investor-readiness/SKILL.md` and `skills/meta-bankability-scoring/references/saas-ai-bankability-checklist.md`:

- **AI Economics** (max 15) — AI-cost-as-%-of-ARR, AI GM trajectory, AI Contribution Margin per tier, per-tenant cost, AI-revenue attribution
- **AI Discipline** (max 12) — eval coverage, hallucination rate, production sampling, model-deprecation watch
- **AI Governance** (max 12) — AI policy, AI committee, AI-incident protocol, training-data provenance
- **AI Moat** (max 7) — pulled from `saas-ai-moats-and-defensibility-checklist.md`
- **AI Risk** (max 9) — vendor concentration, regulatory posture, hallucination-liability reserve

Total ~50; investor-archetype weighting applied (AI-specialist VC, generalist SaaS VC, sovereign-AI fund, DFI, AI-for-good grantmaker, strategic acquirer all weight differently). The AI scorecard composes with — does not replace — the SaaS scorecard. Both are required for AI-feature-led plans.

## References

- `references/saas-bankability-checklist.md` — full SaaS scorecard
- `skills/meta-bankability-scoring/references/saas-ai-bankability-checklist.md` — AI scorecard
- `skills/meta-ai-bankability-and-investor-readiness/SKILL.md` — AI bankability skill
- `book-extractions/mersch-hacking-saas-extraction.md` — CFO-grade metrics
- `book-extractions/cotton-run-a-saas-business-extraction.md` — Rule of 40, LTV:CAC, churn
- `book-extractions/ai-on-saas-business-plan-audit-2026.md` — AI-on-SaaS audit
- `skills/meta-bankability-scoring/SKILL.md` — sister skill for debt / bank-loan readiness
- `skills/saas-valuation-and-fundraising-strategy/SKILL.md` — valuation logic

## Africa / Uganda Application Notes

- African DFIs (FMO, Norfund, BII, Proparco, AfDB, IFC) and patient-capital funds (Acumen, Renew Capital, Catalyst Fund) apply hybrid lenses — both CAMPARI and SaaS-investor. Score both.
- ESG / impact requirements — DFIs increasingly require sustainability scoring (use `meta-sustainability` skill).
- Data-room expectations differ — Africa-focused funds (TLcom, Partech, Norrsken22, Future Africa) ask for more granular cohort data because category benchmarks are scarce.
- Customer concentration is often higher in African SaaS (smaller TAM); be honest, disclose, and show diversification plan.
- FX exposure must be quantified — investors will model the downside scenario.
- Audit standards: prefer IFRS-compliant audit by Big 4 / mid-tier (PwC, Deloitte, KPMG, EY, BDO, Grant Thornton, RSM). DFIs require this above $1M raise.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| SaaS investor-readiness scorecard decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to rewarding growth that destroys retention or cash efficiency. |

## Capability and Permission Boundaries


Default to read-only inspection while producing the SaaS investor-readiness scorecard. Read supplied records and run non-mutating checks; entering cited scores in the supplied fundraise pack is permitted only when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If ARR quality, retention, unit economics, burn, governance, and data room cannot be obtained, return a qualified SaaS investor-readiness scorecard covering only the checks that remain supportable. Leave this decision unresolved: which SaaS metrics block or support fundraising. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which SaaS metrics block or support fundraising | Record the conclusion, source trail, owner, and review trigger in the SaaS investor-readiness scorecard. | Risk of rewarding growth that destroys retention or cash efficiency |
| Material evidence conflicts or remains uncertain | Recalculate readiness after removing disputed ARR, retention, or efficiency adjustments and retain the conservative score for the fundraise gate. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: ARR quality, retention, unit economics, burn, governance, and data room | Mark the decision on which SaaS metrics block or support fundraising `not assessed` in the SaaS investor-readiness scorecard, and send it to the finance owner and investor-readiness reviewer. | Otherwise, the work risks rewarding growth that destroys retention or cash efficiency |

## Quality Standards


Accept the SaaS investor-readiness scorecard only when evidence is sufficient for this decision: which SaaS metrics block or support fundraising. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of rewarding growth that destroys retention or cash efficiency.

## Worked Example


ARR grows quickly, but one customer supplies most revenue and NRR is unreconciled. Score concentration and retention as blockers until the data room supports durable revenue quality.

## Finance Doctrine Gate


Apply the Chwezi doctrine to the SaaS investor-readiness scorecard, using the reporting basis and effective date supported by ARR quality, retention, unit economics, burn, governance, and data room. Reconcile the treatment to the model and narrative, and have the finance owner and lender or investment reviewer review the treatment, reconciliation, and exposure to this risk: rewarding growth that destroys retention or cash efficiency.

<!-- dual-compat-end -->
