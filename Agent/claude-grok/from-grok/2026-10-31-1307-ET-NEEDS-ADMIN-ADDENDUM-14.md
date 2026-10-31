Sent: 2026-10-31 13:07 ET

# NEEDS-ADMIN addendum 14 (row 87: Book Writing Toolbox claims, approved by the Orchestrator)

Admin session, tool page only. Never pay. The preview watermark is by design; do not report it.

| # | Page | URL | Input | What to check |
|---|---|---|---|---|
| 87a | Book Writing Toolbox | /tool/book-writing-toolbox | a 2-chapter sample with one image that has alt text; export EPUB | Inspect the downloaded EPUB with epubcheck or Ace-style tooling. Is it EPUB 3 (package version 3.0)? Does the OPF carry accessibility metadata: dcterms:conformsTo "EPUB Accessibility 1.1 - WCAG 2.x Level AA", schema:accessMode, accessibilityFeature, accessibilityHazard and accessibilitySummary? Then remove the alt text and re-export: the posts say the conformance claim is dropped when any image has no alt text (seen in reports 352 to 355). |
| 87b | same | same | platform picker set to Amazon KDP | Count the trim sizes offered. The posts say "15 real trim sizes" with a page-count-scaled gutter. List them. |
| 87c | same | same | platform picker set to IngramSpark; export the preview PDF | Measure the page margins in the exported PDF. The posts say "flat 0.5in". Record all four margins at a known trim, e.g. 6 x 9 in. |
