Sent: 2026-11-20 22:15 ET

# Scripts (Playwright 1.65, Node 24)

Paths at the top point at our box (`/workspace/deep/26-invoice-generator/…`). WebKit on Linux needs `GIO_EXTRA_MODULES`.

- `ig-copy.js` — expands the info sections; saves the expanded copy + JSON-LD.
- `ig-probe.js` — starting count, JS chunks, controls.
- `ig-ui.js` — no trial use (only contexts already at the cap): calc scenarios S1–S12, validation, at-cap dialogs → Day Pass → email prompt, profile/clients import, keyboard, axe, phones.
- `ig-spend.js A|B|C` — finds a context with uses. A: rich invoice → PDF then Word; B: Excel, reload, 23-line/4-rate A4 PDF, then (Nov 20 addition) at-cap PDF → Day Pass → email prompt; C: AED/Arabic PDF ×2 + Excel. `OUTDIR` sets the output folder; `PWB=firefox|webkit` picks the engine (Word step skipped there). Spends 1–2 trial uses per mode.
- `ig-profile.js` — Save profile cost with uses left; saved JSON kept (never executed).
- `run-matrix.js` + `config.json` — devices/locales/geo/axe matrix.
