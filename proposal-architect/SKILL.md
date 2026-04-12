---
name: proposal-architect
description: >
  Full-lifecycle proposal development workflow. Invoke when starting or continuing
  work on any proposal, bid, tender, or RFP response. Handles workspace initialisation,
  proposal scaffolding, opportunity analysis, brainstorming, section drafting, and
  final DOCX compilation using Pandoc. Both technical and financial outputs are .docx.
---

# Proposal Architect

## When to Invoke

Invoke this skill whenever a consultant says any of the following (or similar):
- "Start a new proposal"
- "I have an RFP to respond to"
- "Help me write a bid"
- "I want to work on a tender"
- "Let's build a proposal for [client]"
- "Continue working on [proposal name]"

Do NOT wait for an explicit skill invocation — if the intent is clearly proposal work,
invoke this skill automatically before doing anything else.

---

## Prerequisites

Pandoc must be installed on the consultant's machine to compile final DOCX outputs.

```bash
# Windows
winget install JohnMacFarlane.Pandoc

# macOS
brew install pandoc

# Ubuntu / Debian
sudo apt install pandoc
```

Verify: `pandoc --version`

If Pandoc is not installed, proceed with all drafting phases. Flag the missing dependency
before the compilation phase. Pandoc is only needed at the very end.

---

## Phase 1: Workspace Initialisation

**Check** whether the `/proposals` directory exists in the repo root.

If it does NOT exist:
1. Create the `/proposals/` directory.
2. Create `/proposals/index.md` using the template below.
3. Announce: "Proposals workspace created. Ready to start your first proposal."

If it already exists:
- Proceed silently to Phase 2.

### proposals/index.md template

```markdown
# Proposals Index

| # | Proposal Name | Client | Sector | Deadline | Type | Status | Directory |
|---|--------------|--------|--------|----------|------|--------|-----------|
```

---

## Phase 2: New Proposal vs. Continue Existing

Ask the consultant:

> "Are you starting a **new proposal**, or continuing work on an **existing one**?"

**If continuing:** List all subdirectories in `/proposals/` (excluding `index.md`).
Ask which one to open. Load its `research/opportunity-analysis.md` and `sections/` for
context, then ask what to work on next. Skip to the relevant phase.

**If new:** Proceed to Phase 3.

---

## Phase 3: New Proposal Intake

Ask each question in sequence. Wait for the answer before asking the next.

1. **Proposal name** — e.g. "Solar Mini-Grid Feasibility Study for MEMD"
   Convert to a directory slug: lowercase, hyphens, no special characters.
   Example: `solar-mini-grid-feasibility-memd`

2. **Client / organisation** — who is issuing the opportunity?

3. **Sector** — e.g. Energy, Health, Agriculture, Education, Infrastructure, Finance

4. **Submission deadline** — date and time if known

5. **Output type** — does the client require:
   - (A) A **single combined** proposal document (technical + financial together), or
   - (B) **Separate** technical and financial envelopes/documents?

Once all answers are collected:

### Create the proposal directory structure

```
proposals/{slug}/
  sections/
  terms/
  sheets/
  research/
  assets/
  drafts/
  submissions/
```

Create a `README.md` inside the proposal root:

```markdown
# {Proposal Name}

**Client:** {client}
**Sector:** {sector}
**Deadline:** {deadline}
**Output type:** {Combined | Split}
**Created:** {date}
**Status:** Drafting

## Quick Reference
- Source materials: `terms/`
- Narrative sections: `sections/`
- Tables and spreadsheets: `sheets/`
- Research and analysis: `research/`
- Charts and diagrams: `assets/`
- Scratch work: `drafts/`
- Final deliverables: `submissions/`
```

### Update proposals/index.md

Add a new row to the index table:

```
| {n} | {Proposal Name} | {client} | {sector} | {deadline} | {Combined|Split} | Drafting | proposals/{slug}/ |
```

---

## Phase 4: Source Materials Intake

Tell the consultant:

> "Please copy all client documents into:
>
> `proposals/{slug}/terms/`
>
> This includes:
> - The RFP, ITT, EOI, or advertisement
> - Terms of Reference (TOR) if provided
> - Any submission template or formatting guide provided by the client
> - Evaluation criteria or scoring matrix
> - Any reference documents or previous reports the client attached
>
> Let me know when they are in place."

Wait for the consultant to confirm. Then read every file in `terms/` thoroughly.

If the consultant pastes text directly into the chat instead of saving files,
save it as `terms/rfp-pasted.md` before proceeding.

---

## Phase 5: Opportunity Analysis

Analyse all materials in `terms/` and extract the following. Write findings to
`research/opportunity-analysis.md`.

### research/opportunity-analysis.md structure

