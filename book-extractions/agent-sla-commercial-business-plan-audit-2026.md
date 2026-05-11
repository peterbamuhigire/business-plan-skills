# AI Agent SLA + Commercial Layer Business-Plan Skills Audit — 2026

**Purpose.** Specification for the **agent SLA + commercial business-plan skill stack** that the engine must add to the existing agent-products skill stack. Where the agent-products audit (2026) established that agents are a distinct product class with their own cost waterfall, moats, risks, talent, and valuation, this audit establishes that **agent SLAs and outcome pricing trigger a distinct financial-reporting and commercial-policy layer** that no existing skill covers end-to-end.

**Scope.** Sits on top of:
- `saas-ict-business-plan-skills-audit-2026.md` (SaaS operating discipline)
- `ai-on-saas-business-plan-audit-2026.md` (AI-on-SaaS layer)
- `agent-products-business-plan-audit-2026.md` (agent product class)

The SLA + commercial layer **does not replace** any prior layer — it composes on top. A serious agent-product plan with measurable SLAs (which any plan selling per-resolution / per-outcome / supervised-tier pricing now requires) must show:

1. **Revenue recognition policy** — ASC 606 / IFRS 15 treatment for the specific pricing primitive (per-resolution, per-outcome, subscription+success, prepaid task credits, hybrid)
2. **Deferred revenue mechanics** — for prepaid agent credits, annual prepaid SLA-tier upgrades, and platform-fee components
3. **SLA-credit reserve** — accrued liability sized off trailing SLA-credit history, true-up cadence, auditor-acceptable
4. **Refund reserve** — distinct from SLA-credit; sized off failed-outcome history
5. **COGS-vs-contra-revenue policy** — which SLA-related cost lines are COGS (HITL labour, retraining amortisation), which are contra-revenue (SLA credits issued, outcome-pricing refunds), which are S&M (customer-success cost related to SLA defence)
6. **Commercial packaging economics** — agent included / agent add-on / agent standalone; attach-rate × ARPU lift × cannibalisation discipline
7. **Outcome-pricing business case** — when outcome pricing wins commercially vs when it loses (margin volatility model)
8. **SLA-specific risks** — catastrophic SLA breach event, model-cost shock breaking SLA economics, customer gaming, regulator-mandated SLA
9. **Investor narrative on SLA** — confidence-builder when strong; liability when weak
10. **Valuation overlay for SLA** — measurable, published, breachable SLA performance trades at a premium; hidden or weak SLA performance trades at a discount

**Method.** Walked the agent-products skill stack and tested it against five 2026-realistic SLA-bearing agent commercial archetypes:

1. **Per-resolution agent under uptime + accuracy SLA** (CX resolution; SLA breach = % credit)
2. **Per-outcome agent under definition-of-done SLA** (collections, legal-research, medical-coding; outcome verified by counter-party process)
3. **Subscription + success-fee hybrid** (platform fee + variable success fee; SLA on success fee triggers credit)
4. **Prepaid task-credit model** (customer prepays N task credits; deferred revenue + breakage policy)
5. **Multi-tier SLA with priced bronze / silver / gold** (different uptime + response + accuracy SLAs at different prices; SLA-tier cannibalisation risk)

For each archetype: which sections of the plan are SLA-specific, which existing skills cover them, where the gaps are.

**Verdict.** The engine handles agent unit economics, pricing primitives, risk registers, and board reporting at world-class depth. It does **not** yet treat the SLA + commercial layer as a distinct financial-reporting and policy domain. There is:

- No ASC 606 / IFRS 15 revenue-recognition policy module specific to agent pricing primitives
- No deferred-revenue mechanics for prepaid agent task credits
- No SLA-credit reserve methodology (formula + true-up cadence)
- No refund-reserve methodology distinct from SLA-credit
- No SLA-COGS-vs-contra-revenue policy
- No SLA-economics-in-projection module (how SLA performance feeds into the 3yr / 5yr plan)
- No commercial-packaging economics module (Included / Add-on / Standalone)
- No outcome-pricing-business-case module (when outcome pricing wins vs loses)
- No SLA-specific risk register (catastrophic breach, gaming, regulator SLA)
- No revenue-recognition policy meta-skill (auditor-ready policy memo template)
- No SLA financial-controls meta-skill (approval workflow, dispute escalation, SOC1 link)
- No investor-narrative-on-SLA module
- No valuation overlay for SLA quality
- No SLA bankability checklist, no SLA data-room contents, no SLA stress-test scenarios, no SLA cadence in living-plan governance, no SLA board-pack block, no SLA exec-summary paragraph

