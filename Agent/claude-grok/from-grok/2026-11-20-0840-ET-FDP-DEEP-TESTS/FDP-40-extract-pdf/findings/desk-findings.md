Sent: 2026-11-21 03:27 ET

# FDP-40 Extract Pages & Text: desk findings (2026-11-21 EST)

- **Page:**
  - Title "Extract Pages or Text From a PDF | FreeDailyPro".
  - Meta description 82 chars: "Pull specific pages or the text content out of a PDF. Fast, right in your browser." Thin: no mention of typed order, odd/even, bookmarks/forms, tables to tabs.
  - Canonical self; in sitemap.
  - JSON-LD: SoftwareApplication, VideoObject ("How to Extract Specific Pages or Text from PDF Online"; YouTube title "How to Use Extract Pages & Text – Free Step-by-Step Walkthrough"), FAQPage 13.
- **Copy vs behaviour:**
  - Accurate: markers, tabs, two-column order, typed order, odd/even, error messages, scanned notice.
  - Stale:
    - (a) How-to "all of them by default": the box is pre-filled with "1", so text mode gives page 1 only.
    - (b) Limitations "A password-protected PDF cannot be opened for either mode": the shared unlock dialog opens it.
- **Code** (`ExtractPdf-C5BRKXT9.pretty.js`):
  - The file loader sets the box to "1" and the selection to {1} (`L`).
  - Text output goes into a `readOnly` textarea (selectable).
  - Copy `G` → `gateShare`.
  - Download → shared `D` button.
  - Extract `q` has no usage call.
  - Pages preview → ToolPage `R` (`Al`): "Preview first page" at scale 0.8.
- **Blog: none.** `/blog/extract-pdf` (and likely variants) are 404 and there's no extract post in the sitemap. "Guides and next steps" links /blog/pdf-to-excel and /blog/pdf-to-jpg, which only mention the tool.
- **Duplicate group C09:** split-pdf (#5), crop, remove-pages, rotate, organize. Extract overlaps Split (one range) and Remove Pages (inverse). The copy explains the Split difference well. Text extraction is unique in the group. Keep it, and cross-link Remove PDF Pages.
- **Locales:** es…id 200 with translated H1; title/meta English; /ar 404.
- **GSC data is not available.**
