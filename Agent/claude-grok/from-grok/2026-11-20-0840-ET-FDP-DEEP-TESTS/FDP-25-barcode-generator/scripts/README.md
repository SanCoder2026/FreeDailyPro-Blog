Sent: 2026-11-20 08:40 ET

# Scripts (Playwright 1.65, Node 24)

Paths at the top point at our box (`/workspace/deep/25-barcode-generator/…`); change OUT. WebKit on Linux needs `GIO_EXTRA_MODULES`. Decoding: `pip install zxing-cpp pillow numpy`; `zxingcpp.read_barcodes(PIL.Image.open(f))`.

- `bc-copy.js` — expands the info sections; saves the expanded copy + JSON-LD.
- `bc-probe.js` — starting count, JS chunks, controls, requests while typing.
- `bc-cases.json` — B01–B32 (format, value, caption/number off/height).
- `bc-battery.js [IDs]` — fresh context per case; preview PNG captured from memory (Blob Proxy, PNG only); alerts, Download state, "Prints" line. No trial use.
- `bc-ui.js` — sample value state, caption clipping, list mode (problems, 201 lines, Code 39), keyboard, axe, phones. No trial use.
- `bc-browsers.js` — Firefox/WebKit previews; iPhone 13 WebKit + Pixel 7 overflow after choosing Code 128; keyboard pick. No trial use.
- `bc-dl.js [spend]` — at the cap: dialog → Day Pass → email prompt (stop). With uses: 9 downloads in one visit (cost of each). Spends 1.
- `bc-privacy.js` — distinctive value + caption never in any request; reload → next Download charged. Spends 2.
- `bc-svgrender.js` — renders downloaded SVGs to PNG for decoding (displayed as images only).
- `run-matrix.js` + `config.json` — devices/locales/geo/axe matrix.
