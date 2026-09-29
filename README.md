# Business Plan Skills Suite

Business Plan Skills is a routed collection of reusable methods for business plans, standalone marketing plans, strategy work, financial planning, proposals, pitch materials, and supporting policies. It combines an end-to-end business-plan workflow with specialist skills, country contexts for Uganda, Kenya, and Tanzania, templates, references, and validation tools.

The suite serves founders, owner-managers, consultants, programme teams, boards, lenders, and investors who need structured planning and review. Its outputs include evidence-led plans and decision packs, market and strategy assessments, forecasts and financial models, marketing plans, grant and investor materials, and execution frameworks. The workflow requires assumptions and evidence to be distinguished, narrative and model logic to reconcile, and release claims to remain within the evidence actually reviewed.

## Installation

For Claude Code, install the plugin from its marketplace:

```text
/plugin marketplace add https://github.com/peterbamuhigire/business-plan-skills
/plugin install business-plan@chwezi-business-plan
```

For a local clone, use the included installer (Node.js 18 or later):

```sh
git clone https://github.com/peterbamuhigire/business-plan-skills
cd business-plan-skills
./install.sh --scope project
```

On Windows PowerShell, run `./install.ps1 -scope project`. The wrappers also support user scope and dry-run options; see their help before installing. This engine's optional sister-engine routes are described in `AGENTS.md`.

## Capabilities

| Category | Skill routes | Coverage |
|---|---:|---|
| Plan pipeline | 49 | [`pipeline/`](skills/pipeline/), including the [business-plan orchestrator](skills/meta-strategy/business-plan-orchestrator/SKILL.md) for full plans; intake, plan sections, SaaS/AI overlays, implementation, appendices, and assembly. |
| Strategy and validation | 22 | [`meta-strategy/`](skills/meta-strategy/): business-model design, market validation, competitive and strategic analysis, due diligence, market entry, and execution governance. |
| Finance and investor readiness | 12 | [`meta-finance/`](skills/meta-finance/): bankability, valuation, stress testing, accounting/finance review, revenue recognition, SLA controls, and investment-committee challenge. |
| SaaS and ICT | 15 | [`saas/`](skills/saas/) and [`ict/`](skills/ict/): SaaS product and go-to-market planning, unit economics, ICT businesses, and e-commerce diagnostics. |
| Marketing, pricing, and pitch | 10 | [`marketing-sales/`](skills/marketing-sales/), [`meta-pricing-gtm/`](skills/meta-pricing-gtm/), and [`meta-pitch/`](skills/meta-pitch/): marketing plans, demand generation, digital strategy, pricing, premium go-to-market, website investment, and pitch preparation. |
| Advisory and reporting | 9 | [`advisory-deliverables/`](skills/advisory-deliverables/) and [`meta-reporting/`](skills/meta-reporting/): finance, procurement, HR, governance, controls, grants, M&E, and board/investor reporting. |
| Writing and language | 8 | [`writing-content/`](skills/writing-content/) and [`language/`](skills/language/): content, commercial and prompt writing, East African English, language standards, and plan-specific writing quality. |
| Utility and sustainability | 7 | [`meta-utility/`](skills/meta-utility/) and [`meta-sustainability/`](skills/meta-sustainability/): skill authoring and safety, proposal architecture, documentation, anti-slop review, and sustainability strategy. |
| Industry guides | 2 skill entries | [`industry-guides/`](skills/industry-guides/): hospitality and general guide entrypoints; additional sector guide files are references, not separate skills. |
| Country contexts | 3 | [`Uganda`](country-context/uganda/), [`Kenya`](country-context/kenya/), and [`Tanzania`](country-context/tanzania/). |

Browse the [skills directory](skills/) and [country-context directory](country-context/) for the current skill files. Counts reflect the discovered `SKILL.md` inventory at this rewrite and can change as the catalogue changes.

## References

- [Business Plan Skills source repository](https://github.com/peterbamuhigire/business-plan-skills)
- [Repository operating guide and routing rules](AGENTS.md)
- [Business-plan orchestrator](skills/meta-strategy/business-plan-orchestrator/SKILL.md)
- [Marketing-plan orchestrator](skills/marketing-sales/marketing-plan-orchestrator/SKILL.md)
- [Country contexts](country-context/)
- [Runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md) for multi-phase work: scoped work packages, evidence checkpoints, context hygiene, least agency, and sanitised handling of external content
- [Installer scripts](install.sh), [Windows installer](install.ps1)
