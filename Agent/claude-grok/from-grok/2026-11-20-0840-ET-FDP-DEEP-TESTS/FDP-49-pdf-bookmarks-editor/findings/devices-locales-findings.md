Sent: 2026-11-21 07:48 ET

# Devices, locales, geo, a11y (matrix-results.json, 2026-11-21 EST)

- **Devices:** all 10 profiles return 200, with the trial strip and drop zone above the fold.
  - iPhone SE has 9 px horizontal overflow (button row, right=329 at vw 320). No other overflow and no ad overlaps.
  - CLS is 0–0.039.
- **Locales:** es, pt, fr, de, ja, hi, zh, ko and id all return 200 with the right html lang.
  - The **H1 / tool name stays "PDF Bookmarks Editor"** on every locale.
  - Title, meta, "About …", "How to use it", "Common questions", "Watch: … in Action", "Share this tool", "Add to favorites" and the video title stay English.
  - Quick Buy and Open from Google Drive are translated.
  - /ja desktop has 3 px overflow. The /ar probe returns 404 (not in hreflang).
- **Geo:** en-US, de-DE, fr-FR, hi-IN, ar-SA and ja-JP all show $3 / $9.99. No consent banner was seen.
- **axe:**
  - Desktop: label-content-name-mismatch (1), region (1).
  - Pixel 7: color-contrast on the muted ad label (1).
- **Subsets:**
  - Firefox: S01 0→1, then S02 (Remove all on 300 bookmarks) downloaded at 1 (per-load again). Its output is byte-identical to Chromium's.
  - WebKit: the context was at 2/2. B01 and B07 loaded and edited fine, and Download showed the cap dialog.
