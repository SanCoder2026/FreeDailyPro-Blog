Sent: 2026-11-20 08:40 ET

# Compare Two Audio Files: devices, platforms, locales, geo and a11y

- **Written:** 2026-11-19 10:25:47 EST (box `date`, ET).
- **Run:** `run-matrix.js` with `scripts/config.json`, 2026-11-19 10:14:11 → 10:22:28 EST (`json/matrix-results.json`).
- **Browsers:** Chromium 159, Firefox 159, WebKit 27.2 (Playwright 1.65.1). Device emulation only, not real phones.
- **Scope:** page load and layout. The interaction checks are in `live-functional-findings.md`, plus keyboard checks in `json/a11y-result.json`.

## Devices and browsers (checks 14, 15)

| Profile | Engine | HTTP | Horizontal overflow | Drop zone above the fold | Trial strip on load | Notes |
|---|---|---|---|---|---|---|
| iPhone SE 320×568 | WebKit | 200 | **yes, 329 px > 320** (header button row) | **no** (input top at y=632, fold 568) | 10 remaining | Ad slot below the tool (y=1288). Stepper and strip push the input down |
| iPhone 14 Pro Max 430×740 | WebKit | 200 | no | yes (y=582) | **0 remaining** | |
| Pixel 7 412×839 | Chromium | 200 | no | yes (y=566) | 10 remaining | CLS 0.014 |
| Galaxy S9+ 329×677 | Chromium | 200 | no | yes, barely (y=632) | **0 remaining** | CLS 0.011 |
| iPad Mini 768×1024 | WebKit | 200 | no | yes | 10 remaining | 11 small targets |
| iPad Pro 11 landscape 1194×834 | WebKit | 200 | no | yes | **0 remaining** | |
| Desktop 1366×768 | Chromium | 200 | no | yes | **0 remaining** | CLS 0.015 |
| Desktop 1920×1080 | Chromium | 200 | no | yes | **0 remaining** | CLS 0.018 |
| Desktop 1440×900 | Firefox | 200 | no | yes | **0 remaining** | Side-rail ads. **The floating "Feedback" button sits over the right-rail ad's call-to-action button** (`devices/desktop-1440x900-firefox-fold.png`), which risks accidental ad taps. Reserve a clear zone for the FAB. LOW |
| Desktop 1440×900 | WebKit | 200 | no | yes | **0 remaining** | |

- **Overlaps:** no ad overlapped the tool's key controls on any profile (`overlaps=[]`).
- **Small targets:**
  - Phones: breadcrumb "Home" 39×20; "Share this tool" 140×32; "Open from Google Drive" 36 px tall.
  - Desktop: the star and share icons are 16×16, and "Quick Buy" is 84×28. These are below the 44 px touch guideline. LOW.
- **Trial strip:** shown "0 remaining today" on load in 7 of 10 fresh device contexts. This is the IP-pool behaviour described in `live-functional-findings.md` §4. It is display evidence only.

## Locales (check 16)

10 hreflang locales plus an `/ar/` probe, each on Desktop 1366×768 and Pixel 7.

| Locale | HTTP | `<html lang>` | `<title>` / meta | Rendered H1 | Other UI |
|---|---|---|---|---|---|
| en | 200 | en | English | Compare Two Audio Files | — |
| es | 200 | es | **English** | Comparar Dos Audios | **Mixed** |
| pt | 200 | pt | **English** | Comparar Dois Áudios | Mixed |
| fr | 200 | fr | **English** | Comparer Deux Fichiers Audio | Mixed |
| de | 200 | de | **English** | Zwei Audiodateien Vergleichen | Mixed |
| ja | 200 | ja | **English** | 音声ファイル比較 | Mixed; **desktop overflow 1369 > 1366** |
| hi | 200 | hi | **English** | दो ऑडियो फ़ाइलें कंपेयर करें | Mixed |
| zh | 200 | zh | **English** | 比较两个音频文件 | Mixed |
| ko | 200 | ko | **English** | 두 오디오 파일 비교 | Mixed |
| id | 200 | id | **English** | Bandingkan Dua File Audio | Mixed |
| /ar/ (probe, not in hreflang) | **404** | en | "Page Not Found" | — | no RTL version (consistent with hreflang) |

What "mixed" means on these pages (`locales/locale-es-desktop-1366x768-full.jpg`):
- **Translated:** H1, strip ("Prueba: 10 usos/día · 10 restantes hoy"), "Abrir desde Google Drive", nav and footer.
- **Still English:** the subtitle ("Compare two audio clips and see a similarity percentage"), the badges ("Files never stored", "Runs on your device"), the whole How-it-works stepper, "Drop first audio file / or click to browse / Large files…", the **Compare Audio** button, the accordion headers ("About …", "How to use it", "Common questions", "Details…", "Guides and next steps"), "Share this tool", and the video label.
- **Server HTML:** for /es (curl) it has an English H1 and FAQ, so crawlers see English under `lang="es"`.
- **Result view and error toasts:** in other locales, not checked (unverified).

## Geo and timezone contexts (check 16)

All six contexts render the same English page with prices in **USD only** ($1, $4.99):
- en-US/New_York
- de-DE/Berlin
- fr-FR/Paris
- hi-IN/Kolkata
- ar-SA/Riyadh
- ja-JP/Tokyo

The consent banner ("We use cookies for analytics and, when ads are shown, advertising. The tools work either way. … Accept all / Reject non-essential / Choose") appeared in the Berlin and Paris contexts only, which is expected for the EU. All six contexts showed "0 remaining today" on load (`geo/`).

## Accessibility (check 15)

**axe-core 4.14.1, empty state:**
- Desktop: `label-content-name-mismatch` (serious, 1, `.right-2`) and `region` (moderate, 1).
- Pixel 7: `color-contrast` (serious, 1, `.text-muted-foreground/50`).

**axe, result view (`json/a11y-result.json`):** `color-contrast` (serious, 9). The 11 px blue/green/red labels on #0d1820 measure 3.4–3.8:1 against a required 4.5:1. Examples are the "File 1" (blue), "File 2, lined up…" (green) and "Difference…" (red) waveform captions.

**Keyboard and screen reader:**
- Drop zones are focusable (`tabindex=0`) with a visible focus ring, and Enter/Space open the file chooser.
- The Compare button works by keyboard.
- Results are announced through polite live regions ("Comparison complete!", "All steps done.").
- Waveform canvases are `role=img` with labels.

**Gaps:**
- Focus falls to \<body\> after Compare.
- Strip cells are `title`-only (no role or name), with colour-only meaning. The "Differs at…" text partly compensates.
- Drop zones have no `aria-label`, so the name comes from the inner text. Fine.
Screenshot note: full-page device/locale/geo/a11y screenshots are JPEG (q80) to keep the zip small; fold screenshots and live/ screenshots are PNG.
