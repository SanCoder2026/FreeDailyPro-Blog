Sent: 2026-11-21 10:39 ET

# FDP-55 scripts

- `make55.py`: builds the test PDFs (reportlab + pikepdf).
- `px55-live.js probe|left|cases [chromium|firefox|webkit]`: guest runs. Env TRIES, CASES, SUF. Writes `<mode>[-engine].json`, screenshots and downloads.
- `px55-ovf.js`: overflow hint screenshots (no trial use).
- `px55-drive.js`: clicks Open from Google Drive, records the popup origin/path, and closes it.
- `px55-scripts.js`, `px55-expand.js`: JS chunk capture and page expansion.
- `run-matrix.js` + `config.json`: devices/locales/geo/axe.
Run from tools-env with `env -u BROWSER node`. No sign-in, no payment, no ad clicks.
