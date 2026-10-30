Sent: 2026-10-30 12:22 ET

# B-0176 Remove PDF pages: one-click "select blank pages"
Priority: P2 · Estimated effort: S · Report: #118 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Clean scanner output (blank backs of double-sided scans) without clicking every page.

## Why
The page selector, ranges and validation messages are excellent (the "7, x" message is the best on the site). Blank pages are the commonest reason to delete pages from scans. ilovepdf mentions blank pages; sejda offers batch ×6.

## Who uses this
Office users cleaning double-sided scans.

## Outcomes (ranked)
1. A "Select blank pages" button with an adjustable threshold that only pre-selects; the user confirms. 2. Thumbnails show why a page was selected. 3. Optional batch.

## Constraints
Never auto-delete. Keep the "at least one page" guard.

## Test cases
PDF with pages 2 and 4 blank → button selects 2, 4 → "2 pages will be removed; 3 stay". Pages with only a tiny footer → not selected at the default threshold.
