---
source: Mersch CFO discipline; Bessemer DD playbook; Tomasz Tunguz; M&A practitioner literature
frameworks: [SaaS Data Room structure; DD readiness checklist; Africa-DFI additions]
skill: meta-due-diligence (enhancement)
cross-reference: [saas-bankability-and-investor-readiness, saas-valuation-and-fundraising-strategy]
---

# SaaS Due Diligence Data Room — Reference

The engine's `meta-due-diligence` builds the general data room. SaaS DD requires additional SaaS-specific exhibits. This reference adds them.

## 1. Folder Structure

```
Data Room/
├── 00 — Cap Table & Corporate
│   ├── Cap table (fully diluted; ESOP modelled)
│   ├── Articles of association / incorporation docs
│   ├── Board resolutions
│   ├── Shareholder agreements
│   ├── Prior round docs (SAFEs, convertibles, priced)
│   └── 409A / valuation reports
│
├── 01 — Financial Statements
│   ├── Audited financials (last 2-3 years if available)
│   ├── Monthly P&L (last 24 months)
│   ├── Monthly cash flow
│   ├── Monthly balance sheet
│   ├── Bank statements (last 12 months)
│   ├── Tax filings (last 3 years)
│   └── Auditor letter / accountant letter
│
├── 02 — SaaS Metrics & Cohorts ★ (SaaS-specific)
│   ├── ARR waterfall (monthly, last 24 months)
│   ├── Customer count (monthly, last 24 months)
│   ├── ARPU by tier / segment
│   ├── Logo cohort retention matrix (CSV / spreadsheet)
│   ├── Revenue cohort retention matrix
│   ├── Involuntary-churn cohort
│   ├── LTV, CAC, payback (monthly)
│   ├── NRR, GRR (monthly)
│   ├── Magic Number, Rule of 40, Burn Multiple (monthly)
│   ├── Pipeline export from CRM (current + last 6 months)
│   └── Sales-funnel conversion data
│
├── 03 — Customers
│   ├── Top 20 customer contracts (signed)
│   ├── Customer concentration analysis (% ARR per customer)
│   ├── Customer health-score export
│   ├── NPS history
│   ├── Customer case studies
│   ├── Customer reference list (with consent)
│   └── Churn analysis (last 12 months)
│
├── 04 — Product & Engineering ★ (SaaS-specific)
│   ├── Product architecture overview
│   ├── Multi-tenancy strategy (pool / silo / hybrid)
│   ├── Cloud / infra provider + cost
│   ├── Tech-stack inventory
│   ├── Security policies (SOC2 / ISO27001 status)
│   ├── Pen-test reports
│   ├── Vulnerability disclosures (history)
│   ├── Code-quality / test-coverage metrics
│   ├── Open-source compliance / dependency licences
│   ├── IP / patent register
│   ├── AI / model strategy (if applicable)
│   └── DevOps / SRE on-call rotation
│
├── 05 — Sales & Marketing
│   ├── GTM motion document
│   ├── Sales-team comp plans
│   ├── Marketing channel mix + per-channel CAC
│   ├── Brand assets
│   ├── Customer acquisition funnel diagram
│   ├── Channel-partner agreements
│   └── Sales playbook
│
├── 06 — Operations & Customer Success
│   ├── Org chart
│   ├── Customer-success operating model
│   ├── Support SLA / metrics
│   ├── Tenant onboarding flow
│   └── Process documentation
│
├── 07 — Team
│   ├── Key bios (founders + execs + senior tech)
│   ├── Employment agreements (template)
│   ├── ESOP plan documents
│   ├── Recent hires
│   ├── eNPS / engagement signals
│   ├── Compensation benchmarking
│   └── Org chart (with succession plan flags)
│
├── 08 — Legal & Compliance
│   ├── Material agreements (top 10)
│   ├── Cap table compliance docs
│   ├── Regulatory licences (per jurisdiction)
│   ├── Data protection compliance (GDPR / POPIA / NDPR / KE DPA / UG DPPA)
│   ├── Tax compliance certificates
│   ├── Pending / threatened litigation disclosure
│   ├── Trademarks / domains
│   └── Insurance (E&O, cyber, D&O)
│
├── 09 — Risk Register & Stress Tests
│   ├── Top 20 risk register
│   ├── Stress-test scenarios
│   ├── Disaster-recovery plan
│   ├── Business-continuity plan
│   └── Incident-response log
│
├── 10 — Plan & Projections
│   ├── Current business plan
│   ├── 3-5 year financial projections
│   ├── Sensitivity + scenario analyses
│   ├── Use of funds
│   ├── Milestone roadmap
│   └── Exit thesis
│
└── 11 — Board / Investor Materials
    ├── Last 12 monthly investor updates
    ├── Last 4 quarterly board packs
    ├── MSPOT (current year)
    ├── Decision log (or summary)
    └── OKR / KPI dashboard
```

