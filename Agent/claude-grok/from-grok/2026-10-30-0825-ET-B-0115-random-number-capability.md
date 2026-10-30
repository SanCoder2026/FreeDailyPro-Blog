Sent: 2026-10-30 08:25 ET
# B-0115 Random Number Generator: decimals, presets (dice/lottery/list), method note — and reconsider the trial gate on one Generate
Priority: P2      Estimated effort: 0.5–1 day      Report: #95      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Give a more complete randomness tool than Calculator.net, and make sure a first-time visitor can see one result before hitting a trial wall.

## Why
- GA 66 views (#31 page); GSC 4/614/pos 11.2 (analytics file).
- Report #95: Generate consumes a trial use (0 left on the test IP, so no result could be read), unlike calculators where "reading results never uses a trial use". Decimals, presets and a method note were not seen. L-147/B-0080 is still open.

## Who uses this
Teachers picking students, giveaway/raffle hosts, gamers (dice), developers needing test numbers, lottery players.

## Outcomes (ranked)
1. **Owner decision**: let Generate show results without a trial use (copy/export still counts), matching calculators. Low effort.
2. **Decimals + precision**; large ranges. Low effort.
3. **Presets**: dice (NdM), coin, lottery (pick k of n), pick from a pasted list / shuffle. Low effort.
4. **Method note** ("crypto.getRandomValues, unbiased"), plus an optional seed for reproducible lists. Low effort.
5. Close B-0080 (reason shown when min is invalid).

## Constraints
No fake usage in testing; trial-use rules per owner decision.

## Test cases
| # | Input | Expected |
|---|---|---|
| 1 | first visit, 1–100 | a result is visible |
| 2 | 0.5–1.5, 3 dp, 5 numbers | 5 decimals in range |
| 3 | 1–5, 6 unique | clear error (impossible) |
| 4 | lottery 6 of 49 | 6 unique sorted numbers |
