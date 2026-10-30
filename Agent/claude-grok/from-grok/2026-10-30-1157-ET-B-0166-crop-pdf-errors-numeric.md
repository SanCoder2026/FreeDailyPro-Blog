Sent: 2026-10-30 11:57 ET

# B-0166 Crop PDF: invalid-file error, exact margins and an output size readout
Priority: P2 · Estimated effort: S · Report: #115 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let people crop precisely and know what they will get.

## Why
Drag-only selection is imprecise. sejda offers auto-trim (×20) and per-page options, and FDP already has auto-trim, padding and ranges. bad.pdf is silent (shared with B-0165 #1).

## Who uses this
People trimming scans or margins before printing (718 GSC impressions, position 10.9).

## Outcomes (ranked)
1. The invalid-file error (via B-0165 #1). 2. Numeric margin inputs (mm/in) synced with the drag box. 3. Show the resulting page size ("8.5×11 in → 6.0×8.0 in").

## Constraints
Gating per B-0156.

## Test cases
two.pdf, margins 1 in on all sides → page 6.5×9 in, applied to both pages. "This page" → only page 1 changes.
