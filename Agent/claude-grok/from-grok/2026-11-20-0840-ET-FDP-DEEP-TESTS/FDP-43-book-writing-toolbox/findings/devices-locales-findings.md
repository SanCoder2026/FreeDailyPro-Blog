Sent: 2026-11-21 04:56 ET

# FDP-43 Book Writing Toolbox: devices, locales, geo, accessibility (matrix 04:25–04:33 EST)

- **Devices:** all 200.
  - **iPhone SE:** 9 px overflow (a full-width button). Top-bar selects are truncated ("Use def", "Print + E", "Auto: le") but usable. P3.
  - **iPad Mini (768):** 8 px overflow from the editor desk container (`-mx-4 md:-mx-8`). P3.
  - Others clean: iPhone 14 Pro Max, Pixel 7, Galaxy S9+, iPad Pro landscape, Desktop Chromium 1366/1920, Firefox 1440, WebKit 1440.
- **Desktop sidebar** (1366, several captures `B07c.png`, `D01.png`): the front-matter rows (Title Page … List of Images) collapse to about 15 px apart and overlap after scrolling or opening the preview. P3 (check the sticky/min-height of the section list).
- **Engines:** Preview, EPUB (same 500), and the Arabic preview behave the same in Firefox and WebKit as in Chromium.
- **Locales** (/es … /id): 200, html lang set, LTR.
  - English title/meta; the H1 translates the old "Book Maker" name.
  - /ja has 3 px overflow; /ar returns 404.
- **Geo** (locale + timezone, US IP): $29.99 shown everywhere. No EU consent banner seen for de/fr, which is an unverified absence (not an EU IP).
- **axe:**
  - Desktop: **button-name critical ×19** (unlabelled icon buttons: section up/down arrows, checkbox rows, `.w-[130px]` select), **label critical ×1** (the borderless chapter/part title input), label-content-name-mismatch serious ×1, region moderate ×1.
  - Pixel 7: button-name ×1, and color-contrast ×2 on the small ad caption. Fix the caption; keep the reserved slot.
