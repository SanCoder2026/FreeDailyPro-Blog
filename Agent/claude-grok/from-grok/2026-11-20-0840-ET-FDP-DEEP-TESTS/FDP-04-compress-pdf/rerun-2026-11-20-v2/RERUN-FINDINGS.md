Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-04 compress-pdf (re-run after the trial reset)

**Supersedes:** `FDP-04-compress-pdf-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-04-compress-pdf-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 4 result: DONE except the batch ZIP (2026-11-20 22:17–22:20 EST)

One fresh context loaded at "10 remaining today".

| Check | Result |
|---|---|
| Cost per compress | 0 (never counted). |
| Cost per download | −1 for the first download of each run: S1 0→1 … S8 7→8. **S9 (one download) went 8 → 10** (counter jump). |
| CP-31: second level of the same run | **Free.** S1b (level-1 download after the S1 download) left the count at 1. |
| CP-22 / CP-04 sizes | S1 A balanced 334,650 B (6 pages). Target 200 KB (S5) → **198,355 B (193.7 KB)**: under target. The 1 MB target was not re-run. |
| CP-23 structure (D) | Outline 3, link annotations 3, form fields 2: **kept**. PASS |
| CP-24 non-Latin (G) | Japanese, Cyrillic, Greek and Arabic text extractable. PASS |
| CP-25 sizes / rotation (H) | Page sizes and `/Rotate 90` kept. PASS |
| CP-28 unlocked E | Output **not encrypted**. PASS |
| CP-26 mark | **No "Created with FreeDailyPro.com" badge** on any downloaded page (checked visually). `watermark_text_found=True` on D in `output-inspection-1120.json` comes from D's own "freedailypro.com" link text, not a badge. PASS (but the cap dialog says a pass "removes the mark from your PDFs": copy mismatch, P2). |
| CP-27 batch "Download all (ZIP)" | **Still pending.** S8 downloaded the single A file, not the ZIP. |

**Counter jumps (display-only):** in today's re-run a single action sometimes moved the counter straight to 10 used (merge-pdf 6→10, compress-pdf 8→10, video-to-gif 0→10, resize-crop 0→10, bulk-qr 0→10 on a failed generate). This matches the intermittent jump seen in FDP-02. It may be the box IP's daily total syncing into the page; that is unverified, and no backend claim is made. To a real visitor it would look like one click spending all of today's trial uses.

**New P1 (display-only):** one Download moved the count from 8 to 10 (S9, 22:20 EST).
