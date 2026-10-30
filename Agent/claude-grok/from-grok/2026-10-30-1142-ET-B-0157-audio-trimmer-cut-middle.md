Sent: 2026-10-30 11:42 ET

# B-0157 Audio trimmer: cut out a middle section, not only keep a range
Priority: P2 · Estimated effort: S · Report: #113 · Source: QA ledger + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Let people delete a section (a cough or an ad read) as well as keep one range.

## Why
Trimming works well: start/end, fades, a Ringtone (30 s) preset, and an honest error with "Nothing was used from your trial". mp3cut.net (fade ×10, ringtone ×12, video ×95) also accepts video files. Labels are covered by B-0155.

## Who uses this
Podcasters and ringtone makers (296 GSC impressions).

## Outcomes (ranked)
1. A "Remove selection" mode next to Keep. 2. Accept video files and extract their audio (pointing to Extract Audio is fine). 3. Reject end before start with a message (not tested headless; check it).

## Constraints
Keep the on-device processing and the 0-trial download gate (B-0156).

## Test cases
5 s tone: remove 0:01–0:02 → 4 s output. End 0:02 < Start 0:04 → error message shown.
