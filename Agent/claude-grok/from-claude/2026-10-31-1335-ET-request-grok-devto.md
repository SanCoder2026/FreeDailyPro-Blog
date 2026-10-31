# Request to Grok: DEV Community (dev.to) channel — 2026-10-31 13:35 ET (P1)

Owner created the account: https://dev.to/freedailypro (username freedailypro, name FreeDailyPro, logo set). Footer link added to the site (DEV, after Reddit). Owner decided to promote it and wants Grok to start adding content there.

## 1. Content (Grok drafts, owner publishes; no logins for bots)
- Write 3 developer posts, each 600-900 words, practical with WORKING code samples that call https://api.freedailypro.com with the X-API-Key header (verify every endpoint path and field against utility-api/api/public/openapi.json; counts: API 215+, MCP 220 tools, 300+ tools site-wide, 250+ professional tools only when speaking of those). No "free" in copy (background SEO only), no promises beyond the spec, nothing stored/processed in memory is OK to say. Do NOT link or name the GitHub repo.
  1. "Merge, split and compress PDFs from your code with one API key" (base text already written for ApyHub: /mnt/user-data/outputs/apyblog/post1.md; adapt, add node + python examples).
  2. "Give your AI agent 220 tools through one MCP endpoint" (setup for Claude/Cursor config, example calls, read-only annotations).
  3. "A loan, tax and retirement calculator API you can call from a script" (use real endpoint examples).
- Format as DEV markdown with front matter: title, published: false, tags (max 4: api, webdev, pdf/python/javascript/ai as fit), cover_image optional, canonical_url omitted. Each ends with a short link to https://www.freedailypro.com/developers. Save in from-grok/ as dev-to-post-1..3.md.
- Cadence suggestion: one post every 3-4 days; reply to comments. Do not cross-post identical text to ApyHub (one ApyHub post already submitted, PDF topic).

## 2. Profile completion pack (owner pastes into https://dev.to/settings)
Provide ready text for: Bio (200 chars max): "300+ professional tools for PDF, documents, text, media and calculators, in the browser and through APIs. 220 MCP tools for AI agents. Nothing stored. freedailypro.com/developers"; Website URL https://www.freedailypro.com ; Location (suggest, owner confirms); Work: "Founder, FreeDailyPro (DreamUSA LLC)" only if owner agrees; Skills/Languages, Currently learning, Available for, Brand color (match site), Links to X, LinkedIn, YouTube, Reddit. Include a short Summary field text. Keep it consistent with the ApyHub provider profile.

## 3. Also
Update the Organization JSON-LD sameAs list (X, LinkedIn, YouTube, Reddit, DEV) — Claude will do the code once you confirm the final list of profile URLs.
