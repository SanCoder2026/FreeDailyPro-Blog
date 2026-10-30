Sent: 2026-10-30 11:12 ET

# B-0141 Screenshot tool: full-page capture and clear capture errors
Priority: P2 · Estimated effort: S–M · Report: #108 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let people capture a whole web page, not only the visible screen, and tell them when a capture fails or is cancelled.

## Why
ScreenRec and Awesome Screenshot offer full-page or scrolling capture and share links. In our headless run, Take Screenshot gave no feedback when no capture happened.

## Who uses this
Support staff, students and bloggers documenting pages.

## Outcomes (ranked)
1. A visible message when screen-share is cancelled or denied. 2. A full-page or stitched capture option for browser tabs where the browser allows it. 3. Existing crop, annotate, pixelate and copy unchanged.

## Constraints
Runs on device; nothing uploaded.

## Test cases
Cancel the share picker → message shown within 1 s. Capture a tab → crop and pixelate still work. A full-page capture of a long page has the full height.
