# B-0056 Compress PDF: Aggressive and Extreme give the same file, and Balanced gives up a smaller file with the same quality
Priority: P2      Estimated effort: 90 min      Report: #68      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the compression pipeline, challenge this if the code shows a deliberate rule, and choose the best fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Each of the four mode buttons should do what its description says. Users who pick the strongest mode should get the strongest result, or a clear sentence explaining why we stopped. Compress PDF is the #2 PDF tool: 62 views, 22 users, 2m40s, 2 key events in 28 days (analytics/2026-10-29-raw.md), and 257 impressions at position 14.4 in GSC (same file). The test plan's acceptance line is "4 levels produce distinct sizes" (test-plan.csv row 6).

## Why (live, Oct 29 2026, 21:52–22:20 ET, desktop 1280 + mobile 390, Chromium)
- Fixture `scan.pdf` (5 pages, 4.87 MB, colour photos, selectable text plus a link):
  - **Balanced** produced 346,015 bytes (level 1 only).
  - **Aggressive** produced 97,664 bytes.
  - **Extreme** also produced 97,664 bytes, byte-identical to Aggressive (same MD5), still in colour (RGB images), with text still selectable.
  - Even after waiting 90 s, only "Level 1" and "Level 2: Pictures inside fitted to the size" are listed. The Extreme copy promises "every page is converted to grey at 70 dpi, and finally to pure black and white".
- Fixture `photos.pdf` (4 pages, 8.45 MB): the same pattern. Balanced gave 2.13 MB; Aggressive and Extreme both gave level 2 at 161.5 KB, colour, text selectable.
- Level 2 keeps text selectable and links intact, yet it only runs under Aggressive. Balanced users get a file 3.5–13× larger with no gain in quality.
- Competitors: iLovePDF (Extreme / Recommended / Less, all free), Smallpdf (Basic free, Strong is Pro), PDF24 (DPI, quality, greyscale) — ilovepdf.com/compress_pdf, smallpdf.com/compress-pdf, timothe.ai comparison, fetched Oct 29. Each of their presets gives a different result.

## Outcomes
- Balanced includes the picture-fit step (level 2) whenever text stays selectable. That's the promise of Balanced.
- Aggressive and Extreme either run their promised levels and offer them for download, or show one plain sentence such as "Stopped at level 2 — further levels would lose colour/text and the file is already 98 % smaller. Run anyway?" with a button.
- The four modes give visibly different results (or the explanation) on an image-heavy PDF.
- The FAQ, help text and meta keep the B-0022 names. B-0022 is verified fixed; don't regress it.

## Constraints
Browser-only processing. Counting: one use per download. Don't change the level-download list UI beyond what's needed. Test Target size again after the change: under the counter flapping in B-0055 we couldn't download a Target-size result.

## Test cases
R68-CMP-01..04: scan.pdf → each mode → Download Compressed PDF → size, MD5, image colour mode, text extractable.
Fixtures are in REPORT-68 test-cases/fixtures.
Owner decisions needed: none (behaviour matches existing copy).
