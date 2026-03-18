---
name: customer-retention-playbook
description: Comprehensive B2B customer retention framework covering retention economics (GRR/NRR/LTV/CAC), 5-tier customer segmentation, ICP validation, health scoring, churn risk mitigation, QBR methodology, account coverage models, renewal management, cross-sell/upsell playbooks, and customer advocacy programmes. Source: Umbrex Consulting LLC (2025).
type: reference
---

# Customer Retention Playbook
**Source:** Umbrex Consulting LLC, *Customer Retention Playbook* (Umbrex, 2025, ISBN 978-1-968040-49-9). 288 pages. Practitioner playbook with templates, checklists, and step-by-step guides.

---

## Chapter 1 — Retention Strategy & Economics

### The Strategic Imperative
Bain & Company research: raising customer retention by 5 percentage points lifts profits 25–95%. B2B firms often spend more acquiring a customer than the customer contributes in year-one revenue — making payback elusive unless the relationship endures.

Three macro trends intensify retention:
- **CAC inflation** — Acquisition costs up 30–50% over five years; acquisition rarely pays back without multi-year retention
- **Subscription/outcome-based models** — Revenue materialises over time; losing a customer mid-term vaporises contracted future cash flows
- **Investor scrutiny** — NRR, CAC payback, LTV/CAC now prioritised over topline growth; companies with NRR >120% trade at 50–100% higher EV/revenue multiples

### Key Retention Metrics

| Metric | Formula | Benchmark (B2B SaaS) |
|--------|---------|----------------------|
| **Logo/Customer Churn** | Customers lost ÷ Beginning customers | <5% annual (best-in-class) |
| **Gross Revenue Retention (GRR)** | (Beginning ARR − churn − contraction) ÷ Beginning ARR | ≥90% best-in-class; <85% = crisis |
| **Net Revenue Retention (NRR)** | (Beginning ARR − churn − contraction + expansion) ÷ Beginning ARR | >100% = growth from existing base; >120% = exceptional |
| **Expansion Revenue** | Incremental ARR from upsell/cross-sell/price increases | Should be 10–30% of total recurring revenue |
| **Contraction Revenue** | Downgrades and reduced usage | Track separately to prevent healthy-looking net figures hiding silent downgrades |
| **ARPA/ARPU** | Total recurring revenue ÷ active accounts | Monitor new-cohort vs. existing-cohort separately |
| **Customer LTV** | (ARPA × Gross Margin %) ÷ Revenue Churn Rate | Should exceed 3× CAC (investors prefer 5×+) |
| **CAC** | Total sales & marketing spend ÷ new logos acquired | Track separately for new business vs. upsell motions |
| **LTV/CAC Ratio** | LTV ÷ CAC | ≥3:1 acceptable; 5:1+ preferred by PE; >7:1 = under-investing in growth |
| **CAC Payback** | CAC ÷ monthly gross margin per customer | <12 months target; >18 months strains cash |

**Investor-grade metric checklist:** Report logo churn, GRR, and NRR monthly by cohort. Break out expansion and contraction separately. Segment ARPA by new vs. existing customers. Use gross margin (not revenue) for LTV and CAC. CAC payback below cost-of-capital horizon.

### Retention Economics Calculator — Core Model
Four-step cohort formula:
1. Project future ARR for static cohort (apply GRR and expansion rates)
2. Translate ARR to gross profit (multiply by gross margin %)
3. Discount to present value (apply WACC)
4. Subtract CAC to arrive at LTV

Build three scenarios (conservative/base/stretch). A 2-point improvement in GRR typically outperforms a 15% boost in new-logo bookings on every capital-efficiency metric.

**Tornado sensitivity:** GRR volatility usually dwarfs CAC volatility — highlight this before board meetings.

### Stakeholder Alignment (10-Step)
1. Frame the economic narrative (retention vs. acquisition capital trade-off)
2. Secure executive sponsorship (CEO or CCO with P&L authority)
3. Codify common metric stack across all functions
4. Map cross-functional roles and handoffs (swim-lane RACI)
5. Align incentives with NRR (AE: 10% commission at-risk until renewal; CSM: 30–50% bonus on NRR)
6. Build monthly Retention Steering Committee
7. Integrate retention into financial planning (set NRR/GRR targets first, then model bookings)
8. Activate real-time dashboard (GRR, NRR, logo churn, health scores by segment)
9. Embed retention in product roadmap (every feature must include "retention boost estimate")
10. Communicate and celebrate retention wins publicly

