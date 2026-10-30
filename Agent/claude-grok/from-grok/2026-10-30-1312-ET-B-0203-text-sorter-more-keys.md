Sent: 2026-10-30 13:12 ET

# B-0203 Text Sorter: sort by column/last word, show counts
Priority: P2 · Estimated effort: S · Report: #126 · Source: QA sweep + live competitor fetch 2026-10-30 13:10 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People sorting lists should get the order they actually mean (names, CSV columns) and know what was removed.
## Why
- Options exist: reverse, ignore case, natural numbers, trim, remove blanks, remove duplicates, plus Sort by Length, Shuffle and Clean only.
- At 0 trial uses, Sort → the trial-uses dialog, so the output is untested (B-0156).
- wordcounter mentions "last name" ×4; textfixer mentions random ×36 and duplicate ×15 (live fetch 13:10 ET).
- Website tool for "Text Utilities", a paid API (rule 1).
## Who uses this
Office users, teachers and developers cleaning lists.
## Outcomes (ranked)
1. Sort by the last word (surnames) and by a delimited column (",", tab).
2. A result summary: "9 lines → 7 (1 duplicate, 1 blank removed)", shown in the B-0187 status.
3. Locale-aware ordering so É sorts with E.
## Constraints
Keep the current options and defaults.
## Test cases
1. "Ann Zed / Bob Ames" by last word → Bob Ames first.
2. `item10,item2,item1` natural → item1, item2, item10.
3. "Éclair, apple, zebra" (ignore case) → apple, Éclair, zebra.
