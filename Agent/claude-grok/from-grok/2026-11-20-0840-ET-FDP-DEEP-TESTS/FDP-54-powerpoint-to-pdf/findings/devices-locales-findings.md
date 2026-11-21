Sent: 2026-11-21 10:12 ET

# Devices, locales, geo, a11y

- **Devices:** 10/10 return 200. Trial strip and input above the fold on all.
  - iPhone SE: scrollWidth 329 on a 320 px viewport (header, site-wide), and the drop zone starts just below the fold (screenshot).
  - CLS 0–0.041.
- **Locales:** 9 return 200 with translated H1s ("PowerPoint zu PDF", "PowerPointをPDFに変換", "PowerPoint से PDF"…), strip and pass labels ("Schnellkauf", "Tagespass für 1 $", "4,99 $").
  - English: title, meta, subtitle, privacy note, drop zone and options.
  - /ar returns 404.
- **Geo:** $1 / $4.99 (+ $3 / $9.99 Premium card) in all 6. The EU consent banner shows for de-DE and fr-FR, not the others. Checked visually in the screenshots.
- **axe:**
  - Desktop: label-content-name-mismatch (1), region (1).
  - Pixel 7: color-contrast (2, ad label).
