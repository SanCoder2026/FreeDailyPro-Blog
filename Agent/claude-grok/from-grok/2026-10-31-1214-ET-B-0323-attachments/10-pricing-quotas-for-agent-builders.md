---
title: "Pricing & quotas explained: 20k trial → paid upgrades for agent builders"
meta_description: "How FreeDailyPro API metering works for agents — shared quotas, 429s, plan tiers, and what is not included."
---

# Pricing & quotas explained (for agent builders)

## The one-key model

- One API key
- One **shared** monthly call count across **every** category (PDF, PPTX, media, text, calculators, business docs, publishing)
- A PDF merge and a word-count cost **the same** (one call each)
- MCP and REST share that pool

## Plans (as published on developers)

| Plan | Price | Calls / month | Notes |
|------|-------|---------------|-------|
| Trial | $0 | 20,000 | No credit card |
| Premium | $24/mo | 200,000 | |
| Ultra | $69/mo | 750,000 | |
| Mega | $129/mo | 2,000,000 | Priority |

Upgrade on [https://www.freedailypro.com/developers](https://www.freedailypro.com/developers).

## What happens at the limit

Over quota → **HTTP 429** with limit/usage in the body. Calls are not silently queued. Reset is the next billing cycle — or upgrade.

## 401 vs 404 (save your weekend)

| Code | Meaning |
|------|---------|
| 401 | Route exists; key missing/wrong/revoked |
| 404 | Route does not exist (OpenAPI is source of truth) |

Regenerating a key **immediately revokes** the previous one in Claude, Cursor, Postman, RapidAPI, and `.env` files.

## Not the same product: browser tools

Website browser tools have a separate **10 uses/day** style limit. Do **not** mix that story into API marketing or agent docs.

## Gaps (so agents don't hallucinate features)

Not in the API: **OCR**, **Word/Excel conversion**, **live camera/mic/screen**. Check [openapi.json](https://api.freedailypro.com/openapi.json).

## Privacy

API requests transmit files for processing; they are handled in memory and **not stored** after the response. That is a different trust model than FreeDailyPro's in-browser local tools.

## CTA for builders

Start on Trial, prove first-call success, then upgrade when agents are in the loop daily: [https://www.freedailypro.com/developers](https://www.freedailypro.com/developers)
