# M&E Framework Document — Document Blueprint

The reusable architecture for a standalone Monitoring, Evaluation & Learning (MEL) Framework deliverable, grounded in results-based management practice (theory of change, results framework / logframe, OECD-DAC evaluation) and real Ugandan NGO M&E and financial-monitoring practice. Use the chapter→source map so M&E methodology always comes from the existing M&E skills and financial-monitoring substance always comes from the finance engine — never improvised.

M&E methodology roots: `business-plan-skills/skills/meta-strategy/meta-monitoring-evaluation`, `proposal-skills/skills/domain-delivery/monitoring-and-evaluation`.
Finance-engine root: `C:\wamp64\www\chwezi-accounting-doctrine` (paths below are relative to it).

## One document, layered logic

The MEL Framework is a single board/donor-owned deliverable, typically 25–60 pages. It moves from *why and what* (theory of change) to *what we will measure* (results framework and indicators) to *how we will measure and use it* (data management, calendar, roles, evaluation, reporting and learning), and closes by tying programmatic performance to financial absorption. Draft the theory of change first; every later chapter must trace back to it.

## MEL-framework chapter map (and where the substance comes from)

| # | Chapter | Substance from skill / reference |
|---|---------|----------------------------------|
| 1 | Introduction, purpose, scope, audiences, definitions | this blueprint; `proposal-skills/skills/domain-delivery/monitoring-and-evaluation` |
| 2 | Theory of change (pathways, assumptions, risks) | `meta-strategy/meta-monitoring-evaluation`; `proposal-skills/skills/domain-delivery/monitoring-and-evaluation` |
| 3 | Results framework / LogFrame (inputs → activities → outputs → outcomes → impact) | `meta-strategy/meta-monitoring-evaluation`; `proposal-skills/skills/domain-delivery/monitoring-and-evaluation` |
| 4 | Indicator matrix (SMART indicators, baselines, targets, MoV, frequency, responsibility) | `meta-strategy/meta-monitoring-evaluation`; `proposal-skills/skills/domain-delivery/monitoring-and-evaluation` |
| 5 | Data management plan (collection methods, tools, data-quality assurance, storage) | `proposal-skills/skills/domain-delivery/monitoring-and-evaluation`; stakeholder/beneficiary engagement via `proposal-skills/skills/domain-delivery/stakeholder-engagement` |
| 6 | M&E calendar (data-collection, reporting, review, evaluation timing) | `meta-strategy/meta-living-plan-governance`; `meta-strategy/meta-monitoring-evaluation` |
| 7 | Roles & responsibilities (M&E unit, programme staff, board, donor, beneficiaries) | `meta-strategy/meta-living-plan-governance`; `proposal-skills/skills/domain-delivery/stakeholder-engagement` |
| 8 | Evaluation plan — OECD-DAC criteria (relevance, coherence, effectiveness, efficiency, impact, sustainability) + ToR template | `proposal-skills/skills/domain-delivery/monitoring-and-evaluation`; `meta-strategy/meta-monitoring-evaluation` |
| 9 | Reporting & learning (utilisation-focused reporting, adaptive management, review gates) | `meta-strategy/meta-living-plan-governance`; `meta-strategy/meta-monitoring-evaluation` |
| 10 | Financial-monitoring linkage (budget-vs-actual-vs-variance, absorption / burn rate, donor flexed-budget variance) | `09-budgeting-fpa-and-costing/variance-analysis-and-kpi-reporting`, `budgeting-and-rolling-forecasts`; `doctrine/references/uganda-ngo-financial-management-patterns.md` |
| 11 | Appendices: indicator tracking table, data-collection tools, evaluation ToR, quarterly report template, version control | this blueprint |

For donor-funded programmes, layer the donor's own result framework and reporting calendar over chapters 3–4 and 9 — the stricter requirement wins.

## Indicator matrix (render as a table in every framework)

Every results-framework level (output and outcome at minimum) carries indicators in this exact shape. Each indicator is SMART; baselines and targets are named client parameters (see below).

| Indicator | Definition | Baseline | Target | Means of verification (MoV) | Frequency | Responsible |
|-----------|------------|----------|--------|-----------------------------|-----------|-------------|
| [e.g. % of trained farmers adopting practice X] | [exactly what is counted, numerator/denominator, disaggregation] | [value + date, or "to be established by baseline survey"] | [value + date — parameter, to be approved] | [survey / register / report / observation] | [monthly / quarterly / annual — parameter] | [named role/unit] |

Disaggregate by sex, age, and any client-relevant group wherever the data allows. No indicator ships without a baseline (or a dated plan to establish one), a means of verification, and a responsible person.

## Financial-monitoring linkage (chapter 10)

Tie programmatic results to money so the framework reports performance, not just activity:

- **Budget-vs-actual-vs-variance with narrative** — per result area / budget line, reported quarterly; substance from `variance-analysis-and-kpi-reporting`.
- **Absorption / burn rate** — spend against plan over time, read alongside output delivery, so under-spend and under-delivery (or over-spend and under-delivery) are visible together.
- **Donor flexed-budget variance** — for donor-funded work, measure variance against a *flexed* (exchange-rate-adjusted) budget, not the original UGX/USD figure; substance from `doctrine/references/uganda-ngo-financial-management-patterns.md`.
- **KPI cascade** — programmatic KPIs and financial KPIs cascade from the same objectives; do not maintain two disconnected scorecards.

Do not author variance or budgeting mechanics here — pull them from the finance engine and reference them.

## Parameterisation rule

Everything the client must choose is a **parameter with an owner and a review date**, presented as a default-to-be-approved, not a hardcoded fact:

> "Outcome 1 target: **[____]%** of beneficiaries by end of Year 2 (recommended default [__]%, against a baseline to be established by the inception survey) — set by the Programme/Board, reviewed annually."

> "Routine data-collection frequency: **[monthly / quarterly]** (recommended quarterly for outcome indicators, monthly for output indicators); board performance reporting **[quarterly]**; donor reporting per the grant agreement — set by the M&E unit, reviewed at each cycle."

Indicator targets, baselines, data-collection frequencies, and reporting cadences are all parameters. The framework body never asserts a fixed number where a client decision is required; it states the recommended default and flags it for approval.

## Tools / templates pack (appendix)

Theory-of-change diagram; results framework / logframe matrix; indicator tracking table / performance tracker (the indicator matrix above, instantiated and updatable); data-collection tools (survey, register, checklist, beneficiary-feedback form); M&E calendar; evaluation Terms of Reference (ToR) template structured on the six OECD-DAC criteria; quarterly performance report template (results against targets + budget-vs-actual narrative + absorption). Tailor the pack to the programme's actual data flows — do not ship tools for data the programme will not collect.
