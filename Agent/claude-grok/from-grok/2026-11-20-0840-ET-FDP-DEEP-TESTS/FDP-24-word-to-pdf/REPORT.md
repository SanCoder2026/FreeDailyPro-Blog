Sent: 2026-11-20 08:40 ET

# FDP-24 Word to PDF (word-to-pdf): deep test report for Claude

- **Written:** 2026-11-19 18:21:43 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/word-to-pdf. Row 24 of TEST-ORDER.md: Pro, PDF Tools, grouped with test-plan rank 19 (Universal File Converter / PDF to Word / Word to PDF). **GSC data is not available.**
- **Classification:** Professional Tool (10 trial uses a day, $1 Day Pass / $4.99 month), PDF Tools. Gated at Download: converting and the preview are free; Download costs 1 trial use; trial PDFs carry the intentional "Created with FreeDailyPro.com" badge.
- **Testers:**
  - **Desk review:** page (expanded), JSON-LD, /es, /ar, /blog/word-to-pdf, category; `WordToPdf`, `docxToPdf`, `docxRead`, `docxRaster`, `textToPdf` code.
  - **YouTube video:** metadata + 25 frames.
  - **Headless Playwright:** 17 cases (rich .docx in all 3 modes and 2 paper sizes, .txt, 200-page doc in Keep formatting and Exact look, two-column doc, Word complex vs simple page fields, .doc/.rtf/.odt, broken/renamed/empty .docx); PDFs inspected with pdfinfo/pdffonts/pdftotext/pypdf and rendered, compared with a LibreOffice reference; gate and dialogs, keyboard, axe, phones, Firefox + WebKit, matrix (10 profiles, 10 locales + /ar, 6 geos, axe).
- **Starting counts:** most contexts load at 10/10 used (0 remaining, e.g. 18:12:36 EST); about 1 in 4–10 load with 10 remaining (18:14:36, 18:16:56 EST). Counters are display-only evidence.
- **Trial use observed:** with uses left (18:16:56 EST) Convert cost nothing; the 1st Download cost 1 (0 → 1); a 2nd Download and a same-file re-convert + Download were free (1 → 1). Downloaded rich.pdf (`dl-1-rich.pdf`, 301,488 B) = the in-memory PDF (298,545 B) + the badge on all 4 pages. Download-gated, consistent with other tools — not flagged.
- **Constraints kept:** guest only, no sign-in, nothing typed into email/card prompts, no ad clicks, no API/MCP, no site/repo changes. Outputs parsed, never executed.
- **Sign-in:** Save to my cloud storage → "Sign in" dialog (Not now); Save to Google Drive at 0 shows the cap dialog (with uses not clicked — Drive sign-in untested); Open from Google Drive not clicked. See INSTRUCTIONS.md.
- **Pending:** none. No RERUN-AFTER-RESET row needed. Not tested: password-protected .docx (no test file).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships PDF tools.

