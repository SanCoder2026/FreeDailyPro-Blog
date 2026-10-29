# QA backlog index — Testing Bot reports #46–#65 (2026-10-29)

Claude fixed Testing Bot reports through #45. These briefs cover reports #46–#65 (the final tools batch) plus three known items (watermark, privacy pop-up, failing count test). Tiering (SW-19: Premium 2/day $3/$9.99 vs Professional 10/day $1/$4.99) and trial watermarks (SW-14) are by design and are not briefed.

**Cadence:** the owner allows multiple exchanges per day. Take batches as fast as you can, in order. After each batch, write a report to `Agent/claude-grok/from-claude/` (e.g. `2026-10-29-1400-report.md`) with per-brief status (`B-000N: done | partial | blocked | not started`) and verification status (`live and checked` / `pushed, deploying` / `needs owner action`). Grok reads new reports during the day and replans.

Total: 18 briefs, 785 min.

| Order | Brief | Priority | Effort | Batch |
|---|---|---|---|---|
| 1 | [B-0001 Trial exhausted: disable exports, show 0 remaining, never leak or charge without a file](2026-10-29-B-0001-trial-exhausted-exports.md) | P1 | 90 | Batch 1 MUST-DO |
| 2 | [B-0002 Privacy opt-out pop-up stays open on every step in fresh sessions](2026-10-29-B-0002-privacy-popup-sticky.md) | P1 | 30 | Batch 1 MUST-DO |
| 3 | [B-0003 Receipt photo OCR drops the decimal (8.91 read as 891.00)](2026-10-29-B-0003-receipt-ocr-decimal.md) | P1 | 45 | Batch 1 MUST-DO |
| 4 | [B-0004 Image / print-shop PDF exports come out absurdly tall](2026-10-29-B-0004-export-height-runaway.md) | P1 | 75 | Batch 2 |
| 5 | [B-0005 PDF watermark tool output nearly invisible](2026-10-29-B-0005-pdf-watermark-visible.md) | P1 | 20 | Batch 2 |
| 6 | [B-0006 Fix failing tool-count test (shared/siteFacts.counts.test.ts)](2026-10-29-B-0006-sitefacts-count-test.md) | P2 | 15 | Batch 2 |
| 7 | [B-0007 Event budget CSV omits Spent / Remaining / Expenses](2026-10-29-B-0007-event-budget-csv.md) | P2 | 30 | Batch 3 |
| 8 | [B-0008 Grocery list: free-text items all land in Produce, causing duplicates](2026-10-29-B-0008-grocery-aisle-autoclass.md) | P2 | 30 | Batch 3 |
| 9 | [B-0009 Packing list 'Back up' JSON doesn't save items or packed state](2026-10-29-B-0009-packing-backup-json.md) | P2 | 25 | Batch 3 |
| 10 | [B-0010 Two-step 'make then Download' flows look broken](2026-10-29-B-0010-two-step-download-ux.md) | P2 | 45 | Batch 3 |
| 11 | [B-0011 'Try a sample' leaves key steps empty or mismatched](2026-10-29-B-0011-sample-data-disconnects.md) | P2 | 60 | Batch 4 |
| 12 | [B-0012 Outdated platform presets (ringtone 40s, YouTube thumbnail, Facebook cover)](2026-10-29-B-0012-platform-size-presets.md) | P2 | 40 | Batch 4 |
| 13 | [B-0013 Mobile overflow and mobile download gaps](2026-10-29-B-0013-mobile-overflow-downloads.md) | P2 | 50 | Batch 5 |
| 14 | [B-0014 Small copy and output accuracy fixes](2026-10-29-B-0014-copy-accuracy-fixes.md) | P3 | 45 | Batch 5 |
| 15 | [B-0015 Remove 'Free' from tool page titles and meta descriptions](2026-10-29-B-0015-remove-free-titles.md) | P3 | 40 | Batch 6 |
| 16 | [B-0016 Small touch targets on mobile (13–16px checkboxes, icons)](2026-10-29-B-0016-small-touch-targets.md) | P3 | 45 | Batch 6 |
| 17 | [B-0017 Paper size and booth unit options](2026-10-29-B-0017-small-options.md) | P3 | 40 | Batch 6 |
| 18 | [B-0018 Add short official-guidance tips (TSA, FDA allergens, CAN-SPAM, etc.)](2026-10-29-B-0018-compliance-tips.md) | P3 | 60 | Batch 7 |

- Batch 1: 165 min
- Batch 2: 110 min
- Batch 3: 130 min
- Batch 4: 100 min
- Batch 5: 95 min
- Batch 6: 125 min
- Batch 7: 60 min

**Owner decision pending (not for Claude):** Government Forms Hub and Travel Countdown Planner show a 2-use trial meter on tools that don't generate files / don't enforce it — keep, remove or enforce? Until decided, do not change them.
