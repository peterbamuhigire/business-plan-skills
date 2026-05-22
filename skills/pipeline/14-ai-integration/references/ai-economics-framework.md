---
source: "Prediction Machines: The Simple Economics of Artificial Intelligence (Updated and Expanded Edition)"
author: "Ajay Agrawal, Joshua Gans, Avi Goldfarb"
year: 2022
publisher: "Harvard Business Review Press"
context: "Reference for the AI Integration section of business plans — Uganda/East Africa SME context"
---

# AI Economics Framework: Prediction Machines

## 1. The Core Thesis — AI = Cheap Prediction

The central insight of Agrawal, Gans, and Goldfarb is elegantly simple: **the current wave of AI does not bring general intelligence; it brings cheap prediction**.

When economists observe that prediction is becoming dramatically cheaper, they apply a standard framework: when the price of something fundamental drops, its use expands — in traditional applications and in entirely new ones. The internet made search, communication, and distribution cheap. AI makes **prediction** cheap.

> "Prediction is the process of filling in missing information. Prediction takes information you have, often called 'data,' and uses it to generate information you don't have."

This definition is deliberately broad. Prediction covers:
- Forecasting future events (demand, weather, defaults)
- Classifying present states (fraud detection, medical diagnosis, quality control)
- Inferring hidden information (customer intent, credit risk, equipment failure)

The economic analogy: just as cheap arithmetic (computers) enabled photography, music, and air-traffic control — tasks nobody thought of as arithmetic problems — cheap prediction will enable applications not currently thought of as prediction problems.

**Key implication for business plans:** Every business has prediction embedded in its operations. Founders should identify *where* those predictions live and ask whether AI can make them cheaper, faster, or more accurate.

---

## 2. The Anatomy of a Decision — Five Components

Agrawal et al. decompose every decision into seven elements. AI affects each differently:

| Element | What It Is | AI's Role |
|---|---|---|
| **Input Data** | Information fed to the algorithm to generate a prediction | Humans or sensors collect; machines consume |
| **Training Data** | Historical data used to build the predictive model | Must be assembled; quality determines model quality |
| **Prediction** | The output: filling in missing information | **AI increasingly replaces human prediction here** |
| **Judgment** | Determining the relative value of different outcomes and errors | Remains human; **increases in value as prediction gets cheaper** |
| **Action** | What is done in response to prediction + judgment | May be human or automated depending on stakes and speed |
| **Outcome** | The consequence — did it work? | Feeds back as new training/feedback data |
| **Feedback Data** | Outcome data used to improve the model over time | Critical for continuous improvement |

**The central point:** A prediction is not a decision. Prediction reduces uncertainty. Judgment assigns value to outcomes. Both are required before an action can be taken. AI handles prediction; humans handle judgment.

---

## 3. What Becomes MORE Valuable When Prediction Gets Cheap

When any input becomes cheap, the value of its **complements** rises. Prediction has three key complements:

### 3.1 Judgment
As AI takes over prediction tasks, human judgment becomes the scarce resource. Judgment is the skill of determining the *reward function* — the relative payoffs of different actions and outcomes. Examples:
- A credit card company's AI predicts fraud probability; a human (or hard-coded rule) judges whether the cost of blocking a legitimate card outweighs the cost of allowing fraud.
- A doctor's AI predicts a 66% probability of malignancy; the physician judges whether to order a biopsy given the patient's overall situation.

**"Reward function engineering"** — determining the weights that an AI should use — is described as a high-value, emerging human skill. It requires understanding both the organisation's objectives and the machine's capabilities.

### 3.2 Data
Data is the essential input to prediction machines. Three types matter:
- **Training data** — used to build the model (historical; consumed once)
- **Input data** — fed to the model at run-time to generate predictions
- **Feedback data** — outcome data used to improve the model continuously

Unique, proprietary data becomes a strategic asset — not because it has inherent value, but because it enables better predictions than competitors can make.

