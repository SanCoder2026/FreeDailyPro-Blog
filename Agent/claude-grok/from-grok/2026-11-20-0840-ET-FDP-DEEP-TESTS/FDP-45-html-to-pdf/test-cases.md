Sent: 2026-11-21 06:06 ET

# FDP-45 HTML to PDF: test cases (rerun after fixes)

Guest, fresh profile; test files in `evidence/testfiles`. "Now" is what we saw on 2026-11-21.

| ID | Case | Expected | Now |
|---|---|---|---|
| HP-01 | At 0: Convert sample, Preview | Converts; page-1 image only | PASS |
| HP-02 | At 0: Download / Drive / cloud | Cap dialog / sign-in dialog | PASS |
| HP-03 | Day Pass / Quick Buy | Email prompt / Stripe (stop) | PASS |
| HP-04 | Uses left: Download, then re-download the same result | +1, then no change | PASS |
| HP-05 | Same load: Download 5 new documents | +1 each | **P1 FAIL** (no change) |
| HP-06 | Reload, Download | +1 | PASS |
| HP-07 | File name per document | Matches each `<title>` or dropped name | **P2 FAIL** |
| HP-08 | H02 invoice | Rows whole, links clickable, external image, text searchable | PASS |
| HP-09 | H02 `#top` link | Not a link to FreeDailyPro | **P2 FAIL** |
| HP-10 | H03 breaks | 4 pages, no blank first page | **P2 FAIL** (5, blank p1) |
| HP-11 | H04 scripts/onerror | Markers absent | PASS |
| HP-12 | H05 meta refresh | Ignored | PASS |
| HP-13 | H06 scripts | Rendered in the picture; text layer Western only (documented) | PASS |
| HP-14 | H07 wide | Fits; warns if tiny | P3 (no warning) |
| HP-15 | H08 > 200 pages | Clear message | PASS |
| HP-16 | H09 windows-1252 | Accents correct, or a warning | **P2 FAIL** |
| HP-17 | H10 Letter/Landscape/margin 0/page numbers | Applied | PASS |
| HP-18 | H11 .txt | Rejected with message | PASS |
| HP-19 | H12 Legal / margin 50 | Applied | PASS |
| HP-20 | Margin 99 | Clamped to 50 | PASS |
| HP-21 | H14 webfont | Renders | PASS |
| HP-22 | Privacy: no document text in any request | None | PASS |
| HP-23 | Firefox / WebKit: sample, scripts | Same as Chromium | PASS |
| HP-26 | WebKit: H02 with an external image | Finishes (blank if blocked) | **P1 FAIL** (hangs 5+ min) |
| HP-27 | WebKit: Stop while stuck | Returns to Convert | **P1 FAIL** (still rendering) |
| HP-28 | WebKit: H02b without the external image | Finishes | PASS (5.9 s) |
| HP-24 | Table header repeats on page 2 | Repeats | P3 FAIL |
| HP-25 | iPhone SE | No horizontal overflow | P3 FAIL (9 px) |
