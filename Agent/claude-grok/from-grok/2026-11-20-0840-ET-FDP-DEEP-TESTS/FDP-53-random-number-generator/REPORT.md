Sent: 2026-11-21 09:47 ET

# FDP-53 Random Number Generator (random-number-generator): deep test report for Claude

- **Written:** 2026-11-21 09:44 EST (box `date`, ET). Testing ran 2026-11-21 09:19–09:44 EST.
- **Tool:** https://www.freedailypro.com/tool/random-number-generator
  - TEST-ORDER row 53: **Professional Tool** in Unit, Date & Everyday Calculators.
  - Plan note: "test-plan (unranked): GA top-traffic".
  - Duplicate group C45 (Random picks), with giveaway-winner-picker.
  - Video: buvkdsqCW5w. Blog: /blog/random-number-generator.
  - **GSC data is not available.** No API/MCP testing.
- **What it is:** five modes, all generated in the browser.
  - **Numbers:** min/max, how many (up to 10,000), 0–10 decimal places, no duplicates, sort, optional seed.
  - **Dice:** NdM±k, up to 10,000 dice and 1,000,000 sides.
  - **Coin:** up to 10,000 flips.
  - **Lottery:** pick k of a pool up to 100,000, with exact odds.
  - **List:** pick or shuffle up to 10,000 lines.
  - Results offer Copy Results, Download .txt, and "How this was generated" steps.
  - Default generator: `crypto.getRandomValues` with rejection sampling. A seed switches to sfc32 with a clear "not secure" warning.
- **Testers:**
  - Desk: copy (5 FAQs), Details, JSON-LD, blog, JS (`RandomNumberGenerator-cHv4w4le.js`, `random-DRWu2o-X.js`, `useShareGate-BYBawloP.js`).
  - Headless Playwright: a 45-case functional battery in Chromium, Firefox and WebKit.
  - Trial-use check in a 0/10 context and a 10/10 context.
  - Big-list timing, UX/keyboard/live-region probe, share buttons.
  - Video frame by frame.
  - Matrix: 10 devices, 10 locales plus an /ar probe, 6 geo contexts, axe.
- **Constraints kept:** guest only. No sign-in, card or email. No ad clicks. No site or repo changes.
- **Sign-in:** nothing on this page needs sign-in. Share copies the link; Create Shortcut gives an install hint.
- **RERUN-AFTER-RESET:** none. Both a context with uses left (0/10) and a capped context (10/10) were tested.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders.

**Owner context (trial uses):**
- Santosh's Nov 20 rule: only Unit Converter, Grammar Checker and Word Counter are uncounted on purpose. Any other tool that takes no trial use is a **policy question**.
- This tool takes none:
  - Generate, Copy and Download never change `fdp-usage-v1` (0/10 stays 0/10).
  - There's no usage.log POST and no cap dialog at 10/10.
  - The page shows no trial strip.
  - The FAQ says so on purpose ("copying or downloading them never takes a trial use").
  - In code, Download passes `{ free: true }`, and both actions go through `gateShare`, which only charges when the tool is `known && !paid`.
  - The old video showed "10 free uses daily · 8 free uses left today", so it used to be counted.
- **Decision needed:** add it to the uncounted list, or count it. If it's counted, judge whether a one-click generator should charge per Copy/Download.

**Where to look:**
- **Stale result under errors:** the result card stays visible when inputs become invalid. "20 numbers" stays under "Only 5 unique values exist…", and "Total 9 / Dice add up to 7, then plus 2" stays under "A die needs at least 2 sides". Clear or dim `f` when `re.ok` turns false.
- **Results region:** it has no `aria-live`/`role=status`, so screen-reader users hear nothing after Generate. Enter in a field doesn't generate.
- **SoftwareApplication JSON-LD** says `offers.price 4.99`, but the page offers nothing to buy and takes no trial use. The schema description and the page subtitle are still "with or without duplicates" and don't mention dice, coin, lottery or list.
- **Locale pages:** only the breadcrumb and badge are translated. H1, subtitle, title, meta and every control label stay English on all 10 locales.

**After you ship:**
- Rerun `px53-live.js func` in all three engines (45 cases; expect the same results, no stale cards).
- Run `px53-live.js gate` (expect whatever the owner decides).
- Run `px53-ux.js` (expect a live region).

## Intent

