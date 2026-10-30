Sent: 2026-10-30 12:33 ET

# B-0179 Repair PDF: say what was fixed, and fix the not-a-PDF wording
Priority: P2 · Estimated effort: S · Report: #119 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should know what repair did before they trust the file.

## Why
A damaged xref → "Recovered 2 pages" ✓. A non-PDF is refused, but the message reads "it looks like not a PDF". The repair endpoint is live and billable (30 Oct).

## Who uses this
Anyone with a PDF that won't open (email attachments, cut-off downloads).

## Outcomes (ranked)
1. Copy: "This file isn't a PDF (it looks like plain text). Open it in the matching program…", naming the detected type when known. 2. A short "What was fixed" line (rebuilt cross-reference table / recovered N of M pages / removed broken objects). 3. Keep the best-effort warning.

## Constraints
No change to the recovery logic.

## Test cases
notpdf.pdf → new wording names text. broken.pdf → "Rebuilt the cross-reference table; recovered 2 pages".
