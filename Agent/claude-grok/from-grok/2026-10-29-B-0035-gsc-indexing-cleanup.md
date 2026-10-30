# B-0035 Search Console indexing cleanup: canonical-only links and sitemap, find 404 sources

**Priority:** P1
**Estimated effort:** ~2 h

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: read-only pull from GA4 (28d Oct 1–28), Search Console (3 months Jul 28–Oct 27; indexing updated 10/22) and AdSense (earnings since Oct 24), taken Oct 29 2026. Totals: 3,412 GA users, GSC 548 clicks / 154K impressions / 0.4% CTR / avg position 18.1, AdSense $0.39.

## Intent
Make Google spend its crawl budget on our real, canonical tool pages, so more of our 300+ tools get indexed and ranked.

## Why
- GSC: Indexed 1.05K, **Not indexed 1.18K**.
- **Page with redirect: 229.** We are still linking to or listing URLs that redirect. Trailing slashes are a likely cause: GSC shows `/tool/url-shortener/` getting impressions separately.
- **Duplicate, Google chose different canonical than user: 76.** Our canonical signals conflict.
- Alternate page with proper canonical: 483. This is mostly expected for /es/ and other locales, but check that hreflang and canonical agree.
- **Discovered – currently not indexed: 328**, and Crawled – currently not indexed: 43. This is a crawl budget and quality signal.
- **Not found (404): 8, Soft 404: 4.** In GA, "Page Not Found | FreeDailyPro" got 87 views plus "Page not found" 26 in the last 7d, so real users are hitting dead links.
- noindex 9, robots-blocked 1. Confirm these are intentional.

## Outcomes
- Every internal link, nav, footer, related-tools block, blog link and hreflang entry points to the final canonical URL: no redirect hop, one consistent trailing-slash policy.
- sitemap.xml lists only 200, indexable, self-canonical URLs. No redirects, noindex, /s/ short links, /admin or /profile.
- Each page's canonical tag matches the URL in the sitemap and its internal links. Locale pages use self-canonical plus hreflang, unless you find a reason not to.
- 404 sources are identified. Log the referrer/path on the 404 page, e.g. a GA event `page_not_found` with `page_path` and `page_referrer`. Fix the linking source, or 301 to the closest tool. Soft 404s return a real 404 or get real content.
- Report: counts before/after from a crawl of our own site, the list of fixed 404 paths, and sitemap URL count. Over the next 2–4 weeks, GSC redirect + duplicate-canonical counts should trend down and indexed should trend up.

## Suggested direction (interpret freely)
Crawl the live site and sitemap, e.g. with a small script, and flag any URL that returns 3xx/4xx or has a canonical ≠ self. Fix this at the source: route helpers and link components. Don't patch links one by one.

## Constraints
- Don't noindex or remove real tool pages to make the numbers look better.
- Keep the existing /es/ and locale strategy; just make the signals consistent.
- Small SEO links stay small (owner decision, B-0024).

## Not in scope / do not decide
Changing URL structure or slugs of live tools.

## Owner decisions needed
None. After deploy, the owner or a bot will click "Validate fix" in GSC; tell us when.

## Source
owner
