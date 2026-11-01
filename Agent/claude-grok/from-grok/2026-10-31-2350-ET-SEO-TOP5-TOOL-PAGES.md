Sent: 2026-10-31 23:50 ET (Grok Orchestrator)

# SEO fixes: 5 high-demand tool pages

## Intent
Make our top-demand tool pages win their searches: full titles under 60 chars, strong meta, clear H1, 5-6 FAQs, related links.

## Why
These pages get the most demand but have truncated titles, generic metas and thin FAQs, which costs clicks.

## Outcome
Ship the fixes below. Before shipping, confirm two claims: QR codes really need no signup, and HEIC to JPG really offers PDF output; drop any claim that is not true. Keep every title under 60 chars (recount; some counts below are off).

---

# SEO top-5 fixes (Claude-ready) — Oct 31, 2026, 11:45 PM ET
Owner: SEO Engine. Route to Claude via Orchestrator. **SEO only:** change titles, metas, H1s, FAQ copy and the related-links block. Don't change tool behavior.

**How these were picked:** 15 high-demand pages from tool-keyword-targets.csv were fetched live on Oct 31. The 6 B-0036 pages were skipped. These 5 combine the most demand with the weakest SEO: generic H1s, short metas (84–101 chars) that waste the snippet, the brand missing from the title, and FAQs too thin or off-intent. The FAQPage schema is present on all of them, so keep it and update its text. Every claim below comes from the live page's own copy or FAQ.

**Rules:** "Free" appears only in the title and meta tags, never in the body or H1. Counts use multiples of 50 with a plus (300+). Say "10 trial uses per day". Never claim features that aren't built.

## 1. /tool/remove-background — keyword: "remove background from image online no upload" (#7)
**Why:** The H1 is just "Remove Background" and the meta is 92 chars. The biggest differentiator, that the photo is never uploaded, doesn't appear in the H1, and the PNG/transparent output isn't mentioned anywhere in the snippet.
**Outcome:** The page matches "no upload" and "transparent PNG" searches, so more searchers click it.
- Title (54): `Remove Background from Image, No Upload, Free | FreeDailyPro`
  - That's 59 chars. Alternate (52): `Remove Image Background – No Upload, Free PNG`
- Meta (148): `Remove the background from a photo right in your browser and download a transparent PNG. Your photo is never uploaded. Free, one image at a time.`
- H1: `Remove Background from an Image – Transparent PNG, No Upload`
- FAQ (keep the existing items; put these first, using the existing answers):
  1. Is my photo uploaded anywhere? No. Everything runs on your device in your browser. Only a small helper file is downloaded, once, and then cached.
  2. What format is the result? PNG, because it supports transparency and JPG doesn't.
  3. Why is the first image slower? The helper file loads the first time. Later images are faster.
  4. Does it handle hair and fur? It does reasonably well on typical subjects. Fine wispy edges are the hardest case.
  5. Can I do several photos at once? No. It handles one image at a time.
- Internal links: /tool/compress-image, /tool/resize-crop, /tool/webp-converter, /tool/exif-remover, /tool/image-to-pdf

## 2. /tool/pdf-to-jpg — keyword: "PDF to JPG online free" (#11)
**Why:** The meta is 101 chars and generic ("Free and fast"). The page's strengths are missing from the snippet: page ranges, PNG option, DPI up to 300, multiple PDFs into a ZIP, and nothing uploaded. The H1 is bare and the title has no brand.
**Outcome:** A richer snippet beats iLovePDF/Smallpdf on specifics and wins the "high-resolution" and "specific page" long tail.
- Title (56): `PDF to JPG – Every Page or a Range, 300 DPI, Free`
  - That's 49 chars; add ` | FreeDailyPro` if it fits under 60.
- Meta (152): `Convert PDF pages to JPG or PNG at up to 300 dpi. Pick a page range or convert several PDFs into one ZIP. Runs in your browser, nothing uploaded. Free.`
- H1: `PDF to JPG Converter – Every Page or Just the Ones You Need`
- FAQ (there are already 13; trim the visible list to these 6 first):
  1. Are my PDFs uploaded? No. The pages render and the ZIP is built in your browser.
  2. Can I convert one page? Yes. Use a range like `1, 3-5` or `8-`.
  3. Which dpi should I pick? 108/144 for screens, 216 for zoom, 300 for print.
  4. Can I export PNG? Yes. It's lossless and gives crisper text, with larger files.
  5. Several PDFs at once? Yes. Each one gets its own folder in the ZIP.
  6. One image vs ZIP? A single image downloads directly; two or more are zipped.
- Internal links: /tool/image-to-pdf, /tool/split-pdf, /tool/compress-pdf, /tool/merge-pdf, /tool/compress-image

