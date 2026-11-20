Sent: 2026-11-20 08:40 ET

# FDP-22 Universal File Converter (universal-file-converter): deep test report for Claude

- **Written:** 2026-11-19 17:55:15 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/universal-file-converter. Row 22 of TEST-ORDER.md: Premium, PDF Tools, test-plan rank 19 (129 + 79 views), duplicate cluster C05. **GSC data is not available.**
- **Classification:** Premium Application (2 trial uses a day, $3 Day Pass / $9.99 month). Category PDF Tools (+ home, premium-apps); breadcrumb says "Premium Applications". Gated at Download: converting and previewing are free, Download costs 1 trial use.
- **Testers:**
  - **Desk review:** page (expanded copy), JSON-LD, /es, /ar, blog, category; `UniversalFileConverter`, `universalCore`, `legacyDeck` code.
  - **YouTube video:** metadata + 21 frames.
  - **Headless Playwright:** 21 input files × every offered target (outputs inspected with openpyxl/python-docx/pdftotext/pdftoppm), request capture per conversion, toast capture for the silent cases, gate and dialogs, keyboard, axe, edit panel, Multiple files (21 files), phones, Firefox + WebKit, matrix (10 profiles, 10 locales + /ar, 6 geos, axe).
- **Starting counts:** most contexts loaded at 2/2 used (0 remaining) — e.g. 17:32:41 EST "Trial: 2 uses/day · 0 remaining today"; about 1 in 4 loaded with 2 remaining. Counters are display-only evidence.
- **Trial use observed:** with uses left, Download of a converted PDF cost 1 (0 → 1); a second Download of the same result was free (1 → 1). The downloaded PDF (6,141 B) is the in-memory result (5,144 B) plus the intentional "Created with FreeDailyPro.com" badge. Conversions themselves cost nothing (gate at Download — consistent with other Download-gated tools, not flagged).
- **Constraints kept:** guest only, no sign-in, nothing typed into email/card prompts, no ad clicks, no API/MCP, no site/repo changes. Outputs were only parsed, never executed.
- **Sign-in:** Save to Google Drive opens Google sign-in (closed); Save to my cloud storage → "Sign in" dialog (Not now); Open from Google Drive and Take photo not clicked. See INSTRUCTIONS.md.
- **Pending:** none. No RERUN-AFTER-RESET row needed.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships converters.

Code to look at:
- `evidence/js/legacyDeck.pretty.js` L17–70: `presentation.convert.mutate({ fileBase64, fileName, to })` (30 MB cap) — the server round trip.
- `evidence/js/universalCore.pretty.js` L260–300 (spreadsheet/CSV read and JSON), L686 ("This file is already a .pptx." skip), import of legacyDeck L46.
- `evidence/js/UniversalFileConverter-D_J0VhRj.pretty.js`: accept list `Os` L223 (no .odp/.key/.pps), generic error toast L1552, edit list L1862–1880, compression levels L2630–2645, batch cap `st = 20` L180 / toast L451, on-page privacy note L2186.

After you ship, rerun `scripts/uf-battery.js` (all), `scripts/uf-toasts.js`, `scripts/uf-gate.js`, `scripts/uf-dl.js`, then `test-cases.md` (UF-01…UF-24).

## Intent

Someone has a file in the wrong format — a HEIC photo, a CSV of customers, an old .ppt deck, a Word letter — and needs it in another format now, without installing anything and without handing the document to a stranger. They chose this page because it promises "No Upload" in the title, a "Files never stored" chip, and FAQs that say "Nothing is uploaded anywhere." They need the converted file to contain the same data they put in. They should leave impressed and see the Premium pass as worth it.

The engine is strong: correct detection for every supported type, ~30 real conversion pairs that finish in about a second, emoji/CJK-safe PDFs, OCR that read a test invoice perfectly, PDF→Excel table extraction, chained conversions, an edit panel (resize/crop/rotate/watermark/page numbers/compress/password/merge), a 20-file batch that counts as one use, clean errors for unsupported and damaged files, and the same results in Chromium, Firefox and WebKit.

Trust is lost in three places: presentation conversions send the whole file to the server while every privacy line says nothing is uploaded; CSV conversions silently change the data (leading zeros, a cell dropped); and several offered targets dead-end with a generic error.

## Why: what the evidence says

