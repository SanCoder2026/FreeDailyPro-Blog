Sent: 2026-10-30 11:05 ET

# B-0137 BMR: let users choose the formula and add body fat
Priority: P2 · Estimated effort: S–M · Report: #107 · Source: QA sweep + live competitor fetch 2026-10-30 11:01 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Give fitter users a more accurate BMR when they know their body fat.

## Why
calculator.net offers Mifflin, Harris-Benedict and Katch-McArdle with body fat; we only offer Mifflin.

## Who uses this
Lifters and people who know their body fat from a scan.

## Outcomes (ranked)
1. Optional body-fat % field switches to Katch-McArdle. 2. Formula picker with Mifflin as default. 3. Show which formula was used.

## Constraints
Keep the default result identical (1699 for the sample).

## Test cases
75 kg, 15% body fat → Katch 370+21.6×63.75 = 1747; Mifflin default still 1699.
