Sent: 2026-11-21 03:05 ET

# FDP-38 PDF to JPG (pdf-to-jpg): deep test report for Claude

- **Written:** 2026-11-21 02:47 EST (box `date`, ET). Testing ran 2026-11-21 02:30–02:46 EST.
- **Tool:** https://www.freedailypro.com/tool/pdf-to-jpg. Row 38 of TEST-ORDER.md: Pro, PDF Tools. Plan note "L-243 rank 1 (PDF Toolkit API live)".
  - Pair page: /tool/pdf-to-jpg/pdf-to-png.
  - Blogs: /blog/pdf-to-jpg and /blog/pdf-to-jpg-slides-from-packet.
  - Video: WUw3lpbCV9E.
  - **GSC data is not available.**
- **Classification:** Professional Tool. Rendering runs in the browser (pdf.js + canvas); no upload or API call was seen (`evidence/json/privacy.json`).
- **Testers:**
  - **Desk review:** copy, JSON-LD, 10 locales + /ar, blog, JS chunks.
  - **Headless Playwright:**
    - 18 live cases in Chromium (5 also in Firefox)
    - a uses-left gate run (6 downloads)
    - an at-0 run (preview capture, page-range preview, cap dialog, Day Pass, keyboard)
    - privacy + Share; the pair page
    - the 10-device / 11-locale / 6-geo / axe matrix
  - **Pixel comparison** of previews and downloads (PIL).
- **Starting counts (display-only):** 10 fresh contexts loaded at 0; the 11th had 10 left and ran the gate.
- **Constraints kept:**
  - Guest only and no sign-in. No email or card typed: stopped at the Day Pass email prompt and at Stripe Checkout (session id redacted).
  - No ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):** Save to Google Drive (Google sign-in popup) and Save to my cloud storage (email sign-in dialog). Open from Google Drive was not clicked.
- **Pending:** nothing needs the 7:00 PM ET reset, so there is no RERUN-AFTER-RESET row.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

**Owner context:** on Nov 20 Santosh decided that every Download on Barcode Generator and Invoice Generator uses a trial use. Charging only the first Download per page load conflicts with that decision, and so do full-quality previews at 0 trial uses. Both are P1 gate gaps, and this tool has both. Here the preview is worse than "full quality": it is the exact output without the trial badge.

**Code to look at:**
- **`PdfToJpg-CeZwXbKx.pretty.js`:**
  - `ne()` makes object URLs from `s.previews[].blob`, the real rendered outputs (first 12).
  - Convert `G` doesn't touch usage.
  - The badge is applied only in the Download path.
  - Options: render previews as small downscaled thumbnails (say 300 px wide, or a low-quality re-encode); or stamp the badge before the preview; and/or charge at Convert.
- **Per-page-load counting:** shared `index-B1CTyGtY.js` `RA`/`xI`/`DI` with the set `Kt` (`evidence/js/index-B1CTyGtY.excerpt-usage.js`). The Download label even drops "uses 1 trial use" after the first charge.

**After you ship:**
1. Rerun `scripts/pj-gate.js` (B and C must charge; previews at 0 must not equal the outputs).
2. Rerun `pj-live.js chromium` and `pj-privacy.js`.
3. Work through test-cases.md (PJ-01…PJ-32).

## Intent

Someone has a PDF and a form, chat or slide that only takes images. They want:
- the right pages as images at a size the destination accepts
- names that sort
- nothing uploaded
- a clear message for locked, damaged or huge files

The engine delivers:
- Four dpi presets, exact on Letter (918×1188 → 2550×3300). Mixed page sizes are kept per page.
- JPG or PNG.
- Page ranges with clear errors ("outside this PDF's 50 pages", "starts after it ends").
- A 16 MP cap that says so.
- Per-PDF ZIP folders with "(2)" for duplicates.
- In-browser unlock for password PDFs; a 50-page Print run in 3.4 s.
- Nothing leaves the tab.

Revenue and trust break in three places:
- **Gate:** the preview hands over the product for free and badge-free, and only the first Download per page load is charged.
- **Discovery content:** the video is from an older UI and shows "0 free uses remaining".
- **Copy drift:** the password behaviour is described three different ways.

## Why: what the evidence says

- **P1 gate gap: full-quality, badge-free previews at 0 trial uses.**
  - At 0 trial uses (`gate.json` → `zero`, 02:41 EST), Print on Q01 rendered a 2550×3300, 1,065,785 B preview, and Download hit the cap dialog.
  - Range "37" on the 50-page PDF previewed page 37 at 2550×3300 (Print setting kept). Any page is reachable, 12 per Convert, and Convert costs nothing.
  - With uses left, preview B is pixel-identical to download B except the download carries the "Created with FreeDailyPro.com" badge (`evidence/screens/cmp-preview-vs-download-B.png`). So the free preview beats the paid trial download and matches what a pass sells.