### 3.3 Action Capacity
The ability to act on predictions is the boundary of value creation. A prediction that demand will spike next week is worthless unless the business can actually stock the product. Whoever owns the action captures part of the AI's value. Traditional businesses retain an advantage here — they already own the logistics, relationships, and infrastructure that enable action.

---

## 4. What Becomes LESS Valuable

**Human prediction tasks** decline in value when machines predict equally well or better. Examples from the book:
- London taxi drivers who spent three years memorising routes ("The Knowledge") lost their advantage overnight when GPS navigation made equivalent prediction free.
- Baseball scouts whose subjective assessments of player potential were replaced by statistical models (the "Moneyball" case).
- Radiologists whose primary function — reading images — is increasingly matched by deep learning systems.

**Human information processing** at scale is also displaced. Tasks that involve reading large amounts of data and extracting patterns (document review, fraud monitoring, customer triage) are prime candidates for AI substitution.

**The bookkeeper analogy:** When spreadsheets made arithmetic cheap, bookkeepers did not disappear — their job transformed. They spent less time on calculation and more time on analysis and judgment. AI will do the same across many professions.

---

## 5. Workflow Redesign — Don't Automate the Old Way

The authors draw on the 1993 "reengineering" movement (Hammer and Champy) to make a critical point:

> "No manager is going to achieve large gains in productivity by just 'throwing some AI' at a problem or into an existing process. Instead, AI is the type of technology that requires rethinking processes."

The Ford accounts payable example: Ford hoped computers would help it match competitor Mazda's efficiency. Mazda had five people in accounts payable; Ford had five hundred. The answer was not to automate Ford's existing five-hundred-person process — it was to redesign the process around what computers could do, reducing the department by 75 per cent.

**The reengineering principle for AI:**
1. Identify the workflow objective
2. Break the workflow into constituent tasks
3. Identify the prediction element in each task
4. Estimate the ROI of AI for each task
5. Redesign the workflow — not just the task — around cheap prediction

**The AI Canvas** (a practical tool from the book):
For each task, specify:
- **Action** — what are you trying to do?
- **Prediction** — what do you need to know to decide?
- **Judgment** — how do you value different outcomes and errors?
- **Outcome** — what is your success metric?
- **Input data** — what feeds the prediction at run-time?
- **Training data** — what was used to build the model?
- **Feedback** — how do outcomes improve future predictions?

---

## 6. Tool vs. Transformation — Two Modes of AI Adoption

### Mode 1: AI as Productivity Tool (Operational)
AI slots into an existing workflow and improves one task's efficiency. Examples: email autocomplete, fraud detection, customer service chatbots, inventory forecasting. Returns are incremental. The strategy does not change.

**When this is appropriate:** When the prediction improvement is valuable but not large enough to alter the fundamental business model. Most early AI adoption by SMEs falls here.

### Mode 2: AI as Business Transformation (Strategic)
When a prediction machine becomes sufficiently accurate, it can tip the balance in a fundamental strategic trade-off, changing the business model itself.

The Amazon example: today's model is shop-then-ship (customer orders, Amazon ships). If AI can predict customer demand with enough accuracy, the model flips to ship-then-shop (Amazon ships proactively, customer ratifies). This requires not just better prediction but investment in new infrastructure (returns logistics), new data collection, and a new value proposition.

**Three conditions for strategic AI adoption:**
1. A core trade-off in the business model that creates friction or cost
2. That trade-off is driven by uncertainty (if you knew X, you would act differently)
3. A prediction machine can reduce that uncertainty enough to change the optimal strategy

**For SME business plans:** Articulate which uncertainty is limiting your business. Then ask whether any available AI tool reduces that uncertainty enough to change what you do.

---

## 7. Risk — Recoverable vs. Catastrophic Errors

Agrawal et al. introduce the concept of **stakes** — the expected losses when a prediction is wrong. The same error rate has very different consequences depending on the decision it informs.

