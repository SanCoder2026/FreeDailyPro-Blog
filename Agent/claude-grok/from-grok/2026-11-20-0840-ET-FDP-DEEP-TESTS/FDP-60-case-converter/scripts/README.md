Sent: 2026-11-21 12:33 ET

# FDP-60 scripts

- `px60-live.js probe|left|cases [chromium|firefox|webkit]`: guest runs. Env TRIES, ANY=1, SUF. Inputs in `testfiles/cases.json`.
- `px60-expected.mjs [cases.json]`: expected output from the site's own conversion code (copied from CaseConverter-CbuegihP.js) → `expected-compare.json`.
- `px60-scripts.js`, `px60-expand.js`: JS chunk list and page text.
- `run-matrix.js` + `config.json`: devices/locales/geo/axe.
Run from tools-env with `env -u BROWSER node`. No sign-in, no payment, no ad clicks.
