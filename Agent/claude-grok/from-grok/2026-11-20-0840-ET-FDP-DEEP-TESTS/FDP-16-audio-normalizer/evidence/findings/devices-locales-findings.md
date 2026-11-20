Sent: 2026-11-20 08:40 ET

# Devices, locales, geo, a11y (matrix 2026-11-19 15:10:58–15:19:13 EST)

| Profile | Engine | Status | Overflow-x | Notes |
|---|---|---|---|---|
| iPhone SE | webkit | 200 | True (329/320) | console errors: 0 (ad or third-party scripts only) |
| iPhone 14 Pro Max | webkit | 200 | False (430/430) | console errors: 0 (ad or third-party scripts only) |
| Pixel 7 | chromium | 200 | False (412/412) | console errors: 0 (ad or third-party scripts only) |
| Galaxy S9+ | chromium | 200 | False (329/329) | console errors: 1 (ad or third-party scripts only) |
| iPad Mini | webkit | 200 | False (768/768) | console errors: 0 (ad or third-party scripts only) |
| iPad Pro 11 landscape | webkit | 200 | False (1194/1194) | console errors: 0 (ad or third-party scripts only) |
| Desktop 1366x768 Chromium | chromium | 200 | False (1366/1366) | console errors: 0 (ad or third-party scripts only) |
| Desktop 1920x1080 Chromium | chromium | 200 | False (1920/1920) | console errors: 1 (ad or third-party scripts only) |
| Desktop 1440x900 Firefox | firefox | 200 | False (1440/1440) | console errors: 3 (ad or third-party scripts only) |
| Desktop 1440x900 WebKit | webkit | 200 | False (1440/1440) | console errors: 1 (ad or third-party scripts only) |

**WebKit functional:** not testable on this box (Playwright WebKit crashes on any `<audio>` blob, `json/webkit-control.txt`). Page loads in WebKit were fine.

| Locale | html lang | Title | H1 | Prices |
|---|---|---|---|---|
| /tool/audio-normalizer | en | Audio Normalizer – Normalize to -14/-16 LUFS  | Normalize Audio Loudness (LUFS) Online | ['$1', '$4.99'] |
| /es/tool/audio-normalizer | es | Audio Normalizer – Normalize to -14/-16 LUFS  | Normalizador de Volumen | ['$1', '$4.99'] |
| /pt/tool/audio-normalizer | pt | Audio Normalizer – Normalize to -14/-16 LUFS  | Normalizador de Volume | ['$1', '$4.99'] |
| /fr/tool/audio-normalizer | fr | Audio Normalizer – Normalize to -14/-16 LUFS  | Normalisateur de Volume | [] |
| /de/tool/audio-normalizer | de | Audio Normalizer – Normalize to -14/-16 LUFS  | Lautstärke-Normalisierer | [] |
| /ja/tool/audio-normalizer | ja | Audio Normalizer – Normalize to -14/-16 LUFS  | 音量正規化 | ['$1', '$4.99'] |
| /hi/tool/audio-normalizer | hi | Audio Normalizer – Normalize to -14/-16 LUFS  | वॉल्यूम नॉर्मलाइज़र | ['$1', '$4.99'] |
| /zh/tool/audio-normalizer | zh | Audio Normalizer – Normalize to -14/-16 LUFS  | 音量标准化 | ['$1', '$4.99'] |
| /ko/tool/audio-normalizer | ko | Audio Normalizer – Normalize to -14/-16 LUFS  | 볼륨 정규화 | ['$1', '$4.99'] |
| /id/tool/audio-normalizer | id | Audio Normalizer – Normalize to -14/-16 LUFS  | Penormal Volume | ['$1', '$4.99'] |
| /ar/tool/audio-normalizer | en | Page Not Found \| FreeDailyPro | Hmm, we couldn't find that page | [] |

- Every locale keeps the English `<title>`, meta, subtitle, steps and drop-zone text. Only the H1, breadcrumbs, badges and the trial strip are translated (`screens/locales/locale-fr-desktop-1366x768-fold.png`). fr/de show prices as "1 $" / "4,99 $" (the matrix regex missed them; not a bug).
- /ar/tool/audio-normalizer returns 404 and is not in hreflang (consistent).
- The es server HTML has no "gratis" (checked with curl); other locales were checked by screenshot only. No EU consent banner seen in de-DE/fr-FR geo contexts (consent=False).

| Geo | html lang | Prices | Consent |
|---|---|---|---|
| en-US America/New_York (baseline) | en | ['$1', '$4.99'] | False |
| de-DE Europe/Berlin | en | ['$1', '$4.99'] | False |
| fr-FR Europe/Paris | en | ['$1', '$4.99'] | False |
| hi-IN Asia/Kolkata | en | ['$1', '$4.99'] | False |
| ar-SA Asia/Riyadh | en | ['$1', '$4.99'] | False |
| ja-JP Asia/Tokyo | en | ['$1', '$4.99'] | False |

**axe (matrix):**
- Desktop 1366x768 Chromium: label-content-name-mismatch (serious, 1); region (moderate, 1)
- Pixel 7: color-contrast (serious, 2)
- axe on `main` in `an-gate-kbd.js` (idle and with a result): 0 violations.

**Ads:** in-flow `ad-container` below the tool on phones (y≈887–1042) and a side rail on desktop. They don't overlap the tool. Keep reserved fixed-height slots; never between the result and Download.
