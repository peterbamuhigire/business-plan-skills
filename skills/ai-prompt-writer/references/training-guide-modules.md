---
name: training-guide-modules
type: reference
source: Upadhyay (2024) Generative AI for Marketing (Packt); Mizrahi (2024); Evelyn (2025); Chavaux (2025)
---

# AI Prompt Writing Training Guide — Full Content (Modules 1–4)

Used by Mode 2 of the `ai-prompt-writer` skill. Substitute all bracketed placeholders with client details before delivering.

---

## Training Overview

**Programme:** AI Prompt Writing for Marketing Teams
**Duration:** Approximately 2.5 hours (150 minutes)
**Audience:** Marketing, communications, and content staff — any AI experience level
**Format:** [Insert: in-person half-day / virtual session / self-guided handout]
**Prepared for:** [Client Business Name]
**Industry:** [Industry]

---

## Module 1: Why Prompt Quality Matters (30 minutes)

### 1.1 What AI Can and Cannot Do

AI tools (ChatGPT, Gemini, Claude) are language prediction engines. They produce statistically probable text based on instructions. They do not:

- Know your brand unless you tell them
- Understand your audience unless you describe them
- Know what to avoid unless you specify constraints
- Default to quality — they default to *plausible*

They excel at: drafting at speed, generating variations, applying named frameworks, adapting tone on instruction.

### 1.2 The GIGO Principle (Anderson, 2022)

Garbage In, Garbage Out. Demonstrate live:

**Weak prompt:** `Write me a caption.` → Show generic output.

**Strong prompt:** `You are a social media copywriter for a Ugandan mobile money brand targeting market traders aged 30–50 in Kampala. Write one Instagram caption using the PAS framework (Problem → Agitate → Solution) for a new zero-fee transfer promotion. Under 150 characters. End with a call to action. No exclamation marks.` → Show the quality gap.

### 1.3 The Quality Gap

The gap between raw AI output and publish-ready copy is closed by:
1. Complete context (Beta)
2. Expert role assignment (Alpha)
3. Exact task + format (Gamma + Epsilon)
4. Explicit constraints (Delta)

### 1.4 Discussion Prompt

*"What is the worst AI output you have seen or produced? What was missing from the prompt?"*

---

## Module 2: The Alpha-Beta-Gamma-Delta-Epsilon Framework (45 minutes)

*Source: Upadhyay (2024), Chapter 3.*

### 2.1 The Five Elements

**Alpha — Role Assignment**

`"You are a [role] who specialises in [specialism] for [market/industry]."`

Without a role: generic, cautious output. With a role: confident, specific, industry-appropriate.

**Beta — Context Block**

Brand name + audience demographics + platform + tone/voice + product/offer details.

The more specific the Beta, the more tailored the result.

**Gamma — Task Instruction**

`"Write [quantity] [format] using [framework]. Each must be [length] and include [required elements]."`

Without a clear task: AI interprets ambiguity in its favour — generic, easiest interpretation.

**Delta — Constraints**

`"Do not [X]. Do not use the word [Y]. Avoid [Z]."`

Constraints remove AI defaults: "seamless", "affordable", "game-changing", "innovative solution".

**Epsilon — Output Format**

`"Present as [numbered list / table / plain text / JSON]. Label each [element] with [label]."`

Formatting makes output paste-ready and prevents burying content in prose.

### 2.2 The 10 Prompt Components (Upadhyay, 2024)

| # | Component | Description |
|---|---|---|
| 1 | Role assignment | Expert persona (Alpha) |
| 2 | Audience description | Demographics, psychographics, location |
| 3 | Platform / channel | Instagram, WhatsApp, email, LinkedIn |
| 4 | Objective | Awareness / engagement / conversion / retention |
| 5 | Tone instruction | Formal, friendly, witty, urgent, warm |
| 6 | Length / format | Character count, word count, list vs paragraph |
| 7 | Constraints | What to avoid — words, topics, brands |
| 8 | Context block | Brand, product, campaign background (Beta) |
| 9 | Few-shot examples | 2–3 examples of desired output style |
| 10 | Output structure | How to present the final result (Epsilon) |

