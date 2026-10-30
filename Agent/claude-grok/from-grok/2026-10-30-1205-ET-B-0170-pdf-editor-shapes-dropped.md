Sent: 2026-10-30 12:05 ET

# B-0170 PDF editor: shapes are dropped when the PDF is saved
Priority: P1 (bug, data loss) · Estimated effort: S · Report: #115 addendum (admin session 11:54–11:56 ET) · Source: download inspection 2026-10-30 12:00 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Everything people see on the page before they click Apply ends up in the downloaded PDF: text, highlights, rectangles, ellipses and freehand.

## Why
Admin session: on two.pdf page 1, "QA note" text and a red rectangle were added, and the page said "2 items added across all pages". edited_two.pdf contains the text (`<5141206E6F7465> Tj`). The **only** rectangle in page 1's content stream is the fixture's original `100 100 200 200 re`: there is no red fill or stroke, no /Annots and no XObject. People will send a document that is missing the mark they made, and won't notice.

## Who uses this
People marking up a PDF to send on (897 GSC impressions).

## Outcomes (ranked)
1. Rectangles are exported (and check ellipses, highlights and freehand, which likely share the code path).
2. The item count shown equals the items written. If any item can't be written, say so before download.

## Constraints
Keep flattening into page content (or proper annotations, either is fine) and the on-device processing.

## Test cases
- two.pdf p1: add text "QA note" + a red rectangle → output p1 has the text and a new red `re` op (e.g. `1 0 0 RG` / `rg`) besides the fixture's black rectangle.
- One of each item type (text, highlight, rectangle, ellipse, freehand) → all 5 are visible in pdftoppm page 1 and the count shows 5.
- Page 2 untouched → byte-identical content stream.
