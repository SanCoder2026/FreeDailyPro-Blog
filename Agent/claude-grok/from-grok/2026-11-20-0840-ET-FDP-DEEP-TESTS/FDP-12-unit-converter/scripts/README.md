Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1); axe-core for `uc-kbd.js`. For WebKit on Linux (matrix), set `GIO_EXTRA_MODULES`.
- **Output folder:** the scripts write to `/workspace/deep/12-unit-converter/live/` (matrix: the `outDir` in `config.json`). Edit `OUT` at the top to change it.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `uc-probe.js` | Starting count, tabs, buttons, notes, URL state, 6 pair pages | No |
| `uc-live.js [ids]` | 48 conversion cases + 7 cooking cases via URL state, PASS/FAIL against built-in references | No |
| `uc-gate.js` | Copy result, Save as text, Print at 0 (and with uses left: typing, a second copy, reload + copy) | No (the tool is ungated) |
| `uc-kbd.js` | Typing, empty, swap, keyboard tabs/selects, tab order, aria-live, axe, de-DE + Save, phones | No |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list (no row for this tool) | n/a |