Simple tasks: 4–5 components. High-stakes content (launch campaigns, CEO communications): all 10.

### 2.3 Common Mistakes

1. **Role missing** — output lacks expertise; reads like generic text
2. **Context too thin** — generic output, misses brand voice
3. **No constraints** — full of clichés
4. **No format instruction** — buried in paragraphs; needs reformatting

### 2.4 Hands-On Activity (15 minutes)

Participants build a complete prompt for their own brand using this template:

```
Alpha (Role):     You are a _______________________________________________
Beta (Context):   The brand is _____, targeting _____ aged _____ in _____. Brand voice: _____. Product/offer: _____.
Gamma (Task):     Write _____ using the _____ framework. Each must be _____ and include _____.
Delta:            Do not _____. Do not use the word "_____". Avoid _____.
Epsilon:          Present as _____.
```

Participants submit to AI and share output.

---

## Module 3: Copywriting Frameworks in Prompts (45 minutes)

Embedding a framework name in the Gamma element gives the AI a proven persuasion sequence to follow.

### 3.1 The Seven Frameworks

**PAS — Problem / Agitate / Solution**
- Structure: Identify pain point → make it emotionally vivid → present the answer
- Gamma instruction: `"Write using PAS: name the problem, agitate it (make it feel urgent or frustrating), then present the product as the solution."`
- EA example: Kampala fuel delivery — stuck in Ntinda traffic, empty tank, no station in sight → [Brand] delivers to your location in 30 minutes.

**AIDA — Attention / Interest / Desire / Action**
- Structure: Grab attention → build interest → create desire → prompt action
- Gamma instruction: `"Write using AIDA: open with a bold hook, develop interest, build desire with a benefit, close with a direct CTA."`
- EA example: Ugandan savings app — "Every week you delay costs more than you think." → auto-saves UGX 5,000 per transaction → thousands have saved their first UGX 1M → Download today.

**BAB — Before / After / Bridge**
- Structure: Painful before state → desirable after state → product as the bridge
- EA example: Nairobi laundry — before: washing on Sunday; after: clean, folded, delivered Saturday evening; bridge: [Brand].

**FAB — Features / Advantages / Benefits**
- Structure: Feature → functional advantage → customer benefit
- EA example: Ugandan solar system — 200W panel → powers lights, phone, small TV → children study after dark.

**SSS — Star / Story / Solution**
- Structure: Relatable character → their struggle → resolved by product
- EA example: Mama Zawadi, Dar es Salaam market vendor → son fell ill, closed stall, borrowed money → [Brand] covered the hospital bill; she never closed her stall again.

**PPPP — Picture / Promise / Prove / Push**
- Structure: Vivid image → specific promise → evidence → call to action
- EA example: Ugandan real estate — imagine your own gate → from UGX 120M → 400+ families moved in since 2021 → book your site visit this weekend.

**AFOREST** (persuasive device toolkit)
- Use selectively: Alliteration, Facts, Opinions, Repetition, Examples, Rhetorical questions, Statistics, Three-part lists
- Gamma instruction: `"Use AFOREST devices: include one rhetorical question, one statistic, and a three-part list."`

### 3.2 Embedding in Gamma

Pattern: `"Write [quantity] [content type] using the [FRAMEWORK] framework ([brief sequence description]). [Length, CTA, hashtag requirements.]"`

### 3.3 Hands-On Activity (20 minutes)

- **Exercise A:** Instagram caption using PAS for own brand. Run, review, refine once.
- **Exercise B:** Email subject line using AIDA for own brand. Compare 3 variations.

---

## Module 4: Prompt Library and Iterative Refinement (30 minutes)

### 4.1 Ready-Made Templates