- **P1 gate gap: one trial use per page load** (02:39–02:41 EST):
  - Download A 0 → 1; again 1 → 1.
  - Convert another, P02 → Download B 1 → **1**. P03 PNG range 2-4 → Download C 1 → **1**.
  - After a reload, D 1 → 2 and E 2 → 3.
- **P2: video out of date.**
  - Recorded 8/23/2026 on the old UI: no quality, PNG, range or thumbnails, and "10 free uses daily".
  - The strip reads "0 free uses remaining today" while the demo converts.
  - It shows the OneDrive label "aloo - Personal" in the file picker.
- **P2: the meta description** (92 chars) doesn't mention PNG, dpi or page ranges. Title and meta stay English in 9 locales; /ar 404.
- **P3 items:**
  - Password copy: the tool copy says "skipped and listed", the blog says "fail with an error", but live there is an unlock dialog (Skip → toast).
  - VideoObject name doesn't match the YouTube title.
  - The video shows the old header "Search 200+ tools"; the live header and blog say 300+ (consistent).
  - Pair-page title says "Free".
  - Firefox JPGs are about 2.6× larger.
  - Owner-only restrictions are removed silently (policy note).
  - iPhone SE 9 px and ja 3 px overflow; axe issues (link-in-text-block ×3, label mismatch, ad-caption contrast).

## Outcomes we want

1. At 0 trial uses, nothing on screen can stand in for the Download: thumbnails are small or badged, and a page range can't be used to harvest pages.
2. Every Download is counted the way Santosh decided, including after "Convert another" without a reload.
3. A current-UI video: dpi buttons, PNG, page range, thumbnail sizes, Download; neutral file names, no personal account labels, and a strip that doesn't show 0.
4. One accurate story about password PDFs across copy, FAQ and blog.
5. A richer meta description and translated title/meta.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | dpi presets exact; PNG; ranges; 16 MP cap; mixed sizes; unlock; 50 pages Print in 3.4 s. |
| 2 | Completeness vs competitors | PASS | Batch, ranges, dpi, PNG, folders. Could add a custom width/dpi or a "max KB" target (the blog's portal use case). |
| 3 | Ease of use | PASS | Clear buttons with dpi; size captions; precise range errors. |
| 4 | Layout attractiveness | PASS (minor) | iPhone SE 9 px, ja 3 px. |
| 5 | Payment process | PASS (stopped) | Cap dialog / Quick Buy day → "Day Pass, $1" email prompt; Quick Buy monthly → Stripe Checkout. Stopped. |
| 6 | Information correct | PARTIAL | Password copy is out of date; otherwise accurate. |
| 7 | Indexing | PASS | 200; canonical self; pair page canonical self; in sitemap. |
| 8 | SEO | PARTIAL | Meta 92 chars, thin; VideoObject name mismatch; locales English title/meta; /ar 404. |
| 9 | Blog exists and accurate | PASS (minor) | /blog/pdf-to-jpg accurate except the password line and "300+". |
| 10 | YouTube video exists | PASS | WUw3lpbCV9E embedded. |
| 11 | FAQ and guide correct | PARTIAL | How-to matches; the "skipped and listed" line is stale. |
| 12 | Video shows current capabilities | **FAIL** | Old UI; shows 0 trial uses; "free" wording; personal OneDrive label. |
| 13 | Storage | PASS | Nothing stored; Drive/cloud need sign-in (untested). |
| 14 | Sharing | PASS | Share copies only the tool URL. |
| 15 | Downloads | PASS | `-page-03.jpg`, `-images.zip`, `converted-images-3-files.zip` with folders and "(2)". |
| 16 | Usage count | **FAIL (2 × P1)** | Full-res badge-free previews at 0; B and C free after the first charge per page load. |
| 17 | Categorization in section | PASS | PDF Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › PDF Tools. |
| 19 | AI need/demand | PASS (demand strong) | "pdf to jpg" is one of the highest-volume PDF queries; no AI needed. |
| 20 | Merge better? | No | Distinct; the PNG pair page is the right pattern. |
| 21 | Remove? | No | |
| 22 | Duplicates | None in-group | Overlaps Universal File Converter (cross-linked as the next step). |

## Severity summary
- **P0:** 0. Rendering and privacy hold.
- **P1:** 2 (full-quality badge-free previews at 0; one use per page load).
- **P2:** about 3 (video, meta/locales, copy drift).
- **P3:** several.