This audit specifies the fix.

---

## Part 1 — The Five Commercial Archetypes (orientation)

| Archetype | Primary unit | Rev-rec trigger | Reserve type | Margin volatility | Investor lens |
|---|---|---|---|---|---|
| **Per-resolution + uptime/accuracy SLA** | Resolved ticket | Point-in-time on successful resolution | SLA-credit accrual | Moderate (intervention-rate-driven) | Premium if cost-per-resolved < anchor and SLA credit < 2% of agent revenue |
| **Per-outcome under DoD SLA** | Verified outcome | Point-in-time on outcome verification by counter-party | Refund reserve + SLA credit | High (outcome variance) | Premium if outcome-attribution clean + low refund |
| **Subscription + success-fee hybrid** | Two performance obligations | Subscription ratable; success-fee point-in-time | SLA credit on subscription, refund on success-fee | Moderate | Premium if both legs disciplined |
| **Prepaid task-credit** | Drawdown of prepaid credits | Recognise as credits consumed; breakage policy required | Deferred revenue liability + breakage estimate | Low if usage smooth | Premium if breakage <10% and drawdown trackable |
| **Multi-tier SLA (bronze/silver/gold)** | Tier price × volume | Per-tier subscription ratable; SLA credit per tier | Tier-specific SLA-credit reserve | Moderate; cannibalisation risk | Premium if mix optimised and base-tier price not eroding |

The plan must declare the **commercial archetype** in the executive summary and the rev-rec policy, reserve methodology, COGS treatment, packaging logic, risk register, and projection must align to that archetype. No existing skill forces this declaration.

---

## Part 2 — NEW SKILLS to Create

Each entry: skill name → target folder → one-line purpose → why-needed.

### Section 10 — Financial Projections

1. **`saas-agent-revenue-recognition`** — ASC 606 / IFRS 15 for agent revenue. Per-resolution = point-in-time at successful resolution; per-outcome = point-in-time at outcome verification by counter-party process; subscription + success fee = bundled allocation with two performance obligations; prepaid credits = deferred revenue with breakage; performance obligations identification; transaction-price allocation; variable-consideration estimation (expected-value vs most-likely-amount) for outcome pricing; constraint on variable consideration; principal-vs-agent (for marketplace agents). **Why:** Standard SaaS rev-rec assumes ratable subscription; agent rev-rec requires per-pricing-primitive policy because the recognition event is fundamentally different.

2. **`saas-agent-deferred-revenue-and-credit-reserves`** — Deferred-revenue mechanics for prepaid agent task credits (recognise as credits consumed; breakage policy under ASC 606 BC394 / IFRS 15.B46); SLA-credit accrued liability (sized off trailing SLA-credit issued ÷ trailing agent revenue × forward agent revenue × adjustment factor); refund-reserve methodology; reserve true-up cadence; balance-sheet presentation. **Why:** No existing skill covers the liability-side of agent commercial commitments; auditors and DD teams quote these reserves.

3. **`saas-agent-sla-cogs-treatment`** — Which SLA-related cost lines are COGS (HITL labour for SLA defence, retraining amortisation, SLA-monitoring infrastructure, eval cost for SLA-relevant metrics), which are contra-revenue (SLA credits issued, outcome refunds), which are S&M (customer-success cost related to SLA management), which are G&A (legal cost defending SLA disputes). Disclosure policy. **Why:** Generic SaaS COGS guidance does not address SLA credits and outcome refunds; getting this wrong overstates revenue and understates COGS.

4. **`saas-agent-sla-economics-in-projection`** — How the 3yr / 5yr projection treats SLA performance: SLA-breach scenarios feed into revenue (credit cost), risk register (reputational), churn (SLA performance as leading indicator), and funding need (reserve drawdown). Modelling SLA performance as a leading indicator of churn. SLA-tier mix evolution. Cost-of-quality assumptions. **Why:** Standard projections treat SLA breach as a one-time event; SLA-bearing agent businesses must model SLA performance as an integrated driver.

