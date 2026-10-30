Sent: 2026-10-30 13:09 ET

# B-0201 Rotate Video: show the result orientation and offer output format
Priority: P2 · Estimated effort: S · Report: #125 · Source: QA sweep + live competitor fetch 2026-10-30 13:04 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should be sure the video is the right way up before they spend a download.
## Why
- Turn right 90° → Apply → "Turned without re-encoding: … the file now carries a rotation flag …". It's a good honest message and a model for B-0187.
- Download is gated at 0 trial uses (B-0156), so the output is untested.
- clideo mentions flip ×11 and format ×17 (live fetch).
- The tool has no preview of the rotated first frame and no output format choice for the re-encode path.
- Website tool for the paid video API (rule 1).
## Who uses this
Phone users fixing sideways clips.
## Outcomes (ranked)
1. Preview the first frame with the chosen turn/mirror applied, before Apply.
2. After Apply, show the final dimensions ("now 240×320").
3. Choose MP4 or WebM output when re-encoding.
## Constraints
Keep the no-re-encode fast path as the default for MP4/MOV.
## Test cases
1. 320×240 + Turn right → the preview is portrait; after Apply, "now 240×320".
2. Mirror → re-encode note, and an MP4 output whose frame is mirrored.
