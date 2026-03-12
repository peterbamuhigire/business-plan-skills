# World-Class Benchmarking
## Does This Suite Produce Plans That Top Consulting Firms Would Be Proud Of?

**Date:** 12 March 2026

---

## What "World-Class" Means in Practice

To answer this honestly, we need to be specific about what McKinsey, BCG, Bain, Deloitte, and PwC actually do when they produce a business plan or investment memorandum. These firms do not use templates — they use methodology. The differentiator is not form, it is analytical rigour applied through named frameworks by experienced practitioners.

The suite is evaluated against six world-class benchmarks.

---

## Benchmark 1: Structured Analytical Thinking

**Standard:** Top consulting firms use MECE (Mutually Exclusive, Collectively Exhaustive) issue trees and the Pyramid Principle (SCQA) to structure every document.

**Suite assessment: STRONG ✅**

- `01-executive-summary/SKILL.md` implements Minto's SCQA framework explicitly. The Pyramid Structure Test and the blank-assertion correction are both present. A plan writer who follows this skill will produce a document with the same logical architecture as a McKinsey memo.
- `meta-market-validation/references/mckinsey-problem-solving.md` implements Rasiel's MECE framework, issue trees, hypothesis-driven analysis, the 80/20 rule, key-driver analysis, and the "Forces at Work" framework directly from *The McKinsey Way*.
- The 30-second test, elevator test, and governing-thought discipline are all present.

**Gap:** MECE and Pyramid Principle are implemented in the executive summary and market validation skills, but are not explicitly cross-referenced in every other skill. A consultant using `04-market-analysis/SKILL.md` alone would not be prompted to apply MECE structure to the market analysis unless they already knew to do so.

**Recommendation:** Add a MECE/Pyramid reminder note in `04-market-analysis`, `06-competitive-analysis`, and `09-management-team` SKILL.md files — single-line cross-reference to `references/pyramid-principle.md`.

---

## Benchmark 2: Financial Rigour

**Standard:** Top-tier financial projections are driver-based (not assumption-free), cash-flow separated from profit, sensitivity-tested, and presented with explicit assumptions documentation.

**Suite assessment: STRONG ✅**

- `10-financial-projections/SKILL.md` implements driver-based modelling, forecast-vs-target-vs-plan distinction (Morlidge), flexible budgets, variance analysis, the One-Minute Business Model (Kagan), and the Six Revenue Dials.
- `meta-financial-stress-test/SKILL.md` implements 4-scenario modelling calibrated to Uganda historical shocks — something even some professional consulting firms do not include for African SME plans.
- `10-financial-projections/references/financial-model-templates.md` provides row-by-row templates for income statement, cash flow, and balance sheet with Uganda-specific rows (NSSF, VAT, PAYE, ITA Sixth Schedule depreciation).
- DSCR ≥ 1.25× is enforced as a hard gate in both the financial projections skill and the bankability scoring meta-skill.
- Damodaran's DCF/WACC/CAPM framework is implemented in `11-funding-request/references/business-valuation-methods.md` with a worked UGX example and Uganda country risk premium (4–6%).

**Gap:** No explicit Monte Carlo simulation methodology. The stress test skill uses 4-scenario analysis which is a proxy, but a top consulting firm advising a PE investor would expect Monte Carlo for a UGX 1B+ deal. This is a Phase 3 gap — not needed for the primary Uganda SME target market.

**Gap:** No explicit guidance on working capital management (debtor days, creditor days, inventory turns). These ratios appear in `references/financial-model-templates.md` but are not prominently structured as a required analysis in the financial projections skill.

---

## Benchmark 3: Market Intelligence

**Standard:** Consulting-grade market analysis uses primary research + secondary data, TAM/SAM/SOM with bottoms-up sizing, and structured competitive intelligence.

**Suite assessment: ADEQUATE — approaching strong ✅⚠️**

- TAM/SAM/SOM with bottoms-up methodology is present in `04-market-analysis/SKILL.md`.
- Uganda macro data is excellent: UBOS GDP, inflation, population, labour market, exchange rates, IFC private sector data, World Bank human capital data — all current and well-structured.
- EAC trade data (2024) and AfCFTA framework are present, enabling regional market sizing.
- 13 industry guides provide sector-specific benchmarks that substitute for primary research when the user cannot commission market studies.

**Gaps:**
- **No Porter's Five Forces** — the most universally recognised industry analysis framework. The `06-competitive-analysis/SKILL.md` uses Teece (business model vs. strategy) and Kaza (Underdog Principles) but does not explicitly name or structure Porter's Five Forces. Any consulting firm, bank, or DFI reviewer who sees a competitive analysis without Porter will note the omission.
- **No PESTLE** — Political, Economic, Social, Technological, Legal, Environmental analysis. While these dimensions are covered across the suite, they are not presented as a named PESTLE framework that a reader can immediately recognise.
- **No primary research protocol** — the suite assumes the user will bring market data. There is no structured customer survey template, focus group guide, or interview framework to generate primary data where secondary sources are absent. `meta-market-validation/SKILL.md` covers customer discovery but does not provide a formal market research methodology.

