Sent: 2026-11-21 11:52 ET

# FDP-58 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md, cases in test-cases.md.
2. **Test files:** `evidence/testfiles/`. `make58.py` adds `many/doc01–28.pdf` and `header_top_right.pdf`; the rest come from FDP-55 (`make55-reused.py`); damaged.pdf and password_u123.pdf (u123) from FDP-52; `notes.txt` for the wrong-type check.
3. **Scripts** (`scripts/`, run from tools-env with `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES`):
   - `px58-live.js probe|left|cases [engine]`. Env: TRIES (fresh contexts to try), CASES=E01,E09 (subset), SUF (suffix).
   - `px58-save.js [engine]` (Save to Drive / cloud, no sign-in), `px58-drive.js` (Open from Drive popup).
   - `px58-scripts.js`, `px58-expand.js` (JS chunks, page text), `run-matrix.js config.json`.
4. **Evidence:** `outputs/` (all PDFs/CSVs/ZIPs, unzipped in `outputs/x/`), `screens/render/` (renders, crops), `json/` (run results, matrix), `video/` (sheet, crops, info), `screens/cases|devices|locales|geo|a11y|live`, `html/`, `js/`.
5. **Rules:** guest only, no sign-in, stop at the email field or Stripe, no ad clicks. Times are EST. Trial uses reset at midnight UTC (7:00 PM ET).
