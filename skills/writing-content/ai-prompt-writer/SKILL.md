---
name: ai-prompt-writer
description: Use when the user needs a prompt for ChatGPT, Claude, Gemini, Midjourney, Sora, or another external AI tool. Use content-writing for general copy and blog-writer for a complete article.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# AI Prompt Writer

## Overview

Use this skill to generate ready-to-use prompts or prompt-writing guidance for external AI tools. It is a utility layer for structured prompting, not a substitute for doing the underlying strategic or writing work inside this repository.

## Use When

- Use when the user needs a prompt for ChatGPT, Claude, Gemini, Midjourney, Sora, or another external AI tool.
- Use when training a team to write better prompts for recurring workflows.
- Use when the output should be a prompt package rather than the final artifact itself.

## Do Not Use When

- Do not use when the task can be completed directly inside the current workflow without a prompt handoff.
- Do not use vague prompting to cover for weak task definition.
- Do not assume one prompt format works equally well across all tools.


- Route to `content-writing` instead for general copy, or `blog-writer` for a complete article.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Ai Prompt Writer brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Target AI tool or tool category
- Intended task, output format, and audience
- Brand, country, or business context where relevant
- Any must-include constraints, style rules, or source material

## Workflow

1. Identify the target tool, task, and output type.
2. Clarify the audience, context, and constraints that the prompt must encode.
3. Choose the right prompt structure for that tool and task.
4. Draft the prompt so it is specific, testable, and easy to reuse.
5. Reconcile the prompt with any brand, business, or quality constraints.
6. Flag missing context that will weaken results.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the tested prompt specification and that the decision concerns which instructions and tests make the prompt usable.
- **Stop condition:** halt the affected conclusion if required evidence is missing (target tool, task, inputs, constraints, examples, and prohibited outputs) or if the work could lead to this identified risk: shipping a prompt that fabricates sources or exceeds tool permissions.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- The prompt is specific enough to drive high-quality output.
- Instructions fit the target tool rather than a generic AI abstraction.
- Constraints, audience, and quality requirements are explicit.
- The prompt can be reused or taught without further explanation.

## Anti-Patterns

- One-line generic prompts with no context or constraints.
- Prompt templates that mix incompatible tool expectations.
- Using prompt polish to avoid clarifying the real task.
- Handing off sensitive or high-stakes work without review instructions.
- Treating a generic ai prompt writer template as a conclusion. **Correction:** tie each choice to the named audience, evidence, and operating constraint.


- Applying the wrong neighbouring route to ai prompt writer. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Ai Prompt Writer deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- A ready-to-use prompt or prompt set
- Optional training guidance or prompt-writing pattern
- Any assumptions or missing context the user should resolve


Generate ready-to-paste prompts for any AI tool. Two modes:

- **Mode 1**  Instant prompt: user needs a prompt right now during a session
- **Mode 2**  Training guide: user wants to teach a team how to write AI prompts

---

## Mode 1: Instant Prompt Generation

### Step 1  Identify tool and task type

Ask (or infer from context):

1. **Target AI tool**  ChatGPT / Gemini / Claude / Midjourney / DALL-E / Firefly / Runway / Sora / other
2. **Output type**  text content / business document / image / video / other
3. **Purpose**  what the output will be used for (caption, business plan section, logo concept, product video, etc.)
4. **Audience and context**  who will see it; what brand, country, tone

If the user describes the need, infer the tool and proceed without asking.

---

### Step 2  Select technique and build the prompt

Use the selector table below. Then build using the appropriate formula.

| Output type | Default technique | Formula section |
|---|---|---|
| Marketing copy, captions, emails | Alpha-Beta-Gamma-Delta-Epsilon + framework | Section A |
| Business documents (plans, reports, proposals) | Instructional + context block | Section A |
| Image generation | Subject-Setting-Style-Composition-Mood | Section B |
| Video generation | Camera-Subject-Action-Setting-Style | Section C |
| Data analysis, strategy, reasoning | Chain-of-thought | Section A |
| Brand voice matching | Few-shot (examples-first) | Section A |

For advanced techniques (self-consistency, knowledge generation, NER, clustering, etc.) read `references/prompt-techniques-john.md`.

