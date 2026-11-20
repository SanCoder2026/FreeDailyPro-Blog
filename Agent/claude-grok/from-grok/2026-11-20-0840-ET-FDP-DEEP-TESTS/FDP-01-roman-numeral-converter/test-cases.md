Sent: 2026-11-20 08:40 ET

# Test cases: Roman Numeral Converter

- **Tool:** https://www.freedailypro.com/tool/roman-numeral-converter
- **For:** Claude retest after a fix, and the browser tester's live pass
- **Written:** 2026-11-19 09:04:54 EST (America/New_York)
- **Source of expected results:** live `RomanNumeralConverter-CIvGjpT-.js` (fetched 2026-11-19) plus the SSR HTML. The 1–100 chart in that HTML was checked against the same algorithm (100/100 match).
- **How to run:** use a Guest or fresh temp Chrome profile only. Do not sign in, do not pay, do not submit payment fields, do not click ads. Open the English URL above unless a case says `/es` or the blog.
- **Vinculum:** a bar is Unicode combining overline U+0305 after each barred letter. 4,000 must look like I̅V̅ (I, U+0305, V, U+0305), not plain `IV` or four M's. Bracket input `(V)` is also accepted for 5,000.
- **Trial uses:** this is a Professional Tool. The English strip strings are `Trial: {limit} uses/day · {count} remaining today`. For a fresh guest the usual limit is 10. Use the numbers the strip actually shows if they differ. From the JS, typing a conversion should not spend a use; the first Copy / Copy table / Download CSV / Print or save as PDF of the visit should. Confirm that in the browser; do not assume a backend count.

Default date on load is today in Day.Month.Year with a dot. On 2026-11-19 the SSR HTML showed `XIX.XI.MMXXVI`. If the test is run on another day, expect that day's Roman date instead.

---

## RN-01 — 2026 to MMXXVI, with working

- **Purpose:** Core year example used in the title, FAQ and blog.
- **Input:** In "Number → Roman Numeral", type `2026`.
- **Steps:** Load the tool. Leave the Roman box alone. Read the result and the "How 2,026 is written" steps.
- **Expected:** Result `MMXXVI`. Steps show thousands 2,000 = MM, tens 20 = XX, ones 6 = VI, joined as MM + XX + VI = MMXXVI. No error.

## RN-02 — MMXXVI back to 2026, lowercase

- **Purpose:** Reverse direction and lowercase input.
- **Input:** In "Roman Numeral → Number", type `mmxxvi`.
- **Steps:** Load a clean page (or clear the Roman box). Type the lowercase letters only. Do not also depend on the number box (the two boxes work separately).
- **Expected:** Result `2026`. No error. Input is accepted in lowercase; output number is 2026.

## RN-03 — 1994 = MCMXCIV, subtractive pairs

- **Purpose:** Classic worked example (M + CM + XC + IV).
- **Input:** `1994` in the number box.
- **Steps:** Type 1994. Open or read the working.
- **Expected:** Result `MCMXCIV`. Working is M + CM + XC + IV. FAQ "How do you write 2026…?" is a different question; this case checks 1994 only.

## RN-04 — 3,999 is the largest plain numeral

- **Purpose:** Upper bound of letters without a bar.
- **Input:** `3999` and, separately, `3,999`.
- **Steps:** Type 3999. Then try the thousands-comma form `3,999`.
- **Expected:** Both give `MMMCMXCIX`. No vinculum note. No "limit" error.

## RN-05 — 4,000 uses a vinculum (I̅V̅), not an error

- **Purpose:** Regression against the old 1–3999 error and against the stale blog. Matches ledger L-012 / report #162.
- **Input:** `4000` in the number box.
- **Steps:** Type 4000. Read the result, any bar note, and the copyable text.
- **Expected:** Result is I̅V̅ (I and V, each with U+0305). A note that a bar multiplies by 1,000. It must **not** say the range is only 1 to 3999. Copied text should include the combining overline, not plain `IV`.

