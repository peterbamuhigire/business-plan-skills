# Pillar 4 — Strategic Synthesis and Narrative Discipline
**Score: 7.5 / 10**

The system has the highest-grade communication frameworks available (Minto, Duarte, Klaff). The gap is that these frameworks guide *how to present* an already-completed analysis but do not enforce the *thinking discipline* that McKinsey/Bain apply before writing begins. The Pyramid Principle works best when the analyst starts with a hypothesis and builds the argument deductively — but the current skill flow allows sections to be drafted without first constructing and validating the underlying logical structure.

---

## 4.1 What Is Already World-Class

### Minto Pyramid Principle — Full Implementation
`01-executive-summary/references/pyramid-principle.md` covers:
- SCQA opening (Situation → Complication → Question → Answer)
- Deductive vs. inductive argument structures
- Three logical orders (time/structure/importance)
- MECE grouping rules
- Seven structural errors (inverted pyramid, no answer, missing so-what, etc.)
- Business plan application table mapping SCQA to each section (01–15)

This is genuinely excellent. The SCQA table mapping to plan sections is something most strategy firms do not document explicitly.

### Cross-Section Consistency Architecture
`meta-bankability-scoring/references/consistency-audit.md` — 12-point cross-section checker. This is the closest the system comes to McKinsey's "consistency board" — ensuring financial projections match market sizing assumptions, which match operational plan capacity, which matches team skills described.

### Issue Tree / MECE Foundation
`meta-market-validation/references/mckinsey-problem-solving.md` — Forces at Work, MECE issue trees, hypothesis-driven analysis, 80/20, elevator test. The reference content is excellent.

---

## 4.2 Strategic Synthesis Gaps

### Gap 1 — Issue Tree Not a Pre-Draft Requirement (HIGH IMPACT)

**The McKinsey standard:** Before drafting any section, the analyst builds an issue tree that decomposes the central question into MECE components. The tree determines what analysis must be done and which findings are *so-what* (answer-forward).

**Current state:** The issue tree methodology is documented in `mckinsey-problem-solving.md` but is not a *required checkpoint* before any skill invokes section generation. A user can invoke `04-market-analysis` without building a market structure issue tree first.

**Consequence:** Plans can be well-formatted but analytically thin — covering standard sections rather than answering the specific question the investor or lender has about *this* business.

**Recommendation:** Add to `meta-market-validation/SKILL.md` a mandatory Step 0 — Issue Tree Construction Protocol:
```
Before drafting any analysis section, answer:
1. What is the core question this funder is asking? (SCQA Question)
2. What are the 3-5 MECE sub-questions that, if answered, would answer Q1?
3. What hypothesis does the plan assert in response to each sub-question?
4. What evidence exists to confirm or refute each hypothesis?
```
Only after completing this should any section be drafted.

### Gap 2 — So-What Test Not Enforced (MEDIUM IMPACT)

**The McKinsey standard:** Every paragraph, every slide, every exhibit must pass the "so-what test" — if you remove this paragraph, does the argument change? If not, cut it. Every data point should advance an argument, not just describe a situation.

**Current state:** Language standards are excellent (`language-standards.md`). But the *analytical so-what test* — which is a structural logic test, not a writing quality test — is not enforced as a section-level checkpoint.

**Consequence:** Plans can be verbose, describing the market without asserting what it means for this business's viability.

**Recommendation:** Add a So-What Test to each section's Quality Criteria checklist:
> For every data point included: "So what does this mean for the business case?"
> If the answer is "nothing specific," remove the data point.

### Gap 3 — Strategic Narrative Coherence (MEDIUM IMPACT)

**The McKinsey standard:** A business plan should read as a single coherent argument, not 15 independent sections. The narrative thread is:
- Why this market is attractive (04, 05)
- Why this company is best-positioned to win (02, 06)
- What it will take to execute (07, 08, 09, 13)
- Why the financial returns justify the investment (10, 11)
- Why the risks are manageable (12)

**Current state:** The suite teaches *how to write each section* excellently. But there is no explicit "narrative arc" skill that ensures the sections build a cumulative argument rather than stand independently.

**Consequence:** Plans can be excellent section-by-section but lack the through-line that makes an investor (or a McKinsey partner) say "I see exactly why this investment will succeed."

**Recommendation:** Add a Strategic Narrative section to `00-plan-assembly/SKILL.md`:
- Require the writer to draft a "one-page strategy statement" before writing any section
- Statement format: Problem → Solution → Why Us → How → Proof → Ask
- Every subsequent section should begin with a statement of how it supports the strategy statement
- Consistency audit (currently financial-focused) should also check narrative consistency