---

## Benchmark 4: Competitive Intelligence

**Standard:** World-class competitive analysis includes structured competitor profiles, competitor financial analysis (where data is available), and a defensible moat analysis.

**Suite assessment: ADEQUATE ✅⚠️**

- `06-competitive-analysis/SKILL.md` covers SWOT, competitive matrix, Teece's business model framework, Kaza's differentiation types, and guerrilla positioning.
- `meta-due-diligence/references/osint-business-intelligence.md` (Hetherington) provides a 5-layer OSINT framework for competitor intelligence including Uganda/EA workarounds for thin data environments.

**Gaps:**
- No structured Porter's Five Forces template (see above).
- No explicit competitor financial benchmarking guidance — how to use public filings, URSB company searches, URA compliance data, or industry association reports to estimate competitor revenues and margins. Consulting firms do this routinely; it is a significant credibility signal.
- No explicit "competitive moat scoring" rubric (network effects, switching costs, cost advantages, intangible assets, efficient scale — Morningstar's five moat types). The concept of moat is present but not structured as a scoring exercise.

---

## Benchmark 5: Execution Credibility

**Standard:** A world-class plan does not just describe the business — it demonstrates that the management team can actually execute the plan.

**Suite assessment: STRONG ✅**

- `09-management-team/SKILL.md` implements Kaza's Founder Purpose Statement (objective function beyond profit), leadership analysis, skills gap assessment, and Ugandan labour market data.
- `13-implementation-timeline/SKILL.md` uses WBS, Gantt structure, critical path, and 90-day game plans (Jan B. King). The Pre-Phase 0 regulatory compliance gate (NIN/BRN → TIN → URSB → trading licence) is present.
- `meta-quarterly-gameplan/SKILL.md` converts the plan into 90-day operational sprints — a significant differentiator that most template-based plans lack entirely.
- `meta-monitoring-evaluation/SKILL.md` includes funder reporting covenants, bank loan covenant compliance, and DFI reporting requirements — signalling to lenders that the management team understands post-funding accountability.

**Minor gap:** No explicit advisory board recruitment strategy or template for "how to attract a credible advisory board when the founding team is young/unproven" — common in EA startup plans.

---

## Benchmark 6: Investor Communication

**Standard:** Top consulting firms produce pitch materials that are visually clean, narratively compelling, and tailored to the specific audience's decision criteria.

**Suite assessment: VERY STRONG ✅✅**

This is one of the suite's standout achievements. The combination of:
- `meta-pitch-preparation/SKILL.md` (Klaff's STRONG method + neurofinance + frame control)
- `meta-presentation-design/SKILL.md` (Duarte's Sparkline + Gallo's three-act + Edwards's delivery + HBR executive standards)
- Five reference files totalling ~3,600 lines from five specialist books

...gives a pitch preparation system that is more rigorous than anything offered by most EA business consulting firms. The 13-slide master template, assertion-evidence slide standard, audience resistance mapping, and 6-session coaching programme are collectively best-in-class.

**The only gap:** These two skills are not integrated into a single "pitch deck" workflow. A user must know to run them both, in sequence, with the right context. This is a discoverability and usability gap, not a content gap.

---

## World-Class Scorecard Summary

| Benchmark | Score | Status |
|-----------|-------|--------|
| Structured analytical thinking (MECE/Pyramid) | 8/10 | Strong |
| Financial rigour (driver-based, stress-tested) | 8.5/10 | Strong |
| Market intelligence (TAM, industry, competitive) | 7/10 | Adequate |
| Competitive intelligence | 6.5/10 | Adequate |
| Execution credibility (team, timeline, M&E) | 8.5/10 | Strong |
| Investor communication (pitch, deck, delivery) | 9/10 | Very Strong |
| **Overall world-class score** | **7.9/10** | **Strong** |

---

## The Honest Gap: What Makes McKinsey Plans Different

The suite covers methodology. What consulting firms add beyond methodology is:

1. **Primary research** — surveys, interviews, focus groups, mystery shopping. The suite can structure how to present primary research, but cannot generate it.

2. **Industry relationships and data access** — Bloomberg, Euromonitor, S&P Capital IQ, proprietary databases. The suite works with publicly available data. East Africa is relatively data-poor, but referencing named data sources (UBOS, IFC, UNDP — all present) is the correct workaround.

3. **Senior practitioner judgement** — knowing when a market is actually too small, when a management team is actually not capable, when a financial model is not credible regardless of how well it is formatted. The suite provides a framework for this judgement but cannot substitute for it.

4. **Validated comparables** — consulting firms benchmark clients against companies they have advised in the same sector. The industry guides partially substitute for this, but real comparables require real deal experience.

**Conclusion:** The suite is not a replacement for a skilled consultant. It is the best available tool to accelerate and structure that consultant's work — or to produce credible output in the many situations where a skilled consultant is not available or not affordable.

For East Africa specifically, where the alternative is often a 40-page plan written in Arial 11pt with no market data and fabricated financial projections, this suite produces output that is categorically better and credibly world-class.
