Sent: 2026-10-30 12:08 ET

# B-0171 Audio converter: reject non-audio at load; convert several files at once
Priority: P2 · Estimated effort: S · Report: #117 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Tell people immediately when a file isn't audio, and let them convert a folder in one go.

## Why
bad.mp3 (text) is accepted with "length unknown". The trimmer already shows "Couldn't read this audio file… Nothing was used from your trial". online-audio-converter offers batch conversion (×3) and trim (×35).

## Who uses this
People converting voice memos and podcast files (55 GA views).

## Outcomes (ranked)
1. Reuse the trimmer's decode check and message at load. 2. Multi-file convert with one ZIP download (gating per B-0156). 3. Optional link to Audio Trimmer after converting.

## Constraints
Keep the honest bitrate note ("source is lossless, so 192 kbps was used").

## Test cases
bad.mp3 → error at load, Convert disabled. 3 WAVs → 3 MP3s in a ZIP.
