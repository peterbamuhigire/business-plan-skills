---
name: saas-agent-investor-narrative-on-sla
description: Use when producing or reviewing the saas agent investor narrative on sla component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS Agent Investor Narrative on SLA Skill

## Overview

In 2025-2026 agent-investor diligence, SLA discipline has migrated from "operational footnote" to "investability gate." Agent-specialist funds (Madrona, Conviction, Greylock-AI, agent-focused early-stage at a16z / Bessemer / Sequoia AI), vertical AI funds, sovereign-AI envelopes and DFIs all now read SLA performance during DD. Bad SLA narrative loses rounds; good SLA narrative compresses diligence and supports premium multiple.

The narrative has two faces:

- **Confidence-builder** — when SLA is measurable, published, audited, disclosed; credit ratio low; reserve methodology disciplined; dispute discipline strong. This narrative reads as "operational maturity at scale" and supports a +5 to +25% multiple overlay.
- **Liability question** — when SLA performance is hidden, ad hoc reserves, undisclosed disputes, credit ratio drift, no third-party validation. This narrative gets read as "unpriced revenue volatility" and drives -10 to -40% discount or "pass with feedback."

Most early-stage agent founders default to the liability question because they have not built the discipline. The fix is structural: build the SLA discipline, then build the narrative.

This skill is the **narrative discipline** — how to talk about SLA in pitch deck, data room, investor updates, board calls, and Q&A. It does not replace the underlying SLA discipline (controls, reserves, telemetry) — it codifies how that discipline is communicated externally.

## Use When

