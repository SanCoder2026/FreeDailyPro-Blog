Sent: 2026-11-21 12:15 ET

# FDP-59 scripts

- `px59-live.js probe|left|cases [chromium|firefox|webkit]`: guest runs. Env TRIES, ANY=1, SUF. Inputs for `cases` in `testfiles/cases.json`. Writes `<mode>[-engine].json` and screenshots.
- `px59-expected.mjs [cases.json]`: expected drafts from the site's own template code (copied from CaptionGenerator-C4DMCLiD.js; imports textUtils.pretty.js from /tmp/textUtils59.mjs) → `expected-compare.json`.
- `px59-scripts.js`, `px59-expand.js`: JS chunk list and page text.
- `run-matrix.js` + `config.json`: devices/locales/geo/axe.
Run from tools-env with `env -u BROWSER node`. No sign-in, no payment, no ad clicks.
