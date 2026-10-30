Sent: 2026-10-30 15:41 ET

# B-0300 Job Experience Calculator: position 54 — show overlap and gaps, label the dates
Priority: P2 · Estimated effort: S · Report: QA-REPORT-158 · Source: live probe 2026-10-30 ~15:37-15:41 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A job seeker gets the exact total an application asks for, and can see why it is that number.

## Why
GSC: 2 clicks / 473 impressions / 0.4% CTR / position 54.4.
Checked live (15:39 ET): Job 1 2020-01-01→2021-12-31 = "2 years, 0 months, 0 days (731 total days)"; Job 2 2021-07-01→2022-06-30 = 1 year; total "2 yr 6 mo 0 d, about 2.5 years (2 jobs, overlapping periods counted once)" ✔ correct union. Reversed dates on Job 2 → "End date must be after start date" and the total drops that job ✔ (L-219's silent no-result is fixed).
- Date inputs still have no accessible name (checked: aria-label and label both empty on all 4 date fields) → L-219 / B-0155.
- "Currently working here" is ticked by default on every new job, so Job 2's end date was disabled until unticked (checked).
- The result shows only the merged total; the overlap (6 months here) and any gaps are not listed (checked on the result text).
Competitors (live search): experiencecalculator.net shows overlaps and gaps separately; unitconvertertool.com gives a timeline and copy formats (resume, months-only, decimal, govt); calcifyai shows decimal years, months, weeks, days.
Title 61 with "Free"; meta 132. /es title English → L-189. Ad text ("Compare Browsers", "Automate Work") → L-004.

## Who uses this
Job applicants, HR, visa and government-form applicants.

## Outcomes (ranked)
1. Snippet as below (page sits at position 54).
2. List overlap and gap periods under the total.
3. Label each date input ("Job 1 start date"); new jobs default to unticked "Currently working here".
4. Extra copy formats (months only, decimal years).

## SEO
- Now: title "Total Work Experience Calculator - Free Online | FreeDailyPro" (61, has Free); meta 132; H1 "Job Experience Calculator"
- Keywords: work experience calculator, total experience calculator, experience in years and months, multiple jobs
- Suggested Title: "Work Experience Calculator: Total Across Jobs | FreeDailyPro" (60)
- Suggested Meta: "Add each job's start and end dates and get total work experience in years, months and days, with overlapping jobs counted once, ready to copy for a CV." (151)
- Suggested H1: "Work Experience Calculator (Multiple Jobs)"
- FAQ: Are overlapping jobs counted twice? · Does the end date count? · How do I show experience in months? · Are gaps excluded?

## Constraints
Keep the full-day toggle and overlap-union math.

## Test cases
1. The two jobs above → 2 yr 6 mo 0 d (regression); overlap "6 months" listed.
2. Jobs 2018-01-01→2018-12-31 and 2020-01-01→2020-12-31 → total 2 years; gap 2019 listed.
3. Reversed dates → error and job left out (regression).
4. Screen reader names every date input; Add Another Job → end date enabled.
5. Title ≤60, meta 140–160; 390 px no overflow.