```markdown
# Opportunity Analysis: {Proposal Name}

## 1. Summary
One paragraph: what the client wants and why.

## 2. Required Deliverables
List every deliverable explicitly mentioned.

## 3. Mandatory Proposal Sections
List sections in the order the client specifies. Note any page/word limits.

## 4. Evaluation Criteria
| Criterion | Weight | Notes |
|-----------|--------|-------|

## 5. Budget and Financial Requirements
- Budget ceiling (if stated):
- Currency:
- Financial format required:
- VAT / tax treatment:
- Payment terms:

## 6. Submission Format
- File format(s):
- Submission method (portal / email / physical):
- Copies required:
- Naming conventions:

## 7. Eligibility Requirements
List any mandatory qualifications, registrations, certifications, or exclusions.

## 8. Key Dates
| Milestone | Date |
|-----------|------|

## 9. Key Themes and Priorities
What the client cares most about, inferred from language and emphasis in the RFP.

## 10. Risks and Red Flags
Any ambiguities, tight constraints, or requirements that need clarification.

## 11. Recommended Section Plan
Based on the above, list the sections this proposal should contain, in order.
Override the default section list if the client specifies a different structure.
```

After writing the file, summarise the top 5 findings for the consultant verbally.

---

## Phase 6: Brainstorm and Draft

This is the creative engine of the skill. Invoke superpowers fully.

### 6a. Positioning brainstorm

Before drafting, think through:
- What is the client's real problem, beneath the stated requirements?
- What differentiates this team / organisation from likely competitors?
- What is the single strongest theme to run through the proposal?
- What methodology or approach will score highest on evaluation criteria?
- What risks must the proposal address proactively?
- What commercial or strategic value should the client expect if this proposal is accepted?

Share this thinking with the consultant. Agree on the positioning before drafting.

### 6a.1 High-value proposal framing

For strategic, advisory, transformation, operational improvement, or other large-value bids, build a clear transformation thesis before drafting:

1. **Why now** — what makes change urgent for the client?
2. **What changes** — what measurable improvement will the client see?
3. **Why this team** — what proof makes the proposal credible?
4. **How risk is controlled** — what reduces delivery risk from day one?

Where relevant, show capability across these transformation pillars:
- leadership
- culture
- people
- systems
- IQ
- EQ
- flexibility
- fearlessness

If the assignment is tied to growth, match the proposal to the client's lifecycle stage:
- launch / early traction
- scaling / repeatability
- mature / optimisation and defence

For high-value bids, include a visible first-90-days mobilisation logic.

### 6b. Section drafting

Draft each section as a separate `.md` file in `sections/`.

Use the section plan from `research/opportunity-analysis.md`.
If the client did not specify sections, use the default plan below.

For each section:
- Open with a strong, client-focused statement (not a generic introduction)
- Address evaluation criteria directly — name the criterion if helpful
- Use concrete language: numbers, timelines, named methodologies, specific outputs
- Avoid filler phrases: "we are pleased to submit", "we have extensive experience"
- Make commercial value legible: revenue upside, efficiency gain, risk reduction, cycle-time improvement, or retention impact

**Do not pad.** A tight, confident proposal beats a long, vague one.

### Default section plan (override if client specifies otherwise)

| File | Section | Notes |
|------|---------|-------|
| `sections/01-executive-summary.md` | Executive Summary | Write last; max 1 page |
| `sections/02-background.md` | Background and Context | Demonstrate you understand the client's world |
| `sections/03-problem-statement.md` | Problem Statement | Restate the problem in your own words; show insight |
| `sections/04-objectives.md` | Objectives | Mirror the client's language; add measurability |
| `sections/05-methodology.md` | Methodology and Approach | The most-read section; be specific |
| `sections/06-implementation-plan.md` | Implementation Plan | Phases, activities, milestones; reference the timeline sheet |
| `sections/07-team.md` | Team and Qualifications | CVs in appendix; highlight relevance here |
| `sections/08-budget.md` | Budget Narrative | Financial proposals only; link to sheets/budget.xlsx |
| `sections/09-risk-analysis.md` | Risk Analysis | Risk register format; mitigation for each |
| `sections/10-monitoring-evaluation.md` | Monitoring and Evaluation | KPIs, reporting cadence, accountability |
| `sections/11-appendices-list.md` | Appendices | List what is attached; do not repeat content |

### 6c. Sheets generation

For every tabular element, generate a structured file in `sheets/`.

| File | Contents |
|------|---------|
| `sheets/budget.xlsx` | Line-item budget: activity, unit, quantity, unit cost, total, notes |
| `sheets/timeline.xlsx` | Gantt-style: activities vs. weeks/months |
| `sheets/staffing.csv` | Role, person, days, rate, total cost |
| `sheets/assumptions.xlsx` | All financial and operational assumptions |

Generate the content in Markdown tables first (so the consultant can review),
then instruct the consultant to paste them into Excel/CSV files in `sheets/`.

