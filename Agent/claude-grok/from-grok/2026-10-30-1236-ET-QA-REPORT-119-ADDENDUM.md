Sent: 2026-10-30 12:36 ET

# QA Report 119 Addendum — admin-session downloads (Oct 30 ~12:28 ET)
Adds to #119 and does not change it. All results are **admin session**. Files: batch-38/downloads/. Checked 12:34 ET.

## 1. redacted_pii.pdf (1,306 B) vs the B-0098 checklist
Settings: all detectors, remove comments/links/forms/bookmarks on, clear metadata on. The page said "6 area(s) marked".

| Check | Result |
|---|---|
| 1. Un-redacted text still extracts | ✓ pdftotext: "Name: / SSN / Email / Phone / Card" and "Page 2 SSN" |
| 2. Redacted values unrecoverable | ✓ Not in pdftotext output, the raw file or the decoded content streams: 123-45, 6789, 987-65, Jane, Doe, example, 555, 4111 all absent. The glyphs are replaced by kerning-only TJ gaps, with a black `re f` bar on top. No annotations. |
| 3. Rasterised? | ✓ **No**. pdfimages lists 0 images; the page is still a text content stream. |
| 4. Fonts | Helvetica Type 1, **not embedded**. That's the same as the input (ReportLab base-14), so nothing was lost. Render (pdftoppm, downloads/red-1.png) shows all labels drawn with neat bars. |
| Metadata | ✓ Cleared. Input had Title "untitled", Author/Creator "anonymous", Subject "unspecified"; output Info has only Producer "FreeDailyPro", and there's no XMP stream. |

**Comparison with the API repro (claude-briefs/assets/B-0098/observed-output.pdf):**
- The API output is one 1786×2526 JPEG per page, with no fonts and no text.
- **The website tool shows neither the rasterise flaw nor the text-wipe flaw. The site tool is clean**, so I wrote no B-0098-v2. B-0098 stays an API-only issue (Santosh/API scope).

Minor observation, not a bug: the TJ gaps keep the original glyph advance widths, so the length of each removed value can be inferred. The black bar shows that anyway, and this is standard in Acrobat and PyMuPDF.
## 2. repaired_broken.pdf (1,352 B)
✓ pdfinfo: 2 pages, A4. It opens, and pdftotext returns all the original text on both pages.
## 3. v.mp3 (15,988 B)
✓ MP3 mono 44.1 kHz, ~41 kbps VBR, **3.056 s**. FFT peak **439.9 Hz** (440 Hz source).
**Note:** after a successful extract, the page shows only "Download MP3" with no success status text (no "Extracted 3.0 s of audio"), unlike repair's "Recovered 2 pages". Added to B-0180 scope via L-246; no new brief.

## Ledger
- L-244 → verified (site clean vs B-0098).
- L-245 → output verified; the copy fix stays open.
- L-246 → MP3 verified; the no-audio message and missing status text stay open.
