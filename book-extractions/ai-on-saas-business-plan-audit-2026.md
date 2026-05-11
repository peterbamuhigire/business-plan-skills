# AI-on-SaaS Business-Plan Skills Audit — 2026

**Purpose:** Hardening report for the business-plan-skills engine to make it world-class at producing **bankable, investor-grade business plans for AI-feature-led SaaS / ICT companies** — startups whose product *is* AI-enabled, or whose roadmap requires AI as a load-bearing capability rather than a "we use ChatGPT internally" footnote.

**Scope:** This audit sits on top of (and assumes) the prior `saas-ict-business-plan-skills-audit-2026.md` work. That audit specified SaaS unit economics, pricing, cohort discipline, GTM motion, customer success, bankability, valuation, and living-plan governance. **This audit adds the AI layer across every section** — AI cost-of-tenant, AI pricing, AI moats, AI risk, AI valuation premium/discount, AI bankability, AI investor reporting, AI exit strategy, AI talent, AI regulation, and the Africa-AI context (compute scarcity, GPU access, sovereign AI demand, local-language data advantage).

**Method:** Walked the full skill catalogue (00→16, all `meta-*`, all SaaS skills produced in the prior session) and tested it against four 2026-realistic AI-SaaS plan archetypes:
1. AI-native vertical SaaS (e.g. AI-first agritech, AI-first healthtech, AI-first legaltech)
2. SaaS-with-AI-features (existing product retrofitted with AI assistants, summarisation, classification)
3. AI-platform / AI-as-infrastructure (model-routing, RAG-platform, eval-platform)
4. AI-services-with-productisation roadmap (AI consultancy productising specific workflows)

For each archetype: which sections of the plan are AI-specific, which existing skills cover them, and where the gaps are. The catalogue covers SaaS operating discipline at world-class depth and has begun the AI-as-feature layer (`saas-ai-feature-roadmap-in-business-plan.md`) but does not yet treat AI as a **first-class business-plan layer**.

**Verdict in one paragraph:** The engine handles AI-as-feature in the product section, AI-as-cost at first-principles in the unit-economics template, and AI-as-internal-efficiency throughout Section 14. It does not yet have AI-COGS modelling at CFO-grade rigour, AI pricing architecture (tier × model × allowance × overage × FX) as a pricing primitive, AI moat-vs-commodity decision logic, AI valuation premium/discount accounting, AI bankability scorecard items, AI-specific stress scenarios (cost spike, model deprecation, hallucination liability event, GPU scarcity), AI data-room standard, AI investor-narrative addendum, AI board-pack section, AI talent strategy for African contexts, or African AI policy context (KE, NG, ZA, RW, AU). This audit specifies the fix.

---

## Part 1 — The Four Archetypes (orientation)

| Archetype | AI cost line | Moat profile | Primary risk | Investor lens |
|---|---|---|---|---|
| **AI-native vertical SaaS** | 8–25% of revenue; rising with usage | Data + workflow moat possible if domain-specific data accrues | Hallucination liability in regulated verticals; data-rights conflict with foundation-model providers | Premium multiple if data + workflow defensibility evident |
| **SaaS-with-AI-features** | 2–10% of revenue; tier-gated | Feature moat weak; product moat carries the business | Cost spike forcing repricing; commodity-feature parity | Neutral multiple; AI is "table stakes," not a multiplier |
| **AI-platform / AI-as-infrastructure** | 30–60% of revenue (COGS-heavy) | Cost moat + integration moat | Foundation-model providers moving down-stack; price compression | Premium if developer adoption + retention; discount if margin <40% |
| **AI-services productising** | Highly variable; productisation maturity dictates | Distribution moat + domain moat | Founder dependency; product never crystallises | Discount until clear product margin emerges |

The plan must **declare its archetype on page one** and the unit economics, pricing, moat thesis, risk, and valuation logic must align to that archetype. The engine currently has no skill that forces this declaration.

