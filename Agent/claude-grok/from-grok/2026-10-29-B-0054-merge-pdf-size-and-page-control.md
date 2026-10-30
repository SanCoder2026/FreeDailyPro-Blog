# B-0054 Merge PDF: wrong output size label; add page-level control before merging
Priority: P3 (label) / improvement      Estimated effort: 20 min (label) + 120 min (page control)      Report: #67      Source: Testing Bot

**How to work with us:** you are the implementation partner, not an order-taker. Inspect the real code and past deploy patterns, challenge anything weak, choose the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Merge PDF is a top PDF page (86 views, 58 s engagement in 28 d — raw.md; 601 impr at pos 35.2 — test-plan.csv). Make the result trustworthy and the workflow as complete as the best competitors.

## Why
- Live Oct 29 ~9:37 PM ET: after merging one.pdf (2 p) + two.pdf (3 p) the result reads "5 pages · 1.7 KB", but the downloaded file is 5,548 bytes (≈5.4 KB). Wrong number on the result screen (P3).
- iLovePDF, Smallpdf and PDF24 show page thumbnails and allow removing/rotating individual pages or choosing page ranges per file before merging; we show only file-level order.

## Outcomes
- Size label equals the size of the file the user downloads (including the trial badge).
- Optional (owner/Claude judgement): per-file page thumbnails with remove/rotate or a page-range field, so "merge pages 1–3 of A with B" works in one tool. Keep it to one screen; keep the current fast path for simple merges.

## Constraints
Browser-only processing; trial 10/day counting on download stays as is (verified correct). API page selection is B-0040 — keep UI and API behaviour consistent if you touch both.

## Test cases
R67-MRG-05: upload fixtures one.pdf + two.pdf → Merge 2 PDFs → compare label vs downloaded file size. Desktop 1280 + mobile 390.
Owner decisions needed: whether to add page-level control (improvement).
