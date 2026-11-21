Sent: 2026-11-21 01:50 ET

# FDP-34 Convert Image Format (convert-image): deep test report for Claude

- **Written:** 2026-11-21 01:48 EST (box `date`, ET). Testing ran 2026-11-21 01:25–01:45 EST.
- **Tool:** https://www.freedailypro.com/tool/convert-image (+13 pair pages). Row 34 of TEST-ORDER.md: Pro, Image Tools. Plan note "L-243 rule 1 (ApyHub billable/live)"; tools.csv tag `gated:file-job`. Duplicate group C05 (heic-to-jpg and webp-converter are presets). **GSC data is not available.**
- **Classification:** Professional Tool. Everything ran in the browser; no ApyHub or other upload call was seen (the "ApyHub billable" note doesn't match what the page does today; the FAQ's "FreeDailyPro API" options were not tested).
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD (20 FAQs), 10 locales + /ar, 13 pair pages, the blog, sitemap. JS chunks: `ConvertImage`, `ConvertOptionsPanel`, `convertCore`, `decode`, `ToolPage`, `index`.
  - **YouTube video:** yt-dlp, 26 frames, 3 sheets, 2 zooms.
  - **Headless Playwright:** 16 synthetic files, 32 conversion cases (Chromium) + 4 in Firefox; 7 pair pages; batch; three uses-left gate runs and one at 0; Quick Buy; Share; print; keyboard; axe on the loaded state; 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** most fresh contexts loaded at 0 remaining (`usageToday` 10, day key 2026-11-21); 1 in about 5 loaded with 10 left — those were used for the gate runs. Trial uses spent: **6**.
- **Constraints kept:** guest only, no sign-in, no email or card typed (stopped at the Day Pass email prompt and at Stripe Checkout; session id redacted), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):** Save to Google Drive (Google sign-in popup), Save to my cloud storage ("Sign in with your email first", $4.99/month 1 GB). Open from Google Drive and Take photo with camera were not clicked.
- **Pending:** nothing that needs the 7:00 PM ET reset (all trial behaviour was observed in uses-left contexts), so no RERUN-AFTER-RESET row. Still unverified: AVIF output in a real desktop Chrome/Firefox.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Code to look at:
- **`evidence/js/index-B1CTyGtY.js`, `xI` / `vI` and the set `Kt`:** once a tool id is in `Kt`, `xI` returns "allowed" without logging. It is filled on the first allowed use and cleared only by `wI`, so a tool logs one use per page load. This is shared code; it likely explains FDP-33's uncharged ZIP too.
- **`ConvertImage-BKNYLFdo.pretty.js`:** single Convert makes no usage call; Download goes through the shared download button in `ToolPage-*` (`logUsageNow("download")`); batch `X()` calls `logUsageNow()` once; the result preview is `<img alt="Result preview" src=blob:…>` of the same blob Download saves.
- **Quality defaults:** single 92, batch 80.

After you ship, rerun `scripts/cim-gate2.js` and `cim-gate3.js` (expect each Download / batch to follow the policy you choose), `cim-live.js` (C01–C32 unchanged), `cim-axe-loaded.js`, then test-cases.md (CI-01…CI-46).

## Intent

Someone has a picture in the wrong format for a form, store, site, printer or app. They want to:
- drop it (or a whole set), pick the target, and get a file the destination accepts
- keep or lose transparency, metadata and size deliberately, not by accident
- do it without uploading private photos

The engine does this very well:
- 30 of 32 conversion cases behaved as the page says (C23 truncated file converts silently; C32 AVIF output disabled), across 9 input formats and 7 working output formats (HEIC, AVIF, TIFF, SVG, animated GIF/WebP, ICO multi-size, BMP depth, EXIF keep/strip with GPS, DPI, resize/fit/no-enlarge, rotate/mirror/grey, validation).
- A 6000×4000 JPEG → WebP in 1.3 s; batches report "5 in, 4 out" with reasons.
- Nothing is uploaded; SVG scripts don't run; location data is stripped by default.
- The 13 pair pages preselect the right target.

Trust breaks in four places:
- **Trial counting:** after the first Download, every further Download and batch in the same page load is free.
- **Gate leak:** the on-page preview is the full converted file, shown even at 0 remaining.
- **AVIF:** advertised as an output but disabled in both tested engines.
- **Video and wording:** a 78 s old-UI video with "10 free uses daily"; 13 pair-page titles say "Free".

## Why: what the evidence says

- **P1, policy question for Santosh: one trial use per page load.**
  - `gate2.json` (01:39:53–01:40:20 EST): Download A 0 → 1; Downloads B and C (different images) 1 → 1; reload; frames ZIP 1 → 2; SVG 2 → 2.
  - `gate3.json` (01:45 EST): single 0 → 1, then a batch of 3 1 → 1; reload; batch 1 → 2, then a single 2 → 2.
  - `gate.json`: re-download 1 → 1; GIF frames ZIP after a Download 1 → 1.
  - Code: `Kt` set in `index-*.js`. Not in the Nov 20 uncounted list (Barcode/Invoice charge every Download). Batch "counts as one use" is documented, but with no trial batch limit (compress-image says "up to 5 at a time on the trial").
