Sent: 2026-11-21 03:05 ET

# FDP-39 Compare PDF (compare-pdf): deep test report for Claude

- **Written:** 2026-11-21 03:03 EST (box `date`, ET). Testing ran 2026-11-21 02:49–03:01 EST.
- **Tool:** https://www.freedailypro.com/tool/compare-pdf. Row 39 of TEST-ORDER.md: Pro, PDF Tools. Plan note "L-243 rank 1 (PDF Toolkit API live)".
  - Duplicate group C24 (audio-comparer, text-similarity-checker, diff-checker).
  - Blogs: /blog/compare-pdf and /blog/compare-pdf-document-differences.
  - Video: f-QHfStX3Po.
  - **GSC data is not available.**
- **Classification:** Professional Tool. Text extraction and the diff run in the browser; no upload or API call was seen (`evidence/json/privacy.json`).
- **Testers:**
  - **Desk review:** copy, 13 FAQs, JSON-LD, 10 locales + /ar, blog, JS chunks.
  - **Headless Playwright:**
    - 19 live cases in Chromium (5 also in Firefox)
    - a uses-left gate run (7 report downloads)
    - an at-0 run (full result, reports → cap dialog, Day Pass, Quick Buy, keyboard)
    - privacy + Share
    - the 10-device / 11-locale / 6-geo / axe matrix
  - **Report checks:** `pdftotext` and a page render of the downloaded reports.
- **Test pairs:** 14 generated PDFs (`scripts/make-pdfs.py`), with known edits, restyling/reflow, a blank page, a scan, two columns, 50 pages with one edit on page 37, Unicode, 3,200 lines and hyphenation; plus a locked, a corrupt and a fake PDF.
- **Starting counts (display-only):** the 1st fresh context loaded at 0; the 2nd had 10 left and ran the gate.
- **Constraints kept:**
  - Guest only and no sign-in. No email or card typed: stopped at the Day Pass email prompt and at Stripe Checkout (session id redacted).
  - No ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):** "Open from Google Drive" on both slots, not clicked. Reports offer no Drive or cloud save.
- **Pending:** nothing needs the 7:00 PM ET reset, so there is no RERUN-AFTER-RESET row.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

**Owner context:**
- On Nov 20 Santosh decided that every Download on Barcode Generator and Invoice Generator uses a trial use. Charging only the first Download per page load conflicts with that decision.
- Full-quality results at 0 trial uses are also P1 gate gaps, and the Oct 30 rule counts results as trial uses.
- This tool has both. For a comparison tool, the on-screen redline *is* the product.

**Code to look at:**
- **`ComparePdf-DabDAhev.pretty.js`:** Compare has no usage call. Report (PDF) goes through the shared gated `D` button; Report (.txt) goes through `K` = ToolPage `vt` → `Sa`.
- **Gating options:**
  - Charge (or check) at Compare, as Oct 30 implies for results.
  - Or, at 0, show only the counts and the first change, with the rest behind the pass.
- **Per-page-load counting:** shared `index-B1CTyGtY.js` `RA`/`xI`/`DI` with the set `Kt` (`evidence/js/index-B1CTyGtY.excerpt-usage.js`).
- **Dark theme:** the diff spans' `dark:text-red-300` / `dark:text-green-300` aren't taking effect; the computed colour is red-700 / green-700.

**After you ship:**
1. Rerun `scripts/cp-gate.js`: B and C must charge, and the result at 0 must not show the full redline.
2. Rerun `cp-live.js chromium` (accuracy must stay at 6/6 on K01) and `cp-privacy.js`.
3. Work through test-cases.md (CP-01…CP-30).

## Intent

Someone has two versions of a contract or report and needs to know exactly what changed before they sign or send. They want:
- every real wording change, with page numbers
- no noise from reflow, headers or styling
- a record to attach
- nothing uploaded

The engine delivers:
- Exactly the 6 planned edits on the test contract, down to a case change and a dropped full stop.
- A one-word change on page 37 of 50 found and located.
- Restyled, rewrapped and repaginated copies correctly reported as "same text"; hyphenated line ends re-joined.
- Scans named and pointed to OCR; empty pages listed.
- Locked files unlocked in the page.
- Clean PDF and .txt reports.
- Nothing leaves the tab.

Revenue and trust break in three places:
- **Gate:** the whole redline is free at 0, and only the first report per page load is charged.
- **Readability:** in the default dark theme the changed words are dark red/green on dark rows.
- **Content:** the video is from an older engine and exposes personal files; the blog, FAQ and protected-file messages have drifted.

## Why: what the evidence says

- **P1 gate gap: full result at 0 trial uses** (`gate.json` → `zero`, 02:59–03:00 EST).
  - At "0 remaining today", Compare showed "6 changes · 1 added · 1 removed · 4 edited", every paragraph with word marks, Side by Side, and navigation. The text is selectable.
  - Only the two Report buttons open the cap dialog. Compare is never counted (0 → 0 even with uses left).
