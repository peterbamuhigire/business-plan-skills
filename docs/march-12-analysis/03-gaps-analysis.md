# Gaps Analysis
## What Is Missing and Why It Matters

**Date:** 12 March 2026

---

## Gap Classification

| Class | Definition |
|-------|-----------|
| **Critical** | Will cause funding rejection or disqualification with a specific funder type |
| **High** | Significantly weakens plan credibility with international lenders/investors |
| **Medium** | Reduces world-class positioning; noticeable omission to any sophisticated reviewer |
| **Low** | Polish and completeness; not a blocker |

---

## CRITICAL Gaps

### GAP-C1: No ESMP Template
**Severity:** CRITICAL for DFI funding (UDB, IFC, EU, AfDB, GIZ projects)
**Affects:** Any plan seeking development finance funding above approximately UGX 200M

**What is missing:**
Any business applying to Uganda Development Bank, IFC facilities, EU grants, AfDB credit lines, or GIZ-administered programmes must include an Environmental and Social Management Plan as a hard gate. Without it, the application is returned unread. Most EA businesses — and many consultants — do not know this requirement exists until they are rejected.

**IFC/UDB minimum ESMP requirements:**
- Environmental baseline: soil, water, air quality, biodiversity, waste generation
- Social baseline: employment creation, gender equity, community relations, land displacement
- Identification of significant impacts and their classification (Category A/B/C or IFC PS1–8)
- Mitigation measures for each identified impact with responsible party and budget
- Monitoring indicators with measurement frequency
- Grievance mechanism for affected communities

**Current state:** `11-funding-request/SKILL.md` mentions that ESMP is required for DFI applications but does not provide a template. There is no reference file for ESMP anywhere in the suite.

**Who this blocks:** Any plan targeting UDB, IFC, USAID, EU, GIZ, AfDB, or World Bank funding.

**Resolution:** Create `11-funding-request/references/esmp-template.md` — a lightweight but complete IFC-aligned ESMP template. Can be structured as: (1) project description, (2) environmental screening, (3) social screening, (4) mitigation plan table, (5) monitoring plan table, (6) grievance mechanism, (7) ESMP budget. Approximately 5–8 pages when completed.

---

### GAP-C2: No Kenya Country-Context File
**Severity:** CRITICAL for plans targeting the Kenyan market or Kenyan funders
**Affects:** Any plan that references "East Africa" scope

**What is missing:**
Kenya is the largest economy in East Africa and the financial hub of the region. Nairobi is where most EA PE/VC investors, international development partners, and regional headquarters are based. A suite that presents itself as East African but only supports Uganda defaults is operationally incomplete for 40%+ of potential use cases.

Kenya differences that significantly affect plan content:
- **Currency:** KES (Kenyan Shilling) — ~KES 130/$1 (2025)
- **Corporate tax:** 30% (same as Uganda but different allowances)
- **VAT:** 16% threshold KES 5M/year (vs Uganda UGX 150M/18%)
- **PAYE:** Different bands, different employer obligations
- **Regulatory bodies:** KRA, CAK (Competition), KEBS (standards), NEMA Kenya, CA (communications), CBK (banking), CMA (capital markets)
- **Banking:** KCB, Equity, Co-op, Stanbic Kenya, I&M — different loan products, different DSCR requirements
- **Registration:** Registrar of Companies, Kenya Revenue Authority (KRA) PIN

**Current state:** `country-context/template.md` exists with an 11-section structure. No Kenya file exists.

**Resolution:** Complete `country-context/kenya.md` using the existing template. This is primarily a research and data-entry task, not a framework design task. Priority: highest among all country files.

---

## HIGH Gaps

### GAP-H1: Porter's Five Forces Not Explicitly Present
**Severity:** HIGH — reduces credibility with all sophisticated plan reviewers
**Affects:** Section 06 (Competitive Analysis), Section 04 (Market Analysis)

**What is missing:**
Porter's Five Forces is the most universally recognised industry analysis framework in business education and consulting. Every MBA graduate, every bank credit analyst trained internationally, every IFC investment officer, and every McKinsey-trained consultant will expect to see it. Its absence signals either unfamiliarity with standard business analysis methodology or an oversight.

The five forces: **Competitive Rivalry** (industry intensity), **Supplier Power**, **Buyer/Customer Power**, **Threat of New Entrants**, **Threat of Substitutes**.

These concepts are partially embedded in `06-competitive-analysis/SKILL.md` under SWOT and competitive matrix, but they are not named and not structured as a five-forces analysis. This means plans produced by the suite will not contain an explicit Porter's Five Forces analysis — a noticeable omission.

