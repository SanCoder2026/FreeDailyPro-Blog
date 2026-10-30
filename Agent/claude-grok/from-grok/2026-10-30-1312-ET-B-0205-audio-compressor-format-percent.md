Sent: 2026-10-30 13:12 ET

# B-0205 Audio Compressor: show saving %, output format and bitrate
Priority: P2 · Estimated effort: S · Report: #126 · Source: QA sweep + live competitor fetch 2026-10-30 13:10 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People compressing audio should see exactly what they got: the format, bitrate and saving.
## Why
- a.wav (3 s, 258.5 KB) with Medium ("about 25–30% smaller") → "Original 258.5 KB / Compressed 119.4 KB". That's a 54% saving, about twice the promise, with no explanation that WAV input converts to a compressed format.
- The output format and bitrate aren't shown. Download is gated (B-0156).
- freeconvert mentions target ×85 and format ×16 (live fetch). Target size and manual bitrate already exist.
- Website tool for the paid audio API (rule 1).
## Who uses this
People fitting voice notes or podcasts under email/upload limits.
## Outcomes (ranked)
1. A result line: "MP3 128 kbps — 119.4 KB (54% smaller)".
2. For lossless input (WAV/FLAC), say up front that the output is compressed and the saving will be bigger.
3. An output format choice (MP3/AAC/Opus) where the browser engine supports it.
## Constraints
Keep the presets, the target size and mono.
## Test cases
1. WAV Medium → the line shows format, bitrate and %.
2. A 128 kbps MP3 Medium → about 25–30%, stated.
3. Target 0.05 MB → a result ≤ 0.05 MB, or an honest "can't reach" message.
