Sent: 2026-11-20 23:05 ET

# FDP-27 BMI Calculator (bmi-calculator): deep test report for Claude

- **Written:** 2026-11-20 23:00:06 EST (box `date`, ET). Testing ran 2026-11-20 22:40–22:58 EST.
- **Tool:** https://www.freedailypro.com/tool/bmi-calculator. Row 27 of TEST-ORDER.md: Pro, Health Calculators, test-plan rank 22 ("54+52 views; 504 impr bmi", from the test plan, not verified), duplicate group C29 (Body calculators). **GSC data is not available.**
- **Classification:** Professional Tool (Health Calculators). The site bundle tags it `absorbable` (DUPLICATES.md legend). **Live, it takes no trial uses at all, and no export is gated, even at 0 remaining.**
- **Testers:**
  - **Desk review:** page (expanded copy), JSON-LD, 10 locales + /ar, robots/sitemap, /blog/bmi-calculator; JS chunks `BmiCalculator`, `BmiExtras`, `MeasureField`, `numberInput`, `useLogToolUsage`, `csv`, `history`; WebSearch on competitors (NHS, CDC, calculator.net, Calculate.Studio).
  - **YouTube video:** yt-dlp, metadata + 44 frames.
  - **Headless Playwright:**
    - 46 calculation cases in metric and imperial, with validation, age, waist, Asian and target.
    - 6-context export and gate run.
    - Share, favorites and URL round-trip.
    - Network capture of where the typed values go.
    - Print rendering, keyboard order.
    - 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** most fresh contexts loaded at "0 remaining" (`usageToday` 10), e.g. 22:40:26 and 22:45:12 EST; two loaded with 10 left (22:45:55 and 22:46:34 EST). Trial uses spent: **0** (the tool never counted anything).
- **Constraints kept:** guest only, no sign-in, nothing typed into email or card prompts (none appeared), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in:** nothing on this tool needs it. Favorites are local; Share copies a link. No URL was blocked by sign-in.
- **Pending:** none. No RERUN-AFTER-RESET row is needed: nothing is counted, so a context with uses left gives no new information. Both a 0-remaining and a 10-remaining context were observed.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Code to look at (`evidence/js/`):
- `BmiCalculator-CIQaJbup.pretty.js`:
  - `le()` + `history.replaceState` write `?kg=&cm=` into the URL on every keystroke (the privacy issue).
  - `A()`/`N()` classify on the rounded BMI.
  - `ee()` handles age; the "Sex … child percentile charts" note.
- `BmiExtras-Fs-a8-UB.pretty.js`:
  - The Target weight block (default "24.9"; ignores the Asian option; "which is " + lose/gain).
  - The export text `M` and the CSV (WHO table only).
  - The `calc-print-area` wrapper, which decides what prints.
- `useLogToolUsage-BdvvKW0n.pretty.js`: the gate only runs when the tool is `known`; live, nothing is gated.

After you ship, rerun `scripts/bmi-privacy.js`, `bmi-gate.js`, `bmi-live.js`, `bmi-misc.js` (print PDF), `bmi-share.js`, then `test-cases.md` (BMI-01…BMI-40).

## Intent

Someone wants a quick, private, trustworthy read of their weight for their height. They want the number, what it means, the healthy weight range in their own units, and what to aim for. They may want to save or print it for a doctor's form or to track it. They should come away feeling "this is better than the other BMI sites", and they should see why the paid Professional Tools are worth it.

The engine is right: every one of 46 cases matched hand maths, in metric and imperial. Validation is friendly ("That looks like metres…"), European comma decimals work, and the extras (8 WHO classes, BMI Prime, Ponderal Index, waist-to-height, Asian cut-offs, worked steps) go beyond most competitors.

Trust is lost in three places:
- The page promises the numbers are "not … sent anywhere", but they ride in the URL to Google Analytics, AdSense and the server.
- The target-weight line tells normal-weight users to "gain 2.0 kg", and with Asian cut-offs it contradicts the main card.
- "Print or save as PDF" produces a page without the BMI on it.

## Why: what the evidence says

