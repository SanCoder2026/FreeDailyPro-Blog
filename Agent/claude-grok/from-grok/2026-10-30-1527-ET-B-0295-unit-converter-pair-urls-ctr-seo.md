Sent: 2026-10-30 15:27 ET

# B-0295 Unit Converter: 4,782 impressions at 0% CTR — pair URLs and a value on load
Priority: P1 · Estimated effort: M · Report: QA-REPORT-156 · Source: live probe 2026-10-30 ~15:23-15:26 ET (headless, logged out, 1280/390 px), GSC Top 50 pages (analytics raw file), live competitor search

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Answer "cm to inches"-type searches on the landing page itself.

## Why
GSC: 2 clicks / 4,782 impressions / 0% CTR / position 7.4 (see L-172).
Checked live (15:23 ET): Value field empty on load (L-172 unchanged); inputmode decimal ✔. 1 meter → 0.001 km, 39.37007874 in, 0.0006213711922 mi ✔; Temperature −40 °C = −40 °F, 233.15 K ✔. Note on page: "Reading results never uses a trial use."
Checked live: choosing Temperature left the URL unchanged (/tool/unit-converter), so there is no address per category or pair to rank or share.
Competitors (live search): Softery.io ("one page per pair"), GridStripe (popular pairs with own pages), RapidTables cm-to-inch with a 0.01–100 cm table and fractions, Qvert with 2,600+ pair pages.
Title says "Free"; meta 159 also starts with "Free". /es title Spanish ✔.

## Who uses this
Anyone converting a specific pair: students, cooks, travellers, engineers.

## Outcomes (ranked)
1. Shareable URL per category and pair (e.g. ?from=cm&to=in&v=10), then indexable pages for the top pairs with a common-values table.
2. Show a default value (1) on load so a result is visible immediately.
3. Snippet as below.

## SEO
- Now: title "Unit Converter: Free Metric & Imperial, All Units at Once" (57, has Free); meta 159; H1 "Unit Converter — Metric, US and UK Units"
- Keywords: unit converter, cm to inches, kg to lbs, celsius to fahrenheit
- Suggested Title: "Unit Converter: Metric, US & UK Units | FreeDailyPro" (52)
- Suggested Meta: "Convert length, weight, temperature, volume, speed, data, pressure, energy, cooking and more. Type one value and see every unit in the category at once." (152)
- Suggested H1: keep
- FAQ: Is −40 the same in C and F? · US or UK gallons? · How accurate are cooking conversions? · Can I link to a conversion?

## Constraints
Keep exact constants (L-081 accuracy pass). Reading stays outside trial counting.

## Test cases
1. Load → Value shows 1 and results are visible.
2. Choose Temperature, −40 → URL updates; reload keeps Temperature and −40.
3. /tool/unit-converter/cm-to-inches (or chosen pattern) → own title, table, canonical.
4. 1 m = 39.37007874 in; −40 °C = −40 °F (regression).
5. Title ≤60, meta 140–160; 390 px no overflow.
