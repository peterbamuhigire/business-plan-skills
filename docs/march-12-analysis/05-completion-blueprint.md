# Completion Blueprint
## Actionable Roadmap to World-Class Standard

**Date:** 12 March 2026

---

## Blueprint Objective

Bring the suite from its current 7.8/10 to a 9.0/10 world-class standard — capable of producing business plans that would be accepted by:
- Ugandan and Kenyan commercial banks
- Uganda Development Bank (UDB) and other DFIs
- International impact investors (Acumen, Novastar, Renew Capital)
- Development partners (USAID, EU, GIZ, IFC)
- PE/VC investors reviewing EA opportunities

---

## Phase 1: Critical Fixes (Highest ROI — complete first)

These are the items that either cause outright rejection or most visibly signal incomplete methodology.

### Task 1.1 — Create Pitch Deck Skill
**File:** `pitch-deck/SKILL.md`
**Complexity:** S (1–2 hours)
**Impact:** High — solves the primary workflow gap; makes the three-component consulting service (plan + deck + training) explicitly invocable as a single skill

**What to build:**
- 100–120 line skill that sequences `meta-pitch-preparation` → `meta-presentation-design`
- Upfront type identification: investor pitch / bank presentation / grant committee / board
- Maps the 15 plan sections to the 13-slide master template
- Outputs a "pitch deck brief" with: One Thing, Sparkline, slide-by-slide content assignments, design decisions, rehearsal schedule
- Cross-references both meta-skills throughout
- Quality criteria: deck can be built from the brief without further guidance

---

### Task 1.2 — Create ESMP Template
**File:** `11-funding-request/references/esmp-template.md`
**Complexity:** M (3–5 hours)
**Impact:** Critical — unlocks DFI funding eligibility for all plans above ~UGX 200M

**What to build:**
- IFC Environmental and Social Categorisation table (Category A/B/C + IFC Performance Standards 1–8)
- Uganda NEMA Environmental Impact Assessment screening table (when EIA is required by law)
- 8-column ESMP table template: Impact | Significance | Mitigation | Responsible Party | Timeline | Cost | Monitoring Indicator | Reporting Frequency
- Environmental baseline checklist: land use, water sources, solid waste, air quality, biodiversity
- Social baseline checklist: employment, gender, land/displacement, community health
- Grievance mechanism structure (required by IFC PS1)
- ESMP budget line items (to be included in operational budget, Section 08)
- Guidance on when to hire a certified Environmental Practitioner vs. self-assessment sufficiency
- Uganda-specific: NEMA permit categories; when to engage UWA (Uganda Wildlife Authority) for biodiversity concerns; water extraction permits (DWRM)

**Note:** A plan that states "Category B — limited impact; ESMP as below" with a credible 2-page table will pass most DFI screening desks. This does not need to be a 50-page environmental report.

---

### Task 1.3 — Add Porter's Five Forces to §06
**File:** `06-competitive-analysis/SKILL.md` (edit, not new file)
**Complexity:** S (1 hour)
**Impact:** High — eliminates the most visible methodology gap for internationally trained reviewers

**What to add:**
```
## Porter's Five Forces Industry Analysis

Apply Porter's Five Forces to establish the structural attractiveness of the industry (Porter, 1980).

| Force | Key Questions | Assessment |
|-------|--------------|------------|
| **Competitive Rivalry** | How many competitors? How intense is price competition? How differentiated is the industry? | High / Medium / Low |
| **Supplier Power** | How many suppliers? Are inputs commoditised or specialised? How easy to switch suppliers? | High / Medium / Low |
| **Buyer Power** | How many customers? Are they price-sensitive? Can they backward-integrate? | High / Medium / Low |
| **Threat of New Entrants** | Are barriers to entry high? Capital requirements? Regulatory licences? Scale advantages? | High / Medium / Low |
| **Threat of Substitutes** | Can customers meet the same need a different way? How price-sensitive is demand? | High / Medium / Low |

**Five Forces summary:** State whether the industry is structurally attractive (most forces Low = favourable) or unattractive (most forces High = unfavourable). Then explain how your competitive strategy addresses the most unfavourable forces.

**Cross-reference:** `meta-due-diligence/references/osint-business-intelligence.md` for methodology on gathering competitor intelligence in low-data EA markets.
```

---

### Task 1.4 — Rewrite README.md
**File:** `README.md`
**Complexity:** S (1–2 hours)
**Impact:** High — critical for credibility, discoverability, and new user onboarding

