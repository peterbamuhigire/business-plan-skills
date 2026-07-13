---
name: saas-agent-funding-stage-playbook
description: Use when producing or reviewing the saas agent funding stage playbook component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS Agent Funding Stage Playbook Skill

## Overview

AI funding (handled by `saas-ai-funding-stage-playbook`) maps AI startups to AI-VC / sovereign-AI / DFI envelopes. **Agent funding** has its own investor archetypes (agent-specialist funds, vertical AI funds) and its own use-of-proceeds shape (heavier on Tool / Eval / Safety than on GTM). Milestones are agent-specific.

## Use When

- Section 11 is being built for an agent-product plan
- A round is being planned (pre-seed -> growth)
- Investor-targeting list is being assembled
- Use-of-proceeds is being argued
- Milestone breakpoints for the next round are being declared

## Do Not Use When

- The product is AI-feature only without agentic action — use `saas-ai-funding-stage-playbook`
- A grant-only path is the funding strategy — use `11b-grant-proposal` instead
- The plan is too early (pre-PMF, pre-customer) — focus on building first customers before funding-stage discipline

## Required Inputs

- Current stage and ARR
- Cost-per-resolved-task trajectory
- Moat-vs-wrapper score
- Bankability score
- Customer mix (regulated / public / SMB / enterprise)
- Geographic footprint

## Workflow

1. **Match stage to investor archetype** per `references/saas-agent-funding-stage-playbook.md`:
   - **Pre-seed (USD 250k-1.5M)** — angels, agent-specialist seed funds, accelerator (YC / Techstars / Founder Institute / MEST / Antler / Future Africa / 500 / Norrsken / Catalyst Fund), DFI early-stage envelopes
   - **Seed (USD 1.5-5M)** — agent-specialist seed funds, AI-specialist seed (a16z AI, Bessemer AI), African / EM seed (TLcom, Norrsken22, Partech Africa, Ventures Platform, Future Africa, Equator, Knife, 4Di), DFI seed envelopes
   - **Series A (USD 5-20M)** — agent-specialist A funds, vertical AI funds, generalist SaaS funds with AI thesis, sovereign-AI strategic, DFI A envelopes
   - **Series B (USD 20-60M)** — agent-specialist growth, vertical AI growth, generalist growth, sovereign-AI strategic at scale, DFI patient capital
   - **Growth (USD 60M+)** — generalist growth + strategic + sovereign at scale; potential pre-IPO; cross-border listings (JSE / NSE / NGX / EGX)

2. **Specify use of proceeds** for agents specifically:
   - **Tool Engineering** (proprietary tools / integrations) — typically 25-40% of seed / A
   - **Eval infrastructure** — typically 10-20%
   - **AI Safety + governance + regulator engagement** — typically 10-15%
   - **Agent Architect + senior engineering** — typically 15-25%
   - **HITL Designer + operations** — typically 5-10%
   - **GTM** (lower than normal SaaS at early stages because product-led + vertical-anchored) — typically 15-25% at seed/A; rises at B
   - **Forward Deployed Engineering** if vertical thesis — 5-15%
   - **Reserve (irreversibility / migration / regulator)** — 5-10%
   - **Compute / infra (LLM + tools + in-region GPU)** — typically 8-15%

3. **Set milestone breakpoints** per stage:
   - **Pre-seed -> seed:** first Class B agent live in production with 5+ customers; eval suite v1; cost-per-resolved-task baselined; AI Safety Lead engaged (fractional acceptable)
   - **Seed -> A:** first Class C agent live in supervised mode; eval coverage >85%; cost-per-resolved under target; 20+ customers; agent GM >50%; AI Safety Lead full-time
   - **A -> B:** first Class D agent live with human-final; eval coverage >95% on Class C/D; cost-per-resolved-task well under competitive anchor; agent GM >60%; 100+ customers or regulated / public-sector anchors; first audit clearance
   - **B -> Growth:** multi-country deployment; multi-vertical or platform play; agent GM >70%; sovereign-AI procurement won; regulator-accepted audit-log in production
   - **Growth -> exit:** category-defining vertical or platform position; multiple sovereign-AI tenders; strategic-acquisition value or IPO path

4. **Diligence preparation** — the bankability scorecard (`meta-agent-bankability-and-investor-readiness`) and data room (`meta-due-diligence` agent contents) prepared 60-90 days before round opens

5. **Investor narrative discipline:**
   - Open with the agent thesis (one paragraph; archetype declared)
   - Cost-per-resolved-task as headline economic metric
   - Moat-or-wrapper thesis paragraph
   - Autonomy ladder progress with gates
   - Regulator-engagement evidence
   - AI Safety Lead in seat
   - Stress-tested

## Quality Bar

- Stage-to-investor match explicit
- Use of proceeds reasoned (% by line)
- Milestone breakpoints for next round declared
- Diligence preparation in train
- Investor narrative draft
- Cross-reference to bankability and valuation

## Anti-Patterns

