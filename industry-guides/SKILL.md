---
name: industry-guides
description: Industry-specific reference guides that tailor business plan generation to specific sectors. Each sub-directory contains best practices, financial benchmarks, operational standards, regulatory requirements, and common pitfalls for that industry. Use when generating or reviewing a business plan for a specific industry to ensure the plan reflects real-world industry norms, cost structures, and success factors. Invoke alongside any core skill (01-15) to inject industry-specific context.
---

# Industry Guides Skill

## Use When

- Use when this skill is the primary workflow for the requested task.
- Use when creating, reviewing, or improving this skill's main artifact.
- Use when this output must align with adjacent sections, assumptions, or audience requirements.

## Do Not Use When

- Do not use when another section or meta-skill is the primary owner of the task.
- Do not use when the required inputs are unavailable and cannot be stated transparently as assumptions.
- Do not use for provider-specific UI behaviour; keep the workflow portable.

## Required Inputs

- Business, client, or proposal context relevant to this skill
- Country, audience, funder, or user context where relevant
- Available assumptions, evidence, constraints, and dependencies
- Adjacent section outputs where consistency matters

## Workflow

1. Clarify the objective, audience, and scope for this skill.
2. Gather the minimum required inputs and note any missing assumptions.
3. Read the referenced materials only as needed.
4. Produce or revise the artifact using the skill-specific method below.
5. Reconcile the output with adjacent sections, numbers, risks, and evidence.
6. Flag unresolved gaps, assumptions, or follow-up work.

## Quality Bar

- Output is specific, decision-useful, and not generic
- Assumptions are explicit where relevant
- Claims align with the rest of the plan, proposal, or workflow
- Wording is structured, concise, and audience-appropriate

## Anti-Patterns

- Generic filler that could describe any business or situation
- Hidden assumptions or unsupported claims
- Contradictions with financials, implementation, risk, or audience requirements
- Provider-specific operating assumptions embedded in the portable workflow

## Outputs

- The primary artifact or analysis owned by this skill
- Any key assumptions, open questions, and cross-skill dependencies



Provide industry-specific context, benchmarks, and best practices to tailor business plan generation to the target sector.

## How to Use

1. Identify the user's target industry
2. Load the relevant industry sub-directory's guide
3. Apply industry-specific benchmarks, cost structures, and operational standards when generating any business plan section
4. Flag where generic assumptions differ from industry norms

## Available Industry Guides

| Industry | Sub-directory | Key Focus Areas |
|---|---|---|
| **Restaurant & Food Service** | `restaurant/` | Food/beverage/labour cost controls, menu engineering, restaurant types, startup costs, licensing, financial benchmarks |
| **Agriculture & Agribusiness** | `agriculture/` | Enterprise budgets, crop planning, farm financial management, agribusiness value chain, marketing channels, organic certification |
| **Retail & Shop Management** | `retail/` | Startup costs by format, retail financial management, Strategic Profit Model, inventory/merchandising, site selection, retail analytics/KPIs, marketing/promotion |
| **Food Processing** | `food-processing/` | Value-addition to agricultural products: dairy, bakery, beverages, spices, oils, cereals, fruits/vegetables, meat/fish processing. 46 UNDP business profiles with investment benchmarks |
| **Cassava** | `cassava/` | Uganda sector overview, production systems (conventional vs mechanised with cost/return tables), agronomy (NASE 14, ISFM, disease management), value chain, processing technologies (HQCF, chips, gari, starch, peel feed), quality standards, seed system (CSEs/CBSMs), startup framework by capital tier, regulatory compliance |
| **Dairy Farming** | `dairy-farming/` | Market structure, 5 production systems with economic benchmarks, regional milksheds, climate-smart feed and manure innovations, startup planning framework, soil nutrient management, value chain actors, financial benchmarks by scale |
| **Livestock, Aquaculture & Farming** | `livestock-aquaculture/` | Poultry, piggery, dairy, cattle, aquaculture, apiculture, horticulture, agri-inputs. 22 UNDP business profiles |
| **Light Manufacturing** | `manufacturing-light/` | Plastics/rubber, paper/stationery, metal products, crafts/decorative, recycling, electronics. 49 UNDP business profiles |
| **Textiles, Fashion & Leather** | `textiles-fashion/` | Garments, leather goods/footwear, natural fibre products, accessories/jewellery. 25 UNDP business profiles |
| **Chemicals & Cosmetics** | `chemicals-cosmetics/` | Cleaning products, personal care/cosmetics, paints/inks, pest control, petroleum products. 18 UNDP business profiles |
| **Construction & Building Materials** | `construction-building-materials/` | Bricks/blocks, tiles/finishing, metal fabrication, wood/timber, construction services. 13 UNDP business profiles |
| **Hospitality & Tourism** | `hospitality-tourism/` | Food service, bars/entertainment, budget accommodation, hotels/lodges. 10 UNDP business profiles |
| **Services** | `services/` | Vehicle services, cleaning/maintenance, tech/digital, personal care, equipment repair, fuel distribution. 10 UNDP business profiles |
| **Mining & Extractives** | `mining-extractives/` | Stone quarrying, mineral extraction, lime/chalk, oil & gas support services. 4 UNDP business profiles |
| **Education & Social Enterprise** | `education-social/` | Private education, health/medical products, hygiene products. 4 UNDP business profiles |

