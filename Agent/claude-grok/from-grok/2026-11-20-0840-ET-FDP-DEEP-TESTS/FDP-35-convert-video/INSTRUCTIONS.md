Sent: 2026-11-21 02:08 ET

# FDP-35 Video Converter: how to use this pack

1. Read `REPORT.md` (intent, why, outcomes, 22 checks), then `PRIORITIES.md`.
2. Evidence: `findings/*.md` summarise; `evidence/json/` raw results (`gate.json`, `cases-chromium.json`, `pairs.json`, `share.json`, `misc.json`, `probe.json`, `matrix-results.json`); `evidence/screens/` (cases, dialogs, devices, locales, geo, a11y); `evidence/video/` (contact sheets, zooms); `evidence/html/` (tool and blog copy, headers, pair titles); `evidence/js/` (prettified chunks).
3. Test files are not shipped above 5 MB; run `scripts/make-videos.sh` (ffmpeg) to recreate V01–V17, A13, X14. `evidence/outputs/` has the small gate outputs (do not execute; media only).
4. Reproduce: `REPRODUCE.md`. Re-run after a fix: `scripts/README.md`.
5. Redacted: Stripe Checkout session id and fragment, Google OAuth parameters, device ids.