**What to include:**
- Updated skill count: 37 skills (not the original 15+5)
- All three categories: core plan skills (01–15), meta-analytical skills (8), support skills (14)
- Prominent mention of pitch deck system, due diligence system, industry guides (13 sectors)
- Country-context system and how to use it
- The three-component consulting service: plan + pitch deck + training
- Quick-start workflow: for a Uganda bank loan / for an equity pitch / for a grant / for a complete plan
- Updated methodology section: 25+ books and frameworks, not just 6
- "Recent additions" section to signal active development

---

### Task 1.5 — Wire OSINT into §06 Competitive Analysis
**File:** `06-competitive-analysis/SKILL.md` (edit)
**Complexity:** S (30 minutes)
**Impact:** Medium-High — connects competitor intelligence to competitive analysis

Add a "Competitor Intelligence Sources" section pointing to `meta-due-diligence/references/osint-business-intelligence.md` with a one-paragraph note on the 5-layer OSINT approach for EA markets.

---

## Phase 2: Country Expansion

### Task 2.1 — Create Kenya Country-Context File
**File:** `country-context/kenya.md`
**Complexity:** M (4–6 hours — primarily research)
**Impact:** High — unlocks Kenya market coverage for 40%+ of potential EA use cases

**Sections to complete (using `country-context/template.md`):**
1. Basic information (currency KES ~130/$1, major cities, languages)
2. Macroeconomics (GDP, growth rate, inflation, sectors)
3. Business registration (Registrar of Companies, Huduma Centre, e-Citizen)
4. Taxation (KRA, corporate 30%, VAT 16%, PAYE bands, NHIF, NSSF)
5. Regulatory bodies (CAK, KEBS, NEMA, CBK, CMA, CA)
6. Banking and finance (KCB, Equity, Co-op Bank, I&M, NCBA; DFI: KDB, AFC)
7. Labour market (wage benchmarks, Employment Act 2007, key sectors)
8. Market data (GDP per capita, consumer segments, mobile penetration)
9. Risk context (political, currency, regulatory specific to Kenya)
10. Data sources (KNBS, CBK Annual Report, Kenya Revenue Authority)

---

### Task 2.2 — Create Tanzania Country-Context File
**File:** `country-context/tanzania.md`
**Complexity:** M (4–6 hours)
**Impact:** Medium — Tanzania is the third major EA market

---

### Task 2.3 — Create Rwanda Country-Context File
**File:** `country-context/rwanda.md`
**Complexity:** M (3–4 hours)
**Impact:** Medium — Rwanda's Doing Business ranking (#38 globally) makes it a significant investment destination

---

## Phase 3: Quality Strengthening

### Task 3.1 — Create Uganda Insurance Reference
**File:** `12-risk-analysis/references/uganda-insurance.md`
**Complexity:** M (2–3 hours)
**Impact:** High for bank loan plans — completes the CAMPARI Insurance criterion

**Content:**
- Required insurance (bank conditions): fire and perils on mortgaged property, comprehensive on pledged vehicles
- Recommended insurance: public liability, employer's liability/workmen's compensation, business interruption, key-person life
- Uganda insurers: UAP, Jubilee, AIG, Liberty, CIC, ICEA Lion, Sanlam, Prudential
- Approximate premium rates: property (0.3–0.5% of value/year), vehicles (4–6% of value/year), public liability (UGX 500K–2M/year for SME)
- How to present in operating budget: annual insurance premium as a fixed operating cost line
- How to present in risk section: insurance as a mitigation for each insurable risk
- Insurance broker recommendation (simplifies multi-product procurement)

---

### Task 3.2 — Add Working Capital Section to §10
**File:** `10-financial-projections/SKILL.md` (edit)
**Complexity:** S (1 hour)
**Impact:** Medium — closes a significant gap in cash management guidance

**What to add:**
- Debtor Days = (Debtors / Revenue) × 365 — target: ≤ 30 days for Uganda SME
- Creditor Days = (Creditors / COGS) × 365 — aim: ≥ 30 days (use supplier credit)
- Inventory Days = (Inventory / COGS) × 365 — lower is better
- Cash Conversion Cycle = Debtor Days + Inventory Days − Creditor Days
- Warning: A business with a long CCC needs more working capital than projected profits suggest
- Uganda-specific: mobile money/M-Pesa collections speed up debtor days vs bank transfer; construction and government clients often pay in 60–90 days