| Scenario | Error Type | Consequence | Stakes |
|---|---|---|---|
| Amazon recommends wrong product | False positive | Customer searches again | Low |
| Facebook allows hate speech | False positive | Reputational damage, regulatory risk | High |
| Doctor's AI misses cancer | False negative | Missed treatment | Very high |
| Autonomous vehicle misidentifies obstacle | False positive | Accident | Catastrophic |

**The recoverable vs. catastrophic distinction:**
- **Recoverable errors**: The cost of the mistake is bounded and the customer/stakeholder can course-correct. AI can be deployed with less human oversight.
- **Catastrophic errors**: The cost of a single mistake can be existential — for a patient, for a brand, for a firm. Human oversight must remain in the loop until prediction accuracy crosses a high threshold.

**For Uganda/East Africa SMEs:** Most early AI applications (customer service chatbots, inventory forecasting, social media scheduling) involve recoverable errors. Be cautious about deploying AI in high-stakes contexts (medical advice, financial decisions, collateral assessment) without robust human review processes.

**The Amazon/Facebook contrast** (from the book): Amazon's product recommendation errors cost it a dissatisfied customer who will likely shop again. Facebook's content moderation errors — allowing harmful content — can cost it regulatory action, advertiser boycotts, and user exodus. Same error rate; entirely different stakes.

---

## 8. The New Division of Labour

Agrawal et al. identify four categories of prediction problems, each with different implications for the human-machine split:

| Category | Description | Human or Machine? |
|---|---|---|
| **Known knowns** | Rich data; prediction is reliable | Machine prediction dominates |
| **Known unknowns** | Sparse data; we know we cannot predict well | Humans remain essential |
| **Unknown unknowns** | Events not captured in past data (Black Swans) | Neither can predict; humans may reason by analogy |
| **Unknown knowns** | Correlations in data that reflect causation problems | Human judgment needed to avoid misleading the model |

**"Prediction by exception"** — the emerging model of human-machine collaboration:
- Machines handle routine predictions at scale, cheaply and continuously
- Humans intervene only when the machine flags an unusual case or low confidence
- This mirrors "management by exception" in traditional management

**What should remain human:**
- Judgment (assigning values to outcomes; setting the reward function)
- High-stakes decisions where errors are catastrophic
- Rare, novel situations without historical precedent
- Decisions requiring empathy, trust, or relationship context
- Cases where the data-generating process is not well understood

**Prediction machines can learn to predict human judgment** (through reinforcement learning on past decisions), but this works only where human decisions are numerous and observable. For rare, strategic decisions (mergers, new market entry, crisis response), machines lack the data to replicate human judgment.

---

## 9. First-Mover vs. Fast-Follower Strategy

The book uses the diffusion of hybrid corn in the US (1930s–1950s) as an analogy. Iowa farmers adopted early because:
- Their farms were large enough that the fixed cost of experimentation was justified
- Their profit margins gave them a buffer to absorb the transition cost
- Once enough farmers adopted, seed markets deepened and costs fell for everyone

**The AI parallel:**
- Large tech companies (Google, Meta, Amazon) are "Iowa" — they have the scale, data, and margins to invest early
- Most other businesses are "Alabama" — they will adopt later when costs have fallen and the technology is proven
- That is not necessarily a disadvantage; Alabama farmers eventually achieved the same yields

**Timing considerations for SMEs:**
- **Adopt early** if: your core business model has an uncertainty-driven trade-off that AI can resolve; competitors are already deploying; your data is perishable (customer behaviour changes quickly)
- **Wait** if: the current AI tools for your sector are immature; implementation risk is high; your margin does not support the transition cost

**The innovator's dilemma warning:** Incumbent businesses that wait too long may find that AI-native startups have built such an advantage in training data and model quality that catching up is prohibitively expensive. The whiff of disruption is a reason to move earlier, even at cost.

---

## 10. Practical Implications for Small Businesses Adopting AI

### 10.1 Start with the Prediction, Not the Tool
Identify the three or four predictions that most determine your business outcomes. Common ones for SMEs:
- Which customers will churn / return / refer others?
- What inventory will I need next week / month?
- Which leads are most likely to convert?
- What is the optimal price for this product in this context?
- Which supplier invoices are most likely to contain errors?

