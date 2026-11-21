Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-17 compress-video (re-run after the trial reset)

**Supersedes:** `FDP-17-compress-video-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-17-compress-video-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 17 result: DONE (2026-11-20 22:28 EST)

Context 0 loaded at 10.

| Check | Result |
|---|---|
| Compress | Free. |
| CV-21 first Download | **−1** (0 → 1). `compressed_noaudio.mp4`, **5,059,360 B = preview size**. PASS |
| Second Download | **Free** (stays 1), identical bytes. |
| Save to Google Drive | Opened Google sign-in; **no charge**. Stopped there (untested past sign-in). |
