Sent: 2026-11-20 08:40 ET

# Live functional findings: Compress Video

- **Run:** 2026-11-19 15:31–15:52 EST, guest headless Chromium 1366×900. Firefox was also checked.
- **Starting count:** every context loaded at 10 of 10 used ("Trial: 10 uses/day · 0 remaining today").
- **How outputs were checked:** each output was read from the "Compressed" preview `<video>` blob, the same blob the Download button saves, and measured with ffprobe.
- **Data:** `json/live-cases.json` (merged and measured), `battery*.json`. Inputs are in `testfiles/INPUTS.txt`.

## Cases (cases C01–C20 in `scripts/cv-cases.json`)

| ID | Input | Mode | Tool result | Measured | Verdict |
|---|---|---|---|---|---|
| C01 | hd1080.mp4 12.90 MB, 10 s, 10 Mbps | Medium (default) | 9.65 MB, 25.2% smaller, target 9.67 reached | H.264 1920×1080 + AAC, 10.0 s, faststart | PASS (35 s, first run incl. engine) |
| C02 | hd1080 | Strong | 6.40 MB, 50.4% smaller | 1080p | PASS |
| C03 | hd1080 | Manual Quality 50% | **13.46 MB, 4.4% larger**; "Keep your original" | video 10.7 Mbps (source total 10.3) | PARTIAL: the "caps the bitrate near 90%" FAQ claim didn't hold on this noisy file; honest message |
| C04 | hd1080 | Custom, "8 MB (Discord)" | 7.99 MB, target 8.00 reached | 7,994,456 bytes (decimal MB) | PASS (but see the preset labels) |
| C05 | hd1080 | Custom 2 MB + 720p | 1.91 MB | 1280×720 | PASS |
| C06 | long60.mp4 46.55 MB, 60 s | Custom 8 MB, trim 0:10–0:40 | 7.67 MB, "83.5% smaller than the original" | 30.0 s | PASS. The % compares a 30 s cut with the 60 s original |
| C07 | long60 | Custom 0.5 MB | 1.42 MB, "Target… not reached… Try Strong or 'Lower resolution to 720p'" | video 100 kbps floor + **audio held at ~80–128 kbps** | PARTIAL: the advice is wrong (the source is already 720p; Strong = 50% = 23 MB); audio is never reduced |
| C08 | phone.mov (H.264, rotation 90) | Medium | 7.12 MB | 720×1280 portrait | PASS (rotation honoured) |
| C09 | hevc.mov (HEVC) | Medium | 2.95 MB | H.264 | PASS |
| C10 | clip.webm (VP9/Opus) | Medium | 4.10 MB | MP4 | PASS |
| C11 | clip.mkv | Medium | 5.03 MB | MP4 | PASS |
| C12 | noaudio.mp4 | Medium | 5.06 MB | no audio track added | PASS |
| C13 | efficient.mp4 0.86 MB | Manual 0% | 0.72 MB | — | PASS |
| C14 | efficient | Medium | 0.47 MB (45% smaller vs 25% asked) | — | PASS |
| C15 | hd1080 12.90 MB | Custom 100 MB | **97.03 MB, "652.4% larger… Target reached (100.00 MB)"**, Keep original offered | (blob not captured) | **FAIL (UX)**: 46 s spent making a file 7.5× bigger, labelled "Target reached" |
| C16 | truncated.mp4 | — | Alert "incomplete or damaged (cut off before the end)"; Compress disabled | — | PASS (good pre-check) |
| C17 | notvideo.mp4 (text) | Medium | "Something went wrong… try re-exporting… or check the browser console (F12)" | — | PARTIAL (no crash; misleading phone-codec advice; F12) |
| C18 | big60.mp4 (71.7 MB on disk) | — | "over 50.0 MB (68.3 MB) — trial use supports up to 50.0 MB. Upgrade to Pro for up to 200.0 MB." Compress disabled | — | PASS (good upsell). Units: MiB here, decimal MB in results |
| C19 | Custom "0" | — | "Enter a valid target size" | — | PASS (the number input blocks letters) |
| C20 | trim 0:05 → 0:02 | — | "Check the trim times…" | — | PASS |

- **Mode buttons:** Medium (default, selected), Strong, Manual Quality, Custom Target. **There is no "Light" button** (`json/gate-kbd.json` `modeButtons`).
- **Hint under Medium:** "the encoder aims at the size, and adjusts once if it lands over". The code allows up to 3 encodes (`utils` L54/L70).
- **Firefox 1440:** noaudio.mp4 to Medium gave 5.06 MB in 10.8 s (`json/browsers.json`).
- **WebKit:** the page and file card load in WebKit. Playwright WebKit on this box crashes on any page that loads a video blob into `<video>`, including a blank control page (`browsers.json` `webkitControl`). Processing is therefore unverified on Safari; check on a real device.

## Gate, payment, storage (at 0 remaining)
- **Compress:** never charged (10 → 10). Both previews play in full.
- **Download:** cap dialog (`dlg-download.png`). "Buy Day Pass — $1" leads to the email prompt; the test stopped there (`dlg-daypass.png`).
- **Save to Google Drive:** cap dialog.
- **Save to my cloud storage:** sign-in dialog; untested.
- **"Keep original (download)":** downloads the original free at 0 (`keep.json`). It still shows "Get a Day Pass to download" under it, which contradicts the free download. "Download the larger MP4 anyway" shows the cap dialog.
- **No "Continue with" next-step button** after the result.

## Keyboard and accessibility
- The drop zone is a focusable role=button. Enter opens the chooser after 28 Tabs.
- Mode buttons have no `aria-pressed`. The Manual Quality slider has no accessible name (`aria-label`/`labelledby` null).
- The result line is not in a live region. Focus goes to `<body>` after Compress.
- axe on `main` (idle and result): 0. Matrix: 1 serious label/name mismatch (desktop), and ad-label contrast on Pixel 7.

## Phones (Chromium emulation)
- **iPhone SE (innerHeight 584):** the drop zone starts at y=615, just below the fold; Compress is at 949 after a file is added.
- **Pixel 7:** drop zone at 553 (visible); Compress at 831 against 839.
- **iPhone SE 320 px (WebKit matrix):** a 9 px overflow from the header "Open menu" (site-wide).
