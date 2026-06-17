# Internal Control & Risk Management Framework — Document Blueprint

The reusable architecture for an internal-control and enterprise-risk deliverable, synthesised from real Ugandan financial manuals, COSO ERM (2017) / ISO 31000, the Whistleblowers Protection Act 2010, and the LG (Financial & Accounting) Regulations 2007. Use the chapter→skill map so control and fraud substance always comes from the finance engine, never improvised.

Finance-engine root: `C:\wamp64\www\chwezi-accounting-doctrine` (paths below are relative to it unless otherwise marked).

## Two documents, one source

A two-document split is usually worth it:

- **Internal Control Policy** — the short, board-/Audit-committee-owned *policy* document (control principles, the five COSO components, authority, appetite, accountability). 12–25 pages.
- **Internal Control & Risk Management Framework** — the long *operating* document (the control set by cycle, the risk register and method, fraud and whistleblowing procedures, monitoring, with forms and registers). 50–120 pages.

The Policy is the apex; the Framework operationalises it. Draft the Policy first, then expand each policy statement into Framework controls and procedures. A small entity may take a single combined document — keep the same chapter spine.

## Chapter map (and where the substance comes from)

| # | Chapter | Substance from finance-engine skill / reference |
|---|---------|--------------------------------------------------|
| 1 | Introduction, scope, definitions, control objectives, the COSO five components / ISO 31000 principles | `10-controls-governance-and-fraud/internal-controls-library`; `engagement-quality-and-plain-language-output` |
| 2 | Control environment & governance (Board, Audit/Risk committee, internal audit, control owners, tone at the top) | `10-controls-governance-and-fraud/internal-controls-library`; `engagement-quality-and-plain-language-output` |
| 3 | Segregation of duties & authorisation matrix | `internal-controls-library`; `doctrine/references/uganda-ngo-financial-management-patterns.md` |
| 4 | ICFR documentation (process narratives, risk-control matrices, walkthroughs, control testing) | `10-controls-governance-and-fraud/sox-style-icfr-documentation` |
| 5 | Control activities by cycle (cash/bank, procurement, payroll, fixed assets, grants) | `internal-controls-library`; the relevant subledger skills (`04-subledgers-and-operations/*`, `05-...`) |
| 6 | Fraud risk & forensics (fraud-risk assessment, red flags, journal-entry testing, Benford, vendor-employee match) | `10-controls-governance-and-fraud/forensic-accounting-and-anti-fraud` |
| 7 | Whistleblowing & ethics (intake, protection, conflict-of-interest, clearance-on-exit) | `10-controls-governance-and-fraud/whistleblowing-and-finance-ethics` |
| 8 | AML/KYC & suspicious-transaction reporting (where the entity handles donor/member funds or is a reporting entity) | `10-controls-governance-and-fraud/aml-kyc-and-suspicious-transaction-reporting` |
| 9 | Enterprise risk management (risk register, appetite, control self-assessment) to ISO 31000 / COSO ERM | `srs-skills/09-governance-compliance/04-risk-assessment`; `business-plan-skills/skills/pipeline/12-risk-analysis`; `internal-controls-library` |
| 10 | Monitoring & internal audit (continuous monitoring, internal-audit plan, evidence) | `06-close-consolidation-and-reporting/audit-pbc-and-evidence-management` |
| 11 | Public-sector overlay (pecuniary liability, surcharge, board of survey) — public/LG bodies only | `doctrine/references/uganda-public-sector-pfm.md` |
| 12 | Appendices: forms & registers pack, dated Statutory Schedule, version control | this blueprint + `doctrine/references/uganda-compliance-caveats.md` |

For a public/local-government body, layer chapter 11: pecuniary-liability/surcharge per the LG (Financial & Accounting) Regulations 2007, vote-book and commitment control, and the board of survey — all in `uganda-public-sector-pfm.md`. Omit it entirely for a private NGO/SME.

## Control set (render these as tables — every figure is a named client parameter)

### Segregation-of-duties matrix

The control chain is *request → check → approve → disburse → prepare accountability → review → approve accountability*. No person occupies two **adjacent** links; nobody approves or signs in their own favour; procurer ≠ approver ≠ inventory-keeper. Render as a matrix of duty (rows) against role (columns), marking who performs, who is barred, and the compensating control where a small team forces overlap.

