---
name: country-context-index
description: Index of all available country context files. Each country has its own subdirectory with a SKILL.md and optional references/ folder. When a country context is active, all business plan skills substitute local currency, tax rates, regulatory bodies, banking, and salary data. Universal frameworks (CAMPARI, DSCR, Minto, Rasiel, Damodaran) always apply regardless of country.
---

# Country Context Index

## How It Works

Each country has a subdirectory: `country-context/{country}/SKILL.md`

When generating a business plan:
1. Identify the target country
2. Load `country-context/{country}/SKILL.md` if it exists
3. All core skills (01–15) substitute the country's currency, tax, regulatory, banking, and salary data
4. Universal frameworks remain constant (see template.md for full list)

If no country file exists, **Uganda defaults apply** (see `uganda/SKILL.md`).

---

## Available Countries

| Country | Directory | Status | Exchange rate | Key feature |
|---------|-----------|--------|---------------|-------------|
| **Uganda** | `uganda/` | ✅ Complete | UGX 3,700/$1 (planning) | Default country; most comprehensive |
| **Kenya** | `kenya/` | ✅ Complete | KES 135/$1 (planning) | EAC hub; deep financial sector; AGOA |
| **Tanzania** | `tanzania/` | 🔲 Planned | TZS [TBC] | East Africa; Swahili-speaking market |

---

## Creating a New Country

1. Copy `template.md` to `{country}/SKILL.md`
2. Fill in all 11 sections
3. Add detailed reference files to `{country}/references/` as needed
4. Add a row to this INDEX.md
5. Update `CLAUDE.md` if the country has unique framework exceptions

---

## Template

`template.md` — fill-in-the-blank 11-section country profile. Copy to start a new country.