---

## Chapter 2 — Customer Segmentation & Prioritisation

### Five-Tier Retention Segmentation Framework
A retention-centric segmentation requires five dimensions (not just firmographics):

| Tier | Dimension | Key Question |
|------|-----------|-------------|
| 1. Structural Fit | Firmographic & technographic | Can this customer succeed with our product? |
| 2. Economic Value | ARR & gross margin contribution | How much cash does this account generate? |
| 3. Behavioural Signals | Product usage, feature adoption, login frequency | Are they actually using it? |
| 4. Relationship Health | NPS, CSAT, executive sponsorship | Do they value the relationship? |
| 5. Strategic Potential | Cross-sell paths, reference value, market influence | What is the intangible upside? |

**Composite weighting (typical):** Economic value 35–40%, behavioural health 30%, structural fit + relationship health + strategic potential share the remainder.

**Four actionable clusters:**
- **Strategic Growth Accounts** — High value, high health, strong expansion runway → intensive white-glove
- **At-Risk Revenue Blocks** — High value but deteriorating usage/sentiment → proactive save plays
- **Emerging Upside Cohorts** — Modest ARR but rapidly rising adoption → scalable nurture
- **Maintain-Efficient Segments** — Low value, low expansion potential → tech-touch automation

### Ideal Customer Profile (ICP)
Five pillars of a robust ICP:
1. **Firmographic fit** — Industry, company size, geography, growth stage
2. **Technographic compatibility** — Cloud providers, identity management, data warehouses (integration path determines time-to-value)
3. **Economic potential** — Contract length, OPEX/CAPEX budgeting, multi-year appetite (a smaller enterprise willing to sign 3-year expansions may be more valuable than a large brand requiring annual competitive bidding)
4. **Behavioural signals** — Usage depth in pilot, onboarding task completion, QBR responsiveness
5. **Strategic alignment** — Lighthouse credibility, new vertical access, advanced use-case influence

**ICP validation scoring (5-point scale):** Prospects averaging ≥4 across all dimensions are ICP-confirmed; ≤3 requires careful scrutiny before committing resources.

Key ICP questions:
- Does the primary pain align with your core value proposition (in top-3 strategic initiatives)?
- Can the solution deploy with out-of-box integrations or light customisation?
- Will end users interact weekly/daily (not just quarterly reporting)?
- Is budget authority centralised (eliminating multi-layer sign-offs that stall renewals)?
- Does the prospect's growth trajectory outpace inflation (expansion headroom)?
- Are executive sponsors personally invested and willing to act as references?

### High-Value Account (HVA) Identification Template
Seven scoring components:
1. **Financial contribution** — ARR, gross-margin dollars, contract term, billing cadence (weight gross margin >topline ARR)
2. **Expansion headroom** — Seat growth, module attach rate, white-space analysis (target 12–18 month expansion window)
3. **Risk exposure** — Concentration risk (flag any account >10% of ARR regardless of sentiment)
4. **Strategic value** — Brand credibility, lighthouse potential, co-marketing willingness (anchor to observable behaviours only)
5. **Product insight** — Beta feedback depth, advanced use cases (these are unpaid R&D partners)
6. **Relationship depth** — Number of active champions across functional levels (multithreading = leading indicator of retention resilience)
7. **Health & sentiment** — Usage health scores and NPS/CSAT

**Scoring:** Assign each component a weight; use 1–5 scale; aggregate composite HVA score. Platinum ≥4.0, Gold 3.5–3.9. Maximum three tiers to avoid diluting focus.

**Red flags:** High ARR + stagnating usage + no executive sponsor (silent churn risk); high strategic value + low margin + escalating support costs (repricing candidate); rapid-growth startups concentrated as high % of ARR (contingency planning required).

### Prioritisation Matrix (2×2)
**Axes:**
- Axis 1: Current gross margin dollars (or ARR)
- Axis 2: Future trajectory (either expansion potential OR churn risk — choose one)

