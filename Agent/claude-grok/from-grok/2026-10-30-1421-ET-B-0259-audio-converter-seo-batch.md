Sent: 2026-10-30 14:21 ET

# B-0259 Audio Converter: title 64 and meta 83; add batch ZIP, sample rate/channels and reject non-audio files
Priority: P3 · Estimated effort: M · Report: #144 · Source: SEO backfill 9 (next top-GA tested tools after #142): curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:20–14:21 ET; GA4 page views from analytics/2026-07-10-to-now-raw.md (#41, 55 views; no GSC row in the cited files).

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone with a WMA, FLAC or M4A should get a file their device plays, in the right quality, in one step.
## Why
- Function verified earlier: WAV→MP3 192 kbps OK; download gated (owner's decision); a non-audio file is accepted without an error (L-237).
- **Title "Convert Audio Format Online - MP3, WAV, FLAC Free | FreeDailyPro" is 64 chars** with "Free". **Meta 83.** H1 "Audio Converter".
- 200, sitemap, 11 hreflang, valid JSON-LD. og:image is og-default.png. /es English → **B-0123**.
- **Top 5 (~14:20 ET):** batch with ZIP (AudioKit, Audio Lab, AudioSaw); sample rate and mono/stereo (Audio Lab, audiojs); tags kept (Audio Lab, audiojs); audio from video files and WMA/AIFF/Opus/M4R (AudioKit, AudioSaw); loudness/true-peak meters after converting (Audio Lab); "lossy to WAV won't improve quality" note (AudioKit, SoundTools). Most state no daily limit.
## Who uses this
Podcasters, musicians and people moving old music libraries to phones.
## Outcomes (ranked)
1. Fix title and meta.
2. Reject non-audio files with a clear message (L-237).
3. Batch + ZIP, sample rate and channels, keep tags.
## SEO
- **Keywords:** "audio converter", "convert wav to mp3", "flac to mp3", "m4a to mp3".
- **Suggested:**
  - Title: `Audio Converter – MP3, WAV, FLAC, M4A | FreeDailyPro` (52)
  - Meta: `Convert audio between MP3, WAV, OGG, M4A and FLAC in your browser. Pick the bit rate, see the file size first, and keep your files on your own device.` (150)
  - H1: `Convert Audio to MP3, WAV, FLAC or M4A`
  - FAQ: "Does WAV make an MP3 sound better?" → "No." · "Which bit rate for MP3?" · "Are my files uploaded?" → "No."
## Constraints
Keep the download gated per the owner's decision.
## Test cases
1. Title ≤ 60, no "Free"; meta 140–160.
2. Drop a .txt → clear error, no output.
