Sent: 2026-11-20 08:40 ET

# FDP-23 PDF to Word (pdf-to-word): deep test report for Claude

- **Written:** 2026-11-19 18:09:36 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/pdf-to-word. Row 23 of TEST-ORDER.md: Pro, PDF Tools, grouped with test-plan rank 19 (Universal File Converter / PDF to Word / Word to PDF). **GSC data is not available.**
- **Classification:** Professional Tool (10 trial uses a day, $1 Day Pass / $4.99 month), PDF Tools (+ professional-tools). Gated at Download: converting and the preview are free; Download costs 1 trial use.
- **Testers:**
  - **Desk review:** page (expanded), JSON-LD, /es, /ar, /blog/pdf-to-word, category; `PdfToWord`, `pdfLayout`, `ocrBlocks` code.
  - **YouTube video:** metadata + 36 frames.
  - **Headless Playwright:** 20 PDF cases (text, scans/OCR, wrong OCR language, page ranges, 500 pages, two columns, tables, form, rotated, non-Latin, password, owner-restricted, damaged/empty/renamed), outputs inspected with python-docx and the raw XML against pdftotext; gate and dialogs, Stop, keyboard, axe, phones, Firefox + WebKit, matrix (10 profiles, 10 locales + /ar, 6 geos, axe).
