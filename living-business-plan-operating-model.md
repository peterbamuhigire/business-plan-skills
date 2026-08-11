# Living Business Plan Operating Model — Engine-Root Reference

This document is the engine-wide canonical reference for how plans become and stay living documents. Every new and enhanced skill in the engine references this file. The full detail lives at `skills/meta-strategy/meta-living-plan-governance/references/living-business-plan-operating-model.md` and the operating skill at `skills/meta-strategy/meta-living-plan-governance/SKILL.md`.

## Why this matters

A business plan that gets approved and shelved is operationally dead. A plan that keeps running — updated with actuals, reviewed at cadence, with explicit decision logs and trigger-replan events — is operationally alive and continues to create value across the lifetime of the business.

For SaaS / ICT plans specifically, the world changes faster than annual planning can absorb:
- Pricing experiments resolve in weeks
- Channel performance shifts quarterly
- AI cost economics change every 6 months
- Competitor moves can invalidate strategy overnight
- African FX, regulation, and payment-rail policy can shift in days

This is why the living-plan discipline is a core engine standard.

## The six-component model

Every plan section must address:

1. **Data feed** — which KPI / metric / signal feeds this section
2. **Cadence** — weekly / monthly / quarterly / annual / trigger
3. **Owner** — which role on the team maintains it
4. **Decision log** — where material changes are recorded with reasoning
5. **Variance threshold** — at what plan-vs-actual gap is replan triggered
6. **Sunset policy** — when content is archived

## The artefacts

The living plan produces and maintains these artefacts:

- **MSPOT** (Mission / Strategy / Projects / Omissions / Tracking) — annual operating artefact
- **KPI dashboard** — weekly / monthly snapshot
- **Cohort retention matrix** — monthly refresh
- **ARR waterfall** — monthly refresh
- **Decision log** — continuous
- **Monthly investor update** — within 7 days of month-close
- **Quarterly board pack** — 5 days before board meeting
- **Risk register** — quarterly review
- **Customer-conversation digest** — quarterly synthesis from monthly interviews

## The cadence calendar

- **Daily / weekly**: KPI dashboard review; pipeline; cash; customer health alerts
- **Monthly**: Monthly Business Review (MBR); investor update; cohort analysis
- **Quarterly**: Quarterly Board Review (QBR); MSPOT projects status; OKR scoring; pivot-vs-persevere decision; risk register review
- **Annually**: full strategy refresh; new MSPOT; 3-year financial re-plan; team offsite; renewed Omissions list; archive snapshot
- **Trigger-replan events**: founder departure; >10% customer loss; FX shock >10%; regulatory shock; technology shock; funding round close; M&A activity

## Engine integration

Every plan section produced through this engine — by `00-client-intake` through `16-sustainability-strategy` and all `meta-*` skills — must conform to this operating model. The `meta-living-plan-governance` skill is the entry-point for installing this discipline in a plan.

When you write a section, ask: *"Six months from now, who refreshes this and how often?"* If the answer is "we'll figure it out later," the section isn't done.

See also:
- `skills/meta-strategy/meta-living-plan-governance/SKILL.md` — the skill
- `skills/meta-strategy/meta-living-plan-governance/references/living-business-plan-operating-model.md` — full reference
- `skills/meta-strategy/meta-living-plan-governance/references/saas-okr-and-kpi-tree-template.md` — OKR / KPI cascade
- `skills/meta-reporting/meta-board-and-investor-reporting/SKILL.md` — the reporting cadence
- `skills/meta-strategy/meta-quarterly-gameplan/SKILL.md` — the 90-day operating rhythm
- `skills/meta-strategy/meta-monitoring-evaluation/SKILL.md` — KPI / M&E discipline
- `book-extractions/cotton-run-a-saas-business-extraction.md` — MSPOT origin
- `book-extractions/haines-how-to-create-a-business-case-extraction.md` — post-implementation audit, decision-log discipline
