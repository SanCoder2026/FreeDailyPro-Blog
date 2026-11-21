Sent: 2026-11-21 09:19 ET

# Scripts (run from /workspace/deep/tools-env with `env -u BROWSER node …`; WebKit needs GIO_EXTRA_MODULES=…/giomods)

- **make52.py:** builds the test inputs (pictures, articles, .docx via LibreOffice, copied PDFs, JSON files).
- **px52-scripts.js / px52-expand.js:** first load (text, chunks, trial strip) and the expanded info sections (text, JSON-LD, links).
- **px52-probe.js:** control inventory in both modes.
- **px52-live.js `<zero|left|left3|left4|subset> [engine]`:**
  - `zero`: at the cap.
  - `left`: the full flow with uses left.
  - `left3`: per-export check.
  - `left4`: Combine download.
  - `subset`: Firefox/WebKit.
- **px52-focus.js:** result area, templates, Combine with and without WebP.
- **px52-wk.js:** WebKit gate in fresh contexts, plus Combine one file type at a time (crash isolation).
- **px52-overflow.js:** finds elements wider than a phone viewport.
- **run-matrix.js + config.json:** devices, locales, geo, axe.
- **Safety:** no sign-in, payment or ad clicks. The scripts redact deviceId, OAuth parameters and the Stripe session. The only password typed is the test PDF's own (u123).
