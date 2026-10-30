Sent: 2026-10-30 13:02 ET

# B-0197 SQL Formatter: dialect-aware output and statement checks
Priority: P2 · Estimated effort: S · Report: #124 · Source: QA sweep + live competitor fetch 2026-10-30 12:59 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should get formatting that's right for their database, with a heads-up when the SQL looks broken.
## Why
- It already has 9 dialects, indent and keyword case options, Minify, Copy and .sql download.
- At 0 trial uses, Format → trial-uses dialog, so output is untested (B-0156).
- At 390 px the button row overflows (408 px) → B-0194.
- dpriver mentions dialect ×18 and case ×55 (live fetch).
- Website tool for the "Code & Data Formatting" paid API (rule 1).
## Who uses this
Developers and analysts.
## Outcomes (ranked)
1. A clear message for unbalanced quotes or parentheses instead of a silent best effort.
2. String literals are preserved exactly ('it''s; ok').
3. Comments stay on their own lines.
4. Multiple statements are separated by a blank line.
5. An identifier case option, separate from keyword case.
## Constraints
Never change literals or identifiers.
## Test cases
1. `select 'it''s; ok'` → the literal is unchanged.
2. `select (1` → "Unclosed parenthesis".
3. Two statements → two blocks, with the `-- c` comment kept.
