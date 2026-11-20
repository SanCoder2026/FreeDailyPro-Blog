Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1) and `axe-core`. For WebKit on Linux, set `GIO_EXTRA_MODULES`. `wc-goal.js` requires playwright by the absolute path `/workspace/deep/tools-env/node_modules/playwright`; edit it if needed.
- **Output:** scripts write to `/workspace/deep/15-word-counter/live/` (matrix: the `outDir` in `config.json`).

| Script | What it does | Costs a trial use? |
|---|---|---|
| `wc-cases.json` | W01–W30: input, expected counts, note | n/a |
| `wc-live.js` | Cases, reading/speaking timings, platform rows, 224k-character text | No |
| `wc-gate-kbd.js` | Starting count, Ctrl+C, Copy stats, Clear, keyboard, aria-live, axe, phones | No today (tool is ungated) |
| `wc-goal.js` | Word goal 5/10/50/0/−3/2.7 | No |
| `wc-webkit-retry.js` | iPhone 14 Pro Max WebKit retry (3 attempts) | No |
| `wc-net.js` | Lists the tool's JS chunks | No |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list (no row for this tool) | n/a |
