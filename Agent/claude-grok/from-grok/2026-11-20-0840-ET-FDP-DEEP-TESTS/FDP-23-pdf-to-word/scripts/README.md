Sent: 2026-11-20 08:40 ET

# Scripts (Playwright 1.65, Node 24)

Paths at the top of each script point at our box (`/workspace/deep/23-pdf-to-word/…`); change OUT/T. WebKit on Linux needs `GIO_EXTRA_MODULES`.

- `pw-copy.js` — expands the info sections; saves `tool-expanded.txt` + JSON-LD.
- `pw-probe.js` — starting count, JS chunks, controls before/after a drop.
- `pw-cases.json` — P01–P20 (file, optional pages/lang).
- `pw-battery.js [IDs]` — fresh context per case; Convert; status polling; .docx captured from memory (Blob Proxy, Word blobs only — keeps OCR working); requests logged.
- `pw-toasts.js` — messages for password/damaged/renamed/empty PDFs.
- `pw-password.js` — wrong then right password on our test PDF (user123).
- `pw-gate.js` — keyboard, labels, axe, result buttons, Stop during OCR, phones.
- `pw-dl.js` — Download at the cap (stops at the email prompt) and with uses (cost of 1st/2nd/re-convert, bytes vs memory); Drive/cloud at the cap. Spends 1 trial use in a context with uses.
- `pw-browsers.js`, `pw-webkit-ocr.js` — Firefox/WebKit conversions; WebKit OCR crash re-check.
- `run-matrix.js` + `config.json` — devices/locales/geo/axe matrix.