**Four quadrants:**
| Quadrant | Description | Action |
|----------|-------------|--------|
| **Grow** | High value, high upside | Intensive success coverage, executive sponsorship |
| **Protect** | High value, low upside | Renewal specialists, proactive health checks |
| **Nurture** | Low value, high upside | Scalable programmes (webinars, usage campaigns) |
| **Streamline** | Low value, low upside | Tech-touch automation, cost-efficient support |

Assign named quadrant owners (VP Customer Success for Grow/Protect; Digital Success Director for Nurture/Streamline). Link compensation and OKRs to quadrant-specific KPIs. Run quarterly matrix audits to catch tier drift.

---

## Chapter 3 — Customer Journey Mapping & Onboarding

### Journey Mapping Methodology
**Start with research, not whiteboards:** Triangulate quantitative analytics (usage logs, support ticket tags, NPS comments) + qualitative interviews (champions, end users, detractors) + shadow sessions (observing real users).

**Journey spine — five macro stages:**
1. **Commit** (contract signed)
2. **Launch** (kickoff, configuration)
3. **Adopt** (reaching usage thresholds)
4. **Realise** (KPI improvement visible)
5. **Renew** (commercial decision)

At each stage gate specify: desired customer outcome, internal owner, time-bound success metric.

**Inventory and prune touchpoints:** Most B2B customers experience 30–50 touchpoints in year one; fewer than a third drive perceived value. Ruthlessly eliminate or automate the rest. Identify "moments that matter" — first login, first KPI visible in dashboard, first executive QBR — and choreograph these carefully.

**Friction/impact scoring:** Plot each touchpoint on a high-friction/low-impact vs. low-friction/high-impact grid. High-friction, low-impact steps → eliminate or self-service. Low-friction, high-impact moments → amplify.

### Onboarding Best Practices
- Anchor on a shared definition of "First Value" before kickoff (document in writing, display on onboarding dashboard)
- Define "Day 1 goals" and "Day 30 goals" in customer language
- Assign a dedicated CSM within 24 hours of contract signature
- Send a structured kickoff package: stakeholder introduction, timeline, pre-work checklist
- Use in-product guidance (tooltips, guided checklists) rather than PDF manuals
- "First 30 days" micro-campaign: drip sequence timed to feature milestones (Day 3 quick-win, Day 10 success story, Day 20 advanced shortcut, Day 28 power-user webinar invitation)
- Instrument real-time telemetry: activation events, frequency metrics, depth indicators

**Common onboarding pitfalls:** Inside-out design (building around the org chart, not customer jobs-to-be-done); overcomplication; lack of executive sponsorship; static artifacts that become wall décor.

---

## Chapter 4 — Voice of Customer & Feedback Loops

### NPS and CSAT Design Principles
- Ask the one-question NPS ("How likely are you to recommend…") + one open-ended follow-up
- Deploy at moments of truth: post-onboarding, post-support interaction, at renewal
- Segment NPS by tier, cohort, and product usage depth (enterprise NPS and SMB NPS often differ by 20+ points)
- CSAT: use after every support interaction; target ≥9/10 on resolved tickets
- VOC dashboard: NPS trend, CSAT trend, response rate, verbatim sentiment categories

### Continuous Feedback Loop (Four Steps)
1. **Capture** — Multi-channel listening: in-app surveys, support ticket tags, executive conversations, review sites (G2, Capterra), social media monitoring
2. **Analyse** — Code verbatim feedback by theme; link to product roadmap; identify top-3 friction sources per segment
3. **Act** — Route actionable feedback to accountable owners with SLA for response
4. **Close the loop** — Inform customers of actions taken ("You said, we did"); this alone improves NPS by 5–10 points

---

## Chapter 5 — Customer Health Scoring & Analytics

### Health Score Model Architecture
A health score combines multiple signals into a single actionable number (0–100 or traffic-light Red/Amber/Green).

**Signal categories:**
| Category | Weight (typical) | Key Signals |
|----------|-----------------|-------------|
| Product usage | 35–40% | DAU/MAU, feature breadth, session depth, API call volume |
| Relationship health | 20–25% | NPS, CSAT, executive sponsor status, responsiveness |
| Support activity | 15–20% | Open tickets, escalation frequency, ticket sentiment |
| Commercial risk | 10–15% | ARR at risk, days to renewal, contract terms |
| Engagement | 10–15% | QBR attendance, training completion, community participation |