---

### Task 3.3 — Add PESTLE to §04 Market Analysis
**File:** `04-market-analysis/SKILL.md` (edit)
**Complexity:** S (45 minutes)
**Impact:** Medium — adds a recognised framework name to existing content

**What to add:**
A 6-row PESTLE table as a named framework within the macro environment analysis section. The content already exists; naming it explicitly signals methodological rigour.

---

### Task 3.4 — Expand meta-quarterly-gameplan
**File:** `meta-quarterly-gameplan/SKILL.md` + new reference file
**Complexity:** M (3–4 hours)
**Impact:** Medium — execution is where most funded businesses fail

**What to build:**
- Explicit 13-week sprint planning template (week-by-week, not just month-by-month)
- OKR (Objectives and Key Results) integration — how to set Q1 OKRs from the annual plan
- Variance analysis template: actual vs. plan with corrective action prompts
- Early warning indicators: what signals to watch in weeks 4, 8, and 12 to know if the quarter is off-track
- Decision framework: when to stay the course vs. adjust the plan vs. escalate to the board

---

### Task 3.5 — Add B2B/Government Tender Section to §07
**File:** `07-marketing-sales-strategy/SKILL.md` (edit)
**Complexity:** S (1 hour)
**Impact:** Medium — significant revenue channel for Uganda SMEs

**What to add:**
- LPO (Local Purchase Order) financing — how it works, what banks/invoice financers require
- Government procurement: PPDA (Public Procurement and Disposal of Assets Authority) thresholds
- Tender preparation basics: what goes in a tender bid, how to price for government
- Building a public sector client reference list: why one government client is a significant asset
- Risk: government payment delays — how to manage cash flow when government owes you money

---

## Phase 4: Polish and Integration

### Task 4.1 — Add MECE Reminders to §04, §06, §09
Add single-line MECE/Pyramid cross-reference to these three skills.

### Task 4.2 — Add Advisory Board Template to §09
2–3 paragraph section on how to build a credible advisory board when the founding team is young.

### Task 4.3 — Add Data Room Link to §15 Appendices
Cross-reference meta-due-diligence data room structure guide from the appendices skill.

### Task 4.4 — Add ISO/UNBS Standards Note to §08
Brief note on when UNBS certification or ISO 9001 is required and how to cost it.

### Task 4.5 — Consistent Version Tracking
Add a "Last updated" date to every SKILL.md frontmatter so users know whether a skill reflects current regulations.

---

## Completion Roadmap Summary

| Phase | Tasks | Effort (hours) | Impact |
|-------|-------|---------------|--------|
| Phase 1: Critical Fixes | 5 tasks | 6–12 hours | Very High |
| Phase 2: Country Expansion | 3 tasks | 11–16 hours | High |
| Phase 3: Quality Strengthening | 5 tasks | 9–13 hours | Medium-High |
| Phase 4: Polish | 5 tasks | 3–5 hours | Medium |
| **Total** | **18 tasks** | **29–46 hours** | **→ 9.0/10** |

---

## Expected Score After Each Phase

| After Phase | Estimated Score | Key Gain |
|-------------|----------------|---------|
| Current (March 12) | 7.8/10 | — |
| After Phase 1 | 8.4/10 | Porter's Five Forces, ESMP, unified pitch deck, README |
| After Phases 1–2 | 8.7/10 | Kenya + Tanzania + Rwanda coverage |
| After Phases 1–3 | 9.0/10 | Insurance, working capital, PESTLE, quarterly gameplan |
| After All Phases | 9.2/10 | Full polish and integration |

---

## What "9.0/10" Means in Practice

A suite at 9.0/10 is capable of producing plans that:
- Pass the credit desk at any Ugandan commercial bank, UDB, or ACF
- Are credible with IFC, USAID, EU, and GIZ programme officers
- Meet the preliminary screening criteria of EA impact investors (Acumen, Novastar)
- Would be recognised as methodologically rigorous by any McKinsey, BCG, or Deloitte analyst
- Cover the three main EA markets: Uganda, Kenya, Tanzania

The gap to 10.0/10 — primary market research capability, Monte Carlo simulation, Bloomberg/Euromonitor data access, senior practitioner judgement — cannot be closed by a skill suite. It requires human expertise.

The suite's role is to make that human expertise go further, faster, and more consistently.
