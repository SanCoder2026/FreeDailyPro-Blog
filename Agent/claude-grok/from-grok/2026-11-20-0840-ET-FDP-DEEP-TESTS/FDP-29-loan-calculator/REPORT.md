Sent: 2026-11-20 23:58 ET

# FDP-29 Loan / EMI Calculator (loan-calculator): deep test report for Claude

- **Written:** 2026-11-20 23:56:48 EST (box `date`, ET). Testing ran 2026-11-20 23:33–23:57 EST.
- **Tool:** https://www.freedailypro.com/tool/loan-calculator. Row 29 of TEST-ORDER.md: Pro, Finance, Tax & Retirement, grouped with test-plan rank 22 (BMI / Mortgage / Loan calculators), duplicate group C28 (Loans). **GSC data is not available.**
- **Classification:** Professional Tool, tagged `absorbable` (DUPLICATES.md). Live, at 0 remaining every export still works with no cap dialog.
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD, 10 locales + /ar, blog URL and sitemap. JS chunks: `LoanCalculator`, `LoanExtras`, `LoanWorkbench`, `loan`, `numberInput`, `useLogToolUsage`.
  - **YouTube video:** yt-dlp, 43 frames and a zoom.
  - **Headless Playwright:**
    - 40 calculation cases (20 main + 20 workbench), each checked against independent Python maths.
    - 6-context gate run.
    - Share, favorites and URL round-trip.
    - Network capture of where typed values go.
    - Print rendering; keyboard order.
    - 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** every fresh context loaded at "0 remaining" (`usageToday` 10 of 10, day key 2026-11-21). Trial uses spent: **0**.
- **Constraints kept:** guest only, no sign-in, no email or card typed (no prompt appeared), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in:** nothing on this tool needs it. No URL was blocked by sign-in.
- **Pending:** the "context with uses left" count → **RERUN-AFTER-RESET row 29** (`lc-gate.js`).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Code to look at (`evidence/js/`):
- `LoanCalculator-c-nwviyv.pretty.js`: `g`/`ae()` + `history.replaceState` (line ~159) mirror `amt/rate/term/xm/cur/m` into the URL (privacy).
- `LoanWorkbench-bbP73gp2.pretty.js`:
  - Line ~477: `useState("biweekly")` (shared frequency) and `useState("536.82")` (hard-coded target), which make Solve-for misleading.
  - `ve()` returns the nominal APR, labelled "effective annual cost".
- `LoanExtras-DkVbNvNv.pretty.js` and the `calc-print-area` wrappers decide what prints.
- `useLogToolUsage-BdvvKW0n.pretty.js`: the gate only runs when the tool is `known`.

After you ship, rerun `scripts/lc-privacy.js` (expect zero hits), `lc-gate.js`, `lc-live.js`, `lc-misc.js` and `lc-share.js`. Then run test-cases.md (LC-01…LC-36).

## Intent

Someone comparing a car, personal, home or education loan (US or Indian "EMI" users) wants:
- the payment, total cost and payoff date they can trust
- what extra payments, a different frequency or a fee really cost
- a schedule they can keep or send

They should feel this beats calculator.net or a bank's EMI page, and see the Professional Tools value.

The engine and the Loan workbench are genuinely strong. Every one of 40 cases matched independent maths:
- frequency and compounding
- solve for rate, amount or term
- APR with fees
- deferred and zero-coupon
- two-loan compare
- flat vs reducing
- INR/JPY formatting

Trust breaks in four places:
- The page promises nothing typed is transmitted, but the loan figures ride in the URL to analytics and ad servers.
- The printout omits the main result.
- "Solve for" opens with a wrong-looking rate.
- There is no blog post, and the video shows a three-field tool.

## Why: what the evidence says

- **P0: Loan figures leave the browser despite the privacy promise.**
  - Typing 48,725 / 7.37% / extra 613 sets `?amt=48725&rate=7.37&xm=613`.
  - With no reload, GA `/g/collect` carried it.
  - On reload or a shared link it also went to the server, 5 × doubleclick `/pagead/ads`, 3 × AdSense ping bodies and GA (23:40 EST, `json/privacy.json`).
  - Copy: "nothing about the loan amount, rate, or term you enter is transmitted or stored anywhere."
  - It is the same pattern as FDP-27 and FDP-28; one shared fix would cover all three.
- **P1, policy question for Santosh (not a PASS):** at 0 remaining all 9 export actions worked with no cap dialog (10 → 10, also after reload; `json/gate.json`, 23:42–23:43 EST). No strip or pass on the page. This tool is not in the Nov 20 uncounted list. With uses left: pending.
- **P1: the printout omits the result.** "Print or save as PDF" produces 6 pages:
  - It starts at "Loan workbench", with overlapping headings and chart lines and printed select boxes.
  - It has no Monthly Payment, inputs, totals or payoff.
  - The schedule header is garbled (`screens/live/printprev-1.png`).
