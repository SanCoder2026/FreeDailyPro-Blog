Sent: 2026-11-21 01:26 ET

# FDP-33 Video Thumbnail Generator: live functional findings (guest, headless Chromium, 2026-11-21 00:57–01:12 EST)

Test videos (synthetic, ffmpeg testsrc2; `testfiles/make-videos.sh` recreates them): V1 1920×1080 H.264 30 fps 10 s (+AAC), V2 1080×1920 H.264, V3 1280×720 VP9 WebM 25 fps 5 s, V4 1280×720 HEVC (hvc1), V5 4 s black, X1 a .txt file, X2 a text file renamed .mp4. Results: `json/cases-*.json`, `json/gate.json`, `json/drain.json`, `json/fake-mp4-hang.json`. Captured images: `testfiles/outputs/`.

## Capture (PASS)
- V1 (H.264), V2 (portrait), V3 (WebM) play in the page; typing 0:03.5 + Enter seeks; Capture adds a PNG at the source size (1920×1080, 1080×1920, 1280×720) in ~0.6 s; toast "Captured at 3.50 s (W x H px)".
- Sizes (V3): YouTube HD 1280×720, YouTube 4K 3840×2160, Shorts 4K 2160×3840, Shorts/Reels 1080×1920 (Fit adds black bars), Square 1080×1080 (Fill crops). JPG option gives image/jpeg (1280×720: 60 KB vs PNG 201 KB). File names follow `video_00m03.53s_<size>[_title].<ext>`.
- Title: Devanagari, emoji and accented Latin render correctly with outline; a long title wraps within ~90 % width (`testfiles/outputs/V3_720p__sq_fill_title.png`, `…yt_title_long.png`). The "Impact style" font falls back to a bold sans on Linux (no Impact installed) — expected.
- Time box: "0:59" on a 5 s clip clamps to the end (5.00 s) but the box keeps showing 0:59 (P3). "abc" + Enter → toast "Use a time like 1:05.5 or 65.5" (PASS).
- "+1 frame" moves by 1/30 s (3.50 → 3.53) on a 25 fps clip; it still landed on a different frame here, but on 50/60 fps video a "+1 frame" press skips frames and on 24/25 fps it can repeat one (step is fixed at 1/30 s; copy says so). P3.
- **Upscaling:** "YouTube 4K 3840 x 2160 (recommended)" and "Shorts 4K … (recommended)" upscale a 720p source 3× with no warning (`V3_720p__yt4k_fill.png`, 1.16 MB PNG). Labelling an upscale "recommended" promises quality the source can't give (P2). Whether YouTube currently accepts/needs 4K thumbnails was not verified here.
- Suggest frames (V3): 10 previews at 0.25…4.75 s in ~1.3 s, star on 0:03.75; clicking jumps (PASS).

## Fallback and errors
- V4 HEVC: Chromium can't play it → message "Your browser can't play this video (often iPhone HEVC video)…"; typing 0:03.5 + Capture → 1280×720 PNG in ~1.8 s via ffmpeg.wasm loaded from `cdn.jsdelivr.net` (@ffmpeg/core 0.12.10) — matches the Privacy copy (CDN only for unplayable videos; V1–V3 made no CDN request).
- X1 (.txt): toast `"X1_notvideo.txt" isn't a video file` (PASS).
- X2 (text renamed .mp4): accepted as a video, shows the "often iPhone HEVC" message, Capture → toast "Could not read that frame from the video" within 1 s (`json/fake-mp4-hang.json`). Message is misleading for a broken/non-video file (P3).

## Privacy (PASS)
- No POST over 50 KB and no upload/storage request in any run (`bigPosts: []`); the video never leaves the device. Share copies only the tool URL (`json/share.json`, 01:12 EST).

## Trial use, badge and payment (key results)
- `json/gate.json` (2026-11-21 01:08:33–01:09:37 EST) — this fresh context loaded **with uses left** (strip "Trial: 10 uses/day · 10 remaining today", `usageToday` 0):
  - Upload, 2 Captures: 0 → 0 (uncounted; the page labels "Download uses 1 trial use").
  - Per-image **Download**: 0 → **1**, file `…_yt.png` with the intentional "Created with FreeDailyPro.com" badges (top and bottom right).
  - **Download all as ZIP (2)**: 1 → **1**, no dialog, `V3_720p_frames.zip` with both images (badged, identical to the single download). **A ZIP of N frames costs no trial use while one single image costs one** (P1; one observation).
  - Save to Google Drive → Google sign-in popup (**blocked by sign-in**, not continued). Save to my cloud storage → dialog "Add cloud storage, $4.99 per month, 1 GB… Sign in with your email first" (stopped).
  - After reload: 1.
  - Quick Buy (day) → "Day Pass, $1 … Email | Continue to payment" (email field shown; nothing typed). Quick Buy (monthly) → Stripe Checkout page (`checkout.stripe.com`, session id redacted); stopped, nothing typed.
- `json/drain.json` (01:10 EST) — next fresh context loaded **at 0**: per-image Download → cap dialog "Today's trial uses are done … downloading needs a pass… Monthly for $4.99 … Day Pass for $1" → Buy Day Pass → email prompt (stopped). At 0: ZIP → same cap dialog (blocked); Download again → dialog; Capture and Suggest still work (results free, download gated). 10 → 10 after reload.
- So the download gate works at 0 for both paths; the gap is the ZIP not being charged with uses left. Trial uses spent by this test: **1**.
- Count the Nov 20 decision: this tool is not in the uncounted list; it charges per Download like Barcode/Invoice, except the ZIP → **policy question / loophole** (P1). Pending confirmation of the ZIP result in a second uses-left context (RERUN row 33).

## Keyboard / a11y (live)
- The drop zone ("Drop a video or click to browse", role=button) is reachable by Tab and Enter opens the file chooser (PASS).
- The two strip buttons are both named "Quick Buy" (no price/plan in the accessible name) (P3).

## Print
- Browser print (`testfiles/outputs/print-preview.pdf`, 2 pages) of a page with a capture: player area, controls and the gallery image; no dedicated print action (none promised).
