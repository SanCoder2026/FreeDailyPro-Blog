Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-07 custom-qr (re-run after the trial reset)

**Supersedes:** `FDP-07-custom-qr-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-07-custom-qr-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 7 result: PARTLY DONE (2026-11-20 22:21–22:25 EST); C, D2, WebKit and a real-phone scan still pending

Context B loaded at "2 remaining today". Contexts C and D (opened right after) loaded at 0 and only showed the cap dialog.

| Check | Result |
|---|---|
| (b) one click costing 2 | **Re-confirmed:** one "Download PDF" click moved the strip from 2 remaining to 0 (`usageToday` 0 → 2). |
| (a) gate leak | **Re-confirmed:** on the same page load, "Download ZIP" then succeeded at "0 remaining" (`styled-qr-codes.zip`, 314,999 B; count stayed 2). |
| (c) PDF | 1 page, 141.7 × 167.7 pt. **Does not decode** at 600 dpi (also not with 60–120 px white padding added). The "Created with FreeDailyPro.com" badge sits over the frame label. The code runs to the page edge with no quiet zone. The frame text "Escanéame 扫码" extracts as "Escan?ame ??" (non-ASCII lost). |
| B2 / CQ-24 ZIP at 2000 px | **FAIL re-confirmed:** 2000 px was chosen but the 3 PNGs are **1000 × 1180** (frame included). All 3 decode; index.csv is correct. |
| CQ-25 "name,value" | The line `name3,https://c.example` was encoded literally (`name3,https://c.example`) with file `003-name3-https-c-example.png`. The script did not tick "Lines are name,value", so CQ-25 itself is still **not run**. |
| D2 (gradient PNG 2000) | **Not observed** (context loaded at 0). |
| Fresh context at 2 after reset | Yes for the first context (B); the next two loaded at 0. WebKit not run. |
| Real-phone scan | Not possible from the box (no phone). Pending for Santosh. |
| Pass removes the PDF badge | Untested (no payment). |

**P0/P1 status:** the gate leak (downloads succeed at 0 remaining) and the one-click-costs-2 issue are both still live.
