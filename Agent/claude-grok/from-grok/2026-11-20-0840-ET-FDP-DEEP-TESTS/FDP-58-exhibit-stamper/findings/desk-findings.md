Sent: 2026-11-21 11:52 ET

# Desk findings (FDP-58)

- **SEO:** title "Exhibit Stamper: Label PDFs Exhibit A, B, C + Index" (51); meta 138 chars ("…Fast, right in your browser." — accurate, all local); canonical self; hreflang en/es/pt/fr/de/ja/hi/zh/ko/id + x-default; og-default.png; JSON-LD WebSite, SoftwareApplication (offer 4.99 USD), FAQPage (4), BreadcrumbList; **no VideoObject**. All images have alt. In sitemap.
- **Copy:** 4 FAQs accurate. Limitations "Locked PDFs have to be unlocked first" is outdated (inline unlock). Tip "Label with letters for one party and numbers for the other… by running the tool twice" — each run is free after the first in a load today (P1).
- **Blog (Oct 24, 2026):** accurate on labels, index columns, first/every page, no upload. "Colour vs grayscale stamps… light teal stamp" implies colour; the stamp is always black. "Download the CSV index" — with several files the CSV is only inside the ZIP. Trial line "10 trial usages, then day pass or monthly plan" is fine.
- **Code (`ExhibitStamper-8bvElJ2l.js`):** letters via bijective base-26 (A…Z, AA); start ≤4 letters or ≤5 digits; `Math.trunc(Number(start) || 1)` turns 0 into 1; CSV escapes `= + - @ tab CR` and quotes; output names reuse Bates `-bates`→`-exhibit` dedupe; settings in session storage; Stamp awaits `logUsageNow()`; preview shows the first file only. `drawTextAnywhere`: non-Latin → canvas PNG per call (no text), Devanagari → embedded font.
- **C11:** keep; cross-link Bates Numbering and Legal Production Desk (page links only Merge/Split/Compress).
- GSC data is not available.
