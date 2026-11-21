Sent: 2026-11-20 23:25 ET

# FDP-28 Mortgage Calculator (mortgage-calculator): deep test report for Claude

- **Written:** 2026-11-20 23:21:43 EST (box `date`, ET). Testing ran 2026-11-20 23:02–23:20 EST.
- **Tool:** https://www.freedailypro.com/tool/mortgage-calculator. Row 28 of TEST-ORDER.md: Pro, Finance, Tax & Retirement, grouped with test-plan rank 22 (BMI / Mortgage / Loan calculators), duplicate group C28 (Loans). **GSC data is not available.**
- **Classification:** Professional Tool. The bundle tags it `absorbable` (DUPLICATES.md). Live, at 0 remaining every export still works with no cap dialog.
- **Testers:**
  - **Desk review:** expanded page copy, JSON-LD, 10 locales + /ar, /blog/mortgage-calculator. JS chunks: `MortgageCalculator`, `MortgageExtras`, `loan`, `numberInput`, `useLogToolUsage`, `csv`, `history`.
  - **YouTube video:** yt-dlp, metadata, 45 frames and zoomed crops.
  - **Headless Playwright:**
    - 48 calculation cases (44 UI + 4 blog), each checked against an independent Python amortisation.
    - 6-context export/gate run.
    - Share, favorites and URL round-trip.
    - Network capture of where typed values go.
    - Print rendering; keyboard order.
    - 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** every fresh context (23:02–23:20 EST) loaded at "0 remaining" (`usageToday` 10 of 10, day key 2026-11-21). Trial uses spent: **0**.
