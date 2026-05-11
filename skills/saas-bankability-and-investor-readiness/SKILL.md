---
name: saas-bankability-and-investor-readiness
description: Score a SaaS / ICT plan against SaaS-investor readiness criteria — ARR growth, Rule of 40, LTV:CAC, NRR, GRR, burn multiple, magic number, board-pack quality, data-room standard. SaaS-specific complement to meta-bankability-scoring (which is CAMPARI / DFI / bank-loan oriented). Use before any SaaS fundraise.
---

# SaaS Bankability & Investor Readiness Skill

## Overview

SaaS investors apply a different lens than commercial bank lenders. Where CAMPARI (`meta-bankability-scoring`) checks character / ability / margin / amount / repayment / insurance for a debt facility, SaaS-investor readiness checks unit economics, growth quality, retention, capital efficiency, and operating discipline for an equity / venture / DFI growth-equity round. Both can be relevant; this skill runs the SaaS-investor layer.

## Use When

- A SaaS plan is preparing for any equity round (pre-seed, seed, Series A, growth, DFI growth-equity)
- A DFI is considering an equity / quasi-equity instrument in a SaaS company
- An accelerator (Y Combinator, Techstars, TinySeed, MEST, Founders Factory Africa, Catalyst Fund) is reviewing
- Strategic acquirer is doing diligence

## Required Inputs

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

## Outputs

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
