---
source: Agent-products business-plan audit (2026); engine synthesis
frameworks: [Agent ethics block; Sustainability KPIs; Section 16 template]
skill: 16-sustainability-strategy
cross-reference: [saas-agent-sustainability-and-ethics, saas-agent-risk-and-stress-test, meta-agent-bankability-and-investor-readiness]
---

# Agent Ethics and Sustainability — Section 16 Block

Use this block in Section 16 for any agent-product plan. Sits after standard SaaS / AI ethics-and-sustainability content. Full discipline in `saas-agent-sustainability-and-ethics/SKILL.md`.

## 1. Action accountability

For each action class:

| Class | Accountable party | Document |
|---|---|---|
| A — reversible info | Vendor for output quality; user for action taken | MSA |
| B — reversible transaction | Vendor for action; user for downstream consequence | MSA + audit log |
| C — soft-irreversible | Shared: vendor for execution; user / customer for authorisation | MSA + audit log + consent record |
| D — hard-irreversible | Customer or end-user via human-final; vendor for adherence to policy | MSA + audit log + signed consent + human-final record |

## 2. Human-final on Class D

Non-negotiable. Document the human-final UX, double-signing, and audit-log record per Class D action type.

## 3. Audit-log retention and queryability

- Retention: 3-7+ years (longer if sectoral)
- Immutability: cryptographic hash chain or equivalent
- Queryability: regulator-on-demand within agreed SLA
- Review cadence: monthly

## 4. Contestability / redress

- Affected party submits request via documented channel
- SLA for response (typically <72h)
- Remediation options: re-process; reverse where possible; compensate where not
- Escalation path
- Reporting cadence to regulators / board

## 5. Jobs-impact disclosure

Where the agent displaces or substantially modifies roles:
- Quantified impact estimate
- Re-skilling / redeployment commitment
- Engagement with labour representatives in regulated sectors
- Public disclosure if material

## 6. Sustainability KPIs

| KPI | Target | Cadence |
|---|---|---|
| Energy per resolved task (kWh-equivalent) | downward trajectory | quarterly |
| Cache-hit ratio | maximise | weekly |
| Model-mix downshift on routine | maximise | quarterly review |
| In-region inference share (if applicable) | per sovereign requirement | quarterly |
| Water for cooling (if in-region) | per facility benchmark | annual |
| Embodied carbon contribution | per facility benchmark | annual |

## 7. Local-language and channel access

For agents serving consumer / public-sector / multi-lingual markets:
- Language coverage roadmap
- Channel coverage roadmap (WhatsApp / USSD / SMS / IVR / web / voice / mobile-money)
- Accessibility commitment for low-literacy / low-bandwidth users

## 8. Training-data provenance

- Audit cadence: quarterly
- Licence registry maintained
- Customer-data not used for cross-customer training without explicit consent
- African-language data sourced with consent and proper licensing

## 9. Downstream-misuse controls

- Acceptable-use policy
- Abuse detection
- Rate-limits
- Kill-switch
- Reporting cadence

## 10. Insurance and indemnity alignment

- AI E&O coverage scope (document exclusions)
- Self-insurance reserve where coverage thin
- Indemnity terms in MSA aligned with action accountability

## 11. External review / certification

- Third-party AI ethics review (annual for vertical / regulated)
- Sector certification where applicable
- ISO / NIST / sectoral framework alignment

## 12. Cross-References

- Full skill: `saas-agent-sustainability-and-ethics/SKILL.md`
- Risk register: `saas-agent-risk-and-stress-test`
- Bankability: `meta-agent-bankability-and-investor-readiness`
- Africa context: `africa-agent-context-extension.md`

## 13. Africa-specific notes

- Jobs-impact in African public-sector deployments is politically consequential; transparent disclosure increasingly required
- Local-language coverage as accessibility commitment (Swahili / Hausa / Yoruba / Amharic / Luganda / Zulu / Xhosa / Wolof / Tigrinya / Lingala)
- Channel coverage including USSD / SMS / IVR is accessibility
- Contestability in vernacular, via voice, in-person where appropriate
- Training-data provenance via Lacuna Fund / Masakhane / Lelapa AI / Awarri standards
- Sovereign-AI / in-region inference as positive sustainability framing
- Insurance thin in Africa; reserve-based commitment
- External review options: Africa AI Safety Consortium; Lelapa AI partners; Mozilla African Innovation Mradi; university ethics boards
