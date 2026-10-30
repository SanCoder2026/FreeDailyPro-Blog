Sent: 2026-10-30 15:45 ET

# B-0303 Bulk Image: WebP output larger than the input, title over 60
Priority: P3 · Estimated effort: S · Report: QA-REPORT-159 · Source: live probe 2026-10-30 ~15:42-15:44 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A "compress" run should never hand back bigger files without saying so.

## Why
No GSC row in the analytics raw file for this page.
Checked live (15:44 ET): three 800×600 PNGs (2,786 B each) → WebP at default quality 80 → bulk-processed-images.zip with in0/in1/in2.webp, each 800×600 WebP ✔, but 6,270–6,370 B, about 2.3× the input size.
Whether the page warned that files grew: unverified absence (result screen text not captured); admin to check.
Formats offered: PNG, JPEG, WebP, AVIF ("not available here" in headless Chromium), GIF, BMP, ICO, TIFF; More options for size, turn, colour, details.
Competitors (live search): CompressUp skips a file when the result would be larger; Compresso shows per-file and total savings; MakerBox compresses to a target KB size.
Title 65 (over 60, has "Free"); meta 160 has "Free". /es title English → L-189. Ad text ("Find Stock Photos", "Earn a CS Degree") → L-004.

## Who uses this
Site owners and sellers converting a folder of images.

## Outcomes (ranked)
1. Show before/after size per file and total; when output is larger, keep the original (or warn).
2. Snippet as below.
3. Optional target file size.

## SEO
- Now: title "Compress or Convert Multiple Images at Once - Free | FreeDailyPro" (65, has Free); meta 160 (has Free); H1 "Bulk Compress & Convert"
- Keywords: bulk image converter, batch image compressor, convert multiple images to webp, bulk resize images
- Suggested Title: "Bulk Image Converter & Compressor (ZIP) | FreeDailyPro" (54)
- Suggested Meta: "Convert and compress many images at once to WebP, JPEG, PNG, AVIF, GIF, TIFF, BMP or ICO, resize or rotate them, and download every file in one ZIP." (148)
- Suggested H1: keep
- FAQ: Can I convert to WebP in bulk? · Why is a file bigger? · Is anything uploaded? · How many images at once?

## Constraints
Keep everything on the device; one ZIP per run.

## Test cases
1. Three 800×600 PNGs → WebP → ZIP of 3 WebP at 800×600 (regression).
2. Flat-colour PNG whose WebP is larger → original kept or a "bigger than original" note.
3. Result list shows sizes before and after.
4. AVIF in desktop Chrome → .avif files.
5. Title ≤60, meta 140–160; 390 px no overflow.
