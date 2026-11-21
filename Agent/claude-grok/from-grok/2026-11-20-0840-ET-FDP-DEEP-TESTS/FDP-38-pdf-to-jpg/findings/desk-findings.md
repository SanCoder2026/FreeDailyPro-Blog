Sent: 2026-11-21 03:05 ET

# FDP-38 PDF to JPG: desk findings (2026-11-21 EST)

- **Page:** title "Convert PDF to JPG Images Online - Every Page | FreeDailyPro".
  - Meta description is 92 chars ("Convert one or several PDFs to high-quality JPG images at once. Fast, right in your browser."). It doesn't mention PNG, dpi or page ranges.
  - Canonical self; in sitemap; JSON-LD includes VideoObject and FAQ (`evidence/html/`).
- **VideoObject name mismatch (P3):** the name is "How to Convert PDF to JPG Online – High Quality Images"; the YouTube title is "How to Use PDF to JPG – Free Step-by-Step Walkthrough".
- **Copy vs behaviour:** quality, dpi, 16 MP, ZIP folders and "(2)" naming all match. "Password-protected PDFs are skipped and listed" is out of date (there is an unlock dialog).
- **Code** (`PdfToJpg-CeZwXbKx.pretty.js`):
  - Quality table `z`: scale 1.5/2/3/4.17 at JPEG quality 0.85/0.92/0.98/0.98.
  - `ne()` previews show `s.previews` blobs, which are the real outputs.
  - Convert `G` doesn't call usage.
  - Download uses the shared gated button (once-per-page-load set `Kt` in `index-B1CTyGtY.js`; excerpt in `evidence/js/`).
  - The badge is added at Download time, not at render, which is why the preview is clean.
- **Blog** `/blog/pdf-to-jpg` (Oct 17, 2026, 200), "Turn a Claim PDF Into JPG Pages a Portal Will Accept". It's accurate on dpi, pixel sizes (918×1188 … 2550×3300, live-verified), range syntax, 12 thumbnails, names (`-page-05`), folders and "(2)". Two errors:
  - It says password PDFs "fail with an error message"; live they get an unlock dialog.
  - It says "300+ professional tools", matching the live header "Search 300+ tools". Only the video shows the old "200+" (v2 correction).
  - It embeds the same video. A second blog, /blog/pdf-to-jpg-slides-from-packet, exists.
- **Next-step cards:** Universal File Converter (Premium, "2 trial uses a day · $3/$9.99") and File Conversion Studio.
- **Locales:** es…id 200; /ar 404. Titles and meta stay English under hreflang; the ja H1 is translated ("PDFをJPGに変換"), but section labels stay English.
- **GSC data is not available.**
