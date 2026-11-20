Sent: 2026-11-20 08:40 ET

# Compare Two Audio Files: YouTube video findings (checks 10, 12)

- **Written:** 2026-11-19 10:26:24 EST (box `date`, ET).
- **Video:** https://www.youtube.com/watch?v=KZVe2ILAUD4. Embedded on the tool page and on /blog/audio-comparer.
- **Method:**
  - Downloaded with yt-dlp (`--js-runtimes node -f 136`, 720p video-only).
  - Read the metadata (`video-KZVe2ILAUD4.info.json`) and both caption tracks (`.en-US.vtt` burned-in titles; `.en-orig.vtt` auto captions).
  - Sampled 15 frames, one every 5 s (`frames/f01–f15.jpg`, contact sheet `video-contact-1.jpg`).
  - **It was not watched with sound.** The summary comes from captions, metadata and frames. The .mp4 is not in the zip.

## Metadata

- **Title:** "How to Use Compare Two Audio Files – Free Step-by-Step Walkthrough".
- **Length and views:** 77 s, 14 views (yt-dlp read on 2026-11-19).
- **Uploaded:** 2026-09-23 08:26:54 EDT.
- **Description:** accurate on the core idea ("…shows how much of the sound matches, as a percentage, and where they differ… Runs entirely in your browser"). It also says "Try Compare Two Audio Files **free**" and "**Free** daily u[ses]…".
- **Tags:** FreeDailyPro, free online tools, **PDF tools**, browser tools, no upload, privacy. None about audio comparison.
- **Title mismatch:** the JSON-LD VideoObject is "How to Compare Two Audio Files Online – Similarity Percentage", and the sitemap video title is "How to Compare Two Audio Files Online Free – Similarity Percentage". Three different titles in total.

## Captions

- **en-US (burned-in cards):**
  - 0:00 "How to Compare Two Audio Files Online Free – Similarity Percentage"
  - 0:05–0:50 "Follow along — free in your browser"
  - 0:50 "Subscribe for the next free tool"
  - 0:57 "Finish on FreeDailyPro.com"
- **Auto captions:** music, plus "Subscribe so you don't miss the next free tool." There is no narration explaining the result.

## What the frames show vs. the live tool

| In the video | Live tool today |
|---|---|
| Thumbnail "AUDIO COMPARE 98% MATCH Wow." | Score, verdict and per-second strip |
| Two file boxes, then a single "Similarity 62.8% — Similar…" card | Verdict sentences ("Partly the same…", "Same recording; file 2 starts 0.50 s later"), "Differs at 0:05–0:07", per-second strip, three waveforms incl. difference, A/B Play file 1/2, Match loudness, property table (duration, rate, channels, size, LUFS, peak), Download the difference (WAV), Copy result summary |
| No trial-use strip | "Trial: 10 uses/day · N remaining today" plus $1 / $4.99 passes |
| Outro "200+ Free Productivity Tools" | Header "Search 300+ tools…"; brand wording is Professional Tools / trial uses |

## Verdict

- **Check 10 (video exists): PARTIAL.** It exists and is embedded, but has low reach (14 views) and off-topic tags.
- **Check 12 (video shows current capabilities): FAIL.**
  - It shows the old single-percentage UI and none of the 2026-11 features.
  - It uses "free" wording in the title, description, cards and outro.
- **Recommendation:** re-record about 60–75 s on the current UI. Use pair 12 (an edit in the middle → "Differs at 0:05–0:07", red cells, difference WAV) and pair 9 (an offset recording auto-aligned).
  - Use Professional Tools / trial uses wording.
  - Use one title everywhere (YouTube, JSON-LD, sitemap).
  - Use audio-specific tags.
