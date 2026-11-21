Sent: 2026-11-21 11:31 ET

# Desk findings (FDP-57)

- **Code:**
  - Drop zones use `gateAtDownload: true`.
  - Assembly (`bookAssembly.ge`) runs with no gate; the D (download) component charges.
  - .docx goes through `docxRead` + `docxToPdf`; .txt is forced to A4.
  - Images go on A4 with 36 pt margins, no upscale.
  - Forms are flattened (`getForm().flatten`).
  - Encrypted PDFs are handled at add time (unlock dialog).
- **FAQ (9):** accurate. 17 page sizes confirmed in code (15 trims + Letter + A4). Bookmarks and links behave as described.
- **Tips:** "Front pages … numbered with roman numerals": not true in output.
- **Limitations:** "stops … with an error naming it": the image error is unnamed.
- **SEO:**
  - Title "Combine PDF, Word & Images Into One PDF | FreeDailyPro".
  - Meta "Combine PDFs, Word files and images into one document with a cover page, an automatic table of contents and real page numbers. Reorder freely; runs in-browser."
  - Canonical self. JSON-LD: WebSite, SoftwareApplication, VideoObject ("How to Combine PDF Word & Images into One Document"), FAQPage 9, Breadcrumb.
- **Blog /blog/document-assembler** (Oct 17, 2026): good walkthrough. Wrong: "Each assembly counts toward your 2 trial usages" and "check the preview". The second Guides link is a catalog-series post.
- **C10:** keep. merge-pdf is the plain path; mail-merge-pdf is a different job.
- GSC data is not available.
