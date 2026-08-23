---
name: idea-testing
description: Use when a business idea, offer, or market hypothesis still needs proof. Use the relevant plan-section skill for section drafting.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Idea Testing

## Overview

Use this skill to test a business idea or major assumption before heavy execution. It structures experiments, evidence review, and decision rules so the team can persevere, pivot, or stop with discipline.

## Use When

- Use when a business idea, offer, or market hypothesis still needs proof.
- Use when risky assumptions should be tested before building, funding, or scaling.
- Use when the outcome should be an experiment plan or validation decision.

## Do Not Use When

- Do not use after decisive evidence already exists unless re-testing is needed.
- Do not mistake opinion gathering for disciplined validation.
- Do not continue testing forever when a clear decision threshold has been crossed.


- For `idea-testing`, route to the relevant plan-section skill instead when the request is section drafting rather than cross-section analysis.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Idea Testing brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Idea, hypothesis, or risky assumption to test
- Target customer and context
- Available evidence, resources, and time constraints
- Decision threshold for what counts as validation or failure

## Workflow

1. Define the exact assumption or idea being tested.
2. Choose the lightest credible experiment that can produce signal.
3. Set success, failure, and learning criteria before running the test.
4. Capture results and interpret them honestly.
5. Decide whether to persevere, pivot, or stop.
6. Flag what still remains unvalidated.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the assumption test card and that the decision concerns persevere, pivot, or kill after the experiment.
- **Stop condition:** halt the affected conclusion if required evidence is missing (named risky assumption, target user, and observable behaviour) or if the work could lead to this identified risk: building the product before testing the failure-prone assumption.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The test targets a real assumption, not a vague ambition.
- Success criteria are observable and decision-useful.
- The experiment is proportionate to the risk and stage.
- Outcomes lead to a clear next decision.

## Anti-Patterns

- Testing too many hypotheses at once.
- Running expensive experiments before cheap ones.
- Redefining success after seeing weak results.
- Confusing interest or compliments with willingness to pay or adopt.
- Treating a generic idea testing template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to idea testing. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Idea Testing deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A validation plan, experiment set, or decision memo
- Clear pass, fail, or pivot criteria
- Remaining unknowns and follow-up tests


## Overview

Testing Business Ideas uses structured experiments to gather evidence before committing to building. Every business idea rests on assumptions about desirability (do customers want it?), feasibility (can it be delivered?), and viability (can it make money?). Test the riskiest assumptions first with the cheapest experiments possible, increasing evidence strength as confidence grows.

**Business Design Loop:**
Ideate  Business Prototype  Assess risk  Experiment  Learn  Decide (Persevere/Pivot/Kill)  repeat

## Three Risk Types

| Risk | Question | Test when |
|------|----------|-----------|
| **Desirability** | Do enough customers want this? | Always first — building something nobody wants is the most common failure |
| **Feasibility** | Can we actually build/deliver it? | Before investing in delivery infrastructure |
| **Viability** | Can we make money from it? | Before scaling — revenue must exceed cost |

Any experiment can test one or more risk types. Always prioritise desirability first.

## Test Card  Design Every Experiment

Before running any experiment, complete a Test Card:

~~~text
We believe:        [the hypothesis  what we assume to be true]
To verify this:    [the experiment  specific action we will take]
We will measure:   [the metrics  what data we will collect]
We are right if:   [the criteria  specific pass/fail threshold]
~~~

After the experiment, complete a Learning Card:

~~~text
We observed:       [what actually happened  raw facts]
From this:         [the insight  what it means]
Therefore:         [the next action  build, iterate, pivot, kill, or test more]
We need to:        [remaining open hypotheses to test next]
~~~

See `references/test-learn-decide.md` for full templates, evidence strength guide, and Decide framework.

## Experiment Selection  Two Phases

### Phase 1: Discovery (go from uncertainty  initial direction)
Use cheap, fast experiments to learn whether you are solving a real problem for real customers. Aim for **1520 customer conversations** before drawing conclusions. Evidence from discovery is generally weak-to-moderate  it is directional, not confirmatory.

**Rule:** Start with exploration (interviews, observations). Layer in interest data (ads, landing pages, surveys). Use prototypes to test concepts quickly.

See `references/discovery-experiments.md` for all 20+ discovery experiments with EA adaptations.

### Phase 2: Validation (confirm direction with stronger evidence)
Once you have a clear direction, use higher-fidelity experiments that generate strong evidence  real actions, real payments, real commitments. These cost more but reduce risk significantly before full build.

**Rule:** Escalate fidelity progressively. Never skip directly to building  use Wizard of Oz, Concierge, or Presale to validate before investing in infrastructure.

See `references/validation-experiments.md` for all 15 validation experiments.

## Evidence Strength

Stronger evidence = more reliable signals. Always push for the strongest evidence your constraints allow.

| Weaker  Stronger | Examples |
|-------------------|----------|
| **Opinions**  **Facts** | "I would buy this"  actual payment made |
| **Say**  **Do** | Survey answer  click, sign-up, purchase |
| **One datapoint**  **Many** | 1 interview  20 interviews |
| **One experiment type**  **Multiple** | Survey only  survey + prototype + presale |

**Confidence levels:**
- **Not Really Confident**  opinions, one-off conversations, single data point
- **Somewhat Confident**  multiple interviews, landing page clicks, prototype feedback
- **Very Confident**  real purchases, LOIs signed, multiple experiment types aligned

## Decide: What to Do With Evidence

After each experiment, decide:

