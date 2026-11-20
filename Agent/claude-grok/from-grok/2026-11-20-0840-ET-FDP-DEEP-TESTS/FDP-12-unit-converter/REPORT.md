Sent: 2026-11-20 08:40 ET

# FDP-12 Unit Converter (unit-converter): deep test report for Claude

- **Written:** 2026-11-19 14:09:52 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/unit-converter, plus 20 pair pages under /tool/unit-converter/<pair>. Row 12 of TEST-ORDER.md (test-plan rank 10: "4,782 impr pos 7.4 0 clicks", quoted from TEST-ORDER and not re-verified). **GSC data is not available.**
- **Classification:** Professional Tool, Unit, Date & Everyday Calculators. **Takes no trial use.** No trial strip is shown, and Copy result, Save as text and Print all work at 0 remaining. This matches /terms, /faq and the homepage.
- **Testers:**
  - **Desk review:** curl of the tool, 10 locales and /ar, a pair page, the sitemap (20 pair URLs) and the blog. JS: UnitConverter, the ToolPage unit tables (`evidence/js/units-data.pretty.js`) and useLogToolUsage. WebSearch for competitors and the brand query.
  - **YouTube video:** metadata, 19 frames, a contact sheet and crops.
  - **Headless Playwright:**
    - 55 conversion cases checked against exact definitions
    - a probe of page notes and 6 pair pages
    - the export gate in 6 contexts
    - UI, keyboard, axe, de-DE and phones
    - matrix: 10 profiles, 10 locales + /ar, 6 geos, axe
- **Constraints kept:** guest only, no sign-in, no card or email entered, no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** none needed. **No URLs were blocked by sign-in.**
- **Nothing pending:** the gate behaviour was observed at 0 remaining (exports work, as the site copy says). No RERUN-AFTER-RESET row was added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real components, then restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work.

Components to look at:
- **UnitConverter:**
  - the tab list layout on narrow screens
  - the result region (aria-live)
  - input validation for negatives
- **ToolPage unit tables** (`wa` categories, `hi` pairs, `Se` formatter, `bi`/`Bl` pair tables, `yi` pair meta): add ft+in; make `toExponential(6)` match the 10-digit promise; ⅓ cup.
- **The number formatter's locale** (`Intl.NumberFormat(undefined)` follows the browser, so an ar-SA browser gets Arabic-Indic digits).
- **The blog's trial line and the video.**

After you ship, rerun `test-cases.md` (UC-01…UC-26).

## Intent

Someone types "cm to inches" or "5'10 in cm" on a phone and wants the answer in one glance. The math here is exact and the feature set is broad (15 categories, cooking by ingredient, an all-units list, shareable URLs). The page loses that "wow" when, on a small phone, the answer is two screens down. It also lacks the single most common everyday conversion, height in feet and inches.

## Why: what the evidence says

- **The core is exact.** All 55 cases match exact legal definitions to 10 significant digits. Absolute-zero and fuel-zero handling work. Cooking weights are standard published values and are labelled approximate. The URL state works as the FAQ says.
- **First screen on small phones (P1).** On iPhone SE the 15 tabs take 156 px, and the Value box (y≈644) and the answer (y≈818) are below the 568 px fold.
- **No feet + inches (P1).** It isn't offered (live-verified). Competitors offer it, and it is the dominant height query.
- **Smaller issues (P2):**
  - 7-digit scientific display vs the 10-digit FAQ promise.
  - Negatives accepted for length and fuel.
  - Pair-page details: 0.33 cup, the "1 celsius = 33.8 fahrenheit" meta, duplicate FAQs, missing high-demand pairs.
  - No aria-live; the shared axe critical on the tabs.
  - 8 locale URLs with English content under a foreign `lang`.
  - Arabic-Indic digits for ar-SA browsers.
  - An old 4-tab video with "free" wording.
  - A blog line claiming "10 trial usages a day".

## Outcomes we want

