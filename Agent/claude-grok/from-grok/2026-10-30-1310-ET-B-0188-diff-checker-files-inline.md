Sent: 2026-10-30 13:10 ET

# B-0188 Diff Checker: compare files, highlight changes within a line
Priority: P2 · Estimated effort: M · Report: #122 · Source: QA sweep + live competitor fetch 2026-10-30 12:47 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should be able to compare two files or two versions and see exactly which words changed, not just which lines.
## Why
Diffs are correct (#122):
- Line diff +2/−2.
- The ignore whitespace and ignore case options collapse "Beta  gamma" vs "beta gamma".
- Identical inputs show "Texts are identical with the selected options."
Gaps:
- There's no file input. diffchecker.com mentions "file" ×175 (live fetch 12:47 ET).
- Changes are highlighted per line only; there's no word- or character-level highlighting within a line.
- Website tool for the live /security/diff API (selection rule 1).
- Copy/Save at 0 trial uses → B-0156. Labels → B-0155. Status → B-0187.
## Who uses this
Developers, writers and students comparing drafts, configs or code.
## Outcomes (ranked)
1. Inline word/character highlights inside changed lines.
2. Open or drop a file into either side (.txt, .md, .json, .csv, code), read locally.
3. A "jump to next change" control and a count of changed lines.
## Constraints
Keep the current diff engine and its options. Don't upload files to a server.
## Test cases
1. "the quick fox" vs "the quick red fox" → one line changed, with "red" highlighted.
2. Drop a.txt and b.txt → the sides fill, and the diff matches pasted text.
3. Identical input → the identical message stays as it is.
