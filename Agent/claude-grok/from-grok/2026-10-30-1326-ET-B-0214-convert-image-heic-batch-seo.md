Sent: 2026-10-30 13:26 ET

# B-0214 Convert Image: HEIC input, batch ZIP, exact sizes in the result, and a title under 60
Priority: P2 · Estimated effort: M · Report: #129 · Source: Playwright headless 0 trial uses 1280/390 + curl server HTML + Google top-5 (WebSearch) 2026-10-30 ~13:22–13:27 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People converting an iPhone photo or a whole folder should get the format they need in one pass and understand the size change.
## Why (repro: g.png 658 B, PNG → JPEG 92%, 1280 px)
- Options: Convert to (JPEG default), quality, fill colour for transparency (clear warning ✓), and an "AVIF output isn't available in this browser" note (headless Chromium; good honest message). More options: size, turn, colour, details.
- Result: **"2 KB (original 1 KB). This is 3.8x larger"**. The ratio is right in bytes (658 B → about 2.5 KB) but contradicts the rounded labels, which read as 2×. Then "0 remaining today" (owner decision, fine).
- Unnamed controls: 11 (B-0155). Two file inputs plus "Take photo with camera".
- Top results (13:25 ET):
  - ImageMatrix: 53+ inputs including HEIC/video/PDF, batch ZIP.
  - Filesmith: batch, edit before convert, a "which format should you use" guide.
  - OneDropConvert: HEIC→JPG, 50 files, paste with Ctrl+V, removes location data.
  - Converti: 64 inputs including RAW/PSD, ZIP.
  - Fotor: batch.
## Who uses this
iPhone users (HEIC), web publishers (WebP/AVIF), people uploading to forms that need JPG.
## Outcomes (ranked)
1. Accept HEIC/HEIF input (needs a browser check of whether it works today). It's the top real-world need.
2. Batch: many files → one ZIP, the same settings for all.
3. Show exact sizes under 10 KB in bytes ("658 B → 2.5 KB, 3.8× larger") so the numbers agree.
4. Paste from the clipboard; a "which format should I use" helper (photo → JPG/WebP, logo → PNG/WebP, web → AVIF).
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, FAQPage, BreadcrumbList, VideoObject), full OG/Twitter set. The site-wide items (og-default.png, template/footer H2s, the boilerplate meta "Free and fast, right in your browser.", empty video alt, unrelated nav category links) are covered by **B-0209**. English on locale pages → **B-0123**.
  - **Title "Convert Image Format Online - JPG, PNG, WebP Free | FreeDailyPro" is 64 chars (over 60).**
  - Meta 136 (just short; ends with the boilerplate).
  - H1 "Convert Image Format" (ok). /es is English (B-0123).
- **Best result:** H1 "Free Online Image Converter"; lists the formats it supports; "HEIC to JPG" sub-pages; FAQ "Can I convert without uploading?", "Convert vs compress?".
- **Suggested:**
  - Title: `Image Converter – JPG, PNG, WebP, HEIC & AVIF | FreeDailyPro` (59) — only if HEIC ships; otherwise `Image Converter – JPG, PNG, WebP, AVIF Online | FreeDailyPro` (59)
  - Meta: `Convert images between JPG, PNG, WebP, AVIF, GIF, BMP, ICO and TIFF. Resize, rotate and set quality as you go. Your photos stay on your device.` (143)
  - H1: `Image Converter – Change JPG, PNG, WebP and More`
  - FAQ:
    - "How do I convert PNG to JPG?" → "Choose JPEG, set the fill colour for transparent parts, then Convert."
    - "Why is my JPG bigger than the PNG?" → "Small, flat graphics compress better as PNG or WebP."
    - "Is my image uploaded?" → "No."
## Constraints
Keep the honest AVIF and transparency notes.
## Test cases
1. Title is 60 chars or fewer.
2. 658 B PNG → result line in bytes and KB that agree with the ratio.
3. 3 files → one ZIP with 3 converted files.
