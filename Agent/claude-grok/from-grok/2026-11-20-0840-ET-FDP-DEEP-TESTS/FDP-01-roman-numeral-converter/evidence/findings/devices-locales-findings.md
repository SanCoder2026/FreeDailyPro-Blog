Sent: 2026-11-20 08:40 ET

# Roman Numeral Converter: device, platform and locale findings

- **Tool:** https://www.freedailypro.com/tool/roman-numeral-converter
- **Runs (box `date`, ET):**
  - Devices: 2026-11-19 09:28:05 to 09:30:54 EST. iPhone 14 Pro Max was rerun at about 09:33 EST.
  - Locales, geo and a11y: 09:30:58 to 09:35:57 EST.
- **Method:** Playwright 1.65.1 headless, with Chromium 159, Firefox 159 and WebKit 27.2 (WPE). Device descriptors set the real UA, viewport, DPR, touch and isMobile.
  - The script only loaded pages, typed into inputs and read results.
  - It made no Copy, Download, Share, pass or checkout clicks, clicked no ads and did not sign in.
- **Rerun:** `node /workspace/deep/tools-env/run-matrix.js devices/config.json`. The script is also saved as `devices/run-matrix.js`.
- **Raw data:**
  - `matrix-results-devices.json`
  - `matrix-results-devices-iphone-14-pro-max.json`
  - `matrix-results-locales-geo-a11y.json`
- **Screenshots:** `devices/`, `locales/`, `geo/` and `a11y/`. Each folder has `*-fold.png` and `*-full.png`.
- **Limits:**
  - This is emulation on Linux engines, not real iOS Safari or Android hardware.
  - CLS is measured only in Chromium. Firefox and WebKit do not support `layout-shift`, so their "0" in the raw JSON from this run is not a measurement. It is shown as n/a below.
  - Geo contexts change locale, timezone, geolocation and Accept-Language. The egress IP stayed in the US.

## 1. Device and platform matrix

Fold = visible in the first viewport without scrolling. Tap targets list only items under 44×44 CSS px inside the tool (header and footer excluded).

| Device (engine) | Viewport | H-overflow | Input font | Fold: input / result / trial strip | Ad overlap on controls | Sticky/fixed covering | CLS | Console errors | 2026→MMXXVI, MMXXVI→2026, 1994↔MCMXCIV |
|---|---|---|---|---|---|---|---|---|---|
| iPhone SE (WebKit) | 320×568 @2 | **FAIL**: scrollWidth 329 > 320 (header icon button right edge 329) | 16px PASS | input PASS (y 500); result **FAIL** (top at y 565 of 568); strip absent | PASS (none) | Sticky header 66px; Feedback FAB 36×32 | n/a | none | PASS (4/4) |
| iPhone 14 Pro Max (WebKit) | 430×740 @3 | PASS | 16px PASS | PASS / PASS / absent | PASS | Header 66px; FAB | n/a | none | PASS (4/4). First attempt "Page crashed" in headless WebKit; rerun clean |
| Pixel 7 (Chromium) | 412×839 @2.6 | PASS | 16px PASS | PASS / PASS / absent | PASS | Header 66px; FAB | 0 | AdSense `no_div` | PASS (4/4) |
| Galaxy S9+ (Chromium) | 320×658 → layout width **329** | **FAIL**: innerWidth became 329 on a 320 device (page zoomed out to fit the same 9px header overflow) | 16px PASS | PASS / PASS / absent | PASS | Header; FAB | 0 | AdSense `no_div` | PASS (4/4) |
| iPad Mini (WebKit) | 768×1024 @2 | PASS | **14px FAIL** (iOS zooms below 16) | PASS / PASS / absent | PASS | FAB 110×40 sits over the chart's 4th column (bottom-right) | n/a | none | PASS (4/4) |
| iPad Pro 11 landscape (WebKit) | 1194×834 @2 | PASS | **14px FAIL** | PASS / PASS / absent | PASS | FAB | n/a | none | PASS (4/4) |
| Desktop 1366×768 (Chromium) | 1366×768 | PASS | 14px (desktop, OK) | PASS / PASS / absent | PASS (no ads filled this run) | Header; FAB | 0 | none | PASS (4/4) |
| Desktop 1920×1080 (Chromium) | 1920×1080 | PASS | 14px | PASS / PASS / absent | PASS | Header; FAB | 0 | AdSense `no_div` | PASS (4/4) |
| Desktop 1440×900 (Firefox) | 1440×900 | PASS | 14px | PASS / PASS / absent | PASS: right rail at x 1280–1440, Google side-rail at x 15–135; tool card starts x 147 | Sticky right-rail ad (top-24); header; FAB | n/a | none | PASS (4/4) |
| Desktop 1440×900 (WebKit) | 1440×900 | PASS | 14px | PASS / PASS / absent | PASS (same rails) | Same | n/a | doubleclick cross-origin frame access error (third party) | PASS (4/4) |

