Sent: 2026-11-20 08:40 ET

# Scripts (Playwright 1.65, Node 24)

Paths at the top of each script point at our box (`/workspace/deep/22-universal-file-converter/…`); change OUT/T for your machine. WebKit needs GIO modules on Linux (`GIO_EXTRA_MODULES`).

- `uf-copy.js` — expands every accordion and saves the page copy (`tool-expanded.txt`) + JSON-LD.
- `uf-probe.js` — first look: starting count, drop small.jpg, result stage, requests.
- `uf-cases.json` — U01–U21 input file → targets.
- `uf-battery.js [IDs]` — per case: fresh context, drop, every target, in-memory capture (Blob/File subclass hook), request log with POST sizes. Note: the hook breaks the OCR worker; use `uf-ocr.js` for OCR.
- `uf-toasts.js` — the silent cases (OCR, .doc, PDF→Excel without tables, .pptx→.pptx, broken.pptx, HTML→PDF) with toasts polled every 500 ms and all requests.
- `uf-ocr.js` — OCR result text via a URL.createObjectURL hook.
- `uf-gate.js` — starting count, keyboard to drop zone, axe, edit panel/compression levels, Download/Drive/cloud at the starting count, Multiple files with 21 files, phones.
- `uf-dl.js` — converted-file Download: cap dialog → Day Pass email prompt (stops); with uses left, cost of 1st/2nd Download and bytes vs memory. Spends 1 trial use in a context that has uses.
- `uf-browsers.js` — Firefox + WebKit conversions.
- `run-matrix.js` + `config.json` — devices/locales/geo/axe matrix.
