Sent: 2026-10-30 12:47 ET

# B-0182 Organize PDF: insert pages from another PDF
Priority: P2 · Estimated effort: S · Report: #120 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let people assemble the final document (add the signed page, the appendix) without leaving the organiser.

## Why
Reorder, reverse, undo, duplicate, blank and rotate all work. The tool is Premium ($3/$9.99), so it should beat free rivals. smallpdf organize mentions insert ×24; we only insert blank pages. The counter mismatch is tracked in L-143/B-0055, not here.

## Who uses this
Office users and paralegals assembling packets.

## Outcomes (ranked)
1. "Insert PDF…" adds another file's pages at a chosen position, with thumbnails. 2. Drag across both sources. 3. Keep "(was N)" labels for the inserted pages ("from file B p2").

## Constraints
On-device. Don't change Merge PDF.

## Test cases
t3.pdf + insert form.pdf after page 1 → 4 pages, order 1, B1, 2, 3. Undo removes the insert.