---

## Part 2 — NEW SKILLS to Create

Each entry: skill name → target folder → one-line description → why-needed → source / cross-reference.

### Section 10 — Financial Projections

1. **`saas-ai-unit-economics-and-cogs`** → `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/` — Decompose AI cost-of-revenue into token COGS, embedding COGS, fine-tuning amortisation, eval COGS, vector-store COGS, GPU-reservation cost (where relevant), retraining-cycle cost, hallucination-liability reserve. Computes AI Gross Margin, AI Contribution Margin per tier, AI margin contribution to blended GM, and the AI-cost-as-%-of-ARR diagnostic that investors will ask for. **Why:** existing `saas-unit-economics-and-cohort-model` treats AI as one cost line; CFO-grade AI plans need a full COGS waterfall. **Source:** Mersch CFO discipline + Golding multi-tenant economics + 2025 AI-SaaS investor practice.

2. **`saas-ai-cost-of-tenant-calculator`** → `skills/10-financial-projections/saas-ai-cost-of-tenant-calculator/` — A calculator-spec skill: per-tenant token usage × per-1k-token rate × FX × cache-hit-ratio × model-mix + embedding cost + eval cost + amortised fine-tune + retraining contribution + liability reserve. Sensitivity matrix on usage, model price, cache ratio, FX. **Why:** without per-tenant AI cost, tier design is fantasy; the engine needs a formal calculator spec. **Source:** Golding ch. 11; 2025 AI-SaaS investor practice; engine synthesis.

### Section 07 — Marketing & Sales Strategy

3. **`saas-ai-pricing-strategy`** → `skills/07-marketing-sales-strategy/saas-ai-pricing-strategy/` — AI pricing architecture: included-with-tier vs metered (per-query, per-1k-token, per-document) vs hybrid (tier with included allowance + overage) vs AI-as-add-on (separate AI tier) vs outcome-based ("only pay when AI succeeds"). Margin-protection mechanics. African FX overlay (USD-denominated AI cost vs local-currency ARPU). **Why:** generic SaaS pricing skill cannot answer the questions an AI-feature pricing decision raises. **Source:** Walling pp. 67–106; Mersch ch. 10; Cotton essay 6; AI-SaaS pricing practice 2024–2025.

### Section 04 — Market Analysis

