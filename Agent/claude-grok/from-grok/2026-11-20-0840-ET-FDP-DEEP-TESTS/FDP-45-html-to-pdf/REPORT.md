Sent: 2026-11-21 06:06 ET

# FDP-45 HTML to PDF (html-to-pdf): deep test report for Claude

- **Written:** 2026-11-21 06:03 EST (box `date`, ET). Testing ran 2026-11-21 05:20–06:01 EST.
- **Tool:** https://www.freedailypro.com/tool/html-to-pdf. Row 45 of TEST-ORDER.md: **Professional Tool** (Pro), PDF Tools, plan note "L-243 rank 1 (PDF Toolkit API live)". No duplicate group.
  - Video: JqeVfUR3J-g. Blog: /blog/html-to-pdf.
  - **GSC data is not available.**
- **Offer:** 10 trial uses a day, charged at Download (Convert and the first-page preview are open). $1 Day Pass / $4.99 monthly.
  - HTML is rendered in a script-blocking iframe and captured page by page (image plus invisible text layer), all in the browser.
- **Testers:**
  - **Desk review:** copy, FAQ (13), JSON-LD, locales, JS chunk HtmlToPdf.
  - **Headless Playwright:**
    - gate at 0 (zero.json)
    - 17 cases in one page load with uses left (left.json); the same cases at 0 (left-at0-run1.json)
    - on-page preview captures at 0
    - Firefox/WebKit subsets, plus a WebKit hang/Stop check (hp-webkit.js)
  - **Checks:** every downloaded PDF checked with poppler/pikepdf; a privacy request scan; the matrix (10 devices, 11 locales, 6 geo contexts, axe); the video, frame by frame.
- **Test files** (`scripts/make-files.py`):
  - invoice (style block, data-URL logo, external image, links)
  - page breaks; script/onerror/noscript/form; meta refresh
  - mixed scripts; 2400 px wide table; 9,000 paragraphs; windows-1252 file; .htm résumé
  - .txt; tall image; relative paths; Google Fonts
- **Constraints kept:** guest only; no sign-in, card or email; stopped at the Day Pass email prompt and the Stripe Checkout title; no ad clicks; no API/MCP calls; no site or repo changes.
- **Sign-in (untested):** Save to Google Drive (Google sign-in popup), Save to my cloud storage ("Sign in with your email first"), Open from Google Drive. Paid-pass behaviour (no badge, unlimited) is untested.
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:** Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps. Copy and results count as trial uses.

**Code to look at:**
- **ToolPage trial-use wrapper** (`vt` → `Sa`) behind the gated Download (`D`): it charges once per tool per page load. This is the same root cause as FDP-44, so one fix covers both.
- **`HtmlToPdf-DMdSWHCi.js`:**
  - `He` (html-to-image `toPng`, `cacheBust: !0`) has no timeout; in WebKit it never resolves when the frame holds a cross-origin image.
  - Stop (`B.current`) is only checked between pages, so it can't interrupt that capture.
  - `te(t => t === "document" ? title : t)`: the file name only updates while it is still "document", so it sticks to the first title or dropped file name.
  - `ze()`: break positions; a break at the first element's top (> 0 because of body margin) creates an empty first page.
  - `a[href]` uses the resolved `t.href`, so `#top` and `/path` point at freedailypro.com, because srcdoc inherits the parent URL. Add a `<base>` or skip non-absolute hrefs.
  - `FileReader.readAsText(h)`: reads as UTF-8 regardless of the file's `<meta charset>`.

**After you ship:** rerun `scripts/hp-live.js left` with a context that has uses left (expect +1 per new result; the file names follow each document) and `hp-live.js zero`, then work through test-cases.md.

## Intent

Someone with HTML (an invoice template, a saved report, a hand-coded résumé) wants a clean PDF with the page size and margins they choose, with clickable links and searchable text, without uploading anything or running untrusted scripts.

The core delivers that well:
- crisp output (about 190 dpi), rows kept whole, forced breaks honoured
- scripts, onerror handlers and meta refresh neutralised
- webfonts and data-URL images work; a 200-page limit with a clear message
- nothing uploaded

What undercuts it:
- **One trial use per page load:** 16 downloads for 1 use.
- **Safari-engine hang:** an external image makes WebKit spin forever, and Stop doesn't help.
- **Small correctness slips in exactly the documents people send:** wrong file names after the first document, a blank first page with page-break CSS, `#anchor` links that open FreeDailyPro, and mangled accents from non-UTF-8 files.

## Why: what the evidence says

- **P1, per-page-load charging (gate gap).**
  - left.json: L01 0→1, then 15 more downloads of 13 different documents in the same page load stay at 1.
  - After a reload: +1 (2). Counters are display-only evidence; the files are real (`outputs/`).
