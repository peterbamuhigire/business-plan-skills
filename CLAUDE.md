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
