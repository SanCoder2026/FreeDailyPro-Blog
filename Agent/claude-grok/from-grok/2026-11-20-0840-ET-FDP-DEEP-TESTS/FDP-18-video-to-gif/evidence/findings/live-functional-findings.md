Sent: 2026-11-20 08:40 ET

# Live functional findings: Video to GIF (headless Chromium unless noted)

- **Written:** 2026-11-19 16:15 EST (box `date`, ET). Runs took place 2026-11-19 15:58–16:12 EST.
- **Measuring:** outputs were taken from the "Result preview" image blob and measured with ffprobe. The loop flag was read from the NETSCAPE2.0 block.
- **Files:** `evidence/json/battery-*.json` and `battery*.log`.
- **Harness note:** the first long run (`battery-run1-settings-carried-over.json`) reused Start/Speed/Width from the previous case, because settings survive New/Reset. Only cases that set every control are counted from it (G02, G07). All other cases were rerun with every control set (`vg-battery.js` now does this and records `carried`).

| Case | Input | Settings | Output (ffprobe) | Verdict |
|---|---|---|---|---|
| G01 | hd1080.mp4 (10 s, 10 Mbps, noisy) | defaults 0/5 s, 480 px, 12 fps | 480×270, 60 frames, 5.01 s, 5.19 MB, loops; 8.6 s incl. engine load | PASS |
| G02 | hd1080 | 2/3 s, 240 px, 5 fps | 240×136, 15 frames, 3.0 s, 0.30 MB | PASS |
| G03 | hd1080 | 0/10 s, 800 px, 20 fps | 42.34 MB, 22.6 s; toast "large; lower the width…" | PASS (honest) |
| G04 | hd1080 | 6 s at 2x | 3.01 s, 36 frames | PASS |
| G05 | hd1080 | 2 s at 0.5x | 4.01 s, 48 frames | PASS |
| G06 | hd1080 | 3 s, Play once | no NETSCAPE loop block (plays once) | PASS |
| G07 | hd1080 | 8 s at 0.5x, 800/20, Largest 2 MB | 220×124, 6 fps, 1.61 MB; "reduced to 220 px, 6 fps to fit 2 MB"; 77.6 s | PASS (220 px is below the 240 px menu minimum) |
| G08 | long60.mp4 | 0/30 s, 640/15, Largest 2 MB | 200×112, 5 fps, **2.15 MB (over 2 MB)**; toast "still over 2 MB at 200 px and 5 fps. Use a shorter clip…" | **FAIL**: the promised "a clip of about N s would fit" hint never appears; it ends over the cap at 200 px |
| G09 | phone.mov (display rotation 90) | 3 s | 480×854 portrait | PASS |
| G10 | hevc.mov | 3 s | 480×270, 2.59 MB | PASS (Chromium) |
| G11 | clip.webm | 3 s | 2.32 MB | PASS |
| G12 | clip.mkv | 3 s | 1.43 MB | PASS |
| G13 | clip.avi (MPEG-4 Part 2 + MP3) | — | "couldn't be read as a video; … Try re-exporting it as MP4." Create GIF disabled | **FAIL**: AVI is listed under "Reads" |
| G14 | clip.wmv (WMV2) | — | same message, disabled | **FAIL**: WMV is listed under "Reads" |
| G15 | clip.flv (FLV1) | — | same message, disabled | **FAIL**: FLV is listed under "Reads" |
| G16 | small320.mp4 (320×240) | Width 800 | 320×240 (no upscale) | PASS |
| G17 | hd1080 | Start 100, Length 0 | clamped to 9.5 / 0.5; 0.51 s GIF | PASS |
| G18 | truncated.mp4 | — | "couldn't be read… may be damaged…" alert, disabled | PASS |
| G19 | notvideo.mp4 (text) | — | same alert (damaged/codec wording; it is not a video at all) | PARTIAL (wording) |
| G20 | big60.mp4 (68.3 MiB) | — | "over 50.0 MB (68.3 MB) — trial use supports up to 50.0 MB. Upgrade to Pro for up to 200.0 MB." + >20 s warning; disabled | PASS (MiB shown as MB) |
| G21 | long60 | Start 50, Length 20 | clamped to 10 s; 9.80 MB; >20 s warning shown on load | PASS |
| G22 | hfr60.mp4 (60 fps) | 640 px, 20 fps, 4 s | 640×360, 20 fps, 1.58 MB | PASS |
| G23 | flat.mp4 (clean test pattern, UI-like) | defaults | 0.80 MB for 5 s | PASS |
| G24 | hd1080 | 10 s, 640/15, Largest 8 MB "(chat apps)" | **550 px, 6 fps**, 6.76 MB; 41.6 s (no-cap 800/20 took 22.6 s) | PARTIAL: fits, but drops to 6 fps (choppy) and leaves 15% of the budget unused |
| G25 | hd1080 | 10 s, 640/15, Largest 5 MB | 440 px, 6 fps, 4.26 MB; 45.9 s | PARTIAL (same pattern) |