- **P0: Health values leave the browser despite the privacy promise.** Typing 87.3 kg / 179.5 cm puts `?kg=87.3&cm=179.5` in the page URL.
  - Without any reload, a Google Analytics collect carried that URL.
  - On reload or a shared link, it went to `www.freedailypro.com`, 4 × `googleads.g.doubleclick.net/pagead/ads`, the AdSense ping body and GA again (2026-11-20 22:56–22:57 EST, `json/privacy.json`).
  - The Details › Privacy copy says "not stored, tied to an account or sent anywhere"; the FAQ says "never stored or uploaded".
- **P1, policy question for Santosh (not a PASS): no trial use is ever taken.** All six exports (Copy result ×2, Download CSV, Print or save as PDF, Save as text, Print) worked in a context at 0 remaining with no cap dialog (10 → 10). In a context with 10 left they cost nothing (0 → 0, also after reload) (`json/gate.json`, 22:45–22:46 EST).
  - The page has no trial strip and no pass offer.
  - The tool is tagged `absorbable`, like grammar-checker. Santosh's Nov 20 decision lists only Unit Converter, Grammar Checker and Word Counter as uncounted on purpose, so BMI needs his call.
  - The blog says "copying, saving or printing uses one trial use per visit", which is wrong today.
- **P1: Contradictory weight advice.** The Target weight block defaults to BMI 24.9 and ignores the Asian option.
  - 70 kg/170 cm with Asian cut-offs: the card says "Overweight (Asian cut-offs)… lose about 3.8 kg"; the line under it says "A BMI of 24.9 at your height is 72.0 kg, which is gain 2.0 kg."
  - Every normal-weight visitor sees a "gain" suggestion by default (53.4 kg → "gain 18.6 kg"). (`json/cases.json` B07, B09, B06)
- **P1: Print / "Print or save as PDF" omits the result.** Only the extras print: the BMI number, category, gauge, healthy range, inputs and date are missing. Interactive bits print instead (target input, collapsed steps, "Clear"). (`screens/live/printprev-1.png`, `testfiles/outputs/print-preview.pdf`)
- **P1: The video is outdated and off-topic.** It shows the old "BMI & Calorie Calculator" with only weight/height, a 3114.2 BMI from 17 cm (now rejected), and promises "Daily Calories". The page's embed and VideoObject are named "How to Calculate BMI & Daily Calories Online"; the YouTube title says "Free…"; 1 view. (`findings/video-findings.md`, `video/f026.png`)
- **P2:**
  - Export and input polish:
    - The CSV holds only the WHO table (no BMI, inputs or date).
    - Two "Copy result" buttons copy different texts; the card copy includes the gauge's screen-reader sentence.
    - Rounded-value classification: 72.2 kg → 25.0 "Overweight"; 53.4 kg → "Normal" below the range shown.
    - The Sex field does nothing ("only used for child percentile charts", but none exist).
    - An invalid age silently hides the extras; target "abc" shows nothing.
    - "which is gain 0 lb".
    - The share link drops age and the Asian option.
  - Copy contradicts itself: FAQ "applies them to every entry", Limitations "does not adjust for age, sex, ethnicity", the "Files never stored" badge, and the CDC tool is named but not linked.
  - The blog is outdated (asks whether to add features that exist; "the tool will reject or flag" kg/lb mix-ups, but 154 "kg" gives 53.3 with no flag).
  - Locales other than es are untranslated, and es says "gratis"; /ar returns 404.
  - Layout and markup: iPhone SE 9 px overflow, and the result is below the fold on phones; JSON-LD Offer 4.99 on an uncounted tool; axe heading-order and label mismatch; the thumbnail has no alt.

## Outcomes we want

