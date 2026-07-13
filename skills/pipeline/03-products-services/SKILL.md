---
name: 03-products-services
description: Use when producing or reviewing the 03 products services component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Products & Services Skill

## Overview

Generate Section 03 of the business plan: the products and services section. Use this skill to explain what the business offers, why customers care, how delivery works, and what makes the offer commercially defensible.

## Use When

- Use when drafting or revising the products and services section for a plan, proposal, or investor document.
- Use when the business needs a clear value proposition, offer structure, and delivery explanation.
- Use when later pricing, marketing, operations, or financial sections depend on precise offer definitions.

## Do Not Use When

- Do not use for detailed market sizing, channel strategy, or financial modelling beyond what supports the offer definition.
- Do not invent features, IP, or regulatory status that the client has not established.
- Do not describe offerings in jargon that hides the real customer benefit.

## Required Inputs

- Product or service list, customer problem, and intended outcomes
- Delivery model, pricing logic, development stage, and key dependencies
- Country or regulatory context where licences, standards, or IP matter
- Adjacent section drafts that must stay consistent with the offer definition

## Workflow

1. List each offer clearly in customer language before adding detail.
2. Map features to benefits, customer pain points, and commercial value.
3. Explain delivery, production, suppliers, and compliance requirements where relevant.
4. If the offer is premium, high-ticket, luxury/affluent, enterprise, or executive-facing, run `meta-premium-go-to-market` to test product design, proof, service layer, pricing power, and buyer fit.
5. If the offer includes a website, ecommerce, portal, web app, content/SEO engine, online booking path, or website-design service line, run `meta-website-investment-planning` so the website role, stack, service design, and cost implications are explicit.
6. Distinguish current offers from pipeline or aspirational offers.
7. Reconcile the section with pricing, operations, IP, and market claims elsewhere in the plan.
8. Flag any missing validation, capability, or compliance facts that weaken the offer narrative.

## Quality Bar

- A reader can understand what is sold, to whom, and why it matters.
- Benefits are clearer than feature lists, and claims are commercially believable.
- Delivery and compliance logic match the operating reality of the business.
- The section creates a usable basis for pricing, marketing, operations, and projections.

## Anti-Patterns

- Feature-heavy descriptions with no customer or revenue logic.
- Mixing live offers, prototypes, and future ideas as if they are equally mature.
- Unsupported claims of uniqueness, IP protection, or regulatory clearance.
- Copying reference frameworks instead of writing the actual offer narrative.

## Outputs

- A finished or revised Section 03 products and services draft
- Explicit assumptions, dependencies, and unresolved product questions
- Cross-skill notes for pricing, marketing, operations, risk, and finance



Generate a clear, compelling description of what the business offers and why it matters to customers.

## What to Generate

### Required Elements

1. **Product/service descriptions**  What each offering is, in plain language
2. **Value proposition**  The specific problem solved and benefit delivered
3. **Features vs. benefits mapping**  Features are what it does; benefits are why customers care
4. **Pricing overview**  Pricing model and rationale (detailed pricing in marketing section)
5. **Product lifecycle stage**  Development, introduction, growth, maturity, or decline
6. **Intellectual property**  Patents, trademarks, copyrights, trade secrets
7. **R&D pipeline**  Planned products, features, or improvements
8. **Production/delivery method**  How products are made or services delivered
9. **Supplier dependencies**  Key inputs and supplier relationships
10. **Regulatory requirements**  Licences, certifications, compliance needs

### Product Description Framework

For each product or service:

```text
Name:
Category:
Description: [2-3 sentences]
Target customer: [who buys this]
Problem solved: [specific pain point]
Key differentiator: [why this vs. alternatives]
Revenue model: [how it generates income]
Stage: [development / launched / mature]
```

### Technology Build Strategy

For products/services requiring technology systems, evaluate the build strategy (Dennis et al., 2021):

| Strategy | When to choose | Key consideration |
|---|---|---|
| **Custom build** | Unique competitive advantage, in-house skills available | Highest control, longest timeline |
| **Buy (packaged)** | Common business need, speed critical | Faster deployment, vendor dependency |
| **Outsource** | Non-core function, skills gap | Focus on core business, loss of direct control |

For each technology decision, document:
- Which strategy was chosen and why
- Feasibility assessment (technical, economic, organisational)
- Integration requirements with existing systems

### Feasibility Assessment for New Products

Before committing to product development, assess three dimensions (Dennis et al., 2021):

