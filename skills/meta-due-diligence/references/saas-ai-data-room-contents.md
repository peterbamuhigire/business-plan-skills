---
source: 2024-2026 AI-investor diligence practice; NIST AI RMF; EU AI Act conformity assessment; engine synthesis
frameworks: [AI data-room sections; Document checklist; AI-specific DD questions investors ask]
skill: meta-due-diligence (cross-listed in meta-ai-bankability-and-investor-readiness)
cross-reference: [meta-ai-bankability-and-investor-readiness, saas-ai-risk-register-template, meta-ai-valuation-adjustments]
---

# SaaS AI Data Room — Contents Checklist

## 1. Why a separate AI section in the data room

Standard SaaS data rooms cover financials, customers, IP, legal, HR, technology. AI-aware investors and DFIs run a parallel AI-specific DD track. A SaaS plan that puts AI documents in an "IP" or "Technology" folder will signal immaturity. Provide a dedicated AI section.

## 2. The 9 AI data-room sections

### Section 1 — AI Architecture & Stack

- One-page architecture diagram (foundation models, embedding models, vector DB, router, eval, cache, observability, hosting regions)
- List of all foundation-model providers with current EULA reviewed dates
- Build-vs-buy decision log per component
- Multi-provider router policy
- Hosting-region map by tenant / by data class
- Disaster-recovery and AI-incident runbook

### Section 2 — AI Economics

- Per-tenant AI cost spreadsheet (from `saas-ai-cost-of-tenant-calculator`)
- AI COGS waterfall (from `saas-ai-unit-economics-and-cogs`)
- AI Gross Margin trajectory (12 months historical + 36 months projected)
- AI-cost-as-%-of-ARR trajectory
- Provider rate history (12 months) and re-pricing decisions
- Cache-hit ratio history
- Model-mix history

### Section 3 — Models & Data

- Model cards for any models you've trained or fine-tuned (Hugging Face / model-card format)
- Datasheets for training data (Gebru et al. format)
- Training-data provenance log (sources, licensing, consent, compensation, curation steps)
- Fine-tune training logs (when, what data, what eval improvement, what cost)
- Data classification (which data is PII / PHI / financial / biometric / sensitive)
- Data residency map (per tenant, per data class, per jurisdiction)
- Data retention policy
- Data deletion / right-to-be-forgotten process

### Section 4 — Eval & Quality