1. On any phone, the Value box and the answer are visible on the first screen.
2. Height in feet + inches converts both ways, with its own pair page.
3. Displays match the stated precision; impossible negatives are flagged.
4. The video, blog and locale pages describe this tool as it is now (no trial use needed).

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PASS** | — | 55 of 55 numeric/alert cases correct (two script reference errors corrected; see findings). `findings/live-functional-findings.md`, `json/cases.json` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | Broad (15 categories, cooking, all-units list, URL state). Missing: ft+in, torr/inHg, troy oz, carat, value-specific pages. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | HIGH | Instant, with swap and the all-units list; keyboard works. On small phones the input and answer are below the fold. |
| 4 | Layout attractiveness | **PARTIAL** | LOW | Clean. The tab wrap leaves a stretched second row on desktop; 9 px header overflow at 320 px (site-wide). `findings/devices-locales-findings.md` |
| 5 | Payment process | **N/A** | — | Ungated tool: no trial strip, no pass buttons on the page, no cap dialog at 0. |
| 6 | Information correct | **PASS** (minor) | LOW | Factors exact; the FAQ is accurate except "ten significant digits" for scientific values. Pair meta "1 celsius = 33.8 fahrenheit"; the 0.33-cup row. |
| 7 | Indexing | **PASS** | — | 200, self-canonical; the tool and 20 pair pages are in the sitemap with a video block. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Strong title, meta, H1 and 13-question FAQPage on the main page. Pair pages repeat the generic FAQ and VideoObject; the high-demand pairs above are missing. 8 English locale copies with a foreign `lang`. The test plan's 0 clicks at pos 7.4 fits a widget-dominated head term, so long-tail pairs are the lever. |
| 9 | Blog post | **PARTIAL** | LOW | /blog/unit-converter: figures right (80 mm, 1.25 kg, 300 mm). It has the "10 trial usages a day" line and doesn't mention cooking, the all-units list or pair pages. |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | i01IkvYUEVo, 57 s, 0 views, embedded. |
| 11 | FAQ / usage guide | **PASS** (minor) | LOW | 13 accurate FAQs (URL state, kB/KiB, horsepower, −40). The precision claim is only true for non-scientific values. |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM | 4 of 15 tabs, old breadcrumb, "free" wording. `findings/video-findings.md` |
| 13 | Storage | **PASS** | — | No account storage; state is in the URL (by design). Runs in the browser (not network-audited). |
| 14 | Sharing | **PASS** | — | The URL updates live (`?c=&from=&to=&v=`) and reloads exactly; 20 pair URLs. |
| 15 | Downloads | **PASS** | — | `unit-converter-result.txt` (full list, locale-formatted, "Calculated with FreeDailyPro.com"); Print. `downloads/` |
| 16 | Usage count | **PASS** | — | No trial use: exports work at 0 (observed 13:58 EST), matching /terms, /faq and the homepage. Counters are display-only. Starting counts: the probe context loaded with 10 remaining; 7 later contexts at 0. |
| 17 | Categorization | **PASS** | — | Unit, Date & Everyday Calculators. |
| 18 | Location in site | **PASS** | — | Breadcrumb, category, popular-conversion links, blog. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic; high demand (test-plan rank 10). |
| 20 | Merge? | **N/A: keep** | — | The hub for the pair pages. |
| 21 | Remove? | **N/A: keep** | — | High demand, exact. |
| 22 | Duplicates | **PASS** | — | No duplicate tool. Pair pages are intentional and canonical, but they share boilerplate FAQs. |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`. All 10 profiles return 200; the only issues are the small-phone fold and the 320 px header. de/fr browsers get "0,001" (fine); ar-SA browsers get Arabic-Indic digits on the English page.

**Ads:** keep them in reserved fixed-height slots below the tool (as now). Never put one between the inputs and the answer.

## Suggested direction (interpret freely)

1. **First screen (P1).** Below about 640 px, swap the 15 tabs for a category select (or a single horizontally scrolling row), and place Value and the answer directly under it. Check on iPhone SE.
2. **Feet + inches (P1).** Add a Length unit "ft + in" with two inputs and output "5 ft 10.08 in". Add pair pages cm-to-feet-and-inches and feet-and-inches-to-cm.
3. **P2:**
   - Make scientific display 10 significant digits (`toExponential(9)`).
   - Warn on negatives in non-negative categories.
   - Use ⅓ and ⅔ in cup tables.
   - Give temperature pair metas a 0 °C / 100 °C anchor.
   - Add aria-live to the result.
   - Translate or de-list the 8 locales.
   - Format with `numberingSystem: 'latn'` (or the page language).
   - Re-record the video; fix the blog trial line.
   - Add torr, inHg, troy oz, carat and more cooking ingredients.
   - Add pair-specific FAQs.

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- This tool takes no trial use, as the site says. Don't add a gate as part of this work.
- Counters are display-only evidence.

## Process

Inspect UnitConverter and the ToolPage unit tables → restate → propose → implement → verify with `scripts/uc-live.js`, `scripts/uc-kbd.js` (phones) and `test-cases.md`.
