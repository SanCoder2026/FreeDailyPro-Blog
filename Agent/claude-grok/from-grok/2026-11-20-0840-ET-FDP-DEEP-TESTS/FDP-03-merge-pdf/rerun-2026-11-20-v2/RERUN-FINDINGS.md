Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-03 merge-pdf (re-run after the trial reset)

**Supersedes:** `FDP-03-merge-pdf-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-03-merge-pdf-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 3 result: DONE (2026-11-20 22:16–22:17 EST)

The first fresh context loaded at "10 remaining today" (MP-25 passed for this context; it failed 16 of 17 times on Nov 19).

| Check | Result |
|---|---|
| Cost per merge | **0.** Merging never changed the count (S1–S7). The result area says "Download uses 1 trial use". |
| Cost per download | **−1 each:** S1 0→1, S2 1→2, S3 2→3, S4 3→4, S5 4→5, S6 5→6 (`battery-*.json`). PASS. |
| **S7 (503-page merge) download** | **6 → 10 in one click** (counter jump; see below). The 503-page output is correct. |
| Badge | "Created with FreeDailyPro.com" text is on the pages of every download (S3: 5 pages, 4 badges; the inserted blank page seems to have none). MP-13 stays **FAIL**: the page copy says "no watermark". |
| File names | `<first file>-merged.pdf` (e.g. `B_letter_2p-merged.pdf`). |
| Pass removes the badge | Untested: no payment allowed. |

**Counter jumps (display-only):** in today's re-run a single action sometimes moved the counter straight to 10 used (merge-pdf 6→10, compress-pdf 8→10, video-to-gif 0→10, resize-crop 0→10, bulk-qr 0→10 on a failed generate). This matches the intermittent jump seen in FDP-02. It may be the box IP's daily total syncing into the page; that is unverified, and no backend claim is made. To a real visitor it would look like one click spending all of today's trial uses.

**New P1 (display-only):** one Download moved the count from 6 to 10 (S7, 22:17 EST).
