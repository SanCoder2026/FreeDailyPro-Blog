Sent: 2026-10-30 15:59 ET

# B-0308 Audio Merger: 0.919 s clip listed as 0:00, total floored, no crossfade
Priority: P3 · Estimated effort: S · Report: QA-REPORT-160 · Source: live probe 2026-10-30 ~15:52-15:58 ET (headless, logged out, 1280/390 px), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People see the true length of each clip and the result before merging, and can blend clips smoothly.

## Why
GSC: /tool/audio-merger 2 clicks / 262 impressions / 0.8% CTR / position 15.9.
Checked live (15:57 ET): a4.wav (4.000 s, 44.1 kHz) + b48.wav (0.919 s, 48 kHz), Same as first file, no gap → a4-merged.wav, 4.919 s, 44.1 kHz ✔. The file list still shows "b48.wav (86.2 KB · 0:00)" and "Total length 0:04" (L-224/L-229 still open). Output formats: Same as first file, MP3, WAV, OGG, M4A, FLAC ✔. Reorder and remove buttons have names ✔.
The 48 kHz clip is resampled to the first file's rate without a note (as in L-224).
Silence between clips: None, 0.5, 1, 2 s. Crossfade: not offered (checked). Loudness matching and per-clip trim: not offered (checked).
Competitors (live search): SoundTools (50 files, per-file trim, crossfade curves), Convertico (gap or crossfade, even out loudness), Tembrica (per-clip trim/volume/EQ, LUFS), johnmcm (LUFS, chapter list), DevZone (crossfade, per-track volume).
Title 63 with "Free"; meta 81 (Free, short). /es title English (H1 "Fusionar Audio") → L-189.

## Who uses this
Podcasters and students joining recordings or songs.

## Outcomes (ranked)
1. Show clip and total length to 0.1 s (0.9 s, 4.9 s).
2. Snippet below.
3. Optional crossfade (0.5–3 s).
4. Optional "even out loudness".

## SEO
- Now: title "Merge Audio Clips Online Free - Combine in Order | FreeDailyPro" (63, Free); meta 81; H1 "Audio Merger"
- Keywords: merge audio files, audio joiner, combine mp3 files, join audio online, merge wav
- Suggested Title: "Audio Merger: Join MP3 and WAV Files in Order | FreeDailyPro" (60)
- Suggested Meta: "Join two or more audio clips into one file in the order you set. Add 0.5 to 2 seconds of silence between clips and save as MP3, WAV, OGG, M4A or FLAC." (150)
- Suggested H1: keep
- FAQ: keep current 6; add: Can I crossfade between clips? · Will clips with different sample rates play at the right speed?

## Constraints
Results count against the trial; do not change that. Keep the order buttons and output format list.

## Test cases
1. 4.0 s + 0.919 s WAV → list shows 0:04.0 and 0:00.9; total 0:04.9; output 4.919 s.
2. Add 1 s gap → total and output 5.9 s.
3. Choose MP3 → a4-merged.mp3 plays at the right speed.
4. View source → title and meta as suggested.
