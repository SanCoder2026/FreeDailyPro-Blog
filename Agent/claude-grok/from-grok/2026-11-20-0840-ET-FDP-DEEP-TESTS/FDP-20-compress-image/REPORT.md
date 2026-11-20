Sent: 2026-11-20 08:40 ET

# FDP-20 Compress Image (compress-image): deep test report for Claude

- **Written:** 2026-11-19 17:02:11 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/compress-image. Row 20 of TEST-ORDER.md: Pro, Image Tools, grouped with test-plan rank 17 (Image Resize/Crop + Compress Image). **GSC data is not available.**
- **Classification:** Professional Tool, Image Tools (+ home, corporate-safe-tools, professional-tools, online-sellers and web-designer solutions). Trial-gated at Download (`gateAtDownload`); Compress itself is not charged, which matches the other gated-at-Download tools and is not flagged.
- **Testers:**
  - **Desk review:** page (all sections expanded), JSON-LD, /es, /ar, blog slug, category; `CompressImage` and `utils` (compress engine) code.
  - **YouTube video:** metadata + 26 frames.
  - **Headless Playwright:** 27 image × setting cases (outputs checked with Pillow, incl. EXIF/GPS), invalid targets, gate and dialogs, batch (Several files), keyboard, axe, phones, Firefox + WebKit, matrix (10 profiles, 10 locales + /ar, 6 geos, axe).
- **Starting counts:** single-file contexts 10/10 used (0 remaining) at 16:43:43 EST; one batch context loaded with 10 remaining. Counters are display-only evidence.
- **Constraints kept:** guest only, no sign-in, nothing typed into email/card prompts, no ad clicks, no API/MCP, no site/repo changes. One ZIP download happened in the batch context (counted); it was not opened or kept.
- **Sign-in:** see INSTRUCTIONS.md. Untested: "Save to my cloud storage" (sign-in dialog), Save to Google Drive (capped at 0 before Google sign-in).
- **Pending:** single-file Download cost with uses left, second-download charge, file name/bytes, and confirming the downloaded "compressed_" file of an unchanged original still carries GPS. **Needs re-run after midnight UTC (7:00 PM ET).** RERUN-AFTER-RESET row 20 added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and pick fixes that fit how FreeDailyPro ships image tools.

Code to look at (`evidence/js/`):
- `utils-BCX55KBw.pretty.js`: `E()` and the `alreadyUnder` branch of `$()` return the original File (metadata intact); `_ = 0.97` margin; scale steps `[1 … 0.12]`.
- `CompressImage.pretty.js`: download name L109; mode buttons L395–430 (no `aria-pressed`); target input/select L460–490 (no labels); result `<p data-testid=compress-result>` L533 (not live).

After you ship, rerun `scripts/ci-battery.js` (all cases), `scripts/ci-gate.js`, `scripts/ci-invalid.js`, then walk `test-cases.md` (CI-01…CI-20).

## Intent

Someone has a photo that is too big: a job portal wants it under 200 KB, an email bounces, a product page loads slowly. They want a smaller file that still looks right, on their own device, without guessing settings, and they often want the location data gone before sharing. They should leave impressed and see the pass as the obvious way to keep going.

The engine is strong: Medium and Strong really hit 25 %/50 % (Chromium, Firefox, WebKit), Custom Target hits KB limits and says when it resized, transparency is kept as WebP, SVG is left alone, HEIC/WebP/BMP/PNG work, Stop works, the 5-file batch is clear, and EXIF/GPS is removed from every re-encoded file.

Trust is lost at the edges where the page promises more than it does: location data survives when the original is handed back, a 1 MB target misses a 1,000,000-byte limit the copy says it handles, and the copy, snippet and video sell a "Light 10 %" mode that is gone.

## Why: what the evidence says

- **P1: location data is kept when the original is returned.** Already-under-target (C26) and not-smaller (C27, C06) return the input file byte-for-byte; our test photo's GPS (40°44′N 73°59′W) is still in it, and it would download as `compressed_small_gps.jpg`. The page says "Metadata such as location is removed" and the FAQ sells the tool for exactly that before sharing. Fix: strip metadata losslessly (or re-encode) when returning the original, or say clearly that the original — with its location data — is returned.
- **P1: "1 MB" target can still be rejected.** Preset 1 MB → 1,016,321 bytes (C10), shown as "993 KB… Target reached". Details promise "portals that count 1 KB as 1000 bytes still accept the file"; that holds for KB targets only. Fix: a ≥5 % margin for MB (or aim under the decimal value) and show the byte count against both readings.
- **P1: copy, snippet and video describe a "Light (10 % smaller)" mode that doesn't exist.** Meta description ("choose 10%, 25% or 50%"), two FAQ answers (also in FAQPage JSON-LD), Details ("first three… 90%, 75% or 50%"), YouTube description and video. A searcher who clicks for "10 %" can't find it.
- **P1: the video shows an older tool** with "Reduce image file size without losing quality" (the FAQ now calls that inaccurate), "10 free uses daily" badge and caption over the controls, the Light button, and ≈40 of 79 s of end cards.
- **P2 (selected; full list in PRIORITIES.md):**
  - Custom Target keeps 12 MP at quality ≈0.13 (blocky) rather than resizing first (C07); Strong on an already-compressed JPEG goes to q≈0.19 with no quality hint (C04).
  - Animated GIF becomes a single-frame JPG with no notice (C14); GIF/BMP aren't in the accepted list.
  - Accessibility: target box and KB/MB select unlabeled (axe critical ×2), mode buttons expose no selected state, result not announced, focus drops to body, invalid target is toast-only.
  - Phones: Compress is 2–3 screens below the fold on iPhone SE after upload; 32 px buttons; 9 px header overflow at 320 px (site-wide).

