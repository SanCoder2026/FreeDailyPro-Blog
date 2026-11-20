Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1), `axe-core` (for gc-kbd.js) and `nspell` (2.1.5, for gc-offline.js). For WebKit on Linux (matrix), set `GIO_EXTRA_MODULES`.
- **Output folder:** scripts write to `/workspace/deep/13-grammar-checker/live/` (matrix: `outDir` in `config.json`). `gc-offline.js` reads the engine and dictionary from `/workspace/deep/13-grammar-checker/js/` (copies are in `../evidence/js/`). Edit the paths at the top to change them.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `gc-cases.json` | FP01–FP28 correct sentences, FX01–FX15 errors with expected fixes | n/a |
| `gc-offline.js [auto\|us\|uk]` | Runs the site's `me()` engine in Node on all cases; writes `offline-<variant>.json` | No (no browser) |
| `gc-probe.js` | Starting count, controls, notes, textarea labels, one Check, filtered network list (deviceId redacted) | No today (tool is ungated) |
| `gc-live.js` | All cases on the live page, UK variant, Copy at the starting count, 10,801-word timing | No today |
| `gc-kbd.js` | Keyboard path, focus, aria-live, axe on main before/after Check, iPhone SE + Pixel 7 layout | No today |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list (no row for this tool) | n/a |

If Santosh decides Check/Copy should take trial uses, the live scripts will start consuming uses; run them in fresh contexts and record starting counts.
