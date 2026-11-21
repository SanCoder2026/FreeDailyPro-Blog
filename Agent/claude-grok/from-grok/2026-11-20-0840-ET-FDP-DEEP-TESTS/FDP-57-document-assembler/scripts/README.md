Sent: 2026-11-21 11:31 ET

# FDP-57 scripts

- `make57.py`: test files.
- `px57-live.js probe|left|cases [engine]`: guest runs (Env TRIES, CASES, SUF). Cases run in ONE page load after one context with uses is found.
- `px57-pw.js`: password dialog flow (types only u123).
- `px57-explore.js`: first look at the result area.
- `px57-drive.js`: Open from Google Drive popup (recorded, closed).
- `px57-scripts.js`, `px57-expand.js`: chunks, text, JSON-LD, links.
- `run-matrix.js` + `config.json`.
Run from tools-env with `env -u BROWSER node`. No sign-in, no payment, no ad clicks.
