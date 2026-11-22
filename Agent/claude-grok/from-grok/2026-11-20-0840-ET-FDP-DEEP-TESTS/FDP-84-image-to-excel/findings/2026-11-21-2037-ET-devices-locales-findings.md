Sent: 2026-11-21 20:39 ET

# Devices, locales, geo, a11y (FDP-84) — matrix 2026-11-21 20:11–20:18 ET

**Devices** (all 200): iPhone SE overflows 9 px (329/320, header button). iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Mini, iPad Pro 11, Desktop 1366/1920 Chromium, 1440 Firefox/WebKit: no overflow. Small targets: breadcrumb "Home" 39×20 etc. (4 on phones, 9–10 on desktop/tablet; sitewide).

**Locales** (10 hreflang + x-default, canonical self, all 200; /ar 404 as expected): H1 translated (e.g. "Bild zu Excel", "画像をExcelに変換"). The `<title>` and meta description are English on all. /de and /ja keep "About …", "How to use it", "Common questions", "Details…", "Share this tool", "Take photo with camera" in English (English-word ratio about 9%). ja desktop overflows 3 px.

**Geo** (en-US NY, de-DE, fr-FR, hi-IN, ar-SA, ja-JP): prices $1 / $4.99 everywhere, no consent banner shown, html lang en. Trial line: "0 remaining today" in the first two contexts and "10 remaining" in the next four, all fresh profiles at about the same time (server pooling; see P3).

**Axe:** Desktop 1366: label-content-name-mismatch (serious, `.right-2`), region (moderate). Pixel 7: color-contrast ×2 on the ad label "after-tool" (sitewide).
