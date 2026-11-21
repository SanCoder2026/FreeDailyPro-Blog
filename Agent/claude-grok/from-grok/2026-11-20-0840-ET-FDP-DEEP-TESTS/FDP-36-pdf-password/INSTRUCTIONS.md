Sent: 2026-11-21 02:24 ET

# FDP-36 Add Password to PDF: how to use this pack

1. Read `REPORT.md` (intent, why, outcomes, 22 checks), then `PRIORITIES.md`.
2. Evidence: `findings/*.md` summarise; `evidence/json/` raw results (`gate.json`, `cases-chromium.json`, `cases-firefox.json`, `unlock.json`, `privacy.json`, `share.json`, `probe.json`, `verify.json`, `matrix-results.json`); `evidence/screens/`; `evidence/video/`; `evidence/html/` (tool and blog copy, headers); `evidence/js/` (prettified chunks + usage excerpt).
3. `evidence/testfiles/` has the small synthetic inputs (the 52 MB file is not shipped; `scripts/make-pdfs.py` recreates all). `evidence/outputs/` has the protected downloads: open them only with a PDF reader and the passwords in test-cases.md (media only, never execute).
4. Reproduce: `REPRODUCE.md`. Re-run after a fix: `scripts/README.md`.
5. Redacted: Stripe Checkout session id and fragment, Google OAuth parameters, device ids.
