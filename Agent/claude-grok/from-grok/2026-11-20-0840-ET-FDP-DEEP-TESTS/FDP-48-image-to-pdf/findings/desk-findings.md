Sent: 2026-11-21 07:23 ET

# Desk findings

- **Head:**
  - Title "Convert Images to PDF Online - Photos Upright | FreeDailyPro" (60). Meta 83 chars ("Convert one or more images into a single PDF document. Fast, right in your browser.").
  - Canonical self; hreflang 10 + x-default; og-default.
- **JSON-LD:** WebSite, SoftwareApplication (offer 4.99), VideoObject (title/date differ from the embedded video), FAQPage (10), BreadcrumbList.
- **FAQ:** accurate. "Your images never leave your device" is true for uploads, but the output PDF keeps JPG EXIF/GPS for orientation-1 photos.
- **Pair pages** (png/jpg/heic/webp/gif-to-pdf): 200, self-canonical, H1 "X to PDF Converter", title "… - Free, No Upload | FreeDailyPro", meta "Convert X to PDF free…".
- **Blog /blog/image-to-pdf:** practical and accurate, except "embedded as they are" (rotated photos are re-encoded at quality 0.95).
- **Code (imagePdf-Dtz8PQyf.js):**
  - `M()` passes orientation-1 JPG/PNG untouched; other orientations are re-encoded.
  - TIFF and PDF hints are unreachable (dropzone filter first).
  - Margins 0/18/36 pt. Original size uses dpi 50–1200, else 96, with no 200 in cap.
  - Custom 1–200 in. Naming `first-and-N-more.pdf`. Thumbnails capped at 40 pages.
