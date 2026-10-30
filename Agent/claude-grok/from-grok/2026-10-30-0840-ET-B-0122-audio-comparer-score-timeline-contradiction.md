Sent: 2026-10-30 08:40 ET
# B-0122 Audio Comparer: the headline score contradicts the timeline (82.6% "some differences" while every cell says "matches")
Priority: P1      Estimated effort: 0.5–1 day      Report: #98      Source: Testing Bot (admin session)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The verdict, the percentage and the timeline must tell one consistent story, so a user can trust whichever one they read.

## Why
- In the admin session, two identical 440 Hz tones with B starting 0.25 s later gave a headline of "Match 82.6%, Same content, with some differences", but all 3 timeline cells said "matches". The user cannot tell where the "differences" are.
- Not covered elsewhere: B-0050 covers offset alignment (this run is new evidence there: 0.25 s → 82.6%, against 0.0% for 0.5 s on 29 Oct). B-0119 covers A/B playback and visuals. Neither covers the internal inconsistency between the score and the timeline.

## Who uses this
Podcasters and musicians checking whether two exports are the same take; editors checking whether a file was altered.

## Outcomes (ranked)
1. The timeline is computed from the same comparison as the headline. If the headline says "some differences", at least one segment shows where; if every segment matches, the headline does not claim differences.
2. When the difference is explained by a start offset, say so ("B starts 0.25 s later; otherwise identical"). The alignment work itself is B-0050.
3. Timeline segments have a stated duration (for example, 3 cells for 3 s = 1 s each) so "matches" is meaningful.

## Constraints
Browser-only processing. Charge trial uses only on a completed result (B-0051).

## Repro (attached: test-cases/tone-a.wav, tone-b.wav)
1. tone-a.wav: 3.0 s, 44.1 kHz mono, 440 Hz from 0 s. tone-b.wav: same tone, first audio at 0.250 s, 3.0 s long (checked on the box).
2. Open /tool/audio-comparer, load A then B, click Compare Audio.
3. Observe: "Match 82.6% · Same content, with some differences"; timeline 3/3 "matches".

## Test cases (ET)
| ID | Input | Expected | Admin session 08:37 ET |
|---|---|---|---|
| TC-1 | tone-a vs tone-b | headline and timeline agree; offset named | 82.6% "some differences" + 3/3 "matches" — FAIL |
| TC-2 | tone-a vs tone-a | 100%, all segments match | (rerun after fix) |
| TC-3 | tone-a vs a tone with a 1 s gap in the middle | middle segment flagged | (rerun after fix) |