- **P1: the result preview gives away the download.** Preview `<img>` blob = Download bytes (sha `ebfb1788…` for both, `gate.json`); full resolution (6000×4000 in C24); shown at 0 remaining (`screens/live/case-C02.png`) while Download opens the cap dialog. "Save image as…" on the preview yields the file (browser behaviour; not clicked).
- **P2: AVIF output unavailable.** "AVIF (not available here)" disabled in Playwright Chromium and Firefox; the page advises "a current Chrome or Firefox desktop" (unverified). AVIF is in the description, title-level copy and JSON-LD.
- **P2: video vHFSmxgaxAU (78 s, 10 views, 2026-09-23):** old "Convert Formats" UI (PNG/JPEG/WebP only, "10 free uses daily", "Works with any file size"), caption "10 free uses daily!", ~30 s end card, "200+ Free Productivity Tools".
- **P2: wording/SEO:** 13 pair titles "… Converter - Free, No Upload"; main title lacks the brand suffix; locale H1s use the old name "Convert Formats"; English title/headings under 9 hreflangs; /ar 404.
- **P2: blog** says SVG is "a different tool path" and "use bulk tools" for batches — this tool does both.
- **P3 items:**
  - Truncated JPEG converts silently with a transparent gap (no "may be damaged" warning).
  - Batch quality starts at 80, single at 92 (FAQ says 92).
  - Duplicate FAQ ("many" / "multiple images at once").
  - Cap dialog promises the passes remove a mark that converted images don't carry.
  - Quality slider has no accessible name; "Which tool" links rely on colour; two "Quick Buy" buttons; iPhone SE 9 px and ja 2 px overflow; thumbnail alt; generic og:image; JSON-LD Offer 4.99.

## Outcomes we want

1. Santosh decides what one trial use buys (one file, one batch of up to N, or one page visit), and the shared counter, labels, FAQ and blog all say the same.
2. The preview can't be saved at full quality without a use: e.g. a downscaled or marked preview, or the preview shown only after Download is allowed.
3. AVIF output that works in common browsers (WASM encoder) or copy that stops promising it.
4. A current, clean video (HEIC → JPG, transparent PNG → JPG with fill, batch ZIP, ICO) with "trial uses" wording.
5. Pair titles and locale H1s with the current name and no "Free".
6. P3 polish: damaged-file warning, one quality default, de-duplicated FAQ, slider label.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | 32 cases incl. HEIC, AVIF in, TIFF, SVG, ICO, EXIF/GPS, DPI, resize, batch (`json/cases-chromium.json`). AVIF out unavailable (P2). |
| 2 | Completeness vs competitors | PASS (minor) | Broad; gaps: AVIF out, lossless/progressive (API only), animated output, size target (desk). |
| 3 | Ease of use | PASS | Smart default targets, fill picker, clear validation and skip list, pair pages. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px, ja 2 px overflow; small targets. |
| 5 | Payment process | PASS (stopped) | Cap dialog / Quick Buy day → "Day Pass, $1" email prompt; Quick Buy monthly → Stripe Checkout. Nothing typed. |
| 6 | Information correct | PARTIAL | Mostly precise. AVIF promise, 92 vs 80 default, mark claim in cap dialog, nothing about per-page-load counting. |
| 7 | Indexing | PASS | 200; canonical self; sitemap incl. 13 pair pages and blog. |
| 8 | SEO | PARTIAL | Good meta, FAQPage (20), VideoObject. Pair titles "Free"; no brand in main title; locale H1 old name; English titles; /ar 404; generic og:image; thumbnail alt. |
| 9 | Blog exists and accurate | PARTIAL | `/blog/convert-image` useful, but wrong on SVG and batch; no ICO/fill/EXIF/HEIC. |
| 10 | YouTube video exists | PASS | vHFSmxgaxAU, 78 s, 10 views, 2026-09-23. |
| 11 | FAQ and guide correct | PASS (minor) | 20 FAQs accurate in behaviour; duplicate question; 92 vs batch 80. |
| 12 | Video shows current capabilities | **FAIL** | Old 3-format UI, "10 free uses daily", long end card. |
| 13 | Storage | PASS | No upload, no storage; EXIF/GPS stripped by default. |
| 14 | Sharing | PASS | Share copies only the tool URL. |
| 15 | Downloads | PASS | Correct names/extensions, ZIPs (frames, batch). Drive/cloud need sign-in (untested). |
| 16 | Usage count | **Policy question (P1)** | Convert free; first Download per page load −1; everything else in that page load free; batch = 1; gate holds at 0 except the full-quality preview. |
| 17 | Categorization in section | PASS | Image Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Image Tools. |
| 19 | AI need/demand | PASS (demand strong) | "png to jpg", "heic to jpg", "webp to png" are high-volume evergreen queries; pair pages target them. No AI needed. |
| 20 | Merge better? | Hub already | C05: keep as hub; heic-to-jpg / webp-converter as presets only if they rank. |
| 21 | Remove? | No | |
| 22 | Duplicates | C05 (presets) | Explained on the page ("Which tool should I use?"). |

## Severity summary
- P0: 0. Privacy holds: no image data in any request.
- P1: 2 (one trial use per page load; full-quality preview available at 0).
- P2: about 5 (AVIF output, video, pair-title/locale wording, blog, completeness).
- P3: several.
