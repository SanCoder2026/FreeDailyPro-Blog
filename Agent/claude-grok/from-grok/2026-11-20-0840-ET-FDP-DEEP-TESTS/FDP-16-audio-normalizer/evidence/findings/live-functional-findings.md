Sent: 2026-11-20 08:40 ET

# Live functional findings: Audio Volume Normalizer

- **Run:** 2026-11-19 15:01–15:22 EST, guest Chromium 1366×900 (headless Playwright). Firefox was also checked.
- **Starting count:** every context loaded at 10 of 10 used ("Trial: 10 uses/day · 0 remaining today").
- **How outputs were checked:** each output was read from the preview `<audio>` blob, which is the same blob the Download button saves. It was measured on the box with ffmpeg 6 `loudnorm` (integrated LUFS and true peak), `volumedetect` (sample peak) and `ffprobe`.
- **Data:** `json/live-cases.json`. Inputs are in `testfiles/INPUTS.txt`.

## Cases

| ID | Input | Target | Tool summary | Measured output | Verdict |
|---|---|---|---|---|---|
| N01 | quiet.wav (−30.3 LUFS) | Podcast | −30.3 → −16.0 (+14.3 dB) + noise note | −16.00 LUFS, TP −1.98 dBTP, 16-bit WAV | PASS |
| N02/N03 | quiet.wav | Spotify / YouTube | −15.1, "loud peaks stop it" | −15.07, TP −1.05 | PASS (honest limit message) |
| N04 | quiet.wav | Broadcast | −23.0 | −23.00, TP −8.98 | PASS |
| N05 | quiet.wav | Audiobook (ACX) | −20.0, "192 kbps CBR MP3 at 44.1 kHz" | MP3 192k, 44.1 kHz, RMS −22.5 dB, sample peak −6.4 | PASS (RMS inside ACX −23…−18, near the low edge) |
| N06 | quiet.wav | Peak to −1 dB | −16.9 → −1.0 dB | sample peak −1.0, **TP −0.47 dBTP** | PARTIAL (sample peak, not true peak) |
| N07 | loud.wav (−10.6) | Podcast | −10.6 → −16.0 (−5.4 dB) | −16.01 | PASS |
| N08 | spike.wav (−32.0, one 0.99 click) | Podcast, limiter off | −31.6, "peaks stop it… −1.5 dB" | −31.65, TP −1.55 | PASS |
| N09 | spike.wav | Podcast, **limiter on** | −16.0 (+16.4 dB), no warning | −16.00, **TP −0.51 dBTP** (ceiling −1.5) | **FAIL**: true-peak ceiling broken by 1 dB |
| N10 | vquiet.wav (−46.4) | Podcast | +30.4 dB + noise warning | −16.01 | PASS |
| N11 | quiet.mp3 128k | Spotify | −16.0, limited; "Saved at 128 kbps" | MP3 128k, −15.98 | PASS |
| N12 | quiet.m4a 96k | Podcast | **−15.7**, "The target is −16, but the loud peaks stop it going louder" | −15.67, **TP −1.11** | FAIL (minor): louder than target while saying it couldn't reach it; AAC overshoots the −1.5 ceiling by 0.4 dB |
| N13 | quiet.ogg | Podcast | −15.8; "Saved at 64 kbps" | Vorbis 64k, −15.77 | PASS |
| N14 | quiet.opus (stereo 48 kHz, ~45 kbps) | Podcast | "Something went wrong… Check the browser console (F12)…" | — | **FAIL**: console shows `libvorbis encoder setup failed`; the matched bitrate (32 kbps) is too low for stereo 48 kHz Vorbis |
| N25 | opus128.opus | Podcast | −16.0; "Saved at 80 kbps" | OK | PASS (higher-bitrate Opus works) |
| N26 | voicenote-opus16k.ogg (mono Opus) | Podcast | −19.3, limited; "Saved at 32 kbps" | OK | PASS |
| N15 | quiet24.flac (24-bit) | Podcast | −16.0 | FLAC, 24-bit kept | PASS |
| N16 | quiet24.wav (24-bit) | Podcast | −16.0 | **16-bit WAV** (`pcm_s16le`) | FAIL (minor): bit depth reduced; FAQ says "a WAV stays lossless" |
| N17 | mono.wav | Podcast | −18.6, limited | mono kept | PASS |
| N18 | silence.wav | Podcast | generic "Check the browser console (F12)" | — | FAIL (UX): code has "could not measure the loudness of this file" but the UI shows the generic text |
| N19 | short03.wav (0.3 s) | Podcast | same generic text | — | FAIL (UX): same |
| N20 | corrupt.mp3 (text) | Podcast | same generic text | — | PARTIAL: no crash; message unhelpful |
| N21 | clip.mp4 (via script; picker accepts `audio/*` only) | Podcast | −16.2; M4A 192k | AAC M4A | PASS (copy says MP4 becomes M4A) |
| N22 | loud.wav | Peak to −1 dB | −3.0 → −1.1 dB | sample peak −1.1, **TP −0.07 dBTP** | PARTIAL: almost at 0 dBTP |
| N23 | quiet.mp3 | Audiobook | −20.2; 192k CBR note | MP3 192k CBR 44.1 kHz | PASS |
| N24 | big60.wav (60.6 MB) | — | "You've selected a file over 50.0 MB (60.6 MB) — trial use supports up to 50.0 MB. Upgrade to Pro for up to 200.0 MB." Normalize disabled | — | PASS (good upsell). The page says "Large files (over 500 MB) may take longer" (see desk findings) |