## Outcomes we want

1. Every file the tool hands back is free of location/camera metadata, or the page says plainly when it isn't.
2. A user who picks "1 MB" (or any MB value) gets a file a strict 1,000,000-byte portal accepts, and the result shows the byte count.
3. Meta, FAQ, JSON-LD, Details, YouTube description and video describe the four modes that exist today.
4. Custom Target picks the better-looking route (resize before going below a sane quality floor) and warns when quality is very low.
5. Screen-reader users can name the target field and unit, hear which mode is on and hear the result.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PASS** | — | Medium/Strong hit ≥25 %/≥50 % on every compressible input (C01–C04, C12–C14, C16–C18, C20); KB targets met or resized with a message (C07, C09, C24). `findings/live-functional-findings.md`, `json/battery.json` |
| 2 | Completeness | **PARTIAL** | LOW | 4 modes, KB/MB presets, keep-dimensions, batch of 5 + ZIP, Stop. Missing: lossless metadata strip on returned originals, quality warning, GIF animation handling. |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Clear result line with bytes and dimensions. Low-quality full-size output for KB targets (C07); invalid target toast-only; Compress far below the fold on small phones. |
| 4 | Layout | **PASS** | LOW | Clean on 10 profiles; 9 px header overflow at 320 px (site-wide). `screens/devices/` |
| 5 | Payment process | **PASS** | — | At 0: Download → "Today's trial uses are done" → "Buy Day Pass — $1" → email prompt (stopped; nothing typed). Drive at 0 → same dialog. Cloud: $4.99/month, sign-in. `json/gate-kbd.json`, `screens/live/dlg-*.png` |
| 6 | Information correct | **FAIL** | HIGH | Light/10 % mode in meta, FAQ, Details, JSON-LD; metadata-removed claim false for returned originals; 1,000-byte-KB claim false at MB. `findings/desk-findings.md` |
| 7 | Indexing | **PASS** | — | 200, self-canonical, in sitemap, not noindex. GSC data is not available. |
| 8 | SEO | **PARTIAL** | MEDIUM | Good title, FAQPage + VideoObject. Meta description promises the missing 10 % option; /es title says "gratis"; /ar 404. |
| 9 | Blog | **PARTIAL** | LOW | No /blog/compress-image (404, live-verified); related posts (strip GPS, HEIC→JPG) are linked; 30 posts link here (tools.csv). |
| 10 | YouTube video | **PASS (low reach)** | LOW | cr7KoCPKvCg embedded; 79 s, 2 views. |
| 11 | FAQ / guide | **PARTIAL** | MEDIUM | Rich FAQ + Details, honest about lossy output; wrong on Light/10 %, metadata on returned originals, MB margin, "Manual can be larger". |
| 12 | Video shows current tool | **FAIL** | MEDIUM | Old UI, Light button, "without losing quality", "10 free uses daily" caption, ≈40 s end cards. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Cloud storage needs sign-in; Drive capped at 0 before Google sign-in. Untested. |
| 14 | Sharing | **N/A** | — | No share-result button; "Share this tool" is site-wide. |
| 15 | Downloads | **PARTIAL / pending** | — | Batch ZIP `compressed-images.zip` downloaded (not opened). Single-file name `compressed_<name>.<ext>` from code and batch buttons; single download not reached (0 remaining). RERUN row 20. |
| 16 | Usage count | **PARTIAL / pending** | — | Compress free (≈40 runs, no change). Batch ZIP: 0 → 1 (one use per batch, as stated). Single-file Download cost unobserved; needs re-run after midnight UTC (7:00 PM ET). |
| 17 | Category placement | **PASS** | — | Image Tools; also home, corporate-safe, online-sellers and web-designer solutions. |
| 18 | Site section | **PASS** | — | Correct. |
| 19 | AI need / demand | **PASS** | — | Evergreen need (portal size limits, email caps); 30 blog posts link here. GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | Core tool; Resize & Crop and Convert Image are complementary (both linked). |
| 21 | Remove? | **N/A (keep)** | — | High demand. |
| 22 | Duplicates | **PASS** | — | Not listed in DUPLICATES.md; compress-powerpoint / gif-resize-compress / audio-compressor are other media. |