Then ask: is there an affordable AI tool that already makes this prediction? The answer is increasingly yes.

### 10.2 Data Before Deployment
A prediction machine without good data is useless. Before investing in AI, assess:
- Do you have historical data on the outcome you want to predict?
- Is that data digitised and accessible?
- Is it labelled (do you know the outcomes for past cases)?

For many Uganda SMEs, the first step is not AI adoption but **record digitisation** — getting transactions, customer interactions, and outcomes into a system that can feed a model.

### 10.3 Low-Stakes First
Begin AI deployment where errors are recoverable. Marketing personalisation, customer service chatbots for FAQs, inventory alerts, and social media scheduling all involve low stakes and offer useful learning.

### 10.4 Preserve Judgment
Do not automate high-stakes decisions without keeping a human in the loop. AI should surface predictions; humans should confirm actions where the cost of error is significant.

### 10.5 Workflow Redesign, Not Task Substitution
The productivity gains from AI come from redesigning workflows, not substituting AI for one step in an unchanged process. Ask: if this prediction were perfectly reliable and free, how would we redesign the whole process?

---

## 11. Worked Examples — Prediction Framework Applied to Common Business Functions

### 11.1 Customer Service
**Old workflow:** Customer contacts business → human agent triages → human agent answers
**AI-redesigned workflow:** Customer contacts business → AI predicts query type and intent → AI answers routine queries (80%) → human handles complex queries (20%) by exception
**What AI predicts:** Which queries can be resolved by a standard response
**Judgment stays human:** When to escalate; how to handle unhappy customers
**Uganda example:** A mobile money agent or SACCO can use a WhatsApp chatbot to answer balance queries, PIN reset instructions, and loan eligibility FAQs — freeing staff for relationship and credit management work

### 11.2 Inventory Management
**Old workflow:** Manager reviews past sales, makes an order estimate, adds safety stock buffer
**AI-redesigned workflow:** AI predicts demand by SKU for the next 2–4 weeks using sales history, seasonality, and local events → manager reviews flagged anomalies → orders placed
**What AI predicts:** Demand volume and timing
**Judgment stays human:** Supplier relationships; deciding when to stock a new product; managing cash-flow trade-offs
**Uganda example:** A maize flour distributor in Kampala can use Google Sheets with a simple forecasting add-in (e.g., Forecast Sheet) to predict weekly restocking needs based on 12 months of sales records

### 11.3 Marketing and Customer Segmentation
**Old workflow:** Send the same promotion to all customers; judge results manually
**AI-redesigned workflow:** AI segments customers by purchase behaviour → personalised messages sent to each segment → AI tracks which messages drive conversion → model improves
**What AI predicts:** Which customers are likely to respond to which offer
**Judgment stays human:** Brand voice; ethical constraints; relationship with key accounts
**Uganda example:** A retail shop or agri-input dealer can use Mailchimp's AI segmentation to send different offers to frequent buyers vs. lapsed customers vs. new subscribers

### 11.4 Finance and Credit Assessment
**Old workflow:** Loan officer reviews application, checks references, makes subjective judgment
**AI-redesigned workflow:** AI scores applicant using transaction history, mobile money data, and behavioural signals → loan officer reviews AI score + reasoning + application → decision made
**What AI predicts:** Probability of repayment given applicant profile
**Judgment stays human:** Character assessment; guarantee quality; relationship context; overriding the model when it lacks key information
**Uganda example:** SACCOs and MFIs are beginning to use psychometric scoring (see women-financing-uganda.md) as an AI-adjacent tool; mobile money platforms can now provide transaction-based creditworthiness signals

### 11.5 Quality Control (Manufacturing / Agriculture)
**Old workflow:** Human inspector checks each unit or batch manually
**AI-redesigned workflow:** Camera + AI model detects defects in real time → human inspector reviews flagged items only
**What AI predicts:** Whether a unit meets quality specifications
**Judgment stays human:** Setting quality thresholds; handling borderline cases; deciding when to reject a whole batch
**Uganda example:** A coffee processor or dairy plant can use a smartphone-based image recognition app to flag defective beans or quality-control issues before export packaging

