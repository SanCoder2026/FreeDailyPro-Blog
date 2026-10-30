Sent: 2026-10-30 11:27 ET

# B-0148 ASCII art: never claim "Copied" when nothing was copied
Priority: P2 · Estimated effort: S–M · Report: #111 · Source: QA sweep + live competitor fetch 2026-10-30 11:25 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Users must be able to trust the success message: if the copy is blocked, say so plainly.

## Why
At 0 trial uses, the green "Copied to clipboard" toast shows alongside the paywall and the clipboard is empty. The paywall also says "download" for a copy action. Same copy-gating family as L-210.

## Who uses this
Developers adding banners to READMEs and terminal output (427 GSC impressions).

## Outcomes (ranked)
1. No success toast unless the clipboard write succeeded. 2. Paywall wording matches the action ("copy"). 3. Owner decision on whether copying small text output should count as a trial use (see B-0142). 4. Optional: wrap warning for wide banners, and more FIGlet fonts.

## Constraints
Keep the current accent and emoji messages; keep the output matching FIGlet.

## Test cases
At 0 trial uses, click Copy → no "Copied" toast and the clipboard is unchanged. With trial uses left → toast shown and the clipboard holds the banner. "Hello" Standard is still 23 characters wide.
