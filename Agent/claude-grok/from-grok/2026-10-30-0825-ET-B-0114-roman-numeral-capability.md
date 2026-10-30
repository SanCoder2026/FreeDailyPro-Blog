Sent: 2026-10-30 08:25 ET
# B-0114 Roman Numerals: vinculum >3999, step-by-step breakdown, 1–100 table — and ship B-0036 for the 38,580-impression page
Priority: P2      Estimated effort: 1 day      Report: #95      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Make the highest-impression tool on the site the best Roman numeral answer on the web, and turn impressions into clicks.

## Why
- GSC: 50 / 38,580 / 0.1% / pos 9.5; /es 11 / 9,585 (analytics file).
- Report #95: the core works well (clock-face IIII note is a plus), but it lacks vinculum >3999 (all 5 competitors in #20 have it), a step-by-step breakdown and a reference table. B-0036 (title/meta/FAQ) and B-0052 (/es hreflang) are still open.

## Who uses this
Students (homework), tattoo/wedding-date seekers, film/Super Bowl/copyright year readers, clock and watch owners, Spanish speakers (/es).

## Outcomes (ranked)
1. **B-0036 + B-0052 shipped** (title/meta/FAQ; /es hreflang and lang). These are the biggest CTR lever.
2. **Step-by-step breakdown** (1994 = M + CM + XC + IV). Low effort.
3. **Vinculum** up to 3,999,999 (overline rendering + copy as Unicode combining overline). Low/medium effort.
4. **1–100 / years table** on the page for snippets; date → "tattoo style" separators (·, ., /). Low effort.
5. Fix the horizontal scrollbar / clipped "Month.Day.Year (US)" (B-0041 evidence). Low effort.

## Constraints
Keep "Free" in SEO tags (owner); no visible "free".

## Test cases
| # | Input | Expected |
|---|---|---|
| 1 | 1994 | MCMXCIV plus the breakdown |
| 2 | 5000 | V̅ (vinculum) |
| 3 | 4000 | MV̅ (or IV̅); no "1 to 3999" error |
| 4 | IIII | 4 + clock-face note (unchanged) |
| 5 | mobile 390 | no horizontal scroll |
