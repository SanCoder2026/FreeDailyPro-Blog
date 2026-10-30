Sent: 2026-10-30 11:05 ET

# B-0138 Calorie calculator: safe minimums and calorie cycling
Priority: P2 · Estimated effort: S–M · Report: #107 · Source: QA sweep + live competitor fetch 2026-10-30 11:01 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Make sure loss targets are never unsafe or above maintenance for small users, and offer weekly calorie cycling.

## Why
calculator.net has zigzag schedules; we cap aggressive loss at 25% but the small-user case is untested.

## Who uses this
Older or small users; people who want a weekly plan.

## Outcomes (ranked)
1. Loss targets never exceed maintenance and show a clear warning if below a safe minimum. 2. Optional weekly zigzag with the same weekly total.

## Constraints
No medical claims; keep existing sample numbers.

## Test cases
Female 60 y/155 cm/50 kg sedentary: maintenance ≈1209, no loss target above it; male sample unchanged (2336/1836/1752).