### Section 07 — Marketing & Sales Strategy

5. **`saas-agent-commercial-packaging-economics`** — Economics of "Agent Included" vs "Agent Add-on" vs "Agent Standalone": ARPU lift, ACV expansion, attach rate assumptions, cannibalisation of base-tier, base-tier price erosion risk, free-trial discipline, packaging migration discipline, multi-product NRR composition. **Why:** Pricing skill covers the pricing primitive; packaging is a separate commercial decision with its own economics.

6. **`saas-agent-outcome-pricing-business-case`** — When outcome pricing wins commercially (high TCV, narrow success definition, low-variance outcomes, regulated/measurable outcomes, customer prefers risk-transfer) versus when it loses (high variance, attribution ambiguity, long verification lag, low TCV not worth measurement overhead). Margin-volatility implications. When to refuse outcome pricing. **Why:** Pricing skill mentions outcome pricing as a primitive; it does not adjudicate when outcome pricing is commercially correct.

### Section 12 — Risk Analysis

7. **`saas-agent-sla-risk`** — SLA-specific risks: catastrophic SLA breach event (sev-1 mass-credit), model-cost shock making SLA-tier pricing economically unviable, customer-side SLA gaming (false intervention reports, false outcome rejections), regulator-mandated SLA standard, SLA-credit accrual blowing past reserve, dispute backlog risk. Stress scenarios. **Why:** Agent risk skill covers autonomy / irreversibility; SLA risk is a separate category with financial-reporting consequences.

### Section 11 — Funding Request

8. **`saas-agent-investor-narrative-on-sla`** — Investor narrative for fundraising. When SLA is a confidence-builder (strong published performance, low credit accrual, disciplined reserve). When SLA is a liability question (hidden performance, ad hoc reserves, undisclosed disputes). Benchmark SLA performance vs peers. SLA as moat element. SLA narrative in pitch deck and data room. **Why:** Funding skills cover use-of-proceeds and milestones; SLA narrative is a separate discipline that determines whether SLA reads as differentiation or risk.

### Meta-Skills

9. **`meta-agent-revenue-recognition-policy`** — Auditor-ready policy declaration template for the plan. Per pricing primitive: performance obligation, transaction-price allocation, recognition trigger, variable consideration treatment, principal-vs-agent, breakage policy, refund policy, contract-modification policy. Policy memo template. **Why:** Audit firms expect a documented policy memo for non-standard revenue patterns; agent revenue is non-standard.

10. **`meta-agent-sla-financial-controls`** — Financial controls for SLA economics: SLA-credit approval workflow (who approves what credit at what threshold), reserve methodology, true-up cadence, dispute escalation, SOC1 financial-controls cross-link, audit-trail of credits issued, segregation of duties. **Why:** Bankability and DD increasingly check financial-control maturity around variable revenue; no skill currently encodes this.

11. **`meta-agent-valuation-overlay-for-sla`** — Valuation overlay for SLA quality. Premium when SLA performance is strong, published, audited, disclosed; discount when SLA performance is hidden, weak, or contested. Effect on ARR multiple. Cross-reference to `meta-agent-valuation-adjustments`. **Why:** Agent valuation skill captures moat-vs-wrapper; SLA quality is a separate valuation driver because it signals operational maturity and risk-of-revenue-volatility.

---

## Part 3 — ENHANCEMENTS to Existing Skills (reference files)

