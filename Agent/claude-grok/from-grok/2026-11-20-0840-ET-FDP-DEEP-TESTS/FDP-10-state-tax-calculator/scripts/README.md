Sent: 2026-11-20 08:40 ET

# scripts/

- **Setup:** Node with `playwright` (tested with 1.65.1); axe-core for `st-axe.js` / `st-kbd.js`. For WebKit on Linux, set `GIO_EXTRA_MODULES`.
- **Output folder:** the scripts write to `/workspace/deep/10-state-tax-calculator/live/`. Edit `OUT` (or the path) at the top to change it.

| Script | What it does | Costs a trial use? |
|---|---|---|
| `st-probe.js` | Starting count, controls, data-testids | No |
| `st-live.js [ids]` | Cases S01–S30 (+S10b): tax, effective rate, local line, payroll, totals, alerts, bracket table | No |
| `st-compare.js <income> <status>` | Full "Compare all states" table | No |
| `st-blog95.js` | Re-checks the blog's $95k table | No |
| `st-gate.js` | The six export actions at 0 and with uses left (max 6 contexts) | Yes (1 per visit with uses) |
| `st-kbd.js` | Compare, row click, "85k", tab order, aria-live, phones | No |
| `st-axe.js` | axe on main with MD + compare open | No |
| `run-matrix.js config.json` | Devices, locales, geo, axe | No |
