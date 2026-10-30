Sent: 2026-10-30 11:15 ET

Supersedes 2026-10-30-1112-ET-B-0141-screenshot-fullpage.md

# B-0141 Screenshot tool: full-page capture and share links
Priority: P2 · Estimated effort: M · Report: #108 + addendum · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let people capture a whole web page, not only the visible screen, and share a capture quickly.

## Why
ScreenRec and Awesome Screenshot offer full-page/scrolling capture and share links. The real-browser run showed our capture, crop, annotate, pixelate, copy, download and cancel message all work, so the gap is scope, not reliability.

## Who uses this
Support staff, students and bloggers documenting pages.

## Outcomes (ranked)
1. A full-page or stitched capture option for browser tabs where the browser allows it.
2. An optional share link. It must be opt-in, and it must keep the "files never stored" promise clear: say plainly when something is uploaded.
3. Current flow unchanged, including the cancel toast.

## Constraints
Runs on device by default; nothing is uploaded unless the user chooses to share.

## Test cases
- Full-page capture of a long page has the full height.
- Cancel picker still shows "Screenshot wasn't taken (permission denied or cancelled)".
- Download PNG still works.
