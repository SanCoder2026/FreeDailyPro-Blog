Sent: 2026-11-21 02:36 ET

# FDP-37 Unlock PDF: how to use this pack

1. Read `REPORT.md` (intent, why, outcomes, 22 checks), then `PRIORITIES.md`.
2. Evidence: `findings/*.md` summarise; `evidence/json/` raw results (`gate.json`, `handoff.json`, `cases-chromium.json`, `cases-firefox.json`, `privacy.json`, `probe.json`, `verify.json`, `matrix-results.json`); `evidence/screens/`; `evidence/html/` (tool copy, JSON-LD, headers); `evidence/js/` (prettified chunks + usage excerpt).
3. `evidence/testfiles/` has the locked inputs and their sources. `evidence/outputs/` has the unlocked downloads (PDF only; open in a reader, never execute).
4. Reproduce: `REPRODUCE.md`. Re-run after a fix: `scripts/README.md`.
5. Redacted: Stripe Checkout session id and fragment, Google OAuth parameters, device ids.