### Gap 4 — Competitive Hypothesis Framework (MEDIUM IMPACT)

**The McKinsey standard:** Competitive analysis does not begin with "here are the competitors." It begins with a competitive hypothesis: "We believe we can win in segment X because of advantage Y, which competitors cannot easily replicate because of Z."

**Current state:** Porter Five Forces is fully implemented. Differentiation layers (Kaza) are present. But the skills do not guide the analyst to construct and validate a competitive hypothesis before describing competitors.

**Recommendation:** Add to `06-competitive-analysis/SKILL.md` a mandatory pre-analysis step:
```
Competitive Hypothesis Statement (must draft before analysis):
"[Business name] will win [specific segment] because of [specific advantage],
which [named competitors] cannot easily replicate because of [barrier to imitation],
giving us [specific quantified outcome] within [timeframe]."
```
The competitive analysis section then serves to *validate or refute* this hypothesis, not just describe the competitive landscape.

### Gap 5 — The Strategy Cascade Is Available but Not Integrated (LOW-MEDIUM IMPACT)

`06-competitive-analysis` references Lafley & Martin's 5-question strategy cascade (Winning Aspiration / Where to Play / How to Win / Must-Have Capabilities / Required Management Systems). This is the cleanest strategy framework available and maps perfectly to a business plan structure.

**Gap:** The cascade is referenced in the competitive analysis skill but is not used as the overarching structure for the entire plan. A plan organised around "Where to Play" and "How to Win" is immediately McKinsey-grade in its framing.

**Recommendation:** Update `00-plan-assembly/SKILL.md` to offer the Lafley & Martin Strategy Cascade as an optional top-level framing — alongside the standard 15-section structure. For sophisticated funders (PE, DFI), the cascade framing is more compelling than numbered sections.

---

## 4.3 Analytical Discipline Gaps

### Missing: Competing Hypotheses Protocol

McKinsey/Bain analysts are trained to *actively seek to disprove* their hypothesis before concluding it is correct. This intellectual honesty is what distinguishes consulting-grade analysis from advocacy documents.

**Current state:** The plan generation skills assume the business is viable and help present it well. No skill asks: "What is the most credible argument *against* this business succeeding? Have you tested it?"

**Recommendation:** Add a "Devil's Advocate Protocol" to `meta-market-validation/SKILL.md`:
1. State the three strongest arguments against the business succeeding
2. For each argument, state what evidence would confirm or refute it
3. Present and resolve each counter-argument explicitly in the plan

This is exactly the approach used in McKinsey's "Competing Hypotheses" methodology and in Berkman's DD "20 Deal-Killers" framework (already present in `meta-due-diligence`).

### Missing: Logical Coherence Audit

The 12-point consistency audit checks financial and cross-section numerical consistency. But it does not check:
- Whether the market sizing in Section 04 is consistent with the revenue assumptions in Section 10
- Whether the competitive advantages described in Section 06 match the marketing strategy in Section 07
- Whether the management team capabilities in Section 09 are sufficient for the operational plan in Section 08

**Recommendation:** Extend the consistency audit (`consistency-audit.md`) with a logical coherence checklist:
- Market size ↔ Revenue projections (SOM must be ≥ Year 3 projected revenue)
- Competitive advantage ↔ Marketing strategy (advantage must be communicated in marketing channels)
- Team skills ↔ Operational requirements (team must have skills needed for operations described)
- Risk mitigation ↔ Implementation timeline (mitigations must be scheduled)

---

## 4.4 Recommended Enhancements

| Enhancement | File to Create / Update | Priority |
|------------|------------------------|---------|
| Issue Tree mandatory checkpoint | `meta-market-validation/SKILL.md` — add Step 0 | HIGH |
| Competitive Hypothesis Statement | `06-competitive-analysis/SKILL.md` — add pre-analysis step | HIGH |
| Strategic Narrative Arc | `00-plan-assembly/SKILL.md` — add one-page strategy statement | MEDIUM |
| Devil's Advocate Protocol | `meta-market-validation/SKILL.md` — add competing hypotheses section | MEDIUM |
| Extended Logical Coherence Audit | `meta-bankability-scoring/references/consistency-audit.md` — add 8 logical coherence checks | MEDIUM |
| So-What Test in Quality Criteria | All section SKILL.md files — add to existing Quality Criteria | LOW (systematic but low effort per file) |
| Lafley & Martin as optional plan frame | `00-plan-assembly/SKILL.md` — optional structure for PE/DFI audiences | LOW |
