Sent: 2026-10-30 08:09 ET
# B-0087 Percentage Calculator: solve-any-two, percentage points, worked steps
Priority: P2      Estimated effort: 0.5–1 day      Report: #89      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Close the small gap to Calculator.net and Omni so the tool is mature and earns clicks on "percentage calculator online" (505 impressions, 0 clicks, pos 10.4).

## Why
- `analytics/2026-07-10-to-now-raw.md`: query "percentage calculator online" 0/505/0%/10.4.
- Report #89: competitors solve any 2 of 3 fields in place (Calculator.net, Omni) and explain percentage points and per mille/basis points (Omni). FDP has more modes but each mode works in one direction only.

## Outcomes (ranked)
1. **Solve any two**: in "% of" mode, filling result + number gives the %, and so on. Low effort.
2. **Worked steps** under the result (2–3 lines, e.g. "150 × 0.20 = 30"). Low effort.
3. **Percentage-point vs percent** output in % change mode when both values are percents (10% → 12% = +2 pp = +20%). Low effort.
4. **Per mille / basis-point** units toggle. Low effort.
5. **Session history** of the last 10 calculations (local only, cleared on close), with copy. Low effort; no competitor has this.
6. **API parity** for all modes with validation (division by zero → 400).

## Constraints
Trial-use rules unchanged; no visible "free".

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | % of: number 150, result 30 | 20% |
| 2 | % change 10 → 12 (as %) | +2 pp, +20% |
| 3 | 25 bps of 10,000 | 25 |
| 4 | X is what % with Y = 0 | inline message, no NaN |