Code to look at:
- `evidence/js/docxToPdf-K5O8yYaD.pretty.js` — Keep formatting / Text only: how non-WinAnsi text is drawn. Devanagari is written with the `FreeSans-devanagari-subset.ttf` font as real glyphs, without shaping (conjuncts dropped), not "as pictures" as the page and the pre-convert note say.
- `evidence/js/docxRaster-Bk1M3JAm.pretty.js` — Exact look (DOM capture): Symbol-font bullets (U+F0B7) and `w:fldSimple` PAGE/NUMPAGES.
- `evidence/js/WordToPdf-CtM3tuGx.pretty.js` L100–160 (file intake: .doc/.rtf/.odt messages that the picker's accept list pre-empts), L159–230 (convert), L300–335 (mode warnings), L500 `gateAtDownload`.

After you ship, rerun `scripts/wp-battery.js` (all), `scripts/wp-browsers.js`, `scripts/wp-gate.js`, `scripts/wp-dl.js`, then `test-cases.md` (WP-01…WP-22).

## Intent

Someone has a finished letter, résumé, contract or report in Word and needs a PDF to send or upload now, on a device without Word. They need the PDF to read exactly like their document — every word in every language they wrote it in, page numbers, lists, tables — so they can send it without checking each line. They need to trust that the document never leaves their device. They should leave impressed and see the Pro pass as worth it.

The engine is strong: about a second for a 4-page document and 1.5 s for 200 pages, headings, bold/italic/underline, colour, bullets and numbered lists, bordered tables with a merged cell and leading zeros intact, pictures, clickable links, headers/footers with real page numbers, a landscape section, Letter/A4 choice for text, an automatic switch to Exact look for multi-column files with a clear "Not carried over" note, honest pre-convert notes about non-Latin scripts, clear errors for .doc/.rtf/.odt/damaged/renamed/empty files, identical results in Chromium, Firefox and WebKit, and nothing uploaded (only a font file from the site itself).

Trust is lost where Hindi words come out broken in the default mode — on a site with a Hindi locale — and where Exact look turns Word's standard bullets into empty boxes.

## Why: what the evidence says

- **P1: Hindi (Devanagari) text is broken in Keep formatting and Text only.** "हिन्दी" is drawn as "हि  दी": the conjunct न् is missing, and the word runs into the next one ("दीemoji"). The page and the pre-convert note say Hindi is "drawn as pictures so they look right"; in fact it's drawn with an embedded Devanagari font without shaping. Exact look draws it correctly. Same in Chromium, Firefox, WebKit. (`screens/live/hindi-crop-1.png`, `testfiles/outputs/out-W01.pdf`)
- **P2 (verify on Windows/macOS): Exact look draws Word's default bullets as empty boxes (☐).** Word's built-in bullet uses the Symbol font (U+F0B7); our Linux browsers have no Symbol font, so the DOM capture shows tofu in all three engines. Keep formatting maps them to "•" correctly. Android/ChromeOS/Linux users would get boxes; Windows/Mac likely fine (unverified). (`screens/live/w02-zoom.png`, `w17-bul.png`)
- **P2:** Exact look leaves "Page  of" when the footer uses simple fields (`w:fldSimple`), while Keep formatting fills them; complex fields work in both. Exact look on 200 pages makes a 31.8 MB PDF (Keep formatting 0.6 MB).
- **P3:** .doc/.rtf/.odt get the picker's generic "can't be used here · This tool takes .docx and .txt files" instead of the specific "save as .docx" messages the page promises (the code has them); no PDF bookmarks from headings; no /blog/word-to-pdf; locale titles English, /ar 404; axe label-content-name mismatch; iPhone SE 9 px overflow (site-wide).
- **Video is current:** cfoa2qODfW4 (Oct 15, 2026, 74 s) shows today's UI with "Trial: 10 uses/day", $1 / $4.99, all three modes and a converted PDF; 0 views.

## Outcomes we want

1. Hindi and other Indic text in the PDF reads exactly as typed in every mode (shaped correctly, or drawn as pictures as promised), with the page copy matching what happens.
2. Exact look shows Word's standard bullets and simple page-number fields on every device.
3. Old formats get the specific "save as .docx" guidance the page describes.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | Latin/Greek/Cyrillic/CJK/Arabic/emoji right; Devanagari broken in 2 of 3 modes; Exact-look bullets. `findings/live-functional-findings.md` |
| 2 | Completeness | **PASS** | LOW | 3 modes, paper size, Stop, clear errors. No bookmarks; password .docx untested. |
| 3 | Ease of use | **PASS** | — | Pre-convert script notes, mode lines saying what's lost, auto Exact look, preview. |
| 4 | Layout | **PASS** | LOW | 10 profiles clean except 9 px header overflow at 320 px (site-wide); ja desktop 3 px. |
| 5 | Payment process | **PASS** | — | At 0: Download → "Today's trial uses are done" ($4.99 / $1) → Buy Day Pass $1 → email prompt (stopped; nothing typed). Result kept. `json/dl-gate.json` |
| 6 | Information correct | **PARTIAL** | MEDIUM | "Hindi… drawn as pictures" untrue in Keep formatting; .doc message differs from copy. `findings/desk-findings.md` |
| 7 | Indexing | **PASS** | — | 200, self-canonical, not noindex. GSC data is not available. |
| 8 | SEO | **PARTIAL** | LOW | Strong title/meta; locale titles English; /ar 404. |
| 9 | Blog | **PARTIAL** | LOW | /blog/word-to-pdf 404; Guides link 2 related posts; 1 post links here (tools.csv). Another-slug post is an unverified absence. |
| 10 | YouTube video | **PASS (no reach)** | LOW | cfoa2qODfW4 embedded; 74 s, 0 views. |
| 11 | FAQ / guide | **PASS** | LOW | 10 FAQs + Details, honest about fonts, scripts and modes; one script claim wrong. |
| 12 | Video shows current tool | **PASS** | — | Today's UI, trial wording, prices, modes, result. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Save to my cloud storage → sign-in dialog; Save to Google Drive gated at 0 (sign-in untested); Open from Google Drive not clicked. |
| 14 | Sharing | **N/A** | — | No share/copy on the result (live-verified) although tools.csv lists share/copy. |
| 15 | Downloads | **PASS** | — | rich.pdf = memory + intentional badge. |
| 16 | Usage count | **PASS** | — | Convert free; 1st Download 0 → 1; repeats free. Counter display-only evidence. |
| 17 | Category placement | **PASS** | — | PDF Tools. |
| 18 | Site section | **PASS** | — | Professional Tools. |
| 19 | AI need / demand | **PASS** | — | Grouped with rank 19. GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | Universal File Converter's Word → PDF is simpler; this is the rich version. Cross-link. |
| 21 | Remove? | **N/A (keep)** | — | Core Professional Tool. |
| 22 | Duplicates | **PASS** | — | C05 ladder (UFC, File Conversion Studio) linked on the page. |