- **Starting counts:** contexts load either at 10/10 used (0 remaining, e.g. 17:58:30 EST) or with 10 remaining (e.g. 18:01:30 EST), roughly half each. Counters are display-only evidence.
- **Trial use observed:** with uses left, Convert cost nothing (0 → 0); the 1st Download cost 1 (0 → 1); a 2nd Download of the same result was free; "Convert another" with the same file and Download again was also free (1 → 1). Downloaded rich.docx (`dl-1-rich.docx`) = the in-memory .docx byte for byte; no mark on Word output. Download-gated, consistent with other tools — not flagged.
- **Constraints kept:** guest only, no sign-in, nothing typed into email/card prompts (only our own test PDF's password "user123" into the unlock dialog), no ad clicks, no API/MCP, no site/repo changes. Outputs parsed, never executed.
- **Sign-in:** Save to my cloud storage → "Sign in" dialog (Not now); Save to Google Drive at 0 shows the cap dialog first (with uses it was not clicked, so the Drive sign-in is untested); Open from Google Drive not clicked. See INSTRUCTIONS.md.
- **Pending:** none. No RERUN-AFTER-RESET row needed.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships PDF tools.

Code to look at:
- `evidence/js/pdfLayout-BswErtWz.pretty.js` L73–94: a number marker ("1.") is detected (`kind: "number"`) and removed from the line (`segs.shift()`), but L553–562 only turns **bullet** markers into list formatting — so the number is lost.
- `pdfLayout` table column split (the "9.99 02134" merge) — the same engine feeds Universal File Converter's PDF → Excel.
- `evidence/js/PdfToWord-BRvpB3Rt.pretty.js`: OCR worker start L240–255; convert handler L565–615; summary/warnings L620–630 and L340–365; Download L700–705; `gateAtDownload` L835; copy L508–510. FAQ text lives with the tool info (see `html/tool-expanded.txt` L94–113).

After you ship, rerun `scripts/pw-battery.js` (all), `scripts/pw-gate.js`, `scripts/pw-dl.js`, `scripts/pw-webkit-ocr.js`, then `test-cases.md` (PW-01…PW-24).

## Intent

Someone has a PDF they must change — a contract template, an old report, a scanned letter — and needs a Word file they can edit right now without retyping it. They need every word, number and clause label to come across, with the structure intact, so they don't have to proofread line by line. They need to trust that the file stays on their device. They should leave impressed and see the Pro pass as worth it.

The engine is strong: about half a second for text PDFs (500 pages in ~1 s), true fonts, sizes, bold and italic, real bullet lists, a real Word table for a ruled table, pictures in place, two-column text in the right order, per-page sizes (a rotated landscape page stays landscape), running headers turned into Word header fields (PAGE / NUMPAGES), filled form values written out, mixed text/scan handling, a working Stop, a clear password dialog, a helpful damaged-file message with Repair PDF, OCR that reads a clean scan well, and nothing uploaded (only analytics requests; OCR data from cdn.jsdelivr.net).

Trust is lost where numbered lists silently lose their numbers, where tables built from text columns put two numbers in one cell, and in a video that sells the tool as free.

## Why: what the evidence says

- **P1: numbered lists lose their numbers.** "1. Step one / 2. Step two / 3. Step three" in the PDF becomes "Step one / Step two / Step three" in Word — no number as text and no Word numbering (numbering.xml has only bullet formats). The page says "Numbered lists keep their numbers as typed text." Contract clauses, steps and legal numbering would vanish silently. (`testfiles/outputs/out-P01.docx`, token diff in `findings/live-functional-findings.md`)
- **P1: the video sells the tool as free.** Title "How to Use PDF to Word – Free Step-by-Step Walkthrough", description "Try PDF to Word free… Free daily uses", on screen "10 free uses daily" and a "0 free uses remaining today" banner the whole time; older UI (Share button, no language/pages options); never opens the Word file. 109 s, 6 views.
- **P1 (verify on real Safari): WebKit tab crash on OCR.** Converting our 2-page 150-dpi scan crashed the page in Playwright WebKit 3 of 3 times (Chromium and Firefox fine; a 4-page grey scan worked in WebKit). If it reproduces on iPhone/Mac Safari, scanned PDFs can't be converted there.
- **P2:** table built from text columns puts Price and ZIP in one cell ("9.99 02134") and leaves the ZIP column empty, although the page says "numbers stay in their own columns"; FAQ says English and Hindi are "automatically recognized, no need to specify" while another FAQ and the UI say pick the language (wrong language gives garbage, as we saw); headings come out as bold 14 pt text, not Word Heading styles; axe: label-content-name mismatch, preview contrast and a non-focusable scrolling preview.
- **P3:** no /blog/pdf-to-word (404); locale titles in English, /ar 404; iPhone SE 9 px overflow (site-wide header); "Unlocked" toast for an owner-restricted PDF without saying restrictions are dropped; OCR data comes from a third-party CDN.

## Outcomes we want

1. Every list number, clause label and step number in the PDF is present in the Word file (as text or as real Word numbering).
2. Values that sit in separate columns of the PDF land in separate Word table cells.
3. The video shows today's Pro tool with trial-use wording and ends with the Word file open.
4. Scanned PDFs convert on Safari (Mac and iPhone) without the tab crashing.
5. One true sentence about OCR language choice; headings usable in Word's navigation pane.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | 17/20 cases faithful; numbered-list numbers lost; text-column table merge; WebKit OCR crash. `findings/live-functional-findings.md` |
| 2 | Completeness | **PASS** | LOW | Language, page range, Stop, password, damaged-file help all present. Heading styles missing. |
| 3 | Ease of use | **PASS** | LOW | 4-step guide, clear summary line, preview, helpful errors. |
| 4 | Layout | **PASS** | LOW | Clean on 10 profiles; 9 px header overflow at 320 px (site-wide); Download at y≈746 on iPhone SE. |
| 5 | Payment process | **PASS** | — | At 0: Download Word File → "Today's trial uses are done" ($4.99 / $1) → Buy Day Pass $1 → email prompt (stopped; nothing typed). Result kept after Escape. `json/dl-gate.json` |
| 6 | Information correct | **FAIL** | HIGH | "Numbered lists keep their numbers"; "numbers stay in their own columns"; contradictory OCR-language FAQs. `findings/desk-findings.md` |
| 7 | Indexing | **PASS** | — | 200, self-canonical, not noindex. GSC data is not available. |
| 8 | SEO | **PARTIAL** | LOW | Strong title/meta; locale titles English; /ar 404. |
| 9 | Blog | **PARTIAL** | LOW | /blog/pdf-to-word 404; Guides link 2 related posts; 9 posts link here (tools.csv). A dedicated post under another slug is an unverified absence. |
| 10 | YouTube video | **PASS (low reach)** | LOW | K61zcnXg6sU embedded; 109 s, 6 views (Sep 23, 2026). |
| 11 | FAQ / guide | **PARTIAL** | MEDIUM | 10 FAQs + Details, honest about reflow; two wrong/contradictory answers. |
| 12 | Video shows current tool | **FAIL** | MEDIUM | "Free" title/description, "10 free uses daily", 0-uses banner, old UI. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Save to my cloud storage → sign-in dialog; Save to Google Drive gated at 0 (Drive sign-in untested); Open from Google Drive not clicked. |
| 14 | Sharing | **N/A** | — | No share/copy on the result (live-verified) although tools.csv lists them and the video shows a Share button. |
| 15 | Downloads | **PASS** | — | rich.docx (`dl-1-rich.docx`), bytes = in-memory .docx; no mark. |
| 16 | Usage count | **PASS** | — | Convert free; 1st Download 0 → 1; repeat Download and same-file re-convert free. Counter display-only evidence. |
| 17 | Category placement | **PASS** | — | PDF Tools; professional-tools. |
| 18 | Site section | **PASS** | — | Professional Tools. |
| 19 | AI need / demand | **PASS** | — | Grouped with rank 19; 9 posts link here. GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | Universal File Converter's PDF → Word is plain paragraphs only; this tool is the rich version. Cross-link both ways. |
| 21 | Remove? | **N/A (keep)** | — | Core Professional Tool. |
| 22 | Duplicates | **PASS** | — | Distinct from OCR PDF (explained in FAQ) and Image to Word. |