- Section 11 (funding request) is being authored for an agent business with SLA commitments
- A round is opening and the pitch deck must include an SLA slide or paragraph
- A data-room SLA section is being assembled
- Quarterly investor updates must include an SLA block
- A board pack includes an SLA narrative section
- An investor Q&A about SLA is anticipated and rebuttals must be prepared
- Cross-loaded with `saas-agent-funding-stage-playbook`, `meta-agent-valuation-overlay-for-sla`, `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- The agent product has no SLA commitments — the narrative is moot
- The plan is pre-PMF and SLA discipline has not yet been built — work on the discipline first
- The round is grant-only (use `11b-grant-proposal`)

## Required Inputs

- Trailing 4-quarter SLA performance (uptime, accuracy, response time, DoD compliance) per tier
- Trailing 4-quarter SLA-credit issued ÷ agent revenue (credit ratio)
- Reserve methodology (formula + true-up cadence)
- Reserve adequacy history (actuals vs reserve drawn)
- Refund-reserve methodology (if outcome pricing)
- Dispute log (count, aging, resolution time, escalations to legal)
- Disclosure posture (published / audited / private / undisclosed)
- Audit firm engagement (Big-4 / regional / none)
- Peer SLA benchmarks (where public)
- Customer references quoting SLA performance
- Regulator engagement on SLA standards (where sector regulator is active)
- Insurance coverage (if any) for SLA exposure
- Recent SLA incident log (sev-1, sev-2, near-misses)

## Workflow

1. **Diagnose the current narrative position** — confidence-builder, neutral, or liability question. Use the dimension scorecard from `references/saas-agent-sla-investor-narrative.md`. Honest scoring; sceptical-investor lens.

2. **Identify the gap** — for each dimension where the score is below "investor-ready", note: is this a discipline gap (SLA discipline not built) or a communication gap (built but not communicated)? Treat these differently.

3. **Build the headline narrative**. Four standard openers, calibrated to score:
   - **Strong (3.5+):** "Our published SLA performance over the last four quarters has held at {x}% uptime, {y}% DoD compliance, with SLA-credit accrual at {z}% of agent revenue against a disciplined reserve methodology audited by {firm}. SLA is part of our moat — we publish and we deliver."
   - **Improving (2.5-3.4):** "Our SLA discipline is maturing. Last four quarters we moved from {prior} to {current} on uptime and from {prior} to {current} on credit ratio; reserve methodology now {auditor-reviewed / quarterly true-up} and we expect to publish by {date}."
   - **Building (1.5-2.4):** "We have committed SLAs in {n} of {m} customer contracts; our internal SLA telemetry shows {x}% uptime; we have built the reserve methodology and will engage an auditor in {quarter}; we expect to publish externally in {quarter}."
   - **Weak (<1.5):** Do not lead with SLA in the deck. Either rebuild discipline first, or position the round explicitly as use-of-proceeds for SLA discipline build.

4. **Build the moat-thesis paragraph** — if SLA is part of the moat (it usually is for vertical / regulated agents):
   - SLA is moat-relevant because: customer switching cost includes re-establishing SLA history with a new vendor; auditor and regulator engagement raises the floor for new entrants; published performance creates an anchor that competitors must beat
   - Cite specific examples: "{Enterprise customer X} renewed at {n}% expansion partly citing our SLA history" or "{Regulator Y} pre-cleared us partly on the basis of our SLA disclosure regime"
   - Reconcile with `saas-agent-moat-and-wrapper-risk` so the moat narrative is consistent

5. **Prepare the peer-benchmark slide / paragraph** — investors compare. Use public agent-vendor SLA disclosures (where available), DFI / multilateral published expectations, and sector-regulator-published expectations. Where direct peer data is unavailable, benchmark against:
   - Hyperscaler SLAs (AWS / Azure / GCP) for uptime
   - Enterprise SaaS SLAs (Salesforce / ServiceNow / Workday) for incident-credit ratios
   - BPO SLAs (Genpact / Concentrix / Teleperformance) for resolution time and quality
   - Vertical regulator SLA expectations (FCA, OCC, SEC, FDA, CBK, CBN, SARB, FSCA, etc.)

6. **Prepare the pitch-deck slide** — one slide. Headline: SLA performance + reserve discipline. Body: 4-quarter trend chart (uptime / accuracy / credit ratio); reserve methodology one-liner; disclosure posture one-liner; one customer testimonial reference quote.

7. **Prepare the data-room SLA section** — populate per `meta-due-diligence/references/saas-agent-sla-data-room-contents.md`. Contents: SLA policy memo; published performance; reserve methodology + true-up history; refund-reserve methodology; dispute log + aging; audit-firm engagement letter; customer SLA contracts (redacted); regulator correspondence (where applicable); insurance certificates (where applicable).

8. **Prepare the investor-update SLA block** — quarterly. Per `references/saas-agent-sla-investor-narrative.md` template. Three sentences: performance vs commitment; credit accrual + reserve adequacy; forward signal (next quarter expected performance + any policy change).

9. **Prepare FAQ rebuttals** — for the standard sceptical-investor questions:
   - "What if you have a catastrophic SLA breach?" — point to reserve adequacy + stress-tested scenarios + insurance (if any)
   - "Are customers gaming the SLA?" — point to gaming-detection controls + dispute escalation
   - "Is your reserve methodology audited?" — point to auditor engagement
   - "What if foundation-model pricing makes your SLA-tier unviable?" — point to vendor-cost pass-through clauses and FX corridor
   - "What if a regulator mandates a new SLA standard?" — point to regulator engagement + monitoring + repricing flexibility
   - "Why are you publishing SLA?" — answer: because investors and enterprise customers reward operational maturity; non-disclosure now signals weakness

10. **Wire to valuation overlay** — the SLA narrative connects to `meta-agent-valuation-overlay-for-sla` which quantifies the multiple effect. Pitch-deck pre-money should be reasoned through the overlay.

11. **Wire to bankability** — the SLA bankability checklist (`meta-bankability-scoring/references/saas-agent-sla-bankability-checklist.md`) is the structured evidence backing the narrative. Investor DD will test the bankability dimensions; narrative should match.

12. **Wire to the living plan** — assign cadence per below.

## Quality Bar

- Narrative position diagnosed honestly (not over-claimed)
- 4-quarter performance data shown (not curated)
- Reserve methodology cited explicitly
- Disclosure posture stated explicitly
- Peer benchmarks named (not "industry standard" handwave)
- Moat-thesis paragraph reconciled with overall moat narrative
- FAQ rebuttals prepared for the 6 standard questions
- Data-room SLA section populated before the round opens
- Investor-update SLA block adopted as standard quarterly format
- A sceptical investor would conclude either "operational maturity confirmed" or "honest about the build"

## Anti-Patterns

- "We have great SLAs" without numbers
- Cherry-picked best quarter; trailing performance hidden
- Reserve methodology not described
- Disputes hidden in the data room
- Disclosure posture vague ("we are working on it")
- Peer benchmarks unnamed
- Moat-thesis inconsistent with overall moat narrative
- Catastrophic-breach question dodged
- Insurance claim made without certificate
- Regulator alignment claimed without correspondence
- Publishing SLA performance "next quarter" for four quarters in a row
- Treating SLA narrative as marketing flourish rather than discipline evidence

## Outputs

- SLA narrative position (confidence-builder / neutral / liability question) with score
- Headline narrative paragraph (1-2 sentences)
- Moat-thesis paragraph on SLA (1 paragraph)
- Peer-benchmark slide / paragraph
- Pitch-deck SLA slide
- Data-room SLA section (populated)
- Quarterly investor-update SLA block
- FAQ rebuttals (6 standard questions)
- Cross-references to valuation overlay and bankability
- Living-plan cadence assignment

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| SLA-narrative score refresh | quarterly | CEO + CFO | -0.5 point quarterly |
| SLA pitch slide refresh | per round + quarterly | CEO + Head of GTM | performance-trend break |
| Investor-update SLA block | quarterly | CFO + CEO | missed quarter |
| Data-room SLA section refresh | quarterly + pre-round | CFO + Legal | DD opens |
| Peer-benchmark scan | quarterly | Head of Strategy | new public peer disclosure |
| FAQ rebuttal refresh | semi-annually + trigger | CFO + CEO + Legal | new sceptical question seen |
| Reserve-methodology disclosure refresh | quarterly | CFO + Auditor | true-up cadence |
| Audit-firm engagement status | quarterly | CFO + Board | status shift |
| Regulator-SLA-engagement comms | quarterly | Compliance + CEO | new consultation |

## References

- `references/saas-agent-sla-investor-narrative.md` — investor-update language + scoring rubric
- `skills/11-funding-request/saas-agent-funding-stage-playbook/SKILL.md` — funding stage parent
- `skills/meta-agent-valuation-overlay-for-sla/SKILL.md` — valuation overlay
- `skills/meta-bankability-scoring/references/saas-agent-sla-bankability-checklist.md` — bankability evidence
- `skills/meta-due-diligence/references/saas-agent-sla-data-room-contents.md` — data-room SLA section
- `skills/meta-agent-board-and-investor-reporting/references/saas-agent-sla-board-block.md` — board pack SLA
- `skills/01-executive-summary/references/saas-agent-sla-executive-summary-paragraph.md` — exec summary
- `skills/meta-agent-sla-financial-controls/SKILL.md` — controls evidence
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **DFI / multilateral lens** — IFC, AfDB, FMO, BII, Proparco, FCDO, USAID, GIZ now read SLA performance in agent-product DD. SLA narrative for DFI rounds should explicitly cite the development outcome that the SLA defends (e.g. "SLA on agri-advisory accuracy underpins farmer-income claim").
- **Sovereign-AI procurement lens** — KE Huduma, NG NIMC, RW Irembo, UG NITA-U, ZA Home Affairs and sector regulators (CBK, CMA, CBN, SEC, SARB, FSCA, BoU, CMA-UG, NDPC) increasingly include SLA schedules in tenders; investor narrative should cite the sovereign anchor as SLA-discipline evidence.
- **African insurer scrutiny** — African insurers (Britam, Sanlam, Old Mutual, Jubilee, ICEA Lion, Liberty, NIC, Heritage, Madison) vetting agent vendors look for SLA evidence; cite where an insurer has placed cover or named the vendor.
- **Peer benchmarking is thin** — published African agent SLA peer data is scarce; benchmark against global agent vendors plus African hyperscale (AWS af-south-1, Azure ZA, GCP africa-south1) plus African BPO majors (CCI Global, iSON Xperiences, Genesys SA, Africa's Talking voice infra).
- **FX-corridor in SLA narrative** — when local-currency revenue meets USD costs, the SLA narrative must reconcile FX-corridor clauses and reserve-currency choice; investors test this.
- **Reserve currency disclosure** — local-currency reserves vs USD-cost exposure; disclose the choice and the FX hedge (if any).
- **Mobile-money settlement reliability** — for per-resolution agents settling through MoMo / M-Pesa / Airtel Money / Wave / Orange Money / OPay, settlement-failure rate is part of SLA performance; disclose.
- **Local audit firm coverage** — where Big-4 unavailable, mid-tier (BDO, Grant Thornton, Mazars, RSM, PKF, Crowe, Baker Tilly) plus auditor-acceptable reserve methodology can still earn a confidence-builder narrative.
- **Public-sector reference value** — strong SLA performance on public-sector contracts (Huduma, NIMC, Irembo, NITA-U, Home Affairs analogues) is reference-grade for institutional investors; cite explicitly with consent.
- **Cross-border listing pathways** — JSE / NSE / NGX / EGX listings increasingly require SLA disclosure for tech issuers; narrative should anticipate listing-doc requirements where exit-via-listing is on the table.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria for saas agent investor narrative on sla | Financial model, implementation plan, client records, and target-financier materials | Yes | If absent, the funding gap, uses, repayment capacity, dilution effect, or stage evidence is unavailable, return a financing-readiness gap note and withhold the amount or instrument recommendation. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Investor SLA narrative linking service evidence, credits, reserves, trust controls, downside, and valuation implications | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent investor narrative on sla exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent investor narrative on sla release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Ask-to-use reconciliation, financing-option decision record, milestone release logic, and caveat register | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent investor narrative on sla decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent investor narrative on sla review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent investor narrative on sla, the controlling focus is SLA performance evidence, credit exposure, trust controls, reserve logic, and investor interpretation. This skill may analyse financing options and draft the ask; it may not solicit investors, submit applications, negotiate terms, value securities, or bind the client without explicit authority and professional review. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent investor narrative on sla, loss of evidence about SLA performance evidence, credit exposure, trust controls, reserve logic, and investor interpretation activates degraded mode. If the controlling saas agent investor narrative on sla evidence is unavailable, the same boundary applies. When the funding gap, uses, repayment capacity, dilution effect, or stage evidence is unavailable, return a financing-readiness gap note and withhold the amount or instrument recommendation. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent investor narrative on sla, the preferred instrument does not match cash-flow capacity, stage, security, or investor-return evidence| reject it, compare the viable alternatives, and state the milestone needed to reopen the option | A mismatched ask can create unaffordable debt, avoidable dilution, or failed diligence |
| For saas agent investor narrative on sla, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent investor narrative on sla decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent investor narrative on sla, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete investor sla narrative linking service evidence, credits, reserves, trust controls, downside, and valuation implications, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent investor narrative on sla decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce investor sla narrative linking service evidence, credits, reserves, trust controls, downside, and valuation implications with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Investor SLA narrative linking service evidence, credits, reserves, trust controls, downside, and valuation implications must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Ask-to-use reconciliation, financing-option decision record, milestone release logic, and caveat register must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent investor narrative on sla, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent investor narrative on sla, treating an unavailable reconciled funding need, use-of-funds schedule, financing capacity, traction evidence, milestones, and investor or lender criteria as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing investor sla narrative linking service evidence, credits, reserves, trust controls, downside, and valuation implications that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

Management cites a 99.95% uptime month without showing the measurement window or credits issued. Present the metric as unverified until monitoring, exclusions, and liability evidence reconcile.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent investor narrative on sla; no local deep-dive reference is declared.
- For saas agent investor narrative on sla claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
