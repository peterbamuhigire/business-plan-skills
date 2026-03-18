# Pillar 6 — Competitive Intelligence Depth
**Score: 7.0 / 10**

The competitive analysis frameworks are excellent — Porter Five Forces (with quantified thresholds), Ohmae 3C, Kaza differentiation, Teece moats, Lafley & Martin strategy cascade. The gap is between framework application and data gathering. McKinsey/Bain analysts do not just apply frameworks to assumptions — they gather primary competitive data, benchmark competitor financials, and conduct systematic market intelligence. That data-gathering protocol is largely absent.

---

## 6.1 What Is Present (Strengths)

| Component | Location | Assessment |
|-----------|----------|------------|
| Porter Five Forces (full) | 06-competitive-analysis, competitive-strategy-porter.md | Force thresholds defined: CR4 <40% = competitive; 60-80% = oligopoly; Uganda/EA examples |
| Ohmae 3C Strategic Triangle | 06-competitive-analysis | Key Factors for Success methodology — underrated and powerful |
| Kaza Differentiation Layers | 06-competitive-analysis | Aesthetic/social/boundary/purposeful — practical for EA positioning |
| Teece Competitive Moats | 06-competitive-analysis | Network effects, IP, complementary assets, tacit knowledge, first-mover |
| Lafley & Martin Strategy Cascade | 06-competitive-analysis | Where to Play / How to Win framing |
| Porter Competitor Analysis Framework | competitive-strategy-porter.md | 4 components: Future Goals / Current Strategy / Assumptions / Capabilities |
| Strategic Groups | competitive-strategy-porter.md | Strategic group mapping by mobility barriers |
| Market Signals | competitive-strategy-porter.md | Price signals, capacity announcements, competitor moves |
| Competitive Advantage Value Chain | competitive-strategy-porter.md | 10 cost drivers, differentiation drivers per activity |
| Good vs. Bad Competitors | competitive-strategy-porter.md | Legitimising market, stabilising price — retain vs. destroy decision |
| OSINT Framework (5 layers) | meta-due-diligence/references/osint-business-intelligence.md | Digital footprint, public records, supply chain intel, financial signals |

---

## 6.2 Data-Gathering Protocol Gaps

### Gap 1 — Competitive Price Survey Protocol (HIGH IMPACT)

**What McKinsey does:** Before pricing analysis, analysts conduct systematic price surveys — visiting competitor locations, calling for quotes, checking price lists, monitoring online listings. For EA markets this is particularly important because pricing is rarely transparent.

**Current state:** Kaza value-based pricing 5-step framework tells *how to set* a price. Porter competitor analysis framework tells *what to look for*. But there is no operational protocol for *how to gather* competitor pricing data in EA markets.

**Missing methodology:**
- Mystery shopping checklist (what to observe, what to buy, what to ask)
- Online price monitoring (competitor websites, social media price posts, OLX/Jumia listings)
- Supplier/wholesaler intelligence (what prices do they quote to competitors?)
- Trade association data (industry pricing surveys where available)
- "Three-quote" protocol — getting quotes from three competitors before setting your own price

**Recommendation:** Add `06-competitive-analysis/references/competitive-data-gathering.md` with:
- Mystery shopping protocol (food/retail/services specific templates)
- Price survey template (gather: base price, discount structure, payment terms, quality tier)
- Digital intelligence checklist (Facebook pages, Instagram posts, Google Business listings)
- Supplier intelligence approach (ask suppliers what competitors are paying for similar volumes)
- Trade press / market research sources by industry in Uganda/EA

### Gap 2 — Competitor Financial Benchmarking (MEDIUM-HIGH IMPACT)

**What McKinsey does:** For any publicly traceable competitor (formally registered, listed company, or reporting to industry association), analysts extract financial ratios — revenue range, EBITDA margin, employee count, revenue per employee, asset turnover.

**Current state:** Uganda Private Sector Markets reference (`uganda-private-sector-markets.md`) has macro SME data. UNDP profiles give startup-cost benchmarks for comparable businesses. But no protocol guides systematic competitor financial assessment.

**Uganda-specific sources available (not currently leveraged):**
- URSB company registry: registered companies, directors, sometimes filed accounts
- Uganda Revenue Authority: no direct access, but registered tax numbers confirm legitimacy
- KCCA business registry: Kampala business permits, categories, since dates
- Industry associations (UNABCEC, UEPB, UMA): member directories, sometimes financial benchmarks
- Bank credit bureau (CRB Africa): used by lenders; not publicly accessible but reference-able
- Social media signal: Instagram/Facebook follower counts, post engagement as proxy for market share

**Recommendation:** Add to `06-competitive-analysis/references/competitive-data-gathering.md`:
- Uganda public sources for competitor intelligence (URSB, KCCA, URA TIN lookup)
- Financial ratio proxies when formal accounts not available (staff count × estimated revenue/employee)
- Social media intelligence (follower count → customer base estimate; post frequency → operational health)
- Industry association intelligence gathering
- Supplier reference checking (what do suppliers say about competitor payment behaviour?)

### Gap 3 — Competitive Position Quantification (MEDIUM IMPACT)

**What McKinsey does:** Porter Five Forces is not just described — each force is scored. A structured scoring approach:

