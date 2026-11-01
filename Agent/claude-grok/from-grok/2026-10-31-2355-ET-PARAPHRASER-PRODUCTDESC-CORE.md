Sent: 2026-10-31 23:55 ET (Grok Orchestrator)

# Paraphraser + Product Description: core (non-AI) upgrade

## Intent
Both tools must equal or beat QuillBot free and marketplace listing tools without any AI, working fully in the browser.

## Why
The Paraphraser returns its input unchanged and is still billed. The product-description tool is a plain template. Both fail Rule 1.

## Outcome
Ship ONLY the non-AI core from the spec below: a rule-and-thesaurus paraphraser with modes, a synonym slider, freeze words and a diff view; a description builder with Amazon/Etsy/Shopify/eBay presets, 3 variants and a claims checker. A no-op result is never billed (see B-API-56/64). Do NOT build the optional AI mode yet; it is waiting on owner decisions about the key, cap, caching and privacy.

---

# Paraphraser + Product Description Generator: Fixing the Core and Adding an Optional AI Mode
FreeDailyPro · 2026-10-31 · Source: Developer audit c11 · Status: SPEC (not launched; do not promote until acceptance tests pass)

## 0. How to work with us (Claude partner framing)
You are a product engineering partner, not an order-taker. Read the real codebase first. Follow how we already deploy tools, metering, and the API/MCP registry. Push back on anything in this spec that is weak, and explain why. Keep every "free-first, files stay on your device" promise true.

## 1. Intent
Two tools are broken or below a usable standard right now:
- **Paraphraser** returns the input unchanged.
- **Product Description Generator** fills in a plain template.

We want:
(a) a **core, non-AI paraphraser that actually rewrites text**, running 100% in the browser;
(b) an **optional, clearly labeled "Optional AI" mode** for both tools that is better than QuillBot (paraphrasing) and Shopify Magic/Amazon listing AI (product copy) in the ways users can see. That means more control, more honesty, multiple marketplaces, and privacy.

## 2. Why / evidence
- Audit c11: Paraphraser output equals its input. That is a broken promise on a ranked tool page, and it hurts both trust and AdSense quality.
- Product description output is a template. Sellers compare it with Shopify Magic and Amazon's tools, which are free inside their own platforms.
- Our brand: privacy-first, client-side, usable under any company AI policy. AI must never be required.

### Competitor benchmark (researched 2026-10-31; facts marked * should be re-checked before quoting on marketing pages)
| Tool | Free tier | Paid | Notable features |
|---|---|---|---|
| QuillBot Paraphraser | 125 words per run; 2 modes (Standard, Fluency); partial synonym slider | $8.33/mo annual, $19.95/mo monthly (help center, quillbot.com/premium) | 9 modes plus unlimited custom modes, mode compare, history (50/mo), 23 languages, freeze words, synonym slider |
| Wordtune* | about 10 rewrites/day | about $13.99/mo annual | Rewrite, Casual/Formal, Shorten/Expand, sentence-level alternatives |
| Grammarly* | a few AI prompts/month | Pro about $12/mo annual | Rewrite for clarity, tone adjust, full-paragraph rewrite inside the editor |
| Copy.ai / Jasper* | Copy.ai has a limited free tier; Jasper has none | about $49+/mo (Jasper Creator about $39–49) | Product description templates, brand voice, bulk generation |
| Shopify Magic | Included in Shopify plans | n/a | Descriptions from keywords plus tone; Shopify only, no bulk, weak on short inputs (App Store page, SellerStacked) |
| Amazon Seller Central listing AI | Free for sellers | n/a | Title, description, and attributes from text, an image, a URL, or a spreadsheet; seller must review; Amazon only |
| Etsy Search Visibility / eRank* | Etsy title suggestions free | eRank about $5.99+/mo | 140-character titles, 13 tags, Etsy keyword data |

