Sent: 2026-11-20 08:40 ET

# FDP-09 Income Tax Calculator (income-tax-calculator): deep test report for Claude

- **Written:** 2026-11-19 13:21:23 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/income-tax-calculator. Row 9 of TEST-ORDER.md. Test-plan rank 9: 7,449 impressions, position 7.5, CTR 0.1% (owner's export; **GSC data is not available** to this tester). Cluster C25 with paycheck-calculator, state-tax-calculator, self-employment-tax, 401k-calculator, uk-tax-calculator and india-income-tax.
- **Classification:** Professional Tool, Finance, Tax & Retirement. 10 trial uses a day, $1 day pass / $4.99 monthly. Reading results never uses a trial use. **Copy result, Save as text, Print and Ctrl+C inside the tool cost 1 use per visit**, and they are blocked at 0.
- **Testers:**
  - **Desk review:**
    - curl of the tool, 10 locales, /ar, /terms, /faq, /pricing, the sitemap and 5 blog posts
    - JS bundles: IncomeTaxCalculator, stateTaxData, useLogToolUsage, calcChecks, k401, numberInput, RatesNote
    - WebSearch for competitors and the brand query
  - **YouTube video:** metadata and 47 frames plus a contact sheet.
  - **Headless Playwright:**
    - 40 calculation cases, checked against an independent 2026 reference (`scripts/ref_federal.py`)
    - trial-cost tests for Copy, Save, Print and Ctrl+C at 10 and at 0
    - Custom Flat Rate, keyboard, axe and phone layout
    - matrix: 10 profiles, 10 locales, 6 geos, axe
- **Constraints kept:** guest only, no sign-in, no card or email entered (stopped at the cap dialog), no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** nothing on this tool needed sign-in. **No URLs were blocked by sign-in.**
- **Needs re-run after midnight UTC (7:00 PM ET):** one item. Does **Save as text** or **Print**, as the *first* action of a visit with uses left, cost 1 use? Six fresh contexts at 13:18 EST all loaded at 0. See row #9 in `/workspace/deep/RERUN-AFTER-RESET.md` (copy in `scripts/`), script `scripts/it-gate4.js`.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components, then restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work.

Components to look at:
- **IncomeTaxCalculator**
  - `z()` QBI
  - the state call that passes filing status and pre-tax
  - Custom Flat Rate
- **stateTaxData:** `localNote` / `localAvg`, HoH schedules, PA
- **useLogToolUsage:** the clipboard.writeText wrapper and the `copy` listener → `tryUse`
- **the Terms and FAQ trial wording**

After you ship, rerun `test-cases.md` (IT-01…IT-44).

## Intent

A US earner, freelancer or someone comparing job offers should get a trustworthy 2026 estimate of federal, FICA/SE and state tax, and take the number with them (copy, save, print) without surprises. The page competes on "income tax calculator 2026". Its CTR is 0.1% at position 7.5, so accuracy, local-tax coverage and honest wording about what costs a trial use are what will earn clicks and return visits.

## Why: what the evidence says

- **The core math is good.**
  - Employees (T01–T09) and self-employed below about $232k (T10–T14, T40) match the independent reference within $1. That covers all filing statuses, the SS wage base, Additional Medicare, the 401(k) catch-up incl. 60–63, and per-period views.
  - Validation is clear and cites the IRS.
  - Sources and rate dates are shown for each state, which is a real trust advantage over competitors.
- **A trial-cost contradiction (P0):**
  - **/terms:** "calculators … take no trial use at all".
  - **/faq (and its FAQ schema):** "unit and tax calculators … never use a trial use".
  - **The tool:** copying, saving or printing costs 1 per visit. At 0 it blocks Copy, Save and Print, and even **Ctrl+C on a number already on screen** (`gate-ctrlc-at-zero.png`).
  - 13 of 15 tracked fresh guest contexts loaded at "0 remaining today" (display-only), so most new visitors hit the dialog the first time they try to take a number away.
- **The QBI cliff (P1):**
  - Self-employed results jump by about $10k of federal tax just above $232k profit (single). Take-home *falls* by $4,437 from $232k to $240k profit.
  - The code zeroes QBI at the 24%-bracket top instead of phasing it in over $75k / $150k.
- **Silent state gaps (P1):**
  - Maryland county tax (2.25–3.30%, paid by every resident; about $2,510 at $85k) and NYC/local taxes are defined in the data but never applied or mentioned.
  - Head of household uses single state brackets: CA HoH $85k is overstated by about $2,024.
- **Smaller issues:**
  - PA lets 401(k) deferrals reduce state tax ($307).
  - No senior deduction or 65+ extra standard deduction.
  - "Effective rate" includes FICA without saying so.
  - Flat-rate mode accepts 150% and −5%.
  - The blog says the tool lacks QBI.
  - The video shows an old UI and the recorder's personal bookmarks.
  - "gratis" appears in the es title.
  - 8 locales are English-only duplicates.

## Outcomes we want

1. The Terms, FAQ and tool agree on what costs a trial use for calculators, and a guest can always at least copy a number they can see.
2. Self-employed results are continuous across the QBI threshold and match §199A (2026 threshold 201,750 / 403,500, $75k / $150k phase-in).
3. Every state result either includes local income tax where it is universal (MD), or says plainly that it is excluded, with the typical amount. HoH uses each state's HoH schedule.
4. Copy, video, locales and the blog say what the tool does today.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | 32 of 40 cases match (including all validation cases). 8 are wrong: T35–T39 SE above about $232k are off by up to $10,333 (QBI cliff), T17 MD omits county tax, T19 CA HoH is overstated by about $2,024, and T18 PA deducts the 401(k). `evidence/findings/live-functional-findings.md` §1–3, `json/cases-*.json`, `scripts/ref_federal.py` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Ahead: local-only, per-state sources and dates, SE mode with QBI, 401(k) age catch-up. Behind: local/city taxes, HoH state schedules, HSA, senior deduction, and copying a result costs a trial use. `findings/desk-findings.md` |
| 3 | Ease of use | **PASS** (minor) | LOW | Instant results, clear errors, good tab order. On 320–375 px phones the income field starts below the first screen. The flat-rate mode doesn't validate the rate. |
| 4 | Layout attractiveness | **PASS** (minor) | LOW | Clean. iPhone SE overflows to 353 > 320 px (header button + "US-Specific" badge); ja desktop +3 px. No ad overlaps; CLS ≤ 0.013. `screens/devices/` |
| 5 | Payment process | **PARTIAL** | HIGH | The cap dialog is clear ($4.99 monthly / $1 day pass) and the test stopped there. But it fires for copy, print and Ctrl+C on a calculator that the Terms and FAQ say never uses a trial use. `screens/live/gate-*-at-zero.png` |
| 6 | Information correct | **FAIL** | HIGH | The Terms and FAQ contradict the tool. The blog says QBI isn't modelled, but it is. "Effective rate" includes FICA unlabelled. Local taxes are omitted with no note. The disclaimer covers credits and itemised deductions but not the senior deduction or local taxes. |
| 7 | Indexing | **PARTIAL** | LOW | 200, self-canonical, in the sitemap with a video block. The brand query (WebSearch index, not Google) did not show the tool page in the top 5. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Strong title and H1; 156-char meta; FAQPage with 10 questions. The Offer has no billing period. 8 locales keep the English title and description and use a shorter H1. The es title says "gratis". CTR 0.1% at position 7.5 (owner data). |
| 9 | Blog post | **PARTIAL** | LOW | No dedicated post (/blog/income-tax-calculator returns 404). Related posts exist; one has a stale QBI claim. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | UvcrEE6Swwc, 141 s, 0 views, embedded and in the sitemap. |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | 10 good FAQs. The site FAQ's "never use a trial use" is wrong for this tool. Missing: local taxes, HoH state handling, the QBI limits. |
| 12 | Video shows current capabilities | **FAIL** (stale) | LOW | Old UI: a state % field, single filer only, "10 free uses daily", "200+ tools", older figures ($20,679 vs about $20,623 now). The bookmarks bar is visible. `findings/video-findings.md` |
| 13 | Storage | **PASS** | — | Nothing is stored server-side by design ("Runs on your device"; not network-audited). Inputs persist on the page; there is no project concept. |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" only; no shareable result link. Copy, Save and Print are trial-gated. |
| 15 | Downloads | **PASS** (one re-run) | MEDIUM | Save as text gave `income-tax-calculator-result.txt` with the full breakdown, the sources and "Calculated with FreeDailyPro.com". Print calls `window.print`. Save-first / Print-first cost **needs re-run after midnight UTC**. `downloads/` |
| 16 | Usage count | **FAIL** (policy) | HIGH | Copy costs 1 per visit (10 → 9, then repeats are free). Save, Print and Ctrl+C after that are free. At 0 all four are blocked. 13 of 15 fresh contexts loaded at 0 (display-only). |
| 17 | Categorization | **PASS** | — | Finance, Tax & Retirement, Professional Tool, "US-Specific" badge. The old /category/tax-calculators 301s correctly. |
| 18 | Location in site | **PASS** | — | Breadcrumb; "Guides and next steps" links the paycheck, state, SE, 401(k), UK and India tools and two blogs. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic tax math. Demand is high (7,449 impressions). GSC data is not available. |
| 20 | Merge? | **N/A: keep** and differentiate | LOW | It overlaps paycheck-calculator on take-home pay. Keep income-tax for annual liability and paycheck for per-period/W-4, and cross-link them with one line each. |
| 21 | Remove? | **N/A: keep** | — | High-impression page with correct core math. |
| 22 | Duplicates | **PARTIAL** | LOW | state-tax-calculator repeats the state module, and paycheck repeats federal + FICA. Shared modules are fine; the risk is keyword cannibalisation, not duplicate code. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.

**PASS:**
- 200 on 10 of 10 profiles (Chromium, Firefox, WebKit, phones, tablets).
- 16 px inputs on phones.
- No ad overlaps.
- The same USD results in 6 geos; a consent banner in EU geos.

**FAIL / PARTIAL:**
- iPhone SE overflows to 353 px; ja desktop +3 px.
- es title "gratis"; 8 locales are English-only; /ar 404 (not in hreflang).
- axe: header label-content-name-mismatch serious ×1; Pixel 7 ad-label contrast serious ×2.
- Results have no aria-live.

**Ads:** keep them in reserved fixed-height slots below the tool (as now). Never put one between the inputs and the result.

## Suggested direction (interpret freely)

1. **Calculator trial policy (P0).**
   - Decide one rule and make the Terms, FAQ (and its schema), the tool note, the blog and the cap dialog say it.
   - Whatever the rule, never block Ctrl+C of text already on screen. Scope the `copy` listener to the Copy button, or drop it.
   - The shared trial-meter P0 (fresh contexts at 0) from FDP-02 to FDP-08 makes this worse. Verify it server-side.
2. **QBI (P1).** Use the 2026 §199A threshold (201,750 / 403,500 / MFS 201,775) and phase in over $75k / $150k. For a no-W-2 sole proprietor the deduction falls linearly to 0. Optionally add a "W-2 wages paid / SSTB" control, and the $400 minimum.
3. **State accuracy (P1).**
   - Apply MD county tax (a county picker, or 3.20% default with a note).
   - Show `localNote` for NY, IN, OH, PA, MI and KY.
   - Use HoH schedules where states have them (CA Schedule Z, std $11,412; NY, etc.).
   - PA: don't deduct 401(k) deferrals.
4. **Clarity (P2).**
   - Label "Effective rate (incl. FICA)".
   - Add a 65+ checkbox (extra standard deduction + the 2025–2028 $6,000 senior deduction), or list it in the disclaimer.
   - Validate the flat rate at 0–100%.
   - Add aria-live on the result.
   - Fix the 320 px overflow.
5. **Content (P2).**
   - Fix the blog QBI line.
   - Re-record the video in a clean profile with the current UI.
   - Remove "gratis" / "free" (use trial-use wording).
   - Localize the titles and H1s, or drop thin locales from hreflang.
   - Add an Offer billing period.

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Don't change pricing in this work. The book watermark is intentional and separate.
- Counters are display-only evidence.
- The tax figures here come from `ref_federal.py` and the cited FTB, DLS and IRS sources. Re-verify them when the 2027 figures publish (the page says "Next review: November").

## Process

Inspect IncomeTaxCalculator, stateTaxData and useLogToolUsage → restate → propose → implement → verify with `scripts/it-live.js` + `ref_federal.py`, `it-gate*.js` and `test-cases.md`. The Save-first / Print-first cost check runs after midnight UTC.