| Section / Skill | Reference to add | Purpose |
|---|---|---|
| `10-financial-projections` (SKILL.md) | Pointer block | Point to new SLA rev-rec + reserve skills |
| `saas-agent-unit-economics-and-cogs` | SLA-COGS-treatment subsection in SKILL.md | Where SLA credits / refunds / HITL-for-SLA flow in cost waterfall |
| `saas-agent-pricing-strategy` | SLA-tier pricing economics subsection | Bronze / silver / gold SLA-tier mix economics |
| `saas-agent-risk-and-stress-test` | Extended stress scenarios | Catastrophic SLA breach + model-cost SLA shock + SLA gaming |
| `meta-bankability-scoring` | `saas-agent-sla-bankability-checklist.md` | SLA bankability questions (policy, reserve, dispute, history) |
| `meta-valuation` | `saas-agent-sla-valuation-adjustments.md` | SLA valuation overlay table |
| `meta-due-diligence` | `saas-agent-sla-data-room-contents.md` | SLA history, reserve calc, audit trail, dispute log |
| `meta-financial-stress-test` | `saas-agent-sla-stress-test-scenarios.md` | SLA-breach financial scenarios |
| `meta-living-plan-governance` | SLA cadence addition to `agent-cadence-table.md` | Weekly SLA performance; monthly credit reserve true-up; quarterly SLA policy review |
| `meta-board-and-investor-reporting` | `saas-agent-sla-board-block.md` | SLA section template for board pack |
| `01-executive-summary` | `saas-agent-sla-executive-summary-paragraph.md` | One-paragraph exec-summary SLA block |
| `11-funding-request` | Pointer | Link to investor-narrative-on-SLA skill |

---

## Part 4 — Reference files / templates

| Path | Purpose |
|---|---|
| `saas-agent-revenue-recognition-policy-template.md` | Per pricing primitive: per-resolution, per-outcome, hybrid, subscription+success, prepaid credits — with worked ASC 606 5-step example |
| `saas-agent-credit-reserve-methodology.md` | Reserve formula; quarterly true-up; balance-sheet presentation |
| `saas-agent-refund-reserve-methodology.md` | Refund-reserve formula and policy |
| `saas-agent-deferred-revenue-template.md` | Prepaid task credits → DR; recognition trigger; breakage |
| `saas-agent-sla-cogs-policy.md` | Which costs go to COGS vs contra-revenue vs S&M vs G&A |
| `saas-agent-sla-stress-test-scenarios.md` | Catastrophic breach financial impact + 8 standardised scenarios |
| `saas-agent-commercial-packaging-economics-template.md` | Attach-rate × ARPU lift × cannibalisation worked model |
| `saas-agent-outcome-pricing-business-case-template.md` | When outcome pricing wins / loses, margin-volatility model |
| `saas-agent-sla-bankability-checklist.md` | SLA bankability scorecard |
| `saas-agent-sla-valuation-adjustments.md` | SLA valuation overlay |
| `saas-agent-sla-board-block.md` | Board-pack SLA section template |
| `saas-agent-sla-investor-narrative.md` | Sample investor-update language |
| `africa-agent-sla-context.md` | FX pass-through impact on SLA; sovereign-AI SLA chains; mobile-money settlement cycles for per-resolution; African insurer interest |

---

## Part 5 — Living-Plan SLA Cadence Additions

Append to `meta-living-plan-governance/references/agent-cadence-table.md`:

**Weekly:**
- SLA performance (uptime / response time / accuracy / DoD compliance) — Owner: Head of Agent + Customer Success; threshold: any breach below contracted SLA
- SLA-credit accrual rate — Owner: CFO + Customer Success; threshold: >2% of agent MRR
- Dispute queue depth — Owner: Customer Success; threshold: >5 open disputes >7 days old

**Monthly:**
- SLA-credit reserve adequacy — Owner: CFO; threshold: actual credits issued >110% of reserve drawn
- Refund reserve adequacy — Owner: CFO; threshold: >110% of reserve drawn
- SLA-driven churn signal — Owner: Customer Success + CFO; threshold: churn correlated with SLA misses
- Deferred-revenue waterfall — Owner: CFO; threshold: deferred-revenue aging anomaly
- SLA-tier mix shift — Owner: Head of GTM + CFO; threshold: >10% mix shift toward lower tier

**Quarterly:**
- SLA policy review (refresh SLA terms, thresholds, credits) — Owner: Head of GTM + CFO + General Counsel
- Reserve methodology true-up — Owner: CFO + Auditor; threshold: methodology assumption change
- SLA narrative for investor update — Owner: CEO + CFO
- Outcome-pricing business case revalidation — Owner: CFO + Head of GTM

**Trigger-replan additions:**
- Catastrophic SLA breach (>5% of customers affected sev-1)
- SLA-credit accrual breach reserve >120%
- Foundation-model price spike making SLA-tier pricing unprofitable
- Customer dispute moves to legal escalation
- Regulator mandates new SLA standard

