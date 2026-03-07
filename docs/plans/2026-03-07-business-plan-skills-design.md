# Business Plan Skills Suite — Design Document

**Date:** 7 March 2026
**Status:** Approved and scaffolded

## Overview

Modular suite of 20 Claude Code skills for generating, monitoring, and evaluating bankable business plans. Each plan section is a standalone skill that can be invoked individually or chained sequentially.

## Architecture

- 15 core plan section skills (numbered 01-15)
- 5 meta-skills for analysis and operations (prefixed `meta-`)
- 4 pre-existing utility skills

## Methodology Sources

- Rogoff (Bankable Business Plans) → financial scoring, bankability criteria
- Palo Alto (On Target) → marketing and sales depth
- King (Business Plans to Game Plans) → M&E, 90-day game plans
- Barrow (Business Plan Workbook) → structured exercises
- Hazelgren & Covello (Complete Book) → comprehensive templates
- Dummies series → accessible financial planning

## Key Design Decisions

1. Numbered prefixes enforce reading/generation order
2. Meta-prefix separates analytical tools from content generators
3. AI integration (section 14) is mandatory for 2026-era plans
4. Skills are self-contained but cross-reference each other
5. British English per east-african-english skill

## Next Steps

- Enhance each skill with `references/` subdirectories containing:
  - Methodology excerpts from reference books
  - Templates and examples
  - Industry-specific variations
- Build integration workflow skill to chain all skills together
- Test with real business plan generation
