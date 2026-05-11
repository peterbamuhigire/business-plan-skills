---
source: Mersch, Cotton, OpenView SaaS Benchmarks, KeyBanc SaaS Survey, Bessemer Cloud Index
frameworks: [SaaS investor readiness; SaaS-DFI scorecard; Equity-investor checklist]
skill: meta-bankability-scoring (enhancement)
cross-reference: [saas-bankability-and-investor-readiness, saas-unit-economics-and-cohort-model, meta-valuation]
---

# SaaS Bankability Scorecard — Enhancement to meta-bankability-scoring

The engine's `meta-bankability-scoring` skill applies the **CAMPARI** framework for commercial bank lending. SaaS investors apply a different lens. This reference adds the SaaS-investor-readiness scoring module so the engine can score plans against both lenses simultaneously.

## 1. When to apply which scorecard

| Audience | Use CAMPARI? | Use SaaS Scorecard? |
|---|---|---|
| Commercial bank (working capital loan, asset finance) | ✓ Primary | Optional |
| Uganda Development Bank (UDB) / sector DFI loan | ✓ Primary | Useful supplement |
| DFI equity / quasi-equity (IFC, FMO, BII, Norfund, Proparco, AfDB) | ✓ Useful | ✓ Primary |
| Venture capital (any stage) | Rarely useful | ✓ Primary |
| Strategic acquirer | Limited | ✓ Primary |
| Patient capital (Acumen, Catalyst Fund, Renew Capital) | ✓ Useful | ✓ Primary |
| Accelerator (TinySeed, YC, Techstars, MEST) | Rarely | ✓ Primary |
| Revenue-based finance | Hybrid — adapted SaaS metrics | ✓ Primary |

## 2. The SaaS Bankability Score (100 points total)

See `skills/saas-bankability-and-investor-readiness/references/saas-bankability-checklist.md` for the full 100-point scorecard. Summary:

- SaaS Quality (unit economics) — 40 points
- Operating Quality (discipline, cadence) — 25 points
- Risk Posture — 20 points
- Data-Room Readiness — 15 points

## 3. Cross-Walking CAMPARI to SaaS

How CAMPARI maps to SaaS investor concerns:

| CAMPARI | SaaS investor equivalent | Why |
|---|---|---|
| **C**haracter | Founder reputation; references; track record | Both lenses care |
| **A**bility | Team execution; ramp pace; hiring quality | Both lenses care |
| **M**argin | Gross margin (recurring); LTV:CAC; CAC payback | SaaS frames as unit economics |
| **P**urpose | Use of funds clarity; milestones unlocked | Both lenses care |
| **A**mount | Round size vs milestones; runway extended | Both lenses care |
| **R**epayment | For debt: cash-flow coverage; DSCR; for equity: exit thesis | Different framing |
| **I**nsurance / Security | Cyber insurance; E&O; D&O; cap-table cleanliness | Both lenses care |

## 4. The DFI-Specific Layer (when relevant)

DFIs apply both lenses plus an additional layer:

### ESG / E&S Performance
- IFC Performance Standards alignment
- Environmental & Social Management System (ESMS)
- Labour rights / health & safety
- Stakeholder engagement
- Environmental footprint

### Impact Metrics
- Jobs created (direct + indirect)
- Smallholder / MSME beneficiaries reached
- Women / youth as % of beneficiaries / employees / leadership
- Climate resilience contribution
- Financial inclusion deepening

Use `meta-sustainability` skill for the full framework. The bankability scorecard should include ESG / impact tab for DFI-targeted plans.

## 5. The Equity-Investor-Specific Layer (when relevant)

### Exit thesis
- Strategic-buyer universe (see `meta-strategic-optionality`)
- IPO realistic? (rare in Africa)
- PE rollup possibilities
- Exit multiple expectations

### Cap-table cleanliness
- Founder equity post-money projected
- ESOP allocation and refresh discipline
- Liquidation preferences (≤1.25× non-participating ideally)
- Anti-dilution (weighted average broad-based ideally)
- Board composition

### Governance
- Independent director appointed
- Board meeting cadence and minutes
- Financial controls / audit
- Stakeholder agreements

## 6. The Living-Plan Discipline

Bankability scoring should be refreshed:
- **Quarterly**: full scorecard refresh
- **At each fundraise**: tailored scorecard for target investor type
- **When a metric trips**: trigger-replan if any single-metric falls into "concerning" band
- **Annually**: comparison across years to demonstrate trajectory

Investors invest in trajectory + discipline; show both.

## 7. Africa / Uganda Application Notes

- African SaaS scoring should be tier-adjusted (Years 1-3 allow lower Rule of 40, longer CAC payback).
- DFIs prefer **IFRS-audited** financials; budget for audit even at pre-revenue if DFI is in target investor list.
- **Cap-table structuring** through Mauritius / Cayman holding is common for cross-border investor compatibility but adds tax structuring complexity — get specialist counsel.
- **Currency presentation**: scorecard in local currency + USD parallel view.
- **Customer concentration** above 15-20% is common in African SaaS; disclose and show diversification plan rather than hiding.
- **Audit standard**: prefer Big-4 / mid-tier audit (PwC, Deloitte, KPMG, EY, BDO, Grant Thornton, RSM) above $1M raise; below that, registered local audit.
- **DFI applications**: each DFI has specific MIS format requirements; ask early to design your reporting to match.
- **Compliance roadmap**: SOC2 / ISO27001 may be required for fintech / healthtech DFI engagement — build it into the milestone-funded use of funds.
