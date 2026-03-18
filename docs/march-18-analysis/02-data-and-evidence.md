# Pillar 2 — Data Quality and Evidence Standards
**Score: 6.5 / 10**

This is the most significant strategic gap. The suite is exceptionally strong on secondary sources — UBOS, World Bank, IFC, UNDP, EAC, Africa Trade Outlook. But McKinsey/Bain always supplement secondary data with **primary research**. The total absence of a primary research design protocol is the gap that most reduces the suite's credibility with sophisticated funders (development finance institutions, private equity, institutional investors).

---

## 2.1 Secondary Source Quality Assessment

### Tier 1 — Highly Credible (Citation-Ready)

| Source Type | Examples in Suite | Assessment |
|------------|-------------------|------------|
| **World Bank / IFC data** | Uganda Human Capital 2025 (154pp), IFC CPSD 2022, Women Entrepreneurship Uganda | Institutional credibility; acceptable to all funders |
| **UBOS macro data** | Uganda Macro Context 2025, NPHC 2024 population data | Official government statistics; Uganda standard |
| **EAC Secretariat data** | EAC Trade Data 2024, Common Market Framework | Regional authority; acceptable for cross-border claims |
| **Africa Development data** | Africa Trade & Economic Outlook 2025, KNBS Kenya Facts 2025 | Development bank quality |
| **Academic/peer-reviewed** | Damodaran (NYU Stern), Porter (HBS), Kotler (Kellogg), COSO (AICPA), CAGR methodology | Academic standard; citation-grade |
| **Practitioner books (sourced)** | Minto (McKinsey alumnus), Feld & Mendelson (VC practitioners), Howson (M&A practitioner) | Acceptable for methodology citation |
| **UNDP Business Profiles** | 200+ profiles, 16 industries | Investment cost benchmarks reliable; margins are estimates |

### Tier 2 — Acceptable with Caveats

| Source Type | Examples in Suite | Caveat |
|------------|-------------------|--------|
| **Industry guides without cited source** | Some food processing benchmarks | Must disclose as estimates when used in plan |
| **Exchange rate / planning rate** | UGX 3,700/$1 conservative planning rate | Rationale documented; acceptable if disclosed |
| **Salary benchmarks** | UGX 200K–10M+ wage bands | From Uganda Labour Market 2025 (WB); cite source |
| **UNDP investment benchmarks** | Startup cost ranges by business type | UNDP 2013/2018 vintage — flag for currency when older |

### Tier 3 — Needs Primary Verification

| Claim Type | Issue | Recommendation |
|-----------|-------|----------------|
| **Market size figures for specific business** | Secondary data gives broad TAM; SOM always requires local primary research | Add primary research checkpoint |
| **Competitive pricing** | No mystery shopping protocol | Add competitive price survey methodology |
| **Customer willingness-to-pay** | Currently estimated from analogues | Add Van Westendorp Price Sensitivity Meter protocol |
| **Local supplier costs** | UNDP gives ranges; actual quotes required | Add supplier quotation process to plan assembly |
| **Customer segment proportions** | Demographic data from UBOS; customer data from business itself | Add customer discovery interview protocol |

---

## 2.2 Primary Research: The Critical Gap

### What McKinsey/Bain Do That This System Does Not

Every McKinsey/Bain engagement supplements secondary data with at least **two primary research methods**:

1. **Expert interviews** — 10–20 structured interviews with industry experts, potential customers, suppliers, regulators
2. **Quantitative survey** — Sample size 100–400 respondents for market sizing, preference, and price testing
3. **Mystery shopping / price auditing** — Competitive intelligence gathered firsthand
4. **Customer intercepts / observation** — For retail, food service, consumer goods
5. **Financial ratio benchmarking** — Requesting actual P&Ls from comparable businesses via industry associations

### What the Suite Currently Has

`meta-market-validation` contains:
- Blank & Dorf customer development framework
- Alam empathy-based interview methodology
- Customer archetype development
- Problem recognition scale

This is a **strong foundation** but is missing:
- Structured discussion guide template (what questions to ask)
- Sample size calculator (how many interviews are enough?)
- Survey design methodology (Likert scale, MaxDiff, Van Westendorp)
- Mystery shopping protocol
- Triangulation protocol (how to reconcile conflicting data sources)
- Primary-vs-secondary data hierarchy (when does primary override secondary?)

---

## 2.3 Specific Data Gaps by Plan Section

### Section 04 — Market Analysis

| Data Point | Current Source | McKinsey Standard | Gap |
|-----------|---------------|-------------------|-----|
| TAM size | World Bank / UBOS sector data | Secondary + primary validation interviews | Primary validation protocol |
| Market growth rate | World Bank CAGR | Secondary + primary expert interviews | Expert interview guide |
| Customer pain points | Persona templates | Primary customer discovery interviews | Interview guide missing |
| Market structure | Porter Five Forces framework | Framework + primary competitor mapping | Data gathering protocol |
| Willingness-to-pay at target price | Not assessed | Van Westendorp Price Sensitivity Meter | **Entirely missing** |

