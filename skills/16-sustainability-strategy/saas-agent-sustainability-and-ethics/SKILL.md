---
name: saas-agent-sustainability-and-ethics
description: Agent-specific ethics (action accountability, human-final on irreversibility, audit-log retention, contestability / redress, jobs-impact disclosure) and sustainability (multi-step compute inflation, energy per resolved task, local-language and channel access ethics). Sits on top of `saas-ai-sustainability-and-ethics`.
---

# SaaS Agent Sustainability & Ethics Skill

## Overview

AI ethics (handled by `saas-ai-sustainability-and-ethics`) covers fairness, transparency, consent, provenance, redress, downstream-misuse. **Agent ethics** must additionally address:

1. **Action accountability** — when the agent acts, who is accountable for the consequence?
2. **Human-final on irreversibility** — Class D actions require human-final; this is an ethical commitment, not just a risk control
3. **Audit-log retention and queryability** — the agent must be auditable end-to-end for every action
4. **Contestability / redress** — affected parties must have a way to challenge agent action and receive remediation
5. **Jobs-impact disclosure** — in markets with high formal-sector unemployment or in regulated contexts, jobs-impact disclosure is increasingly an ethical and funding requirement
6. **Multi-step compute sustainability** — agents inflate compute per task; energy footprint scales accordingly

## Use When

- Section 16 is being built for an agent-product plan
- ESG / IFC Performance Standards alignment required
- DFI / multilateral funding with social / environmental requirements
- Public-sector deployment in regulated markets
- The plan must pass `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- The product is AI-feature only without agentic action — use `saas-ai-sustainability-and-ethics`
- The agent is internal-efficiency only with no customer-facing action — generic Section 16 plus AI ethics is sufficient
- The plan is too early (pre-PMF) for full ethics-and-sustainability commitment — note the direction and the gating thresholds for adopting full discipline

## Required Inputs

- Agent action taxonomy (A/B/C/D)
- Customer-facing impact
- Jobs-impact estimate (if applicable)
- Energy per task estimate
- Channel mix
- Local-language coverage
- Affected-party demographics
- Insurance / indemnity coverage

## Workflow

1. **Action-accountability declaration** — for each action class, who is the accountable party? Vendor (you), customer (your customer), end-user, or shared? Document in customer contract, in regulator submissions, in audit-log schema.
2. **Human-final commitment on Class D** — declare explicitly. Document the human-final UX, the double-signing, the audit. Non-negotiable.
3. **Audit-log retention and queryability** — declare retention period (typically 3-7+ years for regulated; longer if sectoral), queryability standard (regulator-on-demand), immutability mechanism.
4. **Contestability / redress workflow** — affected party submits request; SLA for response; remediation options; escalation path. Document the workflow and the workforce.
5. **Jobs-impact disclosure** — if agent displaces or substantially modifies roles, disclose transparently. Re-skilling / redeployment commitment where applicable. Engage labour representatives in regulated sectors.
6. **Sustainability KPIs:**
   - Energy per resolved task (kWh or equivalent)
   - Water for cooling (where in-region inference)
   - Embodied carbon contribution
   - Multi-step compute inflation vs single-shot LLM baseline
   - Cache-hit ratio (sustainability win)
   - Model-mix downshift (sustainability win)
   - In-region inference vs cross-region (latency + footprint trade-off)
7. **Local-language and channel-access ethics** — agents should serve the languages and channels their users actually use; English-only chat-only is an accessibility failure in African markets.
8. **Provenance** — training-data provenance audited; customer-data not used for cross-customer training without explicit consent.
9. **Downstream-misuse risk** — acceptable-use policy; abuse detection; rate-limit; kill-switch.
10. **Insurance + indemnity alignment** — ethical commitments backed by insurance / reserve where applicable.
11. **External review / certification** — consider third-party AI ethics review for vertical / regulated agents.
12. **Wire to bankability** — `meta-agent-bankability-and-investor-readiness` consumes ethics evidence.

## Quality Bar

- Action-accountability declared per class
- Human-final on Class D non-negotiable and documented
- Audit-log retention + queryability declared
- Contestability / redress workflow operational
- Jobs-impact disclosed where applicable
- Sustainability KPIs measured and reported
- Local-language and channel coverage stated as ethics commitment
- Training-data provenance audited
- Downstream-misuse controls operational
- Cross-referenced to bankability, board reporting, risk

## Anti-Patterns

- "Customer is responsible for the action" without contract clarity
- Class D agentic without human-final
- Audit-log only for engineering debugging; not regulator-acceptable
- No contestability workflow
- Jobs-impact ignored in public-sector deployments
- Sustainability KPIs absent
- English-only agent in multi-lingual market positioned as "AI for everyone"
- Customer-data quietly used for cross-customer training
- Downstream-misuse not monitored

## Outputs

- Action-accountability matrix (per class)
- Human-final policy on Class D
- Audit-log retention + queryability spec
- Contestability / redress workflow
- Jobs-impact disclosure (where applicable)
- Sustainability KPI set with baselines and targets
- Local-language and channel ethics commitment
- Training-data provenance audit
- Downstream-misuse controls
- Insurance + indemnity alignment
- External-review / certification posture

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Audit-log review | monthly | Compliance + AI Safety | findings |
| Contestability request response | continuous | Compliance | SLA breach |
| Jobs-impact tracking | quarterly | CEO + HR | shift in impact |
| Sustainability KPIs | quarterly | Sustainability lead + CTO | regression |
| Training-data provenance audit | quarterly | Head of AI | new data source |
| Misuse detection report | monthly | AI Safety + Compliance | trend up |
| External review cadence | annual | CEO + Compliance | finding |

## References

- `references/agent-ethics-and-sustainability-block.md` — Section 16 block template (also lives at `16-sustainability-strategy/references/`)
- `skills/16-sustainability-strategy/saas-ai-sustainability-and-ethics/SKILL.md` — AI parent
- `skills/16-sustainability-strategy/SKILL.md` — generic
- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — risk
- `skills/meta-agent-bankability-and-investor-readiness/SKILL.md` — bankability
- `book-extractions/agent-products-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Jobs-impact in African public-sector deployments** is politically and reputationally consequential; transparent disclosure and re-skilling commitment increasingly required by donors / multilaterals / regulators
- **Local-language coverage as ethics** — agents serving African end-users that don't cover Swahili / Hausa / Yoruba / Amharic / Luganda / Zulu / Xhosa / Wolof / Tigrinya / Lingala have accessibility gaps; commit to coverage roadmap
- **Channel ethics** — chat-only excludes non-smartphone / unbanked users; commit to USSD / SMS / IVR coverage in mass-market deployments
- **Contestability in low-literacy or low-access contexts** — design redress workflows that work in vernacular, via voice, via in-person mediation when needed
- **Training-data provenance** — African-language data must be sourced with consent and proper licensing (Lacuna Fund standards, Masakhane practices); commercial use of community-built data requires explicit terms
- **Sovereign-AI / residency** — for sustainability, in-region inference reduces network footprint and supports local data-centre demand; consider as positive sustainability story (paired with grid-energy considerations)
- **Insurance / indemnity** — thin in African markets; ethical commitments must be backed by reserve when insurance is not available
- **External review** — Africa AI Safety Consortium, Lelapa AI partners, Mozilla African Innovation Mradi, university ethics boards are options for third-party review
- **Sectoral ethics** — health (UMDPC / KMPDC / HPCSA / Pharmacy Councils), finance (BoU / CBK / CBN / SARB / FSCA / BNR), legal (LSK / SCUEA / Law Society SA / NBA) have sector-specific ethics expectations
