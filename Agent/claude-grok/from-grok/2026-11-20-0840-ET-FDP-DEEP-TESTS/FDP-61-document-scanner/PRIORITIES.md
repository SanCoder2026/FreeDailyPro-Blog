Sent: 2026-11-21 14:11 ET

# FDP-61 Document Scanner: priorities (2026-11-21 EST, -v3)

> **-v3 (2026-11-21 13:37 EST): supersedes -v2.** Puts "full-resolution scan preview at 0 trial uses" back as an **Owner question** (not P1), per the Orchestrator at Nov 21 1:19 PM: Santosh hasn't ruled on full-quality results/previews at 0 uses. Everything else is unchanged from the original report.

| Pri | Item | Evidence | Why it matters | Suggested fix |
|---|---|---|---|---|
| P1 | Edit as Word / Edit as Excel open a 404 (`/tools/image-to-word`, `/tools/image-to-excel`) | zero.json Z08, misc.json; Z08-word-handoff.png, Z09-excel-handoff.png | Advertised next step (FAQ) dead-ends; user loses the scan | Route to `/tool/…`; confirm the "scan-convert" handoff loads the pages; decide whether the handoff takes a trial use |
| P1 | EXIF-rotated phone photos (Orientation 6) come out sideways, on all 3 engines | orient.json, orient-*.png, msgs M05 | Many phone JPEGs carry EXIF rotation; first scan looks broken | Don't re-apply the EXIF matrix on top of `createImageBitmap` (already oriented); test 3/6/8 |
| P1 | One trial use per page load: after the first download, new scans download free with no cap until reload | perload.json P2–P4 at 2/2, P5 capped after reload; leftB B05/B06 | Owner rule (Nov 21): per-page-load charging is a gate gap; 2-a-day Premium becomes unlimited per tab | Charge once per new result (same scan's PDF/PNG/searchable stay one use) |
| P2 | FAQ says no automatic edge detection; privacy says no engine downloaded; how-to says "press Crop" | tool-expanded.txt; straighten-handles.png | Undersells the best feature; contradicts the OCR FAQ | Rewrite the 3 lines |
| P2 | Video fILxNjJP3ZY shows the old one-step tool, removed modes, "10 free uses daily", "Free" title/description, "PDF tools" tag, browser chrome | video/sheet.png, crop-frames.png, info-min.json | Shows a weaker tool than users get; "free" wording | Re-record the 5-step flow, multi-page, ID card, searchable PDF; Premium / trial-use wording |
| P2 | Drop zone below the fold on 1366×768 (hero + steps); hero shows filters the tool doesn't have | devices/desktop-1366x768-chromium-full.png | Visitors must scroll to start; mismatch with the real UI | Smaller or later hero; drop zone first |
| Owner question | Full-resolution scan preview at 0 trial uses; only files are gated (not a file save) | zero.json Z01/Z05 | Pending owner ruling on results/previews at 0 (Orchestrator, Nov 21 1:19 PM); same pattern as FDP-50/51 | Owner call: keep, or watermark/scale the preview at 0 |
| P2 | Locale pages: subtitle, Premium line, pass labels, breadcrumb and all controls in English | locales/*es*, *ja* screenshots | Mixed-language page | Translate tool strings (site-wide) |
| P2 | One photo per pick; no auto colour; no size choice; grayscale stored as RGB | misc.json camera `multiple:false`; pdfimages | Competitors (Adobe Scan, Genius Scan) import batches | Allow multi-select into the page list; add an "Auto" enhance; grayscale JPEG |
| P3 | Corner overlay SVG clipped to ~300×150 | straighten-handles.png, mobile-straighten-webkit.png | Looks broken while handles are right | Size the SVG to the image |
| P3 | Corner handles not keyboard reachable (tabIndex -1, no role/label) | misc.json handles | A11y | Focusable handles, arrow keys |
| P3 | Not-an-image file → empty Crop box, no error | orient.json, M08 | Confusing | Error toast, stay on step 1 |
| P3 | Stale "trial uses are used up" status after a cap dialog persists through later steps | zero.json Z07 | Noise | Clear on new photo |
| P3 | ID PDF named `_2pages.pdf` though one page; Up/Down shown for the single front | idcard-firefox.json, I01-after-front.png | Polish | `_id-card.pdf`; hide reorder in ID mode |
| P3 | Counter jumps 0→2 after one download in some fresh contexts (server pooling, observation) | leftB B03, perload P1 | Shared networks may see "2 remaining" then 0 | Owner awareness |
| P3 | Blog recommends Image to PDF and two images for cards | curl/blog.txt | Built-in features unmentioned | Update the blog |
| P3 | axe: label-content-name-mismatch (serious), region; Pixel 7 ad-caption contrast; iPhone SE 9 px / ja 3 px overflow | matrix-results.json | A11y polish | Fix label and caption colour (keep reserved ad slots); header overflow site-wide |
