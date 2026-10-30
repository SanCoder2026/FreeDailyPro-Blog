# B-0037 Analytics hygiene: filter bot traffic, set up real key events, verify purchase

**Priority:** P1
**Estimated effort:** ~2 h

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: read-only pull from GA4 (28d Oct 1–28), Search Console (3 months Jul 28–Oct 27; indexing updated 10/22) and AdSense (earnings since Oct 24), taken Oct 29 2026. Totals: 3,412 GA users, GSC 548 clicks / 154K impressions / 0.4% CTR / avg position 18.1, AdSense $0.39.

## Intent
Get numbers we can trust, so revenue decisions, video claims and the admin funnel reflect real humans and real conversions.

## Why
- **Singapore: 1,162 of 3,412 users (34%) with 1.29% engagement**, 15 engaged sessions and 0 key events. Realtime at ~9:05 PM EDT Oct 29 showed 10 of 10 active users from Singapore. This is almost certainly bot or datacenter traffic.
- Direct is 2,565 sessions (68%) at 7.76% engagement with 2s avg engagement. This looks bot-inflated too. A 7d engagement of 8% vs 17% over 28d suggests bot traffic is growing (Oct 23 spike: 440 users).
- Real humans look like: Organic Search 56% engaged, Organic Social 87%, Referral 73%, AI Assistant 70%, and India 62%.
- Key events: 97 over 28d, but we can't tell which events they are. tool_completed fires 275 times for 14 users. **purchase = 1 (cd /workspace/FreeDailyPro-Blog/Agent/claude-grok/from-grok && H='**How to work with us:** you'"'"'re the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

Context: read-only pull from GA4 (28d Oct 1–28), Search Console (3 months Jul 28–Oct 27; indexing updated 10/22) and AdSense (earnings since Oct 24), taken Oct 29 2026. Totals: 3,412 GA users, GSC 548 clicks / 154K impressions / 0.4% CTR / avg position 18.1, AdSense $0.39.'
cat > 2026-10-29-B-0035-gsc-indexing-cleanup.md <<EOF
# B-0035 Search Console indexing cleanup: canonical-only links and sitemap, find 404 sources

**Priority:** P1
**Estimated effort:** ~2 h

$H

## Intent
Make Google spend its crawl budget on our real, canonical tool pages, so more of our 300+ tools get indexed and ranked.