- "AI fund" with no distinction between AI-feature and agent funds
- Use of proceeds same as normal SaaS (too heavy on GTM, too light on Tool / Eval / Safety)
- Milestones in MRR / ARR only without agent-specific (cost-per-resolved, intervention rate, autonomy ladder, regulator)
- Round opens before bankability evidence assembled
- No AI Safety Lead at A or later
- Pricing in local currency to USD investors

## Outputs

- Investor target list with archetype labels
- Use-of-proceeds breakdown
- Milestone breakpoints for current and next round
- Investor narrative draft
- Cross-reference to bankability + data room
- Stress on funding ask under tail risks

## Living-Plan Cadence Defaults

| Element | Cadence | Owner |
|---|---|---|
| Investor target list refresh | quarterly | CEO + Head of Strategy |
| Milestone progress | monthly | CEO + CFO |
| Bankability rescore | quarterly | (per bankability skill) |
| Use-of-proceeds variance | monthly | CFO |
| Round opens | per-round | CEO + Board |

## References

- `references/saas-agent-funding-stage-playbook.md` — stage-by-stage detail; investor archetypes; use-of-proceeds patterns
- `skills/11-funding-request/saas-ai-funding-stage-playbook/SKILL.md` — AI parent
- `skills/meta-agent-bankability-and-investor-readiness/SKILL.md` — bankability gate
- `skills/meta-agent-valuation-adjustments/SKILL.md` — valuation
- `skills/meta-due-diligence/SKILL.md` — DD
- `book-extractions/agent-products-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **African agent-fund landscape in 2025-2026** — agent-specialist funds rare; institutional agent investment typically via SF / EU co-investors with African lead (TLcom, Norrsken22, Partech, Ventures Platform, 4Di, Knife, Future Africa, Equator, Catalyst Fund, Renew, Ingressive)
- **DFI / multilateral envelopes** — IFC, AfDB, FMO, BII, Proparco, FCDO, USAID DIV, IDRC, GIZ — increasingly carve out AI / agent allocations
- **Sovereign-AI envelopes** — RW innovation envelope, KE Talanta AI, NG NITDA implementation, ZA Presidential 4IR, EG infrastructure — supportive but slow; use as supplementary not primary
- **Patient capital available** through DFIs; lowers required multiple but slower DD
- **Pricing** — institutional rounds in USD; DFI / strategic in local-currency-equivalent
- **Diligence reality** — DFI DD is rigorous (audit-log, jobs-impact, governance, environmental & social) and takes 6-9 months; build buffer
- **Regulatory clearance evidence** — strongly DD-valued for African plans
- **Co-investment patterns** — typically lead + 2-4 co-investors; sometimes DFI-anchored
- **Currency hedging** — institutional rounds often require USD-equivalent runway projections

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria for saas agent funding stage playbook | Financial model, implementation plan, client records, and target-financier materials | Yes | If absent, the funding gap, uses, repayment capacity, dilution effect, or stage evidence is unavailable, return a financing-readiness gap note and withhold the amount or instrument recommendation. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Audience-specific funding request with instrument, uses, milestones, and repayment or return logic | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent funding stage playbook exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent funding stage playbook release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Ask-to-use reconciliation, financing-option decision record, milestone release logic, and caveat register | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent funding stage playbook decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent funding stage playbook review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent funding stage playbook, the controlling focus is agent-company stage evidence, milestone capital, technical diligence, and investor fit. This skill may analyse financing options and draft the ask; it may not solicit investors, submit applications, negotiate terms, value securities, or bind the client without explicit authority and professional review. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent funding stage playbook, loss of evidence about agent-company stage evidence, milestone capital, technical diligence, and investor fit activates degraded mode. If the controlling saas agent funding stage playbook evidence is unavailable, the same boundary applies. When the funding gap, uses, repayment capacity, dilution effect, or stage evidence is unavailable, return a financing-readiness gap note and withhold the amount or instrument recommendation. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent funding stage playbook, the preferred instrument does not match cash-flow capacity, stage, security, or investor-return evidence| reject it, compare the viable alternatives, and state the milestone needed to reopen the option | A mismatched ask can create unaffordable debt, avoidable dilution, or failed diligence |
| For saas agent funding stage playbook, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent funding stage playbook decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent funding stage playbook, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete audience-specific funding request with instrument, uses, milestones, and repayment or return logic, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent funding stage playbook decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce audience-specific funding request with instrument, uses, milestones, and repayment or return logic with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Audience-specific funding request with instrument, uses, milestones, and repayment or return logic must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Ask-to-use reconciliation, financing-option decision record, milestone release logic, and caveat register must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent funding stage playbook, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent funding stage playbook, treating an unavailable reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing audience-specific funding request with instrument, uses, milestones, and repayment or return logic that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

An agent startup has demos but no production task-success evidence. Frame the raise around validation milestones and technical diligence, not a scale-stage valuation narrative.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent funding stage playbook; no local deep-dive reference is declared.
- For saas agent funding stage playbook claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
