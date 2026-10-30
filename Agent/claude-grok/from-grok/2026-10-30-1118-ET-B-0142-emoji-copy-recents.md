Sent: 2026-10-30 11:18 ET

# B-0142 Emoji picker: let the core copy action work, add recently used
Priority: P2 · Estimated effort: S–M · Report: #109 · Source: QA sweep + live competitor fetch 2026-10-30 11:16 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An emoji picker exists to copy emoji. People should be able to keep doing that, or at least clearly understand the limit, and find their usual emoji fast.

## Why
At 0 trial uses, clicking 👍 opens the paywall and the clipboard stays empty. Emojipedia and GetEmoji copy without limits. This drives away search visitors (10 GSC clicks, 261 impressions) for very little revenue. It is the same pattern as L-183.

## Who uses this
Social posters and writers who copy one emoji at a time.

## Outcomes (ranked)
1. Owner decision: exempt single-emoji copy from trial uses, or count one use per visit as the site copy says. Either way the first copy per visit must work. 2. A recently-used row stored on the device. 3. Show code points (U+, HTML entity) next to the selected emoji.

## Constraints
No change to the paid tiers without owner sign-off; nothing stored on a server.

## Test cases
After the decision: at 0 trial uses, click 👍 → it is on the clipboard or a clear one-line notice appears. Search "xyzzy" still shows the empty-state message. Recents survive a reload.
