---
source: Mersch ch. 11; engine synthesis; 2024-2026 AI-investor stress-test practice
frameworks: [6 quantified AI stress scenarios; Cash / margin / runway impact; Mitigation playbook; Reconciliation to plan]
skill: meta-financial-stress-test (cross-listed in saas-ai-risk-and-stress-test)
cross-reference: [saas-ai-unit-economics-and-cogs, saas-ai-risk-register-template, meta-financial-stress-test]
---

# SaaS AI Stress-Test Scenarios

## 1. The six canonical AI stress scenarios

Every AI-feature-led SaaS plan should run these six scenarios through `meta-financial-stress-test`. Each scenario must produce:
- Quantified impact on AI Gross Margin, AI-cost-as-%-of-ARR, blended GM, runway, NRR
- Cash-impact in one-time vs ongoing terms
- Mitigation playbook with expected effectiveness
- Recovery time
- Living-plan trigger

### Scenario 1 — AI Cost Spike (provider doubles premium-model pricing)

**Trigger:** OpenAI / Anthropic raises premium-model output rate 100% (recent precedent: GPT-4-Turbo → GPT-4o premium tier introductions)

**Quantification:**
- If premium-model share is 50% of AI cost: total AI cost +50%
- AI GM drops ~10-15pp
- AI-cost-as-%-of-ARR rises ~5-10pp
- Runway impact: at $5M ARR with AI 12% of revenue, monthly burn rises ~$25,000-50,000

**Mitigation playbook:**
1. Immediate: aggressive cache (target +15pp cache-hit ratio); expected impact -10-15% of premium cost
2. Within 30 days: model-mix downshift on non-critical queries; expected -20-30% of premium cost
3. Within 90 days: distilled model deployment for high-volume routine queries; expected -50-70% of premium cost on routed share
4. Within 180 days: pricing pass-through where contracted (overage rates re-set); revenue +1-3%

**Recovery time:** 3-6 months to restore AI GM trajectory

**Trigger-replan:** declare cost-spike scenario; refresh Section 10; communicate to board

### Scenario 2 — Model Deprecation (forced migration in 6 months)

**Trigger:** Provider announces deprecation of model X with 6-month notice (recent precedent: GPT-3.5 → GPT-4, Claude 2 → Claude 3 transitions)

**Quantification:**
- One-time migration cost: $50,000-200,000 (eval re-run, prompt re-engineering, customer comms, regression hunting)
- Productivity hit on AI engineers: ~30% capacity for one quarter
- Eval-suite re-build cost
- Possible quality regression in production for 1-4 weeks
- Possible churn from customers if quality regresses (~0.5-2% incremental)

**Mitigation playbook:**
1. Multi-provider router already in place: migration is feature-flag flip
2. If single-provider: emergency dual-provider build; 2-4 weeks
3. Eval-suite comparison: production-sample comparison between old and new model
4. Customer comms: proactive notice; SLA preservation
5. Reserve drawdown: model-migration reserve covers one-time cost

**Recovery time:** 1-2 quarters

**Trigger-replan:** migration project added to MSPOT Projects; risk register updated

### Scenario 3 — Hallucination Event (production incident in regulated vertical)

**Trigger:** AI produces wrong answer with material customer harm (e.g. wrong medication dosage recommendation; wrong financial advice; wrong legal interpretation; wrong public-sector eligibility decision)

**Quantification:**
- Direct liability: legal cost $50,000-500,000; settlement $0-5M depending on severity and jurisdiction
- Reserve drawdown: full reserve allocation
- Customer churn: 5-25% in affected segment over 6 months
- Regulator notification: KE DPC / NG NDPC / ZA Info Regulator / UG NITA-U / EU AI Act authority
- Public-relations cost
- Eval coverage expansion mandatory

**Mitigation playbook:**
1. Pre-incident: hallucination-liability reserve adequate (3-6% of AI revenue accruing); insurance evaluated
2. Sev-1 protocol: immediate disable + human-in-loop + customer comms
3. Forensic: root cause + eval gap identification
4. Remediation: eval extension + monitoring + governance review
5. Communication: board comms + regulator + customers + public if material

**Recovery time:** 6-12 months for trust restoration; 12-18 months for churn unwind

**Trigger-replan:** AI governance committee emergency session; eval-coverage roadmap accelerated; reserve replenishment plan

### Scenario 4 — Data-Rights / Training-Data Lawsuit

**Trigger:** training-data provenance challenged (precedent: NYT v OpenAI, Getty v Stability, Authors Guild v OpenAI), or provider's EULA changes to expose customer

