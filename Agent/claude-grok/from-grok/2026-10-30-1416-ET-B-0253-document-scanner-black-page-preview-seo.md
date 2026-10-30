Sent: 2026-10-30 14:16 ET

# B-0253 Document Scanner: fix the all-black output, show a preview before the gate, add OCR and multi-page; real meta
Priority: P1 · Estimated effort: M · Report: #142 · Source: SEO backfill 8, curl server HTML + seo.py + Google top 5 (WebSearch), 2026-10-30 ~14:15–14:16 ET. Already tested (L-234). GA rank 36, 59 views (`analytics/2026-07-10-to-now-raw.md`); no GSC row in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone photographing a form should get a clean, readable multi-page PDF, and see the cleaned page before paying.
## Why
- **Open bug L-234 (admin session): a solid blue page turns into an all-black PDF with default Grayscale + Remove shadows** (pypdf/pdftoppm confirmed). A scanner that can output a black page shouldn't be promoted until fixed.
- L-234: Premium ($3/$9.99, 2/day); at 0 trial uses the paywall comes before any preview.
- Title "Scan a Document With Your Phone Photo Online | FreeDailyPro" (59) — clumsy wording. **Meta 97.** H1 "Document Scanner".
- **Top 5 offer (~14:16 ET):** automatic edge detection with draggable corners and loupe (Scannr, Scanner.cam); filters Magic Color / Grayscale / B&W (Scannr, Scanner.cam); multi-page with reorder/rotate/retake (Convertful, Scanner.cam); A4/Letter page size (Scannr, Scanner.cam); searchable OCR PDF (SafePaper, Scanner.cam); compression and EXIF/GPS strip + redaction (SafePaper). All are free with no gate.
## Who uses this
People sending a signed form, receipt or ID from their phone.
## Outcomes (ranked)
1. Fix L-234: filters never turn a page fully black (clamp threshold; fall back to Original).
2. Show the cleaned preview at 0 trial uses; gate only the download (owner's decision on the gate itself).
3. Multi-page with reorder; A4/Letter.
4. Searchable OCR option.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD; → **B-0209**; /es English → **B-0123**.
- **Keywords:** "document scanner online", "scan to pdf", "scan document with phone", "camscanner alternative".
- **Suggested:**
  - Title: `Document Scanner – Scan to PDF Online | FreeDailyPro` (52)
  - Meta: `Scan a document with your phone or webcam: crop and straighten the page, clean up shadows, and save a PDF. Works in your browser with no app and no upload.` (155)
  - H1: `Scan Documents to PDF With Your Phone`
  - FAQ: "Can I scan several pages?" (once built) · "Is it a CamScanner alternative?" · "Are photos uploaded?" → "No."
## Constraints
Don't claim OCR or multi-page until shipped.
## Test cases
1. Admin: solid blue photo, defaults → PDF page is not all black (mean pixel > 30).
2. Fresh session at 0 trial uses: cleaned preview visible before the gate.
3. Title ≤ 60; meta 140–160.
