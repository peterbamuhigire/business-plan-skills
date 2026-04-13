---
name: ai-prompt-writer
description: Generate ready-to-use prompts for external AI tools and training guides for prompt-writing workflows used in planning, ideation, and content production.
---

# AI Prompt Writer

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

```
Alpha    Role: "You are a [expert role] specialising in [domain] for [market]."
Beta     Context: brand name, audience, platform, tone, product/offer details
Gamma    Task: "Write [quantity] [format] using [framework]. [Length + required elements]."
Delta    Constraints: "Do not mention [X]. Do not use the word [Y]. Avoid [Z]."
Epsilon  Output format: "Present as [numbered list / table / plain text / JSON]."
```

**Business document variant**  for plans, reports, proposals, pitch sections:

```
Alpha:   You are a [role] with expertise in [domain] writing for [audience/funder].
Beta:    [Business name], [industry], [country], [stage], [specific context].
Gamma:   Write [section name]. Include: [required elements as numbered list].
Delta:   Do not use AI cliches. Do not fabricate figures  use placeholders [X] where data is needed.
Epsilon: Use headers and bullet points. British English. Max [word count].
```

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

```
Here are [23] examples of [content type] in the voice and style I want:
###
[Example 1]
###
[Example 2]
###
Now write a new [content type] about [topic] in exactly the same voice and style.
```

Three or more examples produce reliable voice matching. Adjectives alone ("warm, professional, witty") do not.

#### Chain-of-Thought  for strategy, analysis, reasoning tasks

Append to any prompt: *"Think through this step by step before writing your answer."*

Or for complex tasks: *"First identify the key issues. Then analyse each one. Then give your conclusion."*

---

### Section B  Image Generation Prompts (Midjourney, DALL-E 3, Adobe Firefly)

#### Midjourney formula

```
[Subject description] + [setting/environment] + [art style / medium] + [composition] + [mood/lighting] + [parameters]
```

Parameters: `--ar 16:9` (landscape), `--ar 1:1` (square), `--ar 9:16` (portrait/mobile), `--v 6`, `--style raw`, `--q 2`

**Example  Business branding:**
```
A confident Ugandan businesswoman in a modern Kampala office, reviewing a laptop screen, natural window light, editorial photography style, shallow depth of field, professional and warm mood --ar 16:9 --v 6
```

**Example  Product shot:**
```
A jar of artisan honey on a wooden surface, scattered dried flowers, East African market backdrop, close-up macro photography, golden hour light, warm and natural mood --ar 1:1 --v 6 --style raw
```

#### DALL-E 3 formula (natural language)

DALL-E 3 responds better to descriptive sentences than comma-separated keywords:

```
A [detailed description of subject and action], set in [environment], in the style of [art style or photographer], [lighting description], [mood or atmosphere], [colour palette if relevant].
```

**Example:**
```
A smiling East African entrepreneur presenting to a small group in a bright co-working space in Nairobi, natural daylight, documentary photography style, warm and optimistic atmosphere, muted earth tones.
```

#### Adobe Firefly

Same as DALL-E 3 natural-language style. Add: `[no text]` if you do not want text in the image, and specify `[photorealistic / illustrated / watercolour]` for style control.

---

### Section C  Video Generation Prompts (Runway Gen-3, Sora, Kling)

#### Formula

```
[Camera movement] + [subject and action] + [setting/environment] + [visual style] + [mood/colour grading]
```

**Camera movement options:** slow push in, slow pull back, aerial drone shot, handheld tracking shot, static wide shot, low-angle dolly, panning left/right

**Example  Business/brand video:**
```
Slow push in on a young Ugandan entrepreneur typing on a laptop at a rooftop cafe in Kampala at golden hour, warm cinematic colour grading, professional documentary style, optimistic mood.
```

**Example  Product video:**
```
Close-up slow-motion shot of honey being poured from a wooden dipper into a glass jar, natural light, warm amber tones, artisan food film style.
```

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
