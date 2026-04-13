---
name: idea-testing
description: Test business ideas and risky assumptions before building them using structured experiments, evidence review, and persevere, pivot, or kill decisions.
---

# Idea Testing

## Use When

- Use when this skill is the primary workflow for the requested task.
- Use when creating, reviewing, or improving this skill's main artifact.
- Use when this output must align with adjacent sections, assumptions, or audience requirements.

## Do Not Use When

- Do not use when another section or meta-skill is the primary owner of the task.
- Do not use when the required inputs are unavailable and cannot be stated transparently as assumptions.
- Do not use for provider-specific UI behaviour; keep the workflow portable.

## Required Inputs

- Business, client, or proposal context relevant to this skill
- Country, audience, funder, or user context where relevant
- Available assumptions, evidence, constraints, and dependencies
- Adjacent section outputs where consistency matters

## Workflow

1. Clarify the objective, audience, and scope for this skill.
2. Gather the minimum required inputs and note any missing assumptions.
3. Read the referenced materials only as needed.
4. Produce or revise the artifact using the skill-specific method below.
5. Reconcile the output with adjacent sections, numbers, risks, and evidence.
6. Flag unresolved gaps, assumptions, or follow-up work.

## Quality Bar

- Output is specific, decision-useful, and not generic
- Assumptions are explicit where relevant
- Claims align with the rest of the plan, proposal, or workflow
- Wording is structured, concise, and audience-appropriate

## Anti-Patterns

- Generic filler that could describe any business or situation
- Hidden assumptions or unsupported claims
- Contradictions with financials, implementation, risk, or audience requirements
- Provider-specific operating assumptions embedded in the portable workflow

## Outputs

- The primary artifact or analysis owned by this skill
- Any key assumptions, open questions, and cross-skill dependencies


## Overview

Testing Business Ideas uses structured experiments to gather evidence before committing to building. Every business idea rests on assumptions  about desirability (do customers want itSection ), feasibility (can it be deliveredSection ), and viability (can it make moneySection ). Test the riskiest assumptions first with the cheapest experiments possible, increasing evidence strength as confidence grows.

**Business Design Loop:**
Ideate  Business Prototype  Assess risk  Experiment  Learn  Decide (Persevere/Pivot/Kill)  repeat

## Three Risk Types

| Risk | Question | Test when |
|------|----------|-----------|
| **Desirability** | Do enough customers want thisSection  | Always first  building something nobody wants is the most common failure |
| **Feasibility** | Can we actually build/deliver itSection  | Before investing in delivery infrastructure |
| **Viability** | Can we make money from itSection  | Before scaling  revenue must exceed cost |

Any experiment can test one or more risk types. Always prioritise desirability first.

## Test Card  Design Every Experiment

Before running any experiment, complete a Test Card:

```
We believe:        [the hypothesis  what we assume to be true]
To verify this:    [the experiment  specific action we will take]
We will measure:   [the metrics  what data we will collect]
We are right if:   [the criteria  specific pass/fail threshold]
```

After the experiment, complete a Learning Card:

```
We observed:       [what actually happened  raw facts]
From this:         [the insight  what it means]
Therefore:         [the next action  build, iterate, pivot, kill, or test more]
We need to:        [remaining open hypotheses to test next]
```

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
| Standup | Daily | 15 min | What did we testSection  What's blockedSection  |
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
