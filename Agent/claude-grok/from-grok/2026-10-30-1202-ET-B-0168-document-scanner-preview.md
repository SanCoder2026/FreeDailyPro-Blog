Sent: 2026-10-30 12:02 ET

# B-0168 Document scanner: show the scan before asking for the pass, then multi-page and OCR
Priority: P2 · Estimated effort: S · Report: #116 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should see their cleaned-up scan before paying the higher Premium price ($3 day / $9.99 monthly).

## Why
At 0 of 2 trial uses, dropping a photo opens the $3 paywall before any preview (B-0156 policy). CamScanner's pitch is OCR (×18) and multi-page.

## Who uses this
People scanning receipts and forms from a phone photo (59 GA views).

## Outcomes (ranked)
1. Pending the B-0156 owner decision, preview the cropped scan (it can be watermarked) and gate the PDF download. 2. Add more photos to build a multi-page PDF. 3. Optional OCR text layer.

## Constraints
Premium tier pricing is the owner's call; do not change prices.

## Test cases
doc.jpg → corners detected → straightened preview. 3 photos → 3-page PDF. OCR on → pdftotext returns the lines.