---

## 12. AI Integration for Uganda/East Africa SMEs

### 12.1 Infrastructure Realities
Uganda and East Africa present a distinct operating environment for AI adoption:
- Mobile connectivity is widespread (MTN, Airtel, Safaricom) but data costs matter
- Electricity reliability is variable outside Kampala; cloud-dependent tools need fallback
- Smartphone penetration is growing; feature phones still common in rural areas
- Digital literacy varies significantly between urban and peri-urban operators
- Most SME financial records are informal or paper-based (see informal-business-records.md)

**Implication:** The most appropriate AI tools for Ugandan SMEs in 2025/26 are:
- Mobile-first (WhatsApp, USSD, SMS-based interfaces)
- Low-data or offline-capable where possible
- Pre-trained models (not requiring the SME to build its own AI)
- Integrated with existing platforms (MTN MoMo, Airtel Money, M-Pesa, Xero, QuickBooks)

### 12.2 Practical AI Tools Appropriate for Ugandan SMEs

| Function | Tool / Approach | Cost Level | Infrastructure Need |
|---|---|---|---|
| Customer communication | WhatsApp Business API chatbot | Low-Medium | Smartphone + data |
| Demand forecasting | Google Sheets Forecast function / Inventory management apps | Free–Low | Spreadsheet + records |
| Customer segmentation | Mailchimp AI segmentation | Free–Low | Email list |
| Social media content | ChatGPT / Claude for copy; Canva AI for visuals | Free–Low | Smartphone |
| Credit scoring (SACCO/MFI) | Psychometric tools; mobile money data analysis | Medium | Partnership with provider |
| Translation / language | Google Translate API; DeepL | Free | Internet |
| Voice/language interaction | Swahili/Luganda voice assistants (emerging) | Low | Smartphone |
| Image quality inspection | Google Vision API; custom mobile apps | Medium | Smartphone camera |
| Bookkeeping support | Wave AI features; Xero analytics | Free–Medium | Internet |
| Market price intelligence | Digital marketplaces (Jumia, Jiji price monitoring) | Free | Internet |

### 12.3 Data Strategy for Low-Digitisation Environments
For Uganda SMEs beginning AI adoption, data collection is the first priority:
1. **Digitise transactions** — use mobile money records, M-PESA statements, or a basic POS as the starting dataset
2. **Record customer outcomes** — track which customers returned, which paid on time, which referred others
3. **Label historical data** — for a loan portfolio, mark which loans were repaid and which defaulted; this becomes training data
4. **Start small** — even 200–500 records is enough to detect patterns with basic tools

### 12.4 The East African AI Landscape
- Kenya leads in fintech AI (M-Pesa data scoring, Safaricom AI services)
- Uganda is developing its AI policy framework; NITA-U is the lead agency
- Rwanda is investing in AI infrastructure through Kigali Innovation City
- The EAC's common market (see eac-common-market-framework.md) creates a cross-border data environment that AI tools can leverage
- AfCFTA digital trade provisions will increasingly shape data sovereignty questions for AI-generated predictions crossing borders

---

## 13. AI Strategy Checklist for the Business Plan AI Section

Use this checklist when drafting Section 14 (AI Integration) of a business plan. Each item should be addressed or explicitly noted as not applicable.

### A. Foundation
- [ ] Identify the three to five key predictions that drive business outcomes (demand, credit risk, customer churn, quality, pricing)
- [ ] Assess current data availability: what records exist, are they digitised, are outcomes labelled?
- [ ] Map existing workflows and identify where prediction is embedded (even informally)

### B. AI Tool Selection
- [ ] List the specific AI tools the business will use (not "we will use AI" — name the tool)
- [ ] Confirm each tool is appropriate to Uganda/EA infrastructure (mobile-first, data cost, offline capability)
- [ ] Specify the prediction each tool makes and the input data it requires
- [ ] Identify the judgment that will remain with humans and who in the team holds it

