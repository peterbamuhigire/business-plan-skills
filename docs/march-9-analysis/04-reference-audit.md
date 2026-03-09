# Reference File Audit — Per-Skill Coverage Assessment

This table shows the current state of each skill's reference library against an assessment of what is needed for a bankable EA business plan.

---

## Core Plan Section Skills (01–15)

| Skill | Lines | Refs | Coverage Assessment | Priority |
|---|---|---|---|---|
| `01-executive-summary` | 161 | 3 | Good — Jewinski writing, elevator pitch, venture framing | Medium |
| `02-company-overview` | 44 | 0 | **CRITICAL GAP** — no legal structures, no URSB, no compliance | Critical |
| `03-products-services` | 87 | 6 | Good — value chain, pricing, BM innovation, MVP, feasibility | Low |
| `04-market-analysis` | 119 | 6 | Good — Evans, Hair, Kotler. Missing: industry guide integration | Medium |
| `05-target-market` | 154 | 4 | Good — CLV/CAC, personas, customer discovery, Kaza niche | Low |
| `06-competitive-analysis` | 147 | 4 | Good — Evans, Harris, Fahey, strategy maps | Low |
| `07-marketing-sales-strategy` | 423 | 9 | Strongest skill — comprehensive coverage | Low |
| `08-operations-plan` | 105 | 1 | Thin — BPM good but only 1 ref file; no Uganda infrastructure context | High |
| `09-management-team` | 104 | 8 | Good — Collins, Tuckman, Dennis, stakeholder analysis | Medium |
| `10-financial-projections` | 132 | 4 | **GAP** — no DSCR, no tax framework, no templates, no industry integration | Critical |
| `11-funding-request` | 59 | 0 | **CRITICAL GAP** — equity-only, no CAMPARI, no EA lending landscape | Critical |
| `12-risk-analysis` | 110 | 7 | Good — Dumas, Evans, fishbone, 5 Whys. Missing: insurance framework | Medium |
| `13-implementation-timeline` | 127 | 1 | Reasonable — WBS, Gantt, critical path. Only 1 ref file | Medium |
| `14-ai-integration` | 123 | 1 | Reasonable — Lamplugh AI tools, Kotler phygital. Only 1 ref file | Low |
| `15-appendices` | 52 | 0 | **CRITICAL GAP** — list only, no templates, no document guidance | High |

---

## Meta-Skills

| Skill | Lines | Refs | Coverage Assessment | Priority |
|---|---|---|---|---|
| `meta-bankability-scoring` | 120 | 0 | **GAP** — investor-oriented scoring, not mapped to bank criteria | High |
| `meta-financial-stress-test` | 94 | 0 | **GAP** — methodology present but no historical shock data or benchmarks | High |
| `meta-market-validation` | 247 | 4 | Strong — Blank/Dorf, Cooper, Kagan. Best meta-skill | Low |
| `meta-monitoring-evaluation` | 146 | 0 | **GAP** — good methodology but no refs, not linked to funder reporting | Medium |
| `meta-quarterly-gameplan` | 161 | 0 | Reasonable but no references backing the frameworks | Low |

---

## Industry Guides (integration status)

| Guide | Files | Core Skill Integration | Gap |
|---|---|---|---|
| `restaurant/` | 10 refs | Not referenced from §04, §08, §10 | Medium |
| `agriculture/` | 8 refs | Not referenced from §04, §08, §10 | Medium |
| `retail/` | 7 refs | Not referenced from §04, §08, §10 | Medium |
| `food-processing/` | UNDP profiles | Not referenced from §10 | Low |
| `livestock-aquaculture/` | UNDP profiles | Not referenced from §04, §10 | Low |
| `manufacturing-light/` | 10 refs + UNDP | Not referenced from §08, §10 | Medium |
| `side-hustles/` | 6 refs | Not referenced from §10, §11 | Low |
| `chemicals-cosmetics/` | UNDP profiles | Not referenced | Low |
| `construction-building-materials/` | UNDP profiles | Not referenced | Low |
| `hospitality-tourism/` | UNDP profiles | Not referenced | Low |
| `services/` | UNDP profiles | Not referenced | Low |
| `mining-extractives/` | UNDP profiles | Not referenced | Low |
| `education-social/` | UNDP profiles | Not referenced | Low |
| `textiles-fashion/` | UNDP profiles | Not referenced | Low |

