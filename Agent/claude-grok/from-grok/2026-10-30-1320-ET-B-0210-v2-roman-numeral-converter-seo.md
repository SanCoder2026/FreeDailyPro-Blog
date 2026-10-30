Sent: 2026-10-30 13:20 ET

Supersedes 2026-10-30-1319-ET-B-0210-roman-numeral-converter-seo.md (the stray note in the first suggested title is removed; nothing else changed).

# B-0210-v2 Roman Numeral Converter: win clicks for "roman numeral converter" (48,950 impressions, 0.1% CTR)
Priority: P1 · Estimated effort: S · Report: #128 (SEO backfill) · Source: curl server HTML 2026-10-30 ~13:19 ET + GSC (analytics/2026-07-10-to-now-raw.md) + live Google top-5 (WebSearch)

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

SEO follow-up to B-0036 / L-013 (still open). Only the SEO part is here.
## Intent
We already rank on page 1 for the site's biggest query. The snippet and the page should make searchers pick us over timeanddate and the newer tools.
## Why
- GSC: "roman numeral converter" 57 clicks / 48,950 impressions / 0.1% CTR / position 9.0.
- "roman numerals converter" 1/23, position 11.2.
- Page: 50 clicks / 38,580 impressions, position 9.5.
- /es page: 11 / 9,585, position 8.2.
- At position 9 a 0.1% CTR is very low. The snippet is the lever.
## Who uses this
Students, people planning a tattoo or wedding date, film/clock readers, puzzle solvers.
## SEO
**Now** All checks pass except where listed: HTTP 200, 0 redirects; in sitemap; no robots noindex; self canonical; 11 hreflang; valid JSON-LD (SoftwareApplication, FAQPage, BreadcrumbList, VideoObject); full OG/Twitter set. Generic og-default.png, template/footer H2s, boilerplate meta, empty video alt → **B-0209** (not repeated).
- Title "Roman Numeral Converter: Numbers, Dates & Years Free" (52). The trailing "Free" is weak; there's no example and no brand.
- Meta is 130 chars (under 140), starts with "Free", and is generic.
- H1 "Roman Numeral Converter — Numbers, Years and Dates" (good).
- Locale /es is translated (title, H1, meta in Spanish) ✓. So this page does **not** show B-0123.

**What the top results do** (Google 13:19 ET: listenany, calcendium, timeanddate, pithlab, calculatorem):
- They show the answer in the snippet ("2026 is MMXXVI", "1994 = MCMXCIV").
- They give a step-by-step breakdown of each place (M + CM + XC + IV).
- They explain why IIII or IC is wrong and give the correct form.
- They offer vinculum up to 3,999,999 (L-012), lowercase/Unicode output (Ⅻ), and batch lists.
- They have a rules H2 (seven symbols, six subtractive pairs).
- Their FAQs: "How do I write 4 in Roman numerals?", "What is the largest Roman numeral?", "Why is there no zero?"

**Keyword gaps:** "2026 in roman numerals", "what year is MCMXCIV", "roman numerals chart", "roman numerals for tattoo/dates", "1 to 100 roman numerals".

**Suggested**
- Title: `Roman Numeral Converter – Numbers, Years & Dates (2026 = MMXXVI)` (59)
- Meta: `Convert numbers, years and dates to Roman numerals and back as you type. See each step (1994 = M + CM + XC + IV), why IIII is wrong, and a 1–100 chart.` (151)
- H1: keep `Roman Numeral Converter — Numbers, Years and Dates`
- H2s:
  - "How to convert a number to Roman numerals"
  - "Roman numerals chart 1–100 and key years"
  - "Why IIII and IC are wrong"
  - "Dates in Roman numerals (wedding, tattoo)"
- FAQ:
  - "How do you write 2026 in Roman numerals?" → "MMXXVI: MM (2000) + XX (20) + VI (6)."
  - "How do you write 4 in Roman numerals?" → "IV. IIII is only seen on some clock faces."
  - "What is the largest Roman numeral?" → "3,999 (MMMCMXCIX) in standard form; a bar over a letter multiplies it by 1,000."
  - "Is there a Roman numeral for zero?" → "No. The Romans had no symbol for zero."
## Outcomes (ranked)
1. A new title and meta that show a worked example, so the snippet answers at a glance.
2. Question H2s plus a chart (an HTML table, not an image).
3. A step-by-step breakdown under the result, and a "why invalid" message (also fixes the content side of B-0036).
4. FAQPage JSON-LD that matches the visible FAQ above.
5. The same for /es (translated).
## Constraints
Keep the URL and H1. Titles under 60. No invented claims.
## Test cases
1. curl the title (59 or fewer chars, contains "Roman Numeral Converter" first).
2. Meta 140–160 chars, includes an example.
3. 4 or more question H2s inside `<main>`; the FAQPage questions equal the visible FAQ.
4. GSC check in 28 days: CTR on "roman numeral converter" above 0.1% (the owner reads this).
