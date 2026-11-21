Sent: 2026-11-21 08:44 ET

# Devices, locales, geo, a11y (matrix-results.json, 2026-11-21 08:14–08:21 EST)

## Devices
- All 10 profiles return 200, with the trial strip, Quick Buy and drop zone above the fold. No ad overlaps the tool.
- iPhone SE has 9 px horizontal overflow (button row, right=329 at vw 320).
- CLS: 0 to 0.0814 (Pixel 7 is the highest, still under 0.1).

## Locales
- es, pt, fr, de, ja, hi, zh, ko and id all return 200 with the correct `lang`.
- The header, category breadcrumb, trial strip, Quick Buy and Drive button are translated.
- These stay English on every locale: the H1, title, meta, subtitle, "Runs on your device", the drop-zone lines, the mode cards, the cross-sell card and the accordions.
- /ja desktop has 3 px overflow. The /ar probe returns 404 (not in hreflang).

## Geo
- All 6 contexts (US, DE, FR, IN, SA, JP) show $1 / $4.99 for this tool, plus $3 / $9.99 on the Premium cross-sell card. No consent banner was seen in any of them.

## axe
- Desktop: label-content-name-mismatch (1, `.right-2`), region (1).
- Pixel 7: color-contrast (2) on the muted "Advertisement" label.

## Subsets (contexts at 10/10)
- **Firefox:**
  - S01 picture: 314.7 KB, larger because of Firefox canvas JPEG encoding.
  - S02 P11 editable and S03 P08 editable both convert.
  - Download opens the cap dialog in all 3.
- **WebKit:**
  - The same 3 conversions work, and Download opens the cap dialog.
  - After S03, localStorage `usageToday` read 0 with no download or `usage.log`. This is display-only drift (seen in FDP-50 too); the gate itself held.