- **P1 gate gap: one trial use per page load** (02:53–02:58 EST):
  - Report (PDF) A 0 → 1; A2, then Report (.txt) T, stayed at 1.
  - New Comparison → B (.txt) 1 → **1**; New Comparison on 50 pages → C (PDF) 1 → **1**.
  - After a reload, D 1 → 2 and E 2 → 3.
- **P2: dark-theme diff contrast.** Removed and added words measure about 1.7:1 and 1.3:1 (`evidence/screens/zoom-dark-marks.png`).
- **P2: video out of date and exposes personal details.**
  - Old line-diff UI and "10 free uses daily", and it compares two unrelated files.
  - The macOS picker shows the user folder "chaithra", the tag "Anu ma'am" and personal file names.
- **P2: copy drift on protected files and cost.**
  - The blog says protected files fail and "remove the password in your PDF reader". Live there is an unlock dialog.
  - Cancelling shows inline "Unlock it with Unlock PDF" alongside a toast "Use Unlock on its row", but there is no row here.
  - The blog implies Compare costs a use; it doesn't.
- **P3 items:**
  - The FAQ still says "Download Report saves a plain text file", and says "few thousand lines" vs "3000 paragraphs".
  - VideoObject name mismatch.
  - Title/meta English in 9 locales; /ar 404.
  - iPhone SE 9 px, ja 3 px overflow; axe label mismatch / region / ad-caption contrast.
  - 3,000-paragraph limit message: unverified (dense lines merge into paragraphs).

## Outcomes we want

1. At 0 trial uses the full redline isn't available for free. Either Compare is counted, or the free view is clearly partial, matching the Oct 30 rule.
2. Every report download is counted the way Santosh decided, including after New Comparison without a reload.
3. Changed words are readable in both themes (WCAG AA 4.5:1).
4. A current-UI video using a real two-version contract, with no personal folders or files visible and "trial uses" wording.
5. One accurate story about locked PDFs across blog, FAQ, inline text and toast. FAQ updated for the two report formats.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | 6/6 planned edits; page 37 of 50; reflow/restyle = same; hyphen join; scans; Unicode; unlock. |
| 2 | Completeness vs competitors | PASS | Paragraph + word diff, two views, navigation, PDF/.txt reports. No visual/pixel compare (stated honestly). |
| 3 | Ease of use | PASS | Two labelled slots, clear counters, precise messages. |
| 4 | Layout attractiveness | PARTIAL | Dark-theme marks about 1.3–1.7:1; iPhone SE 9 px, ja 3 px. |
| 5 | Payment process | PASS (stopped) | Cap dialog / Quick Buy day → "Day Pass, $1" email prompt; monthly → Stripe Checkout. Stopped. |
| 6 | Information correct | PARTIAL | Engine claims are accurate; protected-file and report-format lines are stale. |
| 7 | Indexing | PASS | 200; canonical self; in sitemap. |
| 8 | SEO | PASS (minor) | Good title, meta 104 chars, FAQPage 13, VideoObject. Name mismatch; locales English title/meta; /ar 404. |
| 9 | Blog exists and accurate | PASS (minor) | /blog/compare-pdf accurate except the locked-file and trial-cost lines. |
| 10 | YouTube video exists | PASS | f-QHfStX3Po embedded. |
| 11 | FAQ and guide correct | PARTIAL | "Download Report saves a plain text file" is stale; line vs paragraph limit wording differs. |
| 12 | Video shows current capabilities | **FAIL** | Old engine and UI; unrelated files; personal folders and files visible; "free uses". |
| 13 | Storage | PASS | Nothing stored; Drive open needs sign-in (untested). |
| 14 | Sharing | PASS | Share copies only the tool URL. |
| 15 | Downloads | PASS | `pdf-comparison-report.pdf` (badged) / `.txt`, both match the screen. |
| 16 | Usage count | **FAIL (2 × P1)** | Full redline at 0 (Compare uncounted); B and C free after the first charge per page load. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › PDF Tools. |
| 19 | AI need/demand | PASS (demand strong) | "compare pdf" is a high-intent evergreen query. An optional AI "summarise the changes" could be a Premium Applications add-on. |
| 20 | Merge better? | No | C24 peers take other inputs; Diff Checker is cross-linked. |
| 21 | Remove? | No | |
| 22 | Duplicates | C24 (no true duplicate) | Shares the diff engine with Diff Checker; PDF-specific header and paragraph logic. |

## Severity summary
- **P0:** 0. Accuracy and privacy hold.
- **P1:** 2 (full redline at 0 trial uses; one use per page load).
- **P2:** about 3 (dark-theme diff contrast, video, protected-file and cost copy).
- **P3:** several.