**Early Warning Indicators (EWIs):**
- Usage drop >20% for two consecutive weeks
- No login from champion for 30+ days
- Support escalations trending up 3 weeks in a row
- Executive sponsor departure not replaced within 30 days
- NPS drop of 20+ points from baseline
- Payment delinquency >10 days
- Competitor evaluation signals (RFP, security review requests)

**Three-tier risk playbook:**

| Tier | Trigger | Owner | Resolution Target |
|------|---------|-------|-------------------|
| **Watch** | EWI flagged; no action taken in 7 days | CSM | 30 days |
| **At-Risk** | Two EWIs concurrent, or health score <60 | Senior CSM / CS Lead | 30 days from trigger |
| **Critical** | Renewal at risk >50%, explicit churn signal | VP Customer Success + Executive Sponsor | 30 calendar days or renewal date |

**Intervention lever menu (for each playbook tier):**
- Adoption levers: targeted training, workflow redesign sessions, admin coaching, short-form explainer videos
- Technical levers: dedicated solutions architect, hot-fix deployment, temporary feature flag
- Commercial levers: term extension discounts, license true-down with ramp-back, usage credits
- Relationship levers: executive business review, onsite visit, beta/advisory council inclusion
- Support levers: temporary SLA upgrade, named support engineer

**Track effort vs. outcome:** Time-to-Stabilise (TTS) and Cost-per-Save per playbook. Rank playbooks by ROI quarterly to refine or retire low-yield tactics.

---

## Chapter 6 — Escalation Path

Four-stage escalation ladder:

| Stage | Trigger | Response Time | Resolution Target | Decision Maker |
|-------|---------|--------------|-------------------|----------------|
| Stage 1 | Risk playbook fails | 24 h | 5 business days | Team Lead |
| Stage 2 | Stage 1 fails, or >7-figure ARR risk | 48 h | 10 business days | Directors |
| Stage 3 | Renewal risk >50%, C-suite exposure | 24 h | 30 calendar days | C-Suite |
| Stage 4 | >2% of ARR at risk, board visibility | 5 days | Board cycle | Board |

**Auto-promote logic:** If Stage 1 flag open on Day 6, CRM workflow automatically applies Stage 2 flag and notifies directors.

**Pre-approved concession menu:** Keep a concession menu available at Stage 3 so executives can decide in the meeting — not after. Define walk-away criteria in advance.

---

## Chapter 7 — Value Realization & Success Management

### Defining Customer Outcomes
- Capture the customer's "job-to-be-done" verbatim during discovery (this becomes the north star)
- Translate to 2–4 SMART KPIs with baseline values and mutually agreed data sources
- Value Realization Framework template:
  1. Objective Statement (one sentence)
  2. Baseline Metric (current state, source, timestamp)
  3. Target Metric (desired state, confidence interval, deadline)
  4. Value Calculation (formula: metric change → $ or hours)
  5. Ownership & Review Cadence
  6. Assumptions & Dependencies

