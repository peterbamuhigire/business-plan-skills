# AI Agent / Multi-Agent Product Business-Plan Skills Audit — 2026

**Purpose.** Specification for the **agent-product business-plan skill stack**. AI agents (single-agent and multi-agent products that take action on behalf of users, with autonomy, tool use, and consequence) have **materially different** economics, moats, risks, talent needs, regulatory exposure, and valuation logic than RAG-style copilots or AI-as-feature SaaS. Investors in 2026 increasingly demand explicit agent-layer treatment — they will not accept agent businesses being modelled as ordinary AI-SaaS.

**Scope.** Sits on top of:
- `saas-ict-business-plan-skills-audit-2026.md` (SaaS operating discipline)
- `ai-on-saas-business-plan-audit-2026.md` (AI-on-SaaS layer)

The agent layer **does not replace** either prior layer — it composes on top. A serious agent-product plan still passes SaaS bankability and AI-SaaS bankability; this audit adds the agent-specific module.

**Method.** Walked the full skill catalogue (00→16, all `meta-*`, all SaaS-AI skills produced in the AI-on-SaaS session) and tested it against five 2026-realistic **agent-product archetypes**:

1. **Single-agent customer-service / resolution agent** (CX agent: triage, resolve, escalate; per-resolution economics)
2. **Single-agent operations agent** (back-office agent: ledger reconciliation, inventory updates, invoice processing; per-task economics)
3. **Multi-agent orchestrated workflow** (planner + worker + critic; deep research, deep procurement, deep audit; per-outcome economics)
4. **Vertical agentic SaaS** (legal-research agent, medical-coding agent, agri-extension agent, fintech-collections agent)
5. **Agent platform / agent-as-infrastructure** (orchestration framework, tool registry, eval-loop platform; per-step / per-agent economics)

For each archetype: which sections of the plan are agent-specific, which existing skills cover them, and where the gaps are.

**Verdict.** The engine handles AI-as-feature (Section 14 + AI-on-SaaS skills) at world-class depth. It does **not** yet treat agents as a distinct product class. There is no agent unit-economics waterfall (steps × tools × parallel branches × retries), no agent pricing primitive (per-resolution / per-outcome / per-step / hybrid / intervention-credit), no agent-moat-vs-wrapper rubric, no agent talent map (with AI Safety Lead as a mandatory role rather than an optional one), no agent risk register (autonomy / irreversibility / regulator / collusion), no agent valuation overlay (premium when defensible, **wrapper discount** when not), no agent KPI cadence (task success, intervention rate, cost-per-resolved-task, irreversibility-incident log), no agent-specific funding playbook (which agent funds, which DFI AI-agent envelopes), no agent ethics module (action accountability, contestability, jobs-impact disclosure), and no Africa-agent context (public-sector agents, sovereign-AI for agents, talent realities for agent engineering). This audit specifies the fix.

---

## Part 1 — The Five Archetypes (orientation)

| Archetype | Primary metric | Cost driver | Moat profile | Primary risk | Investor lens |
|---|---|---|---|---|---|
| **CX resolution agent** | Resolutions / month; intervention rate | LLM steps × tools per ticket | Workflow + integration depth + eval-loop on real tickets | Hallucination → wrong customer answer; vendor switch | Premium if cost-per-resolved-ticket << cost-per-agent-resolved-by-human |
| **Ops back-office agent** | Tasks / month; STP (straight-through-processing) rate | Steps × ERP-tool invocations + retries | Integration + audit-trail + regulator clearance | Irreversibility incident (wrong ledger entry, wrong inventory adjustment); audit/regulatory exposure | Premium if STP > 80% and audit accepts |
| **Multi-agent orchestrated** | Outcomes / month; cost per outcome | Planner + N workers + critic; tokens × branches × retries | Proprietary tool registry + planner-eval data | Cost runaway from branch explosion; agent collusion / loop | Premium if eval discipline + cost ceiling |
| **Vertical agentic SaaS** | Domain-specific outcomes (cases researched, codes assigned, claims processed) | Steps × domain tools + supervised review | Domain data + workflow + regulatory + customer-trust | Sector regulator action; domain misuse | Premium if vertical regulator engagement evidenced |
| **Agent platform / infra** | Active agents; agent-runtime hours; tool invocations | Compute + tool gateway + observability | Developer adoption + tool ecosystem + eval-loop platform | Foundation model providers absorbing the orchestration layer | Premium if ecosystem; discount if wrapper of LangChain / CrewAI / AutoGen |