**Tap targets under 44×44 (touch devices):**

| Element | Phones (iPhone SE / 14 Pro Max / Pixel 7 / S9+) | Tablets (iPad Mini / iPad Pro 11) |
|---|---|---|
| Copy Roman numeral / Copy number / Copy date | 44×44 PASS | **28×28 FAIL** |
| Add to favorites / Share / Add to Home Screen (title icons) | not in tool area on phones (moved) | **16×16 FAIL** |
| Day.Month.Year / Month.Day.Year radios | 24×24 (the label wraps the radio, so the text is also tappable) | **12×12** (label wraps it) |
| Separator select | 129–133×32–40 (height under 44) | 122×37 |
| 1 to 100 / Years 1950 to 2050 / Copy table / Download CSV / Print or save as PDF / Share this tool | height 32 FAIL | height 32 FAIL |
| **Clear** (history) | **30×16 FAIL** | **30×16 FAIL** |
| Number / Roman / Day / Month / Year inputs | height 36 (width fine) | height 36 |

**Ad slots:**
- Phones: in-content ad containers start well below the tool, around y 3,100 to 3,560 depending on device. That puts them after the chart, with 3 or 4 slots down the page.
- Tablets: the first slot is at about y 2,470 to 2,545.
- Desktop 1440: a 160×600 sticky right rail at x 1280, a Google side-rail at x 15, and in-content slots at about y 2,450, 3,690 and 4,510.
- No ad box intersected any input, copy button or result on any device, before or after typing. Fill varies by run: 1366 had no fill this time.

**Trial strip:** No "uses/day / remaining today" strip or pass labels were visible on first load in any of the 10 fresh contexts. localStorage `fdp-usage-v1` read `usageToday:0, limit:10, tier:"professional"` (display-only evidence). This matches QA445's "strip appears only after the first counted use". The desktop tester owns counting. This note only covers visibility.

## 2. Locale and language

hreflang lists en, es, pt, fr, de, ja, hi, zh, ko, id and x-default. **There is no `ar` (Arabic) alternate.** `/ar/tool/roman-numeral-converter` returns **404**, so there is no RTL page to test.

| Locale | HTTP | html lang / dir | Title / H1 / meta translated? | Visible FAQ | UI labels (inputs, radios, buttons, H2s) | "free"-type words | Prices shown | Date-order default | Numbers |
|---|---|---|---|---|---|---|---|---|---|
| en | 200 | en / ltr | n/a | EN | EN | none | none (no strip) | **Day.Month.Year** checked | 3,999,999 / 2,026 |
| es | 200 | es / ltr | **Yes**: "Convertidor de números romanos: años y fechas, 2026 = MMXXVI" | **Spanish** (JSON-LD and visible) | **English** (e.g. "Copy table", "Separator", "Day.Month.Year", H2 "How to convert a number to Roman numerals") | none | none | D.M.Y | 3,999,999 (EN format) |
| pt | 200 | pt / ltr | **No**: English title, meta and short H1 "Roman Numeral Converter" | EN | EN; only nav chrome is translated ("Para o seu Trabalho") | none | none | D.M.Y | EN format |
| fr | 200 | fr / ltr | **No** | EN | EN; nav "Pour votre Travail" | none | none | D.M.Y | EN format (fr expects 3 999 999) |
| de | 200 | de / ltr | **No** | EN | EN; nav "Für Ihre Arbeit" | none | none | D.M.Y | EN format (de expects 3.999.999) |
| ja | 200 | ja / ltr | **No** | EN | EN; breadcrumb "単位・日付・日常の計算ツール" and badge "ファイルは保存されません" translated, "Runs on your device" not | none | none | D.M.Y (ja convention is Y.M.D, not offered) | EN format |
| hi | 200 | hi / ltr | **No** | EN | EN; nav "आपके काम के लिए" | none | none | D.M.Y (matches IN convention) | EN format (IN uses 39,99,999) |
| zh | 200 | zh / ltr | **No** | EN | EN | none | none | D.M.Y (zh convention Y.M.D, not offered) | EN format |
| ko | 200 | ko / ltr | **No** | EN | EN | none | none | D.M.Y (ko convention Y.M.D, not offered) | EN format |
| id | 200 | id / ltr | **No** | EN | EN; nav "Untuk Pekerjaan Anda" | none | none | D.M.Y (matches) | EN format |
| ar (probe) | **404** | en / ltr | "Page Not Found" | n/a | n/a | n/a | n/a | n/a | n/a |

