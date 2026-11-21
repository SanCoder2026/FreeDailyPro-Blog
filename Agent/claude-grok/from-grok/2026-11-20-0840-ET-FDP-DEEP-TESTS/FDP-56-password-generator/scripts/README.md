Sent: 2026-11-21 10:59 ET

# FDP-56 scripts

- `px56-live.js probe|left [chromium|firefox|webkit]`: guest runs; Chromium reads the clipboard back. Env TRIES, SUF. Writes `<mode>[-engine].json` and screenshots.
- `px56-stats.js`: the site's generator functions (verbatim from the bundle) in Node: 100k sample, brute-force entropy check, edge cases.
- `px56-scripts.js`, `px56-expand.js`: chunk list, page text, JSON-LD, links.
- `run-matrix.js` + `config.json`: devices/locales/geo/axe.
Run from tools-env with `env -u BROWSER node`. No sign-in, no payment, no ad clicks.
