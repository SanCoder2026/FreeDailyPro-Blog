Sent: 2026-11-21 22:51 ET

# FDP-87 desk findings

- **Page claims (tool-expanded.txt) and the result of each check:**
  - Text, picture pixels, drawings and form fields under boxes are removed, including invisible text: **verified**.
  - Pictures are repainted and re-encoded: **verified**.
  - Links, notes and form fields under a box are removed: **verified**.
  - Thumbnails and alt text are dropped on marked pages: **verified**.
  - Old versions are deleted: **verified**.
  - Unmarked pages are not touched: **true except for the trial mark** (P3).
  - The comment option removes all comment annotations plus links, form values and bookmarks that match: **verified** (the outline was removed, and the R07 note on an unmarked page was removed).
  - The metadata option clears Info + XMP: **verified**.
  - Scanned PDFs get a message: **verified**.
  - The rasterize notice: **verified**.
  - The empty-area warning: **verified**.
  - Attachments are counted, not removed: **verified** (P2 gap).
- **Detector regexes (redactSearch):**
  - email `[\w.+-]+@[\w-]+(?:\.[\w-]+)+`.
  - phone: 10 digits with an optional country code.
  - card: 13–19 digits with spaces or dashes. **No Luhn check**, so any long number such as an order ID will be marked. It is a review step, so acceptable; noted.
  - ssn `\d{3}-\d{2}-\d{4}` and ein `\d{2}-\d{7}` (dashed only).
  - name: nameDetect, a list of ~300 first names plus title and label cues.
- **Gate:** the result DownloadButton has no key (per-load P1). The summary .txt uses `{ free: !0 }`. The dropzone uses `gateAtDownload` (Apply at 0 is allowed by design).
- **JSON-LD:** WebSite, SoftwareApplication (Offer 4.99), VideoObject and FAQPage are valid. The VideoObject name differs from the YouTube title.
- **Links:** the next step is Add Password to PDF, and there is an AI PDF Redactor link. There are no links to Redact PowerPoint or Blind CV Redactor.
