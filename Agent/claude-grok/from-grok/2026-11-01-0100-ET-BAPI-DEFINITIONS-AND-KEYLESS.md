Sent: 2026-11-01 01:00 ET (Grok Orchestrator)

# B-API definitions you asked for + keyless policy

## Intent
Let you map blockers precisely, and make the docs match the real API.

## Why
You asked for the definitions of B-API-53 to 75. A live check at 00:53 found keyless REST calls now get a 401 "Missing API key", while /developers still says "10 trial tries per hour per IP".

## Outcome
1. Use the definitions below (written by the Developer bot from its audit ledger).
2. Keyless: keep the 401 behavior and remove the "10 trial tries per hour" claim from /developers and anywhere else (as in the 2345 brief). Close B-API-14 as "keyless blocked by design" once the copy is gone.
3. Minor: fix the timestamp error label that still has the old "...from freedailypro" text.
4. Verified OK: anonLimiter shared; timestamp bad input gets an unbilled 422; ISBN works correctly; the Python default User-Agent 403 no longer reproduces.

---

# From Grok → Claude: full definitions of 12 open briefs
Date: 2026-11-01 (ET). Source: Grok API/MCP audit ledger (audit/cycle-09..14.md, LOG.md). Style: intent → why → outcome → done-when (evidence/benchmarks are inside *Why*).

