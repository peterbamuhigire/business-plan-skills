# Content Gaps — Insufficient Depth for a Strong Plan

These skills exist but lack the reference material and frameworks needed to generate a genuinely strong, unique, bankable section. A plan generated from these skills today would be generic rather than compelling.

---

## GAP D1: Section 02 (Company Overview) — Empty Skill, No EA Legal Guidance

**Current state:** 44 lines, 0 reference files.

**What the skill generates today:**
A generic mission/vision/values narrative. Good for any country, specific to none.

**What a Ugandan bank actually needs to see in Company Overview:**

### Legal Structure in Uganda (none of this is in the skill)

| Structure | Registration Body | Annual Requirements | Best For |
|---|---|---|---|
| Sole Proprietorship | URSB business name | Business name renewal (UGX 20,000/yr) | Single-person, low-liability |
| Partnership | URSB deed registration | Annual renewal | 2–20 partners |
| Private Limited Company (Ltd) | URSB company registration | Annual return, audited accounts if large | Most SMEs seeking bank loans |
| Public Limited Company (PLC) | URSB + CMA | Annual return, listed financial statements | Large enterprises |
| Cooperative Society | Commissioner for Cooperatives | Annual general meeting, audit | Farmer groups, SACCOs |
| NGO/Foundation | NGO Bureau | Annual report, permit renewal | Social enterprise |

**Critical for lending:** Banks strongly prefer lending to Private Limited Companies over sole traders because:
1. The company is a separate legal entity — personal assets are ring-fenced
2. Financial statements can be audited independently
3. Directors are accountable in a traceable way
4. Succession is clearer — death of owner does not end the company

### Key URSB Documents Required by Banks
- Certificate of Incorporation / Business Name Certificate
- Memorandum and Articles of Association (for companies)
- Directors' and shareholders' register
- Trading licence (from KCCA or district local government)
- TIN certificate (URA tax registration)
- Sector-specific licences (e.g., UNBS product registration, NEMA permit, NDA licence for food)

**What needs to be built:**
- `02-company-overview/references/uganda-legal-structures.md` — all business structures, registration process, costs, and bank preferences
- `02-company-overview/references/compliance-checklist.md` — mandatory registrations, licences, and annual obligations by business type and sector
- The SKILL.md should prompt the plan author to list all licences held and pending

---

## GAP D2: Section 11 (Funding Request) — Wrong Orientation for EA Market

**Current state:** 59 lines, 0 reference files. Written entirely for equity investors.

**Specific problems with the current skill:**

1. **Lists "IPO" as an exit strategy** — irrelevant for 99.9% of Ugandan SMEs
2. **Asks for a "capitalisation table"** — standard for startups, but most Ugandan businesses are sole proprietorships or family companies with no cap table
3. **No mention of loan repayment schedule** — this is the primary output banks want
4. **No mention of collateral** — the central question in every Ugandan bank loan application
5. **No mention of guarantors** — often required for loans above UGX 50M
6. **Valuation methodology** is relevant only for equity; for debt, the bank wants assets, income, and DSCR

**What a bank loan section actually needs:**

```
Loan Application Summary:
  Amount requested: UGX [X]
  Purpose: [Specific productive use — not "working capital" without detail]
  Loan term: [Years]
  Preferred structure: [Term loan / overdraft / asset finance / mortgage]
  Proposed repayment: [Monthly UGX X from [revenue source]]

Security Offered:
  Primary security: [Land title, LRV/Block/Plot details OR equipment value]
  Secondary security: [Motor vehicle, fixed deposit, personal guarantee]
  Estimated security value: UGX [X]
  Security coverage ratio: [X]% of loan amount

Debt Service Capacity:
  Monthly net income from operations: UGX [X]
  Proposed monthly loan repayment: UGX [X]
  DSCR: [X.Xx] (target: ≥1.25)
  Remaining monthly operating surplus: UGX [X]
```

