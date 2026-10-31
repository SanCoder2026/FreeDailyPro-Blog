Sent: 2026-10-31 00:24 ET

# B-API: Add image-to-PDF, OCR/invoice extraction, and HEIC input to the API

## Intent
Santosh's rule is that we never put incomplete tool info in front of anyone outside. When we tried to answer real developer questions on Reddit (r/apyhub: "best API for images to PDF" and "scanned invoices"), we couldn't point people to FreeDailyPro because the API is missing these three capabilities. ApyHub and its competitors already offer them. Following Rule 1, close these gaps so we can promote complete, best-in-class endpoints.

## Gaps (found Oct 31 against the live API)
1. **No image-to-PDF endpoint.** The web tool /tool/image-to-pdf exists, but the API doesn't expose it.
2. **No OCR or scanned-invoice extraction.** There's no text extraction for image-only PDF pages or images.
3. **HEIC input is rejected** by the image convert endpoint, which returns a 400. iPhone photos are HEIC by default.

## Outcomes we want
- **image-to-PDF:** multiple images in, one PDF out. It should:
  - auto-rotate using the EXIF orientation;
  - flatten transparency onto a chosen background;
  - offer page-fit options (page = image size, or A4/Letter with margins, handling mixed portrait and landscape);
  - let the user set the DPI.
- **OCR:** for images and PDFs. It should skip pages that already have a text layer and return text with page numbers. It would be good to also return invoice fields: vendor, date, totals and currency.
- **HEIC/HEIF:** accepted wherever images are accepted.
- **Discovery:** expose all three as MCP tools as well, with clear descriptions (good for TDQS) and documentation on the /developers page.
- **Fallback:** if any of these isn't feasible, tell me why and what you'd suggest instead.

Once these are live, the Testing Bot will verify them, and then we'll promote them.

Source: owner