---

### Section A  Text Prompts (ChatGPT, Gemini, Claude, etc.)

#### The Alpha-Beta-Gamma-Delta-Epsilon Formula

Every high-quality text prompt contains five elements:

~~~text
Alpha    Role: "You are a [expert role] specialising in [domain] for [market]."
Beta     Context: brand name, audience, platform, tone, product/offer details
Gamma    Task: "Write [quantity] [format] using [framework]. [Length + required elements]."
Delta    Constraints: "Do not mention [X]. Do not use the word [Y]. Avoid [Z]."
Epsilon  Output format: "Present as [numbered list / table / plain text / JSON]."
~~~

**Business document variant**  for plans, reports, proposals, pitch sections:

~~~text
Alpha:   You are a [role] with expertise in [domain] writing for [audience/funder].
Beta:    [Business name], [industry], [country], [stage], [specific context].
Gamma:   Write [section name]. Include: [required elements as numbered list].
Delta:   Do not use AI cliches. Do not fabricate figures  use placeholders [X] where data is needed.
Epsilon: Use headers and bullet points. British English. Max [word count].
~~~

#### 7 Copywriting Frameworks (embed in Gamma)

| Framework | Structure | Best for |
|---|---|---|
| **PAS** | Problem  Agitate  Solution | Social captions, ads, landing pages |
| **AIDA** | Attention  Interest  Desire  Action | Email, long-form ads |
| **BAB** | Before  After  Bridge | Product launches, testimonials |
| **FAB** | Features  Advantages  Benefits | Product descriptions, pitches |
| **SSS** | Star  Story  Solution | Brand storytelling, case studies |
| **PPPP** | Picture  Promise  Prove  Push | Sales letters, DM campaigns |
| **AFOREST** | Alliteration/Facts/Opinions/Repetition/Examples/Rhetorical questions/Statistics/Three-part lists | Persuasive essays, presentations |

#### Few-Shot (Examples-First)  default for brand voice tasks

~~~text
Here are [23] examples of [content type] in the voice and style I want:
###
[Example 1]
###
[Example 2]
###
Now write a new [content type] about [topic] in exactly the same voice and style.
~~~

Three or more examples produce reliable voice matching. Adjectives alone ("warm, professional, witty") do not.

#### Chain-of-Thought  for strategy, analysis, reasoning tasks

Append to any prompt: *"Think through this step by step before writing your answer."*

Or for complex tasks: *"First identify the key issues. Then analyse each one. Then give your conclusion."*

---

### Section B  Image Generation Prompts (Midjourney, DALL-E 3, Adobe Firefly)

#### Midjourney formula

~~~text
[Subject description] + [setting/environment] + [art style / medium] + [composition] + [mood/lighting] + [parameters]
~~~

Parameters: `--ar 16:9` (landscape), `--ar 1:1` (square), `--ar 9:16` (portrait/mobile), `--v 6`, `--style raw`, `--q 2`

**Example  Business branding:**
~~~text
A confident Ugandan businesswoman in a modern Kampala office, reviewing a laptop screen, natural window light, editorial photography style, shallow depth of field, professional and warm mood --ar 16:9 --v 6
~~~

**Example  Product shot:**
~~~text
A jar of artisan honey on a wooden surface, scattered dried flowers, East African market backdrop, close-up macro photography, golden hour light, warm and natural mood --ar 1:1 --v 6 --style raw
~~~

#### DALL-E 3 formula (natural language)

DALL-E 3 responds better to descriptive sentences than comma-separated keywords:

~~~text
A [detailed description of subject and action], set in [environment], in the style of [art style or photographer], [lighting description], [mood or atmosphere], [colour palette if relevant].
~~~

**Example:**
~~~text
A smiling East African entrepreneur presenting to a small group in a bright co-working space in Nairobi, natural daylight, documentary photography style, warm and optimistic atmosphere, muted earth tones.
~~~

#### Adobe Firefly

Same as DALL-E 3 natural-language style. Add: `[no text]` if you do not want text in the image, and specify `[photorealistic / illustrated / watercolour]` for style control.

---

