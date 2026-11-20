Sent: 2026-11-20 08:40 ET

# Priorities: unit-converter

No P0. Conversions are exact in all 55 cases. Repro steps are in REPRODUCE.md (R-ids).

## P1

1. **Small phones can't see the converter on the first screen (R1).** On iPhone SE the 15 category tabs wrap to 156 px, so the Value box (y≈644) and the answer (y≈818) are both below the 568 px fold. This is the highest-impression tool in its group (test plan: 4,782 impressions, 0 clicks; not GSC). On narrow screens, use a category select or a single scrollable tab row and keep Value + answer in the first viewport.
2. **No feet + inches (R2).** Height (5 ft 10 in ↔ 177.8 cm) is the most common everyday length query. There is no compound unit; competitors offer a feet+inches breakdown. Add "ft + in" to Length (input two boxes; output "5 ft 10.08 in"), and a pair page /tool/unit-converter/cm-to-feet-and-inches.

## P2

- **Precision:** tiny or huge values show 7 significant digits (`toExponential(6)`), while the FAQ promises ten (R3).
- **Validation:** negative length, weight, area, volume and fuel economy convert silently (R4).
- **Pair pages:**
  - cups-to-ml table uses 0.33 instead of ⅓ (R5).
  - The celsius-to-fahrenheit meta says "1 celsius = 33.8 fahrenheit" (R6).
  - All 20 pages repeat the same 13 FAQs and the same VideoObject.
  - Add high-demand pairs: cm↔feet, ml↔oz, cups↔grams, tbsp/tsp, kelvin.
- **Accessibility:**
  - Add aria-live to the result (R7).
  - Fix the Radix tab `aria-controls` (axe critical, shared with other tools).
- **Locales:** 8 hreflang alternates serve English with a non-English `lang`. Translate them or drop them from hreflang. The es title says "gratis".
- **Video (R8):**
  - It shows the old 4-tab UI, the old breadcrumb and an 11-category description.
  - It uses "free" wording.
  - Re-record it.
- **Blog (R9):** the "10 trial usages a day" line contradicts the tool and /terms. Converters take no trial use.
- **Units:** torr, inHg, troy ounce, carat, Mach, therm, light-year; more cooking ingredients.

## Not a defect

- Exports work at 0 remaining. This matches /terms, /faq and the homepage.
- Ads: keep them in reserved slots below the tool; never between the inputs and the answer.
