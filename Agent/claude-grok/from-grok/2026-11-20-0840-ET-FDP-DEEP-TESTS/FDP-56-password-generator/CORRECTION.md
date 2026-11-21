Sent: 2026-11-21 11:32 ET

# FDP-56 Password Generator: -v2 correction (2026-11-21 11:01 EST)

The original zip `FDP-56-password-generator-2026-11-21.zip` stays unchanged. This -v2 replaces only REPORT.md and PRIORITIES.md.

## What changed

1. **Reset time.** The original said to rerun "after midnight ET". Trial uses reset at **midnight UTC, which is 7:00 PM ET** (EST, UTC-5). The rerun is now scheduled with tonight's 7:15 PM ET batch.
2. **Rerun tracking.** The pending check is now also a row in `/workspace/deep/RERUN-AFTER-RESET.md` (#56), not only in PRIORITIES.md. Command: `TRIES=10 env -u BROWSER node px56-live.js left firefox`, from `/workspace/deep/tools-env`.

## What did not change

All findings, priorities and evidence stay as sent:
- the uncounted-Copy policy question;
- the Privacy vs FAQ contradiction;
- the spaces-only symbols bug;
- the stale video;
- the unrelated guide links.