The plan must **declare its agent archetype on page one** and the cost waterfall, pricing, moat thesis, risk register, talent plan, and valuation logic must all align to that archetype. No existing skill forces this declaration.

---

## Part 2 — NEW SKILLS to Create

Each entry: skill name → target folder → one-line purpose → why-needed.

### Section 10 — Financial Projections

1. **`saas-agent-unit-economics-and-cogs`** — Agent COGS waterfall: LLM tokens × steps × parallel branches + tool invocations × tool cost + external API + retry overhead + supervision overhead; agent gross margin; cost-per-task; **cost-per-resolved-task (the true unit)**. Sits on top of `saas-ai-unit-economics-and-cogs`. **Why:** AI unit economics models per-query / per-tenant cost but does not model the multi-step, multi-tool, multi-branch reality of agentic products where one user request can be 30+ LLM calls.

### Section 07 — Marketing & Sales Strategy

2. **`saas-agent-pricing-strategy`** — Pricing patterns: per-resolution / per-outcome / per-step / per-agent / hybrid; success-based pricing; intervention-credit reduction; vendor-cost-pass-through; price-corridor analysis; SLA-tied price. **Why:** AI pricing skill covers tier × allowance × overage; agent pricing must additionally treat **success-conditional pricing** and **intervention credits** as primitives.

### Section 03 — Products & Services

3. **`saas-agent-product-strategy-and-roadmap`** — Agent capability ladder (assist → suggest → supervise → agentic), autonomy progression with gates, build / buy / host of orchestration framework, vertical agent libraries, tool-registry strategy, eval-driven product development for agents specifically. **Why:** AI product strategy covers feature roadmap; agent product strategy must add the **autonomy ladder** as a first-class plan element.

### Section 06 — Competitive Analysis

4. **`saas-agent-moat-and-wrapper-risk`** — Agent moats (proprietary tools, proprietary action data, integration depth, eval-loop, customer-trust, regulatory clearance) **versus wrapper risk** (commoditisable by foundation provider next quarter, replaceable by next-gen model, generic prompt cleverness). The **"is your agent a moat or a wrapper" rubric** with a 7-question test. **Why:** AI moat skill covers data / workflow / distribution / cost / brand / regulatory / switching-cost; agent moat must explicitly model the **wrapper-risk-from-foundation-provider** vector and the proprietary-tool-and-action-data vector.

### Section 12 — Risk Analysis

5. **`saas-agent-risk-and-stress-test`** — Agent risk register (autonomy-action incident, **irreversibility incident**, regulatory action, talent flight of AI Safety Lead, foundation-model deprecation breaking agent, multi-agent collusion / loop, tool-vendor outage, prompt-injection escalation, action-auth bypass); stress tests (intervention rate spikes 2×; irreversibility incident scale; LLM provider 5× price; tool-vendor outage; FX shock on USD agent-spend). **Why:** AI risk register covers cost / model / data / vendor / regulatory; agent risk must add **autonomy and irreversibility** as their own categories.

### Section 09 — Management & Team

6. **`saas-agent-talent-strategy`** — Agent team composition (Agent Architect, Tool Engineer, Eval Engineer, **AI Safety Lead — mandatory**, HITL Designer, MLOps, Forward Deployed Engineer); African talent map for agent skills; comp benchmarks; retention plan; build-vs-buy of supervisors and supervisory infrastructure. **Why:** AI talent skill covers ML engineer / AI product manager / prompt engineer; agent talent makes the AI Safety Lead **mandatory** and adds the agent-specific roles.