- **Mobile (Pixel 7):** no horizontal overflow in any locale. Long localized breadcrumbs (ja) wrap cleanly. The tool itself is identical in every locale; the conversion engine is locale-independent.
- **Canonicals:** each locale self-canonicalizes to its own `/xx/` URL.
- **Date mode:** the order is always Day.Month.Year by default, **regardless of locale or timezone, including en-US**. Year.Month.Day is not offered at all. This matters for Japan, China and Korea, and for ISO-style dates.

**Accept-Language + timezone + geolocation on the English URL** (Desktop 1366, Chromium):

| Context | Redirect | html lang | Prices/currency | Consent banner | Date default |
|---|---|---|---|---|---|
| en-US, America/New_York | none (200) | en | none shown | **none** | D.M.Y |
| de-DE, Europe/Berlin | none, stays on `/tool/` (no auto `/de/`) | en | none shown | **Shown**: "We use cookies for analytics and, when ads are shown, advertising. The tools work either way. Privacy", with **Accept all / Reject non-essential / Choose** | D.M.Y |
| fr-FR, Europe/Paris | none | en | none | **Shown** (same) | D.M.Y |
| hi-IN, Asia/Kolkata | none | en | none | none | D.M.Y |
| ar-SA, Asia/Riyadh | none | en | none | none | D.M.Y |
| ja-JP, Asia/Tokyo | none | en | none | none | D.M.Y |

- The consent banner appears for EU timezones even though the box IP is in the US, so the trigger is client-side (timezone or locale).
- Real EU-IP behaviour, and whether ad requests wait for consent, were **not tested**. That needs an EU egress or a network capture.
- No prices appear on first load in any context. That is consistent with the trial strip being absent until the first counted use. Pricing-page currency was not in scope for this tool page.

## 3. Accessibility quick pass (axe-core 4.14.1; wcag2a/aa, wcag21a/aa, best-practice)

| Run | Violations |
|---|---|
| Desktop 1366×768 Chromium | `label-content-name-mismatch`: serious, 1 node (`.sm:flex`, a header control whose aria-label does not contain its visible text). `region`: moderate, 1 node (`.hover:opacity-90`, content outside a landmark, likely the Feedback FAB). |
| Pixel 7 Chromium | **0 violations** |

The axe run found no colour-contrast, label or button-name violations in the tool area.

## 4. Issues

