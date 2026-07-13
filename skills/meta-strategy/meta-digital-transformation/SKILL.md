---
name: meta-digital-transformation
description: Use when the client wants a digitally enabled growth strategy, operating model, or business-model redesign. Use the relevant plan-section skill for section drafting.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Digital Transformation Meta-Skill

## Overview

Use this meta-skill when a business plan or strategy needs a serious answer to the question: how should this business digitise and use technology in a way that is commercially justified, context-fit, and operationally realistic. It sits above `14-ai-integration` and helps ensure that AI recommendations live inside a broader digital strategy rather than replacing one.

## Use When

- Use when the client wants a digitally enabled growth strategy, operating model, or business-model redesign.
- Use when technology choices affect customer acquisition, fulfilment, service quality, data, or unit economics.
- Use when a plan needs to test platform, marketplace, subscription, or product-as-a-service opportunities.
- Use when digitisation investments need to be prioritised by business case rather than trend.

## Do Not Use When

- Do not use to bolt fashionable tools onto a weak business model.
- Do not use when the task only needs the AI section; use `14-ai-integration` for that narrower purpose.
- Do not recommend full digital transformation when the immediate problem is basic execution discipline or absent demand evidence.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Digital Transformation brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Current business model, offer, target customers, and growth objective
- Existing workflows, systems, channels, data, and digital tools
- Commercial pain points: acquisition, conversion, fulfilment, retention, leakage, reporting, or coordination
- Capacity, budget, team capability, and adoption constraints
- Country, infrastructure, and regulatory realities

## Workflow

1. Diagnose the current business model, customer journey, and operating bottlenecks.
2. Assess digital maturity across customers, competition, data, innovation, and value.
3. Identify digitisation opportunities across channel, process, data, service, and business-model layers.
4. Test whether the right move is workflow digitisation, platform participation, platform creation, subscription/access model, or simple systems discipline.
5. Prioritise options using practical business-case logic: value created, cost, risk, adoption burden, and time to benefit.
6. For software, SaaS, platform, or cloud-dependent businesses, assess DevOps maturity: release path, pipeline discipline, observability, incident response, security checks, backup/restore, and cloud cost control.
7. Produce a phased roadmap with owners, KPIs, dependencies, and handoffs to `14-ai-integration`, `10-financial-projections`, `11-funding-request`, and `13-implementation-timeline` as needed.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the staged digital-transformation roadmap and that the decision concerns which capability to digitise first and what to defer.
- **Stop condition:** halt the affected conclusion if required evidence is missing (customer problem, process baseline, data readiness, and investment case) or if the work could lead to this identified risk: funding technology that has no customer or operating mechanism.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Recommendations solve real customer or operating problems rather than decorating the plan with tech language.
- Digital choices fit the business stage, market context, and team capability.
- Data, channel, and process implications are explicit.
- Major technology bets have option logic, cost logic, and staged rollout discipline.
- Software and platform recommendations include operating capability, not just build features: delivery process, monitoring, support, incident learning, and security ownership.

## Anti-Patterns

- Equating digitisation with launching a website or buying software.
- Recommending AI before fixing process, data, or ownership.
- Assuming platform economics where network effects are absent.
- Treating digital transformation as capex with no adoption, governance, or KPI logic.
- Treating a generic digital transformation template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to meta digital transformation. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Digital Transformation deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Digital maturity and opportunity diagnosis
- Prioritised digitisation and business-model options
- Business-case-tested roadmap for technology investment
- Cross-references for execution, finance, funding, and AI follow-on work

## References

- `../../book-extractions/rogers-digital-transformation-playbook-extraction.md` - five-domain strategy lens: customers, competition, data, innovation, value
- `../../book-extractions/molenaar-demand-driven-business-strategy-extraction.md` - demand-driven redesign, outside-in thinking, value networks, platform logic, and product-as-a-service options
- `../../book-extractions/business-models-ecommerce-extraction.md` - digital transaction models, revenue logic, and supply-side/collaborative digitisation
- `../../book-extractions/haines-how-to-create-a-business-case-extraction.md` - options, do-nothing case, incremental economics, and sensitivity logic for major digital investments
- `../../book-extractions/devops-operating-model-extraction.md` - DevOps, CI/CD, release, observability, incident response, PHP/LAMP, cloud-native, and digital service reliability patterns for technology businesses
- `../14-ai-integration/SKILL.md` - use after the broader digital strategy is clear and the AI layer must be specified

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Staged digital-transformation roadmap decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to funding technology that has no customer or operating mechanism. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the staged digital-transformation roadmap; drafting the authorised roadmap without buying or deploying systems is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If customer problem, process baseline, data readiness, and investment case cannot be obtained, return a qualified staged digital-transformation roadmap covering only the checks that remain supportable. Leave this decision unresolved: which capability to digitise first and what to defer. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which capability to digitise first and what to defer | Record the conclusion, source trail, owner, and review trigger in the staged digital-transformation roadmap. | Risk of funding technology that has no customer or operating mechanism |
| Material evidence conflicts or remains uncertain | Compare the first-stage capability against the current manual process on customer outcome, control burden, adoption, and payback before sequencing it. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: customer problem, process baseline, data readiness, and investment case | Mark the decision on which capability to digitise first and what to defer `not assessed` in the staged digital-transformation roadmap, and send it to the process owner and investment sponsor. | Otherwise, the work risks funding technology that has no customer or operating mechanism |

## Quality Standards


Accept the staged digital-transformation roadmap only when evidence is sufficient for this decision: which capability to digitise first and what to defer. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of funding technology that has no customer or operating mechanism.

## Worked Example


A distributor requests an AI platform while orders still arrive through unstructured messages. Sequence order capture and clean product data first; approve later automation only after adoption and error-rate evidence.

<!-- dual-compat-end -->
