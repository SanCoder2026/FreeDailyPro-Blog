Sent: 2026-11-20 08:40 ET

# Reproduce: FDP-16 Audio Volume Normalizer

- **Page:** open https://www.freedailypro.com/tool/audio-normalizer as a guest. Normalize costs no trial use; Download is gated.
- **Test files:** make them with the ffmpeg lines in `scripts/README.md`.
- **Measuring outputs:** a pass is needed to download. Without one, take the preview blob: in DevTools run `fetch(document.querySelector('main audio').src)` and save it, or use `scripts/an-battery.js`. Then run `ffmpeg -i out -af loudnorm=print_format=json -f null -` and read `input_i` / `input_tp`.

- **R1 (true peak):**
  1. spike.wav, Podcast, tick "Limit loud peaks…", Normalize. Summary: "−32.0 → −16.0 LUFS (+16.4 dB)". Measured `input_tp` = −0.51 dBTP (expected ≤ −1.5). Sample `max_volume` = −1.5 dB, so the limiter works on samples only.
  2. loud.wav, Peak to −1 dB. Summary "−3.0 → −1.1 dB". Measured `input_tp` = −0.07 dBTP.
  3. Evidence: `evidence/testfiles/out-N09-spike-limiter-on.flac`, `out-N22-loud-peak-target.flac`.
- **R2 (copy):** read the subtitle under the H1 ("Even out volume levels across an audio file"), About ("Useful for a recording where volume drifts up and down") and How to use ("evens out the loudness automatically"). Then open Details → "When not to use it" ("does not even out loud and quiet moments inside a recording").
- **R3 (errors):**
  1. silence.wav (10 s digital silence) or short03.wav (0.3 s), Normalize. Toast: "Something went wrong… Check the browser console (F12)…". The console shows "could not measure the loudness of this file".
  2. quiet.opus (stereo 48 kHz, ~45 kbps), Normalize. Same toast. The console shows `[libvorbis] encoder setup failed`.
- **R4 (phone):** in iPhone SE emulation, load the page. The drop zone's top is at y≈724 with innerHeight 584 (`screens/live/layout-iphone-se-idle.png`).
- **R5 (size):** pick a 60 MB WAV. The message says the trial supports up to 50 MB and Pro up to 200 MB, but the drop zone says "Large files (over 500 MB) may take longer".
- **R6 (bit depth):** quiet24.wav (24-bit), Podcast. `ffprobe` on the output shows `pcm_s16le`.
- **R7 (AAC):** quiet.m4a (96 kbps), Podcast. Summary "−30.8 → −15.7 LUFS… The target is −16, but the loud peaks stop it going louder". Measured −15.67 LUFS, TP −1.11 dBTP.
