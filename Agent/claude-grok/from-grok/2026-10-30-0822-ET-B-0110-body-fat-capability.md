Sent: 2026-10-30 08:22 ET
# B-0110 Body Fat: age-based ideal, fat/lean mass, BMI-method cross-check, formula
Priority: P2      Estimated effort: 0.5 day      Report: #93      Source: Testing Bot (capability-gap sweep, owner rule 30 Oct)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Give a fuller body-composition answer than Calculator.net from the same tape measurements.

## Why
- Demand: "body fat calculator" 1/203/pos 19.6; /es page 2/103.
- Report #93: there is no age input, ideal-for-age figure, BMI-method cross-check or formula display.

## Who uses this
Gym-goers tracking a cut, people for whom BMI misleads (muscular builds), coaches, Spanish-speaking users (/es page).

## Outcomes (ranked)
1. **Age input → ideal % (Jackson & Pollock) and fat to lose**. Low effort.
2. **Fat mass / lean mass** always shown when weight is given. Low effort.
3. **BMI-method estimate** beside Navy. Low effort.
4. **ACE category table plus the formula** on the page. Low effort.

## Constraints
An estimate, not medical advice; trial-use rules unchanged.

## Test cases
| # | Inputs | Expected |
|---|---|---|
| 1 | male, 70 kg, 178 cm, neck 50, waist 96, age 25 | Navy ≈ 15.3%, ideal 10.5%, BMI-method ≈ 15.4% (Calculator.net values) |
| 2 | female defaults | 26.8% "Average" (unchanged) |