## RN-06 — 5,000 and bracket input `(V)`

- **Purpose:** Barred output and bracketed input, as the FAQ describes.
- **Input:** (a) `5000` in the number box. (b) `(V)` in the Roman box.
- **Steps:** Convert 5000 first. Then, separately, type `(V)` in "Roman Numeral → Number".
- **Expected:** (a) V̅ (V + U+0305). (b) `5000`, with a note that barred letters are multiplied by 1,000. FAQ example `(XII)CCCXLV` = 12,345 may be used as an optional extra: expected `12345`.

## RN-07 — 3,999,999 is accepted; 4,000,000 is rejected

- **Purpose:** Stated upper cap.
- **Input:** `3999999`, then `4000000`.
- **Steps:** Type each value in the number box.
- **Expected:** 3999999 returns a barred MMMCMXCIX followed by plain CMXCIX (M̅M̅M̅C̅M̅X̅C̅I̅X̅CMXCIX). 4000000 shows the error: `Roman numerals here go from 1 to 3,999,999: above 3,999 a bar over the letters multiplies by 1,000, and three barred M's is the limit.`

## RN-08 — 0 and negative numbers

- **Purpose:** There is no Roman zero.
- **Input:** `0`, then `-5`.
- **Steps:** Type each in the number box.
- **Expected:** Both show: `Roman numerals start at 1. There is no symbol for zero and no negative numbers.` No numeral result.

## RN-09 — Decimals

- **Purpose:** FAQ / blog claim that decimals are refused.
- **Input:** `2026.5`
- **Steps:** Type `2026.5` in the number box.
- **Expected:** `Roman numerals have no decimals. Use a whole number.`

## RN-10 — Empty number and empty Roman boxes

- **Purpose:** Empty input should not show a false error.
- **Input:** Clear both boxes (empty string).
- **Steps:** Load the page, delete any default in the number and Roman boxes (the date boxes may keep today).
- **Expected:** The number and Roman results are blank. No red error on those boxes. The date result may still show today's date.

## RN-11 — Whitespace and thousands separators on numbers

- **Purpose:** JS strips spaces and underscores, and accepts `1,234`-style commas.
- **Input:** ` 2026 `, then `2_026`, then `2,026`.
- **Steps:** Type each form in the number box.
- **Expected:** All three give `MMXXVI`.

## RN-12 — Invalid letters and internal spaces in a numeral

- **Purpose:** Letter whitelist; spaces inside a numeral are not stripped.
- **Input:** (a) `ABC`. (b) `MM XXVI` (space in the middle). (c) `  MMXXVI  ` (outer spaces only).
- **Steps:** Type each in the Roman box.
- **Expected:** (a) and (b): `Use only the letters I, V, X, L, C, D and M.` (c): `2026`, because `P()` trims then uppercases.

## RN-13 — Invalid forms: IIII, VX, IC, MMMM, IIX

- **Purpose:** Clock-face exception, subtractive-rule hints, four M's, and the IIX suggestion described in the blog (the suggestion itself is still how the live JS behaves).
- **Input:** In the Roman box, separately: `IIII`, `VX`, `IC`, `MMMM`, `IIX`.
- **Steps:** Type each form. Read the result or the red message.
- **Expected:**
  - `IIII` → value `4`, plus `IIII is the clock-face way of writing 4 (the standard form is IV).` (XIIII, if tried, should be 14 with the same kind of note.)
  - `VX` → not valid, with a hint that includes V (5). Message includes that only I before V or X, X before L or C, and C before D or M can be subtracted, or a "Did you mean V (5)?" line.
  - `IC` → not valid, suggestion `XCIX (99)`.
  - `MMMM` → `Four M in a row would be 4,000; plain letters stop at 3,999, so write thousands above that with a bar.`
  - `IIX` → not valid, "Did you mean X (10)?" The standard form of 8 is VIII; the hint reflects left-to-right parsing, not an auto-correction to 8.

## RN-14 — Very long input

