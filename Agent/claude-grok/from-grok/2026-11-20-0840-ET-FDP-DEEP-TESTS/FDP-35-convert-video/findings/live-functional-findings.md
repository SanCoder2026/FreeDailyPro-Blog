Sent: 2026-11-21 02:08 ET

# FDP-35 Video Converter: live functional findings (guest, headless Chromium, Playwright 1.65, 2026-11-21 01:50–02:03 EST)

Test files: synthetic, `testfiles/make-videos.sh` (V01–V17, A13, X14). Results: `json/cases-chromium.json` (K01–K23), `json/gate.json`, `json/pairs.json`, `json/probe.json`. Saved previews: `testfiles/outputs/` (ffprobe lines are in the case JSON).

## Conversions (all in the browser; ffmpeg.wasm 0.12.10 from cdn.jsdelivr.net, as the Privacy copy says)
| Case | Input → output | Result |
|---|---|---|
| K01 | H.264/AAC MP4 → MP4 | copied (rewrap) 0.6 s, "+0%", note "This file is already an MP4…" PASS |
| K02 / K03 | same → MOV / MKV | copied 0.4–0.6 s PASS |
| K04 | → WebM | VP8/Vorbis 1280×720, 2.9 s, −68 % PASS |
| K05 | → AVI | MPEG-4/MP3, +130 % (page warns) PASS |
| K06 | 1080p H.264 MOV → MP4 | copied PASS |
| K07 | HEVC MOV (iPhone-style) → MP4 | re-encoded H.264/AAC, 5.7 s PASS |
| K08 | VP9/Opus WebM → MP4 | re-encoded, +161 % with the "MP4 is often larger… normal" note PASS |
| K09 | H.264 MKV → MP4 | copied PASS |
| K10–K12 | AVI (MPEG-4), WMV, FLV → MP4 | re-encoded PASS |
| K13 | 3GP (H.264/AAC) → MP4 | copied PASS |
| K14 | animated GIF → MP4 | 199 KB → 61 KB PASS |
| K15 | H.264 no audio → MOV | copied PASS |
| K16 | H.264 + MP3 audio → MP4 | re-encoded (audio not AAC) PASS |
| K17 | MP3 audio only | rejected: `"A13_audio_only.mp3" isn't a video file` PASS |
| K18 | text file renamed .mp4 | accepted, then after 11.6 s a generic toast blaming "a codec this tool doesn't support (some phone-recorded .mov files…)" — misleading for a non-video (P3) |
| K19 | 1920×1080 VP8 WebM → WebM | scaled to 1280×720 as documented PASS |
| K20 | 60 s 40 MB MP4 → WebM | 33 s, 7.5 MB PASS |
| K21 | 70.6 MB MP4 | Convert disabled: "You've selected a file over 50.0 MB (70.6 MB) — trial use supports up to 50.0 MB. Upgrade to Pro for up to 200.0 MB." Works as the blog says; contradicts the drop zone's "Large files (over 5 GB) may take longer" (P2) |
| K22 | → MP4 for web | same file as MP4 (byte size equal), as the FAQ admits PASS |
| K23 | WebM → WebM | allowed with "already a WebM… pick MP4" note PASS |

- Pair pages (`json/pairs.json`): mov-to-mp4, mp4-to-webm, gif-to-mp4, mp4-to-avi, wmv-to-mp4 preselect the target. PASS.

## Privacy (PASS)
- No request with a body over 20 KB and no third-party host except jsDelivr (engine). The video never leaves the device.

## Trial use, gate and payment
- `json/gate.json`, uses-left context (loaded `usageToday` 0), 02:00:59–02:02:36 EST:
  - Convert V01 → MOV: 0 → 0 (Convert is free).
  - Download A: 0 → **1**. Download A again: 1 → 1.
  - Save to Google Drive → Google sign-in popup (stopped). Save to my cloud storage → "Sign in with your email first… $4.99 per month, 1 GB" (stopped).
  - New → V09 → MP4 → Download B: 1 → **1** (free). New → V11 → MOV → Download C: 1 → **1** (free).
  - Reload → V05 → MP4 → Download D: 1 → **2**. Reload: 2.
  - So **one trial use per page load**: later Downloads of other videos are free until reload. Shared code (`Kt` set in `index-*.js`, see FDP-34). Santosh's Nov 20 decision is that Downloads charge every time (Barcode, Invoice); this is a **P1 gate gap that conflicts with that decision**.
- **Preview gives the file away (P1).** The result `<video controls>` plays a blob that is byte-identical to the Download (sha256 `0762f787…` for the uses-left Download, the uses-left preview and the **at-0 preview**). It has no `controlslist="nodownload"`, so Chrome's built-in player menu offers Download, and "Save video as…" works too (neither clicked). At 0 the page's Download is blocked, so this bypasses the gate.
- At 0 (`gate.json` zero, 02:02:41 EST): Convert works; Download → cap dialog "Today's trial uses are done … downloading needs a pass… Monthly $4.99 … Day Pass $1" → Buy Day Pass → "Day Pass, $1 … Email | Continue to payment" (stopped). Quick Buy day → same email prompt; Quick Buy monthly → Stripe Checkout (session id redacted; stopped). 10 → 10.
- Cap dialog says passes remove the "Created with FreeDailyPro.com" mark; converted videos carry no mark (P3 copy).
- Trial uses spent: **2** (display-only).

## Keyboard / a11y
- Drop zone: Tab (28 stops) + Enter opens the file chooser (PASS). Output select is a labelled combobox. Two "Quick Buy" buttons with the same name.

## Share / print
- Share copies only the tool URL (`json/share.json`). Print (`testfiles/outputs/print-preview.pdf`) shows the page.
