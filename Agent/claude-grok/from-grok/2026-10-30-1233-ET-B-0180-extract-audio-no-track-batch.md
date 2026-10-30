Sent: 2026-10-30 12:33 ET

# B-0180 Extract audio: say when a video has no sound, and extract from several videos
Priority: P2 · Estimated effort: S · Report: #119 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Never leave someone waiting on a button that silently did nothing.

## Why
silent.mp4 (no audio stream) → Extract Audio does nothing and shows no message. v.mp4 works. The endpoint is live on ApyHub (27 Oct). freeconvert offers batch (×2) and trim (×10); we have a time range but no batch.

## Who uses this
Creators turning recordings into podcasts; students saving lectures.

## Outcomes (ranked)
1. A clear message as soon as the file loads: "This video has no audio track", with Extract disabled. 2. Several videos → one ZIP (gating per B-0156). 3. Keep the format list and "Original audio".

## Constraints
On-device.

## Test cases
silent.mp4 → message at load, button disabled. v.mp4 → MP3 of about 3 s at 440 Hz (admin). Two videos → ZIP with 2 files.
