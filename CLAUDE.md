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

### Multi-Country Plans (Non-Uganda)

When a `country-context/{country-name}/SKILL.md` file exists in the repo, **use it as the regulatory and financial context for all plan sections**:

1. **Currency** — use the currency code and exchange rates from Section 1 (replace UGX with local currency)
2. **Tax rates** — use Section 4 (replace Uganda PAYE bands, 30% corporate tax, 18% VAT, EFRIS references)
3. **Regulatory bodies** — use Section 5 (replace KCCA, URA, UNBS, NEMA with local equivalents)
4. **Banking context** — use Section 6 (replace Centenary Bank, Stanbic, UDB with local institutions)
5. **Salary benchmarks** — use Section 7 (replace Uganda wage bands)
6. **Risk context** — use Section 9 (replace Uganda-specific risks table in Section 12 skill)

**Universal frameworks always apply regardless of country:**
- CAMPARI, DSCR ≥ 1.25×, TAM/SAM/SOM methodology
- DCF/WACC/CAPM valuation, revenue multiples, Damodaran rules
- Pyramid Principle / SCQA (Minto), MECE / issue trees (Rasiel)
- Sales methodology (Schiffman, Keenan, gap selling)
- Risk assessment (COSO ERM, Bowtie, MECE risk register)
- All marketing frameworks (AARRR, 4Ps/7Ps, Kotler, Golden Circle)

If no country file exists, Uganda defaults apply. To create a file for a new country, copy `country-context/template.md` to `country-context/{country-name}/SKILL.md`. See `country-context/INDEX.md` for available countries.

### Source Referencing

- Cite reference books where they add credibility to the business plan: financial benchmarks, regulatory frameworks, pricing methodologies, industry statistics
- Format: parenthetical (Author, Year) on first use; full bibliographic details in the appendices
- Do NOT cite for generic advice, the user's own data, or derived projections
