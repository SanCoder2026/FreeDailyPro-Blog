Sent: 2026-11-21 17:13 ET

# FDP-75 Paper Format Checker (paper-format-checker): deep test report for Claude

- **Written:** 2026-11-21 17:15 EST (box `date`, ET). Testing ran 2026-11-21 17:03–17:12 EST.
- **Tool:** https://www.freedailypro.com/tool/paper-format-checker
  - TEST-ORDER row 75: **Pro**, College & Education. Plan note "test-plan (unranked): GSC top-50 SEO backfill 15". No duplicate group (Paper Submission Desk and Citation Generator are different jobs).
  - Strip "Trial: 10 uses/day", Quick Buy $1 day / $4.99 monthly (all 6 geo contexts). JSON-LD Offer $4.99.
  - Video f4VPRP4U4iM (embedded, 99 s, uploaded 2026-09-24). Blogs /blog/check-docx-paper-format-apa-mla-chicago (the tool's own, embeds the video) and /blog/journal-submission-pack-paper-desk (sibling, links here). Both 200.
  - **GSC data is not available.** No API/MCP testing.
- **How it works (`PaperFormatChecker-RAfBEqf7.js`, pretty copy `PFC.pretty.js`):**
  - Style select APA 7 / MLA 9 / Chicago 17, a `.docx` drop zone (`gateAtDownload`), "Open from Google Drive".
  - The file is unzipped in the browser (JSZip). document.xml, styles.xml, theme1.xml and every header*/footer*.xml are parsed. Nine checks: margins (every section), Letter size, font, size, double spacing (≥90 % of body text), no extra paragraph spacing, 0.5" first-line indent (≥80 %), 0.5" hanging indent under a References / Works Cited / Bibliography heading, and a PAGE field. Fonts, sizes and spacing follow the full chain (doc defaults → theme → styles → direct paragraph/run formatting), weighted by body-text share.
  - `logUsageNow()` runs after a file parses; if it returns false, the cap dialog shows and no report is drawn. Switching the style re-scores the same file with no charge.
- **Testers:**
  - Desk: page copy (FAQ, how-to, tips), JSON-LD, both blogs, JS.
  - 16 test papers built with python-docx (`scripts/make-testfiles.py`, files in `evidence/testfiles/`).
  - Playwright, guest:
    - `zero.json`: a context at 10/10 (Chromium): drop apa-good, a wrong-extension file, Open from Google Drive.
    - `left-firefox.json`: a Firefox context at 0/10 (found on try 9 of 30). 14 papers dropped in one page load via "Check another file", each checklist read; APA + MLA + Chicago for 3 of them; then a reload + drop (L90) and the same file again (L91). Every `usage.log` POST was logged and searched for document text.
    - `left.json`: Chromium, 40 tries, none with uses left.
    - `quickbuy.json`: Day Pass → email dialog (stopped); Monthly → Stripe checkout (stopped, ID redacted).
  - **Offline harness** (`scripts/px75-harness.js`): the tool's own checker function `De`, copied verbatim from the bundle, run under node with @xmldom/xmldom + jszip on every test paper for all three styles (`evidence/harness/`). It matches the live checklist row for row on every paper tested live, and covers `footer-pageno.docx`, which was not dropped live.
  - Video frame sheet + frames; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested, rows in SIGNIN-NEEDED.md):** Open from Google Drive (Google sign-in popup, closed); paid-pass output (Day Pass stopped at email, Monthly stopped at Stripe).
- **RERUN-AFTER-RESET:** none. Behaviour was observed both at the cap and with uses left.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to a student who wants to know, the night before a deadline, whether their .docx meets APA, MLA or Chicago, and whether the page turns that need into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is a P1 gate gap. A full-quality result at 0 is a pending owner question. A real save at 0 is P1 (Nov 21, corrected 1:19 PM).

**P0:** none found.

**P1 — per-page-load charging (gate gap):**
- In one Firefox page load starting at 0/10, the first paper (apa-good) took 1 use (0/10 → 1/10, 1 `usage.log` POST).
- The next **13 different papers** (word-default, a4-narrow, direct-format, mixed-fonts, exact-24pt, two-sections, refs-no-hanging, georgia-11, no-page-number, empty, long-60p, minimal, not-docx) were all fully checked with **0 POSTs**; the counter stayed at 1/10.
- After a reload, the next drop charged again (1/10 → 2/10, L90). The same file again in that load: no charge (L91).
- So one trial use buys unlimited checks until the tab is reloaded, and the cap dialog never comes. Same mechanism as #44/#50/#51/#57 (`logUsageNow` remembers "already charged" per load).
- At the cap it holds: at 10/10, dropping apa-good shows the cap dialog ("You've used today's 10 trial uses…") and no report, with 0 POSTs.
- Fix direction: charge per new document (hash of the file) and re-check the cap on every drop.

**P2 — where to look:**
- **The only FAQ is wrong.** "Does this catch formatting I applied to individual paragraphs? No — this checks your document's default formatting (margins and the Normal style's font, size, and spacing). If you've manually formatted individual paragraphs differently, those won't be caught."
  - The code and the page's own text say otherwise: "Reads the formatting Word actually applies — the style chain, document defaults, theme fonts, direct paragraph and run formatting…" plus the tip "Each result is weighted by how much of your body text it covers".
  - Live: `direct-format.docx` (Normal style is APA-perfect TNR 12 double; every paragraph is directly set to Arial 10 single) → Font "Found: Arial (100%)", Size **FAIL** "10 pt", Spacing **FAIL** "1×". Direct formatting is caught.
  - The FAQ undersells the tool's main differentiator and tells students to distrust it. The video still shows the old note with the same claim.
