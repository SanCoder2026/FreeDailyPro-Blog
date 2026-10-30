Sent: 2026-10-30 13:20 ET

# B-0192 Contrast Checker: tune either colour to pass, add a lightness control
Priority: P2 · Estimated effort: S · Report: #123 · Source: QA sweep + live competitor fetch 2026-10-30 13:12 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Designers should get to a passing colour pair quickly, without trial and error.
## Why
Results are correct (#123):
- #777777 on #fff → 4.47:1, with the hint "Use #747474 (passes AA)".
- #767676 → 4.54:1, passes AA.
- An invalid value → "One of the colors isn't readable. Use HEX, rgb(), hsl() or a color name."
- Large-text and 1.4.11 non-text rows are included.
Gaps:
- Only the text colour gets a suggestion. #747474 isn't the closest passing grey; that's #767676.
- There's no lightness slider. WebAIM mentions lightness ×4; coolors mentions fix ×10 and suggest ×2 (live fetch).
- Website tool for the Color Contrast paid API (selection rule 1).
- Copy, Save and Print use trial uses → B-0156.
## Who uses this
Designers, developers and accessibility reviewers.
## Outcomes (ranked)
1. The suggestion is the closest passing colour: the smallest change in lightness, keeping the hue.
2. An option to adjust the background instead.
3. A lightness slider for each colour, with the ratio updating live.
4. Suggestions for AAA as well as AA.
## Constraints
Keep the ratio maths as it is (it's correct). Only round displayed ratios down at a threshold, never up.
## Test cases
1. #777777/#fff → suggests #767676 (4.54:1).
2. "Fix background" on #fff text over #888 → the closest passing background.
3. Moving the slider updates the ratio and the pass/fail badges together.
