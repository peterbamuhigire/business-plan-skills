# Procurement and Funding Gates in the Work Plan

Reference material for the implementation-timeline skill. Treats **procurement approvals and funding releases as BLOCKING gates** in a work plan or Gantt chart: nothing downstream that depends on a signed contract or a released tranche may be scheduled to start before its gate completes. Grounded in Ugandan public-procurement (PPDA) and NGO/donor practice.

This reference governs *sequencing and gating logic*, not statutory figures. **Do not hardcode statutory monetary thresholds (currency-point values, micro/quotation limits, advance-payment ceilings, retention percentages) as current — they change by regulation and must be verified against the current PPDA instrument and the controlling LG procurement regulation in force at the engagement date.** Carry lead times (working-day clocks) as planning defaults, not as guarantees, and verify the live instrument.

Substance authorities (cross-referenced for detail, not restated in full here):
- Procurement: `proposal-skills/skills/profiles-sectors/sectors/ppda-uganda/SKILL.md` and its references — `ppda-act-and-regulatory-framework.md`, `ppda-evaluation-forms-and-procedures.md`, `local-government-procurement.md`, `contract-management-and-payment-linkage.md`, `ngo-and-donor-procurement.md`.
- Public finance / commitment control: `chwezi-accounting-doctrine/doctrine/references/uganda-public-sector-pfm.md`.
- NGO / donor finance: `chwezi-accounting-doctrine/doctrine/references/uganda-ngo-financial-management-patterns.md`.

---

## 1. Procurement approval as a blocking gate (public bodies, PPDA)

For any work plan whose delivery depends on a procured supply, work, or service, the contract is not a background assumption — it is a **predecessor milestone** with its own internal clock. Nothing that consumes the contract (mobilisation, delivery, installation, handover) may start before the gate clears.

The award-to-signature clock (PPDA), in sequence:

1. **Evaluation** — the Evaluation Committee (approved by the Contracts Committee) runs the staged procedure: preliminary examination (pass/fail eligibility and administrative compliance) → detailed/technical evaluation (responsive or merit-point) → financial comparison → post-qualification. For the quotation method the standard schedule allows evaluation **within ~10 working days** of bid closing (verify against the current SRFQ user guide).
2. **Contracts Committee award** — the CC approves the evaluation report and authorises award; for two-envelope (QCBS/consultancy) methods the CC must first approve the technical report before financial envelopes are opened, adding a sequencing dependency.
3. **Notice of Best Evaluated Bidder (NOBEB) and standstill** — the BEB notice is displayed/communicated **within ~5 working days** of CC award; a **standstill of at least ~10 working days** from display runs before signature, preserving the complaints/review window.
4. **Attorney-General / Solicitor-General clearance (public)** — the contract requires **AG approval before signature** (a hard external dependency with its own queue and turnaround; treat as a named gate with an owner and a realistic lead time, not as instantaneous).
5. **Contract signature** — only after the standstill has expired *and* AG clearance is obtained. Signature is the gate that releases all downstream delivery work.

Plan each step as a milestone with an owner (PDU, Contracts Committee, Accounting Officer, AG chambers) and a lead time. A delay at any step pushes the entire downstream schedule; if a delivery milestone is drawn starting before signature, that is a critical-path error to flag, not a scheduling optimism to absorb.

> The full staged evaluation procedure, forms, the standstill, the Performance Securing Declaration, and the standard quotation schedule are in `ppda-uganda/references/ppda-evaluation-forms-and-procedures.md`; LG-specific procurement control in `local-government-procurement.md`.

---

## 2. Funding-release and commitment-control gates

A signed contract does not by itself authorise spend. A second, independent gate controls whether money may be committed in the relevant period.

**Public bodies (commitment control):**
- Budget authority flows **Grant of Credit → Minister's Warrant → Accounting Warrant** to the Accounting Officer, against the **quarterly expenditure/cash limit** (issued early each quarter under the PFMA). Appropriations expire at financial-year end; unexpended balances revert.
- **Commitment Control System (CCS) rule:** *no LPO, contract, or commitment may proceed without an approved commitment requisition and a sufficient uncommitted balance in the quarter's expenditure limit.* At LG level the Head of Finance is personally liable for over-commitment.
- Planning consequence: a milestone that is technically ready but falls in a quarter with no uncommitted budget is **blocked**. Phase milestones so each lands in a quarter that can carry its committed cost; a milestone that is certified-but-not-committed is the classic late failure — surface it before the date, not after.

