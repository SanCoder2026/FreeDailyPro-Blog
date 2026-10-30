# B-0051 Trial use counted when a file is selected, not when a result is produced
Priority: P1      Estimated effort: 60 min      Report: #66      Source: Testing Bot

**How to work with us:** you are the implementation partner, not an order-taker. Inspect the real code and past deploy patterns, challenge anything weak, choose the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID (done | partial | blocked, live and checked).

## Intent
A trial use should be spent only when the user gets value (result/output action), exactly once, so the counter is trusted and limit-hit/upgrade data is real.

## Why
- Standing rule (TESTING-GUIDANCE §1, PROCESS.md): an output action (download/copy/export/result) = 1 use; Professional Tools 10/day.
- Audio Comparer, fresh context, Oct 29 ~9:41 PM ET: load "10 remaining" → **9 after choosing file 1** → 9 after file 2 → 9 after Compare. A second full-flow run in another fresh context ended at **8 remaining**. Count fires on selection and is inconsistent.
- Merge PDF counts correctly (10 → 10 after Merge → 9 after first Download → 9 after second Download), so the correct pattern already exists in the codebase.
- Site admin shows 0 limit hits (guidance §1); wrong counting makes that metric meaningless.

## Outcomes
- Audio Comparer: counter unchanged by file selection; decrements by exactly 1 when a comparison result is shown (or define the output action explicitly and document it); re-viewing the same result does not charge again.
- Audit other Professional Tools using the same upload component for charge-on-select and list them in the report.

## Constraints
Do not change the limits (Premium 2/day, Professional 10/day) or pricing.

## Test cases
R66-AUD-06: fresh context → /tool/audio-comparer → read "N remaining" at load / after file 1 (a440.wav) / after file 2 (a880.wav) / after Compare. Expected 10/10/10/9. Actual 10/9/9/9 (and 8 in another run). Script: test-cases/cnt.py. Desktop 1280, Chromium, logged out.
Owner decisions needed: none.
