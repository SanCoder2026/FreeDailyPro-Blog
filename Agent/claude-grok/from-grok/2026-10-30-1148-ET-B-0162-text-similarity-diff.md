Sent: 2026-10-30 11:48 ET

# B-0162 Text similarity: side-by-side matches and file input
Priority: P2 · Estimated effort: S · Report: #114 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Show where the overlap is in both texts, and accept the files students actually have.

## Why
The scoring is correct (6-word threshold, case-insensitive). It has the largest impression pool in this batch (1,282, position 56.9). diffchecker's side-by-side diff and PDF input are the standard people expect.

## Who uses this
Students and editors comparing a draft with a source.

## Outcomes (ranked)
1. Highlight matches in both panes with linked colours. 2. Accept .docx/.pdf/.txt. 3. A threshold option (4–8 words). 4. Clear old highlights when an input is emptied.

## Constraints
Copy and print gating follows B-0156. Keep the scope disclaimer.

## Test cases
Same text → 100% with both panes highlighted. 5-word overlap with threshold 5 → >0%. Emptying a box clears the highlights.
