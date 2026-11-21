Sent: 2026-11-21 17:36 ET

# FDP-77 Job Experience Calculator (job-experience-calculator): deep test report for Claude

- **Written:** 2026-11-21 17:55 EST (box `date`, ET). Testing ran 2026-11-21 17:25–17:50 EST.
- **Tool:** https://www.freedailypro.com/tool/job-experience-calculator
  - TEST-ORDER row 77: **Pro**, Resume & Career. Plan note "test-plan (unranked): GSC top-50 SEO backfill 16". No duplicate group (Age & Date Calculator is the general date-span tool).
  - **No trial strip, no Quick Buy and no prices on the page** (all 6 geo contexts, every device). JSON-LD Offer $4.99. `fdp-usage-v1` exists (tier professional, 10/day).
  - Video FtITWJlgVKM (embedded, 76 s, uploaded 2026-09-23). Blog /blog/job-experience-calculator "Add Up Work Experience Without Counting Overlaps Twice" (200, linked).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (`JobExperienceCalculator-fu8pMVn_.js` + `dates-DoPZ1fRV.js`, pretty copies in `js/`):**
  - Job cards (optional label, start, end, "Currently working here" ticked by default = today's local date), Add Another Job / Remove, and "Count the end date as a full day" (ticked by default, which adds one day to each end).
  - Per job: calendar years/months/days (month-end clamped) + total days.
  - Total: periods are merged when they overlap or touch, each merged period's y/m/d are added, and days are carried into months at 30. "about N years" = total days / 365.25.
  - Gaps between merged periods are listed with two or more jobs. Copy summary gives one line per job, the gaps and the total. The reversed-date alert leaves that job out.
  - Usage: `useLogToolUsage(true, 3000, { ownActions: true })`. Its copy/clipboard gate and auto-log only act when the tool is `known`. Nothing else charges.
- **Testers:**
  - Desk: page copy (1 FAQ, how-to, tip), JSON-LD, blog, JS.
  - **Offline harness** (`scripts/px77-harness.js`): the tool's own date and total functions copied verbatim. 22 cases + the blog's 4-job example, ticked and unticked (`evidence/harness/`). **All 22 cases entered live match the harness exactly** (per-job y/m/d and total).
  - Playwright, guest:
    - `zero.json`: Chromium at 10/10. 3 jobs, Copy summary, Ctrl+C on the total, edit a date, copy again, untick, reload + new job, copy. Clipboard read back.
    - `left-firefox.json`: the same at 0/10 (try 6 of 30).
    - `cases.json`: 22 harness cases + future start, start only, remove a job.
  - Video frames; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** none. There's no Drive, cloud, account feature or paid path on this page.
- **RERUN-AFTER-RESET:** none. Behaviour was observed both at 10/10 and at 0/10.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to a job seeker filling in "total years of experience" on an application or visa form, and whether the page turns that into a pass.

**Owner context:** copy and results count as trial uses (Oct 30). Unit Converter, Grammar Checker and Word Counter are uncounted on purpose; any other tool that takes no trial use is an owner question (Nov 20; #68, #74 and #76 filed the same way). Per-page-load charging is P1. A full-quality result at 0 is a pending owner question (Nov 21, corrected 1:19 PM).

**P0 / P1:** none found.

**Owner question:**
- **The tool takes no trial use at all.**
  - At 10/10 (Chromium): results, 3 Copy summary presses, Ctrl+C on the total, an edit, untick and a reload with a new job → no dialog, 0 `usage.log` POSTs; the clipboard holds the full summary.
  - At 0/10 (Firefox): the same 8 actions → still 0/10, 0 POSTs.
  - The blog says "the calculator counts toward the 10 trial usages a day". The video shows "10 free uses daily / 8 free uses left today" chips. The page has no strip, because the tool isn't `known`.
  - Decide: register it (results/Copy counted per policy), or list it as uncounted and fix the blog line and the JSON-LD Offer.

**P2 — where to look:**
- **With "Count the end date as a full day" unticked, the total disagrees with the job's own line.**
  - One job 1 Jan–31 Dec 2020 shows "0 years, 11 months, 30 days (365 total days)", but the total panel says **"1 yr 0 mo 0 d"** (`E02-year-exclusive.png`). 31 Jan–30 Mar 2023: job "1 month, 30 days", total "2 mo 0 d" (E21).
  - Cause: the 30-day carry (`u += floor(r/30)`) runs even for a single period. The tip says "a 30-day month is used only when carrying leftover days between periods".
  - Someone who unticks the box to follow a form's rule sees two different answers for one job. Fix: carry only when summing two or more periods, or carry at the real month length.
- **Video FtITWJlgVKM is out of date:**
  - It shows breadcrumb "Converters & Calculators" (now Resume & Career), "10 free uses daily" and "8 free uses left today" chips ("free" wording, no strip on the live page), and the old "--" subtitle.
  - It shows a single job only, with no Add Another Job total, gaps or Copy summary (the tool's main selling point per its blog title).
  - The demo job runs 10-06-2026 to 17-08-2028 (future dates), shown with exclusive counting, the opposite of today's default.
  - The browser find bar ("job e") is open. No personal tabs.
- **Locale pages:** 10 hreflang pages 200 with translated navigation, but the H1, labels ("Start Date", "Currently working here"…), result text and FAQ are English. The date inputs follow the browser locale.

**P3:**
- Unticked mode reports a **1-day gap between back-to-back jobs** (30 Jun → 1 Jul: "Gap: 1 d", E12). The blog example's 2-day break shows as 3 days unticked.
- A future start date with "Currently working here" ticked shows nothing and no message (F01). The reversed-date alert only appears when the box is unticked.
- 29 Feb 2020 – 28 Feb 2021 counted inclusive = "1 year, 0 months, 1 day" (366 days), not 1 year.
- The only FAQ ("Does this handle overlapping employment periods correctly?") never says overlaps are merged and counted once. The tip and the total label do.
- Gap y/m/d can jump by several days when the box is toggled (3 mo 13 d ↔ 3 mo 17 d for 105 ↔ 106 days), from calendar-month clamping at 28 Feb. Correct, but surprising.
- iPhone SE 9 px overflow (329/320, header button); ja desktop overflows a few px. Pixel 7 CLS 0.10. axe desktop: label-content-name-mismatch (serious, `.right-2`) + region (moderate); Pixel 7 clean.

## Intent

A job seeker needs one defensible "total years of experience" figure with overlaps counted once and gaps explained. The tool does that: overlap merge, contained jobs, unsorted entries, gaps, month-end clamping, leap years, reversed dates and a clean Copy summary were all correct on 22 cases. The blog's worked example reproduces exactly (10 yr 2 mo 0 d, 3,712 days, 10.2 years; unticked 10 yr 1 mo 27 d). The open points are the unticked-mode mismatch between a job and the total, a stale video, and the fact that it never counts a trial use.

## What works

- **Overlaps:** 2018–2020 + Jun 2019–May 2021 → 3 yr 5 mo (E13). A job contained in another adds nothing (E14). Duplicate entries count once (E22).
- **Unsorted entries** are sorted and merged (E16).
- **Gaps:** "Gap: 2 mo (61 days, between 2019-10-31 and 2020-01-01)" (E15). Back-to-back jobs, ticked → "No gaps".
- **Edge dates:** same day ticked = 1 day; 31 Jan → 28 Feb = 1 month (documented); 40-year career = 14,610 days.
- **Reversed dates:** alert "End date is before the start date, so this job isn't counted…" and the job is excluded.
- **Copy summary:** "Job: 2016-03-01 to 2019-05-31 = 3 y 3 m 0 d … Gap: 3 mo 13 d between 2021-02-28 and 2021-06-14 / Total (overlaps counted once): …". Ctrl+C on the total works too.
- **Blog numbers** reproduce exactly in the harness.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | 22/22 cases correct vs the tool's own maths; overlaps merged. |
| 2 | Completeness | PASS | Multi-job, gaps, inclusive toggle, Copy summary. No CSV import (fine). |
| 3 | Ease of use | PASS | Live results; clear reversed-date alert. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px. |
| 5 | Payment process | N/A | No strip, prices or Quick Buy on the page. |
| 6 | Information correct | PARTIAL | Unticked total ≠ job line; tip's "only between periods" not true; blog says it counts trial uses. |
| 7 | Indexing | PASS | 200, canonical self, hreflang set. |
| 8 | SEO | PASS | Title "Total Work Experience Calculator" (54); meta ~150. |
| 9 | Blog | PASS (minor) | Numbers exact; trial-usage line false today. |
| 10 | YouTube video | PASS | Embedded and linked. |
| 11 | FAQ / guide correct | PARTIAL | One vague FAQ; tip contradicted by the single-job carry. |
| 12 | Video shows current capability | FAIL | Old category, "free uses" chips, single job only, future-dated demo. |
| 13 | Storage | N/A | None. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | N/A | Copy only. |
| 16 | Usage count | **OWNER QUESTION** | Never counts (0 POSTs at 10/10 and 0/10). |
| 17 | Categorization in section | PASS | Resume & Career. |
| 18 | Correct section of site | PASS | Next step Resume Builder; related CV tools. |
| 19 | AI need and demand | PASS | "work experience calculator", "total years of experience"; chat AIs miscount overlaps. |
| 20 | Merge better? | No | Distinct from Age & Date Calculator (multi-job merge). |
| 21 | Remove? | No | GSC top-50 backfill; works well. |
| 22 | Duplicates | None | — |

## After fixes, rerun

- `node scripts/px77-harness.js` (E02/E21: total should equal the job line) and `px77-live.js cases`.
- `px77-live.js zero` and `left firefox` if the owner decides it should count.
