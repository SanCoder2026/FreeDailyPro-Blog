Sent: 2026-11-20 22:45 ET

# Test cases: FDP-18 Video to GIF (rerun after any fix)

"Today" = observed 2026-11-19 15:58–16:17 EST in headless Chromium. Cases G01–G25 are in `scripts/vg-cases.json`; run them with `node scripts/vg-battery.js [IDs]` (every control is set per case).

| ID | Input / action | Expected | Today |
|---|---|---|---|
| VG-01 | hd1080 defaults | 480 px, 12 fps, 5 s, loops | PASS (5.19 MB, noisy source; clean source 0.80 MB) |
| VG-02 | 240 px / 5 fps / 3 s | small GIF | PASS (0.30 MB) |
| VG-03 | 800 px / 20 fps / 10 s, no limit | completes; "large" advice | PASS (42.3 MB, 23 s) |
| VG-04 | Speed 2x, Length 6 | 3 s GIF | PASS |
| VG-05 | Speed 0.5x, Length 2 | 4 s GIF | PASS |
| VG-06 | Play once | no NETSCAPE loop block | PASS |
| VG-07 | Largest 2 MB from 800/20 (8 s at 0.5x) | ≤ 2 MB, says what was reduced | PASS (220 px, 6 fps, 1.61 MB) |
| VG-08 | long60, 30 s, 640/15, Largest 2 MB | ≤ 2 MB, or shows "about N s would fit" | **FAIL** (2.15 MB at 200 px, no hint) |
| VG-09 | phone.mov (rotation 90) | portrait | PASS (480×854) |
| VG-10 | hevc.mov / clip.webm / clip.mkv | GIF | PASS (Chromium) |
| VG-11 | clip.avi / clip.wmv / clip.flv | GIF (listed under Reads) | **FAIL** (refused as damaged) |
| VG-12 | small320.mp4, Width 800 | 320 px (no upscale) | PASS |
| VG-13 | Start 100, Length 0 on 10 s | clamps to 9.5 / 0.5 | PASS |
| VG-14 | truncated.mp4 | damaged-file alert, disabled | PASS |
| VG-15 | notvideo.mp4 | "not a video" message | PARTIAL ("damaged or codec" wording) |
| VG-16 | big60.mp4 (guest) | 50 MB message; page copy matches | PARTIAL (message good; drop zone says 200 MB) |
| VG-17 | long60 Start 50 Length 20 | clamps to 10; >20 s warning | PASS |
| VG-18 | Largest 8 MB, 640/15, 10 s | ≤ 8 MB at a usable fps | PARTIAL (6 fps, 6.76 MB, 42 s) |
| VG-19 | Stop mid-run | "Processing stopped.", can rerun | PASS |
| VG-20 | At 0: Download → cap → Day Pass | email prompt (stop) | PASS |
| VG-21 | With uses: first Download | +1 used, `<name>.gif` | PASS (0 → 1, noaudio.gif) |
| VG-22 | Second Download, bytes vs preview (`scripts/vg-reset.js`) | no second charge; same bytes | **Pending: needs re-run after midnight UTC (7:00 PM ET)** |
| VG-23 | Keyboard and screen reader | Enter opens chooser; selects named; result announced; focus on result | PARTIAL (Enter works; others missing) |
| VG-24 | Copy consistency | Reads list, fit hint, 200 vs 50 MB, trim advice, video UI all match | **FAIL** |

---

## Updates from the 2026-11-20 re-run (see RERUN-FINDINGS.md)

| ID | 2026-11-20 result |
|---|---|
| VG-22 | Second download not charged again; same bytes as the preview. **First download moved the count 0 → 10** (display-only, P1) |
