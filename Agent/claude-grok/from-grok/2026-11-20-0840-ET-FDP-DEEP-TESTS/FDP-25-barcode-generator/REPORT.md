Sent: 2026-11-20 08:40 ET

# FDP-25 Barcode Generator (barcode-generator): deep test report for Claude

- **Written:** 2026-11-19 18:41:30 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/barcode-generator. Row 25 of TEST-ORDER.md: Pro, QR Codes & Barcodes, test-plan rank 20 (2,045 impressions, pos 7.8, 0.1% CTR per the test plan), duplicate group C04. **GSC data is not available.**
- **Classification:** Professional Tool (10 trial uses a day, $1 Day Pass / $4.99 month). Gated at Download: the live preview is free; Download costs 1 trial use — but only once per page visit (see check 16).
- **Testers:**
  - **Desk review:** page (expanded), JSON-LD, /es, /ar, /blog/barcode-generator, /category/qr-tools; `BarcodeGenerator`, `codeGeneration`, `qrHelpers` (validation/list/file names), `csv`, JsBarcode.
  - **YouTube video:** metadata + 21 frames.
  - **Headless Playwright:** 32 value cases over all 6 formats (valid, check digit, length, letters, spaces, full-width digits, accents, tab, symbols, 80/300/400-char Code 128, Code 39 lower case, caption/number off/Tall); every preview and download decoded with zxing-cpp and measured (quiet zones, dpi, size); list mode (problems, duplicates, 201 lines); captions; gate and dialogs; usage across 9 downloads and a reload; privacy (distinctive value never sent); keyboard, axe, phones; Firefox + WebKit; matrix (10 profiles, 10 locales + /ar, 6 geos, axe).
- **Starting counts:** most fresh contexts load at 10/10 used (0 remaining, e.g. 18:25:07 EST); about 1 in 7 load with 10 left (18:35, 18:37 EST). Counters are display-only evidence. Trial uses spent: 3.
- **Constraints kept:** guest only, no sign-in, nothing typed into the email prompt, no ad clicks, no API/MCP, no site/repo changes. Downloaded files were decoded as images, never executed.
- **Sign-in:** none needed — the tool has no Drive/cloud/save buttons (live-verified). Day Pass stops at an email prompt (not typed). See INSTRUCTIONS.md.
- **Pending:** none. No RERUN-AFTER-RESET row needed.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships its Professional Tools.

Code to look at:
- `evidence/js/codeGeneration-D1g4LVfX.pretty.js` L69–139: `margin: 10 * n`, `width: 2 * n`, fixed bar height; caption canvas as wide as the barcode (L98–110).
- `evidence/js/BarcodeGenerator-Y42ebgv8.pretty.js` L104–108 (sample value `J` and Download), L141–177 (download handlers), L502–519 ("Prints … wide" line), L195–208 (Format select trigger width on phones).
- `evidence/js/qrHelpers-av3Dz-dA.pretty.js` L149–218: validation messages, list parsing, file names, index.csv values.
- The download gate itself is shared (`ToolPage` `V` / `useDownloadedResult`): why does one charge unlock every later download in the same visit?

After you ship, rerun `scripts/bc-battery.js`, `bc-ui.js`, `bc-browsers.js`, `bc-dl.js`, `bc-privacy.js`, then `test-cases.md` (BC-01…BC-20).

## Intent

A small seller, warehouse lead or librarian needs barcodes for shelf bins, stock, asset tags or cartons — one now, or a sheet of 50 — and doesn't own label software. They need every barcode to scan first time on a real scanner once it's printed and stuck on a box, at the size the page tells them to print, without learning GS1 rules. They need to trust that their SKUs stay on their device. They should leave impressed and see the Pro pass as worth it.

The tool is strong: six formats, instant preview, check digits added and verified with exact, friendly messages, lower-case Code 39 explained, full printable ASCII in Code 128, a 300 dpi PNG with real pHYs, a clean SVG, a ZIP of up to 200 with an index.csv (formula-escaped) and a clear problem list, the same output in Chromium/Firefox/WebKit, an honest GS1 warning, and nothing uploaded. Every one of 20 valid inputs and every downloaded file decoded correctly.

Trust is lost after printing: the white margins are half what scanners are specified to need, and the page's print-size advice pushes EAN-13 above the GS1 maximum. And the business side leaks: one trial use buys unlimited different barcodes and ZIPs for the rest of the visit.

## Why: what the evidence says

