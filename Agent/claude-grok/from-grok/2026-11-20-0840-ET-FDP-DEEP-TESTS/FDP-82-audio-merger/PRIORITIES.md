Sent: 2026-11-21 18:56 ET

# FDP-82 priorities

**P0:** none found.

**P1**
1. **One trial use per page load, not per download.** Chromium at 0/10: first Download 0→1/10 (1 POST); then the same file again, a new b+a MP3 set with a 1 s gap and a new 3-clip WAV set downloaded free; after a reload one charge (1→2/10), then a new stereo set free. 6 files for 2 uses (`left.json` X04–X09). The FAQ only says re-downloading the *same* result is free.
2. **Full result saveable at 0 uses (owner rule).** At 10/10 Merge Audio works and "Listen to the result" renders `<audio controls>` on a blob URL with no `controlsList="nodownload"`. Its bytes are **identical** to the paid Download (`zero-X03-result.wav` = `left-0-merged-2-clips.wav`; `zero-X06-result.mp3` = `left-2-merged-2-clips.mp3`). Same as #62 / #80 / #81.

**P2**
1. Bitrate: FAQ "rounded down … so it never exceeds that clip". 128 kbps `cover.mp3` (1.4 MB picture) first → 320 kbps MP3 (`E01`, analysis 322 kbps). `M()` uses file size ÷ length. The row also shows no kHz for that file.
2. Blog /blog/audio-merger: "Silence between clips" None/0.5/1/2 s; download "01-overview-merged.m4a"; "does not overlap them, crossfade them"; "A trial use is logged when you press Merge Audio". All differ from the tool and its FAQ.
3. Size copy: drop zone "over 500 MB"; guest blocked at 50 MB combined with "You've selected a file over 50.0 MB (57.2 MB)" for two 28.6 MB files (`big.json`, `B01`). Page never states 50/200 MB.
4. Video 4p7PyYX44IQ: old UI ("Max file size: 5000MB", no gap/crossfade/format/listen); music demo; "Free" title/description.
5. Locale pages: title, meta, FAQ headings and some labels English.

**P3**
1. Mono first + stereo second → mono output; not documented.
2. Corrupt clip: generic "Check the browser console (F12)" toast, clip not named; Merge enabled although the row has no length.
3. Cap dialog "mark from your PDFs" on an audio tool; iPhone SE 9 px; ja desktop 3 px; axe desktop label-content-name-mismatch + region.