### Success Plan Template (10 Sections)
1. Executive Overview (framed in customer's language)
2. Strategic Objectives & SMART KPIs (max 4, with baseline/target/deadline/owner/verification method)
3. Stakeholder Map (roles not names: Economic Buyer, Executive Sponsor, Technical Champion, Power Users, Data Owner/IT)
4. Milestone Roadmap (4–6 milestones tied to value moments; status: Not Started/In Progress/Complete/At Risk)
5. Enablement & Resource Plan (persona-specific: exec briefings, admin workshops, end-user micro-learning, IT Slack channels)
6. Risk & Dependency Register (running log with owner, due date, escalation path)
7. Communication Cadence (weekly tactical sync, monthly KPI pulse, quarterly QBR, ad-hoc war-room triggers)
8. Mutual Commitments & Success Metrics (both sides commit in writing; advocacy pathway if KPIs hit 120% of target)
9. Expansion & Advocacy Pathway (capture logical next steps as soon as value is proven)
10. Revision History & Governance (dual approval for scope changes, timeline shifts >2 weeks, or KPI redefinitions)

### Quarterly Business Review (QBR) — 10-Step Guide
| Step | Timing | Action |
|------|--------|--------|
| 1. Clarify objectives & audience | T−30 days | Agree single primary objective; confirm attendees including economic buyer |
| 2. Collect & validate data | T−21 days | Reconcile KPIs with customer source systems; resolve discrepancies before the meeting |
| 3. Frame storyline & draft materials | T−14 days | Three chapters: Progress / Business Impact / Forward Path |
| 4. Internal dry-run & role assignment | T−10 days | Assign speaking roles; time-box deck to 30 minutes + 15 for discussion |
| 5. Pre-send executive summary | T−5 days | Two-page brief: headline KPIs, impact highlights, proposed forward plan |
| 6. Conduct the QBR | Day 0 | Lead with outcomes not features; invite champion to co-present; close with 3 commitments + named owners + dates |
| 7. Document decisions & next steps | T+1 day | Circulate deck, notes, action table within 24 hours |
| 8. Execute follow-up campaigns | T+7 days | Launch any new initiatives promised |
| 9. Measure post-QBR momentum | T+30 days | Check adoption telemetry, support volume, sentiment |
| 10. Refine QBR process | After cycle | Internal retro: what data resonated? Which slide dragged? |

**Best practices:** Cap total meeting time at 60 minutes. Lead with outcomes not feature updates. Use customer's branding on the deck.

---

## Chapter 8 — Relationship & Account Management

### Account Coverage Models

| Model | ARR Range | CSM:Account Ratio | Description |
|-------|-----------|-------------------|-------------|
| **Dedicated Pod** | >$1 M | 1:1 | Fixed team (AE + Senior CSM + SA + Support Liaison) for high-complexity accounts |
| **Named Portfolio** | $250K–$1M | 1:5–1:15 | CSM owns 5–15 mid-market accounts within a vertical |
| **Pooled/Tech-Touch** | <$250K | 1:100+ | Automation-driven (trigger emails, in-product guidance, community forums) with selective intervention |
| **Hybrid Tiering** | All | Mixed | Pod for Tier 1, Named for Tier 2, Pooled for Tier 3 |

**Dynamic tier movement triggers:**
- **Up-tier:** Health score ≥80, expansion probability ≥30%, or executive sponsor joins customer's C-suite
- **Down-tier:** Sustained ARR decline >10%, no expansion in two years, or migration notice given

### Executive Sponsorship Programme
- Assign one named executive sponsor per strategic account
- Sponsor role: C-suite relationship glue, roadmap alignment, escalation authority, spend above departmental budgets
- Minimum engagement: joint executive session each quarter; twice-yearly strategic roadmap review
- Measure sponsor health: response time to customer C-suite requests, QBR attendance, expansion deal involvement

### Strategic Account Planning
Relationship map components:
- Economic Buyer, Executive Sponsor, Technical Champion, Power Users, Data Owner/IT
- Flag preferred communication channel and KPI interest for each (e.g., CFO cares about cost savings; Marketing Director cares about lead velocity)
- Multithreading score: number of active champions across functional levels (minimum 3 functions for strategic accounts)

---

## Chapter 9 — Service & Support Excellence

### Support Operating Model
- Define SLA tiers by customer tier (Tier 1: 1-hour response, 4-hour resolution target; Tier 2: 4-hour response; Tier 3: same-business-day)
- Route "how-to" tickets to specialised enablement queue (not general support) — provide support agents account-specific adoption metrics so they recommend next-best actions, not just troubleshooting
- Incident Response Playbook: P1 (system-down) → named crisis manager, 15-minute status updates, post-mortem within 48 hours
- Support quality audit: monthly review of CSAT by agent, ticket resolution time, repeat contact rate

---

## Chapter 10 — Pricing & Contract Levers for Retention

### Retention-Friendly Pricing Models
- **Annual upfront billing** improves cash flow but doesn't change LTV; monthly billing penalises CAC payback
- **Multi-year contracts with ramp clauses** lock in revenue trajectory while reducing friction (customer gets year-1 discount; vendor gets year-3 commitment)
- **Consumption-based models** align vendor incentives with customer growth but require health-score monitoring of usage trajectory
- **Loyalty pricing** — volume discount unlocked at renewal milestone, not new contract (rewards retention vs. rewarding switching)

### Renewal Clause Template
Key renewal provisions: automatic renewal with 90-day notice window; price escalation cap (CPI or 5%, whichever is lower); contractual SLA credits for breach; expansion right of first refusal for existing modules.

**Pricing adjustment guide:**
1. Identify the trigger (market pricing change, cost increase, expansion opportunity)
2. Quantify ROI the customer has realised since last renewal
3. Frame as investment, not cost ("At current pricing, your ROI is 4.7×; proposed pricing delivers 3.9× — still industry-leading")
4. Offer phased increases (ramp from current to new pricing over 12 months)
5. Tie increase to new capabilities (avoid pure price-up without feature enhancement)

---

## Chapter 11 — Communication & Engagement Strategy

### Multichannel Communication Framework
| Channel | Cadence | Content Type | Owner |
|---------|---------|-------------|-------|
| In-product notifications | Event-triggered | Feature updates, usage alerts, milestone celebrations | Product team |
| Email nurture | Weekly/biweekly | Success stories, best-practice tips, webinar invitations | Marketing/CS |
| Executive briefings | Quarterly | Business impact report, roadmap preview | CSM + AE |
| Community forum | Continuous | Peer Q&A, product updates, champion spotlights | Community Manager |
| Webinars/training | Monthly | New feature deep-dives, power-user sessions | Enablement |

**Content Calendar Template:** Map content types to customer lifecycle stages (onboarding, adoption, expansion, renewal). Maintain 8-week content pipeline minimum.

**Engagement campaign best practices:**
- Personalise at segment level minimum (not one-size-fits-all blast)
- Always include a clear call-to-action tied to a specific value outcome
- A/B test subject lines and CTAs; report performance at monthly steering meetings
- Celebrate customer milestones publicly (usage anniversaries, expansion milestones, case study publications)

---

## Chapter 12 — Renewal Management

### Renewal Pipeline Process
**Timeline benchmarks:**
- T−180 days: Health score review; identify at-risk accounts for early intervention
- T−90 days: Formal renewal conversation; confirm economic buyer; present value summary
- T−60 days: Proposal and negotiation phase
- T−30 days: Commercial close; legal review
- T−7 days: Order form signed; provisioning confirmed
- T+1 day: Renewal confirmed; new success plan cycle begins

### Forecasting Template
Assign churn probability by health score band:
- Green (80–100): 5% churn probability
- Amber (60–79): 25% churn probability
- Red (40–59): 55% churn probability
- Critical (<40): 80% churn probability

Weighted renewal forecast = Σ (ARR × (1 − churn probability)) by band

### Negotiation Preparation Checklist
- Total ROI delivered since last renewal (quantified, in customer's metrics)
- Competitive landscape update (is the customer evaluating alternatives?)
- Stakeholder changes (new economic buyer = restart relationship; old buyer promoted = stronger advocate)
- Product roadmap items that expand value in contract period
- Pre-approved concession menu (which concessions are authorised without escalation)
- Walk-away criteria (at what price/term does the deal become unprofitable?)

---

## Chapter 13 — Cross-Sell & Upsell Growth

### Opportunity Identification Framework
**Upsell triggers (structural signals):**
- License utilisation >85% for 3+ consecutive months
- Feature usage hitting plan limits
- KPI targets surpassed ahead of schedule
- New business unit or geography expansion by customer

**Cross-sell triggers:**
- Customer's strategic initiative requires capability outside current product
- Executive sponsor moves to adjacent department (warm introduction path)
- Tool consolidation opportunity (existing point solution creating integration overhead)

### Upsell Guide (11 Steps)
1. Log trigger event with supporting data in CRM
2. Validate readiness with champion (gauge appetite; if tepid, prioritise adoption optimisation first)
3. Quantify incremental value in customer metrics (not vendor metrics)
4. Map stakeholders and decision path (procurement may require new approval even for upsell)
5. Design offer structure (Capacity Pack / Feature Unlock / Premium Support Add-On)
6. Create mini-business case (two slides or one-page PDF: current baseline, pain, upsell benefit, investment, payback)
7. Handle objections proactively (phased billing, short pilot, discount tied to expansion milestones)
8. Generate quote and order form (electronic signature; copy finance and champion)
9. Provision within 24 hours of signature; send "What's New" email with tutorials
10. Monitor early usage daily for 30 days; share progress emails at Day 14 and Day 30
11. Document outcomes; capture advocacy asset (testimonial, case study, reference call)

### Cross-Sell Playbook Checklist
- Strategic fit written in one sentence linking to executive objectives
- New stakeholder map created; champion secured for introductions
- Tool overlap and consolidation opportunities documented
- Customer-specific business case quantifies incremental ROI and synergy
- Pilot scope defined: two weeks, one department, clear success metrics
- Bundle and pricing strategy: tie discounts to consolidation (not volume alone)
- "Same Stack, New Module" compliance dossier ready for procurement reviews
- Post-sale resource plan confirmed before contracts are signed

**Bundle tactics:**
- Step-up bundles: discount on Product B only when combined with incremental spend on Product A
- Platform editions: multiple modules under single SKU for enterprise tiers
- Promo credits: limited-time credits on implementation fees (avoids permanent discount leakage)

---

## Chapter 14 — Customer Advocacy & Community

### Advocacy Programme Framework
**Three advocate tiers:**
- **Advocate** — Public review, short quote, community answers
- **Champion** — Webinars, beta programmes, advisory councils, reference calls
- **Luminary** — Keynote speaker, co-authored whitepapers, strategic design-partner engagements

**Candidate identification:** NPS promoters, high health-score accounts, rapid adoption curves, closed-won upsells. Weight scoring and automate CRM alerts when thresholds are met.

**Non-monetary reward model (B2B best practice):**
- Exclusive roadmap briefings and beta invitations
- VIP passes or speaking slots at user conferences
- Co-branded success stories promoted by vendor's marketing team (boosts the champion's internal profile)
- Subtle, high-quality swag tied to tier milestones

**Engagement cadence:**
- Monthly: Advocate newsletter spotlighting member wins and upcoming opportunities
- Quarterly: Virtual roundtables or product feedback labs; update leaderboards
- Bi-annual: Customer advisory board meetings; release new tier benefits
- Event-driven: Call for session speakers or case-study refresh ahead of conferences

**Measurement:** Reference call volume, case study pipeline, NPS lift in advocate cohort vs. non-advocate cohort, speaker and media contribution value.

---

## Application to Business Plans — Uganda/East Africa Context

### Adapting Retention Metrics to Uganda SMEs
- Most Uganda SMEs operate subscription, retainer, or repeat-purchase models where retention economics apply directly
- **GRR equivalent for product businesses:** "repeat purchase rate" — % of customers who bought again within 12 months
- **Churn risk signals for informal sectors:** mobile money payment delays (3+ weeks), reduced order frequency, competitor introductions via mutual contacts
- **Customer segmentation by segment:** Tier 1 (key accounts, institutions, large corporates); Tier 2 (established SME customers); Tier 3 (individual/casual customers) — align service delivery cost to tier
- **ICP in Uganda context:** Look for customers who: pay on time, refer others, give feedback willingly, and have budget aligned to your pricing — these predict long-term retention better than firmographics alone

### NPS in East Africa
- Adjust NPS anchors for cultural context: East African respondents tend toward higher numerical scores in face-to-face settings; deploy written/anonymous surveys for more accurate readings
- Focus NPS verbatims on specific pain points rather than overall satisfaction scores
- Use VOC to track word-of-mouth referral health (often more impactful than NPS score in relational markets)

### CLV/CAC for Business Plan Bankability
Per the CLV:CAC benchmarks in the `05-target-market` skill:
- LTV/CAC ≥3:1 is minimum bankable threshold
- Use GRR and NRR definitions from this playbook when presenting retention assumptions to lenders
- Present a retention economics model (cohort GRR + expansion + CAC payback) as part of financial projections — banks respond positively to demonstrated understanding of unit economics

---

## Quick-Reference Checklists

### Retention Health Audit (7 Questions)
- Do we report GRR, NRR, and logo churn monthly and by cohort?
- Are expansion and contraction broken out separately in board packs?
- Is ARPA segmented by new vs. existing customers?
- Do LTV and CAC calculations use gross margin (not revenue)?
- Is CAC payback below our cost-of-capital horizon?
- Does a Retention Steering Committee meet monthly with clear agendas, metrics, and owners?
- Do frontline managers have live access to retention KPIs?

### Churn Prevention Quick Wins (Deploy within 30 Days)
1. Build a customer health dashboard (traffic-light) from available CRM + usage data
2. Identify all accounts renewing in next 90 days; score health for each
3. Assign every at-risk account an explicit owner and 30-day rescue plan
4. Set up monthly QBR cadence for top 20% of ARR accounts
5. Define "first value" milestone for every new customer and track time-to-first-value
