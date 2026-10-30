Sent: 2026-10-30 13:12 ET

# B-0204 Video Speed Changer: state the new length, allow custom speed
Priority: P2 · Estimated effort: S · Report: #126 · Source: QA sweep + live competitor fetch 2026-10-30 13:10 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should know the result is what they asked for (the new length) without having to download it.
## Why
- v.mp4 (3 s) at the default 2× → "Change speed" → Download video appears (gated, B-0156) with no result text: no new duration and no confirmation → B-0187.
- The help text promises pitch-preserved audio and MP4 output.
- clideo mentions format ×16, audio ×20 and slow motion ×3 (live fetch). There are only fixed presets plus a slider labelled "Speed 2×".
- Injected "Compare Browsers" text sits inside the About paragraph → L-004.
- Website tool for the paid video API (rule 1).
## Who uses this
Creators making time-lapse or slow-motion clips.
## Outcomes (ranked)
1. After the run: "2× — 3.0 s → 1.5 s, sound kept at the same pitch".
2. A mute-audio option (common for time-lapse).
3. A custom speed field (0.25–4, step 0.05).
## Constraints
Keep pitch preservation and the presets.
## Test cases
1. 3 s at 2× → the message says 1.5 s; the downloaded file is about 1.5 s.
2. Mute on → the output has no audio stream.
3. 1.25 typed → accepted; 5 → an inline error.