- **Video f4VPRP4U4iM is out of date and shows a personal bookmarks bar.**
  - It shows the old 4-check version (margins, font, size, line spacing) where the demo file "Smaple.docx" gets three "Couldn't detect" warnings (frame 0:52), the old "Pro" chip, no trial strip, "Drop your .docx paper" with "Works with any file size", and the old "checks your document's default formatting" note.
  - The browser bookmarks bar is visible throughout (Email, Prime Video, Netflix, YouTube, Twitch, "Welcome to Zepto", Work folder) — frame 0:17, `video/f17.jpg`.
  - Re-record in a clean profile with a paper that shows pass and fail rows.
- **Locale pages:** es/pt/fr/de/ja/hi/zh/ko/id return 200 with translated navigation, badge, strip and Quick Buy, but the H1, subtitle, "Check against", the drop zone text and the FAQ stay English.

**P3:**
- "Page numbers in the header (top right)" passes a page number centred in the **footer** (`footer-pageno.docx`, harness): footers are read as headers, and alignment isn't checked. APA and MLA both want top right. Either check header + right alignment, or relabel the row.
- An empty .docx gets PASS for margins, page size and page number plus 4 "No body text" warnings, but no overall "this document has no text" message.
- `minimal.docx` (no styles.xml): font "Found: unknown" is reported as FAIL rather than undetermined.
- The cap dialog says passes remove "the 'Created with FreeDailyPro.com' mark from your PDFs and images"; this tool has no output to mark.
- Blog TOC shows a literal HTML entity: "Worked example: Maya&#39;s literature review" (heading and anchor). The blog says 300+ tools; the video end card says 200+.
- The page subtitle and drop-zone line mention only "margins, font, and line spacing"; it checks nine things.
- iPhone SE: 9 px overflow (329/320, a header button). ja desktop overflows by a few px. Desktop 1366 CLS 1.0 from a body shift at 427 ms (boot). axe desktop: label-content-name-mismatch (serious, `.right-2`) and region (moderate); Pixel 7 clean.

## Intent

A student wants to know whether their .docx meets the style sheet before submitting. The checker does that well: on all 16 test papers every row was right (margins per section, A4, mixed fonts, Georgia 11 accepted for APA and failed for MLA size, exactly-24 pt spacing counted as double, missing hanging indent, missing page field, invalid files refused clearly), and no document text leaves the browser. The open points are a charge that only happens once per page load, an FAQ that denies the tool's best feature, and a stale video.

## What works

- **Accuracy:** live checklist = harness on every paper (table in test-cases.md). Word-default (Cambria 11, 1.15, 8 pt after, 1.25" sides, no page number) fails 7 of 9 rows with helpful details ("Word's default 8 pt after is the usual culprit").
- **Per-style rules:** Georgia 11 → APA PASS, MLA size FAIL, Chicago font WARN ("acceptable if your instructor allows"). Cambria → Chicago WARN.
- **Sections:** two-sections → "1 of 2 sections differ". A4 → "A4 and other sizes aren't what US style guides assume".
- **Long paper:** 220 paragraphs (~60 pages) checked in a few seconds; "220 of 220".
- **Invalid input:** a renamed PDF → "This isn't a valid .docx file… use Save As .docx… then drop it again", no charge. `.doc` → inline extension error.
- **Privacy:** no `usage.log` POST contained document text ("Files never stored / Runs on your device" holds).
- **Gate at the cap:** cap dialog, no report.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 9 checks, 3 styles, sections, weighting. |
| 2 | Completeness | PASS (minor) | No title-page/running-head checks (blog says manual). |
| 3 | Ease of use | PASS | One drop, clear rows, "Check another file". |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | PASS (to the stop) | Day Pass → email; Monthly → Stripe. Not paid. |
| 6 | Information correct | **FAIL** | FAQ says direct formatting isn't caught; it is. |
| 7 | Indexing | PASS | 200, canonical self, hreflang set. |
| 8 | SEO | PASS | Title "Check APA/MLA/Chicago Format Online"; meta 113 chars. |
| 9 | Blog | PASS (minor) | Accurate; literal `&#39;` in TOC. |
| 10 | YouTube video | PASS | Embedded, linked from the blog. |
| 11 | FAQ / guide correct | FAIL | The only FAQ is wrong. |
| 12 | Video shows current capability | FAIL | Old 4-check version, "Couldn't detect" demo, personal bookmarks bar. |
| 13 | Storage | PASS | Nothing uploaded; no doc text in POSTs. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | N/A | On-screen report only. |
| 16 | Usage count | **FAIL (P1)** | 1 use per page load; 14 papers for 1 use. |
| 17 | Categorization in section | PASS | College & Education. |
| 18 | Correct section of site | PASS (minor) | "More from College & Education" shows cost, loan and 529 calculators, not the writing siblings (Citation Generator, Paper Submission Desk); the guides link Paper Submission Desk. |
| 19 | AI need and demand | PASS | "apa format checker", "mla format checker", "check paper formatting". |
| 20 | Merge better? | No | Paper Submission Desk is a journal-pack job. |
| 21 | Remove? | No | GSC top-50 backfill; works well. |
| 22 | Duplicates | None | — |

## After fixes, rerun

- `px75-live.js left firefox` (TRIES=30): each new paper should take one use; the cap dialog should appear on the 11th distinct paper in one load.
- `px75-live.js zero`; harness + live on `footer-pageno.docx` if the page-number row changes.