1. **Technical feasibility** — Can we build it? Rate: technology familiarity, project size, system compatibility
2. **Economic feasibility** — Should we build it? Calculate: development costs, operational costs, NPV, ROI, break-even timeline
3. **Organisational feasibility** — Will users adopt it? Assess: strategic alignment, champion existence, stakeholder readiness

## Generation Process

1. Ask for: list of products/services, target customers, industry
2. Map each product to a specific customer problem
3. Articulate differentiators  what makes this offering better or different
4. Identify lifecycle stage and growth trajectory for each
5. Document IP protection status and R&D plans
6. Flag any regulatory or compliance requirements

## Quality Criteria

- Benefits are expressed from the customer's perspective, not the company's
- Differentiators are specific and defensible (not "better quality")
- Pricing rationale connects to value delivered
- R&D pipeline shows forward thinking without over-promising

## References

- **Porter's value chain  differentiation sources**: See `../08-operations-plan/references/value-chain-porter.md` for the full value chain (9 activities), uniqueness/differentiation drivers (policy choices, linkages, timing, location, learning, integration, scale, institutional factors), the cost of differentiation, and competitive scope  from Porter (1985). **Read when explaining what makes this product or service genuinely unique and how that uniqueness is sustained.**
- **Value chain and core competencies**: See `references/value-chain-competencies.md` for value chain design, core competency identification (Prahalad), capabilities analysis, small business strategy (SWOT/niche), stakeholder value mapping, capability gap analysis, and VRIO resource-based strategy from Fahey & Randall, Harris & Lenox, and Evans
- **Pricing strategy**: See `references/pricing-strategy.md` for the Five Ways to Grow framework, cost-plus critique, Value Scales model, Price Triangle, Gold/Silver/Bronze tiered packaging, bundling and cross-selling, discount/volume breakeven tables, pricing psychology (anchoring, decoy, charm pricing), directional pricing, competitive pricing, implementing price changes (A/B/C customer grading), and a condensed pricing action checklist  from Hill (Kogan Page, 2013)
- **Product development lifecycle**: See `references/product-development-lifecycle.md` for the Value-Driven Product Development (VDPD) 7-stage process, idea validation, customer discovery interviews, persona building, proof of concept, prototyping, MVP vs. prototype distinction, launch checklist, Marketing Quadfecta, CAC benchmarks, innovation types (product/process/position/paradigm), dynamic capabilities framework, funding by stage, and Business Model Canvas integration  from Bates (2024) and Tidd & Bessant (Wiley, 2013)
- **Product management frameworks**: See `references/product-management-frameworks.md` for Product Owner stances model, customer value layers, feature-to-outcome mapping, product vision template, roadmap types (goal-oriented, now-next-later, user story map, visual, Gantt), innovation sources (inside-out/outside-in), Truth Curve experiment selection, hypothesis template, 8 scaling strategies, pricing alignment check, and Key Value Areas (KVAs)  from Verwijs, Overeem & Lennartz (Scrum.org, 2023)
- **Technology strategy and feasibility**: Build/buy/outsource decision framework, three-dimensional feasibility analysis (technical/economic/organisational), and NPV/ROI methodology  from Dennis, Wixom & Tegarden (Wiley, 2021)
- **MVP and product validation**: See `references/mvp-validation-frameworks.md` for MVP framework (low-fi vs. high-fi, User Story format), BFCE Use Case evaluation (Better/Faster/Cheaper/Easier), Product Vision strategic questions (network effects, lock-in, margins), Experience Implications Template (People/Process/Technology), and prototyping taxonomy  from Blank & Dorf (2012) and Alam
- **Business model innovation**: See `references/business-model-innovation.md` for the 4V framework (value proposition/creation/delivery/capture), five business model performance drivers (customer engagement, external linkages, internal processes, strategic awareness, reconfiguration capacity), freemium strategy (conversion rate benchmarks 25%, seven strategic requirements, failure patterns), multi-sided platform design (six redesign operations, network effects, cold-start problem), open business model dimensions (five dimensions + strategic responses), analogy-based creative modelling, and business model vs. competitive strategy distinction  from Mangematin et al. (*Journal of Business Strategy*, Emerald, 2017). **Read when evaluating a freemium, platform, or open-model business design, or when using analogies to justify a novel business model.**
- **Business models, strategy, and innovation**: See `references/business-models-innovation-teece.md` for Teece's business model definition (value creation architecture + value capture mechanism), business model vs strategy distinction, business model innovation types, value creation vs value capture problem, appropriability mechanisms (IP/complementary assets/first-mover/network effects/complexity), dynamic capabilities (sense/seize/reconfigure), business model archetypes table (Uganda examples), and application to business plan sections  from Teece (Long Range Planning / Elsevier, 2010). **Read when designing the revenue model, defining competitive advantage, or evaluating a platform, subscription, or razor-blade business model.**
- **Uganda IP protection**: See `10-financial-projections/references/uganda-ip-framework.md` for Uganda's full IP registration framework  trademark registration via URSB (Nice Classification, 45 classes, UGX 175,000 total filing fee, 7-year initial term + 10-year renewals), patent filing (20-year protection), utility model (10-year), industrial design (15-year), copyright (automatic, life+50 years), ARIPO regional protection covering 19 African countries from a single application, trade secret protection via NDAs, IP as a balance sheet asset and loan collateral, fees table, and Uganda IP Policy 2019 institutional framework. **Read for any business with a brand, recipe, software, invention, or creative work to protect.**
- **Sustainable product design and circular economy**: See `references/sustainable-product-design.md` for 4 design-stage decisions governing 7080% of lifecycle environmental impact, simplified lifecycle scan table, circular product business models (product-as-a-service, deposit-refund, by-product exchange, refurbishment), technopreneurship product categories for Uganda/EA (clean cookstoves, solar water pumps, cold chain, organic waste-to-compost), 10-question product sustainability assessment tool (scored 020), and NOGAMU organic certification premium data  Source: Kumar et al. (CRC, 2025) and Leleux & van der Kaaij (2019). **Read when designing sustainable products, evaluating lifecycle impact, or incorporating circular economy into the products and services section.**
- **Premium product and offer design**: Run `../meta-premium-go-to-market/SKILL.md` and read `../meta-premium-go-to-market/references/premium-gtm-quality-gate.md` when the product must sell to affluent, executive, enterprise, luxury, high-ticket, or premium customers. Use it to strengthen positioning, service design, proof, pricing power, launch strategy, and sales execution.
- **Website investment and website-design services**: Run `../meta-website-investment-planning/SKILL.md` and read `../meta-website-investment-planning/references/website-investment-costing-gate.md` when the product/service requires a website, ecommerce, portal, content/SEO engine, landing page funnel, web app, or website-design service pricing. Use it to define website role, design philosophy, stack, service scope, operating requirements, and realistic cost assumptions.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Offering catalogue, customer jobs, delivery method, pricing basis, lifecycle stage, and IP evidence for 03 products services | Product owner, customer research, technical lead, and approved model | Yes | If absent, the offering or customer job is unclear, return a product-definition gap list before writing differentiation. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Products and services section with value proposition and lifecycle map | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 03 products services exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 03 products services release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Feature-to-customer-job trace, pricing rationale, and IP-status record | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 03 products services decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 03 products services review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 03 products services, the controlling focus is offering definition, customer value, delivery method, lifecycle, price basis, IP status, and product-development gates. This skill may describe and compare verified offerings; it may not claim unregistered IP, validated demand, or technical performance without evidence. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 03 products services, loss of evidence about offering definition, customer value, delivery method, lifecycle, price basis, IP status, and product-development gates activates degraded mode. If the controlling 03 products services evidence is unavailable, the same boundary applies. When the offering or customer job is unclear, return a product-definition gap list before writing differentiation. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 03 products services, a feature has no evidenced customer job or willingness-to-pay link| remove it from the core proposition or label it as an experiment with a validation owner | A feature catalogue is mistaken for a commercially coherent offer |
| For 03 products services, A current legal, regulatory, tax, accounting, market, or platform claim controls the 03 products services decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 03 products services, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete products and services section with value proposition and lifecycle map, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 03 products services decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect offering catalogue, customer jobs, delivery method, pricing basis, lifecycle stage, and ip evidence and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce products and services section with value proposition and lifecycle map with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Products and services section with value proposition and lifecycle map must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Feature-to-customer-job trace, pricing rationale, and IP-status record must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 03 products services, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 03 products services, treating an unavailable offering catalogue, customer jobs, delivery method, pricing basis, lifecycle stage, and ip evidence as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing products and services section with value proposition and lifecycle map that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A same-day delivery add-on has no delivery-cost estimate or customer interviews. Keep it outside the launch offer and assign a price-and-fulfilment test.

## References

- Use the verified project evidence register and the owning upstream pipeline section for 03 products services; no local deep-dive reference is declared.
- For 03 products services claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->
