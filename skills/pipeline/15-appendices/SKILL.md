---
name: 15-appendices
description: Use when producing or reviewing the 15 appendices component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Appendices Skill

## Use When

- Use when supporting evidence needs to be assembled behind the main plan or proposal.
- Use when a bank, investor, DFI, or partner will expect documentary backup for the main claims.
- Use when the work needs an evidence matrix or data-room style appendix structure.

## Do Not Use When

- Do not use as a dumping ground for unrelated material.
- Do not use before the main body claims are stable enough to map to evidence.
- Do not use appendices to hide core logic that should be visible in the main plan.

## Required Inputs

- Completed or near-complete main sections
- All available supporting documents, exhibits, and datasets
- Audience type and likely due-diligence expectations
- The high-stakes claims, figures, and legal or financial assertions that need proof

## Workflow

1. Identify which main-plan claims require documentary support.
2. Organise the evidence into logical appendix or data-room categories.
3. Build the evidence matrix linking claims to proof.
4. Standardise the naming, order, and purpose of each appendix item.
5. Reconcile the appendix pack against the main document and the audience's DD expectations.
6. Flag missing or weak evidence that still needs to be obtained.

## Quality Bar

- Every material claim in the main plan can be traced to evidence or a labelled estimate.
- The appendix structure is easy for a lender or investor to navigate.
- Financial tables match the summary numbers exactly.
- Missing documents are visible rather than silently omitted.

## Anti-Patterns

- In 15 appendices, treating appendices as miscellaneous storage.
- Including documents with no clear link to the main decision case.
- Leaving unsupported claims unlabelled.
- Presenting appendix evidence that contradicts the main body.

## Outputs

- Appendix structure or data-room map
- Evidence matrix
- Ordered appendix list with purpose and section reference
- A gap list of missing support documents



Generate a well-organised appendices section that provides the supporting evidence investors need without cluttering the main plan.

## What to Generate

### Standard Appendix Items

1. **Detailed financial tables** - Monthly projections, detailed cost breakdowns
2. **Market research data** - Survey results, industry reports, data tables
3. **Product specifications** - Technical details, screenshots, prototypes
4. **Legal documents** - Articles of incorporation, patents, licences, permits
5. **Team CVs/resumes** - Full biographies of key team members
6. **Letters of intent / customer commitments** - Evidence of demand
7. **Partnership agreements** - Signed or draft agreements
8. **Lease/facility agreements** - Property or equipment contracts
9. **Insurance documentation** - Current or planned coverage
10. **Technical architecture** - System diagrams if relevant
11. **Glossary** - Industry-specific terms used in the plan
12. **References and citations** - Sources for market data and claims
13. **Evidence matrix** - Claim-to-proof table for critical assertions
14. **Data room index** - Funder-specific list of available, pending, or missing diligence documents

### Organisation Format

Each appendix item should be:

```text
Appendix [Letter]: [Title]
Purpose: [Why this is included]
Reference: [Which plan section cites this]
Content: [The actual document or data]
```

## Generation Process

1. Review completed sections for claims needing proof
2. List all referenced data, documents, and supporting materials
3. Organise by category: financial, legal, market, team, technical, ESG
4. Generate missing tables or summaries
5. Build an evidence matrix for all high-stakes claims
6. Create a table of contents for the appendices

## Uganda Bank Loan Submission - Required Appendix Documents

| Appendix | Document | Template Available |
|---|---|---|
| A | Director / Guarantor CV | Yes - Template 1 |
| B | Personal Net Worth Statement | Yes - Template 2 |
| C | Loan Repayment Schedule | Yes - Template 3 |
| D | 3-Year Financial Summary | Yes - Template 4 |
| E | Character References | Yes - Template 5 |
| F | Supplier Reference Letters | Yes - Template 6 |
| G | URA Tax Compliance Certificate | Instructions - Template 7 |
| H | NSSF Compliance Certificate | Instructions - Template 8 |
| I | Business Registration Certificate / Certificate of Incorporation | Obtain from URSB |
| J | Land title / logbook / collateral documentation | Original documents |
| K | NEMA permit / UNBS certificate where relevant | Obtain from regulator |

