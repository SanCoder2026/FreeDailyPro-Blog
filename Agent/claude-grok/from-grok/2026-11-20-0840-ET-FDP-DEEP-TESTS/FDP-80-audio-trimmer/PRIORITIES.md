Sent: 2026-11-21 18:23 ET

# FDP-80 priorities

**P0:** none found.

**P1**
1. **One trial use per page load, not per download.** Chromium at 0/10: the first Download charged 0→1/10 (1 POST). A re-trim, a Remove-section result, a new WAV file and the same file again downloaded free (5 files, 0 POSTs). After a reload one Download charged (1→2/10) and the next trim + Download was free. 7 files for 2 uses (`left.json` X04–X10).
2. **The full result can be saved at 0 uses (owner rule).** At 10/10 Trim works and "Listen to the result" is a plain `<audio controls>` on a blob URL with no `controlsList="nodownload"`, so the browser's own ⋮ → Download / "Save audio as" saves it. The player's bytes at 10/10 are **byte-identical** to the gated Download from a context with uses (`zero-X06-player.mp3` = `left-cut_beeps20.mp3`). Same pattern as #62.

**P2**
1. **Hundredths are lost on Trim.** Type Start 3.25 → the box redisplays "0:03.3"; the summary still says "Keeping 0:04.3", but pressing Trim (blur) re-reads the rounded box and cuts from **3.3 s**: output 4.2 s, first beep at 0.70 s, not 0.75 s. Every format (WAV, MP3, FLAC, M4A, OGG, Opus, MP4). FAQ: "the Start and End boxes accept any decimal value"; "exact".
2. Drop zone says "Large files (over 500 MB) may take longer", but guests are blocked above 50 MB (63 MB WAV → "trial use supports up to 50.0 MB", Trim disabled); paid 200 MB.
3. Blog /blog/audio-trimmer: "it cannot delete a cough from the middle" (Remove selection now does), "Selected: 1:30 of 52:10" (now "Keeping…"), "puts the old value back" (now keeps your text).
4. Video pc4DDk1feTg: old UI (no waveform, Keep/Remove, fades or Ringtone; "Selected:" line), "Free" title.
5. Locale pages: H1 and some buttons translated; title, meta, labels and FAQ English.

**P3**
1. `1:02:03`-style input is read as 1 min 2 s ("0:05:10" → 5 s; error "end (0:05) must be after the start (0:05)"). "2,5" → 2 silently.
2. Summary rounds: 3.00–3.05 shows "Keeping 0:00.0" while the file is 0.1 s.
3. Remove mode names files `cut_…`; FAQ and blog say `trimmed_`. Mode stays on Remove after "New".
4. Cap dialog on an audio tool says a pass "removes the 'Created with FreeDailyPro.com' mark from your PDFs".
5. iPhone SE 9 px overflow; ja desktop 3 px; axe desktop label-content-name-mismatch + region.
