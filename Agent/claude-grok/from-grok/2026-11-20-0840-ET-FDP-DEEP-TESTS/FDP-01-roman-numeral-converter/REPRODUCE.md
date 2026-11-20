Sent: 2026-11-20 08:40 ET

# FDP-01 Roman Numeral Converter: reproduction steps

- **Written:** 2026-11-19 09:46:50 EST (box `date`, ET).
- **Setup for all repros:** a guest or fresh profile. Never sign in, never enter a card, and never click ads.
- **Scripts:** in `scripts/`. Run them from `/workspace/deep/tools-env`, or anywhere with `npm i playwright axe-core`.

**R-01: no trial meter and no counting (FAIL, HIGH).**
1. Open the tool in a fresh profile.
2. In DevTools, run `localStorage.getItem('fdp-usage-v1')`. It returns `usageToday:0, limit:10, tier:"professional"`.
3. Search the page for "remaining today". There is no match.
4. Type 1994, then click Copy Roman numeral. The toast "Copied!" appears and `usageToday` stays 0.
5. Click Download CSV (`roman-numerals-1-100.csv`). It stays 0.
6. Click Print or save as PDF, then cancel. It stays 0.
7. Reload. It stays 0, and there is still no strip.
8. Repeat in a second fresh profile: same result.
- **Script:** `node scripts/edge-usage.js` (see `usage[]` in the JSON).

**R-02: US-order date entry (FAIL, MEDIUM-HIGH).**
1. Select "Month.Day.Year (US)". The heading becomes "Date → Roman numerals (month, day, year)".
2. Type 11 in the first box and 19 in the second, with year 2026. The result is "—" with "Month must be between 1 and 12."
3. Type 7, 4, 1776. The result is IV.VII.MDCCLXXVI, which contradicts the FAQ's "7.4.1776 becomes VII.IV.MDCCLXXVI".
- **Script:** `node scripts/edge-date-vinculum-probe.js`.
- **Screenshot:** `evidence/screens/edge/us-order-11-19-error.png`.

**R-03: hreflang targets untranslated (FAIL, HIGH).**
1. Run `curl -s https://www.freedailypro.com/de/tool/roman-numeral-converter | grep -o '<title>[^<]*'`. The title is "Roman Numeral Converter – Years & Dates (2026 = MMXXVI)".
2. Repeat for pt, fr, ja, hi, zh, ko and id: same English title and meta, and the H1 is "Roman Numeral Converter".
3. Open `/es/…`. The title, meta, H1 and FAQ are Spanish, but the labels "Copy table", "Separator" and "Day.Month.Year" and the H2s are English.
- **Script:** `node scripts/run-matrix.js scripts/config.json --only=locales`.

**R-04: stale blog (FAIL, HIGH).**
1. Open https://www.freedailypro.com/blog/roman-numeral-converter (200).
2. Find the text "Type 4000 and it says numerals here go from 1 to 3999" and "Where this tool stops… does not produce the overline notation".
3. On the tool, type 4000. The result is I̅V̅.

**R-05: video out of date (FAIL, MEDIUM-HIGH).**
1. Watch https://www.youtube.com/watch?v=Jrmgcqn_jJw (72 s).
2. It shows only basic conversion, with the on-screen text "Standard Roman numerals support values from 1 to 3999", "10 free uses daily" and "200+ Free Productivity Tools".
3. The YouTube title is "How to Use Roman Numeral Converter – Free Step-by-Step Walkthrough". The JSON-LD name is "How to Convert Numbers to Roman Numerals Online".

**R-06: 320px header overflow (FAIL, MEDIUM).**
1. Use Playwright `devices['iPhone SE']` (WebKit), or Chrome DevTools at 320×568.
2. Run `document.documentElement.scrollWidth`. It returns 329. The right-most header icon is clipped.
3. With `devices['Galaxy S9+']`, innerWidth becomes 329.
- **Screenshot:** `evidence/screens/devices/iphone-se-fold.png`.

**R-07: tablet tap targets (FAIL, MEDIUM).**
1. Use `devices['iPad Mini']`.
2. Measure `button[aria-label="Copy Roman numeral"]`: 28×28. Measure `button[aria-label="Add to favorites"]`: 16×16. Measure the "Clear" button: 30×16 on every device.

**R-08: iPad input font (FAIL, MEDIUM; confirm on a real iPad).**
1. Use `devices['iPad Mini']`.
2. Run `getComputedStyle(document.querySelector('input[aria-label=Number]')).fontSize`. It returns "14px". iOS zooms on focus below 16px.

**R-09: 4 July sentence (FAIL, MEDIUM).**
1. On the tool page, find the H2 "Dates in Roman numerals (wedding, tattoo)".
2. It says "4 July 1776 is VII.IV.MDCCLXXVI", which is US order with no label. In day.month.year it is IV.VII.MDCCLXXVI.

**R-10: Copy table payload (FAIL, LOW).**
1. Click Copy table on "1 to 100", then paste.
2. The text starts "Roman numerals, 1 to 100 / Working for 2,026 / 1. thousands: 2,000 …" before `Number\tRoman numeral`.
- **Script:** `node scripts/edge-copy-table-probe.js`.

**R-11: share loses the value (PARTIAL, LOW).**
1. Type 1994, then click the in-page "Share this tool".
2. The clipboard holds `https://www.freedailypro.com/tool/roman-numeral-converter`, with no value.

**R-12: date order is not locale-aware (PARTIAL, MEDIUM).**
1. Open the English URL with Playwright `locale:'en-US'`, then `'ja-JP'`, then open `/ja/…`.
2. In every case "Day.Month.Year" is checked, and there is no Y.M.D option.

**R-13: number grouping (LOW).**
1. Open `/de/tool/roman-numeral-converter`.
2. The placeholder reads "Enter a number (1 to 3,999,999)", with English grouping.

**R-14: iPhone SE fold (LOW).**
- In `evidence/screens/devices/iphone-se-fold.png` the result box starts at y=565 of 568.

**R-15: Feedback FAB covers chart cells (LOW).**
- See `evidence/screens/devices/ipad-mini-fold.png`, bottom-right.

**R-16: WebKit select and radio (LOW; verify on real Safari).**
- See `evidence/screens/devices/desktop-1440x900-webkit-fold.png`. The Separator select is white with faint text, and the unchecked radio looks filled.

**R-17: axe (LOW).**
- Run `node scripts/run-matrix.js scripts/config.json --only=a11y`. Desktop shows `label-content-name-mismatch` (serious, 1, `.sm:flex` header control) and `region` (moderate, 1).

**R-18: AdSense `no_div` (LOW).**
- Open DevTools on Pixel 7 emulation. The console shows "Error: no_div at …adsbygoogle.js".