**Gaps we can close:**
1. Nobody offers a **private, non-AI paraphraser** that works when AI is banned at work.
2. Nobody shows a **meaning-preserved check** with a diff on every rewrite.
3. Platform AI tools are **locked to one marketplace**. We cover Amazon, Etsy, Shopify, and eBay from one input, with limit and compliance checks.
4. QuillBot charges $19.95/mo month-to-month. Our Premium at $9.99/mo is cheaper and includes every other tool.

## 3. Outcomes (definition of done)
- The core paraphraser changes at least 25% of tokens on typical prose at the default setting and stays readable. It makes zero network calls, and it works with AI turned off.
- The core product description tool produces structured output: platform presets, bullets, character limits, and keyword placement, with no AI.
- Optional AI mode beats QuillBot's free tier (more words, more modes, compare view, meaning check) and beats Shopify Magic (multiple platforms, variants, compliance checks).
- AI cost per Premium user stays at or below $4/mo, and global AI spend stays at or below the monthly cap (suggested $100, pending Santosh).
- No marketing, SEO copy, or social posts mention AI mode until §9 passes.

## 4. Suggested direction (interpret freely)

### 4a. Core paraphraser fix (client-side, NEVER AI-dependent)
- Ship a compact thesaurus with the page as a lazy-loaded JSON file (target 300 KB gzipped or less). Build it from WordNet or Moby; check the licenses. Include part-of-speech tags and a frequency rank.
- Pipeline:
  1. Tokenize and split sentences.
  2. Tag parts of speech with a light tagger (e.g. a compromise.js-style tagger) or heuristics.
  3. Swap synonyms with POS-matched, frequency-ranked candidates, and fix inflection (plural, tense, a/an).
  4. Apply phrase rewrites: about 500 curated pairs such as "in order to"→"to" and "a large number of"→"many".
  5. Apply light structural transforms: clause reordering where safe, and contraction expand/collapse.
  6. Never touch protected tokens: numbers, URLs, emails, code, quoted text, proper nouns, and freeze words.
- Modes without AI: Standard, Simple (prefer high-frequency words), Formal (expand contractions, pick formal synonyms), Shorten (phrase compression), plus a synonym slider (0–100%) and freeze words.
- UI: a diff highlight, click any changed word for alternatives, and a "Regenerate" button that uses a seeded random choice.
- Be honest in the UI: "Rule-based rewrite, runs on your device. For deeper rewrites try Optional AI (off by default)."

### 4b. Core product description fix (client-side)
- Inputs: product name, category, materials/specs, audience, benefits, keywords, and platform preset.
- Platform presets with live counters:
  - Amazon: title 200 chars (check the category rule), 5 bullets of about 250 chars, description 2,000 chars, backend keywords 249 bytes.
  - Etsy: title 140 chars, 13 tags of 20 chars each.
  - Shopify: SEO title about 70 chars, meta description about 160 chars.
  - eBay: title 80 chars.
  - Keep the limits in one config file with a "last verified" date.
- Templates that change by category and tone, plus feature-to-benefit phrase banks, so output is not a single fixed template. Provide 3 variants.
- Client-side compliance lint: banned or unsafe claims ("FDA approved", "cure", "best seller", "#1"), ALL CAPS, emoji limits on Amazon, prices or promos in titles, competitor brand names, and keyword stuffing (density over 3%).

### 4c. Optional AI mode (both tools)
- Label: an **"Optional AI"** badge and a toggle that is OFF by default. Show a one-line disclosure before the first use: "Your text is sent to our AI provider (xAI) only when you click. Not stored. Not used for training." Confirm the training/retention terms in xAI's API terms.
- Hide the toggle entirely if the user's "Prefer no AI" setting is on or the org AI-off switch is set.
- Paraphraser AI modes: Standard, Fluent, Formal, Simple, Creative, Shorten, Expand, Academic, plus a Custom tone line (Premium).
  - Synonym slider maps to rewrite strength.
  - Freeze words go into the prompt and are verified after generation.
  - Compare view shows 2–3 modes side by side (Premium).
  - **Meaning-preserved check:** a second, cheap model call or local heuristics (entity, number, and negation preservation plus a semantic-similarity score) give a flag: ✓ meaning kept / ⚠ check these spans.
  - Local checks always run on-device for free: numbers, names, and negations kept, and freeze words intact.
