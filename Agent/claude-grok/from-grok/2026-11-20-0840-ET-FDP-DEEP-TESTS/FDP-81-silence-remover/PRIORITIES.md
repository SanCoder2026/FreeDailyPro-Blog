Sent: 2026-11-21 18:39 ET

# FDP-81 priorities

**P0:** none found.

**P1**
1. **One trial use per page load, not per download.** Chromium at 0/10: first Download 0→1/10 (1 POST); then the same file again, a new MP3 (shortened pauses) and a new FLAC downloaded free; after a reload one charge (1→2/10), then a new 22 kHz file free. 6 files for 2 uses (`left.json` X05–X10).
2. **Full result saveable at 0 uses (owner rule).** At 10/10 "Preview the result" ("Plays here, costs nothing") and Remove Silence both work and render `<audio controls>` on blob URLs with no `controlsList="nodownload"`. The Preview is the full-length 16-bit WAV of the final edit (PCM md5 identical to the paid Download), and the result player is **byte-identical** to the paid Download (`zero-X04-result.wav` = `left-0-desilenced_speech.wav`). For an MP3 source the free Preview is even lossless WAV. Same pattern as #62 / #80.

**P2**
1. Blog /blog/silence-remover: "Remove completely … keeps about 0.15 seconds of quiet on each side", so its worked example lands "near 22:12". The tool keeps ~15 ms per side (measured pauses 0.02–0.03 s; the page FAQ says 15 ms), so that example would be ~21:52. The blog never mentions the pause list, un-ticking or the free Preview.
2. Video z5CAZByzcc4: old UI (two sliders only: no Auto threshold, Pauses menu, pause list or Preview); demonstrated on a no-copyright **music** track, which the page says not to use it on; "Free" title.
3. Locale pages: H1 translated; title, meta, labels and FAQ English.

**P3**
1. Pauses right at the Minimum Duration are caught only about half the time (1,100 × 0.5 s gaps at min 0.5 s → 550 found), because detection counts whole 20 ms windows from the file start.
2. "New" resets threshold and minimum but keeps the Pauses choice.
3. Shorten modes keep lead/trail silence of half the pause (0.15/0.25/0.5 s); Remove keeps none at the ends. Not documented.
4. Cap dialog says a pass removes the mark "from your PDFs" on an audio tool.
5. iPhone SE 9 px overflow; ja desktop 3 px; axe desktop label-content-name-mismatch + region.