**PESTLE** (Political, Economic, Social, Technological, Legal, Environmental) faces the same issue — the content is distributed across the suite but the named framework is absent.

**Resolution:** Add a Porter's Five Forces section to `06-competitive-analysis/SKILL.md` (15–20 lines with a structured template). Add PESTLE as a named checklist within `04-market-analysis/SKILL.md` (the macro environment section). These are additions to existing skills, not new files.

---

### GAP-H2: README.md Is Significantly Outdated
**Severity:** HIGH — misrepresents the suite's capabilities; damages credibility with new users
**Affects:** All new users, clients, and anyone evaluating the suite

**What is missing:**
The current README.md lists:
- 5 meta-skills (actual: 8)
- No mention of meta-pitch-preparation, meta-presentation-design, meta-due-diligence
- No mention of country-context system
- No mention of industry guides (13 sector guides)
- No mention of blog system
- No mention of 11b-grant-proposal
- Describes the suite as "Built on frameworks from six foundational texts" (actual: 25+ books)
- Lists utility skills that are outdated

A consultant or client reading the README would significantly underestimate the suite's capabilities. This is a credibility problem.

**Resolution:** Rewrite README.md to reflect the actual 37-skill suite. This is a 1–2 hour task.

---

### GAP-H3: No Insurance Framework Reference
**Severity:** HIGH for all bank loan and DFI plans
**Affects:** Section 12 (Risk Analysis), Section 11 (Funding Request)

**What is missing:**
Ugandan banks require insurance on all loan-collateralised assets as a condition of lending. The insurance requirement appears in `meta-bankability-scoring/SKILL.md` (CAMPARI Insurance item: "Insurance on collateral assets included in operating budget") but there is no reference file explaining:
- Which insurance products are required (asset insurance, fire, theft)
- Which are recommended (public liability, business interruption, key-person)
- What the approximate cost is (as a % of asset value or fixed UGX amount)
- Which insurers operate in Uganda (UAP, Jubilee, AIG, Liberty, CIC, ICEA Lion)
- How to present insurance costs in the operating budget

A plan that says "we have insurance" without naming the type, insurer, and annual premium will raise a flag with any credit officer.

**Resolution:** Create `12-risk-analysis/references/uganda-insurance.md` — 3–4 pages covering required vs. recommended insurance by business type, Uganda insurer landscape, approximate premium rates, and how to present insurance in Section 12.

---

### GAP-H4: No Competitor Financial Intelligence Guidance
**Severity:** HIGH for plans with significant competition
**Affects:** Section 06 (Competitive Analysis)

