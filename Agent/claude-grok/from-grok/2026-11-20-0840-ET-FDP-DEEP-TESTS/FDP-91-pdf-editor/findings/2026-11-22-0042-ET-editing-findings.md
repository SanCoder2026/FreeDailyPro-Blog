Sent: 2026-11-22 00:44 ET

# Editing: what was written to the file

Source: files/left2-0-edited_contract.pdf (verify-E11.json, E11 renders), files/left-0-edited_contract.pdf (E01).

## Edit text
- Lines are detected from pdf.js text runs (`as()`); scanned pages get a clear "No editable text" note.
- Replacement = white rectangle over the line box + `drawTextAnywhere` at the original size, x and baseline. Font: Helvetica / Helvetica-Bold. Colour: forced #000000. Bold: the current global Bold toggle.
- Original runs are not removed: "Acme Widgets", "New York", "$4,500.00", "jane.doe@example.com" are all still in the page text. Disclosed in Details/FAQ ("covered, not deleted"), but it means copy/search/screen readers report the old value on a contract where the user "fixed" a price.
- Longer replacement (clause 3): drawn past the white patch toward the margin; no wrap, no warning.
- The open edit box (input + grip + ×) is taller than a 12 pt line and sits over the next line: "Total fee" and "Contact" couldn't be clicked after editing the line above (Playwright: `ann-text-N intercepts pointer events`).
- Competitors: Sejda keeps the original font where possible and lets you change family/size/colour; iLovePDF edits/moves/deletes existing text.

## Additions
- Text: Helvetica; non-Latin via `needsPicture`: any character outside WinAnsi makes the whole string a PNG unless the string is Devanagari-only (then full FreeSans, `subset:false`).
- Devanagari: pdf-lib `drawText` has no shaping, so "हिन्दी" prints as "हिन्  दी" (visible halant, gap) in MuPDF and PDFium. Simple words ("सीता देवी", "राम कुमार") look right.
- Mixed "Mixed Latin 承認 مقبول": one picture; "Mixed Latin" not searchable. Arabic joins correctly in the picture.
- Highlight: yellow rectangle at 40 % opacity (text readable). Rectangle/ellipse: border colour/width, optional 20 % tint. Freehand: SVG path. Whiteout: opaque white. Pictures: PNG via canvas (`toDataURL('image/png')`, max 1600 px), default 30 % page width at 35 %/30 %.
- Long added text runs off the right edge of the page (render E11 p1 bottom).

## Content vs annotations
- `annots: []` on edited pages: every item is page content. Recipients can't toggle, edit or delete them as comments.
- form.pdf: page-2 annotations (Highlight, Text, Ink, FreeText) survive; 12 AcroForm fields stay live with the typed value; nothing flattened.

## Rotation / CropBox
- `pageView.toStored` maps preview positions through /Rotate and CropBox: rotated and cropped outputs match the previews.

## Large files
- 300 pages: first page in 0.5 s; each "next" about 1.5 s; no page-number input; Apply 3 s; edited page correct (6).
- 73.6 MB: loads in 0.5 s (page 1); Apply toast "This file is 70MB, larger than 50MB… It'll still work"; output 73.6 MB; JS heap 50 MB.