## 2. The SaaS-Specific Exhibits (the discriminators)

These exhibits separate SaaS-grade DD from generic startup DD:

### A. ARR waterfall (monthly, 24 months)
The single most-scrutinised exhibit. Shows growth quality.

### B. Cohort retention matrix
Logo + revenue cohort. The honest test of product-market fit.

### C. Per-customer cost / margin breakdown
Demonstrates per-tenant cost telemetry; surfaces tier-mix problems.

### D. Pipeline export (CRM CSV)
Investors will validate stage-to-close rates against your projection assumptions.

### E. Compliance status
SOC2 Type 1 / 2; ISO27001; data-residency by region; sector-specific (HIPAA-equivalent for healthtech; PCI-equivalent for fintech).

### F. AI cost / strategy (2024+)
If material AI usage, per-tenant cost, provider concentration, model strategy.

## 3. Pre-DD Checklist (1-2 weeks of prep before any DD)

- [ ] Update cap table with latest cap-table tool (Carta / Pulley / Capdesk)
- [ ] Reconcile financials to bank statements; have accountant verify
- [ ] Export latest cohort data from billing system
- [ ] Refresh customer concentration analysis
- [ ] Document any unresolved security incidents / compliance gaps
- [ ] Prepare top-3 risk register with mitigations
- [ ] Verify all employment agreements are signed
- [ ] Verify all IP assignments are signed
- [ ] Update product architecture overview
- [ ] Verify regulatory licences are current
- [ ] Update plan with most recent quarter's actuals

## 4. DD Process Discipline

- **NDA first**: never share data room without NDA executed
- **Q&A log**: maintain a Q&A log; every question + answer; deal-team accessible
- **Granular access**: investor team gets read access; not download (unless deal-active)
- **Versioning**: timestamp every doc; version when material changes happen
- **Refresh during DD**: actuals updated monthly during DD process
- **Closing checklist**: track all conditions precedent to close

## 5. Living-Plan Cadence

DD-ready data room should be maintained continuously:
- **Monthly**: financials + ARR waterfall + cohort
- **Quarterly**: full data-room audit; remove stale docs; refresh exhibits
- **At each round**: tailored DD pack for target investor
- **Annually**: audit / accountant refresh

## 6. Africa / Uganda Application Notes

- **DFI DD** is more granular than VC DD — expect 100-200 specific questions, multi-month process. Use IFC / FMO / BII DD checklist templates as references.
- **ESG / impact** exhibits required for DFI: ESMS, IFC Performance Standards alignment, jobs created, beneficiary metrics. Use `meta-sustainability` framework.
- **Tax compliance** more important in African DD because of common reputational risk (multiple-country tax compliance). Maintain current tax-clearance certificates for each jurisdiction.
- **Regulatory licences** vary by jurisdiction and sector — fintech licences (PSP, mobile-money, lending) are the most-scrutinised.
- **Currency**: present all financials in both local currency and USD; explain FX impact separately from operations.
- **Cap-table jurisdiction**: Mauritius / Cayman / Delaware structuring is common; have current legal opinion.
- **Litigation / customs disputes**: be transparent; African business commonly has some unresolved customs / tax dispute; disclose and explain.
- **Audit standard**: prefer IFRS-audited by Big-4 / mid-tier for $1M+ raises. Local audit firms acceptable for smaller raises but harder for international investors to accept.
