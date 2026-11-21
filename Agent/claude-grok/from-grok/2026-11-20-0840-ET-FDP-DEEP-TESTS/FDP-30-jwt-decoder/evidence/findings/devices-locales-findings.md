Sent: 2026-11-21 00:18 ET

# FDP-30 JWT Decoder: devices, locales, geo, a11y (run-matrix, 2026-11-21 00:03:03–00:12:14 EST)

Raw: `json/matrix-results.json`, `json/matrix.log`; screenshots in `screens/devices/`, `screens/locales/`, `screens/geo/`, `screens/a11y/`.

## Devices (10)
- All 10 loaded 200 (iPhone SE, iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11 landscape, Desktop Chromium 1366/1920, Firefox 1440, WebKit 1440).
- **iPhone SE (320 px): 9 px horizontal overflow**; culprit a `button.inline-flex…` whose right edge is 329 px (scrollWidth 329). Other devices: no overflow.
- iPhone SE: the JWT textarea is only ~69 px tall (2 lines) and its placeholder "Paste your JWT here (a leading Bearer prefix is removed automatically)" is clipped (`screens/devices/iphone-se-fold.png`). A real token (300–1,000+ chars) needs scrolling inside a 2-line box. P3.
- Small targets on iPhone SE: breadcrumb links (20 px tall) and "Share this tool" (32 px).
- Ads: 4 slots on iPhone SE, the first directly under the textarea (y≈465). With a token pasted the result renders above it, so the ad does not split input and result. Keep the slots (reserved heights look stable; no layout shifts recorded).
- Badge "Files never stored" is generic; this tool takes pasted text, not files (P3 wording).

## Locales (10 hreflang + /ar probe)
- en, es, pt, fr, de, ja, hi, zh, ko, id → 200, no overflow on Pixel 7 or Desktop 1366.
- es: title/H1 translated ("Decodificador de JWT: encabezado, contenido y vencimiento del token"; title "…en línea gratis…"), one FAQ in Spanish, the rest English. The other 8 serve the English page under their `lang`.
- `/ar/tool/jwt-decoder` → 404 (no ar hreflang, consistent).
- Console errors seen are AdSense `no_div` and a permissions-policy "unload" message (third-party; not tool errors).

## Geo (6)
- en-US NY, de-DE Berlin, fr-FR Paris, hi-IN Kolkata, ar-SA Riyadh, ja-JP Tokyo: all 200, English, no prices shown. de/fr show the cookie consent banner ("…The tools work either way. … Accept all / Reject non-essential / Choose"); others do not.
- Time lines use the browser's local zone (local-time line verified as EST/EDT in live runs; other zones not separately checked for the decoded output).

## Accessibility (axe)
- Desktop: `label-content-name-mismatch` (serious, 1: `.right-2`, a button whose visible text is not in its accessible name) and `region` (moderate, 1). Pixel 7: no violations.
- The textarea has a visible "JWT Token" label; keyboard order is logical: breadcrumb → favorites → share → textarea → Copy result / Save as text / Print → video → accordions (`json/misc.json`).
- Error messages: whether they are announced (role=alert/aria-live) was read from `cases.json` `alerts` (the messages appeared in the alert capture), so they are exposed to assistive tech.
