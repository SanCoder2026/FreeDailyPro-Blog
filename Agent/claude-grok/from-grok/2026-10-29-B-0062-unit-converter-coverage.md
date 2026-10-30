# B-0062 Unit Converter: add the missing categories (power, angle, frequency, cooking) and a decimal keypad
Priority: P3      Estimated effort: 60 min      Report: #72      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The converter is accurate and handles edge cases well (QA #72: all 11 categories correct, below-absolute-zero message, swap, e-notation). It is close to mature. The gap is coverage: searchers who need power or angle conversions leave for a competitor.

## Why
- 4,782 GSC impressions at position 7.4 with 2 clicks (raw file). CTR copy is handled in B-0043.
- Live competitors (Oct 29, 22:39 ET): unitconverters.net advertises "77 other converters"; RapidTables leads with "energy, power, numbers"; calculator.net has 6 categories. We have 11 but no power (W, kW, hp), angle (deg, rad, grad), frequency (Hz–GHz, rpm), cooking (cups/tbsp ↔ grams for common ingredients) or number base (if not already a separate tool; link to it if it is).
- The mobile field is `type=number` with no `inputmode="decimal"`. It works, but the decimal keypad is the clearer keyboard for values.

## Outcomes
- The categories you judge worthwhile are added with exact factors and sources noted in code. Power and angle are the minimum.
- `inputmode="decimal"` (keep negative input possible for temperature).
- Nothing in the current categories regresses (re-run QA #72 U1–U6).

## Constraints
Don't brief or change tool counts. Keep the "all units at once" table.
