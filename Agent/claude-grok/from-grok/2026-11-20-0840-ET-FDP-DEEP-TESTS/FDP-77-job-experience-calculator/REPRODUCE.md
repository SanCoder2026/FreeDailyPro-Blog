Sent: 2026-11-21 17:36 ET

# FDP-77 reproduce

1. **Total ≠ job line (P2):** https://www.freedailypro.com/tool/job-experience-calculator → untick "Currently working here" → Start 2020-01-01, End 2020-12-31 → untick "Count the end date as a full day" → job line "0 years, 11 months, 30 days (365 total days)", total "1 yr 0 mo 0 d".
2. **No trial use:** any guest window at 10/10 (`fdp-usage-v1`) → enter jobs → results appear; Copy summary → clipboard filled; no dialog, and DevTools shows no `usage.log` POST. The same at 0/10: the counter never moves.
3. **Back-to-back gap (P3):** Job 1 2020-01-01 → 2020-06-30, Job 2 2020-07-01 → 2020-12-31, box unticked → "Gap: 1 d".
4. **Future start (P3):** Start 2027-03-01 with "Currently working here" ticked → no duration, no message.
5. **Offline:** `cd scripts && node px77-harness.js ./px77-cases.json`.
