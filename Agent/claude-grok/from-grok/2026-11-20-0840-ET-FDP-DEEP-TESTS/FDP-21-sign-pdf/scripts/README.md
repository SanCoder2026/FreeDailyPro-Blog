Sent: 2026-11-20 08:40 ET

# FDP-21 scripts

Run from `/workspace/deep/tools-env`. Outputs go to `/workspace/deep/21-sign-pdf/`.

| Script | What it does | Costs uses? |
|---|---|---|
| `run-matrix.js config.json` | devices, locales + /ar, geos, axe (WebKit: `GIO_EXTRA_MODULES=$PWD/giomods`) | no |
| `sp-probe.js` / `sp-copy.js` | first-load state and controls / expanded copy + JSON-LD | no |
| `sp-battery.js [IDs\|all] [spend]` + `sp-cases.json` | one context per case; captures the signed PDF from the in-memory Blob; skips contexts with uses unless `spend` (then Download ×2, counted) | only with `spend` |
| `sp-import.js` | signature image import (PNG, JPG) | yes if the context has uses |
| `sp-otherparty.js` | reopen out-S02.pdf as the other party | no at 0 |
| `sp-gate.js` | counts, keyboard, names, axe, cap dialog → Day Pass email prompt (stops), phones | no at 0 |
| `sp-browsers.js` | Firefox + WebKit flow | no at 0 |

Downloaded PDFs are only parsed (pypdf) or rendered (pdftoppm), never executed.