## Gate, storage, keyboard (`evidence/json/gate-kbd.json`, 16:09–16:11 EST)

- **Trial strip:**
  - This context loaded with **10 remaining**. Others that hour loaded at 0, and the 16:12 retry loaded at 0 again.
  - **Create GIF was never charged:** about 30 runs, and the count stayed the same in every battery.
  - **Download was charged 1** (0 → 1 used) and saved `noaudio.gif`.
  - At 0 remaining, the result row shows "Get a Day Pass to download".
- **Save to Google Drive:** a Google sign-in popup opened (count 1 → 1). Not signed in.
- **Save to my cloud storage:** a dialog: "Add cloud storage, $4.99 per month, 1 GB… Sign in with your email first…". Stopped there.
- **Day Pass from Download (separate run at 0, 16:17 EST, `cap.json`):** cap dialog → "Buy Day Pass — $1" → email prompt (stopped there). Drive at 0 opens the same cap dialog.
- **Stop:** a progress bar plus Stop appear; Stop gives the toast "Processing stopped." and Create GIF works again.
- **Keyboard:**
  - Tab reaches the drop zone after 28 stops; Enter opens the file chooser.
  - After Create GIF, focus falls to BODY.
- **Screen reader:**
  - The result line "GIF size: … MB" is not in a live region; the only status region is empty.
  - The preview image has alt "Result preview".
  - The progress bar has no accessible name.
- **axe after a file is chosen:** **select-name (critical) ×4**: Width, Frames per second, Speed and Largest file have visible labels that are not tied to the selects. Also link-in-text-block ×3.
- **Result row:**
  - Download, Save to Google Drive, Save to my cloud storage, New. **No share-result button.**
  - Below it: "NEXT STEP: PREMIUM APPLICATION — Universal File Converter (documents, images)" and "Next: Video Thumbnail Generator". Neither fits a GIF; the GIF Resizer & Compressor / GIF Speed, Reverse & Crop tools would.
- **Phones:**
  - iPhone SE (584 px tall): Create GIF sits at y=946 after a file is chosen, so one scroll is needed.
  - Pixel 7: Create GIF at y=887 vs 839.
  - No horizontal overflow in the tool area.

## Browsers (`evidence/json/browsers.json`)

- **Firefox 1440:** a 3 s GIF took 3.2 s (1.42 MB). The file-load check gave:
  - AVI and WMV: "couldn't be read as a video" (blocked).
  - HEVC MOV, MKV, WebM, phone MOV: accepted.
- **WebKit:**
  - The plain control page (blob → `<video>`) crashes, and so does the tool page. This is the same box harness limit as FDP-16/17.
  - **Safari/iOS processing is unverified; check on a real device.**
  - On real Safari, the same `<video>` pre-check would likely also block MKV (and AVI/WMV/FLV). This is an **unverified absence**.