**Quantification:**
- If you trained: legal cost $200,000-2M; settlement risk; possible injunction
- If provider sued: forced model switch; migration cost as Scenario 2; possible customer concerns
- Insurance: model-specific E&O premiums rising

**Mitigation playbook:**
1. Pre-incident: training-data provenance audit; consent + licensing documented; switch to documented-corpus models where possible
2. EULA-shock: monitor provider EULA changes monthly; rapid migration if EULA-incompatible
3. Customer indemnification posture: review and adjust

**Recovery time:** 6-18 months

**Trigger-replan:** provenance audit reviewed; legal counsel engaged; provider mix revisited

### Scenario 5 — GPU Scarcity / Sovereign-AI Tender Loss

**Trigger:** Anchor tender lost to in-country competitor with sovereign-AI advantage; or GPU capacity in af-south-1 / africa-south1 / Liquid / Cassava reduces to under-needed levels; or in-country compute requirement imposed by regulator (precedent: emerging in KE, NG, RW, EG)

**Quantification:**
- Tender loss: $X annual revenue
- Capacity reduction: queue / wait times rise; user experience degrades; ~2-5% churn risk
- Forced in-country deployment: one-time $100,000-1M build-out + ongoing premium hosting cost

**Mitigation playbook:**
1. Tender pre-loss: in-country compute path designed; pilots running
2. Tender lost: pipeline diversification; competitive intelligence on win
3. Capacity reduction: multi-region; cloud failover
4. Forced in-country: infra build accelerated; ESG / DFI funding for compute build-out

**Recovery time:** 6-24 months depending on cause

**Trigger-replan:** sovereign-AI strategy refresh; in-country compute decision

### Scenario 6 — FX Shock (local currency -20% vs USD)

**Trigger:** NGN-style devaluation; or KES / UGX / ZAR / GHS / EGP material move

**Quantification:**
- USD AI cost unchanged; local-currency revenue stable; AI-cost-as-%-of-ARR rises by FX % × USD share of cost
- For a plan with 60% of AI cost USD-denominated and 100% local revenue, 20% FX move means ~12% rise in AI-cost-as-%-of-ARR
- AI GM drops 5-10pp
- Runway impact in local terms unchanged; in USD terms compressed
- Pricing pass-through possible but takes 30-90 days with customer comms

**Mitigation playbook:**
1. Pre-shock: FX corridor and re-pricing trigger in pricing architecture; 10-15% FX headroom in pricing
2. Shock event: re-price triggered (announced 30 days; effective 60 days); usage caps tightened
3. Cost engineering accelerated: cache + model-mix + local-model substitution
4. Contracts re-papered to include FX adjustment clauses going forward

**Recovery time:** 1-2 quarters

**Trigger-replan:** Section 10 refreshed; pricing communicated; customer impact monitored

## 2. Combined-shock scenarios (the "perfect storm")

For DFI / Series B+ diligence, run combined scenarios:

**Combined A: Cost spike + FX shock simultaneously**
- AI-cost-as-%-of-ARR could double in worst case
- Margin compression severe; runway impact significant

**Combined B: Model deprecation + cost spike on new model**
- One-time migration cost + ongoing higher COGS
- 6-12 month recovery

**Combined C: Hallucination event + regulatory shift**
- Liability cost + compliance build-out + churn
- 12-24 month recovery

## 3. Scenario reporting format (for the plan)

Each scenario reported as a one-pager with:
- Headline: scenario name
- Trigger: explicit event
- Quantification table: ARR impact, GM impact, cash impact, runway impact, NRR impact
- Mitigation playbook: numbered actions with expected effectiveness
- Recovery time
- Trigger-replan condition
- Living-plan owner

## 4. Living-Plan Cadence

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Stress-test scenario refresh | quarterly | CFO + Head of AI | new scenario emerges |
| Provider price watch | monthly | Head of AI / CTO | any change |
| FX corridor | monthly | CFO | move >5% |
| Reserve adequacy | quarterly | CFO | drawdown event or coverage gap |
| Combined-shock scenario | semi-annual | CFO + CEO | strategic shift |

## 5. Africa-specific stress overlays

- **NGN-style devaluation**: model 30-50% local-currency shock; plan must survive at least 6 months at that level
- **Mobile-money payment rail outage** simultaneous with AI cost spike: cash flow + margin double-hit
- **Sovereign-AI policy shift** (forced in-country) — model the build-out as a fundable event, not a unfundable shock
- **Anchor public-sector tender loss** — if a single tender is >20% of ARR, plan must survive its loss
- **Regulatory enforcement** in regulated vertical (KE DPC, NG NDPC, ZA Info Regulator action on a competitor) — compliance investment shock