Someone running a raffle, a classroom draw, a game night or a quick sample wants a number they and the room can trust, in one click, and a record they can copy. The "wow" is: it's instant, it's provably fair, and it handles the odd cases (unique picks, decimals, dice, lists) without a second site.

The tool earns that. It's one of the strongest everyday utilities tested so far:
- **Fairness is real and explained.** 10,000 rolls of 1–6 give chi² of 7.99 (Chromium), 4.27 (Firefox) and 5.77 (WebKit), all below the 5% critical value of 11.07. The method line and the "How this was generated" steps say exactly how.
- **Seeds:** the same seed repeats exactly, a different seed differs, and unseeded draws differ. The warning says not to use a seed for raffles.
- **Edge cases get specific, helpful messages:**
  - 6 unique from 1–5.
  - Decimals typed in whole-number mode, with a hint to set Decimal places.
  - Swapped min/max is auto-fixed with a note.
  - 20,000 is capped to 10,000 with a note, and only the first 500 are shown, with "copy or download to get them all".
  - Huge BigInt ranges (±10^20) work.
  - "1,000"/"2_000" are accepted; text, empty and 0 are rejected.
  - Dice, coin, lottery and list limits each have a clear message.
- **Lottery odds are exact:** 6/49 is 1 in 13,983,816; 5/69 is 1 in 11,238,513.
- **List mode:** handles Unicode and emoji, warns about duplicate lines, and caps at 10,000 lines. 10,000 lines draw in under 0.1 s.
- **Copy and Download .txt** work in all three engines. Files hold one value per line; coin files add a Heads/Tails tally.

What undercuts it:
- **Old video:** it shows the old single-mode tool with "free uses" counters and overlapping captions.
- **Blog is behind the tool:** it says most tools don't expose seeds or decimals, and teaches a manual "without replacement" workflow the tool now does with one switch.
- **Locale pages:** English apart from the breadcrumb.
- **Small polish:** stale results, no live region.
- **No route onward:** the raffle use case isn't linked to Giveaway Winner Picker (backups, tickets, draw record).

## Why: what the evidence says

- **Policy question, trial uses (not on the Nov 20 list):**
  - gate.json: a 0/10 context stayed at 0/10 after Generate, Copy, Download and Copy again, with no usage POST (only funnel/insight analytics).
  - func.json: in all three engines at 10/10, Copy and Download worked with no dialog.
  - No trial strip anywhere (`trialText: []`).
- **P2, video out of date (check 12 FAIL):**
  - Old UI: breadcrumb "Converters & Calculators", "10 free uses daily", "8 free uses left today", "Search 200+ tools", Min/Max/How many plus No duplicates only. No modes, decimals, sort or seed.
  - Burned-in captions overlap the page's own help text, making both unreadable (hi30.png).
  - Recorder's Chrome is visible: profile avatar, "Ask Gemini", and an open Find bar.
  - Wording: end card "200+ Free Productivity Tools"; YouTube title "How to Use Random Number Generator – Free Step-by-Step Walkthrough"; description "Try … free / Free daily uses … no account needed"; tags include "free online tools" and "PDF tools".
  - The VideoObject name ("How to Generate Random Numbers Online No Duplicates") doesn't match the YouTube title.
- **P2, blog accuracy** (/blog/random-number-generator, updated Oct 15):
  - "If you only see integers, scale a larger integer range and divide offline." The tool has Decimal places 0–10.
  - "Most everyday UIs do not expose seeds." The tool has a seed.
  - The manual without-replacement workflow ("cross off winners… re-generate when a crossed number appears") is now one switch (No duplicates), or List mode.
  - No mention of the dice, coin, lottery or list modes.
  - The pricing line ("10 trial usages a day, then $1 day pass or $4.99 monthly" for file tools) is accurate as written.
- **P2, locales:**
  - es, pt, fr, de, ja, hi, zh, ko and id all return 200 with the correct `lang`.
  - H1 "Random Number Generator", the subtitle, the title, the meta and all labels (Numbers/Dice/…, Min, Max, Generate, Seed…) are English.
  - Only the breadcrumb and the "Files never stored" badge are translated (e.g. "Einheiten, Datum und Alltagsrechner", "Ihre Dateien werden niemals gespeichert").
  - /ar returns 404.