- **P1: Solve for opens with a misleading rate.** The Target payment is hard-coded to 536.82 and the shared frequency defaults to Every 2 weeks. So the default loan (5%, $536.82/month) shows "Interest rate 13.7277%", and after changing the amount to $50,000 it shows 27.9079% (W17, W18).
- **P2 items:**
  - No dedicated blog post (`/blog/loan-calculator` 404; none in the sitemap).
  - The video shows the old 3-field UI with "10 free uses daily" (numbers correct), none of the workbench.
  - Copy says fees are not modelled and extra payments are not assumed; both exist.
  - The APR label says "effective" but shows the nominal rate.
  - Copy result / Save as text start with the date help text and omit the inputs; CSVs have no input header; 3 export bars.
  - "400.000" → a $400 loan.
  - iPhone SE overflows by 70 px (the scenario table).
  - Locales are English under 9 hreflangs; /ar 404.
  - Meta description short; "EMI" missing from the title.

## Outcomes we want

1. Typed loan figures never leave the device unless the user explicitly shares a link with numbers. Analytics URLs are stripped. Privacy copy is exact.
2. Santosh decides the trial-use policy for this tool; the page and the JSON-LD Offer reflect it.
3. Print/PDF leads with a summary (inputs, payment, totals, payoff, date), then optional scenarios and schedule. No controls, no overlaps.
4. Solve for opens consistent with the user's loan (monthly, current payment). The APR label is accurate.
5. A dedicated blog post and a current video that shows the workbench, using "trial uses".
6. P2/P3 polish per PRIORITIES.md.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | **PASS** | 40/40 cases match independent maths (`json/cases.json`, `cases-extra.json`). |
| 2 | Completeness vs competitors | PASS (strong) | The workbench exceeds common calculators (desk). Possible adds: reduce-EMI vs reduce-tenure prepayment, balloon, irregular lump sums (desk; not re-verified live). |
| 3 | Ease of use | PARTIAL | Clear two-column desktop; live updates. Solve-for default confusing; 3 export bars; "400.000" trap. |
| 4 | Layout attractiveness | PARTIAL | Clean cards and chart. iPhone SE 70 px overflow; long page with workbench. |
| 5 | Payment process | N/A (untested) | No cap dialog, pass or Stripe appeared, even at 0 remaining. |
| 6 | Information correct | PARTIAL | Maths correct. Privacy copy, fees/extras copy and the APR label are wrong. |
| 7 | Indexing | PASS | 200; no robots meta or X-Robots-Tag; canonical self; listed in the site-map snapshot. |
| 8 | SEO | PARTIAL | Title/H1/FAQPage/VideoObject OK. Meta 100 chars; "EMI" not in the title; English pages under 9 hreflangs; Offer 4.99; thumbnail alt. |
| 9 | Blog exists and accurate | **FAIL** | `/blog/loan-calculator` "Post Not Found" (live); no loan/EMI slug in the sitemap. |
| 10 | YouTube video exists | PASS | ar1i9hJwVXQ, 85 s, 6 views. |
| 11 | FAQ and guide correct | PARTIAL | 4 FAQs, mostly about dates; "When not to use" and Limitations contradict features. |
| 12 | Video shows current capabilities | **FAIL** | Old 3-field UI, "10 free uses daily"; no workbench. |
| 13 | Storage | PASS | Favorites in localStorage; history in memory (as stated). |
| 14 | Sharing | PARTIAL | Link reproduces the main result incl. currency; workbench state not kept; the mechanism leaks data (P0). |
| 15 | Downloads | PARTIAL | Both CSVs and the .txt work; print broken; text export lacks inputs. |
| 16 | Usage count | **Policy question** | At 0 remaining, 9 actions work, 10 → 10. With uses left: pending (RERUN row 29). |
| 17 | Categorization in section | PASS | Finance, Tax & Retirement with Mortgage, Paycheck, Compound Interest. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Finance, Tax & Retirement. |
| 19 | AI need/demand | PASS (demand high) | Loan/EMI is evergreen high-volume; AI not needed for the maths. |
| 20 | Merge better? | No | Distinct from Mortgage and Student Loan (C28: keep). The workbench could be reused by both. |
| 21 | Remove? | No | |
| 22 | Duplicates | None | |

## Severity summary
- P0: 1.
- P1: 3 (print, Solve-for default, trial-use policy question).
- P2: about 9.
- P3: several.
