Sent: 2026-11-21 17:36 ET

# Live functional findings (FDP-77)

- Zero (Chromium, 10/10) and left (Firefox, 0/10, try 6): 8 actions each (3 jobs, Copy summary ×3, Ctrl+C on the total, date edit, untick, reload + new job) → 0 `usage.log` POSTs, counter unchanged, no dialog. The clipboard held the full summary (Chromium).
- Cases: 22/22 live = harness. E02/E21 show the total ≠ job line in unticked mode; E12 a 1-day gap for back-to-back jobs (unticked); F01 a blank result for a future start with "Currently working".
