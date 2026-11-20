Sent: 2026-11-20 08:40 ET

# Desk findings: Audio Volume Normalizer

- **Sources:** tool page HTML (2026-11-19 15:00 EST), es/ja/ar, the blog, the Audio Tools category, the `AudioNormalizer` / `operations` / `ffmpegEngine` chunks (`evidence/js/`), and Auphonic's docs (WebSearch).

## Copy vs behaviour
1. **"Evens out" contradiction (P1).** The tagline "Even out volume levels across an audio file" appears in:
   - the H1 subtitle
   - the drop zone ("Even out volume levels")
   - the SoftwareApplication description
   - the category card
   - the YouTube title ("Even Out Loud & Quiet Parts")

   About also says "Useful for a recording where volume drifts up and down", and How to use says "evens out the loudness automatically".

   The tool's own "When not to use it" and Limitations say the opposite: "one constant gain… does not even out loud and quiet moments inside a recording". The code confirms a single `volume=` gain (operations L749–754).
2. **Target count.** The FAQ says "The first four targets use LUFS". The guide says "Five of the six targets here are loudness targets". The blog says "five targets as buttons". There are six buttons; Audiobook uses LUFS as an RMS proxy.
3. **Size limit.** The drop zone says "Large files (over 500 MB) may take longer or run out of browser memory", and the dropzone `maxSize` is 500. The engine allows 50 MB on trial uses and 200 MB hard for Pro (`ffmpegEngine` L216–231). Users learn this only after choosing a file (N24).
4. **Peak ceilings.**
   - The table promises ceilings (−1.5 / −1 / −3 dB). Without the limiter the code measures **true peak** (`input_tp`) and holds it (N01 −1.98, N08 −1.55).
   - With "Limit loud peaks" on, the code adds `alimiter` (a sample-peak limiter, no oversampling). True peak reached −0.51 dBTP on a −1.5 target (N09).
   - The Peak target uses `volumedetect` sample peak and reached −0.07 dBTP (N22).
   - Streaming and podcast specs are true-peak (dBTP). Auphonic, for example, uses a 4×-oversampled true-peak limiter.
5. **Lossy margin.** The margin is 0.3 dB for MP3/AAC/Vorbis. AAC still overshot the ceiling by 0.4 dB, and the summary said "couldn't reach −16" while the result was −15.67 (N12).
6. **"A WAV stays lossless".** WAV output is always `pcm_s16le` (operations L61–63), so 24-bit WAV becomes 16-bit without dither (N16). FLAC 24-bit is kept (N15).
7. **"OGG and Opus become OGG".** The bitrate is matched from file size and duration (`M`, L141). Stereo 48 kHz Opus around 45 kbps maps to 32 kbps Vorbis, and libvorbis refuses that, so the job fails (N14). Mono voice notes and 128 kbps Opus work.
8. **Errors.** `de()` shows a generic "Something went wrong… Check the browser console (F12)…". Specific messages already exist in the code ("could not measure the loudness of this file", "could not measure the level of this file") but are not shown.
9. **"How it works" step 2** ("Choose a target", optional) is marked done only when the target is not Podcast (`targetChosen: u !== "podcast"`). The live text reads "2 of 4 steps done. Current step: Download", with step 2 still open.
10. **Copy that checks out:** ACX facts (192 kbps CBR MP3, 44.1 kHz, about −20 RMS, −3 dB peak), Spotify −14 LUFS, EBU R128 −23 LUFS, the "measured on the saved file" second pass (L827–836), the 0.25 LU retry, the >12 dB noise note and the "nothing uploaded" claim (network-verified).

## SEO and indexing
- **Title:** "Audio Normalizer – Normalize to -14/-16 LUFS | FreeDailyPro" (59 characters). Meta is 155 characters. H1 is "Normalize Audio Loudness (LUFS) Online". The canonical is self. No robots meta. Both the tool and the blog are in the sitemap.
- **hreflang:** 10 locales plus x-default. Every locale's `<title>` and meta are English; H1s are translated.
- **JSON-LD:** WebSite, SoftwareApplication (offers price 4.99 USD; description = the contradicted tagline), VideoObject, FAQPage (8), BreadcrumbList.
  - The VideoObject name "How to Normalize Audio Volume Online – Even Out Loud & Quiet Parts" doesn't match the YouTube title "How to Use Audio Volume Normalizer – Free Step-by-Step Walkthrough".
  - The schema uploadDate is 2026-09-22; YouTube's is 20260923.
- **OG image:** the generic `og-default.png`. One empty alt.
- **GSC data is not available.** The TEST-ORDER test-plan figures, quoted as-is: "65 views; 32 clicks pos 28".

## Blog (/blog/audio-normalizer, 2026-10-17)
- A good workflow piece: three guests, then merge.
- **Wrong facts:**
  - "five targets as buttons"
  - "Podcast / Spotify is -16 LUFS with a -1.5 dB peak ceiling. YouTube / streaming is -14 LUFS". Spotify is −14 and a separate button. Podcast is its own button.
  - "Each normalization counts toward your 10 trial usages a day". Live: normalizing is not charged; Download is gated.

## Site placement and overlap
- **Category:** Audio Tools; bundle Podcast Cleanup; "Next: Audio Compressor". Both are correct.
- **C20:** volume-booster (fixed dB gain) is a subset of this tool. audio-compressor means file size.
- **ACX Audiobook Checker:** a separate tool, with the same ACX goal as the Audiobook target, but it also checks the noise floor. Cross-link the two, or route Audiobook to the checker.

## Competitors (completeness)
Auphonic, from its docs (verified 2026-11-19 via WebSearch):
- LUFS or RMS targets
- a 4×-oversampled true-peak limiter
- an adaptive leveler (evens out speakers within a file)
- batch processing
- extra targets (−27 Netflix, ATSC −24)

This tool covers the core constant-gain job well, with an honest summary. Gaps (unverified absence for other competitors):
- true-peak limiting
- a within-file leveler (the copy already promises it in places)
- batch / multi-file matching
- a custom LUFS value
- an LRA / peak report
