Sent: 2026-11-21 03:55 ET

# FDP-41 OCR PDF (ocr-pdf): deep test report for Claude

- **Written:** 2026-11-21 03:52 EST (box `date`, ET). Testing ran 2026-11-21 03:27–03:50 EST.
- **Tool:** https://www.freedailypro.com/tool/ocr-pdf. Row 41 of TEST-ORDER.md: Pro, PDF Tools. Plan note "L-243 rank 1 (PDF Toolkit API live)".
  - Duplicate group C06 (ocr-tool, scan-to-document, image-to-word, image-to-excel, document-scanner, camera-capture).
  - Video: djmvThBol8c. No dedicated blog post.
  - **GSC data is not available.**
- **Classification:** Professional Tool. OCR (tesseract.js v7) runs in the browser. The engine and language data come from jsDelivr, and nothing from the file is sent (`evidence/json/privacy.json`).
- **Testers:**
  - **Desk review:** copy, 12 FAQs, JSON-LD, 10 locales + /ar, JS chunks.
  - **Headless Playwright:**
    - a probe; a gate run with one fresh context that had 10 uses left (03:31 EST) plus an at-0 run
    - 15 V and 11 W download cases in uses-left contexts, every file checked by `verify.py` against ground truth
    - 11 K edge cases in Chromium and Firefox
    - a WebKit OCR check, a privacy check and the Compress hand-off at 0
    - the 10-device / 11-locale / 6-geo / axe matrix
- **Test files:** `scripts/make-scans.py` builds 13 image-only "scans" with known text (`truth.json`): clean English; scan/text/scan; sideways; upside-down; a stamped footer; Spanish; German; English+Hindi; blank; 72 dpi noisy; 12 pages; a table; AES-256 locked. Also P02/P06/P07/U01.
- **Starting counts (display-only):** the gate, V and W runs tried 13 fresh contexts. Three loaded with 10 uses left (03:31, 03:36 and 03:41 EST) and were rechecked 6 s later; the rest loaded at 0.
- **Constraints kept:**
  - Guest only and no sign-in. No email or card typed: stopped at the Day Pass email prompt and at Stripe Checkout (session id redacted).
  - No ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):**
  - Save to Google Drive opened the Google sign-in popup, which I closed.
  - Save to my cloud storage opened "Sign in with your email first", which I closed.
  - Open from Google Drive was not clicked.
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row. One open device check remains: OCR on a real iPhone/Mac Safari (see WebKit below).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

**Owner context:**
- On Nov 20 Santosh decided that every Download on Barcode Generator and Invoice Generator uses a trial use. Charging only the first Download per page load conflicts with that, and per-page-load charging is a P1 gate gap.
- Full-quality results at 0 trial uses are also P1 gaps. Here they are **not** present: at 0 the user only gets a 489×633 preview of the original scan, and every route to the searchable PDF is gated.

**Code to look at:**
- **Shared per-page-load set `Kt`** (`evidence/js/index-B1CTyGtY.excerpt-usage.js`) behind the shared Download (`ToolPage` export `D`). Same root cause as #35–40; one fix covers them all.
- **`OcrPdf-BJ90unSe.pretty.js`:** the New handler and the file loader `_` reset the file, result and messages, but **not** orientation (`N`/`L`) or language (`C`/`I`). Reset both on New and on a new file, or show the carried-over choice prominently.
- **`operations-B4LtHhm8.js` `Wn` (ocrPdf):**
  - Auto-rotate tries 90 → 270 → 180 and accepts the first reading with confidence ≥75, so an upside-down page can be "fixed" sideways. Score all three, or prefer 180 when it wins.
  - Any page with ≥3 text characters is skipped, so stamped scans get no OCR.
  - Devanagari goes through a font subset that loses reph/half forms.
- **`ocrEngine-C8AaB6dN.js`:** the progress callback is bound to page 1.

**After you ship:** rerun `scripts/ocr-gate.js 12`, then `ocr-live.js chromium V` and `W`, then `testfiles/verify.py live/downloads`, then test-cases.md (OC-01…OC-32).

## Intent

Someone has a scanned contract, statement or archive PDF and needs to find a name with Ctrl+F, copy a paragraph, or feed it to PDF to Excel. They want:
- the PDF to look exactly the same
- every page readable in their language
- the file never uploaded

The engine delivers:
- **100% word recall** on clean English, Spanish and German scans, a 12-page file in 7–10 s, real-text pages left untouched, and correct turning of sideways pages.
- Clear messages for already-searchable, unreadable, damaged and locked files, and a working Stop.
- Nothing leaves the tab except engine downloads from jsDelivr.

Revenue and trust break in five places:
- **Gate:** one trial use buys unlimited downloads for the rest of the page load (14 documents for 1 use).
- **Orientation memory:** after New, the next upright file is silently turned sideways while the notice says it now "reads upright".
- **Auto-detect:** upside-down pages come out sideways.
- **Coverage:** scans with stamped footers are skipped, table numbers are dropped, and Hindi loses letters.
- **Copy and discovery:** the FAQ says English only, the tips say pages aren't turned, there's no blog post, and the video predates the orientation menu and never shows search working.

## Why: what the evidence says

- **P1 gate gap: per-page-load charging** (`gate-12.json` 03:31–03:33 EST; `cases-chromium-V.json` 03:36–03:39 EST; `cases-chromium-W.json` 03:41–03:43 EST).
  - The first Download cost 1 use. The same file again, a new 3-page file, and then 12 more documents including a 12-page scan were all free in that load.
  - After a reload the next Download cost 1 (1 → 2) and the one after was free (2 → 2).
  - Page loads, file drops, Make Searchable and Preview never count.
