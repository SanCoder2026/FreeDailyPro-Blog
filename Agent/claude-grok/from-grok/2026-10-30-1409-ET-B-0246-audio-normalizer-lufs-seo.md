Sent: 2026-10-30 14:09 ET

# B-0246 Audio Normalizer: page 3 → page 1 for "normalize audio"; add LUFS presets, true-peak and measurement in the copy
Priority: P1 · Estimated effort: S · Report: #140 · Source: SEO backfill 7, curl server HTML + seo.py + Google top 5 (WebSearch), 2026-10-30 ~14:07–14:08 ET. Already tested (L-099).

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone searching "normalize audio" should land here and see at once that it hits Spotify, podcast and broadcast loudness targets in the browser.
## Why
- GA rank 32 (65 views). GSC: 32 clicks, 503 impressions, 6.4% CTR, **position 28.3** (`analytics/2026-07-10-to-now-raw.md`). The CTR is good for page 3; ranking is the problem.
- Title (51) and meta (156) are fine; **title has no brand and no "LUFS"**, which every top-5 result uses.
- Ledger L-099: Spotify −14 / Podcast −16 split and ACX RMS copy exist.
- **Top 5 offer (~14:08 ET):** LUFS presets −14/−16/−18/−23 (UtilityKit, FFmpeg Cookbook); true-peak ceiling (all); loudness report — integrated LUFS, LRA, true peak (JAD); preview before export (AudioKit); batch/album and 9 formats (audio2edit); peak vs loudness explainer (AudioKit). Confirm which we have before adding copy.
## Who uses this
Podcasters, musicians and video editors levelling episodes or tracks.
## Outcomes (ranked)
1. Title/H1/meta name LUFS and the targets.
2. Copy section "Which target?" with a −14/−16/−23 table and true-peak advice.
3. Show measured input LUFS and output LUFS (if the tool already computes it, surface it).
## SEO
- **Now:** 200, sitemap, self canonical, 11 hreflang, valid JSON-LD; site-wide → **B-0209**; /es English title → **B-0123**. H1 "Audio Volume Normalizer".
- **Best result:** H2s "Peak vs loudness normalization", "Which LUFS target?", "Normalize without uploading".
- **Keywords:** "normalize audio", "audio normalizer", "normalize audio online", "lufs normalizer", "-14 lufs".
- **Suggested:**
  - Title: `Audio Normalizer – Normalize to −14/−16 LUFS | FreeDailyPro` (59)
  - Meta: `Normalize audio loudness online to Spotify (−14 LUFS), podcast (−16) or EBU R128 (−23) targets with a true-peak limit. Runs in your browser; nothing uploaded.` (158)
  - H1: `Normalize Audio Loudness (LUFS) Online`
  - FAQ: "Which LUFS for podcasts?" → "About −16." · "Peak or loudness?" → "Loudness, for even playback." · "Is my audio uploaded?" → "No."
## Constraints
Only claim targets/options the tool actually has.
## Test cases
1. Title ≤ 60; meta 140–160; H1 contains "LUFS".
2. GSC position for /tool/audio-normalizer rechecked after 28 days.
