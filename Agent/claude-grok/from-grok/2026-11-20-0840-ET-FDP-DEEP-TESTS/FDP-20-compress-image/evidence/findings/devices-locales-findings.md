Sent: 2026-11-20 08:40 ET

# FDP-20 Compress Image: devices, locales, geo, a11y matrix

`json/matrix-results.json`, run 16:39:59–16:47:32 EST.
- 10 device profiles all 200. Horizontal overflow only on iPhone SE (320 px): scrollWidth 329, culprit a header button (`right=329`) — the same site-wide 9 px header overflow seen on earlier tools. Others clean.
- After upload on iPhone SE, Compress sits at y≈1532 px (viewport 584 px) once Custom Target is open (`json/gate-kbd.json`), i.e. 2–3 screens of scrolling past the preview and note; Pixel 7 y≈1280 (viewport 839). Mode/preset buttons are 32 px tall (below 44 px touch guidance).
- Locales en/es/pt/fr/de/ja/hi/zh/ko/id: all 200, no overflow; /ar 404. Console errors are ad-script (`no_div`, media.net CORS) and "unload" permissions-policy only.
- Geo (de-DE, fr-FR, hi-IN, ar-SA, ja-JP): USD prices $1/$4.99/$3/$9.99 everywhere; cookie banner for de/fr.
- axe (matrix, idle): desktop `label-content-name-mismatch` (serious, 1, `.right-2`), `region` (moderate); Pixel 7 `color-contrast` (serious, 2) on the "Advertisement" caption under the after-tool ad slot. Live axe on Custom Target: `label` + `select-name` critical (see live findings).
