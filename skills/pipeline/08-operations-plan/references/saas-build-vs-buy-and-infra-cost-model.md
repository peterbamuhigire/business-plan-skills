---
source: Golding (Multi-Tenant SaaS Architectures); Bessemer playbooks; OpenView build-vs-buy
frameworks: [Build-vs-Buy decision matrix; Per-tenant infra cost; SaaS control-plane component menu]
skill: 08-operations-plan
cross-reference: [10-financial-projections, 14-ai-integration, saas-unit-economics-and-cohort-model]
---

# SaaS Build-vs-Buy & Infra Cost Model

## 1. The Default Build-vs-Buy Matrix

| Component | Default | Build only if... |
|---|---|---|
| **Identity / Auth** | BUY (Auth0, Cognito, Okta, Keycloak, Supabase Auth) | Specific enterprise requirements (HSM, SAML federation custom) |
| **Billing / Subscription** | BUY (Stripe Billing, Chargebee, Recurly, Maxio/SaaSOptics, Paystack Subscriptions) | Vertical-specific billing logic (e.g., usage in non-standard units) |
| **Payments** | BUY (Stripe, Paystack, Flutterwave, DPO, M-Pesa via direct integration) | Almost never build payments |
| **Email / SMS** | BUY (Postmark, SendGrid, Twilio, Africa's Talking, Mailgun) | Volume-driven self-host (>10M/month) |
| **CRM** | BUY (HubSpot, Salesforce, Pipedrive, Close, Freshsales) | Always buy at <1000 customers |
| **Observability / monitoring** | BUY (Datadog, New Relic; or self-host Grafana+Prometheus+Loki for cost) | Self-host if Datadog >$5k/month |
| **Logs / log management** | BUY at small scale (Datadog, LogDNA/Mezmo, Sumo Logic); SELF-HOST at scale (ELK, Loki) | Always self-host above $3k/month |
| **CDN** | BUY (Cloudflare, Fastly, CloudFront) | Almost never build |
| **Vector DB (for AI)** | BUY at small (Pinecone, Weaviate cloud); SELF-HOST at scale (Qdrant, Milvus self-host) | Self-host at $500+/month |
| **Customer support helpdesk** | BUY (Intercom, Zendesk, Freshdesk, HelpScout, Crisp) | Always buy |
| **Customer Success platform** | BUY (Gainsight, Totango, ChurnZero, Vitally, Catalyst) | Build only at $20M+ ARR if existing tools don't fit |
| **Analytics / BI** | BUY (Mixpanel, Amplitude, Heap, Metabase, Power BI) | Build dashboards in Metabase / Looker |
| **Documentation / Help Centre** | BUY (Document360, Helpjuice, Notion, Markdown + Astro/Docusaurus self-host) | Self-host if low-volume + technical team |
| **Marketing automation** | BUY (HubSpot, Customer.io, Iterable, Mautic self-host) | Self-host at small scale; pay at scale |
| **Status page** | BUY (Statuspage, Better Uptime, Uptime Kuma self-host) | Always buy or self-host minimal |
| **SOC2 / security compliance** | BUY (Vanta, Drata, Secureframe, Sprinto) | Always buy until $20M+ ARR |
| **Data warehouse** | BUY (Snowflake, BigQuery, Redshift, Databricks) | Always buy |
| **CI/CD** | BUY (GitHub Actions, GitLab CI, CircleCI) | Always buy |
| **Cloud infrastructure** | BUY (AWS, GCP, Azure, Africa Data Centres, Liquid Cloud, Raxio for sovereign) | Never build hyperscaler |
| **Foundation LLM** | BUY (OpenAI, Anthropic, Google, AWS Bedrock, Cohere) | Almost never pre-$100M ARR |
| **Fine-tuning pipeline** | BUY/HYBRID (OpenAI FT API, Together AI, HuggingFace AutoTrain) | Build only for proprietary-data moat |

## 2. Per-Tenant Infra Cost Modelling

Build a cost-per-tenant model with these components:

```
Per-tenant monthly cost = 
  Compute (CPU/memory/serverless) per tenant
+ Storage (DB + objects + backups) per tenant
+ Network (egress + CDN) per tenant
+ Identity / Auth per tenant
+ Billing platform per tenant
+ Observability per tenant
+ Email / SMS per tenant
+ Third-party data / API fees per tenant
+ AI / LLM cost per tenant (if applicable)
+ Allocated overhead (G&A, security, compliance)
```

At small scale (<100 tenants), per-tenant cost is dominated by fixed-floor pricing of SaaS tools (Auth0 base, Stripe base). At scale, it converges to consumption-based variable cost.

## 3. Worked Example — African Vertical SaaS at 100 Tenants

```
Component                           Cost per tenant per month
---------                           -------------------------
AWS compute (shared multi-tenant)   $2.00
AWS storage (DB + S3 + backups)     $1.50
CloudFront CDN (light usage)        $0.30
Auth0 (~$240/month at 100 tenants)  $2.40
Stripe Billing                       0.5% of revenue (variable)
Paystack subscription mgmt           0.5%
SendGrid / Postmark email            $0.50
Africa's Talking SMS (50/month/tenant) $1.50
Datadog                              $2.00
Help Scout (support)                 $0.80
HubSpot CRM (Pro)                   $4.00 (amortised)
LLM costs (200 queries/month)        $5.00
Allocated G&A / overhead            $5.00
                                    ---------
TOTAL Per-tenant monthly cost       $25.00
```

If average ARPU = $200/month, gross margin = ($200 − $25) / $200 = 87.5% — healthy SaaS.

If ARPU = $50/month, gross margin = ($50 − $25) / $50 = 50% — unhealthy; either raise price, reduce cost, or change tier mix.

## 4. The Control-Plane vs Application-Plane Investment

Per Golding: the control plane (onboarding, identity, billing, metering, tenant management, deployment, observability) is what makes you SaaS. Most early SaaS teams under-invest here.

Recommended R&D split:
- **Year 1**: 40% control plane, 60% application plane (build it right early)
- **Year 2**: 30/70
- **Year 3+**: 20/80 (control plane is mature; application plane is the moat)

## 5. Living-Plan Cadence

| Element | Cadence | Owner |
|---|---|---|
| Per-tenant cost dashboard | Monthly | CTO + CFO |
| Tool-stack review (what's costing what) | Quarterly | CTO + Head of Ops |
| Build-vs-buy reassessment | At each ARR milestone | CTO + CFO |
| Cloud-cost optimisation review | Quarterly | DevOps / CTO |
| Vendor consolidation review | Annually | CTO + CFO |

## 6. Africa / Uganda Application Notes

- **FX-exposure**: most "buy" tools are USD-priced. Major risk when revenue is local-currency. Mitigation: pass through; price USD tier; budget FX buffer.
- **Africa-priced alternatives** to consider where quality is equivalent:
  - Paystack Subscriptions vs Stripe Billing
  - Mailgun (lower base) vs SendGrid
  - Africa's Talking SMS (lower per-msg) vs Twilio
  - Self-hosted Listmonk / Mautic vs Customer.io for small-scale
  - Self-hosted Plausible / Umami vs Google Analytics for privacy
  - Self-hosted Supabase vs Firebase (data-residency)
- **Data-residency requirements** often force in-country hosting — Africa Data Centres, Raxio, Liquid Intelligent Technologies, Teraco. Higher infra cost; compliance asset.
- **Cloud-cost optimisation**: African SaaS can save 30-50% with rightsizing, reserved instances, Spot instances for non-critical workloads.
- **Local-content / sovereign-cloud** for public-sector deals is increasingly required — plan a hybrid architecture early.
- **SMS / OTP costs** are higher and more variable in Africa — budget 2-3× US benchmarks per tenant.
- **AI costs** are FX-exposed and unhedgeable; budget aggressive scenarios.
