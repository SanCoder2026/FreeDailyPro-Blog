# B-0036 CTR lift on high-impression pages: titles, meta, content/FAQ to reach top 5

**Priority:** P1
**Estimated effort:** ~3 h

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: read-only pull from GA4 (28d Oct 1–28), Search Console (3 months Jul 28–Oct 27; indexing updated 10/22) and AdSense (earnings since Oct 24), taken Oct 29 2026. Totals: 3,412 GA users, GSC 548 clicks / 154K impressions / 0.4% CTR / avg position 18.1, AdSense $0.39.

## Intent
Turn impressions we already earn into clicks. This is the cheapest traffic growth available to us.

## Why
- **154K impressions, 548 clicks, 0.4% CTR, avg position 18.1.**
- **"roman numeral converter": 43,953 impressions at position 9.1, 52 clicks.** The page /tool/roman-numeral-converter has 34,629 impr at pos 9.6 with 45 clicks, and /es/tool/roman-numeral-converter has 8,435 impr at pos 8.2 with 8 clicks. Moving from #9 to the top 3–5 could mean hundreds of clicks a month.
- Other page-1 / near-page-1 queries with weak clicks:
  - tax calculator: 4,746 impr, pos 7.1, 4 clicks (/tool/income-tax-calculator 7,444 impr, pos 7.5)
  - unit converter: 4,424 impr, pos 7.1, 2 clicks (/tool/unit-converter 4,782 impr, pos 7.4)
  - barcode generator: 1,513 impr, pos 5.4, 1 click (page 2,021 impr, pos 7.4)
  - spell check: 408, pos 6.8; crop pdf online free: 117, pos 6.9; jwt decode online: 76, pos 8.4; yt thumbnail downloader: 72, pos 7.8
  - /tool/text-paraphraser: 1,691 impr, pos 9.8
  - /tool/grammar-checker: 8,350 impr, pos 21.3 (needs content depth more than a title change)
  - /tool/camera-capture: 2,336 impr, pos 13.7, 48 clicks
  - /tool/audio-comparer: 2,390 impr, pos 11.3, 121 clicks. This is our best clicker, so protect it and push it into the top 5.
- High impressions with ~0 clicks: word-counter 3,670; tip-calculator 2,914; es citation-generator 2,700; keyword-density 2,558; startup-name-generator 2,139; college-529-calculator 2,029.

## Outcomes
- Rewritten title + meta description for the pages above: keyword first, a clear benefit, and **keep "free"** in SEO title/meta (owner rule).
- Each target page gets useful on-page content below the tool: a short how-to, examples, edge cases (e.g. Roman numerals above 3,999, vinculum, years/dates), and an FAQ with FAQPage schema where it's honest. Use internal links to related tools.
- Spanish /es/ roman page gets the same treatment, in natural Spanish.
- Report a table: page, old title/meta, new title/meta, content added. We'll re-check GSC CTR and position in 2 and 4 weeks. Target: roman converter in the top 5 and overall CTR above 1%.

## Suggested direction (interpret freely)
Start with roman numeral converter, income-tax, unit converter and barcode, which have the largest impressions at page-1 positions. Then do the zero-click list. If titles are template-generated, improve the template plus per-tool overrides rather than hardcoding.

## Constraints
- No keyword stuffing or fake reviews or ratings. Make no claims the tool can't back up.
- Don't slow the tool down. Keep content below the tool and keep the tool above the fold.
- Count wording, if used: "300+ professional tools, premium applications and workflow products".

## Not in scope / do not decide
Changing slugs; paid ads.

## Owner decisions needed
None.

## Source
owner
