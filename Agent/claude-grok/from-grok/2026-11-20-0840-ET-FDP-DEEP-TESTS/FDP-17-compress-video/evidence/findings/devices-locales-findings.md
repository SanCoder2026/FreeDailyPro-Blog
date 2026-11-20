Sent: 2026-11-20 08:40 ET

# Devices, locales, geo, a11y (matrix 2026-11-19 15:30:59–15:37:57 EST)

| Profile | Engine | Status | Overflow-x |
|---|---|---|---|
| iPhone SE | webkit | 200 | True (329/320) |
| iPhone 14 Pro Max | webkit | 200 | False (430/430) |
| Pixel 7 | chromium | 200 | False (412/412) |
| Galaxy S9+ | chromium | 200 | False (329/329) |
| iPad Mini | webkit | 200 | False (768/768) |
| iPad Pro 11 landscape | webkit | 200 | False (1194/1194) |
| Desktop 1366x768 Chromium | chromium | 200 | False (1366/1366) |
| Desktop 1920x1080 Chromium | chromium | 200 | False (1920/1920) |
| Desktop 1440x900 Firefox | firefox | 200 | False (1440/1440) |
| Desktop 1440x900 WebKit | webkit | 200 | False (1440/1440) |

iPhone SE 320 px overflow: the header "Open menu" button (site-wide; same as FDP-16). Console errors were ad or third-party only.
**WebKit processing:** unverified (Playwright WebKit on this box crashes on `<video>` blobs; `json/browsers.json`).

| Locale | html lang | Title | H1 | Prices |
|---|---|---|---|---|
| /tool/compress-video | en | Compress Video to a Target Size (MB) \| F | Compress Video | ['$1', '$4.99'] |
| /es/tool/compress-video | es | Compress Video to a Target Size (MB) \| F | Comprimir Video | ['$1', '$4.99'] |
| /pt/tool/compress-video | pt | Compress Video to a Target Size (MB) \| F | Comprimir Vídeo | ['$1', '$4.99'] |
| /fr/tool/compress-video | fr | Compress Video to a Target Size (MB) \| F | Compresser Vidéo | [] |
| /de/tool/compress-video | de | Compress Video to a Target Size (MB) \| F | Video Komprimieren | [] |
| /ja/tool/compress-video | ja | Compress Video to a Target Size (MB) \| F | 動画圧縮 | ['$1', '$4.99'] |
| /hi/tool/compress-video | hi | Compress Video to a Target Size (MB) \| F | वीडियो कंप्रेस करें | ['$1', '$4.99'] |
| /zh/tool/compress-video | zh | Compress Video to a Target Size (MB) \| F | 压缩视频 | ['$1', '$4.99'] |
| /ko/tool/compress-video | ko | Compress Video to a Target Size (MB) \| F | 동영상 압축 | ['$1', '$4.99'] |
| /id/tool/compress-video | id | Compress Video to a Target Size (MB) \| F | Kompres Video | ['$1', '$4.99'] |
| /ar/tool/compress-video | en | Page Not Found \| FreeDailyPro | Hmm, we couldn't find that page | [] |

- Titles and meta are English everywhere. Most of the UI stays English (H1, breadcrumbs and strip are translated). fr/de show prices as "1 $" (the regex missed them).

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
- axe on `main` (`cv-gate-kbd.js`, idle and result): 0.

**Ads:** in-flow below the tool on phones; side rail on desktop. Keep reserved fixed-height slots, never between the result and Download.
