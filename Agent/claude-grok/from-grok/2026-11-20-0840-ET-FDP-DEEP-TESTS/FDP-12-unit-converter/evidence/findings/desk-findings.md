Sent: 2026-11-20 08:40 ET

# Desk findings: unit-converter

- **Run:** 2026-11-19 13:56–14:04 EST (box `date`, ET). curl, JS bundles (UnitConverter, the ToolPage unit tables, useLogToolUsage), WebSearch.
- **GSC data is not available.** TEST-ORDER.md quotes the test plan: "4,782 impr pos 7.4 0 clicks". That is the only search figure here, and it is not re-verified.

## Page and SEO (`html/tool.html`)

| Item | Live | Note |
|---|---|---|
| HTTP / canonical | 200, self-canonical | PASS |
| Title | "Unit Converter: cm to inches, kg to lbs, °C to °F & More" (57 chars) | Good keyword fit; no brand suffix |
| Meta / OG | "Unit converter: cm to inches, kg to lbs, miles to km, °C to °F, cups to ml and more. See every unit in the category at once, in metric, US and UK." | Good. OG image is the generic `og-default.png` |
| H1 | "Unit Converter — Metric, US and UK Units" | PASS |
| JSON-LD | SoftwareApplication, Offer 4.99 (no period), FAQPage with 13 Q&As, VideoObject, BreadcrumbList | The FAQ matches behaviour (checked against live). Offer on an ungated tool is odd but harmless |
| hreflang | en, es, pt, fr, de, ja, hi, zh, ko, id, x-default | **Only es is translated.** pt/fr/de/ja/hi/zh/ko/id serve English content with `<html lang="pt">` etc., so the declared language is wrong. The es title says "gratis". /ar → 404 (not in hreflang) |
| Pair pages | 20 pages under /tool/unit-converter/<pair> (cm-to-inches … acres-to-hectares), all in the sitemap, self-canonical, SSR result, formula and a common-values table | Good long-tail base. They repeat the same 13 generic FAQs and the same VideoObject. Only en (es pair → 404). Missing high-demand pairs: cm-to-feet / feet-to-cm (height), ml-to-oz / oz-to-ml, tbsp/tsp, cups-to-grams, kelvin, mm-to-cm, ft-in to cm |
| Category card | /category/converters says "Convert length, weight, temperature, and more" | Same as the old video subtitle; fine |
| Brand query | WebSearch "freedailypro unit converter": Glama MCP listings, the category page and the homepage; the tool page is not in the top 5 | Index sample only |

## Competitors (WebSearch 14:03 EST)

numerly.io, digitalunitconverter.com, converter-toolkit.com, asknumbers.com, aiocalc.com, and Google's own unit widget on the results page.
- **Common strengths:** many value-specific pages ("70 kg to lbs"), a feet+inches breakdown (converter-toolkit), shareable links per value (aiocalc), printable charts, everyday reference points.
- **FreeDailyPro's edges:** 15 categories incl. cooking by ingredient, fuel economy and data (kB vs KiB); an all-units list; exact factors; a URL state; locale number formatting; export to .txt/print.
- **Gaps:** ft+in, torr/inHg, troy oz, carat, value-specific pages, more cooking ingredients.
- **SERP:** the "unit converter" head term is largely answered by Google's widget, so a 0-click at pos 7.4 is plausible. The pair pages (long-tail) are the realistic traffic lever.

## Blog (`html/blog.html`, /blog/unit-converter, Oct 17, 2026)

- B2B spec-sheet angle. Figures are right: 80 mm ≈ 3.15 in, 1.25 kg ≈ 2.76 lb, 300 mm ≈ 11.81 in.
- **Wording:** "Browser tools list 10 trial usages a day—convert the full SKU set in one sitting with values prepared." This suggests a cap that this tool doesn't apply (live: exports work at 0 remaining, no trial strip) (P2).
- The blog doesn't mention the all-units list, cooking or the pair pages.

## Trial-use wording

/terms ("Text utilities, calculators and simple converters take no trial use at all"), /faq and the homepage ("none needed for text, calculator and converter tools") match this tool's behaviour. Nothing to fix here, apart from the blog line.

## Cluster / duplicates

There is no cluster in TEST-ORDER. Related: currency-converter and timezone-converter (different jobs), and the cooking tab vs any recipe tools. There is no duplicate page. The 20 pair pages are intentional landing pages with their own canonicals.
