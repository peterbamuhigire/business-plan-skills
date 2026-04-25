---
name: industry-guides
description: Industry-specific reference guides that tailor business plan generation to specific sectors. Each sub-directory contains best practices, financial benchmarks, operational standards, regulatory requirements, and common pitfalls for that industry. Use when generating or reviewing a business plan for a specific industry to ensure the plan reflects real-world industry norms, cost structures, and success factors. Invoke alongside any core skill (01-15) to inject industry-specific context.
---

# Industry Guides Skill

## Overview

Use this skill as the sector-context layer for plan writing. It routes the agent to the correct industry sub-guide so section skills use realistic operating assumptions, benchmarks, and constraints for the business at hand.

## Use When

- Use when a business plan, proposal, or pitch needs industry-specific benchmarks and operating context.
- Use when the sector materially changes margins, processes, regulation, or success factors.
- Use alongside core section skills to inject sector realism.

## Do Not Use When

- Do not use as a substitute for the core section skill that owns the main artifact.
- Do not assume a sector guide is authoritative for every geography without checking the country context.
- Do not copy raw reference material into a plan without translating it into the client's business reality.

## Required Inputs

- Target industry or sub-sector
- Business model, scale, geography, and intended audience
- Any adjacent sections whose assumptions need sector grounding
- Known constraints or differentiators that affect which benchmarks are relevant

## Workflow

1. Identify the closest industry guide that matches the client's actual operating model.
2. Read the guide and only the reference files needed for the current section.
3. Extract the sector assumptions that materially change the draft.
4. Reconcile those assumptions with country context and audience expectations.
5. Apply the sector logic to the owning section skill.
6. Flag where the available guide is only a partial fit.

## Quality Bar

- Sector context materially improves realism.
- Benchmarks are used as ranges and decision aids, not as fabricated facts.
- Industry guidance aligns with the country and funding context.
- The integration makes the plan more specific, not more verbose.

## Anti-Patterns

- Picking a broad sector label when a more specific guide exists.
- Applying guide assumptions mechanically without checking scale or business model.
- Using sector benchmarks that contradict the plan's own economics.
- Treating reference text as publishable plan prose.

## Outputs

- A sector-informed input layer for the owning section skill
- Explicit benchmark assumptions and caveats
- Pointers to the most relevant guide and reference files



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
