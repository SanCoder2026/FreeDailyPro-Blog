Sent: 2026-10-30 13:02 ET

# B-0196 JSON↔CSV: warn on malformed CSV instead of silently merging rows
Priority: P2 · Estimated effort: S · Report: #124 · Source: QA sweep + live competitor fetch 2026-10-30 12:59 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A converter must never quietly change someone's data. If the input is malformed, say so and show where.
## Why
JSON→CSV is correct and live:
- nested objects become `addr.city`;
- lists join with "; ";
- a comma cell is quoted; `x"y` becomes `"x""y"`.
CSV→JSON keeps "007" as a string and handles the embedded newline ✓
**Bug:**
- CSV `a,b / 1,"unclosed / 2,3` gives 1 row, where `b` = "unclosed\n2,3". Row 2 is silently swallowed and there's no warning.
- Minor: "1 rows".
- Minor: the CSV output textarea starts with U+FEFF (BOM), so Copy pastes a hidden character. Keep the BOM for the download only.
- Minor: with "Numbers as real values" on, 3.50 → 3.5 (expected, but say so).
- Status → B-0187.
## Who uses this
Developers and analysts.
## Outcomes (ranked)
1. Detect an unclosed quote: "Row 2: a quote opened at column b is never closed". Show partial output only with that warning.
2. No BOM in the textarea or in Copy.
3. Correct singular/plural counts.
## Constraints
Don't change the valid-input results above.
## Test cases
1. The unclosed-quote CSV → a warning naming row and column.
2. Copy the CSV output → the first character is "i", not U+FEFF.
3. A single row → "1 row".
