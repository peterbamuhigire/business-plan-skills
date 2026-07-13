---
name: meta-due-diligence
description: Use when running commercial, operational, legal, or financial due diligence; preparing an evidence room; or reporting red flags and evidence gaps. Use the relevant plan-section skill for section drafting.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Due Diligence Meta-Skill

## Use When

- Use before presenting a plan to investors, lenders, DFIs, or strategic partners.
- Use when auditing whether claims, numbers, and credentials can survive scrutiny.
- Use for outbound diligence on counterparties where the business itself must verify another party.

## Do Not Use When

- Do not use as a substitute for basic drafting or market research.
- Do not assume DD is complete because the plan sounds polished.
- Do not certify claims that have not been checked against documents or verifiable evidence.


- For `meta-due-diligence`, route to the relevant plan-section skill instead when the request is section drafting rather than cross-section analysis.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Due Diligence brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Completed or near-complete plan sections
- All available supporting documents and source files
- Audience type and DD intensity expected
- Any known risk areas, unsupported claims, or counterparties requiring review

## Workflow

1. Choose the DD mode: inbound readiness, outbound DD, or plan DD audit.
2. Identify the claims and evidence that matter most to the transaction or submission.
3. Check supportability section by section and document by document.
4. Classify issues by severity, missing evidence, and likely investor or lender reaction.
5. Build the DD action list or counterparty findings pack.
6. Hand unresolved items back to the relevant skills for correction.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the due-diligence findings register and that the decision concerns which red flags block, condition, or permit the transaction.
- **Stop condition:** halt the affected conclusion if required evidence is missing (data room, scope, source provenance, and materiality threshold) or if the work could lead to this identified risk: treating a missing document as satisfactory evidence.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Every major claim is either verified, caveated, or flagged.
- The DD output distinguishes missing proof from genuine red flags.
- The result is practical for submission readiness, not just theoretical.
- The work improves survival under real scrutiny.

## Anti-Patterns

- Assuming data quality because the narrative sounds confident.
- Leaving unsupported claims in place because they are strategically useful.
- Mixing minor admin gaps with deal-breaking issues.
- Treating DD as formatting rather than verification.
- Treating a generic due diligence template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to meta due diligence. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Due Diligence deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- DD readiness assessment or counterparty DD findings
- Verified and unsupported claim list
- Severity-ranked issue log
- Recommended remediation actions before submission or deal progression


## Core Principle

A business plan is a collection of claims. Due diligence is the process of verifying whether those claims are true. Every number, every market assertion, every competitive advantage statement, and every management credential in a business plan is a potential DD investigation target.

**Two directions of DD in business planning:**
- **Inbound DD**  What investors, banks, and DFIs will do to you. Prepare for it.
- **Outbound DD**  What you must do on partners, suppliers, customers, and acquisition targets before committing.

A plan that has been through rigorous internal DD before submission is a fundamentally different document from one that hasn't.

---

## When to Use

**Mode A  DD Readiness Preparation:** Before submitting a business plan to any investor, bank, DFI, or grant committee. Use to identify what documentation is missing, what claims are unsupported, and what red flags must be addressed.

**Mode B  Outbound Due Diligence:** Before entering a material business relationship  a major supplier contract, joint venture, partnership, acquisition, or key hire. Use the OSINT and DD frameworks to systematically investigate the counterparty.

**Mode C  Business Plan DD Audit:** Review a completed business plan section-by-section for claim supportability, documentation gaps, and investment-readiness. Produces a scored DD audit with priority action list.

---

## Mode A: DD Readiness  Prepare for Investor Scrutiny

### The Investor's Investigation Map

When a professional investor, bank credit officer, or DFI analyst receives a business plan, their DD process follows a predictable sequence. Knowing what they investigate lets you prepare before they ask.

#### 1. Commercial Due Diligence

**What they verify:**
- Market size: Is the TAM/SAM/SOM calculation methodology credible? Are the data sources reputable and current?
- Growth claims: Is the cited CAGR from a verifiable source? Does historical data support the forward projections?
- Customer claims: Do named customers exist? Are contracts signed or verbal? What is the concentration  does one customer represent >20% of revenue?
- Competitive position: Is the stated competitive advantage real and durable, or asserted without evidence?
- Revenue quality: Is revenue recurring/contracted, or one-off? Is the pipeline real?