| # | Severity | Issue | Repro |
|---|---|---|---|
| D1 | **HIGH** (SEO, site-wide pattern) | hreflang declares 9 language alternates, but 8 of them (pt, fr, de, ja, hi, zh, ko, id) serve the **English** title, meta description, H1, H2s, FAQ and tool UI. Only nav chrome is translated. Even `/es/` has English UI labels and H2s. Google may treat these as duplicates or ignore the hreflang cluster. | `curl -s https://www.freedailypro.com/de/tool/roman-numeral-converter \| grep -o '<title>[^<]*'` → English title. Open in a browser: labels "Copy table", "Separator", "Day.Month.Year" are English. |
| D2 | MEDIUM | The header overflows by 9px at 320px width. iPhone SE gets a horizontal scroll, and Galaxy S9+ Chrome widens the layout to 329 and zooms out. The culprit is the right-most header icon button (`div.flex.items-center.gap-1.sm:gap-3` in `div.container`). | Playwright `devices['iPhone SE']` on WebKit (or any 320px viewport), then `document.documentElement.scrollWidth` → 329. Screenshot `devices/iphone-se-fold.png`: the menu icon is clipped. |
| D3 | MEDIUM | On tablets (touch, ≥ sm breakpoint) the copy buttons are 28×28, and the favorite / share / Add to Home Screen icons are 16×16. Both are well under 44×44. Phones get 44×44 copy buttons. | `devices['iPad Mini']`, then measure `button[aria-label="Copy Roman numeral"]` → 28×28 and `button[aria-label="Add to favorites"]` → 16×16. |
| D4 | MEDIUM | Input font-size is 14px at ≥ sm breakpoints, so iPad Safari zooms on focus of the Number, Roman, Day, Month and Year boxes. Phones use 16px. Needs confirmation on a real iPad, since emulated WebKit does not zoom. | `devices['iPad Mini']`, then `getComputedStyle(input[aria-label=Number]).fontSize` → 14px. |
| D5 | MEDIUM | Date order defaults to Day.Month.Year for every locale, including en-US. There is no Year.Month.Day option for ja, zh or ko (or ISO). | Load the page with context `locale: 'en-US'` (or `/ja/…`). "Day.Month.Year" is checked, and the result shows XIX.XI.MMXXVI. Suggestion: default from `navigator.language` (US → M.D.Y; ja, zh, ko → Y.M.D) and add Y.M.D. |
| D6 | LOW | Number formatting is English everywhere: placeholder "1 to 3,999,999", "How 2,026 is written". de, fr, es, pt and id readers expect 3.999.999 or 3 999 999, and hi expects 39,99,999. | Open `/de/tool/roman-numeral-converter` and read the placeholder. |
| D7 | LOW | "Clear" (history) is a 30×16 text button on all devices. Tab and table action buttons are 32px tall (under 44) on touch. | Measure `button` with text "Clear" (after one conversion shows history). |
| D8 | LOW | On iPhone SE the first result box starts at y 565 of a 568px viewport, so a user sees the input but not the answer without scrolling. Cause: the 6-line H1 and the badges. | Screenshot `devices/iphone-se-fold.png`. |
| D9 | LOW | No trial strip and no pass/upgrade labels appear on first load in fresh contexts. The upgrade path is invisible until after the first counted use. (Display-only; counting is the desktop tester's area.) | Open a fresh context and search the page text for "uses/day" or "remaining today" → no match. localStorage shows `usageToday:0, limit:10`. |
| D10 | LOW | The Feedback FAB (fixed bottom-right, 110×40 on tablet and desktop) covers part of the 4th chart column ("LXX…") at the bottom of the viewport on iPad Mini. | `devices/ipad-mini-fold.png`, bottom-right. |
| D11 | LOW (verify on real Safari) | In WebKit (WPE) the Separator `<select>` renders as a white box with near-invisible light text in dark mode, and the unchecked radio renders as a filled white dot, which reads as "selected". Firefox and Chromium render both correctly. | `devices/desktop-1440x900-webkit-fold.png` and `devices/ipad-mini-fold.png`. Suggest setting `color-scheme: dark` and explicit `select` background/colour, and `appearance` on radios. |
| D12 | LOW | axe flags `label-content-name-mismatch` (serious, 1, a header control) and `region` (moderate, 1). | Inject axe-core on Desktop 1366 → `axe.run()`. |
| D13 | LOW (third-party) | Console errors: AdSense `Error: no_div` (an `ins.adsbygoogle` pushed with no matching slot) on Pixel 7, S9+, 1920 and en/ar loads; a doubleclick cross-origin frame error in WebKit; "Permissions policy violation: unload". No first-party JS errors. | Open DevTools console on Pixel 7 emulation. Suggest guarding `adsbygoogle.push` so it only runs when the reserved slot div exists. |
| D14 | INFO | No Arabic (RTL) version exists. `/ar/…` returns 404 and is not in hreflang, so the RTL check is N/A. If Arabic is planned, it needs `dir="rtl"` and mirrored layout. | `curl -I https://www.freedailypro.com/ar/tool/roman-numeral-converter` → 404. |

**What passed:**
- Conversion worked correctly in both directions on all 10 profiles across the 3 engines.
- No ad overlapped any control or result.
- Measured CLS was 0 in Chromium.
- Phones get 16px inputs and 44×44 copy buttons.
- The chart table scrolls inside its own `overflow-x:auto` box.
- No "free/gratis/kostenlos/gratuit" wording appeared in any locale.
- The EU consent banner offers a true Reject.
- html `lang` is correct on every locale.
- Mobile axe found 0 violations.
