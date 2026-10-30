Sent: 2026-10-30 11:33 ET

# B-0151 Job experience calculator: reversed-date error, employment gaps, labelled dates
Priority: P2 · Estimated effort: S · Report: #112 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Never leave people with a blank result, and answer the follow-up recruiters ask: "any gaps?"

## Why
Reversed dates show nothing. Overlap merging already works well. Gap reporting and business-day modes exist on calculator.net.

## Who uses this
Job seekers filling applications (473 GSC impressions).

## Outcomes (ranked)
1. "End date is before start date" message on the row. 2. List gaps between jobs (e.g. "Gap: 2 mo 3 d"). 3. aria-labels on the date fields.

## Constraints
Keep the union/overlap logic and the full-day default.

## Test cases
2024-05-01→2024-04-01 → error shown. Jobs 2020-01-01→2020-06-30 and 2020-09-01→2021-01-01 → gap of about 2 months listed. The overlap case is still 1 yr 6 mo.
