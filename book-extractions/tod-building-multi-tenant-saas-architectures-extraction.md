# Book Extraction: Tod Golding — Building Multi-Tenant SaaS Architectures

**Source:** Golding, Tod. *Building Multi-Tenant SaaS Architectures* (O'Reilly, 2024). Author is AWS Global Tech Lead for SaaS, who has worked with hundreds of SaaS providers building or migrating multi-tenant systems.

**Why this matters:** Every SaaS business plan that mentions "platform," "multi-tenant," "cloud-native," or "AI" — i.e. nearly every modern ICT/SaaS plan — must be honest about what those words mean financially, operationally, and strategically. Most plans use them as marketing language without understanding the economics. Golding's book is the canonical translation between architecture and business outcomes: agility, operational efficiency, frictionless onboarding, innovation, growth, cost transparency, and **tenancy strategy as the determinant of unit economics**. The book is also the primary source for build-vs-buy, capex-vs-opex, and infra-cost modelling decisions in SaaS plans.

---

## 1. Core Thesis: SaaS is a Business Model, NOT a Deployment Pattern

Golding's opening discipline: when a business says "we built SaaS," it should mean a business model with six characteristics, not just "we hosted software on AWS."

The six business pillars of SaaS (Golding):
1. **Agility** — release new features fast; pivot pricing, packaging, segments quickly
2. **Operational Efficiency** — one team manages all tenants through "a single pane of glass"
3. **Innovation** — agility + operational efficiency frees engineering to invest in differentiation
4. **Frictionless Onboarding** — new tenants self-serve or automated-onboard; no human ops per tenant
5. **Growth** — the infrastructure can absorb 1,000 new tenants tomorrow without specialised teams
6. **Cost Transparency** — per-tenant cost is measurable, allowing pricing/profitability decisions

**Plan implication:** any business plan claiming SaaS must address all six. A plan that has only "shared infrastructure" but lacks frictionless onboarding, single-pane-of-glass ops, and per-tenant cost telemetry is **not yet SaaS** — it is an MSP (Managed Service Provider) or hosted software, with very different economics.

## 2. The Classic Installed-Software Model vs SaaS

Classic: one customer = one install = one version = one support pod. Each customer adds linear operational overhead. Margin erosion is structural; growth eventually slows by design.

SaaS: all tenants on the same version, same shared infrastructure, same ops team. Each new tenant adds near-zero incremental ops cost (the SaaS "operational leverage").

**Plan implication:** the financial section's gross-margin and OpEx scaling assumptions depend entirely on whether the architecture is classic-installed, MSP, or true SaaS. Classic 30% gross margin; MSP 50–60%; SaaS 75–85%.

## 3. The MSP Trap

The Managed Service Provider model is where many would-be SaaS companies actually live: multiple customers, dedicated environments per customer, centralised ops team. It looks like SaaS in pitch decks but:
- Customers run different versions → fragmented support
- Each new customer needs onboarding work
- Innovation slows because new features need testing across version drift
- Operational efficiency caps out around 5–10 customers per ops engineer

**Plan implication:** the engine should detect MSP-language ("on-premise option," "dedicated environment per customer," "customer chooses upgrade timing") and either reclassify the plan as MSP/services (different economics) or require the plan to commit to a true-SaaS migration roadmap.

## 4. Multi-Tenancy Re-Defined

Golding rejects the narrow definition of multi-tenancy ("multiple tenants sharing physical infrastructure"). His broader definition: **any environment that onboards, deploys, manages, and operates tenants through a single pane of glass.**

This matters because real-world SaaS often blends:
- **Pooled** resources (most tenants share)
- **Silo** resources (some tenants get dedicated infra for compliance, security, performance)
- **Hybrid** mixes within the same product (Product microservice pooled, Order microservice silo storage, Fulfillment microservice silo compute)

The strategic decision is which resources to pool, which to silo, by which tenant tier — and how that maps to pricing.

## 5. Tenancy Models and Their Pricing/Margin Implications

| Model | Description | Cost per tenant | Pricing strategy |
|---|---|---|---|
| **Pool** (full multi-tenant) | All tenants share compute + storage | Low | Lowest tier, volume-priced |
| **Silo** (per-tenant) | Each tenant has dedicated infra | High | Premium tier, enterprise pricing |
| **Bridge / Hybrid** | Some resources pooled, others silo | Medium | Mid-tier, by feature |

**Plan implication:** pricing tiers in Section 07 (Marketing/Sales) must map to tenancy models. "Enterprise" tier with dedicated environment commands 3–5× pricing of "standard" pooled tier.

## 6. The Control Plane vs Application Plane

Golding's most useful architectural concept for business planning:
- **Control plane** = the SaaS-specific services (onboarding, identity, billing, metering, tenant management, deployment, observability). This is what makes the company a SaaS.
- **Application plane** = the product features themselves.

Most early SaaS companies over-invest in application plane and under-invest in control plane. Result: they have features but can't onboard, bill, support, or operate at scale.

**Plan implication:** R&D budget in Section 10 must include control-plane investment (typically 25–40% of engineering capacity in years 1–2). Plans that allocate 100% of engineering to "features" are setting up to plateau.

## 7. Frictionless Onboarding as a Business Lever

Golding emphasises: onboarding latency = lost revenue. SaaS unicorns can onboard a tenant in seconds; struggling SaaS take days or weeks of services work per tenant.

The components of automated onboarding:
- Self-service sign-up
- Tenant provisioning (DB, identity, billing setup)
- Tenant-specific configuration
- First-value-in-product (the "aha moment")

**Plan implication:** Section 08 (Operations) must specify the onboarding flow, time-to-first-value, and self-service vs assisted-onboarding mix. Section 10 must include cost-per-onboarding (services labour) as a unit economic.

## 8. Tier-Based Architecture and Noisy Neighbour

Critical operational concept: in pooled environments, one heavy-usage tenant can degrade experience for all others ("noisy neighbour"). Mitigations:
- Tenant-level resource quotas / throttling
- Tier-based isolation (premium tenants get dedicated compute)
- Auto-scaling rules
- Per-tenant observability

**Plan implication:** SLA tiers must be modelled in the financial plan. Enterprise tier requires investment in noisy-neighbour mitigation and dedicated SRE; this changes the cost structure of that tier.

## 9. Build-vs-Buy and Infrastructure Cost Modelling

The book is the gold-standard reference for the build-vs-buy decisions in SaaS. Categories:
- **Always-buy**: identity (Auth0, Cognito, Okta), billing (Stripe Billing, Chargebee, Recurly, Maxio/SaaSOptics), observability (Datadog, New Relic), CDN (Cloudflare, Fastly).
- **Conditionally-build**: tenant provisioning, tenant-specific feature flags, in-app analytics, AI features.
- **Always-build**: the product itself.

**Plan implication:** Section 10 (Financial Projections) needs an explicit "infrastructure & build-vs-buy" line that captures the per-tenant cost of each piece. Section 03 (Products) must justify any "we'll build it ourselves" decision against the buy cost.

## 10. Per-Tenant Cost Telemetry (Cost Attribution)

Golding's discipline: you cannot price intelligently if you don't know what each tenant costs to serve. SaaS companies measure:
- Compute consumed per tenant
- Storage per tenant
- API calls / data egress per tenant
- Third-party costs (AI tokens, payment gateway fees, SMS) per tenant
- Support tickets per tenant
- Custom-development hours per tenant

**Plan implication:** Section 10 cohort analysis should show gross margin per customer segment, not just aggregate. Some customers may have 90% gross margin and some 30%. Plans that don't decompose are leaving money on the table.

## 11. The "AI as a Tenant Cost" Discipline

Critical 2024+ addition: AI features (LLM tokens, embeddings, fine-tuning) are usage-based costs that flow directly to a tenant. Without proper cost attribution, a tenant who heavily uses AI features can destroy the unit economics of their entire tier.

**Plan implication:** any plan with AI features (Section 14) must model AI cost per tenant per month and design pricing to either pass through, cap, or include AI usage explicitly.

## 12. The Tenant Lifecycle in the SaaS Operating Model

Tenants pass through: **Sign-up → Onboard → Activate → Convert → Expand → Renew → (Churn or Re-engage)**. Each stage has architecture, ops, and CS implications. Each stage is also where data, automation, and instrumentation live.

**Plan implication:** Section 07 + Section 08 must show the tenant-lifecycle pipeline, the conversion rate at each stage, and the operational team / automation that owns each stage.

## 13. Hardening Rules for the Business-Plan Engine

- Reject "we built a multi-tenant platform" claims unless the plan addresses all six SaaS business pillars (agility, ops efficiency, innovation, onboarding, growth, cost transparency).
- Detect MSP-language and either reclassify or require a true-SaaS migration roadmap.
- Force pricing tiers (Section 07) to map explicitly to tenancy models (pool / silo / hybrid).
- Force control-plane R&D investment line item (25–40% of eng capacity years 1–2).
- Force onboarding flow specification, time-to-first-value KPI, cost-per-onboarding economic.
- Force per-tenant cost telemetry to be in the operating model (Section 08).
- Force AI cost-per-tenant modelling whenever AI features are claimed.
- Force build-vs-buy decision matrix for identity, billing, observability, AI, payments.

## 14. Uganda / East Africa / Africa Application Notes

- Most African SaaS plans use "platform" language while operating as MSPs or single-tenant hosted-software. The engine should be especially vigilant here.
- Build-vs-buy decisions are FX-sensitive. Stripe Billing / Chargebee / Datadog are USD-priced and at small scale can blow the budget. Africa-friendly alternatives: Paystack Subscriptions, Flutterwave Recurring, Self-hosted Grafana + Prometheus + Loki for observability, Keycloak / Supabase Auth for identity. Plans should justify USD-tooling above $1k/month.
- Per-tenant cost attribution is harder when payment rails are M-Pesa / MoMo (which charge per-transaction). Plans must model mobile-money transaction fees as a per-tenant cost.
- Frictionless onboarding requires solving identity for African users — phone-number primary, OTP via SMS (Africa's Talking, Twilio), and graceful fallback for users without persistent email. Plan for this.
- Data localisation: Kenya Data Protection Act, Nigeria NDPR, South Africa POPIA, Uganda DPPA require certain customer data to reside in-country. Plans that promise full multi-tenant pooled across regions may fail compliance. The hybrid silo-by-region architecture may be mandatory.
- AI-as-cost discipline is critical because LLM API access is USD-priced; African SaaS revenue is local-currency. Plans must show FX hedging or USD-priced AI tier.
