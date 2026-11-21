Sent: 2026-11-21 08:14 ET

# Devices, locales, geo, a11y (matrix-results.json, 2026-11-21 EST)

## Devices
- All 10 profiles return 200, with the trial strip and drop zone above the fold. No ad overlaps.
- iPhone SE has 9 px horizontal overflow (button row, right=329 at vw 320).
- CLS is 0–0.043.

## Locales
- es, pt, fr, de, ja, hi, zh, ko and id all return 200 with the right lang, and the H1 is translated ("PDF zu Excel", "PDFをExcelに変換"…).
- The title ("Extract PDF Tables to Excel Online - Converter"), meta, "Watch: … in Action", "Share this tool", "Add to favorites", the section headings and the video title stay English.
- /ja desktop has 3 px overflow. The /ar probe returns 404 (not in hreflang).
- Number parsing doesn't follow the page locale: the /de page still reads "1.500" as 1.5 (the code has no locale input).

## Geo
- All 6 contexts show $1 / $4.99 for this tool; $3 / $9.99 belong to the Premium cross-sell card. No consent banner was seen.

## axe
- Desktop: label-content-name-mismatch (1), region (1).
- Pixel 7: color-contrast on the muted ad label (2).

## Subsets
- **Firefox** (context at 10/10): S01–S03 extract the same results as Chromium, and Download opens the cap dialog.
- **WebKit:**
  - S01–S03 extract the same results, and the workbooks are byte-identical to Chromium's (sha match).
  - That context's strip read 10/10 ("0 remaining"), yet all three downloads went through, with one `usage.log` POST. So the server had uses left while the displayed counter said none (a display mismatch; counters are display-only evidence), and then per-page-load charging made the other two free.
  - A dedicated recheck (`px-wk-gate.js`, 3 fresh WebKit contexts at 10/10) showed the cap dialog every time, so there's no WebKit gate bypass (json/gate-webkit.json).
