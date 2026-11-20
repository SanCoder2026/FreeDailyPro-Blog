Sent: 2026-11-20 08:40 ET

# Desk findings: Roman Numeral Converter

- **Tool:** https://www.freedailypro.com/tool/roman-numeral-converter
- **Desk review time:** 2026-11-19 09:04:54 EST (America/New_York), from box `date`
- **Method:** read-only GETs (curl) of the live page, `/es` page, blog, robots.txt, sitemap.xml, Professional Tools, `/category/converters`, homepage, YouTube oEmbed/watch, and three competitor pages. WebSearch for indexing and the head query. Past briefs and the QA ledger were read, not re-run in a browser.
- **Not done here:** live typing, payments, sign-in, API/MCP calls, or watching the YouTube video. A separate browser tester covers live use.
- **Page last-modified (response header):** 2026-11-19 08:37:21 EST (the HTTP `Last-Modified` value was 2026-11-19 13:37:21 GMT).
- **Wording:** this is a Professional Tool (10 trial uses/day, $1 day pass, $4.99/month). This report does not say "free tools".

## Claimed capabilities (from live HTML and JS, for the browser tester)

The page and `RomanNumeralConverter-CIvGjpT-.js` claim all of the following. These are claims, not live-use results.

| Claim | Where it is stated |
|---|---|
| Number → Roman and Roman → number, in two separate boxes, as you type | Visible UI, "How to use it", FAQ |
| Standard range 1–3,999 in plain letters (MMMCMXCIX) | On-tool note, FAQ, About |
| Larger numbers 4,000–3,999,999 with a vinculum (bar). 4,000 is I and V with bars (I̅V̅). 5,000 is V with a bar. Copy uses Unicode combining overline U+0305. Input also accepts U+0304 and bracket groups such as `(V)` for 5,000 and `(XII)CCCXLV` for 12,345 | On-tool note, FAQ, About, JS `N=3999999`, function `U` |
| Date mode: day, month, year; Day.Month.Year or Month.Day.Year (US); separators dot, middle dot, slash, hyphen, space | Visible UI |
| Date years 1–3,999; real calendar days (month 1–12; 30 Feb rejected) | FAQ; JS `z()` / `C()`; errors "Year must be between 1 and 3999.", "Month must be between 1 and 12.", "That date does not exist in the calendar." |
| Default date is today. Fetched HTML showed **XIX.XI.MMXXVI**, which is 19 November 2026, matching the desk date | SSR HTML |
| Step-by-step working under the result (e.g. 2026 = MM + XX + VI) | Visible "How 2,026 is written" |
| Charts: 1–100 (in the SSR HTML) and Years 1950–2050 (tab in `RomanExtras`, JS `ye`) | Visible + JS |
| Copy Roman numeral / number / date; Copy table; Download CSV (`roman-numerals-1-100.csv` or `roman-numerals-years.csv`); Print or save as PDF | Buttons + `history-COOh5Nu8.js` |
| "Share this tool" (page/tool share, not a result file) | Guides section |
| "Recent calculations": session only, max 10, "Kept only while this page is open. Nothing is saved on our servers or in your browser." | `CalcHistory-CcxcUFj3.js` |
| "Files never stored" / "Runs on your device"; FAQ: nothing is uploaded | Visible + FAQ |
| Lowercase input is accepted (`trim` + `toUpperCase`). Output is uppercase. No lowercase-output toggle in the JS | JS `P()`; blog also says output is always uppercase |
| IIII / XIIII and other `IIII` forms are read with a clock-face note; standard output stays IV / XIV | JS + visible "Why IIII and IC are wrong" |
| Invalid forms get a reason and often a "Did you mean …?" hint (IIX → X (10), IC → XCIX (99), VX → V) | JS `te()` / `ae()` |
| Trial uses: Professional strip. Copy and table export go through the usage gate (`useLogToolUsage` wraps `clipboard.writeText`; table Copy/CSV/Print call `gate()` first). Typing alone writes only session history after 800 ms and should not, from the JS, spend a trial use. FAQ: "copying or downloading it uses one of your trial uses for the visit." | JS + FAQ |
| Checkout CTAs on the strip: "Ads-free unlimited usage, $1 day pass" and "Ads-free unlimited usage, $4.99 monthly pass", plus Quick Buy. Desktop vs mobile wording differs slightly. This desk review did not open checkout. | `UsageAndUpgradeStrip` + locale strings |