| Duty / control link | Requester | Checker (Finance) | Approver (Budget holder) | Disburser (Cashier/Bank) | Accountability reviewer | Barred from |
|---|---|---|---|---|---|---|
| Initiate request | ✔ | | | | | approving own request |
| Verify & code | | ✔ | | | | approving, disbursing |
| Authorise | | | ✔ | | | disbursing, own-favour items |
| Disburse / sign cheque | | | | ✔ (any 2 of N) | | approving, requesting |
| Prepare accountability | ✔ | | | | | reviewing own accountability |
| Review & approve accountability | | | | | ✔ | preparing it |

### Authorisation matrix (keyed to amount)

Tiers keyed to amount: operational → management → board, with the **board owning the top threshold**. Every figure is a parameter.

| Spend band (parameter) | Operational | Management | Board / committee |
|---|---|---|---|
| Up to UGX [____] | Approve | Note | — |
| UGX [____] – [____] | Recommend | Approve | Note |
| Above UGX [____] | Recommend | Recommend | Approve |

### Control-activity matrix by cycle

For each cycle, state the risk, the control, the owner, the frequency, and the evidence. Bank/cash controls: dual-control mandate (e.g. 3 named signatories, any 2), pre-numbered vouchers/cheques/LPOs/GRNs, cheque books in the safe, banking intact, stamp PAID, surprise cash counts.

| Cycle | Key risk | Control | Owner | Frequency | Evidence |
|---|---|---|---|---|---|
| Cash & bank | Unauthorised / duplicate payment | Dual-signatory mandate (any 2 of [N]); pre-numbered cheques in safe; stamp PAID | Finance Manager | Per payment | Cheque register, voucher |
| Procurement | Collusion / split orders | ≥[3] quotations above threshold; committee award; procurer ≠ approver ≠ stores | Procurement lead | Per procurement | Bid analysis, LPO, GRN |
| Payroll | Ghost workers | Independent payroll review; HR-Finance master-data split | HR + Finance | Monthly | Payroll sheet, exception log |
| Fixed assets | Misappropriation | Tagged register; annual verification; disposal board approval | Asset custodian | Annual | Asset register, verification report |
| Grants | Ineligible / cross-charged cost | Fund coding; donor-rule check; restricted-fund reconciliation | Grants accountant | Per claim | Fund ledger, donor report |

### Reconciliation & monitoring cadence (parameters)

Bank reconciliation monthly; cash count month-end; petty cash monthly + surprise; stock semi-annual; fixed-asset register annual; control self-assessment per the stated cycle; internal-audit plan annual. Each cadence is a board-set parameter.

### Risk register template (ISO 31000 / COSO ERM)

| ID | Risk description | Category | Probability (1–5) | Impact (1–5) | Inherent score | Existing controls | Residual score | Owner | Mitigation / treatment | Monitoring & review date |
|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | … | Financial / Operational / Compliance / Fraud / Strategic | | | P×I | | | | Treat / tolerate / transfer / terminate | |

Pair the register with a **risk-appetite statement** (board-set tolerance per category) and a **control self-assessment** rhythm. For public bodies, add a pecuniary-liability/surcharge column linking realised losses to the responsible officer per the LG Regulations 2007.

## Standard forms / registers pack (appendix)

Risk register; conflict-of-interest register and annual declaration; control self-assessment checklist; exception / incident log; whistleblowing intake form (with protection notice per the Whistleblowers Protection Act 2010); fraud-incident report; segregation-of-duties confirmation; authorisation-matrix sign-off; bank-mandate schedule; surprise cash-count certificate; control-test working paper (ICFR walkthrough); internal-audit finding & action-tracker; staff clearance-on-exit form. Tailor the list to the entity's actual processes — do not ship forms or registers for processes it does not run.

## Parameterisation rule

Everything the entity must choose is a **parameter with an owner and a review date**, presented as a default-to-be-approved, not a hardcoded fact:

> "Bank mandate: **[N]** named signatories, **any [2]** to transact; high-value board-countersignature threshold **UGX [____]** (recommended default UGX 5,000,000) — set by the Board, reviewed annually."

Statutory and surcharge figures are NOT parameters — they live in the dated **Statutory Schedule** appendix and are verified against the live source register at issue (see `uganda-compliance-caveats.md`). The framework body references "the applicable rate per the Statutory Schedule" or "surcharge per the LG Regulations 2007", never a number.
