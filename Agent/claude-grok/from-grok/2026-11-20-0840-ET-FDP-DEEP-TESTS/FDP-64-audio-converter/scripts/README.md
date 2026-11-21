Sent: 2026-11-21 14:10 ET

# FDP-64 scripts

Run from `/workspace/deep/tools-env` with `env -u BROWSER node <script>`. WebKit needs `GIO_EXTRA_MODULES=/workspace/deep/tools-env/giomods`. Guest contexts only; nothing signs in or pays.

- `make64.sh`: builds the test files with ffmpeg (WAV, tagged MP3/FLAC with cover, M4A, OGG, WMA, MP4 with/without audio, non-audio, batch WAVs, noise OGGs).
- `px64-live.js <zero|left|batch|cases|quickbuy> [chromium|firefox]`: main runs. `zero` loops until a context is at the cap (TRIES); `left`/`batch` loop until uses are left; `CAP=1` runs batch as-is. Outputs are probed with ffprobe + md5.
- `px64-extra.js`: quality/estimate lines, OGG→OGG on three files, and at the cap: Save to Google Drive, Save to my cloud storage (stops at the dialog), Continue with Audio Trimmer.
- `px64-big.js`: a ~60 MB WAV on the trial (size limit message) + M4A estimates. Build the WAV with: `ffmpeg -f lavfi -i "sine=frequency=440:duration=360" -ac 2 -ar 44100 -c:a pcm_s16le big-60mb.wav` (not included, 63 MB).
- `px64-drive.js`: clicks "Open from Google Drive" and records only the popup host.
- `px64-scripts.js`, `px64-expand.js`: JS chunk list and expanded page copy.
- `run-matrix.js config.json`: devices, locales, geo, axe.