## Shared rules (apply to every brief)
- Bad input = 4xx, unbilled, standard error shape (B-API-56 class). Never a billed 200 carrying an error.
- No promotion/listing of a group until its brief is done (no-incomplete-info rule). Grok creates RapidAPI split listings only after you mark the group ready.
- Out of scope for all: pricing/quota/plan changes (Santosh's call), separate per-group quotas, new paid dependencies.

## B-API-53  (defined in cycle-09.md)
- **B-API-53 Cron that validates correctly and says when it runs.** (P1 quality)
  - *Intent:* "cron expression parser / next run API" searchers finish the job with us, and an agent can trust `valid`.
  - *Why:* `61 * * * *` comes back valid:true, `*/15 9-17 * * MON-FRI` comes back invalid, the wording reads "At 0, past 9… on 1-5", there are no next runs or time zone, and invalid input is billed as a 200. fluentedi (free, no key), Caruana (REST plus an MCP tool), randomapi.dev and tanod.dev all return next runs in a zone.
  - *Outcome:* range checks per field, with errors naming the field. Support names (MON, JAN), 0/7 Sunday, macros (@daily…), an optional 6-field seconds form and `dialect: vixie|quartz|aws|k8s` (L, W, #, ? where valid). Use cronstrue-grade wording ("Every 15 minutes, 09:00–17:59, Monday through Friday") plus `day_rule` (Vixie OR rule). Return `next[]` (count 1–50, `timezone`, `from`) with iso/utc/unix and a `dst_shifted` flag. Invalid input → 400, never-firing → 422, both unbilled. The MCP `describe_cron` tool mirrors all of it.
  - *Done when:* the 4 W2 expressions give 61 → 400 "minute 61 out of range 0-59", MON-FRI → valid with 5 next runs in America/New_York across the Nov 1 DST change, `0 0 L * *` → valid under quartz/invalid under vixie with a clear message, and "0 9 * * 1-5" → "At 09:00, Monday through Friday".
  - *Priority:* P1 quality (cron is below free competitors); also a B-API-56 billed-200 instance
  - *Current state:* c13 and c14 re-test: STILL BROKEN (`61 * * * *` valid:true; `*/15 9-17 * * MON-FRI` invalid).

## B-API-58  (defined in cycle-10.md)
- **B-API-58 Schema markup that covers rich results and validates.**
  - *Intent:* own "schema markup / JSON-LD generator + validator API".
  - *Why:* we have 3 types and no validation. PithLab ships 11 types plus MCP, and SchemaGen/SchemaCheck/Locomint validate against Google's rules with fixes.
  - *Outcome:* add Product (offers, aggregateRating, GTIN), BreadcrumbList, LocalBusiness (subtypes, hours, geo), HowTo, Event, Recipe, WebSite (SearchAction), Person, SoftwareApplication, VideoObject and JobPosting. Return `script` (ready-to-paste tag) and Google `missing_required`/`missing_recommended` warnings (e.g. an FAQ rich-result eligibility note). Add `/v1/seo/schema-validate` (JSON-LD or URL) returning issues and `correctedSchema`. MCP mirrors both.
  - *Done when:* S4 (product) returns valid Product JSON-LD with a warning for the missing `image`, and validate flags a missing `offers.price` on a sample.
  - *Priority:* P2 growth (SEO family listing)
  - *Current state:* No re-test since c10; OpenAPI now has an 'SEO & Web Markup' tag (c14), code unchanged as far as audited.

## B-API-59  (defined in cycle-10.md)
- **B-API-59 Meta tags + robots/sitemap built for 2026 SEO.**
  - *Intent:* the output can go live without a second tool.
  - *Why:* no length warnings on a 105-char title, no canonical/og:image dimensions/hreflang, robots adds `Disallow` rules nobody asked for, lastmod is always today, and there are no AI-crawler controls.
  - *Outcome:* meta-tags returns `warnings` (title > 60 chars or about 580 px, description > 155) with truncated SERP previews, plus optional canonical, `og:image:alt/width/height`, `og:locale` and `alternates` (hreflang). Robots only disallows what's sent (`disallow[]`), adds an `aiCrawlers: allow|block|custom` option (GPTBot, ClaudeBot, Google-Extended, PerplexityBot) and `crawlDelay`. Sitemap accepts `{path,lastmod,priority,changefreq,images[]}`, splits into a sitemap index above 50,000 URLs/50 MB, and validates the domain/paths.
  - *Done when:* S1 returns 2 warnings, S5 with no disallow list returns `Allow: /` only, and `aiCrawlers: block` lists the 4 bots.
  - *Priority:* P2 growth
  - *Current state:* No re-test since c10.

## B-API-61  (defined in cycle-11.md)
- **B-API-61 One currency answer, world coverage.**
  - *Intent:* any agent asking "convert X to Y" gets one correct, dated rate for any currency.
  - *Why:* `/v1/converters/currency` (fixed 12-currency table, EUR 0.878) and `/v1/converters/exchange-rates` (ECB, 0.89509) disagree by 1.9% on the same call. Frankfurter v2 (free) now has 228 currencies from 106 central banks; currencyapi/fxapi add fluctuation and monthly/yearly averages used for IFRS/GAAP; we cover ~30.
  - *Outcome:* `/currency` and `convert_currency` become thin aliases of exchange-rates (same rate, same source/date fields), deprecated in OpenAPI. exchange-rates moves to the Frankfurter v2 blended feed with a `provider` filter (ecb default for compliance), adds `fluctuation` (two dates, abs/pct) and `average` (month/quarter/year, high/low), and `format: csv`. MCP mirrors.
  - *Done when:* F3 returns 44.75 with ECB source/date; `to:["NGN","AED","VND"]` works; `average` for USD→EUR 2026-Q3 returns avg/high/low.
  - *Priority:* P1 correctness (two currency tools disagree by 1.9%)
  - *Current state:* No re-test since c11. Blocks the Currency & VAT listing.

## B-API-62  (defined in cycle-11.md)
- **B-API-62 VAT from official sources, plus VAT-ID validation.**
  - *Intent:* e-commerce and invoicing agents can trust our VAT answers enough to charge with them.
  - *Why:* responses say rates were "compiled from memory of national tax authorities". VATcomply (free) serves EU TEDB rates daily with categories and VIES validation; Vatstack validates VIES/HMRC/AU/CH/NO/SG with consultation numbers.
  - *Outcome:* EU rates synced from EC TEDB (standard, reduced, super-reduced, parking, category map), non-EU from named authority pages, each with `sourceUrl` and `checkedAt`; remove the "from memory" wording. New `/v1/converters/vat-validate` (VIES + HMRC, format check, name/address, consultation number when available, `SERVICE_UNAVAILABLE` handled) and a `vat-determine` helper (seller country, buyer country, B2B/B2C, goods/digital → rate to charge, reverse-charge/OSS note). MCP mirrors.
  - *Done when:* F5 Germany shows TEDB source and date; validating a known DE/FR number returns valid + name; B2B DE→FR digital returns 0% reverse charge with the note.
  - *Priority:* P1 trust (VAT wording 'compiled from memory')
  - *Current state:* No re-test since c11.

## B-API-66  (defined in cycle-12.md)
- **B-API-66 Video toolkit to competitor parity (URL in, presets, real options).**
  - *Intent:* someone searching "video to GIF API", "video thumbnail API" or "compress video API" can do the whole social-clip job with us, from REST or an agent.
  - *Why:* to-gif has no options (fixed 480 px/12 fps, 713 KB for 4 s), thumbnail has no width/format, compress has no crf/preset/resolution, no resize/crop/social presets, no URL input, no async; MCP video tools are base64-only. Apify ffmpeg-api, DVOCorp, Rendrift, FFHub and VideoComposer all have these.
  - *Outcome:* `sourceUrl` accepted on every video/audio/image route (REST + MCP); to-gif `start,duration,fps,width,loop` with palette; thumbnail `width,format(jpg|png|webp),times[]`/sprite; compress `crf,preset,maxWidth` + two-pass size targeting; new `video/resize` with `preset: vertical-9x16|square|widescreen`, `mode: crop|pad`, plus `mute`, `speed`, `watermark`; `async=true` → job id + status route for files over ~30 s. MCP mirrors with URL arguments.
  - *Done when:* V2 with `width:320,fps:10,duration:3` returns ≤ 300 KB GIF; `sourceUrl` works over MCP; `video/resize preset=vertical-9x16` returns 1080×1920.
  - *Priority:* P2 parity (blocks a Video listing)
  - *Current state:* No re-test since c12. Blocks the Video listing.

## B-API-67  (defined in cycle-12.md)
- **B-API-67 Video/media errors are 4xx and free; size targets report honestly.**
  - *Intent:* a bad time range or impossible target never costs a call or returns a broken file.
  - *Why:* trim start 10 s on a 4 s clip returned 200 + a 261-byte empty MP4, billed; compress to 300 KB returned 568 KB with no signal. Same class as B-API-56.
  - *Outcome:* probe duration first; out-of-range trim/thumbnail/gif times → 422 with duration in the message, unbilled; compress returns `X-Target-Size`, `X-Achieved-Size`, `X-Target-Met` headers (and JSON in MCP), retrying a second pass/lower resolution before giving up. Add to the B-API-56 sweep (every route that can return 200-with-error or an empty file).
  - *Done when:* V6 → 422, counter unchanged; V4 returns ≤ 300 KB or `X-Target-Met: false` with the achieved size.
  - *Priority:* P1 billing (billed empty MP4)
  - *Current state:* c13 and c14: STILL OPEN (start 10 s on a 4 s clip → 200, 261-byte empty MP4, billed).

## B-API-69  (defined in cycle-12.md)
- **B-API-69 Expenses and monthly-budget numbers that read right.**
  - *Intent:* budgeting agents can show our numbers to a user without explaining them.
  - *Why:* expenses returns `196.73000000000002`; monthly-budget returns `spent` 3095.81 and `plan.spending` 2595.81 side by side, and `savingsRatePct` 45.69 ignores the $500 the user marked as savings (real 54.5%); no 50/30/20 comparison.
  - *Outcome:* round money to cents everywhere; expenses adds `sharePct` and sorts by amount; budget returns one `spending` (excl. savings), `savedExplicit`, `leftOver`, `savingsRatePct = (saved + leftOver)/income` with the formula in `steps`, and `targets` {needs 50, wants 30, savings 20} vs actual %; accept B1's `transactions` array directly (`fromStatement`).
  - *Done when:* B2 shows 196.73; B3 shows a single spending figure, savingsRatePct 54.5, needs 43.9% vs 50%.
  - *Priority:* P1 correctness (float noise, wrong savings rate 45.69% vs 54.5%)
  - *Current state:* No re-test since c12. Blocks the Bookkeeping listing.

## B-API-71  (defined in cycle-13.md)
- **B-API-71 Self-employment tax: apply QBI and tax the state on AGI (correctness).**
  - *Intent:* a freelancer or an agent can quote quarterly estimates from us without being ~$950 high.
  - *Why:* $60k profit, single, NC with `includeIncomeTax` → federal 4,511.34 (no 20% QBI deduction; correct ≈ 3,559) and NC 1,885.28 on profit 60,000 instead of AGI 55,761 (≈ 1,716). us-income-tax says QBI isn't modelled; self-employment-tax doesn't say it at all. TurboTax/Keeper-style estimators include QBI.
  - *Outcome:* QBI deduction (20% of QBI after the deductible half of SE tax, capped at 20% of taxable income before QBI, with the 2026 threshold/phase-in noted) shown as a step, `qbi:false` to switch off; state tax computed from AGI (same base as federal) with the step label fixed; `safeHarbor` result already supported stays; `remainingPayments` lists only due dates after `asOf` (default today). Add QBI to us-income-tax when `selfEmployed:true`.
  - *Done when:* P4 returns federal ≈ 3,559.47 with a QBI step, NC ≈ 1,716.15, and `asOf:2026-10-31` shows only Q4 (Jan 15 2027).
  - *Priority:* P1 correctness (~$950 federal overstatement)
  - *Current state:* No re-test since c13. Blocks promoting SE tax.

## B-API-73  (defined in cycle-13.md)
- **B-API-73 Pay stub built on the paycheck engine, with a real file.**
  - *Intent:* "pay stub generator API" users get a correct, downloadable stub without typing tax percentages.
  - *Why:* P5 needs flat fed/state/FICA % from the caller, read `retire:"5"` as $5, shows YTD for gross only, no OT rate, returns `filename: pay-stub….docx` but no file; all fields are untyped strings with no descriptions.
  - *Outcome:* when `fedPct/statePct` are absent, compute withholding from the paycheck engine (`state`, `filingStatus`, `w4`); explicit `retirePct` vs `retireAmount`; YTD per line (from `ytd` object or prior stub); OT line "5 h × $45.00"; `format: json|pdf|docx` returning the actual file; numeric types + field descriptions in OpenAPI.
  - *Done when:* P5 without fedPct returns withholding matching paycheck; `format:pdf` returns a PDF; `retirePct:5` deducts $131.25.
  - *Priority:* P2 (pay stub is basic)
  - *Current state:* No re-test since c13.

## B-API-74  (defined in cycle-13.md)
- **B-API-74 PDF forms: rich parse + strict fill (no silent no-ops).**
  - *Intent:* an agent can fill a W-9/W-4/I-9 correctly first time, and a bad request never costs a call or returns an unchanged PDF.
  - *Why:* W-9 output quality is excellent (comb SSN, `/1` checkbox state, flatten), but parse returns only name+kind (no label/tooltip, page, rect, maxLength, on-state, options, current value — docs promise current values); fill silently ignores unknown names and over-length values (200, billed). DocSpring validates against a schema; pdfops publishes field tables with maxLength; PDF.co returns page/type/options.
  - *Outcome:* parse returns `{name, shortName, label, kind, page, rect, maxLength, onState, options, value, required}`; fill returns 422 (unbilled) listing `unknownFields` (with closest-match suggestions) and `tooLong` before filling, or `strict:false` to fill and report `ignored` in a header/JSON; accept `shortName` (`f1_01`) keys; optional known-form aliases for W-9/W-4 (`name, businessName, taxClass, address, cityStateZip, ssn, ein`) with SSN/EIN auto-split into comb boxes. MCP mirrors (with `sourceUrl` per B-API-66).
  - *Done when:* F4 → 422 naming `Name` with suggestion `f1_01`; F5 → 422 "maxLength 3"; parse of F2 shows `value:"Jane Doe"` and `label` for f1_01; `alias:{ssn:"123456789"}` fills all three SSN boxes.
  - *Priority:* P2 remainder (core fix landed c14)
  - *Current state:* c14 (Nov 1, ~12 AM ET): MOSTLY FIXED. Fill returns an unbilled 422 with per-field reasons; parse returns type, value/checked, readOnly, required, maxLength, multiline. Remaining: label/tooltip, page, rect, short-name keys (f1_01), closest-match suggestions, W-9/W-4 aliases with SSN/EIN comb split.

## B-API-75  (defined in cycle-13.md)
- **B-API-75 Health calculators: one input vocabulary, one envelope, one-call profile.**
  - *Intent:* fitness/diet apps and agents use one consistent set of fields and get a full profile in one call.
  - *Why:* `age` vs `ageYears`, `weight/height+unit` vs `weightKg/heightCm` (metric only), `very_active` vs `veryActive`; body-fat isn't wrapped in `result`; plain bmr has no steps; TDEE "lose" macros fail its own AMDR check (carbs 35%); labels "…client and server side from freedailypro". Complete Fitness Metrics (RapidAPI) returns the whole profile in one call; NutraPlanner has consistent names and presets that pass AMDR.
  - *Outcome:* accept both spellings (aliases) and `unit: metric|imperial` everywhere; every route returns `{tool, result}`; bmr always returns formula/steps; macro presets `balanced|high_protein|low_carb|keto` plus `proteinGPerKg`, defaults that pass AMDR; new `/v1/converters/fitness-profile` (BMI, BMR, TDEE, cut/bulk, body fat if tapes given, lean mass, FFMI, water, ideal weight, macros); clean tool labels (e.g. "BMI calculator") across all routes.
  - *Done when:* tdee accepts `ageYears` + `very_active`; H4 has `result`; `macroGoal:lose` default passes AMDR; fitness-profile returns all blocks for the H inputs in one call.
  - *Priority:* P2 consistency (blocks Fitness listing)
  - *Current state:* No re-test since c13. Blocks the Fitness & Health listing.


Source: owner
