Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1); axe-core for `pc-kbd.js`. For WebKit on Linux (matrix), set `GIO_EXTRA_MODULES`.
- **Output folder:** the scripts write to `/workspace/deep/11-paycheck-calculator/live/` (matrix: the `outDir` in `config.json`). Edit `OUT` at the top to change it.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `pc-live.js [ids] [outfile]` | Cases P01–P30, blog cases B01–B08, video case V01: net, federal, state, SDI, SS, Medicare, 401(k), section 125, gross line, alerts | No |
| `pc-gate.js` | Copy result, Save as text, Print at 0 and with uses left (max 6 contexts) | Yes (1 per visit with uses) |
| `pc-kbd.js` | Page notes, default state, tab order, aria-live, axe (Salary and Hourly tabs), phones | No |
| `ref_federal.py <income> <single\|mfj\|mfs\|hoh> <pretax> [se]` | Independent 2026 federal tax + FICA reference (FICA on gross; subtract section 125 yourself) | n/a |
| `run-matrix.js config.json` | Devices, locales, geo, axe (about 7 minutes) | No |
| `RERUN-AFTER-RESET.md` | Copy of the running list; row 11 is this tool | n/a |
