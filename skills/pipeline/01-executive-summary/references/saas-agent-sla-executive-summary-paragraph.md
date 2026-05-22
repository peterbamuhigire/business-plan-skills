---
source: Agent SLA + commercial business-plan audit (2026); engine synthesis
frameworks: [Executive-summary SLA paragraph; archetype declaration; bankability-overlay reference]
skill: 01-executive-summary
cross-reference: [saas-agent-executive-summary-block, saas-agent-investor-narrative-on-sla, meta-agent-valuation-overlay-for-sla, meta-bankability-scoring]
---

# Executive Summary — Agent SLA Paragraph (Template)

For any agent-product plan with SLA commitments, the executive summary must include a one-paragraph SLA block. This block sits **after** the standard agent-executive-summary block (`saas-agent-executive-summary-block.md`) and **inside** the executive summary (one page max).

The SLA paragraph signals operational maturity to investors, auditors, DFIs, and enterprise procurement teams. Its absence is read as discipline-immaturity.

---

## Block 1 — The Commercial Archetype declaration (required)

```
### Commercial archetype
We operate {per-resolution under uptime + accuracy SLA / per-outcome under definition-of-done SLA / subscription + success-fee hybrid / prepaid task-credit / multi-tier SLA (bronze/silver/gold)} commercial archetype.
```

The archetype declaration is **required** because rev-rec policy, reserve methodology, COGS treatment, packaging logic, risk register and projection must align to it. The audit (`agent-sla-commercial-business-plan-audit-2026.md`) treats this as the anchor declaration.

---

## Block 2 — SLA paragraph variants by narrative position

Use the variant that matches the SLA narrative position (per `meta-agent-valuation-overlay-for-sla` scoring).

### Variant A — Confidence-builder (SLA score 3.5+)

```
### SLA discipline
Our published SLA performance over the last four quarters held at {99.x%} uptime, {97.x%} DoD compliance, with SLA-credit accrual at {z%} of agent revenue (against industry benchmark {y%}). Our reserve methodology — quarterly true-up under {auditor} concurrence — has tracked actuals within {variance%}. We publish performance externally on {status page} and our SLA discipline is part of our moat: {customer reference / regulator pre-clearance / sovereign-AI delivery / etc.}. Catastrophic-breach stress scenarios are modelled and reserved; insurance carries {coverage}. SLA bankability score: {n}/100.
```

### Variant B — Improving (SLA score 2.5-3.4)

```
### SLA discipline
Our SLA discipline is maturing. Last four quarters we moved from {prior} to {current} on uptime, from {prior} to {current} on DoD compliance, and from {prior%} to {current%} on SLA-credit accrual. Reserve methodology is documented and {auditor-reviewed / under auditor engagement} with quarterly true-up. We expect to publish performance externally by {date}. Catastrophic-breach scenarios are stress-tested with reserve coverage. SLA bankability score: {n}/100.
```

### Variant C — Building (SLA score 1.5-2.4)

```
### SLA discipline
We carry contractual SLA commitments on {n} of {m} customer contracts. Internal telemetry shows {x%} trailing uptime and {y%} DoD compliance. Reserve methodology is built and provisioned; we will engage {auditor} for concurrence in {quarter} and publish externally in {quarter}. SLA-discipline build is a stated use-of-proceeds priority for this round. SLA bankability score: {n}/100.
```

### Variant D — Weak (SLA score <1.5)

If SLA narrative is at this position, the SLA paragraph should **not** lead the executive summary. Instead the round narrative should explicitly frame SLA-discipline build as a primary use-of-proceeds item, with the SLA paragraph deferred to Section 11 (funding request) and Section 10 (financial projections). The executive summary should not over-claim.

---

## Composition with the standard agent exec-summary block

The standard agent block (`saas-agent-executive-summary-block.md`) ends with **Bankability and valuation**. The SLA paragraph slots between **AI Safety and governance** and **Regulatory posture**:

```
### AI Safety and governance
{standard content}

### SLA discipline
{paragraph from variant A / B / C above}

### Commercial archetype
{archetype declaration from Block 1}

### Regulatory posture
{standard content}
```

Or, when space-constrained, fold the archetype declaration into the SLA paragraph as the opening sentence.

---

## Tone Notes

- **Numbers, not adjectives.** "99.82% uptime against 99.5% commit" beats "best-in-class uptime"
- **Cite the auditor by name** when possible (or "Big-4 / mid-tier auditor under engagement")
- **Acknowledge weakness honestly** (Variant B / C). Investors reward honesty more than overclaim.
- **Cross-reference** to Section 10 (rev-rec + reserve), Section 11 (funding narrative), and the SLA bankability score
- **One paragraph max.** Executive summary is one page total; SLA gets one paragraph.

---

## Anti-Patterns

- "We have great SLAs" without numbers
- Archetype declaration omitted
- Reserve methodology not mentioned
- Disclosure posture vague
- Auditor named without engagement letter behind it
- SLA bankability score omitted when it would be flattering
- Catastrophic-breach question dodged
- SLA paragraph that contradicts Section 10 (reserve) or Section 11 (narrative)

---

## Cross-References

- `skills/01-executive-summary/references/saas-agent-executive-summary-block.md` — standard agent exec block
- `skills/01-executive-summary/references/saas-ai-executive-summary-block.md` — AI-on-SaaS exec block
- `skills/01-executive-summary/SKILL.md` — exec summary parent
- `skills/11-funding-request/saas-agent-investor-narrative-on-sla/SKILL.md` — investor narrative
- `skills/meta-agent-valuation-overlay-for-sla/SKILL.md` — valuation overlay scoring
- `skills/meta-bankability-scoring/references/saas-agent-sla-bankability-checklist.md` — scorecard
- `skills/10-financial-projections/saas-agent-revenue-recognition/SKILL.md` — rev-rec policy
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Sovereign-AI archetype tie** — when the agent operates under sovereign-AI procurement, name the public-sector anchor in the archetype declaration (e.g. "per-citizen interaction under multi-tier SLA contracted with UG NITA-U / RW Irembo / KE Huduma")
- **FX-corridor disclosure in the paragraph** — when local-currency revenue / USD-cost exposure is material, add one clause: "FX-corridor clauses cover {x%} of contract base"
- **Mid-tier auditor naming** — acceptable in African contexts; do not imply Big-4 if not engaged
- **DFI co-investment signal** — when DFI co-investment is in the round, name the SLA-discipline evidence the DFI relied on (e.g. "IFC DD relied on Q4 reserve true-up and dispute discipline")
- **Public-sector reference** — naming a public-sector SLA-delivery reference materially lifts investor read; do so with consent
- **Insurance scarcity note** — where carrier coverage thin, the paragraph should say "self-insurance reserve of {USD k} backstops catastrophic exposure" rather than imply carrier coverage that doesn't exist
- **Mobile-money settlement note** — where per-resolution settles via MoMo / M-Pesa / Airtel Money / Wave / Orange Money / OPay, note settlement-reliability as adjacent to SLA performance