**Preparation actions:**
- [ ] All market size figures cite named sources with date and URL
- [ ] Customer list prepared with: name, contract status, revenue contribution, tenure
- [ ] No single customer >30% of revenue (or concentration risk explicitly addressed)
- [ ] Competitive advantages supported by evidence (patents, certifications, price comparisons, win/loss data)
- [ ] Sales pipeline documented with stage, value, probability, and contact name

#### 2. Financial Due Diligence

**What they verify:**
- Financial statements: Are the last 2-3 years of financials available and internally consistent?
- Quality of earnings (QoE): Have one-off items been excluded from normalised EBITDA?
- Working capital: What is the normal working capital requirement? Is it stable or deteriorating?
- Cash flow: Does cash flow match reported profit? Large divergences indicate accounting issues.
- Tax compliance: Are all tax returns filed and paid? Are there outstanding assessments?
- Revenue recognition: Is revenue booked when earned or when received? Are policies consistent?

**Preparation actions:**
- [ ] 3 years of audited or reviewed financial statements prepared (or management accounts if pre-audit stage)
- [ ] Normalised EBITDA calculated with adjustments listed and explained
- [ ] Tax compliance certificates (TCC) obtained from URA (or relevant authority)
- [ ] Working capital analysis prepared: debtors, creditors, inventory, cash cycle
- [ ] Any related-party transactions disclosed and at arms-length pricing
- [ ] Financial projections include a detailed assumptions page (not just numbers)

#### 3. Legal and Compliance Due Diligence

**What they verify:**
- Business registration: Is the entity properly registered and in good standing?
- Licences and permits: Are all operating licences current and applicable?
- Contracts: Are key commercial contracts in writing, signed, and favourable?
- IP: Is intellectual property owned by the business (not the founder personally)?
- Litigation: Are there pending or threatened legal claims?
- Land/property: If land is an asset or is used operationally, is title clear and registered?

**Preparation actions:**
- [ ] Certificate of Incorporation / Business Registration Certificate available
- [ ] All trading licences current (KCCA/district, sector-specific)
- [ ] Key supplier and customer contracts in writing with signed copies
- [ ] IP transferred to company name (not founder)  trademarks, software, brand assets
- [ ] Statutory compliance: NSSF, PAYE remittances up to date
- [ ] Land titles or lease agreements in order  no encumbrances undisclosed

#### 4. Operational Due Diligence

**What they verify:**
- Processes: Are core business processes documented or entirely in the founder's head?
- Systems: What accounting, ERP, or management information systems are in use?
- Key person dependency: Would the business survive if the founder was unavailable for 3 months?
- Scalability: Can operations scale to meet the projected growth in the plan?
- Supply chain: How many suppliers for critical inputs? What is the switching cost?

**Preparation actions:**
- [ ] SOPs (Standard Operating Procedures) exist for core processes
- [ ] Accounting software in use  not Excel spreadsheets for a going-concern business
- [ ] Succession plan or key person mitigation addressed in management section
- [ ] Capacity analysis in operations plan: current capacity vs. projected demand
- [ ] Supply chain risk addressed  minimum two suppliers for any critical input

#### 5. Management and People Due Diligence

**What they verify:**
- Founder background: Are the credentials stated in the plan accurate and verifiable?
- Track record: Do prior business successes check out?
- References: What do former employers, clients, and associates say?
- Character: Any adverse history  fraud, criminal records, regulatory sanctions?
- Team completeness: Are the skill gaps in the leadership team addressed?

**Preparation actions:**
- [ ] All CVs in the plan are accurate (dates, qualifications, titles)
- [ ] Professional references prepared  2-3 people who can vouch for each key executive
- [ ] Academic and professional certificates available for inspection
- [ ] No undisclosed conflicts of interest (related-party suppliers, family members in key roles undisclosed)

### The Data Room

For any equity investment or major DFI financing, build a data room  an organised, secure, digital folder of all DD materials.

**Minimum data room structure:**

