# Structural Gaps — Missing Cross-Cutting Capabilities

These are gaps that span multiple skills or affect the plan as a whole. They cannot be fixed by improving one skill — they require new cross-cutting content or new skills.

---

## GAP S1: No Plan Assembly and Submission Guide

**What is missing:**
The suite has 15 section skills plus meta-skills for validation and stress testing. But there is no skill that guides the assembly of a complete, submission-ready business plan document. A plan author who has generated all 15 sections does not know:

1. **Correct binding order** for different funders (banks often want executive summary last, not first)
2. **Cover page requirements** — bank name, loan amount, applicant name, TIN, contact details
3. **Table of contents generation** with page numbers
4. **Covering letter format** — a formal letter from the business owner to the bank/investor is required by most Ugandan lenders; the plan without this letter goes into the wrong pile
5. **Required attachments checklist** — what physical documents must accompany the plan (certified copies of IDs, land title, tax compliance certificate, bank statements)
6. **Format specifications** — some banks require A4 single-sided, others accept digital PDF; font size and margin standards that signal professionalism

**Covering Letter Template (completely absent):**
```
[Letterhead with business name and address]
[Date]

The Branch Manager / Credit Manager
[Bank Name]
[Branch Address]

Dear Sir/Madam,

RE: APPLICATION FOR [LOAN AMOUNT] TERM LOAN / OVERDRAFT FACILITY

We write to formally apply for a [type] facility of UGX [amount] to [purpose].
[2–3 sentences about the business and why this loan makes sense]

Enclosed herewith please find our business plan and supporting documents as listed below:
1. Business plan
2. [List all documents]

We confirm that all information provided is accurate and complete to the best of our knowledge.

Yours faithfully,
[Director Name]
[Title]
[NIN]
[Signature]
[Company Seal if applicable]
```

**Recommendation:** Create a new skill `00-plan-assembly/` or add a section to `15-appendices/SKILL.md` covering document assembly, covering letter, required attachments, and submission format by funder type.

---

## GAP S2: No Cross-Section Consistency Checker

**What is missing:**
When a 15-section plan is generated, numbers and claims must be consistent across sections. Currently there is no mechanism to check this. Common inconsistencies that cause rejection:

| Inconsistency Type | Example | Where It Breaks |
|---|---|---|
| Revenue mismatch | Market analysis says market is UGX 50M; projections show UGX 80M revenue | §04 vs §10 |
| Team vs. operations mismatch | Operations says 20 staff; management section lists 3 people | §08 vs §09 |
| Funding vs. use of funds mismatch | §11 says UGX 200M needed; implementation budget in §13 totals UGX 150M | §11 vs §13 |
| Product vs. marketing mismatch | Products listed at UGX 15,000; marketing section uses UGX 10,000 | §03 vs §07 |
| Risk vs. contingency mismatch | Risk section identifies cash flow risk; financial projections show no cash buffer | §12 vs §10 |
| DSCR vs. loan size mismatch | Projections show EBITDA of UGX 5M/month; funding request asks for loan with UGX 6M/month repayment | §10 vs §11 |

**`meta-bankability-scoring/SKILL.md`** partially addresses this but in a scoring context, not a correction context. A dedicated consistency checker would systematically compare numbers across sections.

**Recommendation:** Extend `meta-bankability-scoring/SKILL.md` with a consistency audit step, or create a new meta-skill `meta-plan-consistency/` that extracts key figures from each section and cross-checks them.

---

## GAP S3: No Grant Proposal Framework

**What is missing:**
Grant funding from development partners (USAID, EU, GIZ, UN Women, NARO, MTIC) is a significant funding route for Ugandan businesses, especially those in agriculture, education, health, and clean energy. Grant applications have a completely different format from bank loans or equity pitches:

| Grant Requirement | Difference from Business Plan |
|---|---|
| **Theory of Change** | Required — must show causal chain from inputs to impact |
| **Logical Framework (LogFrame)** | Standard output/outcome/impact matrix |
| **Beneficiary analysis** | Number of direct and indirect beneficiaries, disaggregated by gender |
| **Budget narrative** | Line-by-line justification of every expense |
| **Sustainability plan** | How the project continues after grant funding ends |
| **M&E framework** | SMART indicators for each objective (covered in meta-monitoring-evaluation but not linked) |
| **Procurement plan** | How inputs/services will be procured (competitive tender for most grants) |
| **Risk register** | Separate from the business risk analysis; focuses on programme delivery risks |

**Currently:** `meta-monitoring-evaluation/SKILL.md` has a good M&E framework but no grant-specific adaptations. `11-funding-request/SKILL.md` does not address grant funding at all.

**Recommendation:** Either extend `11-funding-request/` with a grant funding section, or create `11b-grant-proposal/` as a standalone skill covering LogFrame, Theory of Change, and budget narrative.

