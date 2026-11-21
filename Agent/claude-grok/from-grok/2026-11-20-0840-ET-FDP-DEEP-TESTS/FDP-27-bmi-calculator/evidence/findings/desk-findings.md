Sent: 2026-11-20 23:05 ET

# FDP-27 BMI Calculator: desk findings (copy, SEO, code, blog, competitors)

Sources: `tool.html` and `curl/*.html` (2026-11-20 ~22:47 EST), `tool-expanded.txt` (expanded About / How to use / FAQ / Details / Guides), the JS chunks in `evidence/js/` (BmiCalculator, BmiExtras, MeasureField, numberInput, useLogToolUsage, csv, history, CalcHistory), `curl/blog.txt`, and a WebSearch for competitors. GSC data is not available. Traffic hint from TEST-ORDER.md (test-plan rank 22: "54+52 views; 504 impr bmi"); not verified.

## Code facts (read, not executed)
- BMI = kg / (cm/100)²; **category and WHO class use the value rounded to 1 decimal** (`N()`), so 24.95–24.99 shows Overweight and 18.45–18.49 shows Normal.
- Cut-offs: standard 18.5 / 25 / 30; Asian 18.5 / 23 / 27.5. Healthy-range top: 24.9, or 22.9 with Asian.
- **Target weight block:** defaults to BMI 24.9 and **ignores the Asian option** (`ye(kg, cm, target)`). The sentence is built as "which is " + "lose"/"gain" + amount.
- Age: blank → adult; < 2 → infant note; 2–19 → child note (category hidden, extras hidden); invalid → alert, extras hidden, category still shown.
- Sex: only shows "Sex does not change adult BMI categories; it is only used for child percentile charts". No percentile chart exists in the code.
- Inputs mirrored into the URL with `history.replaceState` (`?kg=&cm=&u=imperial`, defaults omitted). Age, waist and Asian are not mirrored.
- Usage hook: `useLogToolUsage` gates copy, CSV and print through `tryUse()` only when the tool is `known`. Live, nothing is gated (see live findings), which fits the site's `absorbable` tag for this tool.
- CSV: BOM, CRLF, formula guard (`'=`); the content is only the WHO table.
- Validation ranges: weight 30–300 kg (66–661 lb), height 100–250 cm (39–98 in), waist 10–250 cm, target BMI 10–60.

## Copy and FAQ accuracy (check 11)
| Text | Issue |
|---|---|
| FAQ "What are the category cut-offs?": "…the tool applies them to every entry." | False: under 20 the category is hidden, and the Asian option moves the cut-offs (P2) |
| Details › Limitations: "The tool does not adjust for age, sex, ethnicity or muscle mass… fixed cut-offs at 18.5, 25 and 30." | Contradicted by the Asian option and the under-20 handling (P2) |
| Details › Privacy: "not stored, tied to an account or sent anywhere"; FAQ: "never stored or uploaded" | Values travel in the URL to the server, GA and AdSense (P0, live) |
| Header badge "Files never stored" | A calculator with no files (P2 wording) |
| Child note: "use the CDC child BMI percentile tool" | No link (P2) |
| "Sex … is only used for child percentile charts" | There are no child percentile charts (P2) |
| Target sentence "which is gain 2.0 kg" | Grammar; it also nudges normal-weight users to gain (P1, with the Asian conflict) |
| FAQ healthy range "18.5 and 24.9 … (22.9 … Asian)" | Matches the card. PASS |
| FAQ formula and constants (2.54 cm/in, 0.45359237 kg/lb) | Matches code and live (I01). PASS |
| FAQ WHO obesity classes, waist-to-height 0.5 guideline | PASS |

## SEO (check 8) and indexing (check 7)
- Title "BMI Calculator – Kg, Lb & Healthy Weight | FreeDailyPro" (55 chars); meta description 154 chars and specific; H1 "BMI Calculator — Body Mass Index and Healthy Weight Range"; canonical self; 10 hreflang + x-default; OG/Twitter use the generic `og-default.png`.
- JSON-LD: WebSite, SoftwareApplication (Offer **price 4.99 USD**, for a tool that never takes a trial use: inconsistent), VideoObject (name "How to Calculate BMI & Daily Calories Online", which differs from the YouTube title and mentions calories), FAQPage (14 Q, matching the visible FAQ), BreadcrumbList (Home › Health Calculators › BMI Calculator).
- Heading levels: the result's h3 "WHO adult BMI classes" comes before any h2 (axe heading-order).
- 200 for Googlebot UA; robots.txt allows `/tool/`; the tool and `/blog/bmi-calculator` are in sitemap.xml. `cache-control: no-cache`. No `noindex`. GSC data is not available.
- Locales: **only `es` is translated** (title "Calculadora de IMC **gratis**: peso saludable y categoría", H1, breadcrumb). pt, fr, de, ja, hi, zh, ko and id serve the English title and description, and the H1 shrinks to "BMI Calculator", each with a self-canonical. The tool UI is English in every locale, es included. `/ar/tool/bmi-calculator` returns 404 (not in hreflang).
- Keyword fit: strong for "bmi calculator", "bmi calculator kg", "healthy weight range". Missing "stone" (UK), "bmi chart", "bmi for women/men", "child bmi".
- Video thumbnail `<img>` has no alt.

## Blog (check 9): /blog/bmi-calculator, "Read Your BMI Without Being Misled by One Number" (Oct 24, 2026)
- Worked examples are correct: 70/170 → 24.2; 180 lb 5'10" → 25.8; range 129–174 lb; 185 cm/95 kg → 27.8; Asian 160 cm → 58.9 / 70.4 kg.
- **Wrong or outdated:**
  - "copying, saving or printing uses one trial use per visit": live, nothing is counted.
  - "pounds typed into the kilogram box gives a BMI over 60 that the tool will reject or flag": 154 typed as kg at 170 cm is accepted as 53.3 Obese class III, with no flag.
  - The closing question asks whether to add "a waist-to-height check, or age-specific guidance?": both already exist.
  - It never mentions the Asian option, BMI Prime, the target weight, or exports.
  - It embeds the outdated video.
- Says "The tool classifies on the rounded figure it shows… 53.4 kg… counts as normal, matching the start of the range shown beside it". The range beside it starts at 53.5 kg, so the sentence is self-contradictory.

## Competitors (check 2)
- **NHS** adult calculator: asks ethnicity (Asian, Black African, African-Caribbean, Middle Eastern → 23 / 27.5), then waist advice; separate child calculator with age- and sex-adjusted centiles (2–17); shows stone/lb.
- **CDC**: adult calculator plus a child and teen percentile calculator.
- **calculator.net**: BMI table, BMI Prime, Ponderal Index, child percentiles.
- **Calculate.Studio**: WHO 8-class table, NHS ethnicity thresholds, healthy range.
- FreeDailyPro already matches or beats most on: WHO 8 classes, Prime, Ponderal Index, Asian cut-offs, waist-to-height, target BMI/Prime, worked steps, comma decimals, URL share.
- **Gaps:** child/teen percentile (the Sex field implies it); stones; an ethnicity option wider than "Asian" (NHS groups); a real result in the print/PDF; a dated summary in the exports.
