Sent: 2026-11-20 08:40 ET

# Devices, locales, geo, accessibility (matrix 17:26–17:33 EST + gate)

- 10 profiles all 200. Horizontal overflow: iPhone SE 320 → 329 px (a button), iPhone 14 Pro Max 430 → 480 px (select trigger + icon) — both WebKit; Galaxy S9+ (Chromium, 320-ish) clean. Small tap targets 10–19 per profile.
- After converting on phones (gate): iPhone SE and Pixel 7 convert data.csv → Excel by tap; no overflow after conversion.
- Locales en/es/pt/fr/de/ja/hi/zh/ko/id: 200, lang set, title/meta stay English; ja desktop 3 px overflow; /ar 404.
- Geo (de-DE, fr-FR, hi-IN, ar-SA, ja-JP, en-US): prices $3 / $9.99 everywhere; cookie notice text present for de/fr.
- axe (Desktop + Pixel 7): button-name critical ×2 (`.min-w-[160px].flex-1:nth-child(1) > .border-input…` select trigger; `button[data-disabled]`). After a drop: no violations.
- Keyboard: drop zone reachable (Tab 31), Enter opens the chooser.
- Ads: right rail 160×620 on desktop Firefox/WebKit, in-flow slots on phones; no overlaps measured. Keep them; reserve slot heights.