- **P1: presentations are uploaded, but the page says nothing is uploaded.** Live request capture: `.pptx → OpenDocument .odp` sent `POST /api/trpc/presentation.convert` with 40,246 bytes (the 30 KB deck as base64); `.ppt → PDF` and `.ppt → .pptx` each sent 870,466 bytes. The title ("No Upload"), meta ("Nothing is uploaded"), chip ("Files never stored"), two FAQs ("Nothing is uploaded anywhere"; "your document contents are not sent"), Privacy section and the on-page note ("Files are converted in your browser and are not uploaded") all say otherwise. Every other conversion we ran made no upload (image, HEIC, PDF, text, Word, Excel, CSV, HTML, Markdown, .pptx → PDF/JPG). `findings/live-functional-findings.md`
- **P1: CSV conversions change the data.** `data.csv` → Excel and → JSON turned ZIP codes 02134 / 00501 into numbers 2134 / 501; → JSON turned the text cell `=1+1` into an empty string. (Excel kept `=1+1` as text — safe.) Excel → JSON writes dates as serial numbers (46023) while Excel → CSV writes 2026-01-01.
- **P1: `.doc` is accepted, detected as "Word document" and offered PDF/Text/HTML, then fails with "That conversion didn't work on this file."** The console knows why ("NotDocxError: This isn't a Word (.docx) file"). Limitations mention it, but the user at the button is never told. Same generic toast for a damaged .pptx.
- **P2:** `.pptx` is offered "PowerPoint .pptx (from old formats)", then "This file is already a .pptx." (the page promises "never a dead-end option"); the format table lists .pps/.odp/.key as inputs but the picker rejects .odp ("can't be used here"); HTML → Text/PDF print the `<script>` source as visible text; Word → HTML drops bold and table structure; compression levels are "Recommended (~50%) / Medium (~25%) / Strong (~50%)" while the FAQ says "Balanced/Aggressive/Extreme/Target size" and Tips say "Light before Strong"; the page hero image and video show a mock app ("100+ formats", MP4→GIF, JSON→YAML) that doesn't exist; axe: 2 critical unnamed buttons; horizontal overflow on iPhone (WebKit) 9–50 px.
- **P2: video is outdated.** "10 trial usages every day", "10 remaining today", "$1 day pass / $4.99 monthly", "MultiTool Apps" breadcrumb (today: Premium, 2 a day, $3 / $9.99). It does show the tool converting CSV → Excel.

## Outcomes we want

1. What the page says about uploads is exactly true for every conversion, including presentations (either convert them in the browser, or say plainly which conversions go to the server, what happens to the file and how long it's kept — before the user clicks).
2. A CSV converted to Excel or JSON contains exactly the values that were in the CSV (leading zeros, formula-looking text).
3. Every offered target either works or explains, before or at the click, why it can't (real .doc, .pptx → .pptx).
4. The input list on the page matches what the picker accepts.
5. The video, hero image and compression copy show today's tool, prices and options.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | ~30 pairs correct and fast; CSV data altered; .doc and .pptx→.pptx dead-end. `findings/live-functional-findings.md`, `testfiles/outputs/` |
| 2 | Completeness | **PARTIAL** | MEDIUM | .odp/.key/.pps listed but rejected; no SVG/GIF (stated). Edit panel and batch present. |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Detection + only-real-targets is excellent; generic error toasts; dead-end targets. |
| 4 | Layout | **PARTIAL** | LOW | Clean on 8/10 profiles; iPhone SE 9 px and iPhone 14 Pro Max 50 px horizontal overflow (WebKit); ja desktop 3 px. |
| 5 | Payment process | **PASS** | — | At 0: converted Download → "Today's trial uses are done" → Buy Day Pass $3 → email prompt (stopped; nothing typed). `json/dl-gate.json`, `screens/live/cap-dialog.png`, `daypass-email.png` |
| 6 | Information correct | **FAIL** | HIGH | "No Upload"/"Nothing is uploaded" untrue for presentations; compression level names; input list. `findings/desk-findings.md` |
| 7 | Indexing | **PASS** | — | 200, self-canonical, not noindex. GSC data is not available. |
| 8 | SEO | **PARTIAL** | MEDIUM | Title/meta promise "No Upload"; locale titles in English; /ar 404. |
| 9 | Blog | **PARTIAL** | LOW | Blog (Sep 22, 2026) honest about ~30 pairs; says "MultiTool Apps" (old name). |
| 10 | YouTube video | **PASS (low reach)** | LOW | gkHJ4c6-d7s embedded; 61 s, 15 views (Oct 16, 2026). |
| 11 | FAQ / guide | **PARTIAL** | HIGH | Thorough FAQ/Details; two upload FAQs wrong for presentations; compression names wrong. |
| 12 | Video shows current tool | **FAIL** | MEDIUM | 10 uses/day, $1/$4.99, "MultiTool Apps", mock UI. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Save to Google Drive → Google sign-in popup; Save to my cloud storage → $4.99/mo, "Sign in" dialog; Open from Google Drive not clicked. |
| 14 | Sharing | **N/A** | — | No share-result button (live-verified); "Share this tool" is site-wide. |
| 15 | Downloads | **PASS** | — | `dl-1-small-converted.pdf` = in-memory result + intentional badge; free conversions are never charged. |
| 16 | Usage count | **PASS** | — | Convert free; 1st Download 0 → 1; 2nd Download free; batch = 1 use (copy). Counter display-only evidence. |
| 17 | Category placement | **PARTIAL** | LOW | Category PDF Tools, breadcrumb Premium Applications; it converts far more than PDFs. |
| 18 | Site section | **PASS** | — | Premium Applications. |
| 19 | AI need / demand | **PASS** | — | Rank 19, 129 + 79 views; 8 posts link here. GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | Hub for C05; single-format converters feed it. |
| 21 | Remove? | **N/A (keep)** | — | Core Premium Application. |
| 22 | Duplicates | **PARTIAL** | LOW | C05 overlap with convert-image hub and file-conversion-studio (Workflow); link the ladder clearly. |