### Section 11 — Funding Request

7. **`saas-agent-funding-stage-playbook`** — Agent business at pre-seed → seed → A → growth; investor archetypes for agents (agent-specialist funds, vertical AI funds, climate-tech, sovereign-AI envelopes, DFI); use-of-proceeds patterns for agents (heavy on Tool Engineering, Eval, Safety vs heavy on GTM in normal SaaS); milestone breakpoints (first agent in supervised production; first agent in autonomous production; first cost-per-resolved-task under target; first audit clearance). **Why:** AI funding playbook covers AI-VC; agent funding has its own investor archetypes and use-of-proceeds shape.

### Meta-Skills

8. **`meta-agent-bankability-and-investor-readiness`** — Agent-specific bankability scorecard: unit-economic discipline (cost per resolved task), moat-vs-wrapper, governance maturity (kill-switch, audit log retention, drill cadence), safety / red-team practice, regulatory readiness, talent depth (AI Safety Lead in seat?), KPI maturity (intervention rate measured?). **Why:** AI bankability scorecard covers AI-cost / eval / hallucination; agent bankability adds the autonomy-governance and wrapper-or-moat dimensions.

9. **`meta-agent-valuation-adjustments`** — **Agent premium** (when defensible) **vs wrapper discount** (when not); per-resolution-economics premium; intervention-rate-tied valuation; comparable transactions in agent space; foundation-model-platform-risk overlay; multi-agent governance discount when uncontrolled. **Why:** AI valuation adjustments cover AI premium / discount in aggregate; agent valuation requires a separate module because agent businesses span a range from "genuinely defensible vertical agent" to "GPT prompt wrapper" with **wildly different multiples**.

10. **`meta-agent-board-and-investor-reporting`** — Agent KPI section for monthly investor update + quarterly board pack (task success, intervention rate, irreversibility incidents, cost per resolved task, agent-revenue attribution, agent-incident log, safety-drill cadence, regulator engagement). **Why:** AI board reporting covers AI metrics; agent reporting must add the autonomy / incident / drill dimensions.

### Section 13 — Implementation Timeline

11. **`saas-agent-implementation-timeline`** — Agent rollout discipline tied to plan: **shadow → supervised → agentic** gates; eval-coverage gates; cost-gated agent launches; human-in-the-loop ramp-down; irreversibility-class-by-class autonomy expansion. **Why:** Generic implementation timeline does not encode autonomy-progression gates.

### Section 14 — AI Integration

12. **`saas-agent-integration-deep`** — Agent layer atop AI integration: how the plan treats agents as a distinct product class; integration with AI Integration skill; positioning vs AI-as-feature; deep links to all agent-specific skills. **Why:** Section 14 currently treats AI homogeneously; agents need their own deep treatment within or alongside it.

### Section 16 — Sustainability Strategy

13. **`saas-agent-sustainability-and-ethics`** — Agent-specific ethics (**action accountability**, **human-final for irreversibility**, audit log retention, contestability / redress, jobs-impact disclosure if proposed in regulated markets); compute sustainability (multi-step inflation of energy per task); local-language and access ethics. **Why:** AI ethics covers fairness / transparency / consent / provenance; agent ethics must add action accountability and irreversibility ethics.

---

## Part 3 — ENHANCEMENTS to Existing Skills (reference files)

