Sent: 2026-11-21 17:36 ET

# FDP-77 test cases

Harness = the tool's own functions under node (`scripts/px77-harness.js`, `px77-cases.json`). Live = `cases.json`; all 22 matched the harness exactly.

| ID | Jobs (inclusive unless noted) | Expected | Result |
|---|---|---|---|
| X01–X08 (zero) | 3 jobs (blog-like), Copy ×3, Ctrl+C, edit, untick, reload | Counted or gated (owner) | **All work, 0 POSTs at 10/10 (owner question)** |
| X01–X08 (left, Firefox) | Same at 0/10 | 1 use (blog) | **0 POSTs, stays 0/10** |
| E01 | 2020-01-01–2020-12-31 | 1 y | 1 y 0 m 0 d (366 d) PASS |
| E02 | Same, unticked | Total = job line | **Job 0 y 11 m 30 d; total 1 yr 0 mo 0 d (P2)** |
| E03–E05 | 31/30/28 Jan → 28 Feb 2023, unticked | 1 month (documented) | PASS |
| E06 / E07 | 29 Feb 2020 → 28 Feb 2021 unticked / ticked | 1 y | 1 y / 1 y 0 m 1 d (P3) |
| E08 / E09 | Same day ticked / unticked | 1 d / 0 d | PASS |
| E10 | End before start | Alert, excluded | PASS |
| E11 / E12 | Back-to-back, ticked / unticked | No gap | Ticked: merged; **unticked: "Gap: 1 d" (P3)** |
| E13 / E14 / E22 | Overlap / contained / duplicate | Counted once | 3 y 5 m / 6 y / 1 y PASS |
| E15 | Gap Nov–Dec 2019 | Gap 2 mo | PASS (61 days) |
| E16 | 3 jobs unsorted | Sorted, merged | 6 y 6 m 14 d PASS |
| E17 / E19 | 20 d + 20 d; 3 × 25 d | 30-day carry | 1 mo 10 d; 2 mo 15 d (documented) |
| E18 | Blog-like 3 jobs | — | 8 yr 0 mo 0 d, gap 3 mo 13 d |
| E20 | 40-year career | 40 y | PASS (14,610 d) |
| E21 | 31 Jan → 30 Mar 2023 unticked | Total = job line | **Job 1 m 30 d; total 2 mo 0 d (P2)** |
| F01 | Future start + current | Message | **Blank, no message (P3)** |
| F02 / F03 | Start only (current); remove job 2 | Duration; total updates | PASS |
| Blog | 4 jobs from the blog | 10 y 2 m 0 d, 3,712 d, 10.2; unticked 10 y 1 m 27 d | PASS (`harness-blog.json`) |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locales English (P2) |
