Sent: 2026-11-20 08:40 ET

# Merge PDF: devices, platforms, locales, geo and a11y

- **Written:** 2026-11-19 10:49:45 EST (box `date`, ET).
- **Run:** `run-matrix.js` with `scripts/config.json`, 2026-11-19 10:40:42 → 10:47:28 EST (`json/matrix-results.json`).
- **Browsers:** Chromium 159, Firefox 159, WebKit 27.2. Emulation only, not real phones.
- **Scope:** page load and layout. Interaction is covered in `live-functional-findings.md`.

## Devices and browsers (checks 14, 15)

| Profile | Engine | HTTP | Overflow | Drop zone above the fold | Strip on load | Notes |
|---|---|---|---|---|---|---|
| iPhone SE 320×568 | WebKit | 200 | **329 > 320** (header button) | **no** (y=856) | 0 remaining | Strip, upsell row and stepper push the input 1.5 screens down |
| iPhone 14 Pro Max 430×740 | WebKit | 200 | no | **no** (y=749 vs 740) | 0 | |
| Pixel 7 412×839 | Chromium | 200 | no | yes, barely (y=749) | 0 | CLS 0.014 |
| Galaxy S9+ 329×677 | Chromium | 200 | no | **no** (y=856) | 0 | CLS 0 |
| iPad Mini 768×1024 | WebKit | 200 | no | yes | 0 | 16×16 star/share/home-screen icons; Quick Buy 84×28 |
| iPad Pro 11 landscape | WebKit | 200 | no | yes | 0 | same small icons |
| Desktop 1366×768 | Chromium | 200 | no | yes | 0 | CLS 0.015 |
| Desktop 1920×1080 | Chromium | 200 | no | yes | 0 | CLS 0.021 |
| Desktop 1440×900 | Firefox | 200 | no | yes | 0 | side-rail ad 600 px tall |
| Desktop 1440×900 | WebKit | 200 | no | yes | 0 | |

- No ad overlaps the tool's controls on any profile.
- On phones the first ad slot is below the drop zone (y≈881–1703), which is good.
- **All 10 matrix contexts loaded "0 remaining today"** (display-only; IP pool, see live findings §1).

## Locales (check 16)

| Locale | HTTP | `lang` | \<title\> / meta | H1 | Body |
|---|---|---|---|---|---|
| en | 200 | en | English | English | — |
| **es** | 200 | es | **Spanish, server-side**: "Fusionar PDF **gratis**: sin registro y sin subir archivos" | "Fusionar PDF: combina varios archivos en un solo documento" | **Mixed.** Strip, badges, Quick Buy and breadcrumb are Spanish. Subtitle, "Runs on your device", stepper, drop zone, "Open from Google Drive", accordions and "Share this tool" are English (`screens/locales/locale-es-desktop-1366x768-fold.png`) |
| pt / fr / de / ja / hi / zh / ko / id | 200 | correct | **English** | translated client-side (Mesclar PDF, Fusionner PDF, PDF Zusammenführen, PDF結合, PDF मर्ज करें, 合并PDF, PDF 병합, Gabung PDF) | mixed, as above; **ja desktop overflows** horizontally |
| /ar/ probe | 404 | en | — | — | no RTL page (consistent with hreflang) |

- **Brand issue:** the only fully localized title (es) says "gratis", i.e. "free".
- The other 8 locales advertise English titles under translated hreflang.

## Geo and timezone (check 16)

- All six contexts (en-US/NY, de-DE/Berlin, fr-FR/Paris, hi-IN/Kolkata, ar-SA/Riyadh, ja-JP/Tokyo) render English with **USD only**: $1, $4.99, plus the Document Assembler $3 / $9.99.
- The consent banner (Accept all / Reject non-essential / Choose) appears for Berlin and Paris only.
- All six contexts were at 0 remaining.

## Accessibility (check 15)

- **axe, empty state:**
  - Desktop: `label-content-name-mismatch` (serious, 1) and `region` (moderate, 1).
  - Pixel 7: `color-contrast` (serious, 2): the "Advertisement" caption under the ad slot (`.text-muted-foreground/50`).
- **axe, result view:** `aria-allowed-role` (minor, 5), `<figure role=listitem>` (`json/kbd-cloud.json`).
- **Keyboard:**
  - The drop zone opens the chooser with Enter/Space.
  - Move up/down, Remove, and every Arrange and Choose-pages control are labelled buttons.
  - The stepper has a polite live region.
  - **Focus is lost to \<body\> after Move down and after Merge** (LOW).

Screenshot note: in the zip, screenshots are downscaled to ≤1400 px wide (PNG quantized to 256 colours, full-page shots as JPEG q70) to keep the zip under 24 MB.
