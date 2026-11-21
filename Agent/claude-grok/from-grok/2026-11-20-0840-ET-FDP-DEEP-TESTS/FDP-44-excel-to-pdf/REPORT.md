Sent: 2026-11-21 05:21 ET

# FDP-44 Excel to PDF (excel-to-pdf): deep test report for Claude

- **Written:** 2026-11-21 05:18 EST (box `date`, ET). Testing ran 2026-11-21 04:50–05:14 EST.
- **Tool:** https://www.freedailypro.com/tool/excel-to-pdf. Row 44 of TEST-ORDER.md: **Professional Tool** (Pro), PDF Tools, plan note "L-243 rank 1 (PDF Toolkit API live)". No duplicate group.
  - Video: uHlSx5_uZ6o. Blog: /blog/excel-to-pdf.
  - **GSC data is not available.**
- **Offer:** 10 trial uses a day, charged at Download (Convert and the first-page preview are open). $1 Day Pass / $4.99 monthly. Conversion runs in the browser.
- **Testers:**
  - **Desk review:** copy, FAQ (12), JSON-LD, locales, JS chunks (ExcelToPdf, excelPdf, ToolPage).
  - **Headless Playwright:** gate parts 1/2, 18 live cases (T01–T18) in Chromium, with Firefox and WebKit subsets. Every downloaded PDF was checked with poppler.
  - **Also:** a privacy network capture; the matrix (10 devices, 11 locales, 6 geo contexts, axe); the video, watched frame by frame.
- **Test files:** `scripts/make-files.py` (plus LibreOffice conversions):
  - formatted finance workbook with chart, picture and hidden sheet/column/rows; 30×300 wide sheet
  - mixed scripts; formulas without saved results; 50k rows
  - BOM/semicolon CSV, quoted CSV; empty, corrupt and renamed-text files
  - .xls, .ods, .docx, .xlsm, and a LibreOffice re-saved .xlsx
- **Constraints kept:** guest only; no sign-in, card or email; stopped at the Day Pass email prompt and the Stripe Checkout title; no ad clicks; no API/MCP calls; no site or repo changes.
- **Sign-in (untested):**
  - Save to Google Drive (Google sign-in popup), Save to my cloud storage ("Sign in with your email first"), Open from Google Drive.
  - Paid-pass behaviour (no ads, unlimited) is untested.
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:** Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps. Copy and results count as trial uses.

**Code to look at:**
- **ToolPage trial-use wrapper** (`vt` → `Sa`, export `d`) used by the gated Download (`D`): it charges once per tool per page load and then lets every later Download through without checking the limit. That holds even after the counter reaches 10/10 while the page is open.
- **`excelPdf-CkS3r6Jd.js`:**
  - The drawing scan counts `Ct(f,"c:chart")` / `Ct(f,"xdr:pic")` by literal prefix, so a default-namespace `<pic>` (openpyxl/pandas) isn't counted.
  - The .xls path reports no charts or pictures.
  - Devanagari goes to the FreeSans text path, not the picture path.
- **ExcelToPdf copy:** the FAQ answer on Chinese/Hindi/emoji; the .ods message template ("looks like a … file, not a spreadsheet").

**After you ship:** rerun `scripts/xp-gate.js 1` and `xp-live.js chromium` with a context that has uses left (expect +1 per Download of a new result, and a cap dialog once at 10/10), then work through test-cases.md.

## Intent

Someone with a spreadsheet wants a PDF table they can send that doesn't cut off text, doesn't leak hidden data, and looks like their workbook, without uploading it.

Conversion delivers that very well:
- formatting kept, hidden data left out by default
- warnings for formula cells that would print blank
- wide sheets split with the first column repeated
- 50k rows in 9 s
- clear rejects, and nothing uploaded

Two things undercut it:
- **One trial use buys a whole session:** 12 different workbooks for 1 use, and downloads keep working at 0.
- **Silent losses that contradict the copy:** Hindi printed incorrectly and emoji as boxes under a "looks right" warning; pictures that vanish without the promised note.

## Why: what the evidence says