---

## Part 6 — Africa SLA Realities

- **FX pass-through to SLA economics** — USD-priced foundation-model and tool cost flows into the cost-floor that an SLA-backed price must clear. A 15% local-currency depreciation can convert a profitable SLA tier into a loss-maker overnight; SLA contracts must either price in USD or include FX-corridor clauses.
- **Mobile-money settlement realities for per-resolution** — micro-billing on resolved tickets via MoMo / M-Pesa / Airtel Money / Wave / Orange Money / OPay carries 1-2.5% transaction fee + T+0 to T+2 settlement; revenue-recognition timing differs from invoice-and-receivable enterprise contracts; cash and revenue can diverge for 1-3 days.
- **Sovereign-AI provider SLA chains** — when in-region compute (af-south-1, africa-south1, Cassava, Liquid, Raxio, MTN AI Factories, Ethiopian AI Institute) is mandated, the agent vendor's SLA depends on the in-region provider's SLA; chain risk must be disclosed and reserves must cover provider-SLA-breach pass-through.
- **African insurer interest in SLA-backed agentic products** — insurers in regulated sectors (microinsurance, life, motor, agri) want SLA-backed AI vendors before integrating into core operations; SLA disciplined plans win the deals; SLA ambiguity loses them.
- **Public-sector SLA expectations** — KE Huduma, NG NIMC, RW Irembo, UG NITA-U, ZA Home Affairs and analogues increasingly include SLA schedules in tenders; vendors must price and reserve for these.
- **DFI / multilateral SLA scrutiny** — IFC, AfDB, FMO, BII, Proparco, FCDO, USAID, GIZ now read SLA performance in agent-product DD; weak SLA discipline is a disqualifier.
- **Currency-of-record on SLA credits** — SLA credits issued in local currency at time of breach can blow up if USD-denominated cost was the original economics; SLA-credit currency clauses now standard practice.

---

## Part 7 — Coordination with Engineering and Contracts Sessions

This skill stack is the **financial discipline + plan-level treatment** layer. Two paired sessions own the adjacent layers:

- **Software-development session (engineering enforcement)** owns: SLA telemetry; uptime / response-time / accuracy measurement; SLA-monitoring observability stack; SLA-breach detection and alerting; automated SLA-credit calculation; kill-switch wiring to SLA breach events; eval-loop coverage of SLA-relevant metrics.
- **Proposal / contracts session (commercial language)** owns: SLA contract language; SLA-credit clauses; dispute-resolution clauses; force-majeure scope; vendor-cost-pass-through clauses; FX-corridor clauses; outcome-definition language; counter-party verification clauses; insurance / indemnity clauses.

The financial-discipline session here links to both: rev-rec policy depends on contract language (proposal session); reserve methodology depends on telemetry quality (engineering session); cost-floor depends on engineering choices.

---

## Part 8 — Critical Gaps After This Build

After this audit and the skill build, the following remain open:

- **Industry-specific SLA benchmarks** — sector-by-sector SLA benchmark library (CX, collections, legal, medical, agri) — partial; will need a `references/saas-agent-sla-industry-benchmarks.md` in a future session
- **Auditor playbook** — formal Big-4 / regional firm acceptance documentation; out of scope here but flagged for `meta-accounting-finance-review` extension
- **Customer health-score integration with SLA performance** — flagged for `saas-customer-success-operating-model` integration
- **SLA-as-product-differentiation marketing playbook** — flagged for `saas-marketing-channel-economics` integration

---

## Part 9 — Recommended Next Sessions

1. **Engineering enforcement of SLA** (software-dev session) — telemetry, monitoring, alerting, automated credit calculation, kill-switch integration
2. **Contracts and commercial language** (proposal session) — SLA clauses, dispute resolution, force majeure, FX corridor, outcome definition
3. **Industry-vertical SLA benchmark libraries** — CX, collections, legal, medical, agri sector-specific SLA standards
4. **Insurance and indemnity for SLA-bearing agents** — AI E&O coverage of SLA exposure; reinsurance availability in Africa
5. **Auditor acceptance pack** — Big-4 / regional accountancy firm coordination on rev-rec policy memos and reserve methodologies
