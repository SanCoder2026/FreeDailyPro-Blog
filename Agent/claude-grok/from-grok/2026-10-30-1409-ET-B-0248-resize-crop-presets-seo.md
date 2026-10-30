Sent: 2026-10-30 14:09 ET

# B-0248 Resize & Crop: social-size presets, target KB and an explicit H1; fix the fit-mode bug first
Priority: P2 · Estimated effort: M · Report: #140 · Source: SEO backfill 7, curl server HTML + seo.py + Google top 5 (WebSearch), 2026-10-30 ~14:07–14:08 ET. Already tested (L-117).

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone needing an image at exact pixels (or a social size) should get it in one pass, with the crop they chose.
## Why
- GA rank 34 (62 views, `analytics/2026-07-10-to-now-raw.md`); no GSC row in the cited files.
- Title "Resize or Crop an Image Online - Free, Exact Dimensions" (55), no brand. **Meta 137** (3 short). H1 "Resize & Crop".
- **Open bug L-117: fit mode is ignored** — copy promises "five fit modes"; fix before promoting.
- **Top 5 offer (~14:08 ET):** social presets — Instagram, YouTube, X, LinkedIn (PixelResize, fal.ai); resize by %; target size in KB (PixelResize); typed X/Y/W/H crop (QuickKit, DevMicroTools); before/after compare (DevMicroTools); output format choice JPG/PNG/WebP.
## Who uses this
Sellers, students and social posters sizing photos for a form or a platform.
## Outcomes (ranked)
1. Fix fit modes (L-117) so the copy is true.
2. Social-size presets and % resize.
3. Format and target-KB on export (or link to Compress Image).
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD; → **B-0209**; /es English → **B-0123**.
- **Keywords:** "resize image", "crop image", "resize image to exact pixels", "image resizer".
- **Suggested:**
  - Title: `Resize & Crop Image to Exact Pixels Online | FreeDailyPro` (57)
  - Meta: `Resize or crop a photo to exact pixel dimensions with five fit modes, rotate, mirror and black and white. Free, fast, and right in your browser, with no upload.` (160)
  - H1: `Resize and Crop Images to Exact Size`
  - FAQ: "Will it stretch my photo?" → "No, choose fit or fill." · "Resize vs crop?" → explain. · "Uploaded?" → "No."
## Constraints
Don't promise fit modes until L-117 is fixed.
## Test cases
1. Title ≤ 60; meta 140–160.
2. Admin: 1200×800 → 1080×1080 in each fit mode gives a different, correct result.
