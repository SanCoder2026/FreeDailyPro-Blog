Sent: 2026-11-20 22:45 ET

# RERUN-FINDINGS: FDP-02 audio-comparer (re-run after the trial reset)

**Supersedes:** `FDP-02-audio-comparer-2026-11-19.zip` for the items listed below. That zip is frozen and was not edited; everything else in it still stands.
**This package:** `FDP-02-audio-comparer-2026-11-20-v2.zip` · built 2026-11-20 22:38:37 EST (box `date`).
**How it ran:** guest, fresh Chromium contexts from the box IP, no sign-in, no payment, no email or card typed, stopped at any email prompt, Stripe page or Google sign-in. Counters (the strip and localStorage `fdp-usage-v1`) are display-only evidence; no backend claims. GSC data is not available.


## Row 2 result: DONE (2026-11-20 22:12–22:16 EST)

All 14 fresh contexts (2 usage runs + 12 verify-pair contexts) loaded at "10 remaining today".

| Check | Result |
|---|---|
| Cost of one Compare | **−1** (strip 10 → 9, `usageToday` 0 → 1). Play, switching files, Match loudness, Download difference WAV, Copy summary, Share, Compare another and reload all cost nothing (`usage-results.json`). Compare is the counted action, so the tool does take trial uses: PASS under the Oct 30 policy. |
| Counter jump | No 10 → 0 jump seen in this tool today. |
| **AC-19** (72 s `melody_then_noise` as File 1 vs `melody_12s`) | **Still FAIL, 4 of 4 runs:** 100.0% and "Same recording, possibly a different format or quality". Strip: 12 green cells, then 60 grey "silence" cells for 0:12–1:12, where File 1 has loud noise and File 2 has nothing. Screenshot: `screens/AC19-v23r1-crop-1120.png`. |
| AC-19 mirror (v21: 12 s vs 72 s) | Also 100% (4 of 4). |
| v22 (offset copy) | Offset +20.03 s, 100% (4 of 4): PASS. |
| Accessibility of the result | Drop zones are `tabindex=0`; Enter and Space open the chooser; there is a live region. After Compare, focus goes to `BODY`, not the result (P2, as in the original). |

**P1 (unchanged, now re-confirmed with a screenshot):** AC-19. A 72-second file whose last minute is unrelated noise is reported as the "Same recording" at 100%. The extra minute is drawn as grey "silence" instead of "differs" or "no counterpart".