For Uganda-context proposals:
- Use UGX as default currency unless the RFP specifies otherwise
- Apply UGX 3,700/$1 as the conservative planning rate
- Include VAT at 18% where applicable
- Note WHT rates for consultancy fees (6% for residents, 15% for non-residents)
- Flag EFRIS e-invoicing requirement for VAT-registered suppliers

---

## Phase 7: Review and Refinement

Before compiling, run through this checklist with the consultant:

- [ ] Every evaluation criterion is addressed explicitly in at least one section
- [ ] All mandatory sections from the RFP are present
- [ ] Page / word limits are respected
- [ ] Budget in sections/08-budget.md matches sheets/budget.xlsx totals exactly
- [ ] Team CVs and supporting documents are ready for appendices
- [ ] No section contradicts another (check timelines vs implementation plan)
- [ ] Executive summary written last and reflects the final proposal accurately
- [ ] All client terminology and naming conventions used correctly

---

## Phase 8: Compilation

### Prerequisites check

```bash
pandoc --version
```

If this fails, ask the consultant to install Pandoc before proceeding.

### Technical proposal

If a client DOCX template exists in `terms/`:

```bash
pandoc sections/01-executive-summary.md \
       sections/02-background.md \
       sections/03-problem-statement.md \
       sections/04-objectives.md \
       sections/05-methodology.md \
       sections/06-implementation-plan.md \
       sections/07-team.md \
       sections/09-risk-analysis.md \
       sections/10-monitoring-evaluation.md \
       sections/11-appendices-list.md \
  --reference-doc=terms/client-template.docx \
  -o submissions/technical-proposal.docx
```

If no client template exists:

```bash
pandoc sections/01-executive-summary.md \
       sections/02-background.md \
       sections/03-problem-statement.md \
       sections/04-objectives.md \
       sections/05-methodology.md \
       sections/06-implementation-plan.md \
       sections/07-team.md \
       sections/09-risk-analysis.md \
       sections/10-monitoring-evaluation.md \
       sections/11-appendices-list.md \
  -o submissions/technical-proposal.docx
```

### Financial proposal (Split output type only)

```bash
pandoc sections/08-budget.md \
  --reference-doc=terms/client-template.docx \
  -o submissions/financial-proposal.docx
```

If no client template:

```bash
pandoc sections/08-budget.md \
  -o submissions/financial-proposal.docx
```

### Combined output (Combined output type)

Include all sections in one command, with `08-budget.md` after the team section:

```bash
pandoc sections/01-executive-summary.md \
       sections/02-background.md \
       sections/03-problem-statement.md \
       sections/04-objectives.md \
       sections/05-methodology.md \
       sections/06-implementation-plan.md \
       sections/07-team.md \
       sections/08-budget.md \
       sections/09-risk-analysis.md \
       sections/10-monitoring-evaluation.md \
       sections/11-appendices-list.md \
  --reference-doc=terms/client-template.docx \
  -o submissions/proposal.docx
```

### After compilation

1. Ask the consultant to open the DOCX and verify formatting.
2. Remind them to manually paste in tables from `sheets/` if not embedded.
3. Ask them to update `proposals/index.md` status to `Under Review`.

---

## Guiding Principles

1. **Compliance first** — a non-compliant proposal is disqualified regardless of quality.
   Always check mandatory requirements before being creative.

2. **Evaluate-criteria-driven writing** — every paragraph should earn marks.
   If it does not address a criterion, question whether it belongs.

3. **Specificity wins** — "we will conduct 12 community consultations across 4 districts
   between weeks 3 and 6" beats "we will engage stakeholders comprehensively".

4. **Client language** — mirror the client's terminology. If they call it a "workplan",
   do not call it an "implementation schedule".

5. **Financial–narrative alignment** — the budget must match what the methodology
   describes. Reviewers cross-check this. Discrepancies cost marks and credibility.

6. **Confidentiality** — proposals are in `/proposals/` which is gitignored.
   Never commit proposal content to the shared repo.

7. **Value visibility** — high-value proposals should show the business case, not only the workplan.

8. **First-90-days control** — serious buyers want to know how delivery starts; show mobilisation, governance, and early wins where relevant.

---

## Quick Reference: Folder Purposes

| Folder | Contents |
|--------|---------|
| `sections/` | Narrative .md files — one per proposal section |
| `terms/` | All client-issued materials: RFP, TOR, template, advert |
| `sheets/` | Structured/tabular work: budgets, timelines, staffing |
| `research/` | Opportunity analysis, sector notes, competitor intelligence |
| `assets/` | Charts, diagrams, logos, photos |
| `drafts/` | Scratch writing, brainstorm dumps, iteration versions |
| `submissions/` | Final compiled DOCX files ready for client delivery |

---

## Reference Files

- `references/high-value-proposal-strategy.md` — use for transformation, growth, advisory, or operational-improvement proposals that need a clear change thesis, measurable client value, and a credible first-90-days mobilisation plan
