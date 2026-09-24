---
name: prompt-techniques-john
type: reference
---

# Prompting Techniques for Business-Plan Work

Use this reference to choose and phrase a prompting technique for a business-plan task: drafting, analysis, stress-testing, extraction, ideation or tone control. The techniques are standard prompt-engineering practice (see, for example, John, 2023, and the wider literature); the groupings, patterns and business-plan examples below are the engine's own. Keep facts and figures in prompts sourced and dated; the model drafts, a person verifies.

## 1. Quick selector

| Goal | Techniques |
|---|---|
| Produce structured content quickly | Direct instruction, role, controlled output |
| Match a brand or author voice | Few-shot examples |
| Reason through a calculation or analysis | Step-by-step reasoning |
| Stress-test a section | Adversarial critique |
| Build content iteratively | Feedback rounds, staged build-up |
| Extract data from a document | Entity extraction, summarisation |
| Generate ideas | Open generation, clustering |
| Simulate a lender or investor interview | Dialogue simulation |
| Check reliability of an estimate | Self-consistency |
| Adjust tone without changing facts | Sentiment rewrite |

## 2. Setting the task

### Direct instruction
State the deliverable and its requirements. Pattern: "Write [format] that [does X]. It must [requirement], [requirement] and [requirement]."
Example: write an executive summary for a maize-flour processing business in a named town; state the funding request in the first paragraph, include the debt-service coverage figure, and keep it under 300 words.

### Role
Assign an expert perspective before the task. Pattern: "You are a [role] with [expertise] in [domain]. [Task]."
Example: you are a credit officer at a commercial bank reviewing small-business loan applications; identify the three weakest points in this executive summary.

### Plain request (zero-shot)
For simple, well-defined tasks, ask directly with no examples. Example: list five risks facing a poultry business in a named district.

### Controlled output
Fix vocabulary, structure and length. Pattern: "Write [content]. Use [reading level]. Avoid [banned words]. Each paragraph begins with [pattern]. Length [n]."
Example: write the risk-mitigation section at a plain reading level, avoid inflated words such as "robust", "leverage" and "synergy", present each risk as risk, likelihood, mitigation, and list exactly five risks.

### Soft style steer
Use a metaphor or feel to guide tone. Pattern: "Write [content] with the candour of [type of person]; it should feel like [description]." Example: founder narrative with the honesty of a trusted mentor, a conversation rather than a press release.

### Seed word
Anchor vocabulary and direction with a starting word. Pattern: "Write [content] on [topic]; start from the idea of [seed]." Example: an executive-summary hook for a solar business built on independence.

## 3. Showing examples

### One example (one-shot)
Give one sample, then the task. Pattern: "Here is an example of [output]: [sample]. Produce one for [new subject]." Use a sample executive-summary structure, then request one for another business type.

### Several examples (few-shot)
Give two to five examples separated by markers; the most reliable way to match voice and format. Pattern: "Here are [n] examples: ### [1] ### [2] ###. Produce [output] for [subject] in the same pattern." Use three sample risk-register entries then request five more; for voice matching, paste two or three real brand posts before requesting new ones.

## 4. Reasoning and reliability

### Step-by-step reasoning
Ask the model to reason before answering: "Think through this step by step before giving your answer", or list the steps (reasoning, analysis, conclusion). Example: a mill has annual earnings before interest, tax, depreciation and amortisation of 240 million and loan repayments of 180 million; work step by step to state whether it meets a 1.25 times debt-service coverage threshold and why. Verify arithmetic yourself.

### Self-consistency
Generate several independent answers, each from a different perspective, then keep what recurs. Pattern: "Give [three to five] independent responses to [question] from different perspectives; identify which elements appear in all." Example: three independent market-size estimates, then the most defensible figure with the reasoning.

### Knowledge generation
Have the model list relevant background facts first, then use them. Pattern: "Step 1: list [n] facts about [topic] relevant to [context]. Step 2: use them to write [output]." Example: five facts about a national poultry sector for an investor, then the industry overview. Check every generated fact against a source.

### Knowledge integration
Combine information from several sources into one coherent output. Pattern: "Integrate [source 1] and [source 2] into a single [output]; remove contradictions." Example: merge projections and market data into an executive-summary paragraph where growth claims are supported by the market data.

### Multiple choice with reasoning
Pose options and ask for a choice with justification. Pattern: "Which of these best achieves [objective]? A, B, C. Explain." Example: which loan structure suits a seasonal dairy processor (short term loan, overdraft, long term loan with grace period); justify with coverage principles.

### Question-and-answer build-up
Have the model answer a sequence of questions, then write from the answers. Example: what is the business, who does it serve, what problem does it solve, what is different; then write the executive summary.

## 5. Working with existing text

### Summarisation
Pattern: "Summarise [document] as [format], focusing on [aspects], maximum [length]." Example: five bullets from a market report covering size, growth and buyer behaviour.

### Entity extraction
Pattern: "Extract all [entity type] from [text]; present as a [table] with [columns]." Example: all financial figures, percentages and currency amounts, with context and source columns.

### Classification
Pattern: "Classify each [item] as [categories]; justify in one sentence." Example: rate each risk for probability and impact and place it in a two-by-two matrix.

### Clustering
Pattern: "Group these [items] into [n] clusters by [criterion]; name each and explain." Example: twenty article ideas into four clusters by buyer awareness stage.

### Sentiment rewrite
Pattern: "Assess the sentiment of [text]; rewrite it to [target tone] keeping every fact unchanged." Example: turn a cautious, apologetic risk section into a confident, solution-focused one without altering the risk data.

## 6. Stress-testing and simulation

### Adversarial critique
Pattern: "Here is [content]. Identify the weakest arguments and the objections a [sceptic, investor, lender] would raise, and how to pre-empt each." Example: the five strongest objections a bank credit officer would raise.

### Dialogue simulation
Pattern: "Simulate a dialogue between [role 1] and [role 2] about [topic]; role 1 asks, role 2 answers with data." Example: a bank interview with five questions on repayment security, the owner answering strictly from the supplied projections.

## 7. Building and refining

### Feedback rounds
Iterate: round 1 initial prompt; round 2 "keep [x], change [y], add [z]"; round 3 specific refinement. Example: tighten the funding request, add the coverage figure, remove passive voice in the last paragraph.

### Staged build-up (simple to complex)
Start with a one-sentence description, expand to a short paragraph adding audience and problem, then to a full summary adding the funding request and competitive advantage. Build whole sections from bullets, then paragraphs, then data and citations.

### Open generation
Pattern: "Generate [n] ideas or variations for [task]; explore broadly." Example: ten name options for a premium honey export brand aimed at European retailers, mixing English, local-language and hybrid names; check trademarks and meaning before use.

## 8. Good practice

1. Give context (business, place, audience, purpose) and constraints.
2. Supply the source data; do not ask the model to invent figures.
3. Ask for output in a fixed format so it can be reviewed.
4. Combine techniques (role plus controlled output plus few-shot).
5. Verify facts, arithmetic and citations; keep a human approval step.
6. Do not put confidential client data into tools without checking their data terms.

Sources consulted: John, I., The Art of Asking ChatGPT for High-Quality Answers (2023), and general prompt-engineering practice.
