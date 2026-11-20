Sent: 2026-11-20 08:40 ET

# Reproduce: FDP-17 Compress Video

- **Page:** open https://www.freedailypro.com/tool/compress-video as a guest. Compress costs no trial use.
- **Test files:** make them with `scripts/README.md`.
- **Measuring outputs:** take the "Compressed" preview blob (`[...document.querySelectorAll('main video')].pop().src`) and run ffprobe, or use `scripts/cv-battery.js`.

- **R1 (presets):** add any video → Custom Target. The shortcuts read "8 MB (Discord)", "16 MB (WhatsApp)". Compare https://support.discord.com/hc/en-us/articles/25444343291031-File-Attachments-FAQ ("For non-Nitro subscribers, the maximum file upload is 20MB") and the WhatsApp Help Center "How to send media" note (default video size limit 100 MB / 64 MB).
- **R2 (copy):**
  1. The mode row shows Medium / Strong / Manual Quality / Custom Target (no Light).
  2. Common questions → "Will compressing lower the picture quality?" says "…costs more than Light".
  3. Details → "How to use Compress Video" says "Manual Quality, which is selected when the tool opens", but Medium is highlighted.
  4. Medium's hint says "adjusts once"; the FAQ says "two full encoding passes" and "repeats up to twice".
  5. The drop zone says "over 200 MB"; a 71.7 MB file gives "trial use supports up to 50.0 MB".
- **R3 (above source):** hd1080.mp4 (12.90 MB) → Custom Target → press "100 MB" → Compress. After about 46 s: "97.03 MB - 652.4% larger than the original (12.90 MB). Target reached (100.00 MB)…".
- **R4 (miss):** long60.mp4 (60 s 720p) → Custom 0.5 → Compress. Result "1.42 MB… not reached… Try Strong or 'Lower resolution to 720p'". The output audio is still about 80 kbps AAC (ffprobe).
- **R5 (Keep original):** hd1080.mp4 → Manual Quality (50%) → Compress → "4.4% larger". "Keep original (download)" downloads `hd1080.mp4` with no dialog at 0 remaining, but "Get a Day Pass to download" sits under it.