- **Constraints kept:** guest only, no sign-in, no email or card typed (no prompt appeared), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in:** nothing on this tool needs it. No URL was blocked by sign-in.
- **Pending:** the "context with uses left" count could not be observed → **RERUN-AFTER-RESET row 28** (`mc-gate.js`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Code to look at (`evidence/js/`):
- `MortgageCalculator-93FcJ1dd.pretty.js`:
  - `Ae` (URL keys incl. `inc`, `debts`), `ia()` and `history.replaceState` around line 594 cause the privacy issue.
  - `ra(…,15,30)` builds the fixed 15/30 comparison.
  - `o` holds the validation messages.
- `MortgageExtras-Ci9ZoUPC.pretty.js`: the export section (`mortgage-schedule.csv`), the donut and what is inside the printable area.
- `numberInput-5hjoxJ5z.js` `m()`: "400.000" parses as 400.
- `useLogToolUsage-BdvvKW0n.pretty.js`: the gate runs only when the tool is `known`.

After you ship, rerun these scripts: `mc-privacy.js` (expect zero hits), `mc-gate.js`, `mc-live.js`, `mc-misc.js` (print PDF), `mc-share.js`. Then run test-cases.md (MC-01…MC-40).

## Intent

A home buyer wants a payment they can trust before an offer or a rate lock. That means the full monthly cost (P&I, tax, insurance, HOA, PMI/MIP), cash to close, when it is paid off, what extra payments save, and whether it fits their income. Then they want to keep it (PDF/CSV) or send it to a partner or broker. They should think "this beats Bankrate/NerdWallet for my situation" and see why Professional Tools are worth paying for.

The engine is excellent. Every total, PMI/MIP duration, FHA/VA/USDA fee, extra-payment and biweekly saving and DTI ratio matched an independent calculation to the cent. Validation is clear, and the blog's numbers reproduce exactly.

Trust breaks in three places:
- The page says nothing typed leaves the browser, but price, **income and debts** ride in the URL to Google Analytics and the ad servers.
- "Print or save as PDF" prints a donut and three blank pages.
- The embedded video shows an old tool doing an impossible calculation.

## Why: what the evidence says

- **P0: Income and debt figures leave the browser despite the privacy promise.**
  - Typing price 487,250, income 9,137 and debts 612 sets `?price=487250&inc=9137&debts=612`.
  - With no reload, a GA `/g/collect` carried it.
  - On reload or a shared link it also went to the server GET, 5 × `googleads.g.doubleclick.net/pagead/ads`, and GA (23:05 EST, `json/privacy.json`).
  - The copy says: "Nothing you type is sent to a server or stored" and "Nothing is saved on our servers or in your browser".
  - This is the same mechanism as BMI (FDP-27), but with financial data.
- **P1, policy question for Santosh (not a PASS):** at 0 remaining all six exports worked with no cap dialog (10 → 10, also after reload; `json/gate.json`, 23:06–23:07 EST):
  - Copy report, Download CSV, Print or save as PDF, Copy result, Save as text, Print.
  - The page has no trial strip or pass offer.
  - Mortgage is not in the Nov 20 uncounted list (Unit Converter, Grammar Checker, Word Counter).
  - Whether a context with uses left is charged is pending (RERUN row 28).
- **P1: Print / "Print or save as PDF" is unusable.** Page 1 holds only the donut, a collapsed "How this was calculated" and Recent calculations with "Clear"; pages 2–4 are blank. Missing:
  - inputs, loan amount, total interest, cash to close, payoff and the 15/30 table
  - the amortization schedule, even when it is open
  - Evidence: `screens/live/printprev-1.png`, `testfiles/outputs/print-preview*.pdf`.
- **P1: Video p5KPFr4KYm0 is outdated and misleading.**
  - It shows the old 6-field UI with "10 free uses daily" / "8 free uses left today" badges.
  - It types a 0,043 price with an 0,034 down payment and shows 00.00, then ,053.00 with ,953/month tax.
  - Titles mismatch ("Free Step-by-Step" vs "No Signup"); 2 views (`findings/video-findings.md`).
- **P2 items:**
  - Locales: 9 hreflang variants are English pages labelled es/pt/fr/de/ja/hi/zh/ko/id; /ar 404.
  - "400.000" silently becomes a $400 home.
  - The comparison is fixed at 15 vs 30 even when the term is 20.
  - CSV yearly rows have no dates and use loan years; the screen uses calendar years. No tax/insurance/HOA columns or input summary.
  - Copy result and Copy report differ; two overlapping export bars.
  - The Limitations copy says costs are flat, but the tool models cost growth.
  - FAQ: 4 of its 5 questions are about the first payment date.
  - JSON-LD Offer 4.99 on a Professional Tool; thumbnail without alt.
  - Desktop single narrow column.
  - iPhone SE +9 px overflow; ja +3 px.
  - axe: label-content-name-mismatch (serious), ad-caption contrast (serious), heading-order, empty-table-header.
  - Share drops the biweekly option.

## Outcomes we want

1. Typed values (especially income and debts) never leave the device unless the user explicitly shares a link with numbers. Analytics `page_location` is stripped. Privacy copy is exact.
2. Santosh decides the trial-use policy for this tool. The page then shows it (strip/pass, or a clear uncounted state), and the JSON-LD Offer matches.
3. The PDF/print is a one-page "mortgage summary" (inputs, monthly breakdown, loan, cash to close, payoff, 15/30, date), with the schedule appended on request. No blank pages, no controls.
4. A current video with realistic numbers and aligned titles, without "free".
5. P2 polish as listed in PRIORITIES.md.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | **PASS** | 23/23 totals exact; PMI/MIP/VA/USDA, extras, biweekly, DTI exact (`json/cases.json`). |
| 2 | Completeness vs competitors | PARTIAL | Beats most on loan programs, dated schedule, extras, DTI, steps. No affordability mode, points/APR, ARM, refinance, or rent-vs-buy (desk; competitor feature list not re-verified live). |
| 3 | Ease of use | PARTIAL | Clear labels/help; result card on top. About 20 inputs push the breakdown far down on phones; "400.000" trap. |
| 4 | Layout attractiveness | PARTIAL | Clean dark UI, donut, chart. Desktop narrow single column with big empty margins. |
| 5 | Payment process | N/A (untested) | No cap dialog, pass, Day Pass or Stripe appeared even at 0 remaining, so there was nothing to follow. |
| 6 | Information correct | PARTIAL | Maths and program rates correct (desk vs HUD/VA/USDA published rates). Limitations "flat costs" and privacy copy wrong. |
| 7 | Indexing | PASS | 200; no robots meta or X-Robots-Tag (indexable); canonical self; listed in the site-map snapshot `sitemap-urls.txt`. |
| 8 | SEO | PARTIAL | Good title/meta/H1/FAQPage/Breadcrumb/VideoObject. English pages labelled 9 languages; Offer 4.99; default OG image; thumbnail alt. |
| 9 | Blog exists and accurate | **PASS** | Every figure reproduced live (B01–B04). Embeds the outdated video. |
| 10 | YouTube video exists | PASS | p5KPFr4KYm0, 89 s. |
| 11 | FAQ and guide correct | PARTIAL | Accurate, but 4 of 5 FAQs are about the payment date; Limitations contradicts the cost-growth feature; Privacy wrong. |
| 12 | Video shows current capabilities | **FAIL** | Old UI, impossible inputs, "free uses" badges. |
| 13 | Storage | PASS | Favorites in localStorage; history in memory only (as stated). |
| 14 | Sharing | PARTIAL | Share copies a link that reproduces the result (minus biweekly); the same mechanism leaks data (P0). |
| 15 | Downloads | PARTIAL | CSV (391 lines) and .txt work; print/PDF broken (P1); CSV lacks costs/dates on yearly rows. |
| 16 | Usage count | **Policy question** | At 0 remaining, all 6 exports work, 10 → 10. With uses left: pending (RERUN row 28). |
| 17 | Categorization in section | PASS | Finance, Tax & Retirement, next to Loan/EMI, Paycheck, Compound Interest. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Finance, Tax & Retirement. |
| 19 | AI need/demand | PASS (demand high) | Evergreen high-volume query; AI not needed for the maths; "explain my result" could be a Premium hook. |
| 20 | Merge better? | No | Distinct from Loan/EMI and Student Loan (C28: keep). |
| 21 | Remove? | No | High demand, strong engine. |
| 22 | Duplicates | None | C28 siblings have distinct intent. |

## Severity summary
- P0: 1 (privacy).
- P1: 3 (print, video, trial-use policy question).
- P2: about 11.
- P3: a few (see PRIORITIES.md).
