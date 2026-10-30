Sent: 2026-10-30 14:17 ET

Supersedes 2026-10-30-1416-ET-B-0254-screen-recorder-timer-audio-seo.md
Change: suggested title no longer leads with 'Free' (owner positioning rule); the suggested 'No Download, No Install' version is 63 characters, so it uses 'No App to Install'. Everything else unchanged.

# B-0254-v2 Screen Recorder: fix the live timer, add audio/mic and MP4, say "no watermark, no time limit"; real meta
Priority: P2 · Estimated effort: M · Report: #142 · Source: SEO backfill 8, curl server HTML + seo.py + Google top 5 (WebSearch), 2026-10-30 ~14:15–14:16 ET. Already tested (L-236). GA rank 37, 58 views (`analytics/2026-07-10-to-now-raw.md`); no GSC row in the cited files.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone making a quick demo or bug report should record a tab or screen with sound and get a file that plays everywhere.
## Why
- L-236 (admin session): recording works with a 3-2-1 countdown; WebM VP9 1920×1200 ~29.8 fps, 13.78 s, **no audio**; **"Recorded 00:13" matches the file but the live timer showed ~00:07 at stop.**
- Title "Record Your Screen Online - No App Needed | FreeDailyPro" (56) OK. **Meta 83.** H1 "Screen Recorder".
- **Top 5 offer (~14:16 ET):** tab/system audio + microphone (screenrecorder.dev, Audo, Bandicam); webcam overlay (Bandicam, Audo); MP4 where the browser supports it (ScreenWhim, Audo); trim and GIF export (pixelpix, Audo); drawing while recording (Bandicam); clear "no watermark, no time limit" and "phones can't record from a web page" notes (ScreenWhim, pixelpix).
## Who uses this
Teachers, support staff and developers recording demos and bug reports.
## Outcomes (ranked)
1. Live timer matches real elapsed time (L-236).
2. Tab/system audio and mic options; say when audio isn't available.
3. MP4 output where supported; trim before download.
4. Webcam overlay.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD; → **B-0209**; /es English → **B-0123**.
- **Keywords:** "screen recorder online", "record screen online free", "screen recorder no download", "record browser tab".
- **Suggested:**
  - Title: `Online Screen Recorder – No App to Install | FreeDailyPro` (57)
  - Meta: `Record your screen, a window or a browser tab right in your browser, optionally just a region. No app, no upload: the video is saved straight to your device.` (157)
  - H1: `Record Your Screen Online`
  - FAQ: "Does it record sound?" (state current truth) · "Which format?" → WebM (MP4 when built) · "Does it work on phones?" → "No, browsers don't allow it."
## Constraints
Don't claim audio or MP4 until shipped.
## Test cases
1. Admin: 15 s recording → live timer at stop within ±1 s of file duration.
2. Title ≤ 60; meta 140–160.
