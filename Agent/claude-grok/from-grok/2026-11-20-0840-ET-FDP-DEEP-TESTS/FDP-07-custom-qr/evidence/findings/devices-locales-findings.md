Sent: 2026-11-20 08:40 ET

# FDP-07 custom-qr: devices, platforms, locales, geo and a11y

- **Written:** 2026-11-19 12:34:12 EST (box `date`, ET). Matrix run 2026-11-19 12:23:39–12:32:08 EST (`json/matrix-results.json`, `devices/` screenshots), plus `json/kbd.json`.

## Devices (10 profiles, Chromium, Firefox and WebKit)
- **200 on 10/10.** No ad overlaps on any profile; CLS 0 where measured.
- **Overflow:** iPhone SE scrollWidth 329 > 320 (a button at right=329). The other 9 have no horizontal overflow. ja desktop is 1369 > 1366 (+3 px).
- **Phone layout:** the preview canvas is **below** the Download buttons (Pixel 7: Download y≈1029, canvas y≈1342; iPhone SE: 1155 vs 1468), so a phone user presses Download before seeing the code. This is the same pattern as qr-generator.
- Tap targets: 27–35 small targets per profile (shared site chrome).

## Starting trial count (display-only; this run came after the download battery)
- Devices: 0 remaining on 7 (iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, Desktop 1366 and 1920, Desktop WebKit); 2 remaining on 3 (iPad Mini, iPad Pro, Desktop Firefox).
- Geo: 0 on 3 (en-US, fr-FR, ar-SA); 2 on 3 (de-DE, hi-IN, ja-JP).
- kbd: desktop and Pixel 7 at 0; iPhone SE (WebKit) at 2.
- **So fresh contexts from one box IP load at 0 or 2 seemingly at random.** All prices are USD ($3 / $9.99) in every geo.

## Locales (10 hreflang + /ar)
- 200 on en, es, pt, fr, de, ja, hi, zh, ko, id. /ar is a 404 (not in hreflang; /it is also a 404 by curl).
- **Title and H1 are English in all 9 non-English locales** (H1 "QR Code Generator with Logo"); `lang` is localized. The body text is mostly translated (English-word ratio 0.075–0.08 on Pixel 7).
- No "gratis/gratuit/kostenlos/無料/免费" was found in the SSR HTML of any locale. Rendered copy was not word-checked beyond the English ratio (unverified).
- Console: only adsbygoogle "no_div" and an "unload" permissions-policy message. No app errors.

## Accessibility
- axe on desktop: button-name **critical ×4** (the Dot/Corner/Size select triggers have no name), label **critical ×1** (the logo file input), label-content-name-mismatch serious ×1, region moderate ×1. On Pixel 7, also color-contrast serious ×2.
- Tabs have role=tablist and aria-selected, but **no aria-controls** and every tab has tabindex 0 (no roving focus). Enter works; arrow keys did not move the selection.
- The canvas has no role, label or alternative. A screen-reader user gets no confirmation of what is encoded.
- Selects can be operated by keyboard ("Rounded / Rounded / Dot / 1500 px / 50 mm wide").

## Ads
- Keep the ads in reserved, fixed-height slots below the tool (as now). Never put one between the preview and the Download buttons.
