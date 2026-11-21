Sent: 2026-11-20 23:05 ET

# FDP-27: reproduce

Guest, fresh profile, https://www.freedailypro.com/tool/bmi-calculator. No sign-in needed anywhere.

1. **Privacy (P0):** Open DevTools › Network and filter "kg%3D". Type weight 87.3 and height 179.5 and scroll: the address bar shows `?kg=87.3&cm=179.5`, and an `analytics.google.com/g/collect` request carries it. Reload: the document request, `googleads.g.doubleclick.net/pagead/ads` (several) and `pagead2.googlesyndication.com/pagead/ping` all carry it. Compare with Details › Privacy ("not … sent anywhere"). Automated: `node scripts/bmi-privacy.js`.
2. **No trial use (policy):** Note `localStorage['fdp-usage-v1'].usageToday`. Click Download CSV, Copy result, Print or save as PDF, the card's Copy result, Save as text and Print: the count doesn't change, and at 0 remaining no cap dialog appears. Automated: `node scripts/bmi-gate.js`.
3. **Target advice (P1):** Default 70 kg / 170 cm → "A BMI of 24.9 at your height is 72.0 kg, which is gain 2.0 kg." Tick "Use Asian BMI cut-offs": the card says "Overweight (Asian cut-offs)… lose about 3.8 kg" and the target line still says "gain 2.0 kg". With 80 kg + Asian: "lose about 13.8 kg" vs "lose 8.0 kg".
4. **Print (P1):** 82 kg / 178 cm → Print or save as PDF (or Print) → the preview has no BMI value, category, inputs, range or date. Automated: `node scripts/bmi-misc.js` writes `print-preview.pdf`.
5. **Video (P1):** Play the embedded video (or youtu.be/SogofBA7ENk) at 0:50: "BMI & Calorie Calculator", height 17 → BMI 3114.2.
6. **Rounding:** 72.2 kg / 170 cm → 25.0 Overweight (exact 24.98). 53.4 kg → 18.5 Normal while the range shown starts at 53.5 kg.
7. **Sex field:** choose Female (adult) → "only used for child percentile charts"; there is no chart. Age 15 → category hidden; the CDC tool is named, not linked.
8. **CSV:** Download CSV → `bmi-who-classes.csv` has only the WHO table plus "yes".
9. **Blog:** /blog/bmi-calculator, "A short routine…" step 5 ("uses one trial use per visit"); "Common mistakes…" ("the tool will reject or flag"). Type 154 in the kg box: 53.3 Obese class III, no flag.
10. **Locales:** /de/tool/bmi-calculator → English title, H1 "BMI Calculator", English UI; /es title "…gratis…"; /ar/tool/bmi-calculator → 404.

Automated set: `cd scripts && npm i playwright axe-core`; run with `env -u BROWSER node <script>` (on our box `BROWSER` points at a Chrome binary). WebKit needs `GIO_EXTRA_MODULES` (see README).