- **P3, stale result card under validation errors** (N03, D04–D06, C04–C05, L03–L05, N10 screenshots and JSON).
- **P3, a11y:**
  - No live region on results; Enter doesn't submit.
  - The switches are 32×18 px touch targets.
  - axe on desktop: label-content-name-mismatch (1), region (1). Pixel 7: none.
  - 17 Tabs to Generate.
- **P3, iPhone SE:** the page is 329 px on a 320 px viewport. The culprit is a header button, and the hamburger is clipped. This is site-wide, not this tool.
- **P3, copy and SEO:**
  - The "Files never stored" badge is odd on a tool with no files.
  - JSON-LD price 4.99 on a tool that is effectively uncounted.
  - og-default image. Title 59, meta 142 (good).
- **Note:** in one Chromium and one WebKit run, Playwright `fill()` of a 10,001-line list timed out. Setting the same text by input event took 13 ms, and Firefox `fill()` worked, so this is a test-harness artifact, not a site bug.
- **Share:** the icon and "Share this tool" copy the URL ("Link copied…"). Create Shortcut shows a clear "install not available yet" hint. The star gave no visible feedback (unverified whether it saves).
- **Geo:** all 6 contexts are English, with no prices on the page. The EU consent banner appears for de-DE and fr-FR only.

## Outcomes we want

1. The owner decides counted vs uncounted, and the FAQ, JSON-LD offer and trial strip agree with that decision.
2. A re-recorded video of all five modes, with no "free" wording and a clean browser profile.
3. The blog rewritten around No duplicates, List, Seed and Decimals.
4. Translated H1, subtitle and labels on locale pages.
5. Results cleared or dimmed when inputs are invalid, plus a live region and Enter-to-generate.
6. A "Running a raffle with names? Use Giveaway Winner Picker" link from List mode and the blog.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | 45/45 functional cases behave as designed in 3 engines; uniform; seed repeatable. |
| 2 | Completeness vs competitors | PASS (minor) | Matches or beats Google RNG, random.org basic, calculator.net: decimals, unique, dice, coin, lottery odds, list, seed, steps. Missing (verified in the control list): exclude numbers, weighted list entries, a draw record or shareable result link, a projector/fullscreen view. |
| 3 | Ease of use | PASS (minor) | Clear modes and errors; stale result under errors; Enter doesn't generate. |
| 4 | Layout attractiveness | PASS | Clean desktop and phone; big result chips; no overflow apart from the site-wide 9 px on iPhone SE. |
| 5 | Payment process | N/A | No pass offer on the page; tool uncounted (policy question). |
| 6 | Information correct | PARTIAL | FAQ and Details match behaviour; JSON-LD price 4.99 and the "with or without duplicates" description are out of date. |
| 7 | Indexing | PASS | 200, index, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title 59, meta 142, VideoObject + FAQPage (5); og-default; H1 not localized. |
| 9 | Blog exists and accurate | PARTIAL | One post; says seeds/decimals aren't available and teaches a manual no-repeat workflow. |
| 10 | YouTube video exists | PASS | buvkdsqCW5w embedded. |
| 11 | FAQ and guide correct | PASS | All 5 FAQs verified live (crypto + rejection sampling, decimals 1,001 values, modes, unique error, no trial use). |
| 12 | Video shows current capabilities | **FAIL** | Old single-mode UI, "free uses" counters, overlapping captions. |
| 13 | Storage | N/A | No save feature (by design); Download .txt works. |
| 14 | Sharing | PASS | Share icon / Share this tool copy the link. No result sharing (enhancement). |
| 15 | Downloads | PASS | .txt correct in 3 engines (10,000 lines; coin tally). |
| 16 | Usage count | POLICY QUESTION | Uncounted everywhere (0/10 stays 0/10; no dialog at 10/10); not on the Nov 20 list. |
| 17 | Categorization in section | PASS (minor) | Unit, Date & Everyday Calculators is acceptable; an "everyday picks" sub-group with Giveaway Winner Picker would help. |
| 18 | Correct section of site | PASS | Breadcrumb and category match. |
| 19 | AI need/demand | PASS | GA top traffic; a chat assistant can't give auditable crypto-random draws with copyable records. |
| 20 | Merge better? | No | Full-featured. |
| 21 | Remove? | No | Top traffic. |
| 22 | Duplicates | C45: keep both, cross-link | Giveaway Winner Picker adds backups, extra tickets and a draw record. List mode overlaps, but the audiences differ. |