### Section 05 — Target Market

| Data Point | Current Source | McKinsey Standard | Gap |
|-----------|---------------|-------------------|-----|
| Segment size | Uganda Consumer Demographics (WB) | Secondary demographics + primary survey | Primary survey protocol |
| Segment behaviour | Persona templates | Ethnographic observation / intercepts | Protocol missing |
| Customer lifetime value | Benchmark >3:1 CLV:CAC | Modelled from primary churn data | No churn modelling framework |
| Channel preference | Assumed from industry | Primary channel preference survey | Survey template missing |
| Decision-making unit | Described structurally | Primary interviews with actual buyers | Interview guide missing |

### Section 06 — Competitive Analysis

| Data Point | Current Source | McKinsey Standard | Gap |
|-----------|---------------|-------------------|-----|
| Competitor pricing | Not systematically gathered | Mystery shopping / price survey | **Protocol missing** |
| Competitor market share | Industry data where available | CR4 calculation from primary sources | Methodology present; data protocol absent |
| Competitor product quality | Assessed qualitatively | Blind product testing / NPS benchmarking | Protocol missing |
| Competitor financial health | Not assessed | Public financial statements / trade data | **Financial health protocol missing** |

### Section 10 — Financial Projections

| Data Point | Current Source | McKinsey Standard | Gap |
|-----------|---------------|-------------------|-----|
| Revenue assumptions | Business owner estimates | Primary customer commitment letters / LOIs | LOI/MOU process not described |
| Cost of goods | UNDP benchmarks | Primary supplier quotes | Quotation protocol missing |
| Wage rates | Uganda Labour Market benchmarks | Primary HR market survey | Not enforced |
| Customer acquisition cost | Estimated | Primary campaign testing data | Not modelled |
| Churn rate | Not modelled | Primary retention data or industry analogue | **Missing methodology** |

---

## 2.4 Source Referencing Standards Assessment

### Current Standard (per CLAUDE.md)
- Parenthetical (Author, Year) on first use
- Full bibliographic details in appendices
- Do NOT cite generic advice, user data, or derived projections

### Gap: No Citation Quality Hierarchy

McKinsey/Bain use a three-tier citation hierarchy:
1. **Primary data** (this engagement's research) — highest weight
2. **Tier 1 secondary** (World Bank, IMF, peer-reviewed; published within 5 years)
3. **Tier 2 secondary** (industry reports, practitioner sources, press)

When Tier 2 sources are used for a material claim, they should be triangulated. The system has no protocol for:
- Flagging when a source is >5 years old (some UNDP profiles are 2013)
- Requiring triangulation for major claims (e.g., market size)
- Distinguishing between "research finding" and "informed estimate"
- Dating the data being cited (UBOS 2024 vs 2019 data point in same document)

### Recommendation: Add Data Quality Classification

Add to each market-facing section (04, 05, 06) a mandatory **Data Confidence Assessment**:

```
| Claim | Source | Vintage | Confidence | Triangulation Required? |
|-------|--------|---------|------------|------------------------|
| TAM = UGX 45B | World Bank CAGR applied to UBOS base | 2024 | High | No |
| Market growth 12%/yr | UNDP estimates | 2018 | Medium | Yes — primary interview |
| Competitor A pricing | Author estimate | 2026 | Low | Yes — mystery shopping |
```

---

## 2.5 Data Integrity for Specific Industries

### Food Processing (High Use)
The 46 UNDP business profiles are excellent but some were published 2013–2018. For any plan citing startup costs from these profiles, a **validation note** is required because:
- Construction costs in Uganda increased ~35% (2018–2026)
- Equipment import levies changed (1.5% additional in 2025 Finance Act)
- EFRIS compliance adds operational cost not in 2018 profiles

**Recommendation:** Add a "UNDP Profile Age Adjustment" methodology to the food processing guide — a standardised 2018→2026 cost escalation factor (suggest: construction ×1.35, equipment ×1.20 for non-locally-sourced, wages ×1.25 for Kampala).

### Agriculture / Livestock
Dairy benchmarks and livestock profiles are from World Bank/FAO. Feed costs and milk prices are highly volatile in Uganda. **Recommendation:** Add explicit note that livestock and dairy financial projections require primary supplier and market price quotes at the time of writing, not UNDP benchmarks.

---

## 2.6 Recommended New Reference File

**`meta-market-validation/references/primary-research-protocol.md`**

Contents:
1. When primary research is mandatory vs. optional (decision tree)
2. Expert interview protocol — 15-question structured discussion guide template
3. Customer discovery interview protocol — 20 questions based on Blank & Dorf / Alam
4. Survey design standards — Likert, MaxDiff, NPS, Van Westendorp Price Sensitivity Meter
5. Sample size guidelines by research type and confidence level
6. Mystery shopping / price survey template (competitor audit)
7. Supplier quotation checklist (for COGS validation)
8. Triangulation protocol — how to reconcile conflicting sources
9. Data Confidence Assessment table template
10. LOI/MOU process for converting customer intent to revenue evidence
