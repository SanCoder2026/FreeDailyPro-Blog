Sent: 2026-11-21 03:05 ET

# FDP-39 Compare PDF: how to use this pack

1. Read `REPORT.md` (intent, why, outcomes, 22 checks), then `PRIORITIES.md`.
2. **Evidence:**
   - `findings/*.md` summarise.
   - `evidence/json/` has raw results: `gate.json`, `cases-*.json`, `privacy.json`, `probe.json`, `matrix-results.json`.
   - `evidence/screens/`, `evidence/html/` (tool copy, JSON-LD, headers, blog text), `evidence/js/` (prettified chunks + usage excerpts), `evidence/video/`.
3. `evidence/testfiles/` has the PDF pairs (built by `scripts/make-pdfs.py`). `evidence/outputs/` has the downloaded reports (PDF/TXT; open in a reader, never execute).
4. Reproduce: `REPRODUCE.md`. Re-run after a fix: `scripts/README.md`.
5. Redacted: Stripe Checkout session id and fragment, device ids.