**NGO / donor projects (disbursement tranches):**
- Donor funding arrives in **tranches** released against **conditions precedent** (signed agreement, inception report, prior accountability cleared, sometimes audit or registration conditions). The first tranche gates start-up; each subsequent tranche gates the next phase.
- Where the work serves a public body or uses both donor and GoU funds, **the stricter of the donor rule and the PPDA/CCS rule governs** — plan to the stricter gate.

> Commitment control, warrants, virement and vote-on-account detail: `uganda-public-sector-pfm.md` (§ Budget execution and commitment control). Donor disbursement and the stricter-rule test: `uganda-ngo-financial-management-patterns.md` and `ppda-uganda/references/contract-management-and-payment-linkage.md`.

---

## 3. NGO / donor programme cycles

Donor-funded work runs on programme phases, not open-ended calendars. Build the work plan to the cycle:

- **Programme phases** — commonly **6, 12, or 24-month** phases (or multi-year with annual workplans), each opened by a tranche and closed by reporting and accountability.
- **No-cost extension (NCE)** — where activities slip but budget remains, time can be extended without new funds **subject to donor approval before the original end date**. Treat the NCE request itself as a gated milestone (request → donor approval → revised end date), not an automatic right.
- **Reporting-driven tranche release** — the next tranche is not released until the prior period's narrative and financial reports are submitted and accepted. Reporting is therefore on the critical path between phases, not an after-the-fact formality.

> Sector-practice detail (deferred income, restricted funds, advance-at-a-time, donor acknowledgement windows): `uganda-ngo-financial-management-patterns.md`.

---

## 4. M&E reporting cycle as milestone checkpoints

The monitoring-and-evaluation cycle supplies the gate logic between phases and tranches. Render each review as an explicit checkpoint milestone:

- **Quarterly programmatic review** — outputs/outcomes against the logframe or workplan targets.
- **Quarterly financial review** — **budget-vs-actual** with variance measured against the **flexed budget** (donor budgets stated in donor currency and UGX; flexing uses a weighted-average disbursement rate, with exchange differences accumulated and explained). For public bodies, the equivalent is the appropriation/expenditure position against the quarterly limit.
- **Gate effect** — a quarter that misses programmatic targets or shows unexplained financial variance can **hold the next tranche or phase**. Draw the review as a go/no-go milestone that the following phase depends on, with the report submission as its predecessor.

This makes the reporting cycle a structural gate: report → review → acceptance → release, repeated each quarter/phase.

> Flexed-budget variance and the quarterly reporting set: `uganda-ngo-financial-management-patterns.md` (§ Multi-currency grant budgeting and flexing; § Records, audit, and governance).

---

## 5. How to render this in a Gantt / work plan

Show procurement and funding gates as **explicit predecessor milestones**, not as background assumptions buried in the narrative:

- **Give each gate a row.** Evaluation, CC award, NOBEB + standstill, AG clearance, contract signature, commitment requisition / tranche release, and each quarterly M&E checkpoint are milestone bars or diamonds in their own right.
- **Owner and lead time on every gate.** Name who carries it (PDU, Contracts Committee, AO, AG chambers, donor programme officer, Head of Finance) and the working-day lead time, drawn from §1–§4 — as a planning default to verify, never a guarantee.
- **Wire the dependencies.** Every delivery task that consumes a contract takes the **signature milestone** as a finish-to-start predecessor; every phase takes its **tranche/commitment** and the prior **M&E checkpoint** as predecessors. No delivery bar may start to the left of its gate.
- **Flag the critical-path risk.** Where a delivery milestone is scheduled against an approval that is not yet complete (signature pending AG, spend pending an uncommitted-balance check, phase pending a tranche), mark it as a critical-path risk on the chart, with the owner and the gate it waits on — do not absorb it as schedule optimism.
- **Stricter rule wins.** On blended public/donor work, gate to whichever regime (PPDA/CCS or donor conditions) clears last.

This turns the work plan from a calendar wish-list into an executable schedule in which approvals are visible, owned, and on the critical path.

---

## 6. Threshold and lead-time caveat

- **Monetary thresholds** (currency-point value, micro/quotation limits, advance-payment ceiling, regulation-set retention percentages) **change by regulation — verify against the current PPDA Regulations and the LG procurement instrument in force; never restate a figure here as current.**
- **Working-day clocks** (~10-day evaluation, ~5-day NOBEB display, ~10-day standstill, 30-day payment period) are framework defaults from the standard instruments — confirm against the live PPDA guide and the specific bidding document before committing dates in a plan.
- **LG procurement** is now governed by the consolidated **PPDA Regulations 2023** (the former Local Governments (PPDA) Regulations 2006 were revoked, effective 5 Feb 2024) — verify current monetary thresholds against the PPDA instrument in force, per `uganda-public-sector-pfm.md`.
