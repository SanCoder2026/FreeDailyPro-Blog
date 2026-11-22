Sent: 2026-11-21 22:51 ET

# FDP-87 true-redaction findings

**Method:** each downloaded PDF was run through `verify87.py <out> testfiles/secrets.pdf`, which checks:
- pdftotext (`-layout` and `-raw`).
- PyMuPDF `get_text` and `search_for`.
- Text clipped to every black filled rectangle. This is the copy-paste test: select over a bar and copy.
- Raw file bytes.
- Every object decoded with pikepdf (streams decompressed).
- Info and XMP metadata, annotations, links, widgets/AcroForm, outline (`get_toc`), embedded files, `/OCProperties`, StructTree `/Alt` and page `/Thumb`.
- `pdfimages -list`, plus image stream hashes compared with the original, and the %%EOF count.

The JSON for each run is in `evidence/json/verify-*.json`.

## Where each secret ended up

Columns:
- **ORIGINAL** = the input.
- **R01** = typed name + ACCT-7781 + all detectors + both options + hand box over the photo.
- **R02** = name + detectors + both options (no photo box).
- **R03** = hand box over the SSN only, options off.
- **R07** = an empty box on page 3 only (cleanup options on from the session).
- **R09** = detectors only.

| Where a secret can hide | ORIGINAL | R01 full | R02 | R03 | R07 | R09 |
|---|---|---|---|---|---|---|
| pdftotext "Jonathan Reed" | 9 | 0 | 0 | 9 | 9 | 1 |
| pdftotext SSN 123-45-6789 | 1 | 0 | 0 | 0 | 1 | 0 |
| pdftotext email | 2 | 0 | 0 | 2 | 2 | 0 |
| pdftotext phone/card/EIN | 3 | 0 | 0 | 3 | 3 | 0 |
| pdftotext ACCT-7781 | 1 | 0 | 1 | 1 | 1 | 1 |
| PyMuPDF search name p1..p4 | [5, 2, 1, 1] | [0, 0, 0, 0] | [0, 0, 0, 0] | [5, 2, 1, 1] | [5, 2, 1, 1] | [1, 0, 0, 0] |
| Text under black boxes (copy test) contains a secret | False | False | False | False | False | False |
| Decoded objects: name | 28 | 1 | 1 | 35 | 20 | 5 |
| Decoded objects: SSN | 2 | 1 | 1 | 1 | 2 | 1 |
| Hidden OCG text LAYER | 1 | 0 | 0 | 1 | 1 | 0 |
| Old revision OLDREV (raw) | 1 | 0 | 0 | 0 | 0 | 0 |
| %%EOF markers | 2 | 1 | 1 | 1 | 1 | 1 |
| Info metadata keys | title, author, subject, keywords, creator, producer | producer | producer | title, author, subject, keywords, creator, producer | producer | producer |
| XMP name hits | 2 | 0 | 0 | 2 | 0 | 0 |
| Annotations (non-link) | 1 | 0 | 0 | 1 | 0 | 0 |
| mailto link | 1 | 0 | 0 | 1 | 1 | 0 |
| Form field values | [['client', 'Jonathan Reed']] | [] | [] | [['client', 'Jonathan Reed']] | [['client', 'Jonathan Reed']] | [] |
| Outline | ['Jonathan Reed intake'] | [] | [] | ['Jonathan Reed intake'] | ['Jonathan Reed intake'] | ['Jonathan Reed intake'] |
| Attachments | ['notes.txt'] | ['notes.txt'] | ['notes.txt'] | ['notes.txt'] | ['notes.txt'] | ['notes.txt'] |
| Figure alt text | ['Photo of Jonathan Reed'] | [] | [] | [] | ['Photo of Jonathan Reed'] | [] |
| /Thumb pages | [1] | [] | [] | [] | [1] | [] |
| Original image streams kept | 1 | 0 | 1 | 1 | 1 | 1 |
| Keep-line text intact | True | True | True | True | True | True |
| Size (bytes) | 152400 | 28274 | 40941 | 42244 | 149639 | 41019 |

## Reading the table
- **Marked means gone:**
  - Every secret that was marked is absent from the text layer, the copy test, the decoded streams and the metadata.
  - The leftover "name 1 / SSN 1" in decoded objects for R01/R02 is the attached `notes.txt` stream ("Private notes about Jonathan Reed, SSN 123-45-6789"). Confirmed by printing the object.
- **R03 shows only the marked area changes:**
  - The SSN is gone. The vector rectangle around it was cut at the bar edge: stroke [258,80,286,104] kept, the rest removed.
  - Everything else, including metadata ("Metadata not cleared" on the page), is kept, as designed.
  - Alt text and /Thumb were dropped because page 1 was marked, matching the FAQ.
- **R09 leaves 1 name in the text layer:** the invisible (render mode 3) line at the bottom of page 1, bbox y 697–716. The "Likely names" detector did not mark it, while a typed search does. **P2.**
- **R07 (unmarked pages):**
  - Page 1's /Thumb and alt text are kept, which is correct ("unmarked pages are not touched").
  - The page-2 hidden layer is kept, which is expected because nothing was marked there.
  - The trial mark was still added to all 4 pages (P3 wording).
- **Old revision:** every output is a fresh single-revision file (1 %%EOF), so the old page-3 contents (`OLDREV`) are gone even when page 3 was unmarked (R03).
- **Pictures:** in R01 the boxed JPEG became a 700×90 image with all pixels 0 (mean 0.0), and its original stream hash is gone. pdfimages shows the image re-encoded at 1154 B.

## Scanned PDF (R04, `left-2-redacted_scan.pdf`)
- Search: "This PDF is a scanned image, so search can't read it. Draw boxes by hand, or run OCR PDF first."
- Box [43,96,251,128] pt → image region (119,266)-(697,355) px. Mean 2.9 in the output against 240.6 in the original.
- The original image stream is not present. No text layer. Metadata is cleared.
- Crop: `screens/scan-out-crop.jpg` vs `scan-orig-crop.jpg`.

## Rasterize path (R11, `leftd-0-redacted_curve.pdf`)
- `curve.pdf` has the text "Curve secret: Jonathan Reed" and a red stroked circle (r=60) crossing it; page 2 has public text.
- The box covered the text line and part of the circle. Page 1 became a 1836×2376 JPEG (216 ppi) with no text layer. Page 2 keeps its real text.
- Notice: "Page 1 became a picture: a curved or filled-and-stroked drawing is partly under a box. Its text can no longer be selected or searched."
- (The test box stopped 2 letters short of the end of the line; that is the test's placement, not the tool.)

curve.pdf snippet (reportlab):
```python
c=canvas.Canvas('curve.pdf',pagesize=(612,792)); c.setFont('Helvetica',14)
c.drawString(72,700,'Curve secret: Jonathan Reed'); c.drawString(72,640,'Public line under the curve stays.')
c.setStrokeColorRGB(0.8,0,0); c.setLineWidth(3); c.circle(180,700,60)
c.showPage(); c.drawString(72,700,'Page two untouched public text.'); c.save()
```

## Summary .txt
- It lists counts by detector, per-page characters/pictures/drawings/annotations removed, the options taken, "Still in the finished file: 1 attached file", and a "What this tool does NOT do" list.
- It never contains the removed text. "Made:" uses the UTC date (P3).
