Sent: 2026-11-21 00:58 ET

# FDP-32 Hash Generator: devices, locales, geo, a11y (run-matrix, 2026-11-21 00:42:53–00:54:11 EST)

Raw: `json/matrix-results.json`, `json/matrix.log`; screenshots in `screens/devices/`, `screens/locales/`, `screens/geo/`, `screens/a11y/`.

## Devices (10)
- All 10 loaded 200. **iPhone SE (320 px): 9 px horizontal overflow** (`button.inline-flex…` right=329; same shared button as FDP-30/31). Others: none.
- Mobile: the text box is only ~42 px tall (≈1–2 lines); Generate Hashes 36 px; "Share this tool" 32 px; breadcrumb 20 px. Tablet/desktop: favorites/share/add-to-home icons 16 px.
- The file picker is an underlined text label (no button look), easy to miss on mobile.

## Locales (10 hreflang + /ar probe)
- en/es/pt/fr/de/ja/hi/zh/ko/id → 200; /ar → 404. es: translated title/H1 (title "Generador de hash en línea: MD5, SHA-1, SHA-256 gratis", no brand suffix), English body. Others: English under their lang/hreflang.
- ja Desktop 1366: 3 px horizontal overflow (scrollWidth 1369).

## Geo (6)
- en-US, de-DE, fr-FR, hi-IN, ar-SA, ja-JP: all 200, English, no prices; de/fr show the cookie consent banner. Output is locale-neutral.

## Accessibility (axe + manual)
- Desktop: `label-content-name-mismatch` (serious, 1, `.right-2`), `region` (moderate, 1). Pixel 7: `color-contrast` (serious, 1, `.text-muted-foreground/50`, an ad caption style).
- Manual (live): the file input is `display:none` and not keyboard reachable (P1); the five result buttons are all named "Copy" (P3); errors are role=alert; the textarea has an aria-label.
