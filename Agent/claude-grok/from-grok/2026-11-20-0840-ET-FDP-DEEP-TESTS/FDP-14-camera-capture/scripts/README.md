Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1) and `axe-core`; Python with Pillow for `cc-inspect.py`. For WebKit on Linux (matrix), set `GIO_EXTRA_MODULES`. `cc-cameras.js` and `cc-denied-ff.js` require playwright by the absolute path `/workspace/deep/tools-env/node_modules/playwright`; edit that to your path.
- **Output:** scripts write to `/workspace/deep/14-camera-capture/live/` (matrix: the `outDir` in `config.json`). Edit `OUT` at the top to change it.
- **Fake camera test card** (41 MB, not included; regenerate it):
  ```
  ffmpeg -f lavfi -i "color=c=red:s=640x360[a];color=c=lime:s=640x360[b];color=c=blue:s=640x360[c];color=c=yellow:s=640x360[d];[a][b]hstack[top];[c][d]hstack[bot];[top][bot]vstack,drawtext=text='FDP TEST LEFT':x=40:y=40:fontsize=48:fontcolor=black,format=yuv420p" -frames:v 30 -r 10 /workspace/deep/14-camera-capture/fake/quad.y4m
  ```
  Chromium flags: `--use-fake-ui-for-media-stream --use-fake-device-for-media-stream --use-file-for-fake-video-capture=<quad.y4m>`. With a file, Chromium exposes one camera. Without one it exposes `device-count=N` built-in fakes; that is how `cc-cameras.js` tests the picker.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `cc-count.js` | Starting count in 4 fresh contexts and the camera list (read-only) | No |
| `cc-ui.js` | Start, Cancel, JPG, Capture pixel check, crop blob type, Retake, the headless "denied" and no-camera cases | No |
| `cc-cameras.js` | 2-camera picker, switch, Front/rear toggle twice | No |
| `cc-kbd.js` | Keyboard path, focus, aria-live, axe (idle, live, captured), mark notice, iPhone SE and Pixel 7 layout plus touch crop | No |
| `cc-denied-ff.js` | Firefox with camera permission denied → message | No |
| `cc-cloud.js` | Save to Google Drive and Save to my cloud storage as a guest (no sign-in; popups recorded and closed) | Only with uses left (Drive) |
| `cc-probe.js <tag> [n]` | Full flow plus Download Full, Download Crop and Copy, recording the count after each | **Yes, with uses left** |
| `cc-inspect.py files…` | Format, size and non-test-card pixels in the top-right and bottom-right corners (badge detector) | n/a |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list (row 14 = this tool) | n/a |