- Product description AI:
  - Inputs from 4b, with output formatted to each platform preset.
  - Tones: professional, playful, luxury, minimal, technical.
  - Bullets plus an SEO keyword plan (primary and secondary placement).
  - 3 variants, or up to 10 on Premium.
  - "Rewrite for all 4 platforms" in one click (Premium).
  - The compliance lint from 4b runs on the AI output too, and a fact guard flags any number or claim that is not in the user's input.
- Never auto-run AI. Every call needs an explicit click.

### 4d. Server design
- Endpoint `POST /api/ai/rewrite` and `POST /api/ai/product-copy`, server-side only. The xAI key lives in a server env var, never in the client.
- Model: grok-4.3 ($1.25/1M input, $2.50/1M output). Use JSON-structured output.
- Do not log request or response bodies. Log only metadata: user tier, token counts, cost, latency, and a hash for the cache.
- Cache: key = sha256(normalized text + mode + params), TTL 24h, stored as hashed results in an in-memory/KV store. Disclose this. If Santosh prefers "no storage at all", turn the cache off.

## 5. Cost guardrails
**Per-call cost estimates (1 word ≈ 1.35 tokens; system prompt about 400 tokens):**
| Call | Input tokens | Output tokens | Cost |
|---|---|---|---|
| Paraphrase 500 words | about 1,100 | about 750 | about $0.0033 |
| Paraphrase 2,000 words (free cap) | about 3,100 | about 2,900 | about $0.011 |
| Paraphrase 5,000 words (Premium cap) | about 7,200 | about 7,000 | about $0.027 |
| Compare 3 modes, 500 words | — | — | about $0.010 |
| Product copy, 1 platform, 3 variants | about 600 | about 900 | about $0.003 |
| All 4 platforms | — | — | about $0.010 |
| Meaning check (AI), 500 words | about 1,500 | about 150 | about $0.0022 |

**Limits:**
| Limit | Free (signed-out/in) | Professional $4.99 | Premium $9.99 | Workflow $29.99 |
|---|---|---|---|---|
| AI runs/day | 3 | 10 | 100 (fair use) | 300 + batch |
| Input cap | 2,000 words; 500 words signed-out | 2,000 | 5,000 | 5,000/item, batch 50 |
| Output max_tokens | 1.5× input, hard cap 3,000 | 3,000 | 8,000 | 8,000 |
| Monthly AI cost soft cap | — | about $1.50 | about $4 | about $12 |

- When a user hits the soft cap, slow them down (queue, cheaper settings) and show a note. Never cut a paid user off with no message.
- Rate limits: 10 requests/min per user and 3 requests/min per IP when signed out. Add Turnstile/captcha for signed-out users.
- **Global monthly spend cap: $100 (suggested, pending Santosh).**
  - At 80%: alert the owner and stop free AI.
  - At 100%: kill switch. AI is off for everyone and the core tools keep working.
- Kill switch: an env flag `AI_ENABLED=false` plus an admin toggle; the UI hides AI within 60 seconds.
- Budget math: $100 ≈ 30k paraphrase runs of 500 words.

## 6. Pricing and upgrade path
These must match what the site already shows.
- The core tools stay free under the existing trial and metering rules.
- Optional AI: 3 runs/day free; Professional $4.99/mo raises the caps; **Premium $9.99/mo** unlocks all modes, compare view, 5,000 words, and 10 variants. Position it against QuillBot's $19.95 monthly.
- Workflow $29.99/mo adds batch CSV product copy (upload a CSV and download a CSV for multiple platforms), an audit log, and an org AI-off admin.
- Developers: REST and MCP calls bill as **10 API calls per AI run**, within the existing $24/$69/$129 plans.

## 7. API / MCP exposure
- REST:
  - `POST /v1/paraphrase` with `{text, mode, strength, freeze[], engine:"local"|"ai"}`. The default is `local`, which runs the rule engine on the server for the API.
  - `POST /v1/product-description` with `{product, platform[], tone, keywords[], variants, engine}`.
  - Both return `{output, changes[], checks:{meaning, compliance[], limits[]}, engine, cost_units}`.
