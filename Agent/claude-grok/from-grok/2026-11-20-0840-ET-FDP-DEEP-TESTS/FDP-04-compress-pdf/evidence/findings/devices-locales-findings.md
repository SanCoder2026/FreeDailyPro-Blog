Sent: 2026-11-20 08:40 ET

# Compress PDF: devices, platforms, locales, geo and a11y

- **Written:** 2026-11-19 11:23:26 EST (box `date`, ET).
- **Run:** `run-matrix.js` with `scripts/config.json`, 2026-11-19 11:09:19 → 11:21:23 EST (`json/matrix-results.json`).
- **Browsers:** Chromium 159, Firefox 159, WebKit 27.2. Emulation only, not real phones.
- **Scope:** the page in its empty state. The result view (after Compress) is covered in `live-functional-findings.md` §5–6.

## Devices and browsers (checks 4, 14, 15)

| Profile | Engine | HTTP | Overflow | Drop zone above the fold | Strip on load | Notes |
|---|---|---|---|---|---|---|
| iPhone SE 320×568 | WebKit | 200 | **329 > 320** (header button) | **no** (the fold ends at "One file / Several files", `screens/devices/iphone-se-fold.png`) | **10 remaining** | |
| iPhone 14 Pro Max 430×740 | WebKit | 200 | no | partly | **10 remaining** | |
| Pixel 7 412×839 | Chromium | 200 | no | yes | 0 | CLS 0 |
| Galaxy S9+ 329×677 | Chromium | 200 | no | **no** (Open from Google Drive at y=930) | 0 | |
| iPad Mini 768×1024 | WebKit | 200 | no | yes | 0 | 16×16 favourite/share/home-screen icons; Quick Buy 84×28 |
| iPad Pro 11 landscape | WebKit | 200 | no | yes | 0 | same small icons |
| Desktop 1366×768 | Chromium | 200 | no | yes | 0 | CLS 0.013 |
| Desktop 1920×1080 | Chromium | 200 | no | yes | 0 | CLS 0.022 |
| Desktop 1440×900 | Firefox | 200 | no | yes | 0 | |
| Desktop 1440×900 | WebKit | 200 | no | yes | 0 | |

- No ad overlaps the tool's controls on any profile, before or after scroll.
- Phones show the compact "Ad-free: $1 day pass · $4.99/month" link instead of the two Quick Buy buttons. Good.
- **After Compress, the result view overflows on phones** (Pixel 7 page width 958 px) and squeezes the level labels on desktop. See `live-functional-findings.md` §5 (HIGH).

## Trial strip on load (display-only)

The matrix used 16 fresh contexts. **3 loaded uncapped** (iPhone SE, iPhone 14 Pro Max, geo ja-JP/Tokyo) and 13 at 0.

Across the whole run that is **3 of 31 fresh contexts uncapped**:
- the 12 scripted Chromium contexts
- 3 extra WebKit battery attempts at 11:22:43–11:22:53 EST
- the 16 matrix contexts

The uncapped matrix contexts are page-load only; no action was taken in them.

## Locales (check 16)

| Locale | HTTP | `lang` | \<title\> / meta (server) | H1 (rendered) | Notes |
|---|---|---|---|---|---|
| en | 200 | en | English | English | — |
| **es** | 200 | es | **Spanish**: "Comprimir PDF a un tamaño objetivo: **gratis**, sin registro"; meta "Reduce un PDF en cuatro modos: Equilibrado, Agresivo, Extremo…" | "Comprimir PDF: cuatro modos o un tamaño objetivo" | "gratis" (free) is off-brand; the body is mixed (stepper, drop zone and FAQ in English, as on merge-pdf) |
| pt / fr / de / ja / hi / zh / ko / id | 200 | correct | **English** (server HTML H1 is English too) | translated client-side (Comprimir PDF, Compresser PDF, PDF Komprimieren, PDF圧縮, PDF कंप्रेस करें, 压缩PDF, PDF 압축, Kompres PDF) | mixed UI; **ja desktop overflows by 3 px** (1369/1366) |
| /ar/tool/compress-pdf | 404 | — | — | — | no RTL (not in hreflang) |

## Geo and timezone (check 16)

- All six contexts (en-US/NY, de-DE/Berlin, fr-FR/Paris, hi-IN/Kolkata, ar-SA/Riyadh, ja-JP/Tokyo) render English with **USD only** ($1, $4.99).
- The EU consent banner ("We use cookies for analytics and, when ads are shown, advertising… Accept all · Reject non-essential · Choose") is **visible in the Berlin screenshot**. The script's detector missed it this run, so the JSON shows `consent:false`; trust the screenshot (`screens/geo/geo-de-de-…-fold.png`).

## Accessibility (check 15)

- **axe, empty state:**
  - Desktop: `label-content-name-mismatch` (serious, 1) and `region` (moderate, 1). The same as merge-pdf: a shared component.
  - Pixel 7: `color-contrast` (serious, 2) on the "Advertisement" caption under the ad slot.
- **axe, result view:** 0 violations (`json/kbd.json`).
- **Keyboard:** the drop zone opens with Enter, and mode buttons use aria-pressed. **Focus is lost to \<body\> after a file is added and after Compress** (LOW).

Screenshot note: in the zip, screenshots are downscaled to ≤1400 px wide (PNG quantized to 256 colours; full-page shots as JPEG q70).