- Eval suite description (what's covered, coverage %, sample size, refresh cadence)
- Eval results history (12 months)
- Production sampling rate
- Hallucination-rate measurement methodology
- Hallucination-rate trajectory
- Human-in-loop policy for high-stakes decisions
- Quality SLA per tier (if customer-facing)
- Eval-failure incident log

### Section 5 — Governance & Ethics

- AI policy (current version + version history)
- AI governance committee charter (composition, RACI, decision authority, cadence)
- AI governance committee minutes (last 12 months)
- AI ethics framework (fairness, transparency, redress, consent, downstream-misuse)
- Bias audit reports (last 12 months)
- AI compliance posture per jurisdiction (EU AI Act category if applicable, NIST AI RMF mapping, KE / NG / ZA / RW / UG AI framework alignment)
- AI-incident log (sev-1 + sev-2 history; root causes; remediation)
- AI-incident runbook
- Customer indemnification posture
- AI insurance coverage (E&O, cyber-liability with AI rider)

### Section 6 — AI Risk

- AI risk register (from `saas-ai-risk-register-template`)
- AI stress-test scenarios (from `saas-ai-stress-test-scenarios`)
- Vendor concentration analysis (% AI cost / capability by provider)
- Foundation-model platform-risk statement
- FX exposure analysis on AI cost
- Liability reserve adequacy

### Section 7 — AI Talent

- AI org chart (current + plan)
- AI hiring plan
- AI team retention metrics (12 months)
- Key-person dependency identification + mitigation
- AI training / upskilling spend
- Diversity / inclusion metrics for AI team
- AI advisor / board / external-expert relationships

### Section 8 — AI Sustainability

- AI energy / carbon / water estimates (from `saas-ai-sustainability-and-ethics`)
- Hosting-region carbon intensity
- Sustainability KPI dashboard
- Embodied-carbon accounting
- TCFD-aligned climate disclosures (if any)

### Section 9 — AI Commercial

- AI feature roadmap (with cost gating)
- AI feature adoption metrics (per tier, per feature)
- AI revenue attribution methodology
- AI-attributable revenue history
- AI-influenced retention / expansion analysis
- Customer-AI-success case studies
- Competitive AI-claim watch (competitor analysis with AI focus)

## 3. The 30 AI-specific DD questions to expect

1. What's your AI architecture? Diagram?
2. Which foundation-model providers? What's your multi-provider strategy?
3. What's your per-tenant AI cost? Median? Top decile?
4. What's your AI Gross Margin? Trajectory?
5. What's your AI-cost-as-%-of-ARR? Trajectory?
6. What's your cache-hit ratio?
7. What's your model-mix policy?
8. What's your eval coverage? How is it measured?
9. What's your hallucination rate? How is it measured?
10. What's your production sampling rate?
11. What happens if [provider] doubles pricing?
12. What happens if [provider] deprecates your primary model?
13. What's your model-migration playbook?
14. What's your hallucination-liability reserve? How is it sized?
15. What's your AI-incident protocol? Show me the runbook.
16. Has there been any AI incident? Severity? Resolution?
17. What's your training-data provenance? Show me the log.
18. Are you exposed to any training-data lawsuit?
19. What's your data residency posture by jurisdiction?
20. What's your AI policy? Show me the current version.
21. Does an AI governance committee operate? Show me minutes.
22. What's your fairness / bias audit history?
23. What's your AI talent retention?
24. Who is your AI lead? What if they leave?
25. What's your vendor concentration on AI providers?
26. What's your FX exposure on USD AI cost? Mitigation?
27. What's your eval pipeline? Coverage? Cadence?
28. What's your AI feature roadmap? Cost gating per feature?
29. What's your AI compliance posture? Per jurisdiction?
30. What % of revenue is genuinely AI-attributable? How do you measure?

## 4. Anti-patterns the DD will catch

- "AI architecture" diagram drawn on demand (not living)
- AI cost stated without per-query / per-tenant decomposition
- Eval coverage stated without methodology
- Hallucination rate "we don't measure"
- No model migration plan
- Training-data provenance "we use public data" with no documentation
- Single-provider AI dependency with no mitigation
- "We're working on AI governance" (not operating)
- AI committee in draft (not meeting)
- AI revenue attribution = total revenue (over-claiming)
- No AI-incident protocol; no log

## 5. Maturity tiers (investor uses this internally)

| Tier | Description | Typical investor reaction |
|---|---|---|
| Tier 1 — Toy AI | LLM wrapper; no measurement; no governance | "Pre-seed at best; AI premium can't apply" |
| Tier 2 — Working AI | Production AI; minimal measurement; reactive governance | "Seed-able; AI discount may apply" |
| Tier 3 — Engineered AI | Multi-provider, evals, cost engineering, basic governance | "Series A bankable; neutral AI overlay" |
| Tier 4 — CFO-grade AI | Full DD pack as above; mature governance; quantified risk; AI-team retention | "Series B-grade; AI premium plausible" |
| Tier 5 — Institutional AI | External audit + ISO 42001 / SOC 2 with AI; regulator-engaged | "Growth-stage; substantial AI premium" |

The plan should declare which tier it claims and present evidence accordingly.

## 6. Africa / Uganda specifics

- DFI data rooms expect ESG / IFC PS alignment in the AI section (sustainability, ethics, gender, inclusion, theory-of-change)
- Sovereign-AI tender data rooms expect data residency proof, local-talent evidence, local-language coverage, regulator-engagement evidence
- AI-for-good grant data rooms expect theory-of-change, training-data provenance audit, community-benefit measurement, sustainability beyond grant
- For African enterprise customers, customer data-room expectations include local data residency, in-country support, regulatory compliance evidence
