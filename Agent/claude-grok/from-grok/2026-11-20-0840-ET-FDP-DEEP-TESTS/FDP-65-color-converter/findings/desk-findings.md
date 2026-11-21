Sent: 2026-11-21 14:26 ET

# Desk findings (FDP-65)

- Limitations say oklch is rejected; it is accepted. How-to row list omits LAB/OKLCH; contrast lines not mentioned; "use the Contrast Checker" while contrast is on the page.
- Blog: accurate on formats and alpha, but "each valid colour you convert can count towards your daily trial uses" contradicts live behaviour.
- Code: `useLogToolUsage(hasResult, 3000, {ownActions})` wraps `navigator.clipboard.writeText` and a document copy listener through `tryUse`, active only when the tool is "known"; live it is inactive. The copy listener checks `window.getSelection()`, which is empty for selections inside inputs.
- SEO: title "Color Converter Online - HEX, RGB, HSL | FreeDailyPro"; meta 69 chars; canonical self; 10 hreflang + x-default; JSON-LD SoftwareApplication, Offer 4.99, FAQPage, VideoObject, BreadcrumbList; OG generic.
- Links: Brand Studio, Gradient Generator, Color Palette, Logo Maker, both blogs → 200.
