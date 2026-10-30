Sent: 2026-10-30 12:02 ET

# B-0167 Fancy font generator: more styles people search for, and platform hints
Priority: P2 · Estimated effort: S · Report: #116 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Cover the styles people come for and tell them where each one shows up as boxes.

## Why
21 styles render correctly. lingojam and fsymbols list zalgo/glitch/cursive variants. Some styles (squared, bubble) break on some platforms. Copy gating follows B-0156; labels follow B-0155.

## Who uses this
Social bios and gamer tags (621 GSC impressions, position 18.8).

## Outcomes (ranked)
1. Add zalgo (with an intensity setting), glitch and a few cursive variants. 2. A one-line "may show as boxes on…" hint for squared/bubble/circled. 3. Decoration buttons named per B-0155.

## Constraints
Pure Unicode output; no images.

## Test cases
"Hello" → zalgo intensity 1–3 gives increasing combining marks. Squared row shows the hint.