1. Weight and height never leave the device unless the user explicitly shares a link, and the privacy copy is true word for word.
2. The trial-use behaviour matches Santosh's decision for this tool, and the blog, FAQ and terms say the same thing.
3. One consistent piece of advice per screen: the target follows the chosen cut-offs and never suggests gaining toward the edge of the range by default.
4. Every export (print/PDF, text, CSV) carries the result itself: BMI, category, inputs, healthy range, date.
5. The video and its titles show today's BMI Calculator.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PASS** (engine) / PARTIAL (outputs) | MEDIUM | 46/46 cases match hand maths; print and CSV miss the result. `findings/live-functional-findings.md` §1, §3 |
| 2 | Completeness | **PARTIAL** | MEDIUM | Ahead of most on extras; missing child/teen percentile (NHS, CDC have it), stones, wider ethnicity option. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | MEDIUM | Instant results, helpful validation, comma decimals; conflicting target line; two Copy buttons; result below the fold on phones. |
| 4 | Layout attractiveness | **PASS** | LOW | Clean card, colour gauge, WHO table; iPhone SE H1 wraps to 6 lines; 9 px overflow (site header). `screens/devices/` |
| 5 | Payment process | **N/A** (no pass offer on this page) / FAIL for the conversion goal | MEDIUM | No strip, no Quick Buy, no cap dialog: nothing moves a visitor toward a pass. No checkout was reached, so no email/Stripe step was seen. |
| 6 | Information correct | **PARTIAL** | HIGH | Formulas, WHO bands, Asian 23/27.5 correct; target advice contradicts the card; rounding edge cases; Sex note false. |
| 7 | Indexing | **PASS** | — | 200 (also Googlebot UA), self-canonical, in sitemap, robots allow. GSC data is not available. |
| 8 | SEO | **PARTIAL** | LOW | Strong title/meta/H1, FAQPage 14 Q; 8 of 9 locales untranslated, es "gratis"; VideoObject name mentions calories; Offer 4.99; heading-order; thumbnail alt. |
| 9 | Blog | **PARTIAL** | MEDIUM | Exists (Oct 24); examples correct; trial-use sentence, "reject or flag" claim and feature questions outdated. |
| 10 | YouTube video | **PASS** (exists) | — | SogofBA7ENk, 88 s, embedded. |
| 11 | FAQ and usage guide | **PARTIAL** | MEDIUM | 14 FAQs mostly right; 3 contradictions; privacy statement false (P0). |
| 12 | Video matches current tool | **FAIL** | HIGH | Old "BMI & Calorie Calculator", 3114.2 bug, calories promise. `findings/video-findings.md` |
| 13 | Storage | **PASS** | — | Nothing stored except favorites/recent-tools keys; history in memory only (claim true for storage). |
| 14 | Sharing | **PARTIAL** | MEDIUM | Share copies a link with kg/cm that restores the result (good). It drops age/Asian, and the same URL mirroring is what leaks the values (P0). |
| 15 | Downloads | **PARTIAL** | MEDIUM | CSV (BOM, formula guard) and .txt download; CSV has no result; print/PDF misses the BMI. |
| 16 | Usage count | **POLICY QUESTION** | HIGH | 0 uses for every action, nothing gated at 0. Not in Santosh's uncounted list (UC, GC, WC). |
| 17 | Categorization in section | **PASS** | — | Health Calculators; breadcrumb, JSON-LD and tools.csv agree; next steps: Body Fat → Calorie → Ideal Weight. |
| 18 | Correct site section | **PASS** | — | Professional Tools › Health Calculators. |
| 19 | AI need / demand | **MEDIUM demand, low AI need** | — | A chat assistant does BMI well (hence `absorbable`); search demand exists (504 impressions per the test plan, unverified). The page's edge over chat is the visual gauge, healthy range and private local calculation, which the P0 undermines. |
| 20 | Not full-featured / merge? | **No merge** | LOW | Full-featured. Cross-link the healthy range to Ideal Weight rather than merging. |
| 21 | Not useful / remove? | **Keep** | — | Useful, has search demand. |
| 22 | Duplicates | **Keep (C29)** | LOW | Overlaps Ideal Weight (healthy range) and Body Fat; distinct purposes; the site already 301s bmr-macro → calorie. |

Devices, locales, geo and axe: `findings/devices-locales-findings.md`.
Wording: Professional Tools, trial uses. The "Created with FreeDailyPro.com" line in text exports is intentional. Ads were never clicked; reserve slots rather than removing them.
