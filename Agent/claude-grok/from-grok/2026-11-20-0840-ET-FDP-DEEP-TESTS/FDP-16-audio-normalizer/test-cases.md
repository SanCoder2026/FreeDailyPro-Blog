Sent: 2026-11-20 08:40 ET

# Test cases: FDP-16 Audio Volume Normalizer (rerun after any fix)

"Today" = observed 2026-11-19 15:01–15:22 EST in headless Chromium. Cases N01–N26 are in `scripts/an-cases.json`; run them with `node scripts/an-battery.js [IDs]`, then measure the `out-N*.bin` files with ffmpeg (see `scripts/README.md`). Pass rule for LUFS targets: within ±0.5 LU of the target, **and** true peak ≤ the ceiling, or an honest "couldn't reach" message when not.

| ID | Input / action | Expected | Today |
|---|---|---|---|
| AN-01 | quiet.wav → Podcast | −16 ±0.5 LUFS, TP ≤ −1.5 dBTP | PASS (−16.00 / −1.98) |
| AN-02 | quiet.wav → Spotify, YouTube | −14 or honest limit; TP ≤ −1 | PASS (−15.07, message) |
| AN-03 | quiet.wav → Broadcast | −23 | PASS |
| AN-04 | quiet.wav, quiet.mp3 → Audiobook | MP3 192k CBR 44.1k; RMS −23…−18; peak ≤ −3 | PASS |
| AN-05 | quiet.wav → Peak to −1 dB | TP ≤ −1 dBTP | PARTIAL (sample −1.0, TP −0.47) |
| AN-06 | loud.wav → Podcast | lowered to −16 | PASS |
| AN-07 | spike.wav → Podcast, limiter off | stays below; message names the ceiling | PASS |
| AN-08 | spike.wav → Podcast, limiter on | −16 and TP ≤ −1.5 | **FAIL** (TP −0.51) |
| AN-09 | vquiet.wav → Podcast | +30 dB with noise warning | PASS |
| AN-10 | quiet.mp3 → Spotify | MP3, bitrate matched | PASS (128k) |
| AN-11 | quiet.m4a → Podcast | ≤ −16 and TP ≤ −1.5, message consistent | **FAIL** (−15.67, TP −1.11, "couldn't reach") |
| AN-12 | quiet.ogg → Podcast | OGG | PASS |
| AN-13 | quiet.opus (stereo ~45 kbps) → Podcast | OGG saved | **FAIL** (libvorbis setup failed) |
| AN-14 | opus128.opus, voicenote-opus16k.ogg | OGG saved | PASS |
| AN-15 | quiet24.flac | FLAC 24-bit | PASS |
| AN-16 | quiet24.wav | WAV 24-bit (or copy says 16-bit) | **FAIL** (16-bit) |
| AN-17 | mono.wav | mono kept | PASS |
| AN-18 | silence.wav, short03.wav | specific, actionable message | **FAIL** (generic F12 text) |
| AN-19 | corrupt.mp3 | "not readable audio" message | PARTIAL (generic) |
| AN-20 | clip.mp4 (script) | M4A of the audio | PASS |
| AN-21 | big60.wav (guest) | 50 MB message; page copy matches | PARTIAL (message good; page says 500 MB) |
| AN-22 | Download / Save to Drive at 0 | cap dialog → Day Pass → email prompt (stop) | PASS |
| AN-23 | Download with uses left (`scripts/an-reset.js`) | count +1 (per policy), `normalized_<name>.<ext>`, same bytes as the preview | **Pending: needs re-run after midnight UTC (7:00 PM ET)** |
| AN-24 | Keyboard and screen reader | drop zone Enter opens the chooser; selected target announced; LUFS summary announced; focus to result | PARTIAL (Enter works; no aria-pressed; summary not live; focus to body) |