- MCP tools: `paraphrase_text` and `generate_product_description`, with `engine` defaulting to `local`. AI runs only when `engine:"ai"` is passed AND the plan allows it.
- Document these in the API docs only after launch.

## 8. Constraints / out of scope
- No core tool may call AI or the network to function.
- Respect "Prefer no AI" and the org switch on every surface: web, API, and MCP. The API returns 403 `ai_disabled_by_org`.
- No storage of text. No training.
- Name xAI as a processor on /privacy (pending Santosh/legal).
- Do not market this as a plagiarism-evasion or AI-detector-bypass tool, and do not add a "humanizer". It is a brand and AdSense risk.
- Never promote incomplete features. Nothing goes in SEO copy, social posts, or YouTube until acceptance passes.

## 9. Acceptance tests
1. Core paraphraser, 20-sample corpus: at least 25% tokens changed at default strength, output differs from input on 100% of samples, and numbers, URLs, and freeze words are intact on 100% of samples.
2. Core tools in DevTools offline mode / with network blocked: paraphrase and product description both work.
3. With "Prefer no AI" or the org switch on: the AI toggle is absent and the API returns 403.
4. With AI on: no request is sent until the click, which you verify in the network panel. The disclosure shows on first use.
5. Caps: a 2,001-word free input is blocked with an upgrade note; a free user's 4th run in a day is blocked; Premium allows 5,000 words.
6. The output token cap is enforced. The cost logged for each call is within ±20% of the estimate.
7. Global cap: simulate 80% spend (free AI off, alert sent) and 100% spend (all AI off, core tools working).
8. Kill switch hides AI within 60 seconds.
9. The meaning check flags a deliberately dropped negation or number in 5 out of 5 seeded cases.
10. Product copy: each platform preset respects its character limits in 100% of variants; the compliance lint catches "FDA approved", "#1", and ALL CAPS; the fact guard flags invented numbers.
11. Server logs contain no request or response text (grep the logs during the test run).
12. API and MCP parity: the same input with engine `local` returns the same result through REST and MCP, and AI runs deduct 10 units.
13. Blind quality check: 10 samples compared against QuillBot free (Standard and Fluency). Ours is rated equal or better on 7 of 10, or we do not launch.

## 10. Process
Inspect the codebase and the current tool code → restate the problem and your plan → propose changes (flag disagreements) → implement core fixes FIRST (ship them independently) → then AI mode behind a feature flag → run §9 → report results, costs, and any open questions.

## 11. Blocked on Santosh
- Production use of the xAI key and the monthly cap ($100 suggested).
- The 24h hashed cache, or no cache at all.
- /privacy wording naming xAI, and a DreamUSA LLC legal check.
- Approval of the AI cap numbers per plan.

---
## Paste-ready Claude brief
> You're our engineering partner on FreeDailyPro.com, a privacy-first, client-side tool site. Audit c11 found our Paraphraser returns input unchanged and our Product Description Generator is a plain template. First, fix both cores so they work fully in the browser with no AI and no network: a POS-aware thesaurus/phrase-rule paraphraser with modes, a synonym slider, freeze words, and a diff; and a platform-aware (Amazon/Etsy/Shopify/eBay) description builder with limits, variants, and a compliance lint. Ship those on their own. Then, behind a flag, add a clearly labeled, off-by-default "Optional AI" mode using xAI grok-4.3 server-side, only on explicit click, with no text stored. It must respect "Prefer no AI" and the org AI-off switch, the word, token, and daily caps, the per-plan soft caps, a $100 global cap with a kill switch, and API/MCP parity (engine defaults to local). Our bar is to beat QuillBot and Shopify Magic on control, honesty (a meaning-preserved check), and multi-platform output. Read the codebase, challenge anything weak in the attached spec, follow our existing metering and deploy patterns, and prove it with the acceptance tests in §9 before anything is promoted.


Source: owner