---

## GAP S4: No IP and Trademark Guidance

**What is missing:**
`03-products-services/SKILL.md` lists intellectual property as a required element but provides no guidance on how to protect IP in Uganda. This matters for any business with a brand, recipe, software, or invention.

**Uganda IP landscape:**
- **Uganda Registration Services Bureau (URSB)** handles trademarks, patents, and copyrights
- **Trademark registration:** ~UGX 200,000–500,000 fee; 10-year protection; national search required first
- **ARIPO membership:** Uganda is a member of the African Regional Intellectual Property Organisation — one application covers 19 African countries
- **Copyright:** Automatic on creation; no registration needed but can be registered with URSB for evidentiary purposes
- **Patent:** Must be novel, inventive, and industrially applicable; expensive (>UGX 1M + agent fees)
- **Trade secrets:** Protected through confidentiality agreements, not registration

**For a business plan:** The IP section should tell the bank/investor whether the business's core asset is legally protected. A recipe business with no trademark on its brand name is a vulnerability. A software business with no copyright registration of its codebase is a risk.

---

## GAP S5: No Meta-Financial-Stress-Test Reference Content

**Current state:** 94 lines, 0 reference files.

**What is missing:**
The stress-test skill exists and has reasonable methodology but no reference material backing it. A stress test that changes revenue by -20% without justifying why -20% is the right shock is not credible. A bankable stress test needs:

1. **Historical shock magnitudes** — what actually happened to Ugandan businesses during COVID-19 (2020), the exchange rate crisis (2021–22), fuel price shock (2022), and the 2023 LGBTQ law economic fallout
2. **Sector-specific shock factors** — agriculture: rainfall failure probability (ENSO cycles); hospitality: tourist arrivals volatility; construction: cement price volatility; retail: disposable income sensitivity
3. **Formal scenario framework** — base, optimistic, pessimistic, and extreme (tail risk) scenarios with explicit assumptions for each
4. **Monte Carlo reference** — probabilistic analysis for complex businesses
5. **Breakeven sensitivity table** — showing how many units below plan the business can sell before going cash-flow negative

**Recommendation:** Create `meta-financial-stress-test/references/stress-test-methodology.md` with historical shock data, sector-specific factors, and scenario construction methodology.

---

## GAP S6: No Plan for Businesses Without Formal Records

**What is missing:**
Many Ugandan businesses applying for loans have 2–3 years of operation but no formal financial records. They have bank statements, M-Pesa/Mobile Money transaction records, and receipts — but no audited accounts. The suite assumes formal records exist.

**What is needed:**
- Guidance on reconstructing financial history from bank statements and mobile money records
- Cashflow-based lending narrative — how to make the case when formal accounts don't exist
- Reference to the Bank of Uganda Financial Sector Development Plan provisions for cash-flow based lending
- SACCO and microfinance pathways for businesses without collateral or records

---

## GAP S7: No Ugandan Regulatory Compliance Roadmap

**What is missing:**
Different businesses in Uganda need different licences and permits. The suite has no cross-sector compliance guide. When a plan is generated for a food processing business, the plan should automatically include:

- UNBS product registration (mandatory for packaged food)
- NEMA environmental permit (if there's effluent/waste)
- NDA (National Drug Authority) — if any health claims on labels
- Uganda Tourism Board (UTB) — for hospitality businesses
- NEMA EIA (Environmental Impact Assessment) — for construction or large manufacturing
- Financial licences (Bank of Uganda, UMRA) — for lending/microfinance businesses
- Petroleum licences — for fuel stations
- Mining licences (DGSM) — for extractives

**Recommendation:** Add a sector-specific compliance matrix to `02-company-overview/references/` — a lookup table: "if your business is [sector], you need [licence list] from [authority]."

---

## GAP S8: Meta-Monitoring-Evaluation Disconnected from Funding Requirements

**Current state:** 146 lines, 0 reference files.

**The disconnection:**
The M&E skill is well-structured around King's game plan methodology and Page's continuous improvement cycle. But it does not connect to:

1. **Loan covenant monitoring** — banks attach performance covenants to loans (e.g., "maintain DSCR > 1.2x"; "provide quarterly management accounts"). The M&E framework should include covenant reporting as a monitoring obligation.
2. **Grant reporting requirements** — development partner grants require quarterly narrative reports + financial reports against budget. The meta-M&E skill does not address this format.
3. **Impact investor reporting** — Acumen, Pearl Capital, and others require impact metrics (jobs created, women employed, smallholders reached) in addition to financial metrics.

**Recommendation:** Add a "reporting obligations by funder type" section to the M&E skill, linking back to the funding landscape reference (Gap C3).
