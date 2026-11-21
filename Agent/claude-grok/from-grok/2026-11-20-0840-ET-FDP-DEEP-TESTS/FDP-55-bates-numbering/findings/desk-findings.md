Sent: 2026-11-21 10:39 ET

# Desk findings (FDP-55)

- **SEO:**
  - Title "Bates Numbering for PDFs: Stamp Pages and Get an Index" (55 chars).
  - Meta "Stamp a running document number… Fast, right in your browser." (accurate here: all local).
  - Canonical is self; hreflang en/es/pt/fr/de/ja/hi/zh/ko/id + x-default; og:image og-default.png.
  - JSON-LD: WebSite, SoftwareApplication, VideoObject, FAQPage (7), BreadcrumbList.
- **FAQ:** accurate on features. "Does it add a mark on trial? No…" is a design choice (owner question). "one use … however many files you number in the run" matches the per-load gap.
- **Limitations:** "Password-protected and damaged files are left out and marked in the list" is wrong (they are prompted or toasted and never listed).
- **Blog /blog/stamp-bates-numbers-across-pdf-set (Oct 24, 2026):**
  - Features are accurate: digits, -2 names, 30-char prefix, legend corner, overflow warning.
  - Trial note says one use "however many files you number in that visit" (per-load).
  - Two sections ("Digit width…", "Prefix, suffix…") appear after "Closing next step".
- **Code:**
  - Settings persist in session storage.
  - The run awaits `logUsageNow()`.
  - CSV escapes `= + - @`.
  - `drawTextAnywhere` (fontkit) draws non-Latin text without an extractable text layer.
- **C11 duplicates:** keep. Cross-link Legal Production Desk and Exhibit Stamper from the tool page (only Merge/Split/Compress shown today).
- GSC data is not available.
