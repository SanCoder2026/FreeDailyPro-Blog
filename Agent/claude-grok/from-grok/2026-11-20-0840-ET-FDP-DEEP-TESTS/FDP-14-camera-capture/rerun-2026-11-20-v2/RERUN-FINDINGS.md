Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-14 camera-capture (re-run after the trial reset)

**Supersedes:** `FDP-14-camera-capture-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-14-camera-capture-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 14 result: DONE except the JPG option (2026-11-20 22:27 EST)

One fresh context loaded at 10 (fake 1280 × 720 quad camera).

| Check | Result |
|---|---|
| CC-15 Download Full Photo | **−1** (0 → 1). File `camera-20261120-222730.png`, 1280 × 720, 39,632 B. |
| CC-16 Download Crop | **Free** after that (stays 1). File `camera-20261120-222730-cropped.png`, 512 × 286, 10,600 B. The JPG box was not ticked, so `…-cropped.jpg` is still pending. |
| Copy | **Free** (stays 1), toast "Copied to clipboard!", type `image/png`. |
| CC-17 badge | **Both downloads carry two "Created with FreeDailyPro.com" badges, top-right and bottom-right**, as the on-page notice says. This includes Download Full Photo. (The badge is intentional.) Before Download the page shows "Go paid to avoid the mark". Disclosure before Start is still FAIL, as in the original. |
| Copied crop badge | Not checked (clipboard image not saved). |

Cost pattern: 1 per visit (first export counted, the rest free). PASS under the policy.