- **P1: Barcodes don't meet print specs the page implies they meet.** Quiet zones are 5 modules on every format (Code 128/Code 39/ITF-14 need 10, EAN-13 right and EAN-8 need 7); ITF-14 has no bearer bars; bar height is fixed so bars are truncated at print size. The FAQ says an EAN-13 should print at ≈3.1 in / 7.9 cm and "do not shrink it much below that" — that is ≈212% magnification, above GS1's 200% maximum; 100% is 3.73 cm. Screen decoding works; printed labels placed next to other print are at risk. (`findings/live-functional-findings.md`, `testfiles/outputs/downloads/`)
- **P1 — policy question for Santosh (not a PASS):** with uses left, the 1st Download cost 1 (0 → 1); the next 8 downloads in the same visit — different values, formats, SVG, two ZIPs (up to 200 barcodes each) — were free (1 → 1). A reload made the next Download cost again (1 → 2). Owner policy (Oct 30): results count. (`json/dl-spend.json`, `json/privacy.json`)
- **P2:** the pre-filled sample 590123412345 can be downloaded and costs a trial use; long captions are cut off on both sides with no warning; on phones, choosing Code 128 (first in the list) makes the Format box ≈453 px wide and the whole page scrolls sideways (iPhone 13 390 → 469 px, Pixel 7, iPhone SE).
- **P3:** stale "Prints … wide" line under an error; no length guard (400 chars → 118 in PNG); index.csv value column mixes forms; canvas has no text alternative; SVG print size unstated and digits use live `monospace` text; FAQ "Code 128 accepts almost any text" vs "no accents"; cap dialog mentions a mark that barcode images don't carry; video lacks ZIP mode and newer controls; /blog/barcode-generator 404.

## Outcomes we want

1. A barcode printed at the size the page recommends, placed on a label next to other text, scans first time — and the page's size advice matches GS1.
2. Each different barcode or ZIP someone downloads counts the way Santosh's trial policy says it should.
3. Phones never scroll sideways, captions are never silently cut, and a trial use is never spent on the sample number.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | HIGH | All 20 valid cases + all downloads decode; quiet zones 5X, ITF-14 no bearers, print size >200%. `findings/live-functional-findings.md` |
| 2 | Completeness | **PASS** | LOW | 6 formats, check digit, list → ZIP (200), PNG 1/2/4× + SVG, caption, number toggle, bar height. No colour/bar-width (documented). |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Excellent messages; sample value chargeable; caption clipping; stale size line. |
| 4 | Layout | **PARTIAL** | MEDIUM | Clean on load on 10 profiles; Code 128 selection overflows all phones (≈470 px). `screens/live/overflow-iphone13-webkit.png` |
| 5 | Payment process | **PASS** | — | At 0: Download → "Today's trial uses are done" ($4.99 / $1, input kept) → Buy Day Pass $1 → email prompt (stopped). `json/dl-gate.json` |
| 6 | Information correct | **PARTIAL** | MEDIUM | Print-size FAQ conflicts with GS1; "almost any text"; cap-dialog mark wording. Privacy claim verified true. |
| 7 | Indexing | **PASS** | — | 200, self-canonical, not noindex, 10 hreflang. GSC data is not available. |
| 8 | SEO | **PASS** | LOW | Format-rich title/meta, FAQPage (12), VideoObject; locales translated; /ar 404 (not in hreflang). |
| 9 | Blog | **PARTIAL** | LOW | /blog/barcode-generator 404; 2 guides linked; tools.csv says 6 posts link here. Another-slug barcode post is an unverified absence. |
| 10 | YouTube video | **PASS (low reach)** | LOW | MXkKnwkHfrk embedded; 63 s, 11 views. |
| 11 | FAQ / guide | **PARTIAL** | MEDIUM | 12 FAQs + Details, honest GS1 guidance; size advice wrong. |
| 12 | Video shows current tool | **PARTIAL** | LOW | Current pricing/trial wording; no ZIP mode, number toggle or bar height. `findings/video-findings.md` |
| 13 | Storage | **N/A** | — | No Drive/cloud/save on this tool (live-verified). |
| 14 | Sharing | **N/A** | — | Only the site-wide "Share this tool"; tools.csv lists share/save/print for the result. |
| 15 | Downloads | **PASS** | — | PNG 4× 300 dpi pHYs, 1×, SVG, ZIP PNG/SVG all decode; file names include check digit; no mark (good). |
| 16 | Usage count | **POLICY QUESTION** | HIGH | Preview free; 1st Download 0 → 1; 8 more different downloads free; reload → 1 → 2. Counter display-only evidence. |
| 17 | Category placement | **PASS** | — | QR Codes & Barcodes. |
| 18 | Site section | **PASS** | — | Professional Tools. |
| 19 | AI need / demand | **PASS** | — | Test-plan rank 20 (2,045 impr, 0.1% CTR — title/meta could win more clicks). GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | Only barcode maker; Label Sheet Maker / QR & Barcode Scanner are complements, linked or linkable. |
| 21 | Remove? | **N/A (keep)** | — | Clear demand. |
| 22 | Duplicates | **PASS** | — | C04 is the QR trio; this tool is distinct. Suggest linking QR & Barcode Scanner ("test your barcode"). |