| Section | Reference to add | Purpose |
|---|---|---|
| `01-executive-summary` | `saas-agent-executive-summary-block.md` | Agent paragraph: capability, autonomy level, moat, intervention rate, milestones, ask |
| `04-market-analysis` | `agent-tam-discipline.md` | Agentic-tasks-served TAM, NOT just LLM TAM; "actions" not "queries" as the unit |
| `06-competitive-analysis` | `agent-moats-vs-wrapper-risk.md` | Compact rubric for moat vs wrapper diagnosis |
| `07-marketing-sales-strategy` | `agent-pricing-and-positioning.md` | Pricing patterns + positioning ("we charge per resolved ticket, not per seat") |
| `08-operations-plan` | `agent-operations-runbook-summary.md` | Kill-switch, audit cadence, drill cadence, incident runbook |
| `10-financial-projections` | (cross-reference to new agent unit economics skill) | Point existing SKILL.md to agent UE |
| `11-funding-request` | `saas-agent-investor-update-block.md` | Agent KPIs in monthly investor update |
| `12-risk-analysis` | `saas-agent-risk-register-template.md` | Populated agent risk register |
| `14-ai-integration` | overhaul SKILL.md to add agent overlay | Agents as distinct class |
| `16-sustainability-strategy` | `agent-ethics-and-sustainability-block.md` | Action accountability + irreversibility ethics |
| `meta-bankability-scoring` | `saas-agent-bankability-checklist.md` | Agent items in bankability scorecard |
| `meta-valuation` | `saas-agent-valuation-adjustments.md` | Premium / wrapper-discount module |
| `meta-due-diligence` | `saas-agent-data-room-contents.md` | Agent-specific DD checklist |
| `meta-financial-stress-test` | `saas-agent-stress-test-scenarios.md` | Quantified agent stress scenarios |
| `meta-living-plan-governance` | `agent-cadence-table.md` | Agent KPI cadence (weekly task success / intervention / cost; monthly irreversibility / audit / drill; quarterly moat / autonomy expansion / regulatory) |
| `meta-board-and-investor-reporting` | Agent Section clause + cross-reference | Agent section template |
| `country-context/africa-regional/africa-ict-saas-market-context.md` | Append Agent section | Public-sector agents, talent realities, sovereign-AI for agents |
| `saas-ai-cost-of-tenant-calculator` | Agent extension (steps × tools dimension) | Per-tenant cost when agent runs many steps |

---

## Part 4 — REFERENCE FILES / TEMPLATES / MODELS to Add

Each in the most relevant skill's `references/` folder unless cross-cutting.

1. `saas-agent-unit-economics-template.md` — LLM steps × parallel × tools + retries; agent GM; cost per resolved task; sensitivity matrix.
2. `saas-agent-cost-per-task-calculator-spec.md` — formula and worksheet spec; how to build the calculator.
3. `saas-agent-pricing-architecture.md` — per-resolution / per-outcome / per-step / hybrid; intervention-credit reduction; SLA-tied price; price-corridor.
4. `saas-agent-moats-and-wrapper-risk-checklist.md` — 7-question moat-vs-wrapper rubric.
5. `saas-agent-risk-register-template.md` — populated risk register.
6. `saas-agent-stress-test-scenarios.md` — quantified scenarios (intervention 2×, irreversibility incident scale, provider 5×, tool outage, FX shock).
7. `saas-agent-funding-stage-playbook.md` — stage-by-stage agent funding.
8. `saas-agent-investor-update-block.md` — monthly investor update agent section.
9. `saas-agent-board-pack-section.md` — quarterly board pack agent section.
10. `saas-agent-valuation-adjustments.md` — premium / wrapper discount.
11. `saas-agent-talent-and-org-design-template.md` — team composition by ARR / autonomy level.
12. `agent-tam-discipline.md` — agentic-tasks-served TAM.
13. `agent-ethics-and-sustainability-block.md` — Section 16 block.
14. `agent-cadence-table.md` — living-plan cadence specifically for agent KPIs.
15. `africa-agent-context-extension.md` — Africa-agent extension.
16. `saas-agent-data-room-contents.md` — agent DD checklist.
17. `saas-agent-bankability-checklist.md` — agent bankability scorecard.
18. `agent-pricing-and-positioning.md` — positioning discipline.
19. `agent-operations-runbook-summary.md` — kill-switch, audit, drill cadence.
20. `saas-agent-executive-summary-block.md` — exec-summary agent paragraph.

---

