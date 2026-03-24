---
name: prompt-techniques-john
type: reference
source: John, I. (2023) The Art of Asking ChatGPT for High-Quality Answers (Self-published)
---

# 24 Prompt Engineering Techniques (John, 2023)

Each technique below includes: description, formula, and a business plan / East Africa application.

---

## 1. Instructions Prompting

Give explicit, direct instructions about what to produce.

**Formula:** `Write [format] that [does X]. It must [requirement 1], [requirement 2], and [requirement 3].`

**Business plan use:** `Write an executive summary for a maize flour processing business in Gulu, Uganda. It must state the funding ask in the first paragraph, include a DSCR figure, and be no longer than 300 words.`

---

## 2. Role Prompting

Assign an expert persona before the task.

**Formula:** `You are a [expert role] with [X years / deep expertise] in [domain]. [Task follows.]`

**Business plan use:** `You are a Ugandan credit officer at Stanbic Bank reviewing SME loan applications. Identify the three weakest points in the following business plan executive summary.`

---

## 3. Standard Prompting (Zero-Shot)

Ask directly without examples or chain-of-thought. Best for simple, well-defined tasks.

**Formula:** `[Task instruction only]`

**Business plan use:** `List five risks facing a poultry farming business in Mbarara, Uganda.`

---

## 4. One-Shot Prompting

Provide one example before the task.

**Formula:**
```
Here is an example of [output type]:
[Example]
Now produce a [output type] for [new subject].
```

**Business plan use:** Provide one sample executive summary structure, then ask for a new one for a different business type.

---

## 5. Few-Shot Prompting

Provide 2–5 examples before the task. Most reliable method for voice and format matching.

**Formula:**
```
Here are [N] examples of [output type]:
###
[Example 1]
###
[Example 2]
###
Now produce a [output type] for [new subject] following the same pattern.
```

**Business plan use:** Show three sample risk register entries, then ask the AI to produce five more for a specific business. Voice matching: paste 2–3 real brand social posts before requesting new content.

---

## 6. Chain-of-Thought (CoT)

Ask the AI to reason through the problem before producing the answer.

**Formula:** Append `Think through this step by step before giving your answer.` or structure explicitly:
```
Step 1: [reasoning task]
Step 2: [analysis task]
Step 3: [conclusion / output]
```

**Business plan use:** `A maize flour mill in Gulu has annual EBITDA of UGX 240M and annual loan repayments of UGX 180M. Think through this step by step, then state whether this business meets the 1.25x DSCR threshold and explain why.`

---

## 7. Self-Consistency

Generate multiple independent answers to the same question, then select the most consistent or synthesise the best answer from all responses.

**Formula:** `Generate [3–5] independent responses to the following question, each from a different perspective. Then identify which elements appear consistently across all responses.`

**Business plan use:** Ask for three independent market size estimates for a business, then synthesise the most defensible figure.

---

## 8. Seed-Word Prompting

Provide a seed word or phrase that anchors the vocabulary and direction of the output.

**Formula:** `Write [content type] on [topic]. Use the following seed word/phrase as your starting point: [seed word].`

**Business plan use:** `Write an executive summary hook for a solar energy business. Seed word: independence.`

---

## 9. Knowledge Generation

Ask the AI to generate relevant background knowledge before completing a task, then use that knowledge.

**Formula:**
```
Step 1: Generate [N] facts about [topic] relevant to [context].
Step 2: Using those facts, write [output].
```

**Business plan use:** `Step 1: Generate 5 key facts about Uganda's poultry sector relevant to an investor. Step 2: Using those facts, write the Industry Overview section of a business plan.`

---

## 10. Knowledge Integration

Ask the AI to integrate information from multiple sources or domains into a unified output.

**Formula:** `Integrate the following information from [source 1] and [source 2] into a single [output type]. Ensure no contradictions and present a unified view.`

**Business plan use:** `Integrate the following financial projections and market analysis data into a coherent Executive Summary paragraph. Ensure the growth claims are supported by the market data.`

---

## 11. Multiple Choice Prompting

Present options and ask the AI to select and justify its choice.

**Formula:** `Which of the following [options] best [achieves objective]? Options: A) [X], B) [Y], C) [Z]. Explain your reasoning.`

**Business plan use:** `Which of the following loan structures best suits a small dairy processor in Mbarara with seasonal revenue? A) 12-month term loan, B) overdraft facility, C) 36-month term loan with 6-month grace period. Explain your reasoning using DSCR principles.`

---

## 12. Interpretable Soft Prompts

Use abstract or metaphorical language to guide the tone, feel, or approach of the output.

**Formula:** `Write [content] with the energy of [metaphor]. The writing should feel like [description].`

**Business plan use:** `Write the founder narrative with the honesty of a trusted mentor, not the polish of a PR department. It should feel like a candid conversation, not a press release.`

---

## 13. Controlled Generation

Specify exactly what vocabulary, structure, style, or content parameters the output must comply with.

**Formula:** `Write [content]. Use only [language level]. Do not use [banned words]. Each paragraph must begin with [pattern]. Length: exactly [X] words.`

**Business plan use:** `Write the risk mitigation section. Use plain language at a Grade 10 reading level. Do not use the words "robust", "leverage", or "synergy". Each risk must be presented as: Risk → Likelihood → Mitigation. List exactly 5 risks.`

