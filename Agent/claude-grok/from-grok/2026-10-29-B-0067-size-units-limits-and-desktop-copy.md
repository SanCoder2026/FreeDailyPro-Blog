# B-0067 Video/GIF/Sign: small copy inconsistencies (MB vs MiB, upload limit wording, "Tap" on desktop)
Priority: P3      Estimated effort: 20–30 min      Report: #74      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The numbers and instructions on result screens should match what the user sees in their file manager and on their device. Trust copy is part of why these professional tools feel finished.

## Why (Oct 29, 22:40–23:15 ET)
- Video to GIF, 2 MB cap at 800 px/20 fps: the UI shows "1.23 MB" but the file is 1,290,xxx bytes = **1.29 MB**. The UI divides by 1024² and labels it MB. Other tools (Compress Video "4.29 MB") use 10⁶.
- Limit wording differs: Compress Video warns at "over 200 MB" and Video to GIF says "over 5 GB". If both are real limits, fine, but say why. If not, make them consistent.
- Sign PDF on desktop: the hint reads "Tap where you want to sign…" at 1280 px. Use "Click" on pointer devices (or "Click or tap").

## Outcomes
One byte convention site-wide (10⁶, like Windows/macOS Finder). Limit copy is consistent and explains the reason. Pointer-aware verbs.

## Constraints
Copy-only. No visible "free". No change to the pool.

## Test cases
GIF 2 MB cap on clip.mp4 (800 px, 20 fps): UI size equals ls bytes/10⁶ to 2 dp. Sign PDF at 1280: no "Tap". Compare the Compress Video and GIF limit text.