- **P1 functional: the orientation and language choices carry over to the next file** (V05–V11).
  - After V04 used "Turn 90° clockwise", New + an upright Spanish/German/Hindi/table/12-page file produced **sideways output** (`/Rotate 90`, swapped page size), each with "Page 1 was turned 90° clockwise so it reads upright".
  - That contradicts "pixel-identical" and the notice itself. Render: `evidence/screens/cases/output-orientation-V03-V05-V12.png`.
- **P2: auto-detect turns an upside-down page sideways** (V12: `/Rotate 270`, "turned 270° clockwise so it reads upright"). "Turn 180° first" works (W09).
- **P2: scans with a small digital footer are skipped as "already searchable"** (S04, K08 in Chromium and Firefox).
- **P2: tables lose their numbers.** The monospace price table recalled 38%, and the QTY/PRICE columns are missing. The page's own next step is PDF to Excel.
- **P2: the Hindi text layer drops reph/half forms** ("मार्च" → "माच", "शर्मा" → "शम"; 77% recall with English + Hindi).
- **P2 (unverified on a device): Playwright WebKit crashes on Make Searchable** (desktop and iPhone emulation). Loading works. Confirm on a real iPhone/Mac Safari; if it's real, Safari users can't use the tool.
- **P2 copy:**
  - The FAQ says only English is supported (8 languages work).
  - The tips say sideways/upside-down pages aren't turned (they are).
- **P2: no blog post** (four slugs 404).
- **P2: video** predates the orientation menu, says "200+ tools" (live: 300+), and never opens the result to show search/select working.
- **P3 items:**
  - The blank-scan message talks about orientation.
  - The progress % is labelled "page 1" on later pages.
  - Duplicate "looks the same" FAQs; generic OG image; JSON-LD only in the rendered DOM.
  - Title/meta English in 10 locales; /ar 404; iPhone SE 9 px and ja 3 px overflow; axe label mismatch / region / ad-caption contrast.

## Outcomes we want

1. Every Download of a searchable PDF uses a trial use, per Santosh's Nov 20 decision, not once per page load.
2. A new file always starts at "As scanned" and the page's language, or the carried-over choice is shown. Output orientation never changes unless the user or a correct auto-detect asked for it.
3. Upside-down pages come out upright with "Detect automatically".
4. Image-dominant pages with a small text stamp still get OCR, or the user is told and offered "OCR anyway".
5. Table digits and Hindi words survive into the text layer, so Ctrl+F and PDF to Excel work.
6. The FAQ and tips match the 8 languages and the orientation menu. A blog post and an updated video show search working in the result.
7. OCR works on real Safari (iPhone and Mac), or Safari users are told before they start.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PARTIAL | 100% recall on clean EN/ES/DE, multi-page, mixed, locked files. Sticky orientation, the upside-down auto bug, stamped-footer skip, table digits and Hindi forms fail. |
| 2 | Completeness vs competitors | PARTIAL | Has 8 languages, auto-rotate, Stop, unlock. Missing vs Acrobat/iLovePDF/Smallpdf: force-OCR pages that have some text, deskew, batch of several files. |
| 3 | Ease of use | PARTIAL | One button, clear messages; settings silently carry over after New. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px, ja 3 px overflow. |
| 5 | Payment process | PASS (stopped) | Cap dialog → "Buy Day Pass — $1" → email prompt; Quick Buy monthly → Stripe Checkout. Stopped. |
| 6 | Information correct | PARTIAL | "English is currently supported" and "not turned for you" are wrong. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PARTIAL | Good title/meta (114); FAQPage 12, VideoObject, Breadcrumb only in the rendered DOM; generic OG image; locale title/meta English; /ar 404. |
| 9 | Blog exists and accurate | **FAIL** | No post; /blog/ocr-pdf and three other slugs return 404. Two related posts are linked. |
| 10 | YouTube video exists | PASS | djmvThBol8c, embedded. |
| 11 | FAQ and guide correct | PARTIAL | Languages FAQ and orientation tip are stale; duplicate FAQ. |
| 12 | Video shows current capabilities | PARTIAL | No orientation menu; "200+"; never shows search in the output. No personal data. |
| 13 | Storage | PASS (save untested) | Nothing stored. Drive/cloud saving needs sign-in (untested). |
| 14 | Sharing | PASS | Share this tool only; Continue with Compress PDF hands the result over and stays gated. |
| 15 | Downloads | PARTIAL | `searchable_<name>.pdf`, badge added, page visuals identical (diff 0.0), real-text pages untouched, a password-free copy of locked files. Sideways output after the carry-over / auto bugs. |
| 16 | Usage count | **FAIL (P1)** | Once per page load (14 documents for 1 use). Make Searchable is uncounted but the PDF is gated at 0. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › PDF Tools. |
| 19 | AI need/demand | PASS (strong) | "ocr pdf" and "make pdf searchable" are steady high-intent queries; core for legal, bookkeeping and archives. |
| 20 | Merge better? | No | Only C06 tool that keeps the same PDF; differences are explained on the page. |
| 21 | Remove? | No | |
| 22 | Duplicates | C06 overlap | Overlaps the "searchable" option of document-scanner and PDF to Word's OCR; keep and cross-link. |

## Severity summary
- **P0:** 0. OCR is accurate on clean scans and privacy holds.
- **P1:** 2 (per-page-load charging; orientation/language carry-over producing sideways output).
- **P2:** about 8 (auto upside-down, stamped footer skip, table digits, Hindi forms, WebKit crash (unverified), copy, blog, video).
- **P3:** several.

## Open item (not reset-dependent)
| Item | How | Why |
|---|---|---|
| OCR on real Safari (iPhone + Mac) | Drop `S01_scan_clean_en.pdf` and press Make Searchable | Playwright WebKit on Linux crashed every time (`webkit.json`); that build isn't Safari. |
