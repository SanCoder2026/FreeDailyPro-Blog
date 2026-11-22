Sent: 2026-11-22 01:18 ET

# FDP-92 Crop PDF: what the crop really does (owner questions 1–5)

All outputs re-read with pikepdf (raw page boxes), pypdf (whole text layer), PyMuPDF (text clipped to the visible CropBox) and PDFium (the text layer Chrome uses for find / copy), and rendered with PDFium. "Region match" = the output page rendered vs the original page rendered and cut at the expected share of the page (mean abs grey diff, trial-mark corner ignored). See json/verify-*.json and screens/*-exp-vs-got.jpg (left half expected, right half got).

## 1. CropBox only, or real removal? **CropBox only.** The page says so, clearly.

- Code: `operations` `mn()` loads the original with pdf-lib and calls `page.setCropBox()` on each chosen page. Nothing else: content streams, images, fonts, annotations, form fields, bookmarks and the MediaBox/TrimBox/BleedBox/ArtBox are untouched.
- Output (A01, doc.pdf, 1.5 in all round): CropBox [108 108 504 684] on all 3 pages, MediaBox unchanged. "OUTSIDE-SECRET-1" (header strip) and "OUTSIDE-FOOTER" are **gone from view** (MuPDF clipped text: false) but **still in the file** (pypdf: true) and **still in PDFium's text layer** (true): Chrome's find bar and Select-all/Copy can still reach them.
- The page states it in 5 places: FAQ "What's the difference between this and Redact PDF?" ("Crop only changes each page's visible boundaries (its CropBox)… software that ignores crop boxes can still get at it"), FAQ "Is the cropped content deleted? No…", FAQ header/footer answer, Details "When not to use it" / "Limitations", and a note under the result after every crop ("Cropping only hides what is outside the box; that content is still inside the file. To remove sensitive content for good, use Redact PDF"). The guide says the same. **PASS (disclosure).**
- One wording conflict (P3 #9): FAQ "Can I undo a crop after downloading? No — … the crop is permanent in that file" sits next to "can be recovered by software that ignores crop boxes".
- File size: ±1 % on text files (17.0 → 17.9 kB incl. trial mark); the 73.6 MB file stays 73.6 MB, as the page says.

## 2. Per page vs all pages: **PASS**

- All pages (A01), This page on page 2 (A02: only page 2 has a CropBox), Page range "1,3" (A03: pages 1 and 3 only). Region match on every cropped page (diff 0.0).
- Bad ranges get clear toasts: "5-9" → `"5-9" is outside this PDF's 3 pages`; "0" → `Page 0 is outside…`; "abc" → `isn't a valid page number`; "3-1" → `starts after it ends`; empty → `Enter a page range first`. "2-" is read as 2–3 and "1,,3" as 1,3 (lenient, fine).
- Every Apply starts from the original file, so a crop on page 1 followed by "This page" on page 2 gives a file where only page 2 is cropped (A02). Different boxes per page need several runs feeding the download back in; the FAQ says so ("Not in one pass"). Sejda and others crop pages separately in one pass (P3 #12).
- Scope and range **survive New** (P3 #8): after A04 left "1,,3" typed, a new 3-page file was cropped on pages 1 and 3 only with no hint (A05); a 1-page scan after a "3" range got `Page 3 is outside this PDF's 1 page` (T04, screens/T04-scan).

## 3. Rotated pages and existing offset crops: **PASS**, one edge case

- rotated.pdf, /Rotate 0/90/180/270, margins typed on the landscape page 4 (top 1 in, left 2 in): every page cropped where it was drawn on the displayed page. Region match diff 0.0–0.7 on all 4. Stored boxes: p2 (90°) [72 144 612 792], p3 (180°) [0 93.2 500.7 792], p4 (270°) [0 0 540 648] — the `pageView.toStored()` maths is right. Preview shows pages the right way up with the right size (11×8.5 in for 90°/270°).
- offset.pdf: p1 existing CropBox [100 150 500 700] → [147.1 150 476.5 650], inside the old crop, region match ✓. p2 MediaBox origin (50,50) → [122 50 626 770] ✓. p3 /Rotate 90 + offset crop ✓ (diff 2.3).
- **Edge case (P3 #4):** p4 has a CropBox larger than the MediaBox ([-20 -20 632 812] on a 612×792 sheet, seen in some generated PDFs). The preview (pdf.js) shows the clipped 8.5×11 in sheet, but the crop is computed from the raw box, so the result is 16 pt (0.22 in) off on the left/right/top: got [56.7 −20 593.7 736.4], expected [72 0 576 720]. The trial mark is placed at the raw box's bottom edge, so it is half off the page (screens/O01-p4-exp-vs-got). Fix: intersect CropBox with MediaBox before `toStored`.

## 4. Margins, Auto-trim and whitespace detection

- **Margins:** inches or millimetres, four fields, two-way synced with the box (drag → fields update; type → box updates). 25.4 mm ↔ 1 in round-trips. Readout "Page 1: 8.5×11 in → 6.5×9 in" is right.
  - Values are turned into a share of the page **you are looking at** and that share is applied to every page (stated: "Other pages keep the same share of their own size"). So on mixed.pdf 0.5 in becomes 0.38 / 0.69 in on the A4-landscape page and 0.38 / 0.34 in on A5 (X01); on rotated.pdf "left 2 in" typed on a landscape page became 1.55 in on the portrait pages. Matches the docs, but the field says "inches" (P3 #6). Sejda/Burgundy measure typed margins from each page's own edge.
  - Bad input is silently ignored (P3 #7): left 5 + right 5 on an 8.5 in page, "-1", "abc" and the decimal comma "0,5" all stay in the field while the box keeps the old value; only the small readout shows it. No message.
- **Auto-trim** (`pn()` on a 0.7× render): a pixel is content when R, G or B < 250; finds the outermost content, adds 1 % internally, then the Padding menu (None / 2 % / 5 % default / 10 %). Several pages → one union box; blank pages skipped; all-blank → "These pages look blank, so there is nothing to trim to". 300 pages: 5.2 s.
  - clean.pdf (content exactly 1.5 in from each edge): None → 1.38 / 1.40 in (≈0.1 in looser than the content; "None" isn't zero), 5 % → 0.83 / 0.98, 10 % → 0.28 / 0.55. Output matches the box (T01). Toast "Selected the area that holds the content of all 3 pages".
  - stray.pdf (a 6 px dot near page 3's right edge): All pages → right margin 0.05 in (the union, as documented); This page on p1 → 1.40 ✓; range "3" → 0.05 ✓.
  - doc.pdf with grey header/footer text → keeps them (correct: they are content).
  - **Whitespace detection fails on near-white paper (P2 #2):** scan-white (paper 255) trims to the text ✓. scan-249 (paper 249/255, visually white), scan-offwhite (246) and tinted.pdf (240) → the box is the **whole page**, margins 0/0/0/0, **no message** (T08, T03, T04). Most real scans have paper between 235 and 250, and both the page ("scanned or exported with extra whitespace") and the guide ("Trim scanner shadows…") pitch it for scans. The FAQ does warn about "a colored or textured background", but 249 is not coloured.
- **Cut-off warning:** works and is useful (lists pages, "Pages 1, 2, 3, 4, 5, 6, 7, 8 and 22 more…"; Widen / Crop anyway / Cancel all behave). But the detected content box carries the 1 % padding, so a box drawn within ~0.1 in of the content is reported as cutting it off: margins 1.45 in around content at 1.50 in → "Pages 1, 2, 3 have content outside this area" (W03, P3 #5). "Widen the box to fit" goes to 1.38 / 1.40 in.

## 5. Searchable text is kept: **PASS**

- Every output keeps every word: pypdf word counts equal the original +3 (the trial mark "Created with FreeDailyPro.com" is real text). Needles "KEEP-HEADING", "Line 20", "Q2/Q4" are found in the visible area with MuPDF and in PDFium's text layer. No rasterising anywhere.
- Form fields stay live (form.pdf: 12 fields / 13 widgets before and after; password copy enc.pdf unlocked in the browser → output unencrypted, 12 fields). Bookmarks kept (2 → 2). The margin link annotation is kept (hidden by the crop).
- Other page boxes are left as they were (P3 #10): boxes.pdf after a 1 in crop has CropBox [72 72 540 720] but TrimBox [9 9 603 783], BleedBox [0 0 612 792], ArtBox [36 36 576 756]. Viewers are fine; print/prepress tools that use TrimBox (the "trimming margins before printing" case on the page) see the old size. Clamp them to the new CropBox.
