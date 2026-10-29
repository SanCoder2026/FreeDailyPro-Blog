# B-0020 Developer use-case pages in the sitemap return 404
Priority: P1 (must-do)      Estimated effort: 40 min

## Goal / why
Seven URLs listed in the sitemap return HTTP 404. Search engines treat this as a broken site signal, and these pages target developers searching for specific APIs, which is the API/MCP revenue path ($24 / $69 / $129 plans).

## What to change
These URLs (checked live by Grok on 2026-10-29 at about 5:15 PM ET, all HTTP 404, sitemap itself returns 200 with 863 URLs):
- https://www.freedailypro.com/developers/use-cases/pdf-merge-api
- https://www.freedailypro.com/developers/use-cases/json-to-powerpoint-api
- https://www.freedailypro.com/developers/use-cases/pay-stub-api
- https://www.freedailypro.com/developers/use-cases/isbn-validation-api
- https://www.freedailypro.com/developers/use-cases/image-resize-api
- https://www.freedailypro.com/developers/use-cases/loan-calculator-api
- https://www.freedailypro.com/developers/use-cases/word-count-api
Find why the route does not render them (route params, static generation, missing data entries, sitemap builder listing slugs that have no page). Preferred fix: real pages built from the same template as the existing developer use-case pages, each pointing to the matching real endpoint in the OpenAPI spec. If an endpoint does not exist, remove that slug from the sitemap and from any hub links instead of making a page for it.

## Acceptance criteria
- Each of the 7 URLs returns 200 with a unique title, meta description, H1 and canonical, or is no longer in the sitemap or linked anywhere.
- No other sitemap URL starts returning 404 (spot-check the /developers/use-cases/ set).
- Report which slugs became pages and which were delisted; verification `live and checked` after deploy.

## Not in scope / do not decide
API pricing or plan limits. New API endpoints. Other developer pages' copy. Marketing counts (API/MCP figure stays 215+ REST / 211+ MCP).

## Owner decisions needed
none

Source: Testing Bot (Cycle 1.5 ranked list, Oct 28) + SEO bot; re-verified live by Grok 2026-10-29.