- **Purpose:** No hang, clear error, no crash.
- **Input:** (a) a 200-character string of `9`. (b) a 200-character string of `M`.
- **Steps:** Paste each into the matching box. Wait for the UI to settle. Do not run any generated or pasted shell command; this is only text in the web form.
- **Expected:** The page stays usable. (a) is far above 3,999,999, so the same over-limit error as RN-07. (b) is not a valid standard numeral (more than three M's); expect the four-M / bar message or a general "Not a valid Roman numeral" message, not a blank freeze.

## RN-15 — Date mode, both orders and a tattoo separator

- **Purpose:** Date conversion, US order, and a non-dot separator. Also checks the 4 July labelling bug: the **tool output** must be correct even if the H2 text is wrong.
- **Input:** Day 4, month 7, year 1776.
- **Steps:** Set Day.Month.Year and separator "dot .". Read the result. Switch to Month.Day.Year (US). Read again. Switch the separator to middle dot `·`.
- **Expected:** DMY + dot → `IV.VII.MDCCLXXVI`. MDY + dot → `VII.IV.MDCCLXXVI`. MDY + middle dot → `VII·IV·MDCCLXXVI`. Optional check: day 14, month 6, year 2026, DMY + dot → `XIV.VI.MMXXVI`.

## RN-16 — Invalid calendar dates

- **Purpose:** Regression for L-010. Blog claim that each box accepts 1–3999 is wrong; the tool must reject impossible dates.
- **Input:** (a) day 30, month 2, year 2026. (b) day 31, month 4, year 2026. (c) month 13, day 1, year 2026. (d) year 4000, day 1, month 1.
- **Steps:** Enter each combination in the date boxes.
- **Expected:** (a) and (b): `That date does not exist in the calendar.` (c): `Month must be between 1 and 12.` (d): `Year must be between 1 and 3999.` No Roman date result. Optional leap-year check: 29 Feb 2024 is valid (`XXIX.II.MMXXIV` in DMY); 29 Feb 1900 is not a calendar date.

## RN-17 — 1–100 chart accuracy (spot checks plus 4, 9, 49, 99)

- **Purpose:** Visible reference table must use standard forms.
- **Input:** None (read the "1 to 100" table). Optionally switch to "Years 1950 to 2050".
- **Steps:** Open the tool, leave the 1–100 tab selected, and check the rows below. Then open Years 1950 to 2050.
- **Expected:** 1=I, 4=IV (not IIII), 9=IX, 14=XIV, 40=XL, 44=XLIV, 49=XLIX (not IL), 90=XC, 99=XCIX (not IC), 100=C. Years: 1950=MCML, 1994=MCMXCIV, 2000=MM, 2026=MMXXVI, 2050=MML.

## RN-18 — Copy / download spends one trial use; typing should not

- **Purpose:** Usage-count case. FAQ: copying or downloading the table uses one trial use for the visit. JS: copy and table export call the usage gate; typing only updates session history.
- **Input:** `2026` in the number box, then Copy Roman numeral (or Copy table / Download CSV if you are testing the table).
- **Steps:** Fresh guest profile, unused Professional pool. Load the tool and read the strip **before** any copy or download. Type `2026` and wait a few seconds. Read the strip again. Click **Copy Roman numeral**. Read the strip a third time. Stop. Do not open checkout or enter a card.
- **Expected:**
  - On load (typical unused guest): `Trial: 10 uses/day · 10 remaining today` plus the $1 day pass and $4.99 monthly pass labels ("Ads-free unlimited usage, $1 day pass" and "Ads-free unlimited usage, $4.99 monthly pass" on desktop). If the strip already shows a lower remaining count, use that as the baseline and expect a decrease of one after the first export only.
  - After typing 2026 only: remaining count **unchanged**.
  - After the first successful Copy (or first table Copy / Download CSV / Print): remaining count decreases by 1, e.g. `Trial: 10 uses/day · 9 remaining today`.
  - A toast "Copied!" may appear. If trial uses are already exhausted, the blocked note is: `Today's trial uses are used up, so … was not done. Your input is still here and nothing was lost. Trial uses start again at midnight UTC, or see the pass options.`

## RN-19 — Title, meta and H1

- **Purpose:** SEO metadata case (B-0210-v2).
- **Input:** None. View-source or curl the English tool URL.
- **Steps:** GET https://www.freedailypro.com/tool/roman-numeral-converter. Read `<title>`, `meta name="description"`, and the visible `<h1>`. Count characters after HTML entity decode (`&amp;` → `&`).
- **Expected:**
  - Title: `Roman Numeral Converter – Years & Dates (2026 = MMXXVI)` (55 characters).
  - Meta includes `1994 = M + CM + XC + IV` and is in the 140–160 range (live length on 2026-11-19: 158).
  - H1: `Roman Numeral Converter — Numbers, Years and Dates`.
  - No robots `noindex`.

## RN-20 — Canonical, hreflang and JSON-LD

- **Purpose:** Indexing and structured data.
- **Input:** None. View-source or curl the English tool URL, and curl `/es/tool/roman-numeral-converter`.
- **Steps:** Confirm the tags below in the server HTML (do not rely only on a hydrated DOM if it duplicates blocks).
- **Expected:**
  - English canonical: `https://www.freedailypro.com/tool/roman-numeral-converter`.
  - Eleven `hreflang` alternates: en, es, pt, fr, de, ja, hi, zh, ko, id, x-default. x-default and en point at the English tool URL; es points at `https://www.freedailypro.com/es/tool/roman-numeral-converter`.
  - `/es` has `html lang="es"` and a self canonical on the `/es/` URL.
  - JSON-LD types present and valid JSON: WebSite, SoftwareApplication, VideoObject, FAQPage, BreadcrumbList. FAQPage has 11 questions and includes "How do you write 2026 in Roman numerals?" with answer MMXXVI. VideoObject `contentUrl` is `https://www.youtube.com/watch?v=Jrmgcqn_jJw`. (A known defect: VideoObject `name` may not match the live YouTube title; record whatever is live, do not "fix" it in the test.)

## RN-21 — Blog still describes the live tool (currently expected to FAIL)

- **Purpose:** Catch the stale blog before it is updated, and confirm the fix after Claude edits it.
- **Input:** None. Open https://www.freedailypro.com/blog/roman-numeral-converter.
- **Steps:** Confirm the post links to `/tool/roman-numeral-converter`. Read the error-message section and "Where this tool stops".
- **Expected after a fix:** The post still links to the tool. It must not say that 4,000 is rejected, that the range stops at 3,999 with no overline, or that date boxes accept 1–3999 in each field with no other layouts. It should describe vinculum to 3,999,999, calendar-valid dates, and the separator / US-order controls. Until that ships, this case is a **known fail** (see desk-findings check 9).

## RN-22 — On-page date copy does not swap 4 July (currently expected to FAIL)

- **Purpose:** The unlabelled US-order example in "Dates in Roman numerals (wedding, tattoo)".
- **Input:** None. Read that H2 on the tool page.
- **Steps:** Find the sentence about 4 July 1776. Compare it with RN-15's DMY result.
- **Expected after a fix:** The sentence labels both orders, e.g. "4 July 1776 is IV.VII.MDCCLXXVI (day.month.year), or VII.IV.MDCCLXXVI in US order." Until that ships, the live sentence "4 July 1776 is VII.IV.MDCCLXXVI" is a **known fail**.

## RN-23 — Session history, not server storage

- **Purpose:** Storage claim.
- **Input:** Convert `2026`, wait one second, then convert `1994`.
- **Steps:** After both conversions, look for "Recent calculations". Reload the page.
- **Expected:** While the page stays open, history can show both (e.g. `2,026 = MMXXVI` and `1,994 = MCMXCIV`), with the note "Kept only while this page is open. Nothing is saved on our servers or in your browser." After a full reload, that list is gone. No sign-in or cloud save is required for this tool.

---

## Suggested later cases (not required for this pack)

- `/es` conversion of 2026 still yields MMXXVI (same engine, Spanish chrome).
- Print/PDF and CSV of the 1–100 table open or download without a JS error (first export may spend a trial use; see RN-18).
- YouTube embed plays after a click (embedding must be allowed). Watching the clip to compare it with date mode and vinculum is a human/browser step, not a curl case.

---

## Device, platform and locale cases (added 2026-11-19, devices-locales-findings.md)

Run them all automatically with `node /workspace/deep/tools-env/run-matrix.js /workspace/deep/01-roman-numeral-converter/devices/config.json`, or one at a time as below. Do not click Copy, Download, pass or checkout buttons, and do not click ads.

## RN-24 — Conversion works on every engine and device

- **Purpose:** Cross-platform functional check.
- **Input:** `1994`, then `2026` in Number; `MCMXCIV`, then `MMXXVI` in Roman numeral.
- **Steps:** Use the Playwright descriptors iPhone SE, iPhone 14 Pro Max, iPad Mini and iPad Pro 11 landscape (WebKit); Pixel 7 and Galaxy S9+ (Chromium); desktop 1366×768 and 1920×1080 (Chromium); and 1440×900 on both Firefox and WebKit. Load the page and wait for network idle plus 3 s. Type each value with key presses and read the result card under the box.
- **Expected:** The cards show MCMXCIV, MMXXVI, 1,994 and 2,026 on all 10 profiles. No first-party console error. (Result on 2026-11-19: PASS 10/10.)

## RN-25 — No horizontal overflow at 320 px (currently expected to FAIL)

- **Purpose:** Small-phone layout (finding D2).
- **Input:** None.
- **Steps:** Load with `devices['iPhone SE']` (WebKit) and `devices['Galaxy S9+']` (Chromium). Evaluate `document.documentElement.scrollWidth` and `innerWidth`.
- **Expected after a fix:** scrollWidth = innerWidth = 320, and the header menu icon is fully visible. Live on 2026-11-19: 329 (the header's right-most icon button overflows by 9 px). The 1–100 chart table is allowed to scroll inside its own `overflow-x-auto` box.

## RN-26 — Touch targets at least 44×44 on phones and tablets (currently expected to FAIL on tablets)

- **Purpose:** Tap-target size (D3, D7).
- **Input:** None.
- **Steps:** With `devices['iPad Mini']`, then `devices['Pixel 7']`, measure the bounding boxes of the Copy Roman numeral, Copy number, Copy date, Add to favorites, Share this tool and Clear buttons.
- **Expected after a fix:** Every one is at least 44×44 CSS px on touch devices. Live on 2026-11-19: Pixel 7 copy buttons were 44×44 (pass). iPad copy buttons were 28×28, title icons 16×16, and Clear 30×16 on all devices.

## RN-27 — iOS does not zoom on focus (input font ≥ 16 px)

- **Purpose:** iOS auto-zoom (D4).
- **Input:** None.
- **Steps:** With `devices['iPhone SE']` and `devices['iPad Mini']` (WebKit), read `getComputedStyle(el).fontSize` for the Number, Roman numeral, Day, Month and Year inputs and the Separator select. On a real iPad, tap the Number box.
- **Expected:** 16 px or more on every touch profile, and no zoom on a real iPad. Live on 2026-11-19: iPhone 16 px (pass), iPad 14 px (fail).

## RN-28 — Ads never overlap the tool and do not shift it

- **Purpose:** Ad placement (reserved slots) and CLS.
- **Input:** Type `2026` once after load.
- **Steps:** On Pixel 7 and desktop 1440×900, collect the boxes of `ins.adsbygoogle`, `.ad-container` and `iframe[id^=aswift]`, and of the inputs, copy buttons and result cards, before and after typing. Read a buffered `PerformanceObserver({type:'layout-shift'})` total in Chromium.
- **Expected:** No ad box intersects any control or result. Chromium CLS stays under 0.1 (live: 0). Ads sit only in reserved slots: in-content after the chart, and side rails outside the 147–1293 px tool column at 1440. Do not click any ad.

## RN-29 — Language versions are really translated (currently expected to FAIL)

- **Purpose:** hreflang quality (D1, D6).
- **Input:** None.
- **Steps:** For each hreflang alternate (es, pt, fr, de, ja, hi, zh, ko, id), GET the page. Check the status, `html lang`, `<title>`, meta description, H1, the visible FAQ questions, the H2s, and the labels "Copy table", "Separator" and "Day.Month.Year".
- **Expected after a fix:** 200, the correct `lang`, `dir="ltr"`, and title, meta, H1, H2s, FAQ and UI labels in that language. Numbers use local grouping (de 3.999.999, fr 3 999 999). No "free/gratis/gratuit/kostenlos" wording. Live on 2026-11-19: only `/es` has a translated title, meta, H1 and FAQ. Every locale has English UI labels and H2s, and pt through id are English apart from the nav.

## RN-30 — Date order follows the visitor's locale

- **Purpose:** Locale date conventions (D5).
- **Input:** Default date (today).
- **Steps:** Open the English URL in contexts `en-US` (America/New_York), `de-DE` (Europe/Berlin) and `ja-JP` (Asia/Tokyo), and open `/ja/tool/roman-numeral-converter`. Read which order radio is checked and the date result.
- **Expected after a fix:** en-US defaults to Month.Day.Year (US). de defaults to Day.Month.Year. ja, zh and ko offer, and default to, Year.Month.Day (e.g. MMXXVI.XI.XIX). Live on 2026-11-19: Day.Month.Year in every context, and there is no Y.M.D option.

## RN-31 — EU visitors get cookie consent; others are unaffected

- **Purpose:** Consent banner by region.
- **Input:** None.
- **Steps:** Open the English URL in a fresh context with `locale: 'de-DE'`, `timezoneId: 'Europe/Berlin'` and `Accept-Language: de-DE`. Repeat with `en-US` / America/New_York. Ideally also from a real EU IP, capturing network requests to `googlesyndication` / `doubleclick` before any choice.
- **Expected:** EU shows "We use cookies for analytics and, when ads are shown, advertising…" with Accept all, Reject non-essential and Choose. US shows no banner. No redirect to `/de/`. With a real EU IP, no personalised ad requests fire before Accept (not verified on 2026-11-19, since the box IP is in the US). Do not click Accept or ads during the test, other than reading the banner.

## RN-32 — Accessibility smoke (axe-core)

- **Purpose:** a11y regression guard.
- **Input:** None.
- **Steps:** On desktop 1366×768 and Pixel 7 (Chromium), inject `axe-core` and run `axe.run` with the tags wcag2a, wcag2aa, wcag21a, wcag21aa and best-practice.
- **Expected:** No critical or serious violations. Live on 2026-11-19: desktop had `label-content-name-mismatch` (serious, 1 header control) and `region` (moderate, 1). Pixel 7 had 0.

---

## Step A cases (added 2026-11-19 09:45:06 EST, edge-usage-findings.md)

Live status of the earlier cases on 2026-11-19:
- **RN-18** FAILS live: Copy, Download CSV and Print left `usageToday` at 0, and no strip rendered. See RN-35.
- **RN-15** passes only if the boxes are filled in DOM order (Day box first) in both modes. See RN-33.

## RN-33 — US order: the boxes follow the heading (currently expected to FAIL)

- **Purpose:** The Month.Day.Year (US) input bug.
- **Input:** Select Month.Day.Year (US). Type `11` in the first date box, `19` in the second and `2026` in the third. Then type `7`, `4`, `1776`.
- **Steps:** Read the heading, the result and any error after each set. Also read each box's aria-label and visible label.
- **Expected after a fix:** The heading "(month, day, year)" matches the box order, or the boxes have visible labels that move with the mode. 11/19/2026 gives `XI.XIX.MMXXVI`. 7/4/1776 gives `VII.IV.MDCCLXXVI`, which matches the FAQ "7.4.1776 becomes VII.IV.MDCCLXXVI".
- **Live 2026-11-19:**
  - 11/19/2026 gives "—" and "Month must be between 1 and 12."
  - 7/4/1776 gives `IV.VII.MDCCLXXVI` (it is read as 7 April).
  - The boxes stay aria Day / Month / Year with no visible labels.

## RN-34 — Edge inputs, verbatim messages

- **Purpose:** Regression guard for range, error and hint copy.
- **Input / Expected (Number box):**
  - `4000` → barred I̅V̅
  - `3999999` → M̅M̅M̅C̅M̅X̅C̅I̅X̅CMXCIX
  - `4000000` → "Roman numerals here go from 1 to 3,999,999: above 3,999 a bar over the letters multiplies by 1,000, and three barred M's is the limit."
  - `0` and `-5` → "Roman numerals start at 1. There is no symbol for zero and no negative numbers."
  - `12.5` → "Roman numerals have no decimals. Use a whole number."
  - letters → "Enter a whole number from 1 to 3,999,999."
- **Input / Expected (Roman box):**
  - `mmxxvi` → 2026
  - ` XIV ` → 14
  - `IIII` → 4 with the clock-face note
  - `VX` → "…Did you mean V (5)?"
  - `MMMM` → "Not a valid Roman numeral. Four M in a row would be 4,000…"
  - `IIX` → "Did you mean X (10)?"
  - `IC` → "Did you mean XCIX (99)?"
  - `(V)` → 5000
  - `(XII)CCCXLV` → 12345
  - `I̅V̅` → 4000
  - digits or `ABC` → "Use only the letters I, V, X, L, C, D and M."
- **Steps:** Run `scripts/edge-usage.js` and compare `edgeNumber` / `edgeRoman` in the JSON.
- **Live 2026-11-19:** all as listed (PASS).

## RN-35 — Trial uses are spent by Copy / CSV / Print / Copy table (currently expected to FAIL)

- **Purpose:** Monetization policy. Copy and results count against trial uses, as the page FAQ says.
- **Input:** A fresh guest context.
- **Steps:**
  1. Read the strip and `localStorage['fdp-usage-v1']` at load.
  2. Type 1994 and read again.
  3. Click Copy Roman numeral and read again.
  4. Click Download CSV and read again.
  5. Click Print or save as PDF (stub `window.print`) and read again.
  6. Reload and read again.
  7. Repeat everything in a second fresh context.
- **Expected after a fix:** The strip "Trial: 10 uses/day · N remaining today" is visible on load (or at least after the first counted action), and it shows the pass options. Typing does not decrease it. The first Copy or export of the visit decreases it by 1, following the owner's visit rule. After a reload the stored and displayed counts agree.
- **Live 2026-11-19:** no strip at any step, `usageToday` 0 throughout, in both contexts.

## RN-36 — Copy table copies only the table (currently expected to FAIL)

- **Purpose:** Clean paste into Sheets or Docs.
- **Input:** The "1 to 100" tab, then "Years 1950 to 2050".
- **Steps:** Click Copy table and read the clipboard (`scripts/edge-copy-table-probe.js`).
- **Expected after a fix:** The clipboard is the title (optional) plus a tab-separated `Number\tRoman numeral` table only.
- **Live 2026-11-19:** a "Working for 2,026 … Result: MMXXVI" block is inserted before the table.

## RN-37 — Share carries the conversion (enhancement, currently expected to FAIL)

- **Purpose:** Sharing a result.
- **Input:** Type 1994, then click the in-page "Share this tool".
- **Steps:** Read the clipboard, or the native share payload on mobile. Open the link in a new fresh context.
- **Expected after enhancement:** A link such as `?n=1994` opens with 1994 / MCMXCIV filled in.
- **Live 2026-11-19:** the clipboard holds the bare tool URL, so the value is lost.
