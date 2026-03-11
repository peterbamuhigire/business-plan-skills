# Consulting Quality Gap Analysis
## Target: Plans that Bain, McKinsey, and Deloitte would be proud of

The user's stated aspiration: business plans that meet management consulting standards —
not just bankable documents but analytically rigorous, structured, and compelling deliverables.

This audit identifies the gap between current suite quality and consulting firm standard.

---

## What Defines a McKinsey/Bain/Deloitte Quality Document

Management consulting deliverables differ from traditional business plans in five ways:

| Dimension | Current Suite | McKinsey/Bain/Deloitte Standard |
|-----------|--------------|----------------------------------|
| **Structure** | Section-by-section, sequential | Pyramid: conclusion first, evidence below (Minto) |
| **Logic** | Descriptive ("here is our market") | Hypothesis-driven ("we believe X because Y and Z") |
| **MECE compliance** | Moderate (some overlap between sections) | Strict: every category Mutually Exclusive, Collectively Exhaustive |
| **Data standards** | Cite sources; flag estimates | Every chart has a source, every number has a footnote, zero rounding without disclosure |
| **Visual communication** | Markdown tables and bullets | Chart selection framework (waterfall, Minto-Minto charts, pyramid diagrams); data tells a story |

---

## Gap 1: Structured Communication — The Pyramid Principle `CRITICAL`

**Current state:** Plans are written section by section. Each section leads with context and ends with conclusions. This is bottom-up: evidence → argument → conclusion.

**McKinsey standard:** Bottom line up front (BLUF). Lead with the governing thought. Support with key lines of argument. Back each argument with data. Audience gets the answer in the first sentence, not the last.

**The Minto Pyramid:**
```
GOVERNING THOUGHT (the one thing the reader must know)
    └── KEY LINE 1            KEY LINE 2            KEY LINE 3
         └── Support data      └── Support data       └── Support data
```

**What this changes in every section:**
- Executive summary: state the investment conclusion in sentence 1, not paragraph 8
- Market analysis: "This is a UGX 4.7 trillion market growing at 12% — large enough to support a UGX 350M business" before any methodology
- Competitive analysis: "We can win because of two durable advantages" before listing competitors

**Book to find:** Barbara Minto — *The Pyramid Principle: Logic in Writing and Thinking* (Pearson, classic edition)

---

## Gap 2: MECE Thinking and Issue Tree Construction `HIGH PRIORITY`

**Current state:** Risk categories, market segments, and financial drivers are listed but not structured for MECE compliance. There is often overlap (e.g., "regulatory risks" and "compliance risks" in the same list) and gaps (entire categories of risk not captured).

**McKinsey standard:** Every analytical framework is MECE — Mutually Exclusive (no overlap), Collectively Exhaustive (no gaps). Issue trees decompose problems into branches that cover all possibilities without duplication.

**What this changes:**
- Market sizing: TAM/SAM/SOM must be MECE — the segments must add up to the whole market with no overlap
- Risk register: risks must be classified in non-overlapping categories that together cover all risk dimensions
- Revenue model: revenue streams must be mutually exclusive with no double-counting

**Book to find:** *The McKinsey Way* by Ethan Rasiel (covers MECE, issue trees, hypothesis-driven analysis); *The McKinsey Mind* by Rasiel & Friga

---

## Gap 3: Strategic Portfolio and Positioning Tools `HIGH PRIORITY`

**Current state:** The suite has Porter's Five Forces (in market-strategy-frameworks.md), SWOT, competitive matrix, BCG matrix is not present.

**Missing strategic frameworks used by consulting firms:**

| Tool | What it does | Currently in suite? |
|------|-------------|---------------------|
| BCG Growth-Share Matrix | Classify products by market growth and relative share | Not present |
| GE-McKinsey Nine-Box | Business unit attractiveness vs. competitive strength | Not present |
| McKinsey 7-S Framework | Organisational alignment (strategy/structure/systems/shared values/style/staff/skills) | Not present |
| Ansoff Growth Matrix | Market penetration/development/product development/diversification | Partially present (Blank & Dorf mentions it) |
| Value chain analysis (Porter) | Internal activities that create competitive advantage | Partially in value-chain-competencies.md |
| Balanced Scorecard | Four-perspective performance measurement (financial/customer/internal/learning) | Partial reference |
| Jobs-to-be-Done (Christensen) | Why customers hire products; disruptive innovation framework | Not present |
| Blue Ocean Strategy | Value innovation; eliminate/reduce/raise/create (ERRC) grid | Referenced but not extracted |
| McKinsey Three Horizons | Innovation and growth pipeline (Horizon 1/2/3) | Not present |

**Books to find:**
- Kim & Mauborgne — *Blue Ocean Strategy* (if not already extracted from references)
- Clayton Christensen — *The Innovator's Dilemma* (disruption theory and Jobs-to-be-Done)
- Kaplan & Norton — *The Balanced Scorecard* (four-perspective measurement)
- Robert Waterman / Peters & Waterman — original 7-S framework paper

---

## Gap 4: Rigorous Financial Modelling `HIGH PRIORITY`

**Current state:** Strong Uganda financial templates, tax framework, DSCR. Good for bank lending. Insufficient for consulting quality or private equity.

