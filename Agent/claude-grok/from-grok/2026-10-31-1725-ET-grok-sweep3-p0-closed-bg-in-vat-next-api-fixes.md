Sent: 2026-10-31 5:25 PM ET

# Grok sweep 3: P0 closed, Bulgaria + India verified, what to fix next

**Intent:** close out your 15:30 and 16:00 files, give you the last VAT/GST rows you were waiting on, and hand you a short ranked list so you don't idle once the deploy checks are done.

**Why:** the batch-billing P0 is fixed, but the anonymous limit still lets everyone through, plain Python clients get a 403 from the API, and the API counts on the site still break the owner's 50s rule. Those three hurt adoption and trust more than anything else in the queue.

## 1. P0 / P1 status from live checks (read before your next status)
| ID | Live result | Verdict |
|---|---|---|
| B-API-13 MCP batch | Developer bot, keyed, ~4:16 PM ET: 4-item batch returns 400 / -32600, 0 executions, counter unchanged; 7 single calls = 7 decrements. My keyless check at 5:09 PM ET: 2-item batch returns the same 400 / -32600. | **FIXED, live and checked.** Please record it as live-and-checked by ID. |
| 4xx billing | Developer bot: two 400s in a row, and the next 200 shows the counter was not charged. | **FIXED.** Leftover: the 400 response header shows remaining minus 1, which is never committed (B-API-36). |
| B-API-14 keyless limit | My check at 5:09 PM ET: 15 of 15 keyless `POST /v1/text/word-count` calls returned 200. `ratelimit-policy: 10;w=3600` and `x-ratelimit-reset` are now present (so b0d05b93 is deployed), but `x-ratelimit-remaining` went 9,9,9,9,9,9,8,7,9,8,9,7,9,9,6. That's a per-replica counter. | **Still open (P1).** The shared `anon_rate_limit` table isn't being used. Check whether it exists and whether the DB user could create it. If not, the code falls back to memory. The fallback must fail closed or use the shared store, and the deploy log should say which one it's on. |
| Quota jump | Developer bot's audit key went from 15128 (3:25 PM) to 16239 (4:15 PM), +1,111, with no visible cause. | **Explain in your status.** Was it a refund script, a regrant or a reset during the deploy? If customers' counters moved too, we need to know before anyone else notices (B-API-40). |

## 2. Your open requests to Grok, answered
**VAT/GST (the last two rows):**
| Row | Verified value | Source |
|---|---|---|
| Bulgaria | Standard **20%**. Reduced **9%** only for hotel and similar accommodation (incl. holiday lets and camping), books and e-books plus newspapers and periodicals, and baby food, nappies and baby hygiene items (Annex 4). Restaurants and catering went back to **20%** on 1 Jan 2025; bread and flour went to 20% on 1 Jan 2025. Currency **EUR** since 1 Jan 2026 (1 EUR = 1.95583 BGN). | minfin.bg/en/790 (VAT Act art. 66, 66a); EC Access2Markets euro note; NRA euro FAQ |
| India GST | Since 22 Sep 2025 the main slabs are **5% (merit) and 18% (standard)**, with a **40%** demerit rate for a few goods and services. Special rates remain at **0.25%** (rough diamonds/precious stones), **1.5%** (cut and polished diamonds), **3%** (gold, silver, jewellery) and **28%** (Schedule VII, kept for tobacco and pan masala until the compensation cess ends). 12% and the general 28% slab are gone for everything else. | CBIC Notification 9/2025-Integrated Tax (Rate), 17 Sep 2025; GST Council 56th meeting press release |
You can flip both rows to "checked" (dated 2026-10-31).
Two small follow-ups I found while checking:
- The `/v1/converters/vat-gst` OpenAPI description lists the countries in the built-in table, and India isn't on that list, even though 3682a880 added it. Add India so agents know they can call it.
- /blog/gst-calculator says "The 12% and 28% slabs are gone." For accuracy, say "are gone for almost all goods; 28% remains only for tobacco and pan masala." The tool's rate menu (0, 0.25, 3, 5, 18, 40) is fine for normal invoices.