## Past findings and what looks fixed now

Sources: test-plan.csv rank 2; B-0036, B-0043, B-0114, B-0209, B-0210 and B-0210-v2; RETEST-LEDGER L-010–L-016, L-179.

**Look fixed in the live HTML/JS (2026-11-19 desk check):**

- **B-0210-v2 SEO copy.** Live title is `Roman Numeral Converter – Years & Dates (2026 = MMXXVI)` (55 characters once `&amp;` is decoded). Meta includes the 1994 worked example and is 158 characters. H1 is `Roman Numeral Converter — Numbers, Years and Dates`. The four content H2s from B-0210-v2 are all present. Visible FAQ has 11 questions and matches the FAQPage JSON-LD.
- **B-0114 / L-012 / L-179 capability.** Vinculum is implemented to 3,999,999. The JS writes 4,000 as I̅V̅ (I and V, each with U+0305), 5,000 as V̅, and 12,345 as X̅I̅I̅CCCXLV, which matches the FAQ. Step-by-step working and the 1–100 / 1950–2050 tables are present. Date separators include middle dot and slash.
- **L-010 invalid dates.** `z()` rejects 30 February and 31 April with "That date does not exist in the calendar."
- **L-011 US date order.** "Month.Day.Year (US)" is in the UI and in `C(..., "mdy")`.
- **L-014 /es.** `/es/tool/roman-numeral-converter` is HTTP 200, `html lang="es"`, self-canonical to the `/es/` URL, 11 hreflang tags (including en and x-default), and a Spanish title, meta and H1.
- **Core examples** from older notes (MMXXVI = 2026, MCMXCIV = 1994, 3,999 = MMMCMXCIX, clock-face IIII) are still correct in the copy and in the JS.
- The earlier "meta 130, no example" and "stops at 1–3999" issues are fixed on the **tool page**. The **blog** still describes the old 1–3999 limit (see check 9).

**Still open, stale, or new:**

