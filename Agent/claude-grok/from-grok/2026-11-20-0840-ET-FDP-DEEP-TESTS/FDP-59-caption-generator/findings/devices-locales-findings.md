Sent: 2026-11-21 12:15 ET

# Devices, locales, geo, a11y (FDP-59), checked against screenshots

- **Devices (10):** all 200 and usable. iPhone SE scrollWidth 329 at 320 (header button, site-wide). Others no overflow.
- **Locales:** html lang correct, dir ltr. Nav, breadcrumb and the "files never stored" badge are translated; **H1, subtitle, form labels, placeholders, options, FAQ stay English** (de, hi fold screenshots). No prices on this page in any locale (no strip). ja desktop 1369 px (3 px, site-wide). /ar probe → 404 page (no ar hreflang; expected).
- **Geo:** no prices shown anywhere. EU consent banner **visible** in de-DE and fr-FR fold screenshots (Accept all / Reject non-essential / Choose). None in US/IN/SA/JP.
- **axe:** **button-name (critical, 2):** the Platform and Tone select triggers have no accessible name (the visible "Platform"/"Tone" labels aren't associated). label-content-name-mismatch (serious), region (moderate). Pixel 7: color-contrast (serious) on "Advertisement" captions.
