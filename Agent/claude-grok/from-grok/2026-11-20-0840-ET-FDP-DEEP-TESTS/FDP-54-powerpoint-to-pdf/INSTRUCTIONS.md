Sent: 2026-11-21 10:12 ET

# FDP-54 package: how to use it

1. **Read first:** REPORT.md, then PRIORITIES.md. Steps are in REPRODUCE.md, and cases in test-cases.md.
2. **Test decks:** `evidence/testfiles/`, built by `make54.py` (python-pptx + LibreOffice).
3. **Scripts** (tools-env, `env -u BROWSER node`; WebKit needs `GIO_EXTRA_MODULES`):
   - `px54-live.js probe|left|cases [engine]`. Env: TRIES (fresh contexts to try), CASES=K05,K06 (subset), SUF (output suffix).
   - `px54-ext.js`: renamed extensions.
   - `px54-drive.js`: Drive popup and Tabs.
   - `run-matrix.js config.json`.
4. **Evidence:**
   - `outputs/`: every PDF.
   - `screens/render/`: page sheets and crops.
   - `json/`: all run results.
   - `video/`: sheets and hi-res crops (individual frames left out for size).
5. **Rules:** guest only, no sign-in, stop at the email field or Stripe, no ad clicks. Times are EST.
7. **Left out of the zip (size limit):** the two 60-slide PDFs (about 9 MB each; their pdfinfo is in `outputs/long60-pdfinfo.txt`) and duplicate outputs (L01 = K01; L01b re-download; L02 ≈ K04; first-run K06/K07 without a text layer). Regenerate them with the scripts.