**What is missing:**
A world-class competitive analysis does not just list competitors — it estimates their revenues, margins, and market shares. In Uganda and East Africa, competitors are rarely public, but financial intelligence can be gathered from:
- URSB company searches (filing history, director changes, charges registered)
- Uganda Gazette (company announcements, deregistrations)
- Industry association data (UNCCI, UHOA, UMA, UFPEA)
- Tax compliance status (URA confirms whether businesses are TIN-registered, VAT-registered)
- Physical observation (customer counts, pricing surveys, product range audits)
- Supplier conversations (a major supplier often knows competitors' volumes)
- LinkedIn employee counts and growth rates

`meta-due-diligence/references/osint-business-intelligence.md` covers this (5-layer OSINT, Uganda/EA workarounds) but is not linked to `06-competitive-analysis/SKILL.md`. The knowledge exists in the suite but is not connected to where it is needed.

**Resolution:** Add a "Competitor Intelligence" section to `06-competitive-analysis/SKILL.md` with a cross-reference to `meta-due-diligence/references/osint-business-intelligence.md`. No new content needed — this is a wiring task.

---

### GAP-H5: No Unified Pitch Deck Skill
**Severity:** HIGH for usability and consultant workflow
**Affects:** All plans that include a pitch deck deliverable

**What is missing:**
The suite has two excellent skills that together constitute a complete pitch deck system:
- `meta-pitch-preparation/SKILL.md` — pitch strategy, frame control, message architecture
- `meta-presentation-design/SKILL.md` — slide design, master template, coaching protocol

But these are two separate skills that a user must know to invoke in sequence. There is no single `pitch-deck` skill that:
1. Confirms this is a pitch deck request (not just a plan)
2. Sequences the two meta-skills in the correct order
3. Maps the business plan sections to the 13-slide master template
4. Produces a complete "pitch deck brief" document as output

Without a unified entry point, users are likely to invoke only one of the two skills, missing the complementary methodology.

**Resolution:** Create `pitch-deck/SKILL.md` — a 100–120 line integration skill that sequences the two meta-skills and produces a structured pitch deck brief. The content already exists; this is an integration and routing task.

---

## MEDIUM Gaps

### GAP-M1: No Tanzania / Rwanda Country-Context Files
**Severity:** MEDIUM — limits EA regional positioning
After Kenya, Tanzania and Rwanda are the most common EA markets for business plan clients.

### GAP-M2: No Working Capital Management Section in §10
**Severity:** MEDIUM — missing a key cash flow management concept
Debtor days, creditor days, inventory turns, and cash conversion cycle should be explicit in the financial projections skill. Profitable businesses fail because of working capital, not P&L.

### GAP-M3: No B2B / Government Tender Guidance in §07
**Severity:** MEDIUM — significant revenue channel for Uganda SMEs
LPO (Local Purchase Order) financing, government procurement processes, and tender preparation are major business activities that are not covered in the marketing/sales strategy skill.

### GAP-M4: No ISO / UNBS Quality Standards Guidance
**Severity:** MEDIUM — required for export, DFI funding, certain government contracts
No guidance on when ISO 9001, UNBS certification, or KEBS (Kenya) certification is required and how to cost it in the operational plan.

### GAP-M5: No Advisory Board Recruitment Template
**Severity:** MEDIUM — a frequent need for young/first-time entrepreneurs
When founding teams lack sector experience, a credible advisory board is the compensating factor. No template exists for how to identify, approach, and compensate advisors.

### GAP-M6: meta-quarterly-gameplan Is Under-Developed
**Severity:** MEDIUM — execution is where most plans fail
The most execution-focused meta-skill has less content than any other meta-skill. Given that implementation failure is the primary reason funded businesses underperform, this deserves more investment.

### GAP-M7: No Primary Research Protocol
**Severity:** MEDIUM — plans without primary data are weaker
No structured customer survey template, interview guide, or focus group protocol. The suite tells users they need primary market data but does not give them a methodology to generate it.

---

## LOW Gaps

### GAP-L1: No EA Governance Standards for DFI Loans > UGX 500M
Board composition requirements, audit committee, conflict of interest policy — required by UDB and most DFIs for loans above a certain size.

### GAP-L2: No UDB Submission Format
UDB requires a specific feasibility study format distinct from a commercial bank business plan. A UDB-specific template would add value.

### GAP-L3: No Shareholder Agreement Template
For businesses with multiple founders or incoming investors, a basic SHA template in the appendices would be valuable.

### GAP-L4: Appendices Skill is the Weakest Core Section
At approximately 200 lines, it is the thinnest core skill. Could benefit from a data room structure guide cross-referenced from meta-due-diligence.

### GAP-L5: MECE Cross-Reference Missing in §04, §06, §09
The Pyramid Principle and MECE are implemented in §01 and meta-market-validation but not explicitly prompted in the analysis sections where they are most needed.

---

## Summary: Gaps by Priority

| Gap | Severity | Effort | Resolution |
|-----|----------|--------|-----------|
| GAP-C1: ESMP template | Critical | M | Create `esmp-template.md` |
| GAP-C2: Kenya country file | Critical | M | Complete `country-context/kenya.md` |
| GAP-H1: Porter's Five Forces | High | S | Add to §06 and §04 SKILL.md |
| GAP-H2: README outdated | High | S | Rewrite README.md |
| GAP-H3: Insurance framework | High | M | Create `uganda-insurance.md` |
| GAP-H4: Competitor intelligence | High | S | Wire OSINT ref into §06 |
| GAP-H5: Unified pitch deck skill | High | S | Create `pitch-deck/SKILL.md` |
| GAP-M1: Tanzania/Rwanda files | Medium | M | Fill country-context template |
| GAP-M2: Working capital in §10 | Medium | S | Add section to §10 SKILL.md |
| GAP-M3: B2B/govt tender in §07 | Medium | S | Add section to §07 SKILL.md |
| GAP-M4: ISO/UNBS guidance | Medium | S | Add to §08 SKILL.md |
| GAP-M5: Advisory board template | Medium | S | Add to §09 SKILL.md |
| GAP-M6: Quarterly gameplan depth | Medium | M | Expand meta-quarterly-gameplan |
| GAP-M7: Primary research protocol | Medium | M | Add to meta-market-validation |

S = Small (< 2 hours) | M = Medium (2–8 hours)
