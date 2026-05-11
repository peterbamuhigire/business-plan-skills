---
name: meta-board-and-investor-reporting
description: Design the monthly investor-update + quarterly board-pack rhythm for a SaaS / ICT company. Specifies the KPI dashboard, narrative structure, decision-asks discipline, governance artefacts, and the cadence by which the board becomes a force-multiplier rather than an audit. Use when a SaaS company has external investors or is preparing to take them on.
---

# Board & Investor Reporting Skill

## Overview

Funded SaaS companies that fail to maintain investor confidence often had great plans and weak reporting. The board pack is the operating artefact of the living plan — it embodies what's working, what's broken, and what the company is asking the board to help with. This skill installs the canonical monthly investor update + quarterly board pack rhythm.

## Use When

- A SaaS company has external investors (priced round, SAFE notes outstanding, DFI partners)
- A company is preparing for a fundraise (boards expect this artefact)
- An existing board pack is ad hoc, late, or causing surprise
- Investors are asking for more transparent reporting

## Required Inputs

- Plan and operating metrics (from `saas-unit-economics-and-cohort-model`)
- MSPOT for the year (from `meta-living-plan-governance`)
- Decision log
- Board composition and term lengths
- Investor letter cadence expectations

## Workflow

1. **Set the monthly investor-update structure:**
   - One-line headline (top metric movement)
   - KPI snapshot (5-8 numbers)
   - Wins (3-5)
   - Losses / risks (2-4, honest)
   - Asks (where investors can help)
   - Cash position + runway
2. **Set the quarterly board-pack structure** (see references):
   - Cover + agenda
   - CEO letter (narrative)
   - Financial dashboard (P&L, cash, ARR waterfall, unit economics)
   - Operating dashboard (KPIs, cohorts, NPS, NRR)
   - Strategic discussion (1-3 decisions board needs to weigh)
   - HR / people / culture
   - Risk register update
   - Forward look (next quarter targets)
   - Appendix (deeper financials, customer wins, product roadmap)
3. **Install the cadence**:
   - Monthly investor update — within 7 business days of month-close, every month
   - Quarterly board pack — sent 5 business days before board meeting
   - Board meeting — 90-120 minutes, focused on strategy, not status (status was the pre-read)
4. **Define decision-ask discipline** — every board meeting should have 1-3 explicit decisions the board is asked to weigh in on; never use the board as a status audience.
5. **Tie to MSPOT** — the board pack mirrors MSPOT structure (Mission unchanged, Strategy progress, Projects status, Omissions confirmed, Tracking).
6. **Use the decision log** — major decisions log entries are board-pack content.
7. **Set up the data room** in parallel — keeps DD-readiness continuous, not just at fundraise time.
8. **Train the team** on board-pack content production — Finance produces financials, Heads produce operating dashboards, CEO writes the narrative.

## Quality Bar

- Monthly update delivered within 7 days every month — no exceptions
- Quarterly board pack delivered ≥5 days before board meeting
- KPI dashboard consistent month-over-month (no metric-substitution)
- Asks explicit; status implicit (no surprises)
- Honest about losses and risks (board will discover anyway)
- Decision log surfaces in the pack

## Anti-Patterns

- Slide deck only — no written narrative
- Highlights only — no losses / risks
- Different metrics each month (cherry-picking)
- Board meeting as status presentation, not decision forum
- Missing month-close discipline (Day 5 close discipline matters)
- Asks vague ("we'd appreciate any advice")

## Outputs

- Monthly investor-update template (filled or fillable)
- Quarterly board-pack template
- KPI dashboard standard
- Cadence calendar
- Decision-ask discipline
- Data-room structure

## AI Section (mandatory for AI-feature-led companies)

When AI is material to revenue or product, every quarterly board pack must include an AI section per `references/saas-ai-board-pack-section.md`. Every monthly investor update must include the AI block per `skills/11-funding-request/references/saas-ai-investor-update-block.md`. The AI section includes:
- AI KPI dashboard (AI-ARR, AI GM, AI-cost-%-of-ARR, eval coverage, hallucination rate, cache-hit, per-tenant cost, vendor spend, incidents)
- AI strategic decisions for board (1-3 explicit asks)
- AI risk register update
- AI roadmap progress with cost-gate decisions
- AI compliance and governance update
- Forward look (AI KPI targets + roadmap targets + top AI risk)

This sits alongside the financial dashboard and is treated as a first-class section, not as an appendix.

## References

- `references/saas-board-pack-template.md` — full template + worked example
- `references/saas-ai-board-pack-section.md` — AI section template for AI-feature-led companies
- `book-extractions/cotton-run-a-saas-business-extraction.md` — MSPOT and cadence
- `book-extractions/mersch-hacking-saas-extraction.md` — financial reporting standards
- `skills/meta-living-plan-governance/SKILL.md` — sister skill (this skill operationalises the living plan via investor reporting)
- `skills/meta-quarterly-gameplan/SKILL.md` — sister skill (quarterly operating rhythm)

## Africa / Uganda Application Notes

- DFI investors (IFC, FMO, BII, AfDB, Norfund, Proparco) require specific reporting formats — adopt theirs as the master template if DFI is on cap table.
- Many African boards are part-international, part-local — boards may be in 2-3 time zones. WhatsApp / Slack-asynchronous board engagement between meetings is normal.
- ESG / impact reporting is often required — embed in the quarterly pack rather than producing a separate report.
- FX volatility: include USD and local-currency views; explain FX impact separately from operational performance.
- Public-sector / NGO customer reporting: when these are >20% of ARR, include separate customer-concentration analysis.
- Board governance compliance: Ugandan Companies Act, Kenya Companies Act, South Africa Companies Act 2008 have specific board-resolution and minute-keeping requirements; embed in the cadence.
