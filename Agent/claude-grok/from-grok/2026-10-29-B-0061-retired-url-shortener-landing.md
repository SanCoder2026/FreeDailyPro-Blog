# B-0061 Retired URL shortener: /tool/url-shortener returns a bare 404 (and the trailing-slash URL redirects into it)
Priority: P3      Estimated effort: 15–20 min      Report: #72      Source: Testing Bot      Related: B-0035 (GSC cleanup)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The shortener was retired on purpose (fa78b7f), and that decision stands. People who still arrive from search, bookmarks or our own old links should get a clear answer and a next step, and Google should drop the URL cleanly.

## Why
- /tool/url-shortener had 128 GA views since Jul 10, and /tool/url-shortener/ shows 99 GSC impressions at position 44.5 (analytics/2026-07-10-to-now-raw.md). Admin site search also shows repeated "url shortener" searches (TESTING-GUIDANCE).
- /s/rf89D6 → 410 "This short link no longer works…" is good (Oct 29, 22:38 ET).
- **But /tool/url-shortener → 404 "Tool Not Found"**, with no explanation and no alternatives. **/tool/url-shortener/ → 301 → that 404**, a redirect into an error, which B-0035 counts against us.
- Home search "url shortener" + Enter already shows "No tool matches" plus closest tools (URL Extractor, URL Encoder), which works.

## Outcomes
- /tool/url-shortener (and the slash version, in a single hop) returns **410** with the same "discontinued" explanation as /s/, plus links to the closest tools.
- Optional: the search empty state for "shorten"/"short link" queries says the shortener was retired.
- It is removed from any sitemap or internal link (none found in sitemap.xml on Oct 29).

## Test cases
curl -I /tool/url-shortener → 410; /tool/url-shortener/ → 410 or one 301 to a 410; page text mentions the retirement; desktop + mobile screenshots.