- **P1, WebKit hang on external images (core flow broken on the Safari engine).**
  - hang-webkit.json: H02 (one external Wikimedia image) stays at "Rendering page 1 of 3" for 120 s and, in the subset run, 305 s.
  - **Stop doesn't recover:** after Stop it was still "Rendering page 1 of 3" with no Convert button.
  - H02b (same file, external image removed) converts in 5.9 s; H10/H14 convert. Chromium and Firefox finish H02 in about 2 s.
  - Hosted logos in invoice and email templates are the common case. Headless WebKit on Linux, so confirm on real Safari/iOS.
- **P2 items:**
  - **File name sticks:** after an invoice, five unrelated documents downloaded as "Invoice INV-2026-045.pdf"; after a dropped résumé, five more as "H10_resume.pdf".
  - **Blank first page:** when the first element has `page-break-before: always` (a common pattern for chapter templates).
  - **In-document and relative links** become links to freedailypro.com (`#top` → `/tool/html-to-pdf#top`).
  - **windows-1252 .html files are misread** ("Caf� cr�me"), and the damaged words drop out of the text layer.
  - **Lookalike ad:** in the Firefox run, an ad styled "Start Download (Free) / Add Extension to Firefox" sat directly under Convert to PDF, where the real Download button appears (S08-firefox.png). Keep the slot; block that creative category.
  - **Video:** old UI, "10 free uses daily", a personal Chrome downloads list and extension badge, and a sample that says "not a screenshot".
- **P3 items:**
  - **FAQ:** duplicate questions (URL ×2, JavaScript ×2).
  - **Page copy:** meta description 70 chars; generic OG image; English locale titles.
  - **Layout:** table headers don't repeat; very wide tables shrink to unreadable size with no warning.
  - **Overflow:** iPhone SE 9 px, /ja 3 px; the Margin label/aria-label mismatch.

## Outcomes we want

1. Safari/WebKit finishes every conversion. A blocked or slow image becomes the promised blank, capture has a timeout, and Stop always returns control.
2. Each Download of a **new result** takes one trial use; re-downloading the same result stays free; at 10/10 the cap dialog shows regardless of when the page was opened.
3. The download name follows the current document (its title, or the dropped file name) every time.
4. No empty first page from a leading forced break; in-document and relative links aren't turned into FreeDailyPro links.
5. Dropped files honour their declared charset (or warn when they aren't UTF-8).
6. A new video recorded on a clean profile; FAQ duplicates merged; a fuller meta description.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PARTIAL | Paste/drop, A4/Letter/Legal, landscape, margins, page numbers, breaks, links, text layer, 200-page guard. **WebKit hangs on external images (P1).** |
| 2 | Completeness vs competitors | PASS | Compared with Sejda, PDFCrowd and iLovePDF HTML: no upload and no script execution are differentiators. Missing: URL fetch (by design, explained), repeating table headers, real vector text. |
| 3 | Ease of use | PASS | Sample preloaded; clear messages; Edit to iterate. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px overflow. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass email (stopped); Quick Buy → Stripe Checkout (stopped). |
| 6 | Information correct | PARTIAL | The "file name" promise; undocumented relative-link and charset behaviour; FAQ duplicates. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Good title and JSON-LD; meta 70 chars; generic OG image; English locale titles. |
| 9 | Blog exists and accurate | PASS | /blog/html-to-pdf is accurate and practical (file-name line aside). |
| 10 | YouTube video exists | PASS | JqeVfUR3J-g, embedded. |
| 11 | FAQ and guide correct | PARTIAL | Accurate but duplicated; the 200-page limit sits inside a JavaScript answer. |
| 12 | Video shows current capabilities | **FAIL** | Old UI, "free uses", personal downloads list. |
| 13 | Storage | PASS (N/A) | Nothing stored; cloud save is sign-in (untested). |
| 14 | Sharing | PASS | Share this tool; Drive save is sign-in (untested). |
| 15 | Downloads | PARTIAL | WebKit never reaches Download with an external image. Correct PDFs otherwise, but the file name sticks to the first document; blank first page with a leading break. |
| 16 | Usage count | **FAIL (P1)** | Per page load: 16 downloads for 1 trial use. |
| 17 | Categorization in section | PASS | PDF Tools / Professional Tools. |
| 18 | Correct section of site | PASS | PDF Tools breadcrumb and category. |
| 19 | AI need/demand | PASS | Steady demand (invoice and report templates). Chat assistants produce HTML but can't hand back a paginated PDF. |
| 20 | Merge better? | No | Distinct input (markup); cross-links to Universal File Converter / File Conversion Studio exist. |
| 21 | Remove? | No | L-243 rank 1, PDF Toolkit. |
| 22 | Duplicates | None | No duplicate group. |