### Section C  Video Generation Prompts (Runway Gen-3, Sora, Kling)

#### Formula

~~~text
[Camera movement] + [subject and action] + [setting/environment] + [visual style] + [mood/colour grading]
~~~

**Camera movement options:** slow push in, slow pull back, aerial drone shot, handheld tracking shot, static wide shot, low-angle dolly, panning left/right

**Example  Business/brand video:**
~~~text
Slow push in on a young Ugandan entrepreneur typing on a laptop at a rooftop cafe in Kampala at golden hour, warm cinematic colour grading, professional documentary style, optimistic mood.
~~~

**Example  Product video:**
~~~text
Close-up slow-motion shot of honey being poured from a wooden dipper into a glass jar, natural light, warm amber tones, artisan food film style.
~~~

**Runway-specific tips:**
- Keep prompts under 300 characters for Gen-3
- Specify exact duration: `[4 seconds]`, `[8 seconds]`
- Avoid complex scene changes in one prompt  generate separate clips

---

### Quality Checklist for Any Generated Prompt

Before handing the prompt to the user, verify:

- [ ] Role assigned (Alpha)  not generic
- [ ] Context specific  brand, audience, country, tone stated
- [ ] Task precise  format, quantity, length, framework named
- [ ] Constraints present  at least 2 things to avoid
- [ ] Output format specified  how to present the result
- [ ] No AI cliches in the prompt itself ("innovative", "seamless", "game-changing")
- [ ] Uganda/EA context used where relevant (UGX pricing, local references, cultural markers)
- [ ] Prompt is paste-ready  user can copy and run immediately

---

### East Africa Prompt Notes

- Always include `UGX [amount]` when price is relevant  never let the AI invent pricing
- For WhatsApp: add `plain text only, no markdown, no bullet symbols`
- For Luganda/Swahili: `Include one [Luganda/Swahili] phrase with English translation in brackets`
- Local references that work: boda-boda, rolex (Ugandan street food), market day, Kampala traffic, Lake Victoria, matooke, mobile money
- Avoid AI photo cliches: generic smiling call-centre staff, stock handshake photos, non-African faces in African context prompts

---

## Mode 2: Team Training Guide

When the user needs a full AI prompt-writing training programme for client staff, read `references/training-guide-modules.md` and generate the complete 4-module guide substituting all client details.

Ask for: business name, industry, country/city, team size, AI experience level, primary content types, preferred AI tools, training format.

---

## References

- `references/prompt-techniques-john.md`  24 Ibrahim John prompt techniques with formulas and business plan applications (John, 2023)
- `references/training-guide-modules.md`  Mode 2 full training content: Modules 14, all worked examples, East Africa context notes, quality criteria

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Tested prompt specification decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to shipping a prompt that fabricates sources or exceeds tool permissions. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the tested prompt specification; drafting and locally testing prompts without submitting private data externally is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If target tool, task, inputs, constraints, examples, and prohibited outputs cannot be obtained, return a qualified tested prompt specification covering only the checks that remain supportable. Leave this decision unresolved: which instructions and tests make the prompt usable. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which instructions and tests make the prompt usable | Record the conclusion, source trail, owner, and review trigger in the tested prompt specification. | Risk of shipping a prompt that fabricates sources or exceeds tool permissions |
| Material evidence conflicts or remains uncertain | Run both prompt variants on the same representative cases, including refusal and missing-input tests, and keep the simpler one that meets the rubric. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: target tool, task, inputs, constraints, examples, and prohibited outputs | Mark the decision on which instructions and tests make the prompt usable `not assessed` in the tested prompt specification, and send it to the prompt owner and tool-risk reviewer. | Otherwise, the work risks shipping a prompt that fabricates sources or exceeds tool permissions |

## Quality Standards


Accept the tested prompt specification only when evidence is sufficient for this decision: which instructions and tests make the prompt usable. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of shipping a prompt that fabricates sources or exceeds tool permissions.

## Worked Example


A research prompt asks the model to fill every missing statistic. Rewrite it to cite supplied sources, label gaps, refuse invention, and pass representative missing-input tests before handoff.

<!-- dual-compat-end -->