~~~text
/data-room/
 1-corporate/
    certificate-of-incorporation.pdf
    memorandum-and-articles.pdf
    shareholders-register.pdf
    board-resolutions.pdf
 2-financial/
    financial-statements-FY2023.pdf
    financial-statements-FY2024.pdf
    management-accounts-current-year.pdf
    tax-compliance-certificate.pdf
    projections-with-assumptions.xlsx
 3-commercial/
    customer-list-and-contracts.pdf
    supplier-agreements.pdf
    sales-pipeline.xlsx
    market-research-sources.pdf
 4-legal/
    operating-licences.pdf
    land-title-or-lease.pdf
    ip-registrations.pdf
    litigation-disclosure.pdf
 5-operations/
    org-chart.pdf
    key-process-sops.pdf
    asset-register.pdf
 6-people/
     management-cvs.pdf
     key-employment-contracts.pdf
~~~

---

## Mode B: Outbound Due Diligence (Investigating Others)

### When Outbound DD is Required

Before any material business commitment:
- Major supplier or subcontractor (>20% of COGS from one source)
- Joint venture or partnership
- Key hire (C-suite, technical lead, financial controller)
- Business acquisition or asset purchase
- Major customer (extending credit or entering long-term contract)
- Investor or lender (reverse DD  vetting who your capital partners are)

### OSINT Investigation Framework (Hetherington)

Open-source intelligence (OSINT) is the systematic collection and analysis of publicly available information. For business due diligence, it is the first layer of investigation  fast, low-cost, and often revealing.

**Layer 1  Identity and Registration Verification**
- Business registration: confirm legal name, registration number, incorporation date, directors/shareholders  use URSB (Uganda Registration Services Bureau) portal or equivalent national registry
- Verify that the business is in good standing (not struck off, not under administration)
- Cross-check trading name against registered name  discrepancies are a red flag

**Layer 2  Financial and Credit Signals**
- Credit bureau checks (Uganda: CRB Africa, Compuscan)  payment history, defaults, judgements
- Court records: civil judgements, winding-up petitions, bankruptcy records
- Regulatory enforcement actions: check sector regulator databases (Bank of Uganda, URA, NEMA)
- Annual returns: filed on time? Financials filed? Gaps in filing history are signals

**Layer 3  Digital Footprint Assessment**
- Website: domain registration date, hosting country, HTTPS, contact details verifiable?
- Social media: account age, follower quality, engagement consistency  new accounts with no history are high-risk for new suppliers
- Adverse media search: [company name] + fraud, scam, dispute, lawsuit, complaint  across Google, local news, social media
- LinkedIn: do stated employees actually exist and have credible histories?
- Google Maps / satellite: does the stated physical address match a real business location?

**Layer 4  People Verification (Key Principals)**
- Director background: search [name] + company names + past roles
- Professional credentials: verify via licensing boards, professional associations (e.g., ICPAU for accountants, LSB for lawyers in Uganda)
- Sanctions and PEP screening: check UN Sanctions List, OFAC SDN list, EU Consolidated List
- Court records: civil and criminal history where public records permit

**Layer 5  Reputation Intelligence**
- Industry references: ask peers in your industry about their experience with this counterparty
- Customer references: request and actually call 2-3 customer references; ask hard questions
- Supplier references: ask the target's own suppliers about payment behaviour
- Association and chamber of commerce membership: members face peer accountability

### Outbound DD Red Flag Register

| Signal | Risk Level | Action |
|---|---|---|
| Business registered < 12 months ago for contract >UGX 50M | High | Require parent guarantee or advance payment |
| Directors not findable on any digital platform | High | In-person verification; request ID |
| Adverse media: fraud, dispute, non-payment | Critical | Do not proceed without full explanation and evidence |
| Registered address is a PO box or residential | Medium | Verify actual operating premises in person |
| Refuses to provide bank account name to match business name | Critical | Walk away |
| Financial projections provided but no historical financials | High | Require minimum 2 years historical before proceeding |
| Key credential claimed but unverifiable | High | Require certified copies |
| Payment history: 3+ late payments on credit bureau | High | Require advance payment or guarantee |
| Annual returns not filed for 2+ years | Medium | Regulatory non-compliance; request explanation |
| Social media presence inconsistent with claimed scale | Medium | Verify in person |

---

## Mode C: Business Plan DD Audit

Use this section after all plan sections (0115) are drafted, before submission to any funder.

### Audit by Plan Section

For each section, the audit asks: **Is every material claim in this section verified, sourced, and defensible?**

