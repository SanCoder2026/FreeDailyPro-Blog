Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-18 video-to-gif (re-run after the trial reset)

**Supersedes:** `FDP-18-video-to-gif-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-18-video-to-gif-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 18 result: DONE (2026-11-20 22:28 EST)

Context 1 loaded at 0; context 2 loaded at 10.

| Check | Result |
|---|---|
| Create GIF | Free. |
| First Download | `noaudio.gif`, **1,419,726 B = preview size**, but the **count went 0 → 10** in one click (counter jump, display-only). |
| VG-22 second Download | No further change (stays 10), identical bytes. |
| Mark | No "Created with FreeDailyPro.com" badge seen on the GIF (480 × 270, 36 frames; middle frame checked). The cap dialog says a pass removes the mark from images: copy mismatch, P2. |
| Save to Google Drive | Google sign-in popup; count stays 10. Stopped there. |

**Counter jumps (display-only):** in today's re-run a single action sometimes moved the counter straight to 10 used (merge-pdf 6→10, compress-pdf 8→10, video-to-gif 0→10, resize-crop 0→10, bulk-qr 0→10 on a failed generate). This matches the intermittent jump seen in FDP-02. It may be the box IP's daily total syncing into the page; that is unverified, and no backend claim is made. To a real visitor it would look like one click spending all of today's trial uses.