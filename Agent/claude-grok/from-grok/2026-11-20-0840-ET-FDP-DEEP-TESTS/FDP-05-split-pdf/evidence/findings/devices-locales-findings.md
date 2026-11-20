Sent: 2026-11-20 08:40 ET

# Split PDF: devices, platforms, locales, geo and a11y

Written: 2026-11-19 11:44 EST. Matrix run 2026-11-19 11:35:57–11:43:19 EST.

- **Script:** `run-matrix.js scripts/config.json`, results in `json/matrix-results.json`.
- **Plus:** sp-kbd.js (`json/kbd.json`) for the result view.
- **Method:** emulation only; no real iOS or Android hardware, no real foreign IP.

## Trial state across fresh contexts (display-only)

- Contexts where the count was readable: probe, explore, kbd ×2, ranges-rows, 10 devices, the en locale load, 6 geo = **22 contexts**.
  - **21 showed "0 remaining today".**
  - **1 showed 10**: geo hi-IN / Asia/Kolkata, about 11:42 EST. That was a page load only, so no downloads were possible from it.
- The localized strips in the other locale loads weren't parsed for a count.
- Same pattern as FDP-02 to FDP-04 (P0, shared). No backend claim is made.

## Devices (empty state)

| Profile | Engine | HTTP | Overflow | CLS | Notes |
|---|---|---|---|---|---|
| iPhone SE 320×568 | WebKit | 200 | **329 > 320**. Culprit: the header menu button (right=329) | — | The fold shot ends inside "How it works"; the drop zone and "Open from Google Drive" (y=772) are **below the fold** |
| iPhone 14 Pro Max | WebKit | 200 | none | — | |
| Pixel 7 | Chromium | 200 | none | 0 | |
| Galaxy S9+ 329 px | Chromium | 200 | none | 0.013 | "Open from Google Drive" (just under the drop zone) at y=772 of 677, below the fold |
| iPad Mini | WebKit | 200 | none | — | |
| iPad Pro 11 landscape | WebKit | 200 | none | — | |
| Desktop 1366×768 | Chromium | 200 | none | 0.013 | adsbygoogle "no_div" console error |
| Desktop 1920×1080 | Chromium | 200 | none | 0.027 | same console error |
| Desktop 1440×900 | Firefox | 200 | none | — | |
| Desktop 1440×900 | WebKit | 200 | none | — | ad-frame CORS console noise |

- **Ads:** no overlaps with the tool in any profile. The slots sit below the tool and between sections.
- **Phone strip:** collapses to "Ad-free: $1 day pass · $4.99/month". Good.

## Result view (after split, sp-kbd.js)

- **Pixel 7:** scrollWidth 412 = viewport; no overflow (better than compress-pdf). See `screens/live/phone-result-view.jpg`.
- **Desktop 1366:** the file name in each row is truncated to about 100 px ("A_10p_bookm…"). All rows of one PDF look identical until you read the second line ("pages 1-3 · 3 pages · 1.8 KB"), so it's hard to tell the parts apart (P2).
  - Each row also carries Download, the cap note, Save to Google Drive, Save to my cloud storage and the mark notice, so it's busy.
  - See `screens/live/kbd-result-view.jpg`.

## Locales (client-rendered, Desktop 1366 + Pixel 7)

| Locale | HTTP | lang | Title (server and client) | H1 (client) | Notes |
|---|---|---|---|---|---|
| en | 200 | en | English | Split PDF | |
| es | 200 | es | **English** | Dividir PDF | Section headings "How to use it", "Common questions", "Guides and next steps", "HOW IT WORKS" and "Share this tool" stay English (12 English labels) |
| pt / fr / de / id | 200 | ✓ | **English** | Dividir PDF / Diviser PDF / PDF Teilen / Pisah PDF | same mixed UI |
| ja | 200 | ja | **English** | PDF分割 | **3 px horizontal overflow** at 1366 (1369) |
| hi / zh / ko | 200 | ✓ | **English** | localized | mixed UI (10 English labels) |
| /ar | **404** | en | "Page Not Found" | — | ar is not in hreflang, so it's consistent, but there is no RTL locale |

- The search placeholder "Search 300+ tools…" is English in every locale.
- Prices are USD only in all 6 geos.
- No consent banner was detected by the script (the EU banner was seen on compress-pdf; the detector is weak).

## Geo (Accept-Language + timezone, en URL)

- en-US, de-DE, fr-FR, hi-IN, ar-SA and ja-JP all return 200 with htmlLang en.
- Prices are $1 / $4.99 everywhere.
- There's no auto-redirect to a locale (fine).

## Accessibility

- **axe on the empty page:**
  - Desktop: label-content-name-mismatch (serious, 1, `.right-2`), region (moderate, 1).
  - Pixel 7: color-contrast (serious, 2), the "Advertisement" caption under the ad slots.
- **axe on the result view (desktop, after split): 0 violations.**
- **Keyboard:** Enter on the drop zone opens the file chooser. The Split button works by keyboard.
- **Focus (P2):** focus falls back to BODY after a file is added and after Split. Screen-reader users get the polite live-region text ("Split into 3 files", "3 of 4 steps done. Current step: Download."), but keyboard users must tab from the top.
- **Range field:** visible label "Page ranges (comma-separated, e.g. "1-3, 4-6, 7")". axe on the result view is clean, and invalid input sets aria-invalid with an inline error. Good.
- **Thumbnails:** `img alt="Page N"`, not interactive. That's fine, but it contradicts the Details copy.