| Plan Section | Key Claims to Verify | Evidence Required | Common DD Finding |
|---|---|---|---|
| **01 Executive Summary** | All headline numbers accurate; funding ask consistent with plan | Consistency with sections 10-11 | Numbers in summary don't match financial projections |
| **02 Company Overview** | Registration, legal structure, ownership | Certificate of Incorporation; shareholding register | Business not properly registered |
| **03 Products/Services** | IP claims; pricing based on real costs | Cost build-up; IP certificates if claimed | No cost data behind pricing |
| **04 Market Analysis** | TAM/SAM/SOM; growth rates; data sources | Named sources; bottom-up calculation | Market size top-down only; outdated sources |
| **05 Target Market** | Customer segment defined; sizing credible | Primary research evidence; customer interviews | Segments overlap (not MECE); no primary research |
| **06 Competitive Analysis** | Competitors correctly identified; advantages real | Competitor product data; price comparisons | Advantages asserted, not evidenced; key competitors omitted |
| **07 Marketing & Sales** | CAC estimate; channel effectiveness claims | Pilot data or comparable benchmarks | CAC assumed, never tested |
| **08 Operations** | Capacity matches projections; suppliers identified | Supplier quotes; site visit; permits | No identified suppliers; no permits in place |
| **09 Management Team** | Credentials accurate; team has required skills | CVs; certificates; references | Inflated credentials; critical skill gaps unaddressed |
| **10 Financial Projections** | Revenue assumptions grounded; costs complete | Assumption page; benchmark comparisons | No assumptions page; costs understated |
| **11 Funding Request** | Loan amount = sum of line items; DSCR  1.25 | Use-of-funds table; DSCR calculation | Funding gap unaddressed; collateral unverified |
| **12 Risk Analysis** | Risks are real, not cosmetic; mitigations are actionable | Risk register with owners and dates | Risks generic; no mitigations with owners |
| **13 Implementation** | Timeline is realistic; milestones are measurable | Dependency map; regulatory lead times included | Timeline ignores regulatory delays; no dependencies |
| **14 AI Integration** | AI claims are real tools, not buzzwords | Tool names; cost; use case specifics | AI section is aspirational, not operational |
| **15 Appendices** | All supporting documents present | Data room cross-reference | Missing: TCC, certificates, audited accounts |

### DD Readiness Score

After auditing each section:

| Score | Meaning |
|---|---|
| 5  Fully documented | Every claim has cited evidence; documents are available |
| 4  Substantially supported | Key claims cited; minor gaps addressable before submission |
| 3  Partially supported | Some claims verified; material gaps require work |
| 2  Mostly asserted | Claims present but most unsupported; requires significant work |
| 1  Not DD-ready | No supporting evidence; plan will not survive basic investor scrutiny |

**Minimum for bank submission:** Average score  3.5, no section below 3.
**Minimum for DFI / equity:** Average score  4.0, no section below 3.5.

---

## Execution Readiness Dimension

Due diligence also tests whether a plan can actually be executed. A well-written plan that the management team cannot execute is worthless  investors call this the "implementation gap."

### Execution Readiness Checklist

- [ ] Every milestone in Section 13 has a named responsible person, not just "management"
- [ ] Pre-launch regulatory steps (licences, permits, registrations) are in the timeline with realistic lead times
- [ ] Every financial assumption in Section 10 can be traced to a specific action in Section 13
- [ ] The team in Section 09 has the skills to execute every phase of the Section 13 plan
- [ ] Cash flow projections account for the time lag between investment, operations launch, and revenue generation
- [ ] Section 12 risk mitigations are built into the Section 13 timeline, not left as promises
- [ ] Key supplier relationships have been initiated (quotes obtained, samples tested, agreements in principle)
- [ ] The operations plan (Section 08) is consistent with the budget  space, equipment, staffing match the numbers
- [ ] Board governance or advisory structure is in place to hold management accountable post-funding

---

## Generation Process

1. Identify the mode (A, B, or C) and the purpose (what funder? what counterparty?)
2. **Mode A:** Work through the 5 DD categories; produce a gaps list with priority actions and data room requirements
3. **Mode B:** Apply the 5-layer OSINT framework; produce a red flag report with recommendations
4. **Mode C:** Audit each of the 15 plan sections against the verification table; produce a DD Readiness Score with a priority action list
5. In all modes, check execution readiness using the checklist above

## Quality Criteria

