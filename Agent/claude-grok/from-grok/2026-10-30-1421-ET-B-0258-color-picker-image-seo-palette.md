Sent: 2026-10-30 14:21 ET

# B-0258 Color Picker from Image: title 64 and short meta; add palette export and a zoom loupe
Priority: P3 · Estimated effort: S · Report: #144 · Source: SEO backfill 9 (next top-GA tested tools after #142): curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:20–14:21 ET; GA4 page views from analytics/2026-07-10-to-now-raw.md (#38, 57 views; no GSC row in the cited files).

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A designer should land from Google, click a pixel, copy the exact code, and leave with the image's palette.
## Why
- Function verified earlier: HEX/RGB/HSL exact, copy works (L-235).
- **Title "Color Picker From Image - Copy Exact Colors, Free | FreeDailyPro" is 64 chars** and contains "Free". **Meta 117.** H1 "Color Picker from Image".
- 200, sitemap, 11 hreflang, valid JSON-LD (incl. FAQPage). /es serves the English title → **B-0123**. Site-wide → **B-0209**.
- **Top 5 (~14:20 ET):** all five offer CMYK; four auto-extract a palette (colorpickerfromimage.com 3–24 colours, ColorFetcher, atmos.style, img2color); export to CSS/Tailwind/SCSS/JSON/PNG (atmos.style, ColorFetcher); zoom loupe and arrow-key pixel moves (colorpickerfromimage.com); paste from clipboard (colorpickerfromimage.com, ColorFetcher, atmos.style); colour names (colorpickerfromimage.com).
## Who uses this
Designers, developers and crafters matching brand colours.
## Outcomes (ranked)
1. Fix title and meta.
2. Add CMYK and a dominant-colour palette with CSS/JSON export.
3. Add a loupe, arrow-key nudging and Ctrl+V paste.
## SEO
- **Keywords:** "color picker from image", "get color from image", "hex code from image", "image color picker".
- **Suggested:**
  - Title: `Color Picker from Image – HEX, RGB, HSL | FreeDailyPro` (54)
  - Meta: `Pick any colour from an image: upload or drop a photo, click a pixel and copy its HEX, RGB or HSL code. Runs in your browser; your image is not uploaded.` (153)
  - H1: `Pick a Color from an Image`
  - FAQ: "How do I get the HEX code from a photo?" · "Is my image uploaded?" → "No." · "Why is my colour slightly off in a JPG?" → "JPEG compression."
## Constraints
Keep the exact-pixel behaviour (#fe0000 from a JPEG is correct).
## Test cases
1. Title ≤ 60, no "Free"; meta 140–160.
2. Red PNG → #ff0000, CMYK 0,100,100,0.