Seven reusable prompt templates:

**1. Instagram / Facebook Caption**
```
Alpha: You are a social media copywriter for a [country] [industry] brand.
Beta: Brand: [X]. Audience: [demographics]. Platform: Instagram. Tone: [voice]. Offer: [product/promotion].
Gamma: Write 3 captions using the [FRAMEWORK] framework, each under 150 characters with a CTA and 2–3 hashtags.
Delta: No competitor mentions. No [banned words]. No exclamation marks.
Epsilon: Numbered list with framework label for each element.
```

**2. WhatsApp Broadcast**
```
Alpha: You are a WhatsApp copywriter for a [country] [industry] brand.
Beta: [Brand, audience, promotion details]
Gamma: Write one broadcast message using [FRAMEWORK]. Max 3 short paragraphs. End with "Reply YES to [action]".
Delta: No emojis. No markdown. No bullet points — plain text only. No "limited time".
Epsilon: Single plain-text message, paste-ready for WhatsApp Business.
```

**3. Email Subject Lines**
```
Alpha: You are an email copywriter for an East African [industry].
Beta: Re-engagement email to [audience segment]. Brand tone: [voice].
Gamma: Write 5 subject lines using AIDA, each under 50 characters.
Delta: Do not mention [sensitive topic]. Do not use the word "[banned word]".
Epsilon: Numbered list, subject line only, no explanation.
```

**4. Email Body (Short-Form)**
```
Alpha: You are an email copywriter for [brand].
Beta: [Audience, campaign context, offer details]
Gamma: Write one email body using BAB framework. Max 150 words. Include one CTA button label.
Delta: [Constraints]
Epsilon: Plain text with one [BUTTON LABEL] placeholder.
```

**5. LinkedIn Post (Thought Leadership)**
```
Alpha: You are a thought leadership copywriter for a [role/industry] professional in [country].
Beta: Author: [Name], [Title], [Company]. Audience: [LinkedIn audience]. Topic: [subject].
Gamma: Write one LinkedIn post using the SSS framework (Star/Story/Solution). 150–250 words. End with one reflective question.
Delta: No corporate jargon. No excessive hashtags (maximum 3).
Epsilon: Single paragraph post with 3 hashtags at the end.
```

**6. Blog Post Introduction**
```
Alpha: You are an SEO content writer for a [industry] business in [country].
Beta: Brand: [X]. Target reader: [persona]. Topic: [title]. Primary keyword: [keyword].
Gamma: Write a blog post introduction using AIDA (Attention hook → Interest/context → Desire/benefit preview → Action/read on). 100–150 words.
Delta: No "In today's fast-paced world". No "In this article". No AI clichés.
Epsilon: Plain prose, no headers, starts with the Attention hook directly.
```

**7. SMS / Short Copy**
```
Alpha: You are an SMS copywriter for a [country] [industry] brand.
Beta: [Brand, audience, offer]
Gamma: Write one SMS message under 160 characters including a CTA and opt-out line.
Delta: No special characters. No emojis.
Epsilon: Single line of plain text.
```

### 4.2 Five Prompting Approaches

| Approach | Description | Best for |
|---|---|---|
| Zero-shot | Single instruction, no examples | Simple, quick tasks |
| One-shot | One example before the request | Tone matching with one reference |
| Few-shot | 2–5 examples before the request | Brand voice, consistent series |
| Chain-of-thought | Reason step by step first | Strategy, analysis, calculations |
| Iterative refinement | Start broad, narrow with follow-ups | High-stakes content |

**Live demo — iterative refinement:**
1. Initial Alpha-Beta-Gamma-Delta-Epsilon prompt
2. `"Good. Shorten caption 1 to under 100 characters. Make the CTA more direct. Keep everything else."`
3. `"Replace the third hashtag with a more location-specific Ugandan tag. Do not change the rest."`

### 4.3 AI Content Quality Checklist