| Evidence says | Decision |
|---------------|----------|
| Clearly refutes hypothesis | **Kill or Pivot**  change the offer, segment, or business model |
| Clearly supports hypothesis | **Persevere**  test the next riskiest hypothesis at higher fidelity |
| Mixed / unclear | **Continue testing**  same hypothesis with stronger experiment |
| Unexpected new insight | **Pivot**  adjust direction based on what you actually learned |

**Pivot triggers:** customers want a different feature, wrong segment, pricing mismatch, delivery cost makes viability impossible.

**Kill triggers:** multiple experiments all refute desirability, feasibility is technically impossible, no viable revenue model found after thorough testing.

## Experiment Ceremonies (for ongoing testing)

| Ceremony | Frequency | Duration | Purpose |
|----------|-----------|----------|---------|
| Standup | Daily | 15 min | What did we test? What's blocked? |
| Planning | Weekly | 60 min | Prioritise next experiments; write Test Cards |
| Learning Review | Weekly | 3060 min | Review Learning Cards; generate insights |
| Retrospective | Biweekly | 60 min | Improve the testing process itself |
| Stakeholder Review | Monthly | 90 min | Present evidence; investment/kill decisions |

## Funding by Stage (Innovation Portfolio Model)

| Stage | Budget | Team | Time | Experiment mix |
|-------|--------|------|------|----------------|
| **Seed** | <$50,000 | 13 | 2040% | 5080% desirability experiments |
| **Launch** | $50k$500k | 25 | 4080% | Mix: desirability + feasibility + early viability |
| **Growth** | $500k+ | 5+ | 100% | Prove model: viability + scaling experiments |

## EA Context Adaptations

- **Online ad platforms:** Facebook Ads dominates in Uganda; Google Search Ads for business-to-business
- **Email campaigns:** WhatsApp broadcast lists are more effective than email in most EA B2C markets
- **Presale / payment:** Use Mobile Money (MTN MoMo, Airtel Money)  more friction-free than bank transfer for small amounts
- **Pop-up stores:** KCCA market stalls, church/school trade fairs, roadside stalls  low permit cost
- **Letter of Intent:** Widely understood in Ugandan B2B and institutional procurement  especially for government/NGO buyers
- **Concierge MVP:** Ideal for service businesses  deliver manually first, automate once validated
- **Interviews:** In-person visits to potential customers are expected and welcomed; cold calls less effective than warm introductions

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| **Time Trap** | Running experiments when too busy | Carve out dedicated weekly testing time |
| **Analysis Paralysis** | Endless debate instead of testing | Time-box decisions; test reversible choices fast |
| **Confirmation Bias** | Ignoring evidence that conflicts with the idea | Create competing hypotheses; involve external reviewers |
| **Weak Evidence** | Only asking what people say; never observing what they do | Run call-to-action experiments |
| **Incomparable Data** | Testing different segments with different experiments | Define test subject and context explicitly on Test Card |
| **Too Few Experiments** | One experiment per hypothesis | Run multiple experiment types for each risky hypothesis |
| **Failure to Learn** | Testing without synthesis | Schedule Learning Review every week; write Learning Cards |
| **Outsourcing Testing** | Agency runs experiments on your behalf | Testing requires rapid iteration  build an internal team |

## Reference Files

- `references/test-learn-decide.md`  Test Card, Learning Card, evidence guide, decide framework
- `references/discovery-experiments.md`  All 20+ discovery experiments with EA adaptations
- `references/validation-experiments.md`  All 15 validation experiments with EA adaptations

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Assumption test card decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to building the product before testing the failure-prone assumption. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the assumption test card; recording experiments in the approved learning backlog is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If named risky assumption, target user, and observable behaviour cannot be obtained, return a qualified assumption test card covering only the checks that remain supportable. Leave this decision unresolved: persevere, pivot, or kill after the experiment. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: persevere, pivot, or kill after the experiment | Record the conclusion, source trail, owner, and review trigger in the assumption test card. | Risk of building the product before testing the failure-prone assumption |
| Material evidence conflicts or remains uncertain | Run the cheapest behaviour test that can falsify the assumption and set the pivot or stop threshold before collecting results. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: named risky assumption, target user, and observable behaviour | Mark the decision on persevere, pivot, or kill after the experiment `not assessed` in the assumption test card, and send it to the research lead and plan owner. | Otherwise, the work risks building the product before testing the failure-prone assumption |

## Quality Standards


Accept the assumption test card only when evidence is sufficient for this decision: persevere, pivot, or kill after the experiment. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of building the product before testing the failure-prone assumption.

## Worked Example


A founder plans six months of development for a supplier marketplace. First test whether ten target buyers will submit real orders under the proposed fulfilment terms, with the pivot threshold agreed before outreach.

## References

- [`AGENTS.md`](../../../AGENTS.md) - repository routing, evidence, finance, and release rules.

## Market-to-commitment validation ladder

Before expensive build or launch, test in stages: define the target user and
problem; inspect demand, trends, alternatives, and saturation; run interviews or
observation; test a concept/landing page; prototype or deliver manually; then
seek real use, payment, renewal, LOI, or another material commitment where
appropriate. Search volume, compliments, registrations, and portfolio examples
are signals, not validation.

For every stage record the hypothesis, sample/segment, behaviour, threshold,
guardrail, time window, decision, and remaining unknowns. Escalate evidence only
when the next investment decision requires it. This keeps validation reversible
and prevents a launch plan from substituting for product proof.

Practitioner cross-check: [Eleken product-idea validation](https://www.eleken.co/blog-posts/how-to-validate-product-ideas) and [UX ideas](https://www.eleken.co/blog-posts/ux-design-ideas); corroborating practice: [GOV.UK plan user research](https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service).

<!-- dual-compat-end -->