## Part 5 — The Living-Plan Agent Cadence (engine-wide standard)

Every agent-product plan must encode this cadence in addition to standard living-plan and AI-living-plan cadence:

| Agent element | Cadence | Owner | Variance threshold | Trigger-replan condition |
|---|---|---|---|---|
| Task success rate (per agent) | weekly | Head of Agent / Eval Engineer | -3pp | -5pp in single week |
| Intervention rate (HITL takes over) | weekly | HITL Designer + Head of Agent | +3pp | +5pp sustained 2 weeks |
| Cost per resolved task | weekly | CFO + Head of Agent | +15% WoW | +30% WoW |
| Irreversibility-class incidents | continuous + monthly | AI Safety Lead | any sev-1 | sev-1 = immediate re-plan |
| Audit-log review | monthly | AI Safety Lead + Compliance | missed review | sev-1 finding |
| Red-team / safety drill | monthly | AI Safety Lead | missed drill | drill exposes critical gap |
| Tool-invocation reliability (per tool) | weekly | Tool Engineer | tool error >2% | tool outage / 5xx surge |
| Branch-explosion / loop detection | weekly | Eval Engineer | branch count >ceiling | runaway loop |
| Agent-revenue attribution | monthly | CFO | -10% of attributable revenue | -20% |
| Foundation-model deprecation / migration | monthly | Head of AI / CTO | provider notice | deprecation announced |
| Regulator engagement / watch | quarterly | Compliance + Legal | new rule | active enforcement vs analogue |
| Moat-vs-wrapper reassessment | quarterly | CEO + Head of Strategy | foundation-model commoditises step | provider absorbs orchestration |
| Autonomy expansion review | quarterly | AI Safety Lead + Head of Agent + CEO | proposed level-up | irreversibility class added |
| AI Safety Lead retention | quarterly | Head of People + CEO | flight risk signal | departure |
| Customer-contestability requests | monthly | Compliance | request rate trend | rate spike |

---

## Part 6 — Africa-Agent Context (summary; full text in extension reference)

- **Public-sector agents** — KE Huduma / e-Citizen automation, NG NIMC / NIN identity assistance, ZA SARS / Home Affairs assistive agents, RW Irembo and government services automation, UG NITA-U e-Government — significant 2025-2030 demand for agentic interfaces to public services; sovereign-AI residency mandatory.
- **Vertical agents in Africa** — agri-extension agents (smallholder advisory via WhatsApp / USSD), fintech-collections agents (PAR>30 case management), healthtech triage agents (CHW support), edutech tutoring agents (in local languages), legal-aid agents (paralegal assistance).
- **Talent realities for agent engineering** — Agent Architects scarce; Tool Engineers scarce; Eval Engineers extremely scarce; AI Safety Leads almost non-existent in-region (consider remote-first or fractional). Carnegie Mellon Africa, ALU AI track, Andela AI pool, Deep Learning Indaba alumni are starting points; Lelapa AI, Awarri, EqualyzAI as local AI-employer precedents.
- **Sovereign-AI for agents** — RW innovation envelopes, KE Talanta AI / Konza initiatives, NG NITDA NAIS implementation, ZA Presidential 4IR Commission, EG national AI infra; agents serving public sector often need in-country compute (af-south-1, MainOne, Liquid, Cassava, Raxio, Ethiopian AI Institute).
- **Channel realities** — agent UX in Africa is **multichannel-first** (WhatsApp Business API, USSD, SMS, voice-IVR, mobile-money interface); a chat-only agent design loses 60–80% of the addressable user base.
- **FX realities** — agent costs are USD (LLM + tools); revenue often local currency. Per-resolved-task pricing must include FX corridor headroom.
- **Regulatory environment for agents** — KE ODPC, NG NDPC, ZA Information Regulator, RW NCSA, UG NITA-U / PDPO are evolving AI-action accountability expectations; high-stakes agentic action in regulated sectors (finance, health, public service) requires documented HITL and audit trail.
- **DFI / grant funding for agents** — IFC AI envelopes, AfDB AI-for-development, GSMA AI for Impact, Mozilla African Innovation Mradi, IDRC AI4D, Lacuna Fund (training data for agent supervision), Patrick J. McGovern Foundation; donor expectation increasingly for **human-final on irreversibility** as a funding condition.

