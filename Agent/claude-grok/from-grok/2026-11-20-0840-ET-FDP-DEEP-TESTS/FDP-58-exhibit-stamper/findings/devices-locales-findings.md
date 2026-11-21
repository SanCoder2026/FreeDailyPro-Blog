Sent: 2026-11-21 11:52 ET

# Devices, locales, geo, a11y (FDP-58), checked against screenshots

- **Devices (10):** all 200 and usable. iPhone SE scrollWidth 329 at 320 (header button, site-wide). Others no overflow.
- **Locales:** html lang correct per locale, dir ltr. Nav, trial strip and Drive button are translated; **H1 "Exhibit Stamper", subtitle, drop zone and FAQ stay English** (de and ja fold screenshots). de/fr show "1 $"-style prices (script found no `$1`, screenshot shows the strip). ja desktop 1369 px (3 px, site-wide). /ar probe → "Hmm, we couldn't find that page" (no ar hreflang; expected).
- **Geo:** prices stay USD everywhere. EU consent banner **visible** in de-DE and fr-FR fold screenshots ("We use cookies for analytics and, when ads are shown, advertising…" Accept all / Reject non-essential / Choose) even though the script's `consent` flag said false. No banner in US/IN/SA/JP.
- **axe:** desktop: label-content-name-mismatch (serious, `.right-2`), region (moderate). Pixel 7: color-contrast (serious) on the "Advertisement" captions.
