Sent: 2026-11-20 23:05 ET

# FDP-27 BMI Calculator: test cases

URL https://www.freedailypro.com/tool/bmi-calculator, guest. Defaults: metric, 70 kg, 170 cm, age/sex/waist empty, Asian off, Target BMI 24.9. "Live" = 2026-11-20 22:42–22:57 EST. "Currently: FAIL" should pass after the fix. Scripts: `scripts/bmi-live.js` (cases B*/I*), `bmi-gate.js`, `bmi-privacy.js`, `bmi-misc.js`, `bmi-share.js`.

## A. Calculation (reading only)
| ID | Input | Expected | Live |
|---|---|---|---|
| BMI-01 | default 70 / 170 | 24.2 Normal; range 53.5–72.0 kg; Prime 0.97; Ponderal 14.2 | PASS |
| BMI-02 | 50 kg | 17.3 Underweight; gain about 3.5 kg; WHO Mild thinness | PASS |
| BMI-03 | 90 kg | 31.1 Obese; lose about 18.0 kg; WHO Obese class I | PASS |
| BMI-04 | 72.25 kg | 25.0 Overweight | PASS |
| BMI-05 | 72.2 kg (exact 24.98) | Normal (WHO < 25), or the rounding rule stated | **Currently: FAIL** (Overweight, "lose 0.2 kg") |
| BMI-06 | 53.4 kg (exact 18.48) | Underweight, or the range edge consistent with the label | **Currently: FAIL** (Normal, range starts at 53.5) |
| BMI-07 | 70 kg + Asian | Overweight (Asian); range to 66.2 kg; target line consistent with the card | **Currently: FAIL** (target says "gain 2.0 kg") |
| BMI-08 | 80 kg + Asian | Obese (Asian); one "lose" figure | **Currently: FAIL** (13.8 vs 8.0) |
| BMI-09 | default, Target section | No "gain" suggestion for a Normal result by default; grammatical wording | **Currently: FAIL** ("which is gain 2.0 kg") |
| BMI-10 | age 15 | Category hidden; child note; link to a percentile tool or an own chart | PARTIAL (no link) |
| BMI-11 | age 1 | Under-2 note | PASS |
| BMI-12 | age 25.5 / 130 / abc | Error, and the extras stay or say why they are hidden | PARTIAL (extras vanish silently) |
| BMI-13 | height 1.7 | "That looks like metres…" | PASS |
| BMI-14 | 99 / 251 cm; 29 / 301 / −5 kg | Range messages, no result | PASS |
| BMI-15 | weight "abc" / empty | "Numbers only, please." / "Enter your weight." | PASS |
| BMI-16 | "70,5" | 24.4 | PASS |
| BMI-17 | waist 85 / 60 / 110 cm | WHtR 0.50 / 0.35 / 0.65 with notes | PASS |
| BMI-18 | waist 5 | Error naming the waist | PARTIAL ("length") |
| BMI-19 | target 22 | 63.6 kg, lose 6.4 kg | PASS (numbers) |
| BMI-20 | target type Prime 1 | 72.2 kg | PASS |
| BMI-21 | target 5 | "Enter a target BMI between 10 and 60." | PASS |
| BMI-22 | target "abc" | Error message | **Currently: FAIL** (nothing shown) |
| BMI-23 | 300 kg / 100 cm | 300.0, Obese class III, gauge clamped | PASS |
| BMI-24 | 30 kg / 250 cm | 4.8, Severe thinness | PASS |
| BMI-25 | Sex female, adult | Field has a purpose, or no misleading note | **Currently: FAIL** ("child percentile charts" that don't exist) |
| BMI-26 | Imperial 154 lb, 5 ft 7 in | 24.1 Normal; 118–159 lb | PASS |
| BMI-27 | Imperial 200 lb, 6 ft 0 in | 27.1 Overweight; lose 16 lb | PASS |
| BMI-28 | 5 ft 12 in | Inches error | PASS |
| BMI-29 | 50 lb | "Enter a weight between 66 and 661 lb." | PASS |
| BMI-30 | 5.5 ft, 0 in | 24.9 Normal; target line not "gain 0 lb" | PARTIAL |
| BMI-31 | 154 typed in kg | A plausibility hint (as the blog claims), or the blog corrected | **Currently: FAIL** (53.3 accepted, no hint) |

## B. Exports, trial uses, sharing, privacy
| ID | Steps | Expected | Live |
|---|---|---|---|
| BMI-32 | Context at 0 remaining: all 6 exports | Per Santosh's decision: either cap dialog → Day Pass → email prompt (stop), or uncounted on purpose | **Policy question** (all 6 work, no dialog) |
| BMI-33 | Context with uses: all 6 exports, then reload | Per decision; documented on the page | **Policy question** (0 → 0) |
| BMI-34 | Download CSV | CSV with BMI, category, inputs, date (plus the WHO table) | **Currently: FAIL** (WHO table only) |
| BMI-35 | Print or save as PDF / Print | Sheet shows BMI, category, inputs, range, date; no controls | **Currently: FAIL** |
| BMI-36 | Both Copy result buttons | One consistent text with inputs; no sr-only gauge sentence | **Currently: FAIL** |
| BMI-37 | Type 87.3 / 179.5, scroll, reload; watch the network | No request to any host carries the values | **Currently: FAIL** (GA, doubleclick, AdSense ping, server) |
| BMI-38 | Share this tool | Link copied; opens to the same result incl. options (only when the user chooses to share numbers) | PARTIAL (drops age/Asian) |
| BMI-39 | Add to favorites, Recent calculations, Clear | Local only; history in memory; Clear empties it | PASS |
| BMI-40 | Video at ~0:50 | Current tool UI; no calories promise | **Currently: FAIL** |