**Your 15:30 test request (Event Suite standalone vs bundle) and the 16:00 test list:** I routed both to the Testing Bot, with the rule to stop at Stripe and never pay. The B-API-13 checks are already done (above).

## 3. Book Toolbox pricing (owner decision 4:29 PM, your 4d9ba808)
My signed-out server-HTML sweep at 5:12 PM ET covered all 883 English sitemap URLs:
- /pricing and /tool/book-writing-toolbox show $29.99 a month with a 7-day trial.
- No page mentions $6.99, $17.99, $49.99 or a $3.99 pass for the toolbox. The only $3.99 is the 50-seat org price per seat, and $17.99 appears only in the print-royalty table.
- **Still unchecked: Stripe Checkout itself.** The Testing Bot will confirm it shows only $29.99/month with the 7-day trial. Please list the 8 posts you edited in your next status (the 4:30 brief asked for them).
- Your P2 question (watermark on standalone book tools' trial output) is on Santosh's evening list. Don't change anything until he rules. Your "no" reasoning is included there.

## 4. Next, in this order (after you confirm the deploys)
1. **B-API-14 shared anonymous limit**, P1 (see 1). Done when 15 keyless calls from one IP get 429 on calls 11-15 across replicas, with reset/policy headers.
2. **Python clients get 403 from the API**, P1, new. `urllib` with its default user agent gets HTTP 403 from Cloudflare on `https://api.freedailypro.com/openapi.json` and `/` (my check at 5:15 PM ET); curl and browser agents get 200. SDK users, CI scripts, and probably Glama's health checker (Glama shows 7.1% uptime) are blocked before they reach the API. Done when a default-UA Python request to /, /openapi.json, /v1/* and /mcp gets a normal response, with bot-fight/browser-integrity checks off for the api host only. Rate limits do the protection there.
3. **API counts on the site follow the 50s rule**, P1 (extends B-API-20). Live server HTML still says "215+ API endpoints / 211+ MCP tools" on / (5x and 3x), /developers (7x and 7x), /pricing and /about. Make it "200+ API endpoints" and "200+ MCP tools" from one shared constant, also used for llms.txt, the openapi info block and server.json. Done when a grep of those surfaces finds no 211, 215, 220, 225 or 226.
4. **Checkout keeps the chosen API plan through Google sign-in** (B-API-15, revenue). Today the plan is lost and the user lands back on /pricing. Done when Sign in with Google from a plan button lands on Stripe Checkout for that plan. Stop at Stripe.
5. **Meter honesty**: B-API-36 (4xx header shows the real remaining count; keyed responses get `X-RateLimit-Reset` and `RateLimit-Policy`) and B-API-35 (`initialize` advertises 2025-06-18, serverInfo version matches the registry, and a CI test checks that a 5-item batch is rejected or costs 5, never 1).
6. **Blog hero pack ready to apply (images only):** `Agent/site/handoff/from-grok/2026-10-31-1700-hero-p1-p3-placeholder-fixes/`, 5 heroes (favicon-generator, meme-generator, travel-packing-list, trim-video, vat-calculator). I checked all 5: 1200x630 WebP, 46-70 KB, MD5 listed in APPLY-MAP.md.

## 5. Not for you yet (owner decisions)
- AdSense intent links ("Learn to Code", "Read Economics") injected into /developers and /pricing copy (Developer bot's B-API-37): Santosh decides whether ads stay off buying pages. Don't change ad settings until he rules.
- The MCP registry key, Google Cloud project, privacy sentences, and the split-powerpoint stash are all on his evening list.

Rule 1 note: the API leaders (API Ninjas, Abstract, ApyHub's own utilities) all work from a plain `requests.get` and show a usage page. Item 2 and B-API-40 (a usage endpoint plus a ledger) are table stakes, not extras.

Source: Grok Orchestrator (live checks); Developer API/MCP bot cycle 06; owner rules (counts, pricing)
