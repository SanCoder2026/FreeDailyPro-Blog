Sent: 2026-11-21 01:26 ET

# FDP-33 Video Thumbnail Generator: devices, locales, geo, axe (run-matrix.js, 2026-11-21 01:11:19–01:21:11 EST)

All matrix contexts loaded at "0 remaining today" (display-only).

## Devices (10, all 200)
- iPhone SE (320 px): page 329 px wide → 9 px horizontal overflow; culprit is a shared `button.inline-flex…` (same family as FDP-30/31/32) (P3). All other devices: no overflow.
- Small targets: breadcrumb "Home" (≈39×20) everywhere; favourites/share/Add to Home Screen icons 16×16 on tablet/desktop; "Quick Buy" 84×28 on desktop (P3).
- Layout: header card (title, privacy chips, trial strip with two Quick Buy buttons), drop zone, "Open from Google Drive", video, then copy. Clean on all engines (Chromium, Firefox, WebKit). Screens: `screens/devices/`.

## Locales (11 incl. probe /ar)
- es, pt, fr, de, ja, hi, zh, ko, id → 200 with `lang` set and the H1 translated client-side; title and meta description stay English; section headings and most labels English (es English-word ratio low on visible text but "About…/How to use it/Common questions" English). Server HTML (curl) has the English H1.
- `/ar/tool/thumbnail-gen` → 404 "Hmm, we couldn't find that page" (not linked by hreflang; probe only).

## Geo (6 contexts)
- Same page, prices "$1" and "$4.99" in every context (en-US, de-DE, fr-FR, hi-IN, ar-SA, ja-JP); no consent banner shown in headless. No local currency (P3 suggestion only).

## axe
- Desktop: label-content-name-mismatch (serious, 1: `.right-2`), region (moderate, 1).
- Pixel 7: color-contrast (serious, 2) — the ad caption text under reserved ad containers. Keep the ad slots; fix the caption colour.
- Manual: both strip buttons are named "Quick Buy" with no plan in the name (P3).