**What needs to be built:**
- Complete rewrite of `11-funding-request/SKILL.md` to be context-aware: ask whether the funding source is a bank loan, DFI facility, grant, or equity — and generate the appropriate format for each
- `11-funding-request/references/ea-funding-landscape.md` (see Gap C3)
- `11-funding-request/references/credit-assessment-frameworks.md` (see Gap C1)
- `11-funding-request/references/loan-application-templates.md` — standard bank loan narrative format used by Ugandan commercial banks

---

## GAP D3: Section 15 (Appendices) — Passive List, No Templates or Guidance

**Current state:** 52 lines, 0 reference files.

**Current skill behaviour:** Generates a list of what to include. Does not generate any of the actual documents.

**What a strong appendices section requires:**

### Documents That Can Be Generated (currently not supported)

1. **CV/Profile template for directors** — banks require a standard format: full name, NIN, TIN, address, qualifications, business history. The current skill says "include CVs" but provides no template.

2. **Financial summary table** — a one-page consolidated view of the 3-year projections matching the detailed financials exactly. Banks often read the appendix first to get numbers.

3. **Loan repayment schedule** — monthly table showing: outstanding principal, interest payment, principal repayment, closing balance. Banks generate this themselves but a plan that includes it shows sophistication.

4. **Net Worth Statement (Personal Statement of Assets and Liabilities)** — required by most Ugandan banks for the directors/guarantors. Format:

```
Personal Net Worth Statement
Name: _____________ NIN: _____________

ASSETS                          UGX
Cash and bank deposits:         ______
Motor vehicles (market value):  ______
Property (current valuation):   ______
Business interests:             ______
Other assets:                   ______
TOTAL ASSETS:                   ______

LIABILITIES
Existing loans:                 ______
Other debts:                    ______
TOTAL LIABILITIES:              ______

NET WORTH:                      ______
Signature: ___________  Date: ________
```

5. **Reference letters format** — for character/CAMPARI assessment, banks require reference letters from professional contacts, community leaders, or existing bankers.

**What needs to be built:**
- `15-appendices/references/document-templates.md` — CV template, net worth statement, loan schedule template, reference letter format
- The skill should actively generate the financial summary table from data in section 10, not just list it as "to be included"

---

## GAP D4: Section 10 (Financial Projections) — Missing Ugandan Cost Benchmarks Integration

**Current state:** 132 lines, 4 refs. Reasonable skill but with gaps.

**What is missing:**

### 1. Integration with Industry Guides
The suite has 13 industry guides with detailed cost benchmarks, startup costs, and revenue models. **Section 10's SKILL.md never references them.** When generating financial projections for a restaurant, the skill does not say "read `industry-guides/restaurant/references/`". This means:
- Cost benchmarks are in the guides but projections ignore them
- The financial model and the industry guide generate inconsistent numbers
- A restaurant plan could show a 40% food cost while the Schmidgall reference benchmarks say 28–32%

**Fix:** Add a cross-reference table in the financial projections skill: "If generating projections for [industry], read [industry guide references] for cost benchmarks before generating numbers."

### 2. No Breakeven Analysis Template
The skill mentions break-even but provides no standard template. A break-even analysis for bank submission requires:
```
Fixed Costs per Month: UGX [total]
Variable Cost per Unit: UGX [X]
Selling Price per Unit: UGX [X]
Contribution Margin per Unit: UGX [X - variable cost]
Break-even Volume: Fixed Costs / Contribution Margin
Break-even Revenue: Break-even Volume × Selling Price
Break-even Month: [Month when cumulative revenue exceeds cumulative costs]
```

### 3. No Sensitivity Analysis Template
Banks want to see scenarios. The skill mentions stress-testing but `meta-financial-stress-test/SKILL.md` (94 lines, 0 refs) is disconnected from the projections skill. No shared template ties them together.

---

## GAP D5: Section 08 (Operations) — Thin Industry Integration

**Current state:** 105 lines, 1 reference file (`operations-frameworks.md`).

**What is missing:**
The operations skill covers BPM, process design, and capacity planning well (thanks to the BPM batch). But it is generic and does not connect to:

