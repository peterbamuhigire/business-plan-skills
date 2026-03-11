# Proposal Architect — Design Document

**Date:** 2026-03-11
**Status:** Approved and implemented

---

## Problem

Consultants using this skills repo need a structured, repeatable workflow for developing
competitive proposals and bids. Without it, each consultant invents their own folder
structure and risks inconsistent, incomplete, or non-compliant submissions.

---

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Workspace location | `/proposals/` inside repo | Single repo pull, everything in one place |
| Version control | `/proposals/` in `.gitignore` | Proposals are confidential |
| Invocation | Manual skill (`proposal-architect`) | Repo is also used for skill development; auto-startup would be intrusive |
| DOCX compilation | Pandoc | Best Markdown → DOCX quality; supports client template inheritance; single CLI command |
| Financial output | Separate `.docx` | Matches real-world RFP requirements for separated technical/financial envelopes |

---

## Workspace Structure

```
proposals/
  index.md                        <- master index of all proposals
  {proposal-slug}/
    sections/                     <- narrative content, one .md per section
    terms/                        <- client materials (RFP, TOR, template.docx, advert)
    sheets/                       <- tabular work (budget.xlsx, timeline.xlsx, staffing.csv)
    research/                     <- opportunity analysis, sector notes, references
    assets/                       <- charts, diagrams, logos
    drafts/                       <- scratch work and brainstorm dumps
    submissions/
      technical-proposal.docx
      financial-proposal.docx     <- only if client requires separate financial envelope
```

---

## Skill Phases

1. **Workspace init** — create `/proposals/` and `index.md` if missing
2. **Proposal intake** — name, client, sector, deadline, output type (combined / split)
3. **Source materials intake** — consultant drops files into `terms/`; skill reads them all
4. **Opportunity analysis** — extract requirements, criteria, themes → `research/opportunity-analysis.md`
5. **Brainstorm and draft** — sections into `sections/*.md`, tables into `sheets/`
6. **Compile** — Pandoc → `submissions/technical-proposal.docx` (+ financial if split)

---

## Pandoc Dependency

Consultants must have Pandoc installed:

```bash
winget install JohnMacFarlane.Pandoc   # Windows
brew install pandoc                     # macOS
sudo apt install pandoc                 # Ubuntu/Debian
```

Verify: `pandoc --version`

---

## Files Created by This Implementation

- `proposal-architect/SKILL.md`
- `proposals/index.md`
- `.gitignore`
