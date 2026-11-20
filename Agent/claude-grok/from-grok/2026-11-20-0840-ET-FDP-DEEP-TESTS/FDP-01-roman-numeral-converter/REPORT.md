Sent: 2026-11-20 08:40 ET

# FDP-01 Roman Numeral Converter: deep test report for Claude

- **Written:** 2026-11-19 09:46:08 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/roman-numeral-converter. The slug was confirmed in `/workspace/deep/site-map/tools.csv`.
- **Classification:** Professional Tool in Unit, Date & Everyday Calculators. It has 10 trial uses per day, a $1 day pass and a $4.99 monthly pass.
- **Testers:**
  - Desk review (curl, JS read, competitors)
  - Live desktop Chrome on a fresh profile
  - Headless Playwright: 10 device/browser profiles, 10 locales, 6 country contexts, axe, and the Step A edge/usage pass
  - Video watched by a video-analysis model
- **Constraints kept:** guest only, no sign-in, no card entry (stopped at the Stripe page), no ad clicks, no API/MCP calls, no site or repo changes.

## How to work with us

You know the codebase better than this report does. Treat the findings as evidence and judgment, not orders. Inspect the real components, then:
- Restate what you think the problem is.
- Challenge anything that looks wrong.
- Choose the implementation that fits how FreeDailyPro has shipped similar fixes before.

After you ship, rerun the test cases in this zip.

## Intent

This is the site's highest-demand tool. The last recorded Search Console figures were about 49k impressions for "roman numeral converter", at position 9 and 0.1% CTR. Those figures are old, and **current GSC data is not available** for this review.

When someone arrives with a year, a tattoo date or a big number, they should:
1. Get a correct, beautiful answer instantly.
2. Feel "wow, it even does dates, bars over thousands and shows the working".
3. Meet a clear, honest trial uses meter that nudges heavy users (teachers, designers, tattoo studios, publishers) toward the $1 or $4.99 pass.

## Why: what the evidence says

The engine is excellent. All 4 conversions were correct on 10 device/browser profiles. Vinculum works to 3,999,999 with bars rendered. Errors and "Did you mean…" hints are accurate. The CSVs are clean, and no ad overlaps the tool.

The weak points are elsewhere:
1. **Monetization:** the trial meter never appears, and nothing is counted.
2. **US date entry:** it is broken.
3. **Language pages:** 8 of the 9 hreflang language pages are English.
4. **Packaging:** the blog and video describe an older, smaller tool.

## Outcomes we want

- A guest sees the trial uses strip and its pass options on this tool. Copying or exporting a result spends a trial use as the FAQ promises, and the stored and displayed counts agree across reloads.
- A US user types 11 / 19 / 2026 in Month.Day.Year mode and gets XI.XIX.MMXXVI. The FAQ example 7.4.1776 → VII.IV.MDCCLXXVI works as written.
- Every hreflang target is genuinely translated, or it is removed from the hreflang cluster until it is.
- The blog, the video and its title/description, the JSON-LD and the sitemap all describe today's tool (vinculum, dates, working, charts) without "free" wording.
- 320px phones have no horizontal scroll. Touch targets are at least 44px and inputs at least 16px on tablets.

## The 22 checks

