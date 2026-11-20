Sent: 2026-11-20 08:40 ET

# Test cases: unit-converter (UC-)

Run on https://www.freedailypro.com/tool/unit-converter, guest. URL form: `?c=<category>&from=<unit>&to=<unit>&v=<value>` (cooking adds `&ing=`). "Live" = 2026-11-19 13:57–14:02 EST. Scripted: `node scripts/uc-live.js` (U01–U48, K01–K07).

| ID | Input | Expected | Live (before fix) | Status |
|---|---|---|---|---|
| UC-01 | 1 inch → cm | 2.54 | 2.54 | PASS |
| UC-02 | 26.2 mile → km | 42.1648128 | Same | PASS |
| UC-03 | 1 UK gallon → US gallon | 1.200949926 | Same | PASS |
| UC-04 | 98.6 °F → °C; −40 °C → °F | 37; −40 | Same | PASS |
| UC-05 | −300 °C → K; −1 K → °F | Absolute-zero alert, no result | Alert shown | PASS |
| UC-06 | 1 kWh → BTU; 1 hp (mech) → kW | 3,412.141633; 0.7456998716 | Same | PASS |
| UC-07 | 30 mpg (US) → L/100 km; 0 L/100 km → km/L | 7.840486111; "—" | Same | PASS |
| UC-08 | 1 GiB → GB | 1.073741824 | Same | PASS |
| UC-09 | Cooking: ½ cup butter → g; 100 g sugar → cup | 113.5; 0.5 | Same | PASS |
| UC-10 | URL `?c=temperature&from=fahrenheit&to=celsius&v=98.6` | Loads 37 | 37 | PASS |
| UC-11 | Swap units (meter→km, value 1) | 1,000 (km→m) | Same | PASS |
| UC-12 | Keyboard: Arrow+Enter on tabs; Enter/Arrow/Enter on From select | Category and unit change | Works | PASS |
| UC-13 | de-DE browser, 1234.5 in → cm | 3.135,63 (locale format) in result, list and .txt | Same | PASS |
| UC-14 | At 0 remaining: Copy result / Save as text / Print | Works, no cap dialog (converters take no trial use, per /terms) | Works | PASS |
| UC-15 | iPhone SE 320×568: first screen | Value box and answer visible without scrolling | Value y≈644, answer y≈818 | FAIL (P1) |
| UC-16 | 5 ft 10 in → cm; 178 cm → ft + in | 177.8 cm; 5 ft 10.08 in | No compound unit | FAIL (P1) |
| UC-17 | 1 nanometer → mile | 6.213711922e-13 (10 significant digits, as the FAQ says) | 6.213712e-13 | FAIL (P2) |
| UC-18 | −5 m → ft; −30 mpg | Warning for impossible negatives | Converted silently | FAIL (P2) |
| UC-19 | /tool/unit-converter/cups-to-ml table | ⅓ cup = 78.86 ml | 0.33 = 78.07 | FAIL (P2) |
| UC-20 | Pair meta, celsius-to-fahrenheit | A useful anchor (0 °C = 32 °F) | "1 celsius = 33.8 fahrenheit" | FAIL (P2) |
| UC-21 | Screen reader: change the value | The new answer is announced (aria-live) | No live region | FAIL (P2) |
| UC-22 | axe on main (Length, Cooking) | 0 critical | aria-valid-attr-value on the tab trigger (aria-controls → missing panel) | FAIL (P2) |
| UC-23 | /pt/ … /id/ tool pages | Translated, or not listed in hreflang | English content with lang="pt" etc. | FAIL (P2) |
| UC-24 | Video i01IkvYUEVo | Current 15-category UI | 4 tabs, old breadcrumb | FAIL (P2) |
| UC-25 | Blog trial line | Matches the tool (no trial use for converters) | "10 trial usages a day" | FAIL (P2) |
| UC-26 | 1 atm → torr; 30 inHg → hPa | 760; 1015.9 | No torr / inHg | FAIL (P2) |
