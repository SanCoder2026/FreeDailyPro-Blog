Sent: 2026-10-30 13:34 ET

# B-0221 PDF to JPG: show the pixel size for each quality, add WebP, and an H1 that says what you get
Priority: P2 · Estimated effort: S · Report: #131 · Source: Playwright headless 0 trial uses 1280/390 + curl server HTML + Google top-5 (WebSearch), 2026-10-30 ~13:30–13:36 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People turning PDF pages into images should pick the right quality without guessing and get sharp, well-named files.
## Why (repro: p.pdf, 3 A4 pages; default settings; 1280 px; 0 trial uses)
- Options: Quality (Standard 108 / High 144 / Maximum 216 / Print 300 dpi), Format JPG/PNG, Page range.
- Convert → "3 pages converted to JPG", a per-page list (`p-page-01.jpg 1190 × 1683 px · 14.6 KB` …) and `p-images.zip`. Download gated (owner decision).
- 1190 × 1683 is A4 at 144 dpi, so High is the default ✓, but the UI doesn't mark it as the default.
- Injected ad text "Compare Browsers", "Upgrade Monitors" and "Try Cloud Tools" → L-004. 9 unnamed controls → B-0155. No overflow.
- Top results (13:33 ET):
  - XConvert: 72–1200 DPI with pixel examples.
  - PDFBetter: pick pages from thumbnails, shows the first page's pixel size.
  - KivaroTools: JPG/PNG/**WebP**.
  - ClearConvert: JPG quality 85/95/100%, page limit stated, a message for password-protected PDFs.
## Who uses this
People posting a page to social media, putting slides into a deck, or uploading a document as an image.
## Outcomes (ranked)
1. Show the first page's pixel size next to each quality option ("High · 144 dpi · 1190 × 1684").
2. Mark the default and say what each level is for (screen / print).
3. WebP output and a JPG quality setting.
4. Say what happens with a password-protected PDF, with a link to Unlock PDF.
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD, full OG/Twitter set. The site-wide items (og-default.png, template/footer H2s, short boilerplate-style metas) → **B-0209**. **/es serves the English title** → **B-0123**.
  - Title "Convert PDF to JPG Images Online - Free, Every Page" (51, no brand, "Free" in the title).
  - **Meta is 101 chars.**
  - H1 "PDF to JPG" (bare).
- **Best result:** H1 "Convert PDF to JPG", DPI explained with pixel examples, file naming stated, and a "Will the text still be selectable?" FAQ.
- **Keyword gaps:** "pdf to jpg high quality", "pdf to image", "pdf to png", "pdf to jpg 300 dpi".
- **Suggested:**
  - Title: `PDF to JPG – Convert PDF Pages to Images | FreeDailyPro` (55)
  - Meta: `Turn every page of a PDF into a sharp JPG or PNG at up to 300 dpi. Pick a page range and get one ZIP with numbered files. Your PDF never leaves your device.` (156)
  - H1: `PDF to JPG – Convert PDF Pages to Images`
  - FAQ:
    - "Which quality should I pick?" → "High (144 dpi) for screens, Print (300 dpi) for printing."
    - "Can I convert only some pages?" → "Yes. Type a range like 1-3, 5."
    - "Will the text be selectable?" → "No. A JPG is a picture; keep the PDF for searchable text."
    - "Is my PDF uploaded?" → "No."
## Constraints
Keep the per-page result list.
## Test cases
1. Each quality option shows its pixel size.
2. WebP selected → .webp files in the ZIP.
3. Meta is 140–160 chars.
