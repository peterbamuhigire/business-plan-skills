---
name: industry-guides
description: Industry-specific reference guides that tailor business plan generation to specific sectors. Each sub-directory contains best practices, financial benchmarks, operational standards, regulatory requirements, and common pitfalls for that industry. Use when generating or reviewing a business plan for a specific industry to ensure the plan reflects real-world industry norms, cost structures, and success factors. Invoke alongside any core skill (01-15) to inject industry-specific context.
---

# Industry Guides Skill

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

*More industries will be added over time.*

## Industry Guide Structure

Each industry sub-directory contains:

```
industry-guides/
├── SKILL.md (this index file)
└── [industry-name]/
    ├── guide.md (industry overview, business model types, key success factors)
    └── references/
        ├── financial-benchmarks.md (cost structures, margins, ratios, P&L templates)
        ├── operations.md (staffing, equipment, supply chain, daily operations)
        └── [additional topic files as needed]
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

## Quality Criteria

- Financial benchmarks cite ranges, not single numbers (industries vary)
- Regulatory requirements note they are jurisdiction-dependent
- Startup costs provide ranges by business size/format
- Operational standards distinguish between formats (e.g., full-service vs. fast-casual)
- Common mistakes are specific to the industry, not generic business advice
