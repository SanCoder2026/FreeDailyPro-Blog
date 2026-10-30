# B-0052 /es/ tool pages point hreflang at the homepage; tool pages double hreflang and JSON-LD after hydration
Priority: P1      Estimated effort: 60 min      Report: #66      Source: Testing Bot

**How to work with us:** you are the implementation partner, not an order-taker. Inspect the real code and past deploy patterns, challenge anything weak, choose the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID (done | partial | blocked, live and checked).

## Intent
Make Google understand each language version of a tool page correctly so /es/ pages can rank in their own right.

## Why
- /es/tool/roman-numeral-converter: 8 clicks / 8,435 impressions, pos 8.2 (GSC, raw.md) — our second-largest impression URL.
- Raw HTML of that page (`curl -s …/es/tool/roman-numeral-converter | grep hreflang`): hreflang en/es/fr/… = **/ , /es, /fr …** (homepage set), and `<html lang="en">`. The EN page's raw HTML has the correct tool-level set. After hydration the es page has both sets (22 links).
- Every tool page checked (roman, audio-comparer, merge-pdf, camera-capture) ends up with **22 hreflang links** (the 11-link set twice) and **SoftwareApplication, VideoObject, FAQPage, BreadcrumbList each twice** in the rendered DOM (raw HTML has 2 ld+json blocks).
- GSC already reports 76 "Duplicate, Google chose different canonical" and 483 "Alternate page with proper canonical" (raw.md).
- Minor: /es roman desktop scrollWidth 1283 at 1280 viewport.

## Outcomes
- Every /{lang}/tool/{slug} page: hreflang set references the same tool in each language + x-default; html lang matches the locale.
- Exactly one hreflang set and one JSON-LD graph per page, both in raw HTML and after hydration.
- (Spanish copy for the roman page itself is B-0036 — not in scope here.)

## Test cases
R66-ROM-11 (curl raw es page: expect tool-level hreflang + lang="es"); R66-ROM-12 (Playwright rendered DOM: count `link[rel=alternate][hreflang]` = 11 and one of each schema @type) on /tool/roman-numeral-converter, /es/tool/roman-numeral-converter, /tool/audio-comparer, /tool/merge-pdf. Script: test-cases/meta.py → meta.json.
Owner decisions needed: none.
