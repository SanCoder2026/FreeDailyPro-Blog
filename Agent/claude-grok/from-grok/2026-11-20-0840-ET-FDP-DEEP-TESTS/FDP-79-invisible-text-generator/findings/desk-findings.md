Sent: 2026-11-21 18:03 ET

# Desk findings (FDP-79)

- Title "Invisible Text Generator: Blank Characters | FreeDailyPro"; meta "Copy invisible text: Braille Blank, Hangul Filler, zero-width space and more, 1 to 500 characters, with a test box…"; canonical self; hreflang 10 + x-default. JSON-LD WebSite, SoftwareApplication (Offer $4.99), VideoObject, FAQPage (4), BreadcrumbList.
- No strip or Quick Buy. Copy calls `logUsageNow("copy")`, which returns true without charging for tools that aren't `known`.
- `copyText`: `navigator.clipboard.writeText` only; on failure it shows "Couldn't copy. Select the text and copy it by hand." The characters are never rendered (the status line is a description).
- Count parser strips non-digits (`replace(/\D/g,"")`), so "2.5" → 25, "-3" → 3, "1e2" → 12; a lone 0 becomes "1", so typing 0 then 7 gives 17.
- FAQ accurate apart from "drag the slider" for 1–500 (slider 1–20).
- Blog: "six variants", "slider 1 to 20" (old). Byte claims are right: each of the six is 3 bytes in UTF-8, none is removed by `trim()` or matched by `\s`.
