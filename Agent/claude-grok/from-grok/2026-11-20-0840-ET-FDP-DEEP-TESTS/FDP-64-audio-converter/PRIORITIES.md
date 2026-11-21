Sent: 2026-11-21 14:10 ET

# FDP-64 Audio Converter: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Why it matters | Suggested fix |
|---|---|---|---|---|
| P1 | At 0 trial uses Convert runs and the result plays in `<audio controls>` (no `controlsList="nodownload"`); the player blob is byte-identical to the gated download, so ⋮ Download / "Save audio as" saves it | zero-capped.json (+firefox) Z02–Z06; md5 7e24a7ecf8ff in zero-player-blob.mp3 = tone-12s.mp3; Z02-converted-capped.png | Real save at 0 uses (same as FDP-62 "Save video as"); the pass becomes optional | nodownload + no context menu, and/or short excerpt at 0 |
| P1 | One trial use per page load: Convert again / New file downloads are free until reload | left.json L03–L09; left-firefox.json | Nov 21 rule: per-page-load charging | Charge per converted file (batch stays one use) |
| P2 | Drop zone says "over 500 MB may take longer"; trial blocks at 50 MB, hard limit 200 MB; "Upgrade to Pro" | big.json, cases/big-63mb.png, ffmpegEngine R/g | Wrong expectation; wrong plan name | State 50 MB trial / 200 MB with a pass |
| P2 | Video Ux4d3tMWQx4: old UI, presenter's Downloads folder with third-party tracks, "free" wording, "PDF tools" tag | video/sheet.jpg, frames f003–f004, info-min.json | Off-brand, privacy-sloppy, undersells batch/player | Re-record clean |
| P2 | Locale pages: subtitle, on-device note, mode toggle, drop zone, FAQ English | locales/*es* | Mixed-language page | Translate tool strings (site-wide) |
| P2 | SEO: meta 74 chars, generic OG | tool.html | CTR | 140–160-char meta (MP3/WAV/M4A/FLAC/OGG, video to audio, batch ZIP) |
| P3 | 32 kbps stereo OGG → OGG fails ("Something went wrong") | cases.json C06; extra.json | Low-bitrate voice OGGs | Clamp Vorbis bitrate |
| P3 | How-to promises kbps + size for every lossy quality; MP3/OGG show it only for Same as original | extra.json, big.json | Small mismatch | Align copy (blog already explains VBR) |
| P3 | Cap dialog mentions removing the mark from "PDFs and images" on an audio tool | zero-capped.json Z04 | Confusing | Tool-specific line |
| P3 | Off-topic guide link (Text to Speech API) | tool-expanded.txt | Relevance | Replace with an audio guide |
| P3 | Phones "Tap to choose… / or tap to choose"; iPhone SE 9 px overflow; axe label mismatch, link-in-text-block ×4, region; Pixel 7 ad-caption contrast; ja 3 px | devices/*, matrix-results.json | Polish | Fix copy, label, link styling, caption colour (keep reserved ad slots) |
