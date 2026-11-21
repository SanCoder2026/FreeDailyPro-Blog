Sent: 2026-11-21 07:23 ET

# Devices, locales, geo, a11y (matrix-results.json, 2026-11-21 07:05–07:14 EST)

- **Devices:** 10 profiles all 200. Trial strip and drop zone above the fold.
  - iPhone SE has 9 px horizontal overflow (button row / count badge, right=329–331 at vw 320). No other overflow and no ad overlaps.
  - CLS 0–0.018.
- **Locales:** es, pt, fr, de, ja, hi, zh, ko, id all 200, with lang set and H1 translated.
  - Title, meta and many labels stay English ("About …", "How to use it", "Common questions", "HOW IT WORKS", "Take photo with camera", "Share this tool", the video title).
  - /ja desktop has 3 px overflow. The /ar probe gives a 404 (not in hreflang; expected).
- **Geo:** en-US, de-DE, fr-FR, hi-IN, ar-SA, ja-JP all show $1 / $4.99 for this tool (the $3/$9.99 on the page belong to other offers). No consent banner seen.
- **axe:**
  - Desktop: label-content-name-mismatch (1), link-in-text-block (4), region (1).
  - Pixel 7: color-contrast on the ad label (2), link-in-text-block (4).
