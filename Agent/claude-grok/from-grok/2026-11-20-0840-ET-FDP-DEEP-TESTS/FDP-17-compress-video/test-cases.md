Sent: 2026-11-20 08:40 ET

# Test cases: FDP-17 Compress Video (rerun after any fix)

"Today" = observed 2026-11-19 15:31–15:52 EST in headless Chromium. Cases C01–C20 are in `scripts/cv-cases.json`; run them with `node scripts/cv-battery.js [IDs]`. Pass rule for targets: output bytes ≤ target (decimal MB) and the duration is correct.

| ID | Input / action | Expected | Today |
|---|---|---|---|
| CV-01 | hd1080 → Medium | ≤ 75% of the source, 1080p MP4 | PASS (9.65 / 9.67) |
| CV-02 | hd1080 → Strong | ≤ 50% | PASS (6.40 / 6.45) |
| CV-03 | hd1080 → Custom 8 MB preset | ≤ 8,000,000 bytes | PASS (7,994,456) |
| CV-04 | hd1080 → Custom 2 + 720p | ≤ 2 MB, 1280×720 | PASS (1.91) |
| CV-05 | long60 → Custom 8, trim 0:10–0:40 | 30 s, ≤ 8 MB | PASS (7.67) |
| CV-06 | long60 → Custom 0.5 | reached, or a miss with advice that fits (audio, 480p, trim) | PARTIAL (1.42 MB; generic advice) |
| CV-07 | phone.mov (rotation 90) | portrait output | PASS (720×1280) |
| CV-08 | hevc.mov / clip.webm / clip.mkv | MP4 H.264/AAC | PASS |
| CV-09 | noaudio.mp4 | no audio added | PASS |
| CV-10 | efficient.mp4 Manual 0% / Medium | not larger | PASS |
| CV-11 | hd1080 → Manual 50% | not larger, or honest + Keep original | PARTIAL (4.4% larger, honest) |
| CV-12 | hd1080 → Custom 100 MB | no encode up; "already under" | **FAIL** (97 MB "Target reached") |
| CV-13 | truncated.mp4 | pre-check alert, Compress disabled | PASS |
| CV-14 | notvideo.mp4 | "not a video" message, no F12 | PARTIAL |
| CV-15 | big60.mp4 (guest) | 50 MB message; page copy matches | PARTIAL (message good; page says 200 MB) |
| CV-16 | Custom 0 / trim end < start | validation toasts | PASS |
| CV-17 | Preset labels | match current Discord / WhatsApp / email limits | **FAIL** (8 / 16 MB) |
| CV-18 | Copy: modes, default, passes | match the UI and code | **FAIL** |
| CV-19 | Download / Drive / larger-anyway at 0 | cap dialog → Day Pass → email (stop) | PASS |
| CV-20 | Keep original at 0 | free download, no pass text under it | PARTIAL (pass text shown) |
| CV-21 | Download with uses left (`scripts/cv-reset.js`) | count +1, `compressed_<name>.mp4`, same bytes as the preview | **Pending: needs re-run after midnight UTC (7:00 PM ET)** |
| CV-22 | Keyboard and screen reader | Enter opens the chooser; mode state, slider name, result announced | PARTIAL (Enter works; others missing) |
