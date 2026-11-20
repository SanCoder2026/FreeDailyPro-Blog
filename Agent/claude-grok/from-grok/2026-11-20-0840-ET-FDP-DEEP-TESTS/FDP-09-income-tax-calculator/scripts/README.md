Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` installed (tested with 1.65.1). For WebKit on Linux, set `GIO_EXTRA_MODULES` to the gio modules folder.
- **Python:** `ref_federal.py` uses the standard library only.
- **Output folder:** all `it-*.js` scripts write to `/workspace/deep/09-income-tax-calculator/live/`. Edit `OUT` at the top to change it.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `it-probe.js` | Starting strip/localStorage, controls, loaded bundles | No |
| `it-live.js [ids]` | Calculation cases T01–T40: reads net, federal, payroll, state, SDI, boxes, notes, alerts | No (no copy, save or print) |
| `ref_federal.py` | Independent 2026 reference: `python3 ref_federal.py 240000 single 0 se` | — |
| `it-gate.js` | First run: Copy, Save, Print, Ctrl+C, tab order, axe, phones. Its clipboard sentinel itself triggers the gate | Yes (1 if uses left) |
| `it-gate2.js` | Copy ×3 with uses left; Copy ×3 + Save at 0 | Yes (1 if uses left) |
| `it-gate3.js` | Print and Ctrl+C at 0 | No (blocked) |
| `it-gate4.js` | **Re-run:** Save-first and Print-first with uses left; skips contexts at 0 (max 6) | Yes (1 each) |
| `it-flat.js` | Custom Flat Rate cases | No |
| `it-dbg.js` | Strip and buttons in one fresh context | No |
| `run-matrix.js config.json` | Devices, locales, geo, axe (about 7 min) | No |

`RERUN-AFTER-RESET.md` is a copy of the running list (row #9 is this tool).
