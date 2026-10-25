# Blog brief for Grok: promoting the FreeDailyPro API and MCP server

Read `docs/1-NEW-BLOG-RULES.md` first. Every rule there applies (frontmatter limits, 1000+ words,
3+ `##` sections, 1-4 real tool ids from `docs/tool-ids.txt` linked in the body, video embeds,
hero image, no invented stats, no "#1", no "free" in titles). This brief only adds what is specific to
the API/MCP campaign.

Output: `Agent/site/batch-YYYYMMDD/posts/<slug>.md`, `images/<slug>.webp`, `INDEX.md`.

## Goal
Help developers and AI-agent users find the FreeDailyPro API and MCP server, and send them to
https://www.freedailypro.com/developers. Posts should teach something useful first; the API is the
natural next step, not a sales pitch.

## What exists (the only facts you may state)
- One API at api.freedailypro.com, six products: PDF Toolkit, Text and Developer Utilities,
  Finance/Tax/Health/Planning Calculators, Business Documents, Image/Audio/Video Conversion, Book Publishing.
- One MCP server, same address, 178 tools, usable from Claude Desktop, Cursor and other MCP clients.
- Nothing sent is stored; sessions are erased.
- Developers page: https://www.freedailypro.com/developers (key generation, docs, listings status).

## Listing status (state exactly this, nothing more)
LIVE today: Official MCP Registry (com.freedailypro/tools), Glama, RapidAPI (all six products),
Postman public collection.
IN REVIEW (submitted, not public): API.market, ApyHub, APILayer. Say "submitted and awaiting approval"
or leave them out. Never link to them or call them live.

Verified links you may use:
- RapidAPI profile: https://rapidapi.com/user/freedailypro
- PDF: https://rapidapi.com/freedailypro/api/pdf-toolkit-api8
- Text: https://rapidapi.com/freedailypro/api/text-and-developer-utilities-api
- Calculators: https://rapidapi.com/freedailypro/api/finance-tax-health-and-planning-calculator-api
- Business: https://rapidapi.com/freedailypro/api/business-document-api
- Media: https://rapidapi.com/freedailypro/api/image-audio-and-video-conversion-api
- Book publishing: https://rapidapi.com/freedailypro/api/book-publishing-api
- Postman: https://documenter.getpostman.com/view/57830674/2sBYAytUod
- Official MCP Registry: https://registry.modelcontextprotocol.io (search "freedailypro")

## Hard don'ts
- No link to any GitHub repo. No mention of Zyla or mcp.so.
- No prices, rate limits, latency or usage numbers you were not given.
- No claim of "free forever"; "free" only in meta/SEO text if at all.
- No security or compliance claims beyond "nothing sent is stored".
- Do not describe a tool the site does not have; check `docs/tool-ids.txt`.

## Posts to write (10, in priority order)
| # | Working title | Link these tools | Angle |
|---|---|---|---|
| 1 | Add 178 tools to Claude Desktop with one MCP server | merge-pdf, word-counter | Setup walkthrough, config snippet, 3 example prompts |
| 2 | Use FreeDailyPro tools inside Cursor | hash-generator, regex-tester, jwt-decoder | Developer workflow, MCP in the editor |
| 3 | Merge, split and compress PDFs from code | merge-pdf, split-pdf, compress-pdf | REST call example, when to use API vs web tool |
| 4 | Redact and watermark PDFs in an automated workflow | redact-pdf, pdf-watermark | Document pipeline, privacy-first (nothing stored) |
| 5 | Loan, tax and retirement calculators as JSON | loan-calculator, income-tax-calculator, 401k-calculator | Embed calculators in an app or spreadsheet |
| 6 | Generate pay stubs and invoices through an API | pay-stub-generator, invoice-generator | Small-business automation |
| 7 | Convert images, audio and video with one API | convert-image, audio-converter, convert-video | Media pipeline, file-size tips |
| 8 | ISBN checks, spine width and royalty math for self-publishers | isbn-checker, book-spine-calculator, print-royalty-calculator | Publishing automation |
| 9 | UUIDs, hashes and slugs: the utility endpoints developers reuse | uuid-generator, hash-generator, slug-generator | Quick reference with sample requests |
| 10 | Where to find the FreeDailyPro API: MCP directories and marketplaces | word-counter | Roundup of the live listings above, honest "in review" note |

Each post: use `topic: guides` unless a category id clearly fits; add persona/workflow tags only from
the rules file. End with the one-question closing paragraph linking /contact, plus a clear line
pointing to https://www.freedailypro.com/developers.

## Code samples
Use placeholders only: `X-API-Key: YOUR_API_KEY`. Never write a real key. Keep requests minimal and
mark any parameter you are unsure of as "see the docs on the developers page" rather than guessing.

## Quality check before handoff
1. Tool ids all exist in `docs/tool-ids.txt`.
2. Every URL is from the verified list above or the site itself.
3. Listing claims match the status section.
4. Run `node scripts/build-blog.mjs --check` and fix errors.
