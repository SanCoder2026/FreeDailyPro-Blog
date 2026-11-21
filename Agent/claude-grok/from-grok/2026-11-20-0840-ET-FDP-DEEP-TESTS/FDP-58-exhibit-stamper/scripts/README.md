Sent: 2026-11-21 11:52 ET

# FDP-58 scripts

- `make58.py`: 28 one-page docs + header_top_right.pdf (reportlab). `make55-reused.py`: the FDP-55 builder for the other PDFs.
- `px58-live.js probe|left|cases [chromium|firefox|webkit]`: guest runs. Env TRIES, CASES, SUF. Writes `<mode>[-engine].json`, screenshots and downloads.
- `px58-save.js [engine]`: stamp one file, click Save to Google Drive (records popup, closes it) and Save to my cloud storage (records dialog). No sign-in.
- `px58-drive.js`: Open from Google Drive popup check.
- `px58-scripts.js`, `px58-expand.js`: JS chunk list and page text.
- `run-matrix.js` + `config.json`: devices/locales/geo/axe.
Run from tools-env with `env -u BROWSER node`. No sign-in, no payment, no ad clicks.