## Industry Guide Structure

Each industry sub-directory contains:

```
industry-guides/
 SKILL.md (this index file)
 [industry-name]/
     guide.md (industry overview, business model types, key success factors)
     references/
         financial-benchmarks.md (cost structures, margins, ratios, P&L templates)
         operations.md (staffing, equipment, supply chain, daily operations)
         [additional topic files as needed]
```

## Integration with Core Skills

When an industry guide is active, it modifies the output of core skills:

| Core Skill | Industry Guide Contribution |
|---|---|
| 04-market-analysis | Industry-specific market size data, growth rates, concentration |
| 05-target-market | Customer demographics and behaviour patterns for this industry |
| 06-competitive-analysis | Industry-specific competitive dynamics and positioning |
| 07-marketing-sales-strategy | Channel preferences, customer acquisition methods for this sector |
| 08-operations-plan | Industry-standard processes, equipment, staffing models |
| 10-financial-projections | Industry benchmarks for revenue, costs, margins, break-even |
| 12-risk-analysis | Industry-specific risks, failure rates, regulatory risks |

## Source Referencing in Business Plans

When generating the final business plan, cite the underlying reference books where they add credibility:

- **Financial benchmarks and ratios**  cite the source when presenting industry-standard percentages, cost structures, or financial targets (e.g., "Industry benchmarks indicate a target food cost of 30-35% of food sales (Dittmer & Keefe, 2009)")
- **Regulatory and compliance frameworks**  cite when referencing specific standards (e.g., HACCP, Uniform System of Accounts, organic certification standards)
- **Market data and industry statistics**  cite when presenting market size, growth rates, or industry structure data
- **Pricing and costing methodologies**  cite when applying specific pricing formulas or costing methods (e.g., contribution margin pricing, enterprise budgeting)
- **Operational best practices**  cite when recommending specific management systems or benchmarks

Do NOT cite sources for:
- Generic business advice that is common knowledge
- The user's own market research or primary data
- Financial projections derived from the user's specific numbers

Format citations as parenthetical references: (Author, Year) on first use. Include a "Sources and References" section in the appendices listing all cited works with full bibliographic details.

## Quality Criteria

- Financial benchmarks cite ranges, not single numbers (industries vary)
- Regulatory requirements note they are jurisdiction-dependent
- Startup costs provide ranges by business size/format
- Operational standards distinguish between formats (e.g., full-service vs. fast-casual)
- Common mistakes are specific to the industry, not generic business advice
