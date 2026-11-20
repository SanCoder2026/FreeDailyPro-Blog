Sent: 2026-11-20 08:40 ET

# QR Code Generator: devices, platforms, locales, geo and a11y

Written: 2026-11-19 12:03 EST. Matrix 2026-11-19 11:55:22–12:01:49 EST (`json/matrix-results.json`), plus qr-kbd.js. Emulation only.

## Trial state

All 22 readable fresh contexts showed **0 remaining** (display-only, shared P0).

## Devices (empty state)

| Profile | Engine | HTTP | Overflow | QR preview position | Notes |
|---|---|---|---|---|---|
| iPhone SE 320×568 | WebKit | 200 | **329 > 320** (header menu button) | y=1185, 254 px; **below the Download buttons and 2 screens down** | |
| iPhone 14 Pro Max | WebKit | 200 | none | y=1094, below the fold | |
| Pixel 7 | Chromium | 200 | none | y=1094 (vh 839), below the Download buttons (y=869) | CLS 0 |
| Galaxy S9+ | Chromium | 200 | none | y=1185 | |
| iPad Mini / iPad Pro 11 | WebKit | 200 | none | visible above the fold, beside the form | |
| Desktops (1366, 1920 Chromium; 1440 Firefox, WebKit) | — | 200 | none | above the fold, right column | CLS ≤ 0.013 |

- **Phone UX (P2):** on all phones the preview sits **below** the Download PNG/SVG buttons and off-screen while typing. Users press Download (and spend a use) before seeing the code. Desktop and tablet show it side by side. See `screens/live/phone-pixel-7-full.jpg`.
- **Ads:** no overlaps in any profile.

## Locales

| Locale | HTTP | Server title | Client H1 | Notes |
|---|---|---|---|---|
| en | 200 | English | QR Code Generator | |
| es | 200 | **"Generador de códigos QR gratis: …"** | localized | "gratis" = free (off-brand) |
| pt fr de ja hi zh ko id | 200 | **English** | **"QR Code Generator" (English)** | The H1 is not localized even client-side, unlike split-pdf. About 15–17 English labels per page |
| ar | 404 | — | — | not in hreflang |

- ja overflows by 3 px at 1366. Phones: no overflow in any locale.
- Prices are USD only ($1/$4.99 and the Premium $3/$9.99) in all 6 geos. htmlLang is en on the en URL. No consent banner was detected (the detector is weak).

## Accessibility

- **axe (empty page, desktop and Pixel 7):**
  - **button-name critical ×2** (the size and EC select triggers)
  - **label critical ×1** (the logo file input)
  - label-content-name-mismatch serious ×1 (desktop)
- **Keyboard:** tabs activate with Enter but not with the arrow keys, and selects work. The canvas has no alt text.
- Small touch targets: 17 on phones (breadcrumb links, Share).
