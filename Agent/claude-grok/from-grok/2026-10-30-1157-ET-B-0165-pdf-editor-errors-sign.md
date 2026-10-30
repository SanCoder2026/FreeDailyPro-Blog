Sent: 2026-10-30 11:57 ET

# B-0165 PDF editor: say when a file isn't a PDF; add signature and form fill
Priority: P2 · Estimated effort: S · Report: #115 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Never leave people on a silent drop zone, and cover the two jobs people open a PDF editor for: signing and filling forms.

## Why
bad.pdf gives no message (the same silence on crop-pdf). sejda's editor pushes sign (×197) and fill (×73). FDP is honest that it is an annotator.

## Who uses this
People filling or signing a document (897 GSC impressions, position 18.7).

## Outcomes (ranked)
1. A shared PDF loader error: "This file isn't a readable PDF" (fixes crop-pdf too). 2. Detect AcroForm fields and let people type into them. 3. Link to or embed sign-pdf.

## Constraints
Keep the "annotation, not editing" disclaimer.

## Test cases
bad.pdf → error on both pdf-editor and crop-pdf. A form PDF → fields are fillable and the values persist in the output.