### C. Implementation Mode
- [ ] State whether AI adoption is operational (task-level efficiency) or strategic (changes business model)
- [ ] If strategic: identify the core uncertainty being resolved and how the business model changes
- [ ] If operational: estimate the productivity gain and cost saving from AI deployment

### D. Risk Assessment
- [ ] Classify each AI application as low-stakes or high-stakes (can errors be recovered?)
- [ ] For high-stakes applications: specify the human oversight process
- [ ] Identify the algorithmic bias risks relevant to your customer base
- [ ] Note the data security measures protecting customer information

### E. Data and Learning Strategy
- [ ] Specify how training data will be obtained or built
- [ ] Specify how feedback data (outcomes) will be captured to improve the model
- [ ] Confirm that ownership of key data resides with the business, not a supplier
- [ ] State the timeline for moving from manual records to AI-ready data

### F. Competitive Positioning
- [ ] Assess whether competitors are using AI and at what stage
- [ ] Identify the first-mover advantage (if any) from early AI adoption in your sector
- [ ] Note any proprietary data that could sustain a prediction advantage over time

### G. Jobs and Workforce
- [ ] Identify which tasks will be automated and which roles will change
- [ ] Specify any training or reskilling required for existing staff
- [ ] Describe the new judgment-intensive roles that AI creates (reward function engineers, exception handlers, data stewards)

### H. Investment and ROI
- [ ] Estimate the cost of AI implementation (tools, data digitisation, training, integration)
- [ ] Estimate the return (cost saving, revenue increase, risk reduction)
- [ ] State the payback period and any assumptions underlying the projection

---

## 14. Key Quotations for Business Plans

These quotations can be cited in the AI Integration section to add credibility and framing:

**On the nature of AI:**
> "The new wave of artificial intelligence does not actually bring us intelligence but instead a critical component of intelligence — prediction." (Agrawal, Gans & Goldfarb, 2022, p.1)

**On cheap prediction:**
> "When the price of something fundamental drops drastically, the whole world can change." (2022, p.17)

**On complements:**
> "As machine prediction increasingly replaces the predictions that humans make, the value of human prediction will decline. But the other elements of a decision — judgment, data, and action — remain, for now, firmly in the realm of humans." (2022, p.8)

**On workflow redesign:**
> "AI is the type of technology that requires rethinking processes in the same way that [reengineering] did." (2022, p.14)

**On strategy:**
> "Some AIs will affect the economics of a business so dramatically that they will no longer be used to simply enhance productivity in executing against the strategy; they will change the strategy itself." (2022, p.2)

---

## 15. Cross-References Within This Skills Suite

- **03-products-services**: AI as a product feature; business model innovation — see `business-models-innovation-teece.md`
- **05-target-market**: AI-driven customer segmentation — see `uganda-consumer-demographics-2025.md`
- **07-marketing-sales-strategy**: AI content tools, Hero Narrative for AI-aware brand — see `social-business-brand-strategy.md`
- **08-operations-plan**: Workflow automation, bottleneck analysis — see `small-business-unconventional-strategy.md`
- **10-financial-projections**: AI-assisted financial modelling — see `financial-model-templates.md`
- **11-funding-request**: Demonstrating AI-readiness to lenders; CAMPARI criteria — see `11-funding-request/SKILL.md`
- **12-risk-analysis**: AI risk categories (bias, data security, model failure) — see `uganda-risk-context.md`
- **14-ai-integration**: `process-automation-readiness.md`, `uganda-ict-ip-guidelines.md`

---

*Source: Agrawal, A., Gans, J., & Goldfarb, A. (2022). Prediction Machines: The Simple Economics of Artificial Intelligence (Updated and Expanded Edition). Harvard Business Review Press. Cite as (Agrawal, Gans & Goldfarb, 2022) on first use; full bibliographic entry in plan appendices.*
