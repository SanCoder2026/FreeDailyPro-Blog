Sent: 2026-11-20 08:40 ET

# Scripts (Playwright 1.65, Node 24)

Paths at the top point at our box (`/workspace/deep/24-word-to-pdf/…`); change OUT/T. WebKit on Linux needs `GIO_EXTRA_MODULES`.

- `wp-copy.js` — expands the info sections; saves `tool-expanded.txt` + JSON-LD.
- `wp-probe.js` — starting count, JS chunks, controls after dropping rich.docx.
- `wp-cases.json` — W01–W17 (file, mode, paper size).
- `wp-battery.js [IDs]` — fresh context per case; Convert to PDF; PDF captured from memory (Blob Proxy, PDFs only); requests logged.
- `wp-errors.js` — messages for broken/renamed .docx and .doc.
- `wp-gate.js` — keyboard, axe, result buttons, Stop during an Exact-look run, phones.
- `wp-dl.js [spend]` — Download at the cap (stops at the email prompt), Drive/cloud at the cap; `spend` looks only for a context with uses and records the cost of 1st/2nd/re-convert Downloads. Spends 1 trial use.
- `wp-browsers.js` — Firefox/WebKit Keep formatting + Exact look.
- `run-matrix.js` + `config.json` — devices/locales/geo/axe matrix.
- Note: W14/W15 inside `battery-W02-W15.json` used a first cols.docx whose column setting was malformed (our mistake); `battery-W14-W15-rerun.json` is the valid run with the fixed file.
