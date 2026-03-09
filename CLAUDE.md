# Business Plan Skills Suite

## Project Structure

This is a collection of Claude Code skills for generating bankable business plans. Each folder is a self-contained skill with a `SKILL.md` and optional `references/` directory.

### Naming Conventions

- Core plan sections: `01-executive-summary` through `15-appendices` (numbered for reading order)
- Meta/analytical skills: `meta-` prefix (e.g., `meta-financial-stress-test`)
- Utility skills: plain names (e.g., `skill-writing`)

### Skill Authoring Rules

- Every skill MUST have a `SKILL.md` with YAML frontmatter (`name`, `description`)
- Keep SKILL.md concise — reference files go in `references/` subfolder
- Skills are self-contained and can be invoked independently
- Use British English spelling (organisation, programme, colour) per east-african-english skill

### Key Methodologies

- Financial sections follow Rogoff's bankability criteria
- Marketing sections follow Palo Alto's On Target framework
- Implementation/M&E follows Jan B. King's game plan methodology
- AI integration section is mandatory for 2026-era plans

### When Generating Plan Content

- Always ask for the business name, industry, and country context first
- Financial projections need explicit assumptions — never fabricate numbers
- Market data must be sourced or clearly flagged as estimates
- Each section should cross-reference related sections for consistency

### Currency and Localisation

- **Default context: Uganda (UGX)**. All examples, costs, and financial projections should use Ugandan Shillings (UGX) unless the user specifies a different country
- When reference materials quote USD figures, convert to UGX at a realistic rate. **Current official rate: approx. UGX 3,550 per $1 (Q1 2025/26, UBOS KEI)**. Use **UGX 3,700** as a conservative planning rate in projections (to account for exchange-rate depreciation risk). Adjust for local economic realities — do not simply multiply by the exchange rate. Account for differences in:
  - Labour costs (significantly lower in Uganda)
  - Land/rent costs (varies by location — Kampala vs rural)
  - Input costs (some imported inputs may be more expensive)
  - Market prices and consumer purchasing power
- Use local regulatory context (URA tax requirements, KCCA/district licensing, UNBS standards, NEMA environmental permits)
- Reference local institutions: Bank of Uganda, Uganda Development Bank, microfinance institutions, SACCOs

### Source Referencing

- Cite reference books where they add credibility to the business plan: financial benchmarks, regulatory frameworks, pricing methodologies, industry statistics
- Format: parenthetical (Author, Year) on first use; full bibliographic details in the appendices
- Do NOT cite for generic advice, the user's own data, or derived projections
