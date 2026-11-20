Sent: 2026-11-20 08:40 ET

# Live functional findings: unit-converter

- **Run:** 2026-11-19 13:57–14:02 EST (box `date`, ET), headless Chromium, guest. Scripts: `scripts/uc-probe.js`, `uc-live.js`, `uc-gate.js`, `uc-kbd.js`. Files: `json/probe.json`, `json/cases.json`, `json/gate.json`, `json/kbd.json`.
- **Reference:** exact legal definitions (1 in = 2.54 cm, 1 lb = 0.45359237 kg, US gal = 3.785411784 L, UK gal = 4.54609 L, 1 atm = 101325 Pa, IT BTU, mechanical hp = 745.6998716 W) and NIST SP 811 factors, typed independently into `uc-live.js`.

## Conversions: exact

55 cases (U01–U48, K01–K07) across all 15 categories. Every numeric case matches the reference to 10 significant digits. Three rows first flagged by the script are reference or display items, not tool errors:
- U06 (1,000,000 km → nm): the tool's 1e18 is right; the script's expected value was wrong.
- U41 (30 UK mpg → US mpg): the tool's 24.98022554 is right; the script's expected value was wrong.
- U33 (1 atm → mmHg = 759.9998917): correct for the conventional mmHg (133.322387415 Pa). There is no torr unit, so users looking for "760" won't find it (P2 completeness).
- Temperature, including −40 = −40, 98.6 °F = 37 °C, Rankine, and absolute zero: right. Below absolute zero shows a clear alert (U24, U26).
- Fuel economy reciprocals: right. 0 L/100 km shows "—", as the page says.
- Cooking grams per cup: flour 120, sugar 200, brown sugar 213, butter 227, honey 339, milk 244, oil 218, water 236.59. These are typical published values (King Arthur / USDA style), and the page labels them approximate.
- The URL state (`?c=&from=&to=&v=`) loads exactly as the FAQ says (98.6 °F → 37; ½ cup butter → 113.5 g). Invalid values (1e400) fall back to 1.

## Defects and gaps

| ID | Case | Live | Expected | Severity |
|---|---|---|---|---|
| F1 | iPhone SE (320×568) first screen | The 15 category tabs wrap to 156 px. The Value box is at y≈644 and the answer at y≈818, so **neither is on the first screen**. Pixel 7: answer at y≈669 of 839 | Value and answer above the fold on a 568 px phone (for example a category select on small screens, or a shorter header block) | P1 |
| F2 | Length list | No feet + inches compound (e.g. 5 ft 10 in ↔ 177.8 cm), the most common height query. Live-verified: the Length list is meter, kilometer, centimeter, millimeter, micrometer, nanometer, mile, yard, foot, inch, nautical mile | A "ft + in" input and output (converter-toolkit.com advertises a "feet+inches breakdown"; per WebSearch 14:04 EST) | P1 |
| F3 | U05: 1 nm → mile | 6.213712e-13 (7 significant digits) | The FAQ promises ten significant digits; scientific notation uses `toExponential(6)` | P2 |
| F4 | U43 −5 m, U44 −30 mpg | Converted (−16.40419948 ft; −7.84 L/100 km), no message | Negative length, weight and fuel economy are meaningless; warn (temperature and angle are fine) | P2 |
| F5 | /tool/unit-converter/cups-to-ml table | Row "0.33 cup = 78.07 ml" | Use ⅓ cup = 78.86 ml; bakers read 0.33 as ⅓ | P2 |
| F6 | Pair meta description, celsius-to-fahrenheit | "1 celsius = 33.8 fahrenheit" | Use a meaningful anchor (0 °C = 32 °F, 100 °C = 212 °F) | P2 |
| F7 | Result region | `sr-only` result text exists but there is no `aria-live`/`role=status`, so screen readers aren't told the answer changed | Add `aria-live="polite"` | P2 |
| F8 | Units | No torr, inHg (weather), troy ounce, carat, light-year, Mach, therm, month; only 9 cooking ingredients | Add the common ones | P2 |

## What works well

- Instant result, a swap button, and an "equals" list showing every unit at once.
- Keyboard: Radix tabs (Arrow, Enter) and selects (Enter, Arrow, Enter) work; the tab order is From → Value → Swap → To.
- Typing letters is blocked (number input); "1e5" works.
- Empty value shows "—" and hides the actions.
- de-DE formats numbers as "3.135,63" in the result, the list and the saved .txt.

## Trial gate and exports (`json/gate.json`, 13:58–13:59 EST)

- **Starting counts (display-only):** the probe context (13:57:39 EST) loaded at usageToday 0 (10 remaining) and stayed at 0 after reading results and pair pages. The six gate contexts (13:58) and the kbd context (14:01) loaded at 10 of 10 used.
- **At 0 remaining, all exports still work with no cap dialog.** Copy result copies "1 meter = 0.001 kilometer" plus the full list; Save as text downloads `unit-converter-result.txt` (ending "Calculated with FreeDailyPro.com"); Print opens the print dialog. No trial strip shows on the page.
- This matches /terms ("simple converters take no trial use at all"), /faq and the homepage ("none needed for text, calculator and converter tools"). **No wording defect on this tool.** Not observed: whether an export with uses left changes the display counter. Because nothing is blocked at 0, users are unaffected, so no RERUN row was added.
- The blog says "Browser tools list 10 trial usages a day—convert the full SKU set in one sitting", which suggests a limit this tool doesn't have (P2 wording).
