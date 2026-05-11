---
source: ASC 606 / IFRS 15 implementation guidance; Big-4 SaaS policy memo practice 2024-2026; engine synthesis
frameworks: [Policy memo structure; Auditor-acceptance pack; Cross-reference discipline]
skill: meta-agent-revenue-recognition-policy
cross-reference: [saas-agent-revenue-recognition-policy-template (operational), saas-agent-credit-reserve-methodology, saas-agent-sla-cogs-policy]
---

# Revenue Recognition Policy Memo — Meta Template

The operational skill (`saas-agent-revenue-recognition`) provides the worked memo template per primitive. This meta-template is the **artefact discipline** — the structure that ensures the memo is auditor-ready as a standalone document.

## Memo cover

```
Company: {Company name}
Document: Revenue Recognition Policy Memo
Reporting framework: {ASC 606 / IFRS 15 / both}
Effective date: {YYYY-MM-DD}
Version: {N}
Prepared by: {CFO + Controller}
Reviewed by: {Auditor (if appointed); Audit Committee}
Next refresh: {YYYY-MM-DD}
```

## Section 1 — Executive summary
- 1-page summary of the policy
- Pricing primitives covered
- Material judgments
- Estimated impact on revenue (recognised vs gross)

## Section 2 — Scope and framework
- Pricing primitives in scope
- Reporting framework
- Effective date
- Predecessor policy (if updating)

## Section 3 — Pricing primitive analyses
For each primitive, the ASC 606 / IFRS 15 5-step analysis per the operational template:
- Contract
- Performance obligations
- Transaction price
- Allocation
- Recognition

## Section 4 — Variable consideration
- Inventory of variable components (SLA credits, refunds, rebates, success fees, breakage)
- Estimation method per component (expected value / most likely amount)
- Constraint methodology
- Reassessment cadence

## Section 5 — Principal-vs-agent
- Service flows reviewed
- Indicator analysis per flow
- Conclusion (gross or net)

## Section 6 — Contract modifications
- Modification policy
- Common modification scenarios

## Section 7 — Significant judgments
- Estimation uncertainty
- Sensitivity
- Disclosure language

## Section 8 — Worked examples
- One example per primitive
- Edge cases

## Section 9 — Disclosure
- Revenue recognition footnote draft
- Significant judgments footnote draft
- Contract balances footnote draft
- Performance obligations footnote draft

## Section 10 — Cross-references
- Contract templates
- Financial model
- Deferred revenue and reserve methodologies
- SLA-COGS treatment policy

## Section 11 — Refresh schedule
- Trigger events
- Owner

## Section 12 — Sign-off
- CFO sign-off
- Auditor concurrence (if obtained)
- Audit committee acknowledgement

---

## Memo discipline checklist

- [ ] Every pricing primitive in scope is covered
- [ ] Each primitive has a 5-step analysis
- [ ] Variable consideration is estimated and constrained
- [ ] Constraint is non-trivial (auditor will test)
- [ ] Principal-vs-agent analysis where applicable
- [ ] Contract-modification policy stated
- [ ] Worked example per primitive
- [ ] Disclosure language drafted
- [ ] Cross-references valid
- [ ] Auditor pre-review obtained (where appointed)
- [ ] Audit committee acknowledged
- [ ] Refresh cadence documented
- [ ] Filed in the data room

## Common audit findings to pre-empt

| Finding | Pre-emption |
|---|---|
| "Variable consideration not constrained" | Document the constraint calculation explicitly |
| "Principal-vs-agent not analysed for marketplace revenue" | Include the indicator-by-indicator analysis |
| "SLA credits treated as opex" | Reclassify as contra-revenue with disclosure |
| "Refunds treated as COGS" | Reclassify as contra-revenue |
| "Breakage recognised at expiry" | Apply proportional method with disclosure |
| "Contract-modification policy missing" | Add modification policy section |
| "Performance obligations not distinct" | Re-test the distinct criterion; document |
| "SSP not estimated" | Document SSP estimation method |

## Africa / Uganda overlay

- **IFRS 15 wording** — use "highly probable" for the constraint (not "probable" which is the US GAAP wording)
- **Local audit firm coaching** — mid-tier and local firms may need the worked-example walkthrough; offer it
- **VAT reconciliation appendix** — add an appendix showing VAT-output (on invoice / prepayment) vs revenue (on recognition) reconciliation; auditor will request
- **WHT and gross-up reconciliation appendix** — add an appendix
- **FX revaluation policy appendix** — document IAS 21 application
- **Public-sector collectability constraint** — explicitly state where DSO history exceeds threshold