## Why
- GSC: Indexed 1.05K, **Not indexed 1.18K**.
- **Page with redirect: 229.** We are still linking to or listing URLs that redirect. Trailing slashes are a likely cause: GSC shows \`/tool/url-shortener/\` getting impressions separately.
- **Duplicate, Google chose different canonical than user: 76.** Our canonical signals conflict.
- Alternate page with proper canonical: 483. This is mostly expected for /es/ and other locales, but check that hreflang and canonical agree.
- **Discovered – currently not indexed: 328**, and Crawled – currently not indexed: 43. This is a crawl budget and quality signal.
- **Not found (404): 8, Soft 404: 4.** In GA, "Page Not Found | FreeDailyPro" got 87 views plus "Page not found" 26 in the last 7d, so real users are hitting dead links.
- noindex 9, robots-blocked 1. Confirm these are intentional.

## Outcomes
- Every internal link, nav, footer, related-tools block, blog link and hreflang entry points to the final canonical URL: no redirect hop, one consistent trailing-slash policy.
- sitemap.xml lists only 200, indexable, self-canonical URLs. No redirects, noindex, /s/ short links, /admin or /profile.
- Each page's canonical tag matches the URL in the sitemap and its internal links. Locale pages use self-canonical plus hreflang, unless you find a reason not to.
- 404 sources are identified. Log the referrer/path on the 404 page, e.g. a GA event \`page_not_found\` with \`page_path\` and \`page_referrer\`. Fix the linking source, or 301 to the closest tool. Soft 404s return a real 404 or get real content.
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
EOF
cat > 2026-10-29-B-0036-ctr-lift-high-impression-pages.md <<EOF
# B-0036 CTR lift on high-impression pages: titles, meta, content/FAQ to reach top 5

**Priority:** P1
**Estimated effort:** ~3 h

$H

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
EOF
cat > 2026-10-29-B-0037-analytics-hygiene-key-events.md <<EOF
# B-0037 Analytics hygiene: filter bot traffic, set up real key events, verify purchase

**Priority:** P1
**Estimated effort:** ~2 h

$H

## Intent
Get numbers we can trust, so revenue decisions, video claims and the admin funnel reflect real humans and real conversions.

## Why
- **Singapore: 1,162 of 3,412 users (34%) with 1.29% engagement**, 15 engaged sessions and 0 key events. Realtime at ~9:05 PM EDT Oct 29 showed 10 of 10 active users from Singapore. This is almost certainly bot or datacenter traffic.
- Direct is 2,565 sessions (68%) at 7.76% engagement with 2s avg engagement. This looks bot-inflated too. A 7d engagement of 8% vs 17% over 28d suggests bot traffic is growing (Oct 23 spike: 440 users).
- Real humans look like: Organic Search 56% engaged, Organic Social 87%, Referral 73%, AI Assistant 70%, and India 62%.
- Key events: 97 over 28d, but we can't tell which events they are. tool_completed fires 275 times for 14 users. **purchase = 1 ($1.00)**, which doesn't match our known Stripe activity or prices, so it may be a test or the wrong value.
- There's no limit_hit or checkout_start event, so we can't see the funnel from tool use → trial limit → checkout → purchase.

## Outcomes
- **Events** (GA4 + our own admin funnel) with consistent params (tool_slug, tier premium/professional, plan, value, currency):
  - \`tool_completed\` (audit: 275/14 users looks like repeat firing; dedupe per run)
  - \`limit_hit\` (Premium 2/day and Professional 10/day trial limits)
  - \`checkout_start\` (Day Pass / monthly / API)
  - \`purchase\` fired from a server-confirmed Stripe success (webhook or verified session), with real value and currency and transaction_id for dedup
- **Purchase verification:** trace the single \$1 purchase (test mode? hardcoded value?) and report what it was. Make sure test-mode payments don't fire production purchase events.
- **Bot / internal traffic:**
  - Our admin funnel/revenue panel excludes known bots, our own and internal traffic (admin users, box/agent browsers), and datacenter traffic. Use UA/bot heuristics, server-side signals and an internal flag, and show the "excluded" count transparently.
  - Write a short owner guide in \`from-claude/\` for GA4 Admin steps the owner does himself: mark the 4 events as key events; define internal traffic (traffic_type=internal) with a data filter; a "Likely bots" comparison/segment (Singapore + Direct + <1s engagement); and enable bot filtering notes. Bots don't change GA settings (owner rule: test and review only).
- After deploy: a test run shows each event in GA DebugView/Realtime and in the admin funnel. Report screenshots or logs.

## Constraints
- Privacy honesty: no new PII in events. Respect the cookie/consent behavior already shipped.
- Don't block Singapore users at the edge. Real users there must still work. Filter in reporting; only rate-limit clearly abusive automation.
- Trial limits stay at Premium 2/day and Professional 10/day.

## Not in scope / do not decide
Changing GA property settings yourself; changing trial limits.

## Owner decisions needed
The owner applies the GA4 Admin settings from the guide.

## Source
owner
EOF
cat > 2026-10-29-B-0038-adsense-viewability-placement.md <<EOF
# B-0038 AdSense: raise viewability and RPM with better placements, without hurting UX

**Priority:** P2
**Estimated effort:** ~1.5 h

$H

## Intent
Earn more from the ads we already show by putting them where real users actually look, while keeping tools fast and clean and never interfering with paying.

## Why
- Earnings started Oct 24: **\$0.39 over 7d**, 1,055 page views, **page RPM \$0.37**, impression RPM \$2.23, 173 impressions, 5 clicks.
- **Active View viewability 18.56%.** Most ads load where nobody sees them, either far below the fold or in hidden containers.
- Only 173 ad impressions over 1,055 page views, so most page views get no ad at all.
- Ad unit report: "Tool Page Inline" \$0.04 / 73 imp, In Article 1 imp. Auto ads + Auto optimize ON, 0 page exclusions.
- US page RPM is \$0.68. Much of the traffic is low-value or bot (see B-0037), which drags RPM down.
- ads.txt authorized, no policy issues. Payout needs a \$10 balance.

## Outcomes
- A tool-page placement shown **right after the user gets their result** (near the output/download area, the moment they're looking), with reserved space so there's no layout shift.
- One responsive unit lower on the page, beside the how-to/FAQ content from B-0036, lazy-loaded so it's in view when rendered.
- Blog articles get an in-article unit after the first sections.
- **Page exclusions for Auto ads and no manual ads** on checkout, pricing/payment dialogs, login, profile, admin and API-key pages. Paid/logged-in plan users get whatever the plan promises; check that no ad shows if ad-free is a plan benefit.
- Don't fill containers that are hidden or collapsed (that's what kills Active View).
- Report: placements changed, CLS/LCP before/after. Target in 2–3 weeks: viewability above 50%, page RPM up, no Core Web Vitals regression.

## Constraints
- Never place ads next to buttons in a way that invites accidental clicks (AdSense policy), or inside the tool's working area.
- Keep tool UX first. Output must stay visible without scrolling past an ad.
- Changes in the AdSense console (Auto ads formats, exclusions) are written up for the owner to apply. Bots don't change console settings.

## Not in scope / do not decide
New ad networks; adding ads to checkout.

## Owner decisions needed
Apply the AdSense console page exclusions/format tweaks from your note.

## Source
owner
EOF
mkdir -p /workspace/freedailypro-growth-orchestrator/claude-briefs && cp 2026-10-29-B-003[5-8]*.md /workspace/freedailypro-growth-orchestrator/claude-briefs/
cd /workspace/FreeDailyPro-Blog && git log --oneline origin/main..main && git status --short.00)**, which doesn't match our known Stripe activity or prices, so it may be a test or the wrong value.
- There's no limit_hit or checkout_start event, so we can't see the funnel from tool use → trial limit → checkout → purchase.

## Outcomes
- **Events** (GA4 + our own admin funnel) with consistent params (tool_slug, tier premium/professional, plan, value, currency):
  - `tool_completed` (audit: 275/14 users looks like repeat firing; dedupe per run)
  - `limit_hit` (Premium 2/day and Professional 10/day trial limits)
  - `checkout_start` (Day Pass / monthly / API)
  - `purchase` fired from a server-confirmed Stripe success (webhook or verified session), with real value and currency and transaction_id for dedup
- **Purchase verification:** trace the single $1 purchase (test mode? hardcoded value?) and report what it was. Make sure test-mode payments don't fire production purchase events.
- **Bot / internal traffic:**
  - Our admin funnel/revenue panel excludes known bots, our own and internal traffic (admin users, box/agent browsers), and datacenter traffic. Use UA/bot heuristics, server-side signals and an internal flag, and show the "excluded" count transparently.
  - Write a short owner guide in `from-claude/` for GA4 Admin steps the owner does himself: mark the 4 events as key events; define internal traffic (traffic_type=internal) with a data filter; a "Likely bots" comparison/segment (Singapore + Direct + <1s engagement); and enable bot filtering notes. Bots don't change GA settings (owner rule: test and review only).
- After deploy: a test run shows each event in GA DebugView/Realtime and in the admin funnel. Report screenshots or logs.

## Constraints
- Privacy honesty: no new PII in events. Respect the cookie/consent behavior already shipped.
- Don't block Singapore users at the edge. Real users there must still work. Filter in reporting; only rate-limit clearly abusive automation.
- Trial limits stay at Premium 2/day and Professional 10/day.

## Not in scope / do not decide
Changing GA property settings yourself; changing trial limits.

## Owner decisions needed
The owner applies the GA4 Admin settings from the guide.

## Source
owner