- **P1, per-page-load charging and the gate bypassed while the page stays open.**
  - gate-1: Download 0→1, then the same file, X02 and X07 in the same load stay at 1; after a reload X06 → 2.
  - cases-chromium: 12 distinct PDFs from 12 workbooks in one load for 1 trial use.
  - After the counter synced to 10/10 mid-session, T14 (.xls) and T17 (.xlsm) still downloaded with no cap dialog. Counters are display-only evidence; the downloads are real files (`outputs/`).
- **P2 items:**
  - **Hindi and emoji:** Hindi shaped wrongly ("नमस्ते" → "नमस् ते") and 🚀 drawn as a box, while the warning says these are drawn as pictures "so they look right". The FAQ separately says they'd appear as "?" (three different stories).
  - **Pictures not noted:** in openpyxl/pandas-written .xlsx, and chart and picture both dropped silently for .xls, despite "a note tells you how many charts or pictures were left out".
  - **Blog:** tells readers to "scroll the whole preview, including the last page"; the tool shows only a first-page preview.
  - **.ods reject message:** "looks like a OpenDocument spreadsheet file, not a spreadsheet".
  - **Video:** old UI, a personal macOS Downloads folder, "Free … no account" wording.
- **P3 items:**
  - **Overflow:** iPhone SE 9 px, /ja 3 px.
  - **axe:** label-content-name-mismatch, plus ad-caption contrast (keep the reserved slots).
  - **Locales:** titles and meta in English; meta description 86 chars; generic OG image.
  - **Copy:** "EXCEL" in caps on the File Conversion Studio link.

## Outcomes we want

1. Each Download of a **new result** takes one trial use, and at 0 the cap dialog appears even if the page was opened earlier with uses left. Re-downloading the same result stays free.
2. Script handling and copy agree. Either draw Devanagari (and all emoji) as pictures like the other scripts, or warn accurately. One FAQ answer that matches.
3. The pictures/charts note counts every drawing (namespace-aware) and covers .xls, or the copy stops promising it.
4. The blog matches the first-page preview; the .ods message reads correctly; a new video is recorded on a clean profile.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | xlsx/xlsm/xls/csv; formatting, hidden data, wide sheets, blank-formula warning, 50k rows. Hindi/emoji rendering is a P2. |
| 2 | Completeness vs competitors | PASS (strong) | Compared with iLovePDF, Smallpdf and Adobe online: no upload, hidden-data control, cut-off prevention and first-column repeat beat them. Missing: charts and pictures, print areas. |
| 3 | Ease of use | PASS | One drop, sensible defaults (Letter for en-US), clear notes and rejects. |
| 4 | Layout attractiveness | PASS (minor) | Clean card; iPhone SE 9 px overflow. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass email prompt (stopped); Quick Buy → Stripe Checkout (stopped). |
| 6 | Information correct | PARTIAL | Script copy conflict (pictures vs "?" vs actual); picture-note promise; .ods message. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Strong title, FAQ/Offer/Video JSON-LD; meta 86 chars; generic OG image; locale titles English. |
| 9 | Blog exists and accurate | PARTIAL | /blog/excel-to-pdf is accurate except the "scroll the whole preview" advice. |
| 10 | YouTube video exists | PASS | uHlSx5_uZ6o, embedded. |
| 11 | FAQ and guide correct | PARTIAL | See check 6. |
| 12 | Video shows current capabilities | **FAIL** | Old UI, personal macOS Downloads, "Free … no account". |
| 13 | Storage | PASS (N/A) | Nothing stored; options carry over within the session; cloud save is sign-in (untested). |
| 14 | Sharing | PASS | Share this tool. Drive save is sign-in (untested). |
| 15 | Downloads | PASS | Correct PDFs, selectable text, embedded fonts, badge on every page; same-file re-download is free. |
| 16 | Usage count | **FAIL (P1)** | Per page load: 12 workbooks for 1 use; downloads continue after 10/10. |
| 17 | Categorization in section | PASS | PDF Tools / Professional Tools. |
| 18 | Correct section of site | PASS | PDF Tools breadcrumb and category. |
| 19 | AI need/demand | PASS | High demand. A chat assistant can't hand back a paginated, formatted PDF of a private workbook without an upload. |
| 20 | Merge better? | No | It's the entry point; it already cross-links Universal File Converter and File Conversion Studio. |
| 21 | Remove? | No | L-243 rank 1, the PDF Toolkit lead. |
| 22 | Duplicates | None | No duplicate group. PDF to Excel is the reverse tool (linked). |
