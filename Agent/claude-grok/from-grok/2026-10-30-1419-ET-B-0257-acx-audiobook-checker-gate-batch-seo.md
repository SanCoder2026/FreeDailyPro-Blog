Sent: 2026-10-30 14:19 ET

# B-0257 ACX Audiobook Checker: show the pass/fail table before the trial-uses gate; add batch chapters and a level view
Priority: P2 · Estimated effort: M · Report: #143 · Source: Playwright headless, logged out, 0 trial uses, 1280/390 px + curl server HTML + Google top 5 (WebSearch), 2026-10-30 ~14:16–14:18 ET. L-243: no untested tools remain behind live ApyHub APIs, so alphabetical (first 3 untested). No GA/GSC rows for this page in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A narrator should drop a chapter and see at once which ACX numbers pass or fail, before deciding to pay for the corrected MP3.
## Why (repro: a.mp3, 6 s 440 Hz tone, 128 kbps; 1280 px; 0 trial uses)
- **Dropping the file opens "You've used today's trial uses" at once; no measurements are shown** — same pattern as Bates (L-307) and Exhibit Stamper (L-309). Measurements untested; admin run needed (the 128 kbps fixture should FAIL bit rate and room tone).
- About text promises RMS, peak, noise floor, sample rate, MP3 bit rate, length, room tone start (0.5–1 s) and end (1–5 s), pass/fail per line, and a one-click corrected 44.1 kHz 192 kbps CBR MP3 re-checked.
- **Missing vs competitors (~14:17 ET):** whole book / many chapters at once with CSV/PDF report (audiobook.tools); level view with failing spots marked (audiobook.tools); true peak shown beside sample peak (LufsReady); mono/stereo consistency across chapters (audiobook.tools); choose the room-tone sample (Loudness.ai). All show results free.
- No overflow at 390 px. Ad text "Compare Browsers" glued to copy → L-004.
## Who uses this
Indie narrators and authors self-producing for Audible/ACX.
## Outcomes (ranked)
1. Show the pass/fail table at 0 trial uses; gate only the corrected MP3.
2. Several chapters at once with a CSV report.
3. True peak and a level view.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD, all images have alt. /es English → **B-0123**.
  - Title "ACX Audiobook Checker: RMS, Peak, Noise Floor, Bitrate" (54), no brand. Meta 145 ✔. H1 "ACX Audiobook Checker".
- **Keywords:** "acx check", "acx audiobook requirements", "acx rms peak noise floor", "audiobook mastering check".
- **Suggested:**
  - Title: `ACX Check – RMS, Peak & Noise Floor | FreeDailyPro` (50)
  - Meta: keep current (145).
  - H1: `Check an Audiobook Chapter Against ACX Specs`
  - FAQ: "What are the ACX numbers?" (RMS −23 to −18 dB, peak ≤ −3 dB, floor ≤ −60 dB) · "Does passing guarantee approval?" → "No, ACX also listens." · "Is my audio uploaded?" → "No."
## Constraints
Keep the corrected-MP3 download gated per the owner's decision.
## Test cases
1. Fresh session at 0 trial uses, drop a.mp3 → table shows bit rate 128 kbps FAIL.
2. Admin: corrected MP3 is 44.1 kHz, 192 kbps CBR (ffprobe) and re-check passes levels.
3. Title ≤ 60, no "Free".
