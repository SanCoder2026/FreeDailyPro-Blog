Sent: 2026-11-21 03:27 ET

# FDP-40 Extract Pages & Text (extract-pdf): deep test report for Claude

- **Written:** 2026-11-21 03:24 EST (box `date`, ET). Testing ran 2026-11-21 03:05–03:22 EST.
- **Tool:** https://www.freedailypro.com/tool/extract-pdf. Row 40 of TEST-ORDER.md: Pro, PDF Tools. Plan note "L-243 rank 1 (PDF Toolkit API live)".
  - Duplicate group C09 (split-pdf, crop-pdf, remove-pdf-pages, rotate-pdf, organize-pdf).
  - Video: XZ3ghDwxXf4. No dedicated blog post.
  - **GSC data is not available.**
- **Classification:** Professional Tool. Page copying and text extraction run in the browser; no upload or API call was seen (`evidence/json/privacy.json`).
- **Testers:**
  - **Desk review:** copy, 13 FAQs, JSON-LD, 10 locales + /ar, JS chunks.
  - **Headless Playwright:**
    - a probe (the only context with uses left)
    - an at-0 gate run (text at 0, manual copy, Copy/Download → cap dialog, pages preview, Day Pass, Quick Buy, keyboard)
    - 9 V cases (preview-checked) + 16 K cases in Chromium (K also in Firefox)
    - corrupt-file check, privacy + Share
    - the 10-device / 11-locale / 6-geo / axe matrix
- **Test files:** `E01_mixed_8p_bookmarks_form.pdf` (8 pages: bookmarks per page, a text field and checkbox, a table, header and page numbers, two columns, Unicode; `scripts/make-pdfs.py`) plus earlier P01/P02/P03/U01/U05/C04/C05/C08/P06/P07.
- **Starting counts (display-only):** the probe context at 03:06 EST had 10 left (1 used by its Copy). Every one of the 22 fresh contexts after that loaded at 0.
- **Constraints kept:**
  - Guest only and no sign-in. No email or card typed: stopped at the Day Pass email prompt and at Stripe Checkout (session id redacted).
  - No ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):** Save to Google Drive, Save to my cloud storage (shown with the text result; not clicked, because the uses-left run that clicks them could not start) and Open from Google Drive (not clicked).
- **Pending: RERUN-AFTER-RESET row 40.** Still to check:
  - per-page-load counting for Download/Copy
  - downloaded-output checks: page order, duplicates, bookmarks, form fields, file name, badge, .txt file

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

**Owner context:**
- On Nov 20 Santosh decided that every Download on Barcode Generator and Invoice Generator uses a trial use. Charging only the first Download per page load conflicts with that decision.
- Full-quality results at 0 trial uses are also P1 gate gaps, and the Oct 30 rule counts copy and results as trial uses.
- Here the extracted text is the result, and it's fully readable and selectable at 0.

**Code to look at:**
- **`ExtractPdf-C5BRKXT9.pretty.js`:**
  - Extract (`q`) has no usage call. Text goes into a `readOnly` textarea, which is still selectable.
  - Copy (`G`) is behind `gateShare`.
  - Options: at 0, show a short excerpt or no text, or count at Extract Text.
- **The loader `L`** sets the page box to "1", so Extract Text defaults to page 1 only. Either leave the box empty in text mode or change the copy.
- **Pages preview** (`R`/`Al`, 0.8-scale first page) is fine.
- **Shared per-page-load set `Kt`** (`evidence/js/index-B1CTyGtY.excerpt-usage.js`): likely the same once-per-load pattern as #35–39. Not yet observed here.

**After you ship:**
1. Run the RERUN row 40 scripts.
2. Rerun `scripts/ex-gate.js`: at 0, the full text must not be available.
3. Rerun `ex-live.js chromium K`, then work through test-cases.md (EX-01…EX-30).

## Intent

Someone needs a few pages of a long PDF to send, or the text of a PDF to paste elsewhere. They want:
- the right pages in the right order
- forms and bookmarks intact
- clean text with tables usable in a spreadsheet
- nothing uploaded

The engine delivers:
- Typed order honoured (5,1,3 starts with page 5); odd/even buttons; tolerant parsing (`1,,3;;5 , 7`); precise errors ("outside this PDF's 8 pages", "starts after it ends", "isn't a valid page number").
- Text with `--- Page N ---` markers, tab-separated table rows, form values, column order, Unicode.
- A scanned-page notice with an OCR link; corrupt files sent to Repair; locked files unlocked in the page.
- Nothing leaves the tab.

Revenue and trust break in four places:
- **Gate:** the full text is free at 0.
- **Defaults:** text mode silently gives page 1 only.
- **Discovery:** no blog post; an old video that never shows text mode and exposes personal files.
- **Copy drift:** locked PDFs and the "all pages by default" line.

## Why: what the evidence says