4. **`saas-ai-market-and-tam`** → `skills/04-market-analysis/saas-ai-market-and-tam/` — AI-SaaS-specific TAM logic: addressable-by-AI subset of the SaaS TAM; AI-attribution discipline (what % of the customer's "willingness to pay" is genuinely AI-attributable vs general SaaS); sovereign-AI / local-language / regulated-vertical AI TAM segments; AI-skeptic-friendly market sizing (do not over-claim). **Why:** AI plans routinely fail TAM scrutiny because they double-count generic SaaS TAM as if it were AI-specific. **Source:** Cotton TAM discipline; OpenView 2024 AI-SaaS report; Africa.ai market reports.

### Section 06 — Competitive Analysis

5. **`saas-ai-moat-and-defensibility`** → `skills/06-competitive-analysis/saas-ai-moat-and-defensibility/` — Honest defensibility test for AI claims: data moat, workflow moat, distribution moat, cost moat, brand/trust moat, regulatory moat, switching-cost moat. The "false moat" taxonomy (LLM-wrapper, "we use AI," "we fine-tuned a model," API-resale). Wardley-map placement of AI components. **Why:** "AI moat" is the most over-claimed line in 2025–2026 plans; the engine needs a discipline that calls it. **Source:** Walling moats chapter + AI-investor practice 2024–2026.

### Section 03 — Products & Services

6. **`saas-ai-product-strategy-and-roadmap`** → `skills/03-products-services/saas-ai-product-strategy-and-roadmap/` — AI product strategy: feature-vs-platform decision, AI-native vs AI-augmented, build-vs-buy-vs-host-vs-orchestrate, model-router architecture, eval-driven product development, model-deprecation strategy, AI-feature roadmap by ARR milestone with explicit cost gating. **Why:** generic product strategy can't reason about AI product specifics. **Source:** Golding ch. 11; AI-product-management literature 2024–2026; Walling pp. 43–66.

### Section 09 — Management & Team

7. **`saas-ai-talent-strategy`** → `skills/09-management-team/saas-ai-talent-strategy/` — Hiring plan for AI capability: ML / applied-ML engineer, AI product manager, prompt engineer (still real), AI infra / MLOps, AI safety / eval lead, AI policy / compliance, domain-expert-as-AI-trainer roles. African talent pool reality (Lelapa AI, Masakhane, ALU, Andela AI tracks, Carnegie Mellon Africa). Outsource-to-build-to-buy decision. Comp benchmarks. **Why:** AI plans claim "we'll hire an AI team" without specifying what or where; the engine should force the specification. **Source:** Cotton hiring discipline + AI-talent market data + Briter Bridges African AI talent reports.

### Section 12 — Risk Analysis

8. **`saas-ai-risk-and-stress-test`** → `skills/12-risk-analysis/saas-ai-risk-and-stress-test/` — AI-specific risk register: cost spike, model deprecation, performance degradation between model versions, hallucination-liability events, data-rights conflict (training-data lawsuit, model-provider EULA shift), data-sovereignty/residency, vendor concentration, prompt-injection / adversarial input, eval-coverage gaps, model-bias regulatory exposure (EU AI Act, KE / NG / ZA / RW frameworks). AI-stress-test scenarios for `meta-financial-stress-test`. **Why:** generic risk registers miss AI-specific failure modes. **Source:** Mersch ch. 11 + Golding ch. 11 + EU AI Act / NIST AI RMF / African AI policy.

### Meta-Skills

9. **`meta-ai-bankability-and-investor-readiness`** → `skills/meta-ai-bankability-and-investor-readiness/` — AI-specific bankability scorecard layered onto SaaS bankability: AI-cost-as-%-of-ARR, AI-gross-margin trajectory, hallucination-rate trajectory (eval data), eval-coverage %, model-deprecation-watch evidence, AI-data-room contents, AI-incident history, AI-governance committee existence. **Why:** SaaS bankability is no longer sufficient when AI is material; an additional layer is required. **Source:** Mersch CFO discipline + AI-investor diligence practice 2024–2026.

10. **`meta-ai-valuation-adjustments`** → `skills/meta-ai-valuation-adjustments/` — AI premium / discount logic on top of standard SaaS valuation: when AI adds multiple (real data moat, real eval discipline, real cost engineering, real distribution); when AI subtracts multiple (commodity wrapper, undisclosed liability, undisclosed cost trajectory, foundation-model platform risk). Adjustment table by archetype. **Why:** investors in 2026 price the AI thesis explicitly; the engine should model both directions, not just the upside narrative. **Source:** 2024–2026 SaaS multiples research (Bessemer, OpenView, ICONIQ) + Damodaran AI-premium commentary.

### Section 11 — Funding Request

11. **`saas-ai-funding-stage-playbook`** → `skills/11-funding-request/saas-ai-funding-stage-playbook/` — AI-overlay on the standard SaaS funding stage ladder: what an AI plan must show at pre-seed / seed / A / B / growth. AI-specific milestone breakpoints (first model in production; first eval suite; first cost-engineering milestone; first AI-revenue ARR; AI gross margin >X%). Investor-archetype map (AI-specialist funds vs generalist SaaS funds vs sovereign-AI funds vs DFI AI-for-good envelopes). **Why:** AI startups raise differently; the engine should specify. **Source:** Walling funding taxonomy + AI-VC practice (a16z AI, Index AI, Cohere founders fund, Bessemer AI) + DFI AI envelopes.

### Section 11b — Grant Proposal

12. **`saas-ai-for-good-grant-proposal`** → `skills/11b-grant-proposal/saas-ai-for-good-grant-proposal/` — AI-for-good grant proposal architecture: Mozilla African Innovation Mradi, GSMA AI for Impact, IDRC AI4D, Google.org AI for Social Good, Microsoft AI for Good, Lacuna Fund, Patrick J. McGovern Foundation AI, Bill & Melinda Gates AI envelopes. Theory-of-change for AI interventions. **Why:** AI grants follow different rubrics than commercial AI funding; the engine should support both. **Source:** Donor-specific RFPs 2023–2026 + impact-measurement frameworks for AI.

### Section 14 — AI Integration

13. **`saas-ai-integration-deep`** → enhancement scope captured in references (no new skill folder needed beyond the existing `14-ai-integration`); use the existing skill plus new references. *Recommendation: deepen rather than fork.*

### Section 16 — Sustainability Strategy

14. **`saas-ai-sustainability-and-ethics`** → `skills/16-sustainability-strategy/saas-ai-sustainability-and-ethics/` — AI sustainability (compute energy intensity, water for cooling, embodied carbon of GPU manufacture) + AI ethics (fairness, transparency, redress, consent, training-data provenance, downstream-misuse risk). Practical KPIs for plans. Africa angle: where local compute / sovereign AI is genuinely lower-emission vs imported compute. **Why:** ESG and IFC Performance Standards now include AI dimensions; plans must address. **Source:** Stanford AI Index 2024 + Hugging Face energy estimator + IEA AI-and-energy report + IFC PS2-PS6 alignment.

### Meta — Board Reporting

15. **`meta-ai-board-reporting`** → enhancement to existing `meta-board-and-investor-reporting/` (new reference file). *Recommendation: extend the existing skill rather than fork.*

---

## Part 3 — ENHANCEMENTS to Existing Skills

| Existing skill | Enhancement | Reference / source |
|---|---|---|
| `01-executive-summary` | New reference `saas-ai-executive-summary-block.md` — AI archetype declaration, AI-revenue %, AI gross margin, AI moat one-liner, AI risk one-liner, AI funding-use breakdown. | Mersch + AI-investor practice |
| `04-market-analysis` | New reference `ai-tam-attribution.md` — how to honestly compute AI-attributable TAM, avoid the "AI everywhere" inflation, segment by AI-readiness of buyer. | Cotton TAM discipline + OpenView AI-SaaS |
| `06-competitive-analysis` | New reference `ai-moats-vs-false-moats.md` — extends Walling moats taxonomy with AI-specific cases and counter-cases. | Walling + AI-investor practice |
| `07-marketing-sales-strategy` | New reference `ai-feature-pricing-and-positioning.md` — AI-as-positioning vs AI-as-feature, "AI-native" claim discipline, freemium-on-AI cost-control. | Walling + Garbugli + AI-SaaS pricing practice |
| `08-operations-plan` | New reference `ai-cost-and-vendor-management-ops.md` — multi-model vendor strategy, model-router design, eval pipeline operational discipline, cost-engineering rituals, model-deprecation calendar, AI-incident runbook. | Golding ch. 11 + 2024–2026 AI-ops practice |
| `10-financial-projections` | Update `SKILL.md` to point new AI-aware SaaS plans to the new `saas-ai-unit-economics-and-cogs` and `saas-ai-cost-of-tenant-calculator` skills. | Engine cross-wiring |
| `11-funding-request` | New reference `saas-ai-investor-update-block.md` — AI section for monthly investor update (AI revenue, AI margin, eval scores, top AI risks, model-mix changes). | AI-investor diligence practice |
| `12-risk-analysis` | New reference `saas-ai-risk-register-template.md` — AI risk register populated with cost / model / data / vendor / regulatory / ethical risks plus mitigation owners and cadence. | Mersch + Golding + EU AI Act + NIST AI RMF |
| `14-ai-integration` | Update `SKILL.md` to reference the deep AI-SaaS plan skills (cost-of-tenant, AI pricing, AI moat, AI risk) so this section becomes the cross-section integrator rather than a standalone island. | Engine cross-wiring |
| `16-sustainability-strategy` | New reference `ai-ethics-and-sustainability-block.md` — practical AI ethics + sustainability KPIs for plans. | Stanford AI Index + IEA + IFC PS |
| `meta-bankability-scoring` | New AI-scorecard items added to existing `saas-bankability-scorecard.md` (or new file): AI-cost-as-%-of-ARR, AI gross margin, eval coverage, hallucination trajectory, governance committee. | Engine synthesis |
| `meta-valuation` | New reference `saas-ai-valuation-adjustments.md` — premium / discount logic by archetype. | Damodaran AI commentary + 2024–2026 multiples research |
| `meta-due-diligence` | New reference `saas-ai-data-room-contents.md` — AI-specific data-room checklist (model card, eval suite + history, training-data provenance, EULA exposures, AI-incident log, governance artefacts). | AI-DD practice 2024–2026 |
| `meta-financial-stress-test` | New reference `saas-ai-stress-test-scenarios.md` — AI cost-shock, model-deprecation, hallucination-event-liability, GPU-scarcity, foundation-model-platform-risk, FX-on-USD-AI-cost. | Mersch + AI-risk practice |
| `saas-bankability-and-investor-readiness` | Append AI scorecard module to checklist + workflow. | Engine cross-wiring |
| `saas-valuation-and-fundraising-strategy` | Append AI premium/discount module + AI-archetype investor-target map. | Engine cross-wiring |
| `meta-living-plan-governance` | AI cadence addition: eval weekly, hallucination rate monthly, per-tenant AI cost monthly, retraining-trigger and model-deprecation watch monthly. | Engine cross-wiring |
| `meta-board-and-investor-reporting` | New reference `saas-ai-board-pack-section.md` — AI section template for quarterly board pack. | Engine cross-wiring |
| `country-context/africa-regional/africa-ict-saas-market-context.md` | Append Section 14 — Africa-AI context (compute scarcity, GPU access, sovereign AI demand, local-language opportunity, AI policy by country: KE strategy, NG NITDA AI roadmap, ZA AI policy framework, RW AI policy, AU AI strategy). | African Union Continental AI Strategy 2024; KE National AI Strategy; NG NITDA NAIS 2024; ZA AI Policy Framework; RW National AI Policy 2023 |

---

## Part 4 — REFERENCE FILES / TEMPLATES / MODELS to Add

Each of these lives in the most relevant skill's `references/` folder unless noted as engine-cross-cutting.

1. `saas-ai-cost-of-tenant-calculator.md` — formula spec, worksheet structure, sensitivity matrix, worked East-African vertical-SaaS example.
2. `saas-ai-unit-economics-template.md` — AI-COGS waterfall, AI gross margin, AI contribution margin, AI tier contribution, AI cost-as-%-of-ARR.
3. `saas-ai-pricing-architecture.md` — tier × model × allowance × overage × FX architecture; African pricing realities.
4. `saas-ai-moats-and-defensibility-checklist.md` — moat-claim test + false-moat taxonomy.
5. `saas-ai-risk-register-template.md` — populated risk register with mitigation owners.
6. `saas-ai-funding-stage-playbook.md` — AI overlay on the SaaS stage ladder.
7. `saas-ai-grant-proposal-template.md` — AI-for-good grant architecture.
8. `saas-ai-investor-update-block.md` — AI section of the monthly investor update.
9. `saas-ai-board-pack-section.md` — AI section of the quarterly board pack.
10. `saas-ai-valuation-adjustments.md` — premium / discount logic.
11. `saas-ai-talent-and-org-design-template.md` — AI-team composition by ARR milestone, African talent map.
12. `africa-ai-context-extension.md` — Africa-AI context block (sits inside `africa-ict-saas-market-context.md` as Section 14, plus standalone copy).
13. `saas-ai-stress-test-scenarios.md` — quantified AI stress scenarios.
14. `saas-ai-data-room-contents.md` — AI-specific DD checklist.
15. `saas-ai-executive-summary-block.md` — AI section of the executive summary.
16. `ai-tam-attribution.md` — AI-TAM honest-attribution discipline.
17. `ai-moats-vs-false-moats.md` — moat decision logic.
18. `ai-feature-pricing-and-positioning.md` — positioning discipline.
19. `ai-cost-and-vendor-management-ops.md` — AI ops practice.
20. `ai-ethics-and-sustainability-block.md` — Section 16 block.

---

## Part 5 — The Living-Plan AI Cadence (engine-wide standard)

Every AI-enabled SaaS plan must encode this cadence in addition to the standard living-plan cadence:

| AI element | Cadence | Owner | Variance threshold | Trigger-replan condition |
|---|---|---|---|---|
| Eval suite scores (accuracy, hallucination, refusal, latency) | weekly | Head of AI | -5pp on any metric | -10pp drop in a single week |
| Per-tenant AI cost | monthly | CFO + Head of AI | +20% MoM | sustained +30% over 2 months |
| AI gross margin | monthly | CFO | -3pp MoM | -5pp QoQ |
| AI-cost-as-%-of-ARR | monthly | CFO | >15% alarm | >20% absolute alarm |
| Hallucination rate (production sampling) | monthly | Head of AI / Head of QA | +1pp absolute | High-severity event = immediate |
| Retraining trigger watch | monthly | Head of AI | drift >threshold | concept drift confirmed |
| Model-deprecation watch | monthly | Head of AI / CTO | provider notice | provider deprecation notice issued |
| AI moat reassessment | quarterly | CEO + Head of Strategy | competitive parity claim | foundation-model commoditises capability |
| Regulatory AI watch | quarterly | Head of Legal / Compliance | new rule in operating jurisdiction | active enforcement against analogue |
| AI-incident log | continuous + monthly review | Head of AI | any sev-1 incident | sev-1 customer-impact event |
| AI vendor concentration | quarterly | CFO + CTO | >80% on single provider | provider EULA / pricing shock |
| AI talent retention | quarterly | Head of People + CTO | >20% AI-team attrition | departure of AI lead |

---

## Part 6 — Africa-AI Context (summary; full text in extension reference)

Africa-AI realities that must shape any African AI-SaaS plan:

- **Compute scarcity** — limited GPU availability in-region; pricing typically 1.5-3× US/EU equivalents when available; most workloads run on AWS Cape Town / Azure SA / GCP Jo'burg or US/EU regions with latency cost.
- **GPU access** — Cassava Technologies / Africa Data Centres GPU build-out (2024–2026); Liquid Intelligent Technologies; MainOne (Nigeria); MTN AI factories programme; Ethiopian AI Institute. Demand exceeds supply.
- **Sovereign AI demand** — public-sector and regulated-sector procurement increasingly requires in-country data residency for AI. Procurement preferences for locally-trained or locally-hosted models.
- **Local-language data advantage** — African-language data (Swahili, Hausa, Yoruba, Amharic, Igbo, Zulu, Xhosa, Luganda, Lingala, Wolof, Tigrinya) is a real moat for AI startups that legitimately curate it. Lelapa AI, Masakhane, EqualyzAI, Awarri.
- **AI policy environment** —
  - **African Union Continental AI Strategy** (2024) — set policy direction for member states
  - **Kenya** National AI Strategy 2025-2030 (drafted/launched)
  - **Nigeria** NITDA National AI Strategy (NAIS) 2024 + draft AI regulation
  - **South Africa** National AI Policy Framework
  - **Rwanda** National AI Policy 2023 (one of Africa's earliest)
  - **Egypt** National AI Strategy (updated 2024)
  - **Mauritius** AI Strategy
  - **Ghana** AI Strategy in draft
  - **Uganda** ICT Policy 2024 with AI provisions; NITA-U guidelines emerging
- **AI funding ecosystem in Africa** — IFC AI envelopes, AfDB AI-for-development, Google.org AI for Social Good, Microsoft AI for Good, GSMA AI for Impact, Mozilla AI, IDRC AI4D, Lacuna Fund (training-data grants), Patrick J. McGovern Foundation.
- **AI talent in Africa** — Carnegie Mellon Africa (Rwanda); ALU AI track (Rwanda/Mauritius); Andela AI talent pool; AIMS network (South Africa, Cameroon, Senegal, Tanzania, Ghana, Rwanda); Deep Learning Indaba alumni network; Black in AI Africa chapters; Lelapa AI (research + startup); InstaDeep (now BioNTech; African-roots success precedent).

---

## Part 7 — Priority Order

**Tier 1 (do in this session):**
- `saas-ai-unit-economics-and-cogs` + template
- `saas-ai-cost-of-tenant-calculator` + spec
- `saas-ai-pricing-strategy` + architecture reference
- `saas-ai-moat-and-defensibility` + checklist
- `saas-ai-risk-and-stress-test` + register + stress scenarios
- `meta-ai-bankability-and-investor-readiness` (scorecard)
- `meta-ai-valuation-adjustments` (premium/discount)
- `africa-ai-context-extension.md` + append Section 14 to africa regional context
- Living-plan AI cadence wired into `meta-living-plan-governance`
- AI section added to `meta-board-and-investor-reporting`
- AI executive-summary block

**Tier 2 (do in this session if budget allows):**
- `saas-ai-product-strategy-and-roadmap`
- `saas-ai-market-and-tam` + TAM attribution reference
- `saas-ai-talent-strategy` + team-design template
- `saas-ai-funding-stage-playbook`
- `saas-ai-for-good-grant-proposal`
- `saas-ai-sustainability-and-ethics`
- Section enhancements (01, 04, 06, 07, 08, 10, 11, 12, 14, 16) via reference files
- AI data-room contents
- AI investor-update block

**Tier 3 (next session):**
- Full AI-policy-by-country expansion (per-country playbooks)
- AI-supply-chain due diligence (training-data provenance audit framework)
- AI agent / multi-agent product economics
- AI procurement for African public sector (sovereign-AI tendering)
- Vertical-specific AI playbooks (AI-agritech, AI-healthtech, AI-fintech, AI-legaltech, AI-edtech, AI-govtech)

---

## Part 8 — How this audit composes with the prior SaaS audit

The prior `saas-ict-business-plan-skills-audit-2026.md` made the engine world-class at SaaS operating discipline. This audit lays AI on top:

- Where SaaS unit economics had one AI cost line, AI unit economics decomposes it into a full COGS waterfall.
- Where SaaS pricing had AI as one tier dimension, AI pricing makes the tier-model-allowance-overage-FX architecture a primitive.
- Where SaaS moats had a 5-question test, AI moats run the test with AI-specific evidence and reject the most common false-moat claims.
- Where SaaS risk register had "AI cost spike" as one bullet, AI risk register decomposes into 12+ failure modes with mitigation owners.
- Where SaaS valuation had a Rule-of-40-adjusted multiple, AI valuation applies a premium / discount on top with explicit reasoning.
- Where SaaS bankability had a SaaS scorecard, AI bankability adds eval discipline, hallucination trajectory, cost engineering, governance.
- Where SaaS living-plan cadence had weekly KPIs and monthly cohorts, AI living-plan cadence adds weekly evals, monthly per-tenant AI cost, monthly hallucination sampling, monthly model-deprecation watch.
- Where SaaS board pack had product / GTM / financial / risk sections, AI board pack adds an AI section.

This audit is the work order. The session that follows executes Tier 1 in full and Tier 2 substantially, with Tier 3 deferred.
