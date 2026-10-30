Sent: 2026-10-30 15:03 ET

# B-0283 Audio Speed Changer: wider range, output choice and snippet
Priority: P3 · Estimated effort: S · Report: QA-REPORT-152 · Source: GSC Top-50 pages (analytics/2026-07-10-to-now-raw.md), live probe 2026-10-30 ~15:02 ET, live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Be the obvious choice for slowing a song to practise or speeding a lecture to save time, with the result in the format the user needs.

## Why
GSC page: 5 clicks / 315 impressions / 1.6% CTR / avg position 12.1. Title (53) has "Free" and no brand; meta 93; /es English (L-189). Pitch preservation already verified (FFT 439.93 Hz, L-213); open: 0:04→0:02 display truncation and slider without accessible name (L-213, B-0155).
Live competitors: nah.tools 0.25–3×, Toolbox365 0.25–4× with presets (0.5/0.75/1.25/1.5/1.75/2×), audiojs exports MP3/WAV/FLAC/OGG/Opus/AAC and adds a separate semitone pitch slider, AudioKit offers "change pitch with speed" as an option.

## Who uses this
Musicians practising parts, students and podcast listeners, language learners.

## Outcomes (ranked)
1. One-click presets (0.5×, 0.75×, 1.25×, 1.5×, 2×) and a range of at least 0.25–3× (state the range on the page).
2. Output format choice (MP3/WAV at minimum).
3. Optional pitch shift in semitones (separate control).
4. Fix L-213 duration display; name the slider.
5. Snippet as below.

## SEO
- Now: title "Change Audio Speed Without Pitch Change - Free Online" (53); meta 93; H1 "Audio Speed Changer".
- Keywords: change audio speed, speed up audio without changing pitch, slow down audio, audio speed changer.
- Suggested Title: "Audio Speed Changer – Keep the Pitch | FreeDailyPro" (51)
- Suggested Meta: "Speed up or slow down a song, lecture or voice note without the chipmunk effect. Pitch stays the same at any speed, and the audio never leaves your browser." (156)
- Suggested H1: "Audio Speed Changer – Change Speed Without Changing Pitch"
- FAQ: Does the pitch change? · What speed range? · Which formats? · Is my file uploaded?

## Constraints
Keep pitch-preserving output (regression of L-213 FFT check). Trial gating unchanged.

## Test cases
1. 440 Hz 4 s tone at 1.5× → 2.67 s, peak 440 ±1 Hz.
2. 0.5× → 8 s, peak 440 ±1 Hz; display shows 0:08.
3. Preset buttons set the slider; slider has an accessible name.
4. WAV and MP3 outputs open and play.
5. /es title Spanish; title ≤60, meta 140–160; 390 px no overflow.