| # | Check | Result | Severity | Evidence (zip paths) |
|---|---|---|---|---|
| 1 | Capability | **PARTIAL** | MEDIUM-HIGH | Number↔Roman, vinculum, edge errors and DMY dates all PASS. **US-order date entry is broken** (see #3). `evidence/findings/edge-usage-findings.md` §1, `evidence/screens/edge/us-order-11-19-error.png` |
| 2 | Completeness vs competitors | **PARTIAL** | LOW | Exceeds timeanddate and RapidTables on dates plus working plus both charts plus CSV. Live-verified gaps: no result-carrying share link, no Year.Month.Day order. Lowercase output toggle: *unverified absence* (JS-only read). `desk-findings.md`, `edge-usage-findings.md` §3 |
| 3 | Ease of use | **PARTIAL** | MEDIUM | US mode heading says "(month, day, year)" but the first box is still Day: 11/19 gives "Month must be between 1 and 12."; 7/4 silently becomes 7 April. Date boxes have no visible labels. The Number box says only "Enter a whole number…" for Roman input. iPad copy buttons are 28px and title icons 16px. `edge-usage-findings.md`, `devices-locales-findings.md` D3/D4 |
| 4 | Layout attractiveness | **PARTIAL** | LOW-MEDIUM | The dark layout is clean, results are large, there is no ad overlap and Chromium CLS is 0. The 320px header overflows by 9px (iPhone SE, S9+). On iPhone SE the result sits below the fold. The WebKit select is low-contrast. `evidence/screens/devices/*-fold.png` |
| 5 | Payment process | **PARTIAL** | HIGH | On /pricing, "$1 Buy Day Pass" opens the email prompt and "$4.99 Subscribe Monthly" reaches checkout.stripe.com (stopped there, nothing typed). **On the tool page itself no strip or pass CTA renders for guests**, so the upgrade path from this tool is invisible. `live-desktop-findings.md`, `edge-usage-findings.md` §2 |
| 6 | Information correct | **PARTIAL** | MEDIUM | The rules, examples and the 1–100 chart are correct. Wrong items: the H2 sentence "4 July 1776 is VII.IV.MDCCLXXVI" is unlabelled US order; the FAQ "7.4.1776 becomes VII.IV.MDCCLXXVI" fails live in US mode; the JSON-LD Offer $4.99 has no period. `desk-findings.md` Check 6 |
| 7 | Indexing | **PARTIAL** | LOW | 200, indexable, self-canonical, in the sitemap with a video block; the English URL is confirmed indexed via WebSearch. Locale URLs are not in sitemap.xml. **GSC data not available.** `desk-findings.md` Check 7 |
| 8 | SEO | **PARTIAL** | HIGH (hreflang) / MEDIUM | Title (55), meta (158), H1 and H2s are good, and JSON-LD has 5 valid blocks. **hreflang points to 8 untranslated pages** (pt, fr, de, ja, hi, zh, ko, id serve the English title, meta and H1). Also: generic og-default.png, empty video-thumbnail alt, VideoObject name differs from the YouTube title, and the meta omits the 3,999,999 range. `devices-locales-findings.md` §2, `desk-findings.md` Check 8 |
| 9 | Blog post | **FAIL** | HIGH | /blog/roman-numeral-converter returns 200 and links the tool, but it says 4,000 is rejected, that there is no overline and that there are no date layouts. All three are false today. `desk-findings.md` Check 9 |
| 10 | YouTube video exists | **PARTIAL** | MEDIUM | Jrmgcqn_jJw, 72 s, embedded on the tool and the blog. Its title and description use "Free" wording, the keywords lack "roman numeral", and the titles differ across YouTube, JSON-LD and the sitemap. `desk-findings.md` Checks 10/12 |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | 11 FAQ questions, visible and matching JSON-LD. Two answers are contradicted live: the 7.4.1776 US example, and "copying or downloading it uses one of your trial uses", which never happens. `edge-usage-findings.md` |
| 12 | Video shows current capabilities | **FAIL** | MEDIUM-HIGH | It shows only basic both-way conversion. It says "values from 1 to 3999… beyond that… not supported", shows "free uses" badges and "200+ Free Productivity Tools", and claims the other field fills automatically, which is false. `evidence/findings/video-findings.md` |
| 13 | Storage | **PASS** | — | Session "Recent calculations" with Clear and the honest note "Kept only while this page is open…". Reload resets to the defaults, as designed. `edge-usage-findings.md` §3 |
| 14 | Sharing | **PARTIAL** | LOW | "Share this tool" copies the bare tool URL; the value is lost. Share does not touch the counter. `evidence/screens/edge/share-click.png` |
| 15 | Downloads | **PARTIAL** | LOW | `roman-numerals-1-100.csv` (BOM, 100 rows) and `roman-numerals-years.csv` (101 rows) are correct. **Copy table** inserts an unrelated "Working for 2,026" block before the table. Print calls `window.print`; layout was not inspected. `evidence/csv/`, `evidence/json/copy-table-clipboard.json` |
| 16 | Usage count | **FAIL** | HIGH | In 2 fresh contexts, Copy, CSV ×2, Print, Copy table and reload all left `usageToday` at 0, and the strip never rendered (display-only evidence). This breaks the owner policy and the page's own FAQ. `evidence/json/edge-usage-results.json` |
| 17 | Categorization | **PASS** | — | Unit, Date & Everyday Calculators card; Professional Tools hub. `desk-findings.md` |
| 18 | Location in site | **PASS** | — | Breadcrumb Home › Unit, Date & Everyday Calculators › Roman Numeral Converter. |
| 19 | AI need / demand | **PASS** (no AI needed) | — | Deterministic answers beat model guesses. Demand is the site's #1 recorded query (old GSC). Growth levers are CTR, packaging and the meter, not AI. |
| 20 | Merge? | **PASS: keep standalone** | — | No better merge target. Add cross-links to Number to Words and Add Page Numbers (Roman page numbers) instead of the generic Unit, Currency and Time Zone links. |
| 21 | Remove? | **N/A: keep** | — | Highest demand, full feature set. |
| 22 | Duplicates | **PASS** | — | This is the only Roman numeral tool in the sitemap and catalog. |

## Devices, platforms, countries and languages

Full matrix in `evidence/findings/devices-locales-findings.md`.
- **PASS:** conversion correct on 10/10 profiles (iPhone SE and 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11, desktop Chrome 1366/1920, Firefox and WebKit 1440). No ad overlap anywhere. Chromium CLS 0. Phones get 16px inputs and 44px copy buttons. html `lang` is correct on every locale. No "free/gratis/kostenlos/gratuit" wording. The EU-timezone consent banner offers Accept all, Reject non-essential and Choose. Mobile axe found 0 violations.
- **FAIL / PARTIAL:**
  - 320px header overflow (MEDIUM)
  - tablet tap targets and 14px inputs (MEDIUM)
  - Day.Month.Year is the default for every locale, including en-US, and there is no Y.M.D option (MEDIUM)
  - English number grouping in every locale (LOW)
  - no Arabic page: `/ar/` returns 404, so RTL is N/A
  - desktop axe: 1 serious and 1 moderate violation
  - AdSense `no_div` console errors (LOW)
  - The consent banner was triggered by timezone. A real EU IP, and whether ads wait for consent, were **not tested**.
- **Ads:** keep them. If any placement work happens, use reserved, fixed-height slots below the tool and in the side rails, which is what the page already does. Never put ads between the input and the result.

## Suggested direction (interpret freely)

1. **Meter and upgrade nudge.** Find out why `UsageAndUpgradeStrip` does not render and why `useLogToolUsage` / `gate()` do not increment on this tool. The fix might be a tool-id/tier mismatch, or a guard that skips the gate. Show the strip, with its $1 / $4.99 options, from first paint.
2. **US date order.** Either reorder the input boxes (and their visible labels and aria-labels) when the mode changes, or keep the boxes fixed and label them visibly. Then make the FAQ example true.
3. **Locales.** Translate the tool strings and content for the 8 locales, or drop them from hreflang until they are translated. Consider adding the locale URLs to the sitemap once they are real.
4. **Packaging.** Update the blog, re-record or re-edit the video (dates, bars, working, charts, trial uses wording), and sync the YouTube title, the JSON-LD and the sitemap.
5. **Polish.** Fix the 320px header, the tablet targets and font size, the Copy table payload, share-with-value, a Y.M.D option, and locale-aware defaults.

## Constraints

- Say "Professional Tools" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Keep the privacy honesty ("Files never stored", "Runs on your device", session-only history).
- Don't change pricing in this work.
- The counters here are display-only evidence. Verify backend behaviour in code.

## Process

Inspect the components (RomanNumeralConverter, UsageAndUpgradeStrip, useLogToolUsage, history and csv) → restate → propose → implement → verify with `scripts/` and `test-cases.md` (RN-01…RN-37).
