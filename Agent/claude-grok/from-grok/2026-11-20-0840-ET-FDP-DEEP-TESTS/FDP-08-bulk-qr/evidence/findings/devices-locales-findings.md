Sent: 2026-11-20 08:40 ET

# FDP-08 bulk-qr: devices, platforms, locales, geo and a11y

- **Written:** 2026-11-19 12:59:46 EST (box `date`, ET). Matrix `json/matrix-results.json` (started 2026-11-19 12:50:21 EST, finished 2026-11-19 12:58:06 EST), plus `json/kbd.json`.

## Devices (10 profiles: Chromium, Firefox, WebKit)
- **200 on 10/10.** No ad overlaps. CLS ≤ 0.023.
- **Overflow:** iPhone SE scrollWidth 329 > 320 (a button at right=329, the same site-chrome culprit as FDP-06/07). ja desktop 1369 > 1366 (+3 px). No other overflow.
- **Phone layout (good):** the list, the preview and Generate stay in order. On Pixel 7 the textarea is at y≈434, the preview at y≈847 and Generate at y≈935, so the user sees the codes before pressing Generate.

## Starting trial count (display-only)
- All 16 matrix and geo contexts loaded at **0 remaining** (10 uses/day).
- Across the whole run, about 36 readable fresh Chromium/WebKit/Firefox contexts were seen; **2 loaded at 10** (both battery D contexts), and the rest at 0.
- This is the same pattern as the Professional Tools in FDP-02 to FDP-06. Prices are USD ($1 / $4.99) in all 6 geos.

## Locales (10 hreflang + /ar)
- 200 on en, es, pt, fr, de, ja, hi, zh, ko, id. /ar returns 404 (not in hreflang).
- The title and H1 are **English in all 9 non-English locales**. The body is mostly translated (English-word ratio 0.086–0.091 on Pixel 7).
- No "gratis"-type words in the SSR HTML.

## Accessibility
- axe on desktop: button-name **critical ×3** (Format/PNG size/EC select triggers), label-content-name-mismatch serious ×1, region moderate ×1. On Pixel 7, also color-contrast serious ×2.
- The hidden file input for Open project has no label (it's hidden; the button is labelled).
- Tab order is logical: textarea → name,value checkbox → Format → size → EC → colours → Save/Open/Try a sample. Generate ZIP was skipped in that capture because the list was empty, so the button was disabled (expected).
- Preview images have alt "QR for <value>", which is better than the canvas-only custom-qr and qr-generator.
- The progress bar has role=progressbar with aria-valuenow.

## Ads
- Keep the ads in reserved, fixed-height slots below the tool (as now). Never put one between the preview and Generate ZIP.