**Missing:**
- **DCF modelling** — Discounted Cash Flow with terminal value; not in any reference file
- **IRR (Internal Rate of Return)** — The primary metric for equity investors; absent
- **NPV (Net Present Value)** — Mentioned briefly in process costing; not modelled for the business
- **Sensitivity tables (two-way)** — McKinsey shows a 3×3 grid: e.g., price × volume; the suite has scenario analysis but not in consulting format
- **Waterfall analysis** — How investment returns flow from revenue through costs to equity
- **Working capital deep-dive** — Cash conversion cycle, receivables days, payables days, inventory days as management levers
- **Industry benchmarking** — Every financial ratio compared to sector median and top quartile

**Books to find:**
- Fridson & Alvarez — *Financial Statement Analysis: A Practitioner's Guide* (ratio analysis)
- Damodaran — *Investment Valuation* or *The Little Book of Valuation* (DCF/IRR/NPV)
- A financial modelling textbook (Pignataro — *Financial Modeling and Valuation*)

---

## Gap 5: Data Visualisation and Document Standards `MODERATE PRIORITY`

**Current state:** The suite outputs Markdown — tables, bullets, and headings. This is appropriate for the SKILL.md format but final plans need presentation-quality visual standards.

**Missing:**
- Chart selection guidance: when to use bar charts vs. line charts vs. waterfall vs. pie charts (hint: rarely pie charts)
- McKinsey visual standards: each chart has a "so what" headline (not a title), axis labels, source footnote
- Slide/document storyboarding (before writing, design the narrative arc of visuals)
- Data table formatting standards (significant figures, thousands separators, UGX vs. $ labelling)
- Executive presentation format: not a 50-page document but a 20-page deck with appendices

**Books to find:**
- Gene Zelazny — *Say It with Charts* (McKinsey's internal visualisation standard, published externally)
- Garr Reynolds — *Presentation Zen* (visual communication principles)
- Cole Nussbaumer Knaflic — *Storytelling with Data*

---

## Gap 6: Multi-Country Localisation Architecture `HIGH PRIORITY`

**User's requirement:** Plans for Fiji, Algeria, Canada, or any market should work when the user provides country-specific research.

**Current state:** Uganda is hardcoded throughout the suite. CLAUDE.md states "Default context: Uganda (UGX)." Skills reference Uganda-specific files directly (uganda-tax-framework.md, uganda-macro-context-2025.md, doing-business-uganda.md). When a user provides data for another country, the skills have no systematic way to receive and use it.

**What's needed:**
- A **country context file template** — a structured template the user fills in with: currency, exchange rate, GDP, inflation, major banks, tax rates, regulatory bodies, key data sources
- Skills should check whether a country context file exists and use it, or fall back to Uganda defaults
- Skills should distinguish between **universal frameworks** (market sizing methodology, financial ratios, CAMPARI) and **context-specific data** (tax rates, regulatory requirements, local benchmarks)
- A `country-context/` directory for user-provided country files (similar to how `references/` files work for Uganda)

**Implementation:** This is primarily a CLAUDE.md architecture change and a new template file. No new book is needed — it is a structural redesign of how skills consume country data.

**Action:** Create `country-context/template.md` — a blank-fill country profile template. Update CLAUDE.md to tell Claude how to use it when present.

---

## Gap 7: Hypothesis-Driven Analysis (Consulting Method) `MODERATE PRIORITY`

**Current state:** Skills generate sections descriptively. A market analysis section describes the market. A competitive analysis describes competitors.

**Consulting method:** Start with a hypothesis. "We believe this business can achieve 12% market share within 3 years because: (1) the market is fragmented, (2) no competitor serves the underserved mid-market, (3) our cost structure enables 15% price advantage." Then assemble evidence to test this hypothesis. Revise the hypothesis based on evidence. Conclude with the validated (or modified) hypothesis.

**This is a methodology shift, not just a book addition.** It requires adding a "hypothesis statement" step to the generation process of each analytical skill.

**Book to find:** Rasiel — *The McKinsey Way* (covers hypothesis-driven problem solving, issue trees, MECE); alternatively, *The McKinsey Mind* by Rasiel & Friga.

---

## Consulting Quality Enhancement Roadmap

| Priority | Gap | Fix | Skill(s) Affected |
|----------|-----|-----|-------------------|
| 1 | Pyramid Principle | Add Minto's book + update each skill's generation process | All analytical skills |
| 2 | MECE / issue trees | Add McKinsey Way book + update analytical frameworks | 04, 05, 06, 12 |
| 3 | DCF / IRR / NPV | Add Damodaran or Pignataro | 10, 11 |
| 4 | Strategic portfolio tools | Add BCG matrix, 7-S, Three Horizons | 06, 08 |
| 5 | Chart selection | Add Zelazny or Knaflic | 01, 04, 10 |
| 6 | Multi-country architecture | Design country-context template | CLAUDE.md + all skills |
| 7 | Hypothesis-driven process | Add Rasiel; update generation steps | 04, 05, 06, 10 |
| 8 | Jobs-to-be-Done / disruption | Add Christensen | 03, 06 |
