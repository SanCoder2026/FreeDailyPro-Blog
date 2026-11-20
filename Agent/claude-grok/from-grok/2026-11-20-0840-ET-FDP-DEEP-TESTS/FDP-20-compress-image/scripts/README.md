Sent: 2026-11-20 08:40 ET

# FDP-20 scripts

Run from `/workspace/deep/tools-env` (Playwright 1.65.1, axe-core). Output paths point to `/workspace/deep/20-compress-image/`.

| Script | What it does | Costs uses? |
|---|---|---|
| `run-matrix.js config.json` | 10 device profiles, 10 locales + /ar, 6 geos, axe; WebKit needs `GIO_EXTRA_MODULES=$PWD/giomods` | no |
| `ci-probe.js` | first-load state, controls list, upload photo.jpg | no |
| `ci-copy.js` | expands About/How/FAQ/Details/Guides, writes tool-expanded.txt + JSON-LD | no |
| `ci-battery.js [C01,C02…]` + `ci-cases.json` | one fresh context per case; captures the output blob via a canvas.toBlob hook; saves `out-<ID>.*` and, when the original is returned, `preview-<ID>-*` | no |
| `ci-invalid.js` | target 0 / −5 / empty / 0.4 KB / 99999: toast, aria-invalid, inline error | no |
| `ci-gate.js` | starting count, keyboard, mode state, axe, live regions, Download/Drive/cloud dialogs (stops at the email prompt), Several files ×6 and ZIP, phones | ZIP only when the context has uses |
| `ci-browsers.js` | Firefox + WebKit: Medium, 5 KB transparent logo, HEIC | no |
| `ci-batchdl.js` | batch with GPS photo; single + ZIP downloads, only in a context with uses | yes |
| `ci-reset.js` | after 7:00 PM ET: Download ×2, Drive (stops at Google), GPS-original download check | yes |
| `RERUN-AFTER-RESET.md` | copy of the shared rerun table (row 20) | — |

Test images: `evidence/testfiles/make.py` (Pillow, pillow-heif). Downloads are only read as bytes, never opened or executed.
