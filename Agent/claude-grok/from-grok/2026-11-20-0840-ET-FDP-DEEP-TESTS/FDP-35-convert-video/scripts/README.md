Sent: 2026-11-21 02:08 ET

# FDP-35 scripts (Playwright 1.65, Node; run with `env -u BROWSER node <script>` from a folder with playwright installed)

- `make-videos.sh` — builds the synthetic test files with ffmpeg (incl. 60 s and 74 MB files).
- `cvv-probe.js` — loads the tool, lists controls/outputs, records network hosts.
- `cvv-live.js [K01,K02|all] [firefox]` — conversion cases K01–K23; saves preview blobs, timings, summaries, ffprobe-able outputs, screenshots.
- `cvv-gate.js` — finds a fresh context with uses left (up to 14 tries) and one at 0: Download A/A2, Drive and cloud dialogs (stops at sign-in), New + B, C, reload + D; preview hashes; at 0: Download → cap dialog → Day Pass (stops at email), Quick Buy day/monthly (stops at Stripe), keyboard.
- `cvv-pairs.js` — pair landing pages preselect check.
- `cvv-share.js`, `cvv-misc.js` — Share clipboard, print PDF, misc.
- `cvv-copy.js`, `cvv-blog.js` — expanded copy / JSON-LD and blog text.
- `run-matrix.js config.json` — 10 devices, 11 locales, 6 geos, axe.
Never type an email or card; never click ads; never sign in.