- Every material claim in the plan has an identified evidence source
- Data room structure is complete (Mode A) or red flags are documented (Mode B)
- DD Readiness Score  3.5 (bank) or  4.0 (equity/DFI) before submission
- Execution readiness checklist passes  plan is executable, not just presentable
- No section of the plan makes claims that contradict evidence elsewhere in the plan

## References

- `references/osint-business-intelligence.md`  OSINT methodology; 5-layer investigation framework; competitor intelligence checklist; digital footprint assessment; red flag signals; Uganda/East Africa limitations with workarounds  Source: Hetherington. **Read for any outbound DD investigation, competitor research, or partner vetting.**
- `references/due-diligence-ma-howson.md`  Full DD taxonomy (commercial, financial, legal, operational, tax, HR); quality of earnings; working capital analysis; data room requirements; management presentation standards; sell-side VDD; full DD checklists by type; investment readiness framework  Source: Howson. **Read for any equity investment, DFI funding, or business sale preparation.**
- `references/operational-due-diligence-pe.md`  Operational DD standards for PE/impact investors; valuation scrutiny and defence; liquidity analysis; financial controls adequacy; documentation standards; governance requirements; PE-ready operations standard  Source: Scharfman. **Read when preparing for PE, impact investor, or DFI operational due diligence.**
- `references/due-diligence-transactions-berkman.md`  Transaction DD checklists (financial, legal, commercial, people); pre-transaction preparation timeline; business plan verification table (claims to evidence map); execution readiness framework; 20 common DD deal-breakers  Source: Berkman. **Read for any business transaction requiring DD  investment, acquisition, partnership, or major contract.**
- `meta-bankability-scoring/SKILL.md`  CAMPARI 28-item checklist. Run alongside Mode A (DD Readiness) for bank submissions.
- `meta-market-validation/SKILL.md`  Mode B (Post-Plan Claim Auditing) complements Mode C of this skill. Run both for comprehensive pre-submission review.
- `11-funding-request/references/business-valuation-methods.md`  Valuation methodology defence (cross-reference with Scharfman's valuation scrutiny section).
- `12-risk-analysis/SKILL.md`  Risk register. Every DD finding that cannot be resolved before submission must appear in the risk register with a mitigation.
- `references/esmp-template.md`  Environmental and Social Management Plan (ESMP) template and reference guide for DFI-funded projects. Contains: full 14-section document structure; AfDB 14 Material Actions with KPIs and deadlines; impact/mitigation matrix template; representative mitigation measures by impact type (dust, noise, waste, OHS, community safety, asbestos); environmental monitoring plan; 5-step GRM procedure with SEAH protocols; stakeholder engagement timeline; ESMP budget structure; Uganda NEMA/KCCA/DOSH regulatory requirements; 20-term glossary. Sources: AfDB, FAO/WB, UNDP, World Bank (2025). **Read when any section of the plan involves construction, land use, natural resources, or DFI/development bank financing  any funder following AfDB OS or IFC Performance Standards will require an ESMP.**

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Due-diligence findings register decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to treating a missing document as satisfactory evidence. |

## Capability and Permission Boundaries


Default to read-only inspection while producing the due-diligence findings register. Read supplied records and run non-mutating checks; writing findings only; remediation needs separate authority is permitted only when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If data room, scope, source provenance, and materiality threshold cannot be obtained, return a qualified due-diligence findings register covering only the checks that remain supportable. Leave this decision unresolved: which red flags block, condition, or permit the transaction. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which red flags block, condition, or permit the transaction | Record the conclusion, source trail, owner, and review trigger in the due-diligence findings register. | Risk of treating a missing document as satisfactory evidence |
| Material evidence conflicts or remains uncertain | Test the red flag against an independent source or primary record and keep it open, with materiality stated, until the contradiction is resolved. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: data room, scope, source provenance, and materiality threshold | Mark the decision on which red flags block, condition, or permit the transaction `not assessed` in the due-diligence findings register, and send it to the diligence lead and transaction sponsor. | Otherwise, the work risks treating a missing document as satisfactory evidence |

## Quality Standards


Accept the due-diligence findings register only when evidence is sufficient for this decision: which red flags block, condition, or permit the transaction. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of treating a missing document as satisfactory evidence.

## Worked Example


A target reports a major customer as recurring revenue but supplies only unsigned purchase orders. Flag revenue quality, quantify materiality, and keep the finding open until contracts, invoices, and collections reconcile.

<!-- dual-compat-end -->