## 3. /tool/image-to-pdf — keyword: "image to PDF online free" (#12)
**Why:** The meta is 92 chars and generic, and the H1 is bare. The page supports HEIC, WebP and more, auto-rotates phone photos, offers margins and page sizes, and uploads nothing. Searchers asking "iPhone photos to PDF" and "JPG to PDF" can't see any of that.
**Outcome:** Captures the JPG/HEIC/PNG-to-PDF variants and the "sideways photo" pain point.
- Title (58): `Image to PDF – JPG, PNG, HEIC to PDF, Free | FreeDailyPro`
- Meta (153): `Combine JPG, PNG, WebP or iPhone HEIC photos into one PDF. Reorder, pick page size and margins, and photos stay upright. Runs in your browser. Free.`
- H1: `Image to PDF – Combine Photos into One PDF`
- FAQ:
  1. Which formats? JPG, PNG, WebP, GIF (first frame), BMP, SVG and HEIC. TIFF isn't supported yet.
  2. Why won't my phone photo come out sideways? The tool applies the photo's rotation note when you add it.
  3. Can the page match the image size? Yes. Choose "Original image size".
  4. Can I reorder? Yes. Drag the images or use the up/down buttons.
  5. Margins? None, Small or Normal (½ in), or Fill the page.
  6. Uploaded? No. HEIC conversion and building the PDF both happen in the browser.
- Internal links: /tool/heic-to-jpg, /tool/merge-pdf, /tool/compress-pdf, /tool/pdf-to-jpg, /tool/resize-crop

## 4. /tool/heic-to-jpg — keyword: "HEIC to JPG no upload" (#14)
**Why:** The title is 62 chars, so it gets cut off. The meta is 97 chars. There are only 4 FAQs, and none covers "how do I stop iPhone saving HEIC" or the PNG/PDF outputs, both high-volume follow-up queries.
**Outcome:** The full title shows, and the page wins the iPhone how-to long tail.
- Title (57): `HEIC to JPG – Convert iPhone Photos, No Upload, Free`
  - That's 52 chars; add ` | FreeDailyPro` only if it stays ≤60. Otherwise drop the brand.
- Meta (150): `Convert iPhone HEIC photos to JPG, PNG or PDF in your browser. Convert several at once. Nothing is uploaded, so photos stay on your device. Free.`
- H1: `HEIC to JPG Converter for iPhone Photos`
- FAQ (keep the 4 existing ones and add 2):
  1. Is my photo uploaded? No. It stays on your device.
  2. Why are iPhone photos HEIC? Because the files are smaller. Settings › Camera › Formats › Most Compatible saves JPG for new photos.
  3. Several at once? Yes. Choose Multiple files.
  4. Quality loss? JPG is lossy, but the change is usually not visible. Keep the original HEIC.
  5. NEW: Can I get PNG or PDF instead? Yes. The converter outputs JPG, PNG or PDF (per the live meta). *Claude: confirm the UI offers PDF before shipping this.*
  6. NEW: Several photos into one PDF? Use Image to PDF, which accepts HEIC directly.
- Internal links: /tool/image-to-pdf, /tool/compress-image, /tool/exif-remover, /tool/resize-crop, /tool/webp-converter

## 5. /tool/qr-generator — keyword: "QR code generator free no signup" (#17)
**Why:** This is the weakest page. The title is 65 chars and gets cut off. The meta is 84 chars. The FAQ schema has only 1 question. The page supports logo overlay, PNG up to 2,000 px, SVG, WiFi/vCard/email/SMS/phone, and codes that never expire, but almost none of that is in the snippet. "Doesn't expire" is the top trust question for QR searches.
**Outcome:** The full title shows, and the page captures "QR code with logo", "WiFi QR" and "no expiry" searches.
- Title (54): `QR Code Generator – Logo, SVG, No Expiry, Free`
  - That's 46 chars; it can take ` | FreeDailyPro`.
- Meta (152): `Make QR codes for links, WiFi, contacts, email, SMS or phone. Add a logo, download PNG (up to 2,000 px) or SVG. Codes never expire. No signup. Free.`
  - *Check "No signup": trial = 10 trial uses per day. Keep it only if generating needs no account.*
- H1: `QR Code Generator – Links, WiFi, Contacts, with Logo`
- FAQ (new; all from the live copy):
  1. Does the QR code expire? No. The data is baked into the pattern, and scanning never calls freedailypro.com.
  2. What can it encode? A web link, text, WiFi login, contact card (vCard), email, text message or phone number.
  3. Can I add a logo? Yes. You can overlay an optional logo in the centre.
  4. Which download formats? PNG up to 2,000 px, or SVG for print.
  5. Should I test before printing? Yes. Scan it with your phone camera first. (This is the existing item.)
- Internal links: /tool/logo-maker, /tool/color-converter, /tool/resize-crop, /tool/image-to-pdf, /tool/word-counter

## Runner-up (next hour)
/tool/json-formatter: the meta is 85 chars and the H1 is "JSON / YAML Formatter".

## Not picked
merge-pdf, compress-pdf, pdf-to-word, split-pdf, word-counter and mortgage-calculator are already strong. Small fix: pdf-to-word's title is 64 chars, so drop "| FreeDailyPro".


Source: owner