| Force | Indicators | Score (1-5) | Weight |
|-------|-----------|-------------|--------|
| Competitive rivalry | CR4, growth rate, fixed costs, switching costs | 3 | 25% |
| Buyer power | Buyer concentration, switching costs, backward integration threat | 2 | 20% |
| Supplier power | Supplier concentration, input availability, forward integration threat | 3 | 20% |
| New entrant threat | Capital requirements, brand loyalty, regulatory barriers | 4 | 20% |
| Substitute threat | Price-performance of substitutes, switching costs, consumer propensity | 2 | 15% |

**Current state:** Five Forces are described with Uganda/EA examples and CR4 thresholds. But no scoring protocol turns this into a quantified "industry attractiveness" assessment.

**Recommendation:** Add a Five Forces Scoring Protocol to `06-competitive-analysis/SKILL.md`:
- Score each force 1-5 (1 = favourable to incumbents, 5 = unfavourable)
- Calculate weighted industry attractiveness score
- Benchmark: >3.5 = unattractive; 2.5-3.5 = moderate; <2.5 = attractive
- Use score to calibrate required competitive advantage (higher attractive score → lower advantage needed)

### Gap 4 — Competitor SWOT Depth (LOW-MEDIUM IMPACT)

**Current state:** Competitor profiles are described structurally (market position, strategy, capabilities, vulnerabilities). This aligns with Porter's 4-component competitor analysis.

**Missing:** A systematic approach to identifying and validating competitor *vulnerabilities* — the places where the new business can attack. Porter's "Good vs. Bad Competitors" analysis touches this but the operational "vulnerability map" is not present.

**Recommendation:** Add to `06-competitive-analysis/SKILL.md` a Competitor Vulnerability Map:
- For each named competitor: list their strategic commitment that *limits* their flexibility
- Example: large competitor committed to premium segment → cannot credibly attack budget segment
- Example: market leader optimised for institutional clients → poor service for micro-enterprises
- Map each vulnerability to a specific "where to play" opportunity

### Gap 5 — Competitive Response Analysis (LOW-MEDIUM IMPACT)

**The McKinsey standard:** Before finalising strategy, analysts war-game how competitors will respond to your market entry. What will they do? Price cut? Product launch? Distribution block? Regulatory complaint?

**Current state:** Porter's Competitive Moves section (`competitive-strategy-porter.md`) covers this conceptually. No operational protocol in the skills.

**Recommendation:** Add a Competitive Response Protocol to `12-risk-analysis/SKILL.md`:
- For each named competitor: state their most likely response to market entry
- Classify response likelihood: Immediate / Within 6 months / Within 1-2 years / Unlikely
- State your defensive response to each competitor reaction
- Include in risk register as "Competitive Response Risk" with probability × impact scoring

---

## 6.3 Competitive Intelligence Sources by Industry (EA)

The following sources exist but are not documented in the suite. Adding them to `competitive-data-gathering.md` would materially improve the quality of competitive analysis sections:

### Uganda / EA Public Competitive Intelligence

| Source | What It Provides | Industries |
|--------|-----------------|-----------|
| **URSB Business Registry** | Company names, directors, registration date, business type | All |
| **KCCA Online Portal** | Kampala business permits by type and area | All Kampala businesses |
| **UMA (Uganda Manufacturers)** | Member directory; occasionally production capacity data | Manufacturing |
| **UEPB (Export Promotion Board)** | Exporter directory; export volumes by product | Exporters |
| **EAC Trade Portal** | Import/export data by HS code; tariff information | Trade |
| **UNBS Certified Products List** | Which companies have UNBS certification; compliance status | Food, manufacturing |
| **NEMA EIA Records** | Environmental permits — indicates project scale and investment | Construction, mining, agro-processing |
| **African Business Magazine** | EA company profiles, revenue estimates, rankings | Larger companies |
| **BuddeComm / GSMA** | Telecom, digital, mobile money market share data | Digital businesses |
| **Jumia / Kilimall price listings** | Real-time price benchmarking for consumer goods | Retail, e-commerce |
| **Farmgain / Apollo Agriculture** | Agri-input prices, farmer data | Agriculture |

---

## 6.4 OSINT Integration (Existing Asset — Underused)

`meta-due-diligence/references/osint-business-intelligence.md` contains a 5-layer OSINT framework specifically designed for competitor and partner intelligence. This is a world-class asset that is not cross-referenced in `06-competitive-analysis/SKILL.md`.

**Current state:** `meta-due-diligence` is positioned as a "DD readiness" skill for the business itself. The OSINT framework is not explicitly positioned as a competitive intelligence tool for use *during plan drafting*.

**Recommendation:** Add a reference from `06-competitive-analysis/SKILL.md` to `meta-due-diligence/references/osint-business-intelligence.md` with the framing: "Use the OSINT framework in meta-due-diligence for systematic competitor intelligence gathering before completing the competitive analysis section."

---

## 6.5 Recommended New Reference File

**`06-competitive-analysis/references/competitive-data-gathering.md`**

Contents:
1. Mystery shopping protocol (food, retail, services, B2B variants)
2. Competitive price survey template
3. Digital intelligence checklist (social media, website, review sites)
4. Uganda/EA public sources for competitor intelligence (URSB, KCCA, UMA, UEPB, NEMA)
5. Five Forces quantification scoring template
6. Competitor Financial Estimation methodology (staff count × productivity benchmarks)
7. Competitor Vulnerability Map template
8. Competitive Response Protocol (war-gaming table)
9. Cross-reference: OSINT framework in meta-due-diligence
