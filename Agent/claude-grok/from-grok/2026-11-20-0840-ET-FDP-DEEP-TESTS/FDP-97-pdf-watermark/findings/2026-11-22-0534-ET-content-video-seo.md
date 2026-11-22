Sent: 2026-11-22 05:35 ET

Sent: 2026-11-22 05:34 ET

# FDP-97 content, video and SEO findings

## Page text (tool-expanded.txt)
- Limitations: "Every page gets the stamp, with no page-range option, and it is drawn on top of the content rather than behind it." **Wrong**: Pages box (W08 `2-5, 8`), Skip the first page (W09) and Layer "Behind page content" (W08, W10) all work.
- When not to use: "This tool also stamps every page, so it cannot mark only a chosen section of the document." **Wrong** (same evidence).
- FAQ "Which image formats…": "TIFF is refused with a message asking you to convert it." The toast says only "Failed to add watermark"; the message is in the console (I04).
- FAQ "Can I remove a watermark…": see strip-demo.md.
- FAQ has 14 items with three duplicate pairs (Tiled ×2, copying ×2, language ×2); FAQPage JSON-LD carries all 14.
- Correct and verified: angle 0–90 and reset rule, 5–100 % opacity, EXIF straightening, WebP/GIF/SVG conversion, batch 5 on trial, in-browser privacy, non-Latin drawn as a picture (but the note also shows for Hindi, which is real text, and says "Latin-alphabet text is added as real text", false for mixed labels such as `🔒 SECRET` / `Entwurf № 3`).

## Blog
- /blog/pdf-watermark: "Colour: a light grey (#b3b3b3) to begin with" and "Opacity: 30 percent by default". Live default: #808080, 40 %.
- "Splitting before you stamp … cut them out with Split PDF, stamp that piece" – unnecessary; the tool has a Pages box and Skip first page.
- No mention of "Behind page content" or image tiling.
- /blog/stamp-bates-numbers-across-pdf-set: links here appropriately; no errors found for this tool.

## Video (YouTube g65Ab2hXV-I)
- 1:46, uploaded 2026-09-30 00:14 ET, 8 views at test time. Title/description say "Free".
- Shows an older dark UI with only a "Watermark Text" field, "5 free uses remaining", recorded on a Windows desktop; the watermarked PDF is never opened on screen.
- Missing: image/logo, position, tiling, layer, page range, batch.
- VideoObject JSON-LD: uploadDate 2026-08-22 and a different name from the YouTube title; no duration.

## SEO / indexing
- Title "Add a Watermark to a PDF Online - Mark as Draft | FreeDailyPro"; meta description 71 chars (short); canonical self; hreflang ×10 + x-default; /ar → 404 (sitewide).
- JSON-LD: SoftwareApplication (Offer 4.99 USD/MON), VideoObject, FAQPage (14), BreadcrumbList. OG image = site default.
- Locales de/ja: H1 and breadcrumb translated; strapline, drop zone, controls, hints, title and meta in English.

## Matrix / accessibility
- iPhone SE: +9 px horizontal scroll (button, sitewide). Other devices fine; iPhone 13 Chromium/WebKit 390 = 390.
- axe desktop: `label-content-name-mismatch` (serious, `.right-2`), `region` (moderate). Pixel 7: `color-contrast` on the ad label text (label contrast only).