- **P1 gate gap: full extracted text at 0 trial uses** (`gate.json` → `zero`, 03:09–03:10 EST).
  - Extract Text returned all 8 pages (2,210 chars), and the count stayed at 10.
  - Ctrl+A/Ctrl+C in the read-only box copied all 2,210 chars. Copy and Download Text File opened the cap dialog.
  - With uses left, Extract Text was 0 → 0 and only Copy cost a use (probe, 03:06 EST).
- **P1 (pending verification): per-page-load counting.** It couldn't be observed because no uses-left context appeared after 03:06 EST. Rerun row 40. Downloads go through the same shared gated button as #35–39.
- **P2: text default is page 1 only.** On load the box reads "1", so Extract Text gives 227 of 2,210 chars (K06). The How-to says "all of them by default".
- **P2: no blog post** for the tool (404; none in the sitemap).
- **P2: video.**
  - Old UI; text mode never shown; "0 free uses remaining today" visible.
  - The macOS picker shows the "chaithra" folder, the "Anu ma'am" tag and personal files ("Q4_Report.pdf", "project mtect…xlsx").
  - About 30 s of end card.
- **P3 items:**
  - Limitations say locked PDFs can't be opened, but they unlock.
  - The selection counter is stale ("1 page selected" for "9" and for "2,2").
  - Meta description 82 chars.
  - VideoObject name mismatch.
  - Title/meta English in 9 locales; /ar 404.
  - iPhone SE 9 px, ja 3 px; axe label mismatch / region.

## Outcomes we want

1. At 0 trial uses the full text isn't available for free (count at Extract Text, or show only a short excerpt), matching the Oct 30 rule.
2. Every Download/Copy is counted the way Santosh decided, confirmed by the rerun.
3. Text mode extracts every page unless the user narrows it, or the copy says page 1 is preselected.
4. A blog post and a current video covering both modes, with no personal files visible and "trial uses" wording.
5. Accurate Limitations (locked files unlock in the page), a fuller meta description, translated title/meta.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS (downloads pending) | Typed order, odd/even, ranges, text with tabs and markers, scans, unlock. Output files pending the rerun. |
| 2 | Completeness vs competitors | PASS | Pages + text, thumbnails, odd/even, typed order. Could add "extract to separate files" (Split covers it). |
| 3 | Ease of use | PARTIAL | Clear steps and errors; the text default of page 1 surprises. |
| 4 | Layout attractiveness | PASS (minor) | iPhone SE 9 px, ja 3 px. |
| 5 | Payment process | PASS (stopped) | Cap dialog / Quick Buy day → "Day Pass, $1" email prompt; monthly → Stripe Checkout. Stopped. |
| 6 | Information correct | PARTIAL | "All pages by default" and "locked cannot be opened" are wrong. |
| 7 | Indexing | PASS | 200; canonical self; in sitemap. |
| 8 | SEO | PARTIAL | Meta 82 chars; FAQPage 13; VideoObject name mismatch; locales English title/meta; /ar 404. |
| 9 | Blog exists and accurate | **FAIL** | No post; /blog/extract-pdf 404. |
| 10 | YouTube video exists | PASS | XZ3ghDwxXf4 embedded. |
| 11 | FAQ and guide correct | PARTIAL | FAQs match; How-to default and Limitations lines are stale. |
| 12 | Video shows current capabilities | **FAIL** | Old UI; no text mode; personal files; at-0 strip. |
| 13 | Storage | PASS (untested save) | Nothing stored; Drive/cloud save need sign-in (untested). |
| 14 | Sharing | PASS | Share copies only the tool URL. |
| 15 | Downloads | PENDING | Download names/content pending the rerun (code: `-pages-<min>-<max>.pdf`, `-text.txt`). |
| 16 | Usage count | **FAIL (P1)** | Full text at 0 (Extract uncounted, manual copy works); per-page-load pending the rerun. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › PDF Tools. |
| 19 | AI need/demand | PASS (demand strong) | "extract pages from pdf", "pdf to text" are high-volume. An optional AI "summarise extracted text" could be a Premium Applications add-on. |
| 20 | Merge better? | No | Text mode is unique in C09; the Split difference is explained. |
| 21 | Remove? | No | |
| 22 | Duplicates | C09 overlap | Partial overlap with Split (one range) and Remove Pages (inverse); cross-link Remove Pages. |

## Severity summary
- **P0:** 0. Extraction and privacy hold.
- **P1:** 1 confirmed (full text at 0), 1 pending the rerun (per-page-load).
- **P2:** about 4 (text default, no blog, video, copy drift).
- **P3:** several.

## RERUN-AFTER-RESET
| Item | Script | Why pending |
|---|---|---|
| Per-page-load counting; download content (order, duplicates, bookmarks, forms, name, badge, .txt) | `ex-gate.js`, then `ex-live.js chromium V`, then `testfiles/verify.py` | All 22 fresh contexts after 03:06 EST loaded at 0. Row 40 was added to `/workspace/deep/RERUN-AFTER-RESET.md`. Report as FDP-40 -v2. |
