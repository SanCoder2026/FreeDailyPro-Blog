Sent: 2026-11-21 13:02 ET

# Desk findings (FDP-61)

- **SEO:** title "Document Scanner - Scan to PDF Online | FreeDailyPro" (52). Meta 154. Canonical self. hreflang 10 + x-default. H1 "Document Scanner — Scan Paper to PDF". JSON-LD: SoftwareApplication (9.99 USD), VideoObject "How to Scan Documents from Photos Online" (2026-09-22), FAQPage (19), BreadcrumbList. In sitemap. og-default.png. Hero alt "Document Scanner preview".
- **Copy:**
  - FAQ "Does this automatically detect and straighten… No" contradicts the live auto corners and the FAQ "Why did the automatic corners land in the wrong place?".
  - Privacy "no engine is downloaded" contradicts the searchable-PDF FAQ.
  - How-to says "press Crop" (the button is Continue).
  - The rest is accurate: contrast 0–120 step 5 start 60, A4/Letter 18 pt margin, Fit 150 dpi, camera = file chooser, page reorder, ID card.
- **Code:**
  - `G("download")` gates PDF, PNG and searchable.
  - `le()` (Edit as Word/Excel) is not gated and navigates to `/tools/${t}`.
  - The upload handler applies an EXIF matrix (`Ze`, `Ke`) to `createImageBitmap(e, {imageOrientation: "none"})`, which leads to the double rotation.
  - Paper defaults from `navigator.language`.
  - The corner overlay `<svg>` has no size.
  - `nr()`/`pt()` log usage once per tool per load.
- **Blog (Sep 23 / Oct 15):** generic capture advice; points to Image to PDF for stacks and to two images for cards; "2 trial usages a day; $3 day pass or $9.99 monthly" (correct).
- **C06:** distinct. GSC data is not available.
