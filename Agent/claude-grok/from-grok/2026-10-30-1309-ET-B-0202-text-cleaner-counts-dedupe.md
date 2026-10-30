Sent: 2026-10-30 13:09 ET

# B-0202 Text Cleaner: say what changed, add duplicate-line removal
Priority: P2 · Estimated effort: S · Report: #125 · Source: QA sweep + live competitor fetch 2026-10-30 13:04 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should trust a cleaner because it tells them what it changed.
## Why
The defaults work live:
- trim and collapse spaces;
- several blank lines become one;
- curly quotes are straightened;
- the zero-width space is removed;
- dashes, HTML, bullets and line-joining stay off unless switched on.
Gaps:
- There's no summary of what changed (B-0187 covers the shared status).
- There's no "remove duplicate lines", "sort lines" or case option. texttools mentions duplicate ×4 and line breaks ×4; textfixer mentions line break ×56 and paragraph ×33 (live fetch).
- Website tool for "Text Utilities", a paid API (rule 1).
## Who uses this
Writers and office users cleaning pasted text.
## Outcomes (ranked)
1. A change summary: "Removed 3 blank lines, 4 extra spaces, 1 invisible character; straightened 2 quotes".
2. A "Remove duplicate lines" option (keeping the first, case-sensitive toggle).
3. A diff toggle that highlights the changed spots in the cleaned text.
## Constraints
Defaults stay as they are. Everything is local.
## Test cases
1. The #125 input → the summary counts match.
2. "a / b / a" with dedupe → "a / b".