---

## 14. Question & Answer (Q&A) Prompting

Frame the task as a series of questions the AI must answer, building toward the full output.

**Formula:**
```
Answer the following questions, then use your answers to write [output]:
1. [Question 1]
2. [Question 2]
3. [Question 3]
Output: [Final task]
```

**Business plan use:** Have the AI answer: What is the business? Who does it serve? What problem does it solve? What makes it different? Then generate the executive summary from the answers.

---

## 15. Summarisation Prompting

Condense long source material into a shorter, structured summary.

**Formula:** `Summarise the following [document / passage] in [format]. Focus on [specific aspects]. Maximum [length].`

**Business plan use:** `Summarise the following market research report in 5 bullet points relevant to a business plan for a Ugandan agri-processing company. Focus on market size, growth rate, and key buyer behaviours.`

---

## 16. Dialogue / Conversation Prompting

Structure the task as a simulated conversation or interview.

**Formula:** `Conduct a [role 1] / [role 2] dialogue about [topic]. [Role 1] asks questions; [Role 2] provides expert answers.`

**Business plan use:** `Conduct a simulated bank interview: the Credit Manager asks 5 questions about loan repayment security; the business owner provides convincing, data-backed answers. Base the business owner's answers on the following financial projections: [data].`

---

## 17. Adversarial Prompting

Challenge or stress-test existing content by asking the AI to argue against it.

**Formula:** `Here is [content]. Identify the weakest arguments and the most likely objections a [sceptic / investor / lender] would raise.`

**Business plan use:** `Here is our executive summary. Identify the five strongest objections a Ugandan commercial bank credit officer would raise about this application. For each, suggest how to pre-empt it.`

---

## 18. Clustering Prompting

Ask the AI to group a list of items into meaningful categories.

**Formula:** `Group the following [items] into [N] clusters by [criterion]. Name each cluster and explain the logic.`

**Business plan use:** `Group the following 20 blog post ideas into 4 clusters by buyer awareness stage (Unaware / Problem-Aware / Solution-Aware / Ready to Buy). Name each cluster.`

---

## 19. Reinforcement Learning from Feedback

Refine output through iterative feedback cycles. Each round, tell the AI what to keep, change, and add.

**Formula:**
```
Round 1: [Initial prompt]
Round 2: "Good. Keep [X]. Change [Y]. Add [Z]."
Round 3: "Better. Now [specific refinement]."
```

**Business plan use:** Draft an executive summary, then iteratively sharpen: tighten the funding ask, add the DSCR figure, replace passive voice in the final paragraph.

---

## 20. Curriculum Learning

Structure the prompts from simple to complex, building toward a complete output.

**Formula:** Start with the foundational task, then add complexity in subsequent prompts:
1. `Write a one-sentence description of [business].`
2. `Expand to a 3-sentence paragraph adding [audience] and [problem solved].`
3. `Expand to a 200-word executive summary adding [funding ask] and [competitive advantage].`

**Business plan use:** Build entire business plan sections progressively — start with bullet points, then expand to paragraphs, then add supporting data and citations.

---

## 21. Sentiment Analysis Prompting

Ask the AI to identify the emotional tone of text and revise it to match a target sentiment.

**Formula:** `Analyse the sentiment of the following text: [text]. Then rewrite it to achieve a [target sentiment] tone while keeping all factual content unchanged.`

**Business plan use:** `Analyse the sentiment of this risk section. Then rewrite it to be confident and solution-focused rather than cautious and apologetic, while keeping all risk data unchanged.`

---

## 22. Named Entity Recognition (NER) Prompting

Ask the AI to identify and extract specific types of entities from text.

**Formula:** `Extract all [entity type] from the following text. Present as a [table / list] with [columns].`

**Business plan use:** `Extract all financial figures, percentages, and UGX amounts from the following market research document. Present as a table: Figure | Context | Source.`

---

## 23. Text Classification Prompting

Ask the AI to assign items to predefined categories.

**Formula:** `Classify each of the following [items] as [Category A / B / C]. Explain each classification in one sentence.`

**Business plan use:** `Classify each of the following business risks as High / Medium / Low probability and High / Medium / Low impact. Present as a 2×2 risk matrix table.`

---

## 24. Text Generation Prompting

Open-ended creative or generative task with minimal constraint — useful for ideation.

**Formula:** `Generate [N] ideas / options / variations for [task]. No constraints — explore broadly.`

**Business plan use:** `Generate 10 possible names for a premium Ugandan honey export brand targeting European retailers. No constraints — include English, Luganda, and hybrid names.`

---

## Quick Selector — Which Technique to Use

| Goal | Best technique(s) |
|---|---|
| Produce structured content quickly | Instructions (1) + Role (2) + Controlled Generation (13) |
| Match a brand voice | Few-shot (5) |
| Reason through a calculation or analysis | Chain-of-thought (6) |
| Stress-test a business plan section | Adversarial (17) |
| Build content iteratively | Reinforcement Learning (19) + Curriculum (20) |
| Extract data from a document | NER (22) + Summarisation (15) |
| Generate ideas | Text Generation (24) + Clustering (18) |
| Simulate a lender/investor Q&A | Dialogue (16) |
| Check for consistency across multiple outputs | Self-consistency (7) |
| Adjust tone without changing facts | Sentiment Analysis (21) |