Before publishing any AI-generated content:

- [ ] Does it sound like a human wrote it?
- [ ] Does it match the brand voice guide?
- [ ] Are all facts and figures verified?
- [ ] Any AI clichés? ("game-changing", "seamless", "dive into", "in today's fast-paced world", "unlock", "leverage")
- [ ] Has a human editor reviewed and approved it?

### 4.4 East African Context Notes

- **WhatsApp**: conversational tone, short paragraphs, no markdown, clear opt-out
- **Local phrases**: `Include one Luganda phrase with English translation in brackets`
- **Length default**: under 150 characters for captions; under 160 characters for SMS
- **Local references**: boda-boda, rolex (street food), market day, Kampala traffic, KCCA, mobile money, Lake Victoria, supper culture
- **UGX pricing**: always provide in Beta — never let AI invent pricing
- **Avoid**: generic stock-photo language, non-African cultural references, AI filler phrases

### 4.5 Examples-First and Separator Syntax

**Examples-first default for voice tasks (Evelyn, 2025):**
```
Here is an example of [content type] in the voice and style I want:
###
[Example 1]
###
[Example 2]
###
Now write a new [content type] on [topic] in the same voice and style.
```

**### Separator** — any prompt containing both instructions and material to process must use `###` to separate them. Prevents AI from confusing instructions with content.

**Contextual continuity** — three rules for long sessions:
1. Use the same chat window per project
2. Re-state brand, tone, and audience every 6–10 exchanges
3. Reference previous outputs explicitly — never assume AI remembers

### 4.6 Q&A and Team Practice (10 minutes)

Participants write one prompt for real content they need this week. Share output for peer feedback.

---

## Worked Prompt Examples

### Example 1: Instagram Caption — PAS (Telecoms Brand)

```
Alpha: You are a senior social media copywriter specialising in Ugandan telecoms brands.
Beta: Brand: [X], targeting urban professionals aged 25–35 in Kampala. Voice: confident, friendly, slightly witty. Product: 5G bundle, UGX 15,000 for 5GB/7 days.
Gamma: Write 3 Instagram captions using PAS (Problem → Agitate → Solution). Each under 150 characters, with CTA and 2–3 hashtags.
Delta: No competitor mentions. No "affordable" or "seamless". No exclamation marks.
Epsilon: Numbered list with PAS label for each element.
```

### Example 2: Email Subject Lines — AIDA (Microfinance)

```
Alpha: You are an email copywriter for an East African microfinance institution.
Beta: Re-engagement email to customers inactive 90 days. Tone: warm, encouraging, professional.
Gamma: Write 5 subject lines using AIDA, each under 50 characters.
Delta: No mention of overdue balances. No "urgent".
Epsilon: Numbered list, subject lines only.
```

### Example 3: WhatsApp Broadcast — BAB (Delivery Service)

```
Alpha: You are a WhatsApp copywriter for a Kampala same-day delivery service.
Beta: Brand: [X]. Audience: small business owners aged 28–45 in Kampala. Tone: direct, reliable. Promotion: free delivery above UGX 50,000 this Friday.
Gamma: One WhatsApp message using BAB (Before → After → Bridge). Max 3 short paragraphs. End with "Reply YES to book your first delivery".
Delta: No emojis. No markdown. No bullet points — plain text. No "limited time".
Epsilon: Single plain-text message, paste-ready for WhatsApp Business.
```

---

## Quality Criteria

Training guide is complete when:

- All 4 modules included with time allocations totalling ~150 minutes
- Alpha-Beta-Gamma-Delta-Epsilon framework explained in full with ≥1 worked example per element
- All 7 copywriting frameworks named, defined, and illustrated with EA brand example
- Hands-on activities specified in Modules 2, 3, and 4
- All worked examples use Ugandan/EA brands, UGX pricing, local cultural references
- Structured for non-technical facilitator delivery without additional preparation
- Written in British English, imperative language throughout
