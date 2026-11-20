Sent: 2026-11-20 08:40 ET

# FDP-10 State Tax Calculator (state-tax-calculator): deep test report for Claude

- **Written:** 2026-11-19 13:33:02 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/state-tax-calculator. Row 10 of TEST-ORDER.md, grouped with test-plan rank 9 (Income Tax / Tax Calculator). Cluster C25 with income-tax-calculator (#9), paycheck-calculator (#11), self-employment-tax, 401k-calculator, uk-tax-calculator and india-income-tax. **GSC data is not available.**
- **Classification:** Professional Tool, Finance, Tax & Retirement. 10 trial uses a day, $1 day pass / $4.99 monthly.
  - Reading results and Compare all states are free.
  - The first of Copy report, Download CSV, Print or save as PDF, Copy result, Save as text or Print costs **1 use per visit**. They are blocked at 0.
  - Per owner policy, copying and results may count as trial uses, so only the wording that promises otherwise is a defect.
- **Testers:**
  - **Desk review:**
    - curl of the tool, 9 locales, /ar, the sitemap and the blog
    - JS bundles: StateTaxCalculator, stateTaxData, CalcReport, report, useLogToolUsage
    - WebSearch for competitors, the brand query, and official 2026 sources (FTB, NC G.S. 105-153.5, Utah TC-40, OR-40, 30 Del. C. § 1110, phila.gov, the MD Comptroller)
  - **YouTube video:** metadata, 32 frames and a contact sheet.
  - **Headless Playwright:**
    - 31 calculation cases
    - the full 51-state comparison at $75k, checked against SumAtlas
    - the blog's $95k table re-checked
    - all six export actions at 10 and at 0
    - keyboard, axe and phones
    - matrix: 10 profiles, 9 locales + /ar, 6 geos, axe
- **Constraints kept:** guest only, no sign-in, no card or email entered (stopped at the cap dialog), no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** nothing on this tool needed sign-in. **No URLs were blocked by sign-in.**
- **Nothing pending:** a context with uses left was found, and all six export actions were observed. No RERUN-AFTER-RESET row was added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components, then restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work.

Components to look at:
- **stateTaxData `s()`:** `std[mfj?1:0]`, joint brackets only for MFJ, `exemption*S`, `credit`, `localAvg`. This is shared with income-tax-calculator and paycheck-calculator.
- **The Utah entry** `c("UT","Utah",4.45)`.
- **StateTaxCalculator:**
  - `de(a)` parsing and the missing invalid state
  - `pe(x, N)` notice logic
  - compare rows
  - the two export bars
- **The Terms and FAQ trial wording.**

After you ship, rerun `test-cases.md` (ST-01…ST-40).

## Intent

Someone choosing where to live or comparing job offers wants a trustworthy state-by-state figure, including city tax where it matters, and the ability to take it with them. The page already outdoes most competitors on local taxes and payroll programs. Its weak points are filing-status accuracy, a couple of states' structures, input validation, and a video that shows a wrong number.

## Why: what the evidence says

- **The core is strong:**
  - CA, NY, NYC (bands), Yonkers, every MD county incl. the banded ones, Philadelphia (rates from 1 July 2026), IL, MA, NJ and WA payroll all match the official sources to the cent.
  - The ranking lists all 51.
  - The CSV is clean.
  - Sources and "as of" dates are shown for each state and payroll line.
- **Head of household = single, everywhere (P1).**
  - The shared engine never uses a state's HoH deduction or HoH brackets.
  - CA HoH $75k is overstated by **$1,656** ($2,774.57 vs $1,118.19, FTB Schedule Z); NC HoH by $254.
  - Income-tax-calculator (#9) inherits this.
- **Utah's structure is wrong (P1).** Utah has no standard deduction; it has a 6% taxpayer credit that phases out above $18,696. The tool deducts $16,100 instead and **understates by about $482** at $75k (up to $716 at higher incomes).
- **Silent $0 (P1).** "85k" or "abc" shows "$0.00" with no error, where the income tax tool rejects the same input.
- **The embedded video (P1).** It shows the old tool computing **$9,975** for California at $75k (13.3% on all income), against $2,774.57 now. It also uses "free" wording and shows the recorder's personal bookmarks.
- **Wording (P1, shared).** /terms and /faq say calculators never use a trial use. The tool (as intended per owner policy) charges 1 per visit for copy, save or print. Fix the Terms and FAQ wording.
- **Smaller issues (P2):**
  - OR $256, DE $110 (and likely IA and RI) personal credits are omitted, while the FAQ says "any state credit is taken off".
  - A "local tax not included" notice shows even when a city line is included.
  - The NY 3.5% box applies to all of NY.
  - Compare rows aren't keyboard-selectable.
  - The blog's $95k table is stale (NY, CA, OR).
  - All 9 locales are in English.
  - The Offer has no billing period.

## Outcomes we want

1. HoH (and every filing status) uses each state's own deduction and brackets, in all three tools that share the engine.
2. States whose structure isn't "deduction + brackets" (Utah's credit; OR, DE and IA credits) are modelled, or are flagged on the result line.
3. Invalid income shows an error, never a confident $0.
4. The video, blog and Terms/FAQ match what the tool does now.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | 23 of 31 cases are exact vs official sources. 6 are wrong: HoH in CA/NC/NY (S02, S05, S27), OR credit omitted (S30), and "85k"/"abc" → $0 (S15, S17). 2 GA cases are unverified. Utah is understated by about $482 (compare table). `findings/live-functional-findings.md`, `json/cases-S01-S30.json`, `json/compare-75000-single.json` |
| 2 | Completeness vs. competitors | **PASS** (ahead) | LOW | Ahead on named local taxes with bands, 7 payroll programs, steps, CSV/PDF and the 51-state rank. Behind on HoH, personal credits, two-state compare and a "next $1,000" figure. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Instant, clear, good defaults. But there is no error on "85k"; two export bars duplicate each other; and the local notice contradicts a picked city. |
| 4 | Layout attractiveness | **PASS** (minor) | LOW | Clean. The compare table scrolls inside a box on phones (426 px table in 286–378 px). See `findings/devices-locales-findings.md`. |
| 5 | Payment process | **PASS** | LOW | The cap dialog is clear ($4.99 / $1); the test stopped there. The "Copy report" dialog says "downloading needs a pass". |
| 6 | Information correct | **PARTIAL** | HIGH | Per-state sources and dates are excellent. The video shows $9,975 for CA $75k. The FAQ "any state credit is taken off" vs the footer "credits not modelled". Terms/FAQ trial wording vs the tool. |
| 7 | Indexing | **PASS** | — | 200, self-canonical, in the sitemap with a video block, #1 for the brand query (WebSearch index). **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | LOW | Strong title and meta; FAQPage with 7 questions. The Offer has no period. 9 locales are English duplicates. The sitemap video title says "Free". |
| 9 | Blog post | **PARTIAL** | LOW | /blog/state-tax-calculator: good angle, but the NY/CA/OR figures are stale and it has the "federal standard deduction as starting point" error. It doesn't mention the city picker. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | uRiqzi4ARPY, 96 s, 0 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | LOW | 7 FAQs match the city list and payroll lines. The credit sentence is wrong for OR/DE/IA. HoH limits aren't mentioned. |
| 12 | Video shows current capabilities | **FAIL** | HIGH | Old UI, top-rate-on-everything result ($9,975), "free" wording, personal bookmarks. `findings/video-findings.md` |
| 13 | Storage | **PASS** | — | "Recent calculations" are kept only while the page is open; no localStorage key was found. Runs on the device (not network-audited). |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" only; no shareable result link. Copy and exports are trial-gated (intended). |
| 15 | Downloads | **PASS** | — | CSV (BOM, numeric, no formulas), .txt with full sources, Print/PDF via `window.print`. `downloads/` |
| 16 | Usage count | **PASS** (behaviour) / wording **FAIL** | MEDIUM | 1 use per visit on the first export, consistent with the page note. Terms/FAQ say calculators take none, so fix the wording (owner policy). 7 of 9 fresh contexts loaded at 0 (display-only). |
| 17 | Categorization | **PASS** | — | Finance, Tax & Retirement; US-Specific. |
| 18 | Location in site | **PASS** | — | Breadcrumb, guides, links to the income tax and paycheck tools. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic. Demand is grouped with rank 9. |
| 20 | Merge? | **N/A: keep** | — | A distinct job (state compare, city lines). Share the engine with #9 and #11 (already the case). |
| 21 | Remove? | **N/A: keep** | — | Strong, sourced, #1 for its brand query. |
| 22 | Duplicates | **PARTIAL** | LOW | The engine is reused in #9 and #11; one fix covers all three. No duplicate page. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**Ads:** keep them in reserved fixed-height slots below the tool (as now). Never put one between the inputs and the result.

## Suggested direction (interpret freely)

1. **Filing status (P1).**
   - Give each state entry an HoH deduction and HoH brackets (or a multiplier), and use them in `s()`.
   - Start with CA (Schedule Z, $11,412), NY and NC ($19,125), then sweep the Tax Foundation table.
   - Re-run S02, S05 and S27 plus the HoH compare.
2. **Utah (P1).** 4.45% of income minus the taxpayer credit: 6% × (federal standard deduction + $2,167 per dependent), less 1.3% of income over $18,696 / $28,045 / $37,392. No standard deduction.
3. **Input (P1).** Reuse the income tax tool's validation: "Enter an income as a number". Optionally accept "85k".
4. **Video (P1).** Re-record the current UI in a clean profile, with trial-use wording.
5. **Wording (P1, shared).** Align /terms and /faq with the tool's "Copying, saving or printing uses 1 per visit" (owner policy).
6. **P2:**
   - Model the OR $256 and DE $110 personal credits (and check IA and RI), or fix the FAQ sentence.
   - Make the local notice say "Includes <city>" when a locality is picked.
   - Label the NY box "NYC residents only".
   - Make compare rows buttons.
   - Merge the two export bars.
   - Refresh the blog table.
   - Add an Offer period; localize or trim the locales.
   - Verify SC, WI, NE, AR, GA, MT, ME and AZ against their 2026 forms (they differ from SumAtlas by more than $100).

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Owner policy: copying and results can count as trial uses. Fix the wording, not the gate.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence.
- Secondary-source differences (SumAtlas) are leads, not proof.

## Process

Inspect stateTaxData `s()` and the StateTaxCalculator parsing and notice → restate → propose → implement → verify with `scripts/st-live.js`, `st-compare.js` and `test-cases.md`.