---

## Part 7 — Priority Order

**Tier 1 (this session):**
- `saas-agent-unit-economics-and-cogs` + template
- `saas-agent-pricing-strategy` + architecture
- `saas-agent-moat-and-wrapper-risk` + checklist
- `saas-agent-risk-and-stress-test` + register + scenarios
- `saas-agent-talent-strategy` + team template
- `meta-agent-bankability-and-investor-readiness` + checklist
- `meta-agent-valuation-adjustments` + adjustments doc
- `meta-agent-board-and-investor-reporting` + investor-update + board-pack blocks
- `africa-agent-context-extension.md`
- Living-plan agent cadence wired into `meta-living-plan-governance`
- Agent exec-summary block; agent risk-register template

**Tier 2 (this session if budget allows):**
- `saas-agent-product-strategy-and-roadmap`
- `saas-agent-funding-stage-playbook`
- `saas-agent-implementation-timeline`
- `saas-agent-integration-deep` (or 14-ai-integration overhaul)
- `saas-agent-sustainability-and-ethics`
- Agent TAM discipline; agent pricing/positioning; agent operations runbook summary
- Bankability checklist (agent items); DD checklist; stress-test scenarios doc

**Tier 3 (next session):**
- Vertical-agent playbooks (agri-extension agent, fintech-collections agent, healthtech triage agent, edutech tutoring agent, legal-aid agent, public-sector citizen-service agent)
- AI-procurement for African public sector (sovereign-AI agent tendering)
- Multi-agent governance (federation, contractor-style agent marketplaces, agent-to-agent trust)
- Agent-incident postmortem template + library
- Agent regulator engagement playbook by country

---

## Part 8 — How this audit composes with the prior two

- Where **SaaS unit economics** had one AI cost line and **AI unit economics** decomposed it into a COGS waterfall, **agent unit economics** further decomposes per-task into steps × tools × branches × retries — and introduces **cost-per-resolved-task** as the true unit.
- Where **SaaS pricing** had per-seat / per-tier and **AI pricing** added allowance × overage × FX, **agent pricing** adds per-resolution / per-outcome / per-step and **intervention-credit reduction** as a primitive.
- Where **SaaS moat** ran a 5-question test and **AI moat** ran a 7-question test, **agent moat** runs an 8-question test that includes **wrapper risk from foundation provider** as its own dimension.
- Where **SaaS risk register** had AI cost spike as one bullet and **AI risk register** decomposed into 12+ failure modes, **agent risk register** adds **autonomy incidents and irreversibility incidents** as their own categories with explicit severity-class taxonomy.
- Where **SaaS valuation** had Rule-of-40 multiples and **AI valuation** applied premium / discount, **agent valuation** applies **premium when defensible vs wrapper discount when not** with a separate adjustment table.
- Where **SaaS bankability** had a scorecard and **AI bankability** added eval / hallucination / cost-engineering, **agent bankability** adds **autonomy-governance / safety practice / talent depth (AI Safety Lead in seat?)**.
- Where **SaaS living-plan cadence** had weekly KPIs / monthly cohorts and **AI living-plan cadence** added weekly evals / monthly per-tenant AI cost, **agent living-plan cadence** adds **weekly task success / intervention rate / cost-per-resolved**, **monthly irreversibility incidents / audit / drill**, and **quarterly moat / autonomy / regulator**.
- Where **SaaS board pack** had GTM / financial / risk and **AI board pack** added AI section, **agent board pack** adds intervention rate, irreversibility incidents, safety-drill cadence, and regulator engagement.

This audit is the work order. The session that follows executes Tier 1 in full and most of Tier 2.
