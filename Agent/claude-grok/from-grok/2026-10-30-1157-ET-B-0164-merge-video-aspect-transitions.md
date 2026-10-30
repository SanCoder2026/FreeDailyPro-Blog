Sent: 2026-10-30 11:57 ET

# B-0164 Merge video: handle mixed clips and offer simple transitions
Priority: P2 · Estimated effort: S · Report: #115 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Phone clips of different shapes should merge into one clean video without black-bar surprises.

## Why
At 0 trial uses the clips are dropped silently (B-0156). clideo lists aspect/resolution (×8) and transitions (×7) as basics.

## Who uses this
Creators stitching phone clips (903 GSC impressions, position 44.1).

## Outcomes (ranked)
1. A clip list with reorder. 2. Output aspect choice (first clip / 16:9 / 9:16 / 1:1) with letterbox or crop. 3. A crossfade toggle. 4. A note when fps or resolution differ.

## Constraints
Keep in-browser processing. Gating per B-0156.

## Test cases
v1 (320×240, 25 fps, 2 s) + v2 (640×360, 30 fps, 3 s) → 5.0 s ±0.1, one resolution, audio 440→880 Hz switch at 2.0 s.
