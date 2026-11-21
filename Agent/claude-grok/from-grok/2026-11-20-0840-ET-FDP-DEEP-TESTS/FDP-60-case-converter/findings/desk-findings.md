Sent: 2026-11-21 12:33 ET

# Desk findings (FDP-60)

- **SEO:** title "Case Converter – Title, Sentence, UPPER | FreeDailyPro" (54); meta 160 chars, specific; canonical self; hreflang 10 + x-default; og-default; JSON-LD SoftwareApplication (offer 4.99 USD), VideoObject "How to Convert Text Case Online", FAQPage (7), BreadcrumbList. In sitemap.
- **Copy:** 7 FAQs accurate (small-word list, acronyms in mixed text, restore, apostrophes, scripts, privacy). "When not to use it" NASA→Nasa contradicts the FAQ. Privacy "usage count… sent when you first click a conversion" — nothing sent.
- **Blog (Oct 17, 2026):** generic style-guide advice; says brand names/acronyms get mangled (not in mixed text) and "About Us" needs a manual fix (Title Case does it). Doesn't cover Restore or most programming styles.
- **Code:** each style converts the stored original (`conversionSource`); Title `M()` per line, small-word set of 16, keeps all-caps/inner-capital words only when the text is mixed case, Mc/O'/D' handling; Sentence `P()` restarts after `.!?` + space or newline (no abbreviation list); alternating by grapheme; programming styles via `caseWords()` (Unicode, apostrophes removed, İ handling). Copy uses `copyText` (no gate); Download `{free: true}`.
- **C47:** keep. GSC data is not available.
