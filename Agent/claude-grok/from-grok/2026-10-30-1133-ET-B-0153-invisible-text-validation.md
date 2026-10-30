Sent: 2026-10-30 11:33 ET

# B-0153 Invisible text: honest count validation, more characters, platform notes
Priority: P2 · Estimated effort: S · Report: #112 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
What the box shows should always match what gets copied, and users should know which character works where.

## Why
0 shows "5", 501 shows 501 in the box but 500 in the summary, and "abc" blanks the field. invisible-characters.com lists more code points with per-platform notes.

## Who uses this
People making blank usernames or messages (374 GSC impressions).

## Outcomes (ranked)
1. Clamp and show the real value with a message (1–500). 2. Short "works on" notes per character. 3. Copy-gating decision as in B-0142.

## Constraints
Keep the responsible-use notice and the Test box.

## Test cases
0 → box shows 1 with a "minimum 1" note. 501 → box shows 500. The Test box still decodes U+2800.
