Sent: 2026-10-30 11:10 ET

Supersedes 2026-10-30-1105-ET-B-0138-calorie-floor-zigzag.md

# B-0138 Calorie calculator: meaningful loss tiers and calorie cycling
Priority: P2 · Estimated effort: S–M · Report: #107 + addendum · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make every loss option a real choice, keep the safe-minimum handling that already works, and offer weekly calorie cycling.

## Why
The admin session found the floor handling already works: Case A hides loss targets and warns at 1200. But in Case B the 25% cap leaves "Aggressive" (1535) only 11 cal below Moderate (1546), and both are labelled about 1.0 lb a week. calculator.net offers zigzag schedules; we do not.

## Who uses this
Smaller or moderately active users; people who want a weekly plan.

## Outcomes (ranked)
1. When the cap leaves the aggressive tier within ~100 cal of moderate, merge or relabel it rather than showing two near-identical options. 2. Keep the Case A behaviour ("Not recommended" plus the 1200 warning). 3. Optional weekly zigzag with the same weekly total.

## Constraints
No medical claims; unchanged numbers for the male sample (2336/1836/1752) and for Cases A–C apart from the tier label.

## Test cases
Case B (F 30/165/60, moderate): no two loss tiers within 100 cal with the same lb/week label. Case A unchanged. Imperial 5'5"/132 lb within 1 cal of metric.
