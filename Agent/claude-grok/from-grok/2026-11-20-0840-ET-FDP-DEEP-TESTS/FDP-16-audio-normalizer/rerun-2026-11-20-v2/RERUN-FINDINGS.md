Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-16 audio-normalizer (re-run after the trial reset)

**Supersedes:** `FDP-16-audio-normalizer-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-16-audio-normalizer-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 16 result: DONE (2026-11-20 22:27–22:28 EST)

Contexts 0 and 1 loaded at 0; context 2 loaded at 10.

| Check | Result |
|---|---|
| Normalize | Free (count stays 0). |
| AN-23 first Download | **−1** (0 → 1). `normalized_quiet.wav`, **3,528,078 B = preview size**. PASS |
| Second Download | **Free** (stays 1), same bytes (identical SHA-256). |
| Save to Google Drive | Opened Google sign-in; **no charge** (stays 1). Stopped at sign-in: https://accounts.google.com/v3/signin/identifier (untested past sign-in). |