- **Speed:** every case took 1–4 s after the first engine load (about 25 MB from cdn.jsdelivr.net).
- **Firefox 1440:** quiet.mp3 to Podcast gave −16.6, limited, in 2.4 s (`json/browsers-kbd.json`).
- **WebKit:** not verifiable on this box. Playwright WebKit crashes when *any* page loads an audio blob into `<audio>`, including a blank control page with no FreeDailyPro code (`json/webkit-control.txt`, `webkit-retry.json`). This is a harness limit, not a site finding; check on a real iPhone/Mac.

## Gate, storage, sharing, payment (at 0 remaining)
- Normalize was never charged: the count stayed 10 → 10 across all runs. The full-length result plays in the preview player at 0 remaining. Download is gated.
- **Download:** cap dialog "Today's trial uses are done… downloading needs a pass" (`screens/live/dlg-download.png`). Focus moves into the dialog. A "0 remaining today Get a Day Pass to download" status line sits under the button.
- **Buy Day Pass — $1:** "Day Pass, $1. Enter your email and go straight to payment." The test stopped there (`dlg-daypass.png`). Nothing was typed.
- **Save to Google Drive:** same cap dialog (`dlg-drive.png`).
- **Save to my cloud storage:** "Cloud storage… Sign in with your email first…" (`dlg-cloud.png`). Sign-in is needed, so this is untested.
- **Continue with Audio Compressor:** goes to /tool/audio-compressor and shows "Use the result from Audio Volume Normalizer: normalized_quiet.wav". This confirms the output file name (`continue-with.png`).
- **Share this tool:** no visible dialog or toast in headless Chromium. Unverified; the native share sheet needs a real phone.
- **Privacy:** after the page load, the only network requests were the engine files from jsdelivr, blob: URLs and `usage.check` GETs. No request carried the audio (`json/probe.json` `net`).

## Keyboard and accessibility
- The drop zone is a focusable `role=button`. Enter opens the file chooser after about 27 Tabs (`browsers-kbd.json`).
- Target buttons have no `aria-pressed`, so the selected target is shown only by colour.
- After Normalize, focus falls to `<body>`. The summary line is not in a live region, so screen readers hear only the "Volume normalized!" toast, not the LUFS result.
- axe on `main`, idle and with a result: 0 violations (`gate-kbd.json`). The matrix found 1 serious `label-content-name-mismatch` on the desktop page and 2 colour-contrast nodes in the ad label text on Pixel 7.

## Phones
- **iPhone SE (375×667 emulation, innerHeight 584):** the drop zone starts at y=724, below the fold. Target buttons start at 822 and Normalize at 1166 after a file is added (`layout-iphone-se-idle.png`).
- **Pixel 7:** the drop zone is at 569 (visible). Normalize is at 995 against an 839 px viewport.
- **iPhone SE 320 px (matrix, WebKit):** a 9 px horizontal overflow from the header "Open menu" button (site-wide; `json/se-overflow.json`).