---

## Completely Missing Skills / Reference Files

The following are content gaps with no current skill or reference file addressing them:

| Missing Content | Suggested Location | Priority |
|---|---|---|
| Uganda tax computation framework (PAYE/VAT/WHT/CIT) | `10-financial-projections/references/uganda-tax-framework.md` | Critical |
| EA funding landscape (UDB, ACF, SACCOs, DFIs, commercial banks) | `11-funding-request/references/ea-funding-landscape.md` | Critical |
| Credit assessment frameworks (CAMPARI, 5 Cs, DSCR) | `11-funding-request/references/credit-assessment-frameworks.md` | Critical |
| Collateral analysis guide | `11-funding-request/references/collateral-analysis.md` | Critical |
| Uganda legal structures + URSB process | `02-company-overview/references/uganda-legal-structures.md` | Critical |
| Sector compliance matrix | `02-company-overview/references/compliance-checklist.md` | High |
| Financial model templates (P&L, CF, BS row-by-row) | `10-financial-projections/references/financial-model-templates.md` | Critical |
| Document templates (CV, net worth statement, loan schedule) | `15-appendices/references/document-templates.md` | High |
| Plan assembly and submission guide | `15-appendices/references/submission-guide.md` or new `00-plan-assembly/` | High |
| Covering letter templates | `15-appendices/references/document-templates.md` | High |
| ESMP template for DFI applications | `11-funding-request/references/esmp-template.md` | High |
| Grant proposal framework (LogFrame, Theory of Change) | New `11b-grant-proposal/` skill or extension of §11 | Medium |
| Financial stress test benchmarks | `meta-financial-stress-test/references/stress-test-methodology.md` | High |
| Bank loan repayment schedule template | `11-funding-request/references/loan-application-templates.md` | High |
| Loan covenant monitoring framework | `meta-monitoring-evaluation/references/` | Medium |
| Uganda insurance product benchmarks | `12-risk-analysis/references/uganda-insurance.md` | Medium |
| Uganda IP registration guide | `03-products-services/references/ip-registration-uganda.md` | Low |
| Informal business formalisation pathway | `02-company-overview/references/` | Medium |
| Bank statement reconstruction methodology | `10-financial-projections/references/` | Medium |
| Industry guide cross-reference matrix | Each relevant core skill | High |

---

## What the Suite Does Well

To give a balanced view — these are areas where the suite is genuinely strong:

1. **Marketing and sales strategy (§07)** — 423 lines, 9 reference files. Covers guerrilla marketing, Gap Selling, growth marketing, digital marketing, AARRR funnel, social media. Comprehensive enough for a sophisticated marketing plan.

2. **Market validation (meta)** — 247 lines, 4 reference files. Customer development process, MVP testing, product-market fit, earlyvangelist identification. Very strong for startup validation.

3. **Digital marketing strategy** — 473 lines, 12 reference files. Best-resourced skill in the suite. Covers POEM, RACE, platform-specific tactics, AI integration, EA WhatsApp/Facebook context. Excellent.

4. **Risk analysis (§12)** — 110 lines, 7 reference files. Fishbone, 5 Whys, Pareto, scenario planning, Suns & Clouds. Good depth for a non-financial audience.

5. **Target market (§05)** — 154 lines, 4 reference files. CLV/CAC framework, segmentation, customer personas, Problem Recognition Scale. Strong for a growth-oriented business.

6. **Industry guides** — 13 guides with deep content, particularly restaurant (10 refs), agriculture (8 refs), retail (7 refs), manufacturing-light (10 individual files). Excellent reference material — just not wired into the workflow.

7. **Operations plan (§08)** — BPM lifecycle, Devil's Quadrangle, 29 redesign heuristics, Little's Law. Good analytical depth even if Uganda-specific context is thin.

The pattern is clear: the suite excels at **strategy, marketing, and product thinking** — the language of startup pitches and MBA programmes. It is weak on **credit, legal, and compliance** — the language of bank credit committees and regulators. The plan it generates today is more likely to impress an accelerator than a bank branch manager.