1. **Supply chain specifics for Uganda** — no mention of supplier verification (UNBS certified suppliers), local procurement challenges, import procedures, bonded warehousing
2. **Utility infrastructure realities** — power outages requiring UPS/generator, water supply unreliability in peri-urban areas, internet connectivity constraints (important for digital businesses)
3. **Labour law basics** — Employment Act 2006, minimum wage, working hours, probation periods (applicable to the staffing section of operations)
4. **Quality standards** — UNBS certification requirements by product category, NEMA environmental compliance, NAADS/MAAIF requirements for agriculture

---

## GAP D6: Meta-Bankability-Scoring — No Formal Lender Criteria Mapped

**Current state:** 120 lines, 0 reference files.

**What is missing:**
The bankability scoring skill should be the capstone that tells a plan author: "here is how a lender would rate your plan." But the scoring dimensions are internally derived rather than mapped to formal lender criteria.

**What it should score against:**
1. **Does the DSCR exceed 1.25x?** (bank minimum)
2. **Is collateral ≥125% of loan value?** (standard bank requirement)
3. **Does the management team have sector experience?** (CAMPARI Ability)
4. **Are financial statements prepared by a qualified accountant?** (credibility marker)
5. **Is the business registered with URSB, TIN held, trading licence current?**
6. **Has the market been validated with named customers or LOIs?**
7. **Is the ESMP included if applying to a DFI?**

The current skill scores innovation, traction, and market size — useful for investor pitches, not bank applications.

**What needs to be built:**
- Two scoring modes: "Bank Loan Readiness" and "Investor Readiness" — with different criteria
- Bank readiness mapped explicitly to 5 Cs / CAMPARI
- At minimum, a reference file linking scoring to formal credit criteria

---

## GAP D7: Section 09 (Management Team) — No EA-Specific Governance Standards

**Current state:** 104 lines, 8 reference files. Strongest of the mid-tier skills.

**What is missing:**
The skill has excellent leadership theory (Collins, Tuckman, Dennis) but lacks:
1. **Board governance standards** for EA companies applying for DFI funding — UDB and impact investors require a functioning board with independent directors for loans above UGX 500M
2. **Director signing authority** — for loans, banks require board resolutions authorising specific directors to borrow; the plan should show governance is in place
3. **Professional qualifications** — for credentialed industries (finance, medicine, engineering, law), list the relevant professional body membership (ICPAU for accountants, MUK/MUST for engineers, ULS for lawyers)

---

## GAP D8: Section 12 (Risk Analysis) — No Insurance Framework

**Current state:** 110 lines, 7 reference files. Good analytical depth.

**What is missing:**
Risks are identified and analysed but the mitigation section does not connect to the Ugandan insurance market. Banks require proof of insurance on collateral assets. The plan should include:

1. **Fire and allied perils** — mandatory on any property or equipment offered as collateral
2. **Motor vehicle comprehensive** — required on any vehicle in the loan
3. **Public liability** — for hospitality, construction, events
4. **Business interruption** — rarely mandated but strengthens the plan
5. **Life assurance on key person** — some banks require life cover on the borrowing director equal to the loan amount

**Ugandan insurers:** UAP, Jubilee, AIG, Liberty, CIC, ICEA Lion — should be referenced as the local providers.

---

## GAP D9: Industry Guides — Not Integrated with Core Skills

**Current state:** 13 industry guides exist with detailed content. None of the core skill SKILL.md files reference them.

**The problem:**
A user generating a business plan for a restaurant follows the core skills (01–15). The `restaurant/` industry guide exists with 10 detailed reference files covering financial benchmarks, food cost controls, hygiene standards, and staffing ratios. But nothing in the workflow tells the core skills to use that industry guide data.

**Specific integration failures:**
- `04-market-analysis` should say: "If industry = restaurant, read `industry-guides/restaurant/guide.md` for market context"
- `10-financial-projections` should say: "If industry = agriculture, read `industry-guides/agriculture/references/` for cost benchmarks"
- `08-operations-plan` should say: "For manufacturing businesses, read `industry-guides/manufacturing-light/guide.md` for operations benchmarks"
- `09-management-team` should say: "For agribusiness, the management team should include MAAIF-certified agronomists or equivalent"

**What needs to be built:**
A cross-reference matrix in each core skill pointing to relevant industry guides by sector. This is a documentation fix, not new content creation — the content already exists.