## Evidence Matrix Requirement

Create a one-page evidence matrix before finalising appendices:

| Claim / Figure | Main Plan Section | Appendix Proof | Status | Notes |
|---|---|---|---|---|
| [Example: Year 1 revenue] | 10 | Appendix B | Verified | ties to model |
| [Example: signed customer interest] | 07 | Appendix F | Pending | LOI expected |

Status options:

- Verified
- Partially evidenced
- Pending
- Management estimate

High-stakes claims should not remain unlabelled.

## Data Room Architecture

Where the audience is an investor, DFI, or strategic partner, organise appendices like a simple data room:

- Corporate and legal
- Financial and tax
- Commercial and market proof
- Operations and technical
- Team and governance
- ESG / compliance

State what is available now, what is pending, and what still needs to be created.

## Quality Criteria

- Every major claim in the plan has supporting evidence in the appendices
- Every high-stakes claim appears in the evidence matrix with a status
- Appendices are referenced from the main plan
- Financial appendices match summary figures exactly
- Legal documents are current and valid
- Organisation follows a logical structure with clear labelling
- For bank submissions: all CAMPARI document requirements are met

## References

- `references/document-templates.md` - Uganda-specific templates for director CVs, net worth statements, repayment schedules, and compliance certificates
- `../meta-due-diligence/SKILL.md` - use for investor and DFI data-room readiness
- `../meta-consulting-synthesis/SKILL.md` - use to identify the high-stakes claims that must appear in the evidence matrix

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Final evidence register, approved exhibits, source documents, calculations, licences, biographies, and confidentiality rules for 15 appendices | Section owners, client document room, and release reviewer | Yes | If absent, a cited exhibit is unavailable or disclosure authority is unclear, remove the citation from release or mark the appendix pending. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Indexed appendices with verified cross-references and disclosure controls | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 15 appendices exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 15 appendices release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Appendix inventory, source/provenance trace, redaction record, and body-to-appendix link check | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 15 appendices decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 15 appendices review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 15 appendices, the controlling focus is exhibit provenance, body cross-reference, document version, confidentiality, redaction, completeness, and release authority. This skill may organise and redact authorised copies; it may not alter source evidence, disclose restricted material, or attach personal records without permission. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 15 appendices, loss of evidence about exhibit provenance, body cross-reference, document version, confidentiality, redaction, completeness, and release authority activates degraded mode. If the controlling 15 appendices evidence is unavailable, the same boundary applies. When a cited exhibit is unavailable or disclosure authority is unclear, remove the citation from release or mark the appendix pending. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 15 appendices, an exhibit is relevant but contains unnecessary confidential or personal data| redact to the minimum disclosure, record the redaction, and obtain approval before inclusion | Appendices can create privacy exposure or expose unsupported body claims |
| For 15 appendices, A current legal, regulatory, tax, accounting, market, or platform claim controls the 15 appendices decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 15 appendices, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete indexed appendices with verified cross-references and disclosure controls, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 15 appendices decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect final evidence register, approved exhibits, source documents, calculations, licences, biographies, and confidentiality rules and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce indexed appendices with verified cross-references and disclosure controls with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Indexed appendices with verified cross-references and disclosure controls must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Appendix inventory, source/provenance trace, redaction record, and body-to-appendix link check must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 15 appendices, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- Treating an unavailable final evidence register, approved exhibits, source documents, calculations, licences, biographies, and confidentiality rules as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing indexed appendices with verified cross-references and disclosure controls that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

Customer contracts prove traction but contain personal contacts and confidential prices. Include an approved redacted schedule and retain originals outside the release pack.

## References

- Use the verified project evidence register and the owning upstream pipeline section for 15 appendices; no local deep-dive reference is declared.
- For 15 appendices claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