- **Current Google Search Console figures are not available** in this review. Last recorded figures in test-plan.csv / B-0043 (cited, not refreshed): head query "roman numeral converter" 48,950 impressions, position 9.0, CTR 0.1%; `/es` 9,585 impressions. L-013's CTR target (above 0.1%, top 5) cannot be confirmed.
- **B-0209** still applies: generic `og-default.png`; the YouTube thumbnail `<img>` has an empty `alt`.
- **L-016** recorded "Free" in the title/meta as by-design. The live title and meta no longer contain "Free". That is consistent with later Professional Tools wording. Do not put "free tools" in visible copy.
- **Blog post is stale** (dated 17 October 2026, sitemap lastmod 2026-10-17). It still says 4,000 is rejected, there is no overline, and there are no alternative date layouts. The tool changed after that date (vinculum was verified in report #162 around 30 October 2026).
- **YouTube title and description** use "Free" and do not match the JSON-LD or sitemap video titles (checks 10 and 12).
- **Unlabelled US-order example** on the tool page: "4 July 1776 is VII.IV.MDCCLXXVI" is Month.Day.Year, but the sentence does not say so (check 6).
- **Sitemap.xml lists no locale URLs** (`/es/` count is 0). The `/es` tool page is only discoverable via hreflang (and was historically indexed).
- **B-0114 mobile horizontal scroll** on the date-order control was not rechecked (no browser).

---

## Check 6 — Information is correct and valid

**Result: PARTIAL. Severity: MEDIUM.**

Factual Roman-numeral rules on the tool page are correct:

- Letters I=1, V=5, X=10, L=50, C=100, D=500, M=1,000.
- Six subtractive pairs: IV, IX, XL, XC, CD, CM. Only I before V/X, X before L/C, C before D/M. V, L and D are never repeated or subtracted.
- 4 is IV, not IIII (clock-face exception is explained). 49 is XLIX, not IL. 99 is XCIX, not IC. 999 is CMXCIX, not IM.
- 1994 = M + CM + XC + IV = MCMXCIV. 2026 = MM + XX + VI = MMXXVI. 1887 = MDCCCLXXXVII. 1776 = MDCCLXXVI. 3,999 = MMMCMXCIX.
- The SSR 1–100 table was checked against the standard algorithm: 100/100 pairs match, none missing.
- Vinculum rule (bar × 1,000), the 3,999,999 cap, bracket input, and "no zero / no negatives / no decimals" are all consistent with the JS.
- Date examples XIV.VI.MMXXVI and VI.XIV.MMXXVI for 14 June 2026 are correct. Default XIX.XI.MMXXVI for 19 November 2026 is correct. Leap-year logic in `z()` is the Gregorian rule (29 Feb 2000 allowed, 29 Feb 1900 rejected).

**Defects:**

1. **Unlabelled date order (MEDIUM).** In "Dates in Roman numerals (wedding, tattoo)": "14 June 2026 is XIV.VI.MMXXVI (day.month.year), or VI.XIV.MMXXVI in US order; 4 July 1776 is VII.IV.MDCCLXXVI." VII.IV.MDCCLXXVI is **Month.Day.Year**. Day.Month.Year for 4 July 1776 is **IV.VII.MDCCLXXVI**. The FAQ is careful (it uses 7.4.1776 in US order). The H2 body is not. Fix: "4 July 1776 is IV.VII.MDCCLXXVI (day.month.year), or VII.IV.MDCCLXXVI in US order."
2. **Blog is factually out of date (MEDIUM, scored under check 9).** It tells readers that 4,000 errors with a 1–3999 limit, that there is no overline, and that date boxes accept 1–3999 in each field and have no alternative layouts. The live tool accepts 4,000 as I̅V̅, validates real calendar dates, and offers five separators plus US order.
3. **JSON-LD SoftwareApplication** description is only "Convert between numbers and Roman numerals" and its Offer is `"price": "4.99"` with no billing period. The price matches the $4.99 monthly pass, but as written it can look like a one-time price. The page also has a $1 day pass. Severity LOW, listed again under check 8.

All other checked examples and FAQ answers on the **tool page** matched the JS and standard rules.

---

## Check 7 — Indexing

**Result: PARTIAL. Severity: LOW (locale sitemap), otherwise PASS.**

Evidence:

- HTTP 200, no `robots` meta, no `X-Robots-Tag`. `robots.txt` is `User-agent: *` / `Allow: /` and does not disallow `/tool/`. It points at `https://www.freedailypro.com/sitemap.xml`.
- Canonical: `https://www.freedailypro.com/tool/roman-numeral-converter` (self).
- In sitemap.xml: yes, lastmod `2026-11-19`, weekly, priority 0.7, plus a `video:video` block for YouTube id `Jrmgcqn_jJw`. The blog URL is also in the sitemap (lastmod `2026-10-17`).
- Hreflang: 11 tags (`en`, `es`, `pt`, `fr`, `de`, `ja`, `hi`, `zh`, `ko`, `id`, `x-default`). The `/es` page returns the same set and canonicalises to itself.
- **Sitemap gap:** the 987 sitemap URLs include **no** `/es/` (or other locale) loc. Locale tool pages are not in `sitemap.xml`. `/es` has historically ranked (9,585 impressions in the last recorded GSC extract), so Google has found it, but the sitemap does not list it.
- **WebSearch, 2026-11-19:** `site:freedailypro.com roman numeral` returned the tool page first, titled "Roman Numeral Converter – Years & Dates (2026 = MMXXVI)", and the blog second. `roman numeral converter freedailypro` returned the blog first, then Professional Tools and the converters category; the tool URL was not in the first five results of that particular search. Indexing of the English tool URL is confirmed. **Current rank and impression counts are not available** (no GSC access this turn).

---

## Check 8 — SEO

**Result: PARTIAL. Severity: MEDIUM (snippet still fighting a historically weak CTR; leftover template issues). On-page structure is largely a PASS against B-0210-v2.**

Live tags (English tool page):

| Element | Live value | Length |
|---|---|---|
| Title | Roman Numeral Converter – Years & Dates (2026 = MMXXVI) | 55 |
| Meta description | Convert numbers, years and dates to Roman numerals and back as you type. See each step (1994 = M + CM + XC + IV), why IIII is not standard, and a 1–100 chart. | 158 |
| H1 | Roman Numeral Converter — Numbers, Years and Dates | 50 |
| Canonical / OG URL | https://www.freedailypro.com/tool/roman-numeral-converter | — |
| OG/Twitter | Full set (`og:type` website, `og:site_name` FreeDailyPro, title, description, url, image; Twitter `summary_large_image`) | — |
| OG/Twitter image | https://www.freedailypro.com/og-default.png (generic, B-0209 still open) | — |

H2s on the page: "Roman numerals chart 1–100 and key years"; "How to convert a number to Roman numerals"; "Why IIII and IC are wrong"; "Dates in Roman numerals (wedding, tattoo)"; "Watch: Roman Numeral Converter in Action"; "About Roman Numeral Converter"; "How to use it"; "Common questions"; "Guides and next steps"; plus footer headings.

JSON-LD (5 blocks, all parse as JSON): `WebSite`, `SoftwareApplication`, `VideoObject`, `FAQPage` (11 questions, same text as the visible FAQ), `BreadcrumbList` (Home → Unit, Date & Everyday Calculators → Roman Numeral Converter). Issues: VideoObject `name` is "How to Convert Numbers to Roman Numerals Online", which does not match the live YouTube title; SoftwareApplication Offer is $4.99 with no period; SoftwareApplication description omits dates and vinculum.

Images: YouTube thumbnail `alt` is empty (FAIL, LOW). Product Hunt badge has an alt.

Internal links: breadcrumb to `/category/converters`; "Guides and next steps" links the matching blog post and "Convert Binary and ASCII for Homework and Debug Checks". The blog also points at Case Converter and Word & Character Counter; those are not linked from the tool page. Number to Words would be a fair related Professional Tool.

Keyword fit: the title and H1 lead with "Roman Numeral Converter" and put a worked year in the snippet, which is what the top results do. The live meta still does not mention the 1–3,999,999 vinculum range, which RapidTables and Calculator Soup put in their descriptions.

**Top results for `roman numeral converter` (WebSearch, 2026-11-19; not a substitute for a live SERP rank):** timeanddate.com, quto.dev, thehandycalculators.com, rapidtables.com, alleasycalc.com. FreeDailyPro was not in those five, which is consistent with the last recorded position of 9. Comparison:

- timeanddate: title "Roman Numeral Converter" (23). Meta 145 chars, range 1–3999, dates. Shows "2026 is MMXXVI" in the body. No vinculum in the fetched copy.
- RapidTables: title "Roman Numeral Converter" (23). Meta 163 chars, range 1–3,999,999, steps and a table.
- Calculator Soup: title "Roman Numeral Converter" (23). Meta 137 chars, range 3,999,999.

FreeDailyPro's differentiators, if the snippet and page are believed: date mode with US/DMY and tattoo-style separators, as-you-type working, 1–100 and 1950–2050 charts, clock-face IIII handling, bracket/overline input, and a usage video. Those are stronger than a 23-character generic title. The historically 0.1% CTR at position 9 is the remaining problem; current CTR is not available.

**Suggested title (55, keep unless a CTR test is run):**
`Roman Numeral Converter – Years & Dates (2026 = MMXXVI)`

**Suggested meta (154 chars; adds the high range that competitors advertise, keeps the worked example):**
`Convert numbers, years and dates to Roman numerals as you type. See each step (1994 = M + CM + XC + IV). Range 1–3,999,999 with a bar, plus a 1–100 chart.`

**Suggested H1 (keep):**
`Roman Numeral Converter — Numbers, Years and Dates`

**Suggested FAQ / copy additions:**

- Fix the 4 July 1776 sentence as in check 6.
- Optional visible question: "Does the converter accept lowercase?" → "Yes. `mmxxvi` is read as 2026. The result is always uppercase."
- Optional H2 for a related query: "How to write a tattoo or wedding date in Roman numerals" is already covered by "Dates in Roman numerals (wedding, tattoo)". A year-specific H2 is not required if the title already answers 2026.
- Align VideoObject `name` (and the sitemap `video:title`) with the real YouTube title once that title is corrected (see checks 10 and 12).
- Give the YouTube thumbnail a real alt, and replace `og-default.png` with a tool-specific image that shows `2026 = MMXXVI`.
- On SoftwareApplication Offer, either add a monthly unit or drop the price rather than implying a one-time $4.99.

`/es` SEO is translated: title "Convertidor de números romanos: años y fechas, 2026 = MMXXVI" (60 chars), meta 148 chars mentioning 3999 and the bar, H1 "Convertidor de números romanos: números, años y fechas". That is in good shape.

---

## Check 9 — Blog post

**Result: FAIL. Severity: HIGH** (it teaches a smaller, older tool than the one that is live).

- URL https://www.freedailypro.com/blog/roman-numeral-converter is in the sitemap (lastmod 2026-10-17). HTTP 200. Canonical is self. Title: "Roman Numerals for Chapters, Copyright Years and Old Dates | FreeDailyPro". Meta 130 chars. It links to `/tool/roman-numeral-converter` more than once and embeds YouTube `Jrmgcqn_jJw`. Dated October 17, 2026.

Correct and still true: 1–14 chapter list; 49 = XLIX not IL; 2026 = MMXXVI; 1994 = MCMXCIV; MDCCCLXXXVII = 1887; date lines XXIV.X.MMXXVI and III.VII.MDCCCLXXXVII; lowercase `iv` = 4; IIX hint toward X (10); IC → XCIX; VX hint toward V; XIIII read as 14 with a clock-face note; no zero; output is uppercase.

**Stale or wrong against the live tool:**

- "Type 4000 and it says numerals here go from 1 to 3999" — the live JS converts 4,000 to I̅V̅ and explains the bar.
- "it accepts whole numbers from 1 to 3999 in each box" for dates — the live tool validates calendar months and days.
- "The tool does not offer alternative layouts" — the live tool offers five separators and US vs day-month-year order.
- "Where this tool stops: The converter handles whole numbers from 1 to 3999. It does not produce the overline notation" — directly false now.
- "Assuming years can go past 3999. They cannot here" is still true for **date years**, but it is no longer true for the number converter.

The post should be updated to the current range, vinculum input (`(V)`, combining overline), date validation, and separators, and it should keep linking to the tool. Until then, a reader who follows the blog will think 4,000 is impossible.

---

## Checks 10 and 12 — YouTube video

**Result: PARTIAL. Severity: MEDIUM.** The video exists and is embedded; the packaging does not match the tool or the video rules. **This desk review did not watch the video**, so on-screen capabilities are unverified.

Evidence:

- `VIDEOS.md` (blog handoff, written 2026-10-15) lists 60 tools that still need a video. `roman-numeral-converter` is not on that list. The mandate is: title "How to <do the task> with <Tool name> | FreeDailyPro"; description should include the tool link and "10 trial usages every day"; "No 'free', no '#1', no AI wording"; 60–150 seconds; embedding allowed.
- The tool page has a "Watch: Roman Numeral Converter in Action" section, a `VideoObject` for `https://www.youtube.com/watch?v=Jrmgcqn_jJw`, and a sitemap video entry. The blog embeds the same id.
- YouTube oEmbed and the watch page (fetched 2026-11-19): **title** "How to Use Roman Numeral Converter – Free Step-by-Step Walkthrough"; **channel** FreeDailyPro (`@FreeDailyPro`); **length** 72 seconds (inside 60–150); **published** 2026-09-22 21:43:17 PT, which is **2026-09-23 00:43:17 EST**; **viewCount** in the player response was **1**.
- Description (from `videoDetails.shortDescription`):

> Converts numbers to Roman numerals and Roman numerals back to regular numbers, in either direction.
>
> This video shows how to use Roman Numeral Converter step by step.
>
> Try Roman Numeral Converter free: https://www.freedailypro.com/tool/roman-numeral-converter?utm_source=youtube&utm_medium=description&utm_campaign=roman-numeral-converter-tutorial&utm_content=v2
>
> Free daily uses in your browser, no account needed.

- That description does not mention date mode, vinculum, or "10 trial usages every day". It says "free" twice, against `VIDEOS.md`.
- YouTube keywords on the watch payload are generic (`FreeDailyPro`, `free online tools`, `PDF tools`, …) and **do not include "roman numeral"**.
- Title mismatches: YouTube vs JSON-LD ("How to Convert Numbers to Roman Numerals Online") vs sitemap ("How to Convert Numbers to Roman Numerals Free Online").
- WebSearch for `@freedailypro roman numeral youtube` did not surface this video in the useful results (it has almost no views). A curl of the YouTube search results page was also inconclusive. Existence is confirmed from oEmbed and the watch page, not from search visibility.

Recommendations for Claude / the video bot (after someone watches the clip): retitle to the VIDEOS.md pattern, for example `How to convert numbers and dates to Roman numerals with Roman Numeral Converter | FreeDailyPro`; rewrite the description without "free", add "10 trial usages every day" and, if the pictures support it, date mode and the bar for numbers above 3,999; add roman-numeral keywords; sync JSON-LD and sitemap titles to the live YouTube title. If the 72-second clip still only shows the old 1–3999 tool, it needs a reshoot — that can only be decided by watching it.

---

## Check 11 — FAQ and usage guide

**Result: PARTIAL. Severity: LOW on the tool page (the 4 July issue is in the guide H2, not the FAQ); HIGH if the blog "usage guide" is counted, see check 9.**

The on-page "How to use it", About, and 11 FAQ answers match the JS:

- Both directions, boxes independent, date boxes, separators, year 1–3,999 for dates.
- Range 1–3,999,999 with a bar; how to type `(V)` / `(XII)CCCXLV`.
- Working + 1–100 and 1950–2050 tables; "copying or downloading it uses one of your trial uses for the visit."
- Letter values; 2026 = MMXXVI; 4 = IV with a clock-face note for IIII; no zero; nothing uploaded.

The usage guide H2 "Dates in Roman numerals (wedding, tattoo)" has the unlabelled 4 July US-order example (check 6). Otherwise the on-page guide is accurate. The blog "Steps in order" / "What the error messages are telling you" / "Where this tool stops" sections are not accurate anymore.

---

## Checks 17 and 18 — Categorization and location

**Result: PASS. Severity: n/a.**

- Breadcrumb and BreadcrumbList: Home → **Unit, Date & Everyday Calculators** (`/category/converters`) → Roman Numeral Converter.
- `/category/converters` (H1 "Unit, Date & Everyday Calculators") lists "Roman Numeral Converter" as its own card, beside Percentage Calculator and other calculators.
- `/professional-tools` (title "Professional Tools | FreeDailyPro") lists it under "Unit, Date & Everyday Calculators" with Unit Converter, Currency Converter, Time Zone Converter, Tip Calculator, Business Days Calculator, Online Timer, Age & Date Calculator, Percentage Calculator, Random Number Generator, and Discount Calculator.
- The homepage lists it in the same All Tools / category footer group.

This is the right section: it is a number-and-date converter, not a Premium app and not AI Studio. It is a **Professional Tool**: 10 trial uses/day, $1 day pass, $4.99/month, as shown in the English usage-strip strings (`Trial: {limit} uses/day` · `{count} remaining today`; "Ads-free unlimited usage, $1 day pass"; "Ads-free unlimited usage, $4.99 monthly pass").

---

## Check 19 — AI need and demand

**Result: PASS as a non-AI tool. Demand is real. Do not add AI to the conversion itself.**

Demand evidence (sourced, not refreshed):

- Last recorded GSC, test-plan.csv / B-0043: **48,950** impressions for "roman numeral converter" at position **9.0**, CTR **0.1%**; `/es` **9,585** impressions. That is the site's #1 query in that plan. Current GSC is **not available**.
- A full competitor set ranks for the same head term (timeanddate, RapidTables, Calculator Soup, and others). Related intents already written into the page — years, tattoo/wedding dates, clock-face IIII, 1–100 chart — match real uses named in B-0114 (students, tattoos, copyright years, clocks, `/es` speakers).

AI would not make the conversion more trustworthy. Users need a deterministic, checkable answer (MMXXVI, not a model guess). The step-by-step working already shows the method. An AI feature is not needed to grow this tool. Demand is already there; the gap is the snippet/CTR and the stale blog/video packaging, not missing AI.

---

## Checks 20, 21 and 22 — Merge, remove, or duplicate

**Result: KEEP. No merge. No removal. No duplicate tool.** Severity: n/a.

Sitemap and catalog overlap check (grep of `/workspace/deep/sitemap-urls.txt` and the category / Professional Tools pages):

- Only one Roman numeral tool: `/tool/roman-numeral-converter`.
- Nearby but different jobs: `/tool/number-to-words` (spells numbers in words), `/tool/timestamp-converter` (Unix/ISO time), Age & Date Calculator (ages and date math), `/tool/add-page-numbers` (can stamp Roman page numbers on a PDF). None of these convert general numbers or calendar dates to Roman numerals.

Do not merge this into Number to Words or Age & Date Calculator. Do not remove it: it has the site's largest recorded query demand and a complete, distinctive feature set. Optional internal links to Number to Words and Case Converter (for lowercase preface numerals) are enough.

---

## Decisions for Santosh

1. **Update the blog** so it describes vinculum to 3,999,999, date validation, and the separator / US-order controls. High priority: the guide currently contradicts the tool.
2. **Fix the 4 July 1776 sentence** on the tool page so day-month-year and US order are both labelled.
3. **Retitle and rewrite the YouTube packaging** (and then sync JSON-LD and sitemap). Someone needs to watch the 72-second clip to see whether it still shows only the pre-vinculum tool.
4. **SEO:** keep the live title; consider the 154-character meta above so the snippet advertises the 3,999,999 range; add thumbnail alt and a tool-specific OG image; optionally qualify the $4.99 SoftwareApplication price as monthly. Current CTR is not available — a GSC check is still owed against the old 0.1% / position 9 baseline.
5. **Sitemap:** decide whether locale URLs such as `/es/tool/roman-numeral-converter` should be listed (they are not today).
6. **Keep the tool as a non-AI Professional Tool** in Unit, Date & Everyday Calculators. No merge or removal.

## Files used

- Live fetches under `/workspace/deep/01-roman-numeral-converter/` (`tool.html`, `tool-es.html`, `blog.html`, `robots.txt`, `sitemap-roman.xml`, catalog pages, `js/`, YouTube and competitor HTML).
- Test cases: `/workspace/deep/01-roman-numeral-converter/test-cases.md`.
