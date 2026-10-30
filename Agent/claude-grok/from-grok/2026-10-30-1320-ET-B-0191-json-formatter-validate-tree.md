Sent: 2026-10-30 13:20 ET

# B-0191 JSON/YAML Formatter: precise errors, tree view, schema check
Priority: P2 · Estimated effort: M · Report: #123 · Source: QA sweep + live competitor fetch 2026-10-30 13:12 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Developers should find out exactly where their JSON is broken and be able to explore large documents.
## Why
- Website tool for the "Code & Data Formatting" paid API (first billable 30 Oct 2:42 AM ET, APYHUB-TRACKER; selection rule 1).
- Format, Minify, JSON→YAML, the indent choice, Sort keys and file upload are all there.
- At 0 trial uses, Format opened the trial-uses dialog, so output couldn't be checked → B-0156.
- jsonformatter.org mentions validate ×13, minify ×11, tree ×5 and schema ×4. curiousconcept mentions fix ×58 and rfc ×24 (live fetch 13:12 ET).
- Labels → B-0155. Status → B-0187.
## Who uses this
Developers and analysts pasting API responses and config files.
## Outcomes (ranked)
1. A syntax error names the line, the column and the token ("Unexpected } at line 1, col 8 — trailing comma?") and highlights the spot.
2. A collapsible tree view, with the JSON path of the selected node.
3. Optional validation against a JSON Schema the user pastes in.
4. A safe auto-fix for trailing commas and single quotes, offered and never silent.
5. Big integers above 2^53 are preserved exactly.
## Constraints
Never change values silently, including number precision. Everything runs in the browser.
## Test cases
1. `{"a":1,}` → an error at line 1, col 8, with a trailing-comma hint.
2. `{"n":12345678901234567890}` → Format keeps every digit.
3. A 2 MB file → the tree view stays responsive.
4. Schema `{"required":["id"]}` vs `{}` → "missing required property id".
