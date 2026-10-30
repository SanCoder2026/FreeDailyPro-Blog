# FreeDailyPro Testing Bot – Full Retest Guidance Pack
Last updated: 2026-10-30 08:05 AM ET (Growth Orchestrator)
Owner rule: Source: owner. Testing is READ-ONLY – test and review; Claude makes all changes.
Companion: `test-plan.csv` (ranked, 25 rows, batch number = report package).

## RULE 1 — Best in the world & easiest to use: capability-gap review (owner, 2026-10-30 08:05 ET)
Owner: "Not just test what it is now, but suggest based on demand, competition, what make sense, to add more capabilities so such rejection will never happen."
- **Every tool test must include a `Capability gap` section.** Benchmark the top 3–5 competitors (top Google results, marketplace equivalents). Use demand signals: GSC + GA queries, site search terms, Google People Also Ask, marketplace reviewer feedback.
- **List missing features ranked by demand × effort**, then write a **P2 capability brief** with specs (inputs, outputs, UI, API params, examples, acceptance tests).
- **Trigger case:** ApyHub rejected the Finance/Tax/Health/Planning calculators as "too basic". Look for e.g. scientific / graphing / history modes, step-by-step working shown, units, more inputs & outputs, export (PDF/CSV/copy), shareable results.
- **"Mature" now means:** works correctly AND is at least as good as the best competitor. Recheck every tool already marked mature (BMI, Loan, JWT, UUID, Hash, category pages, /developers, Image to PDF, Password Generator, ...) against this.
- **Priority sweep:** all calculator and finance tools first.
- Fill the `capability_gap` column in test-plan.csv for every row.

## 0. Rules (non-negotiable)
1. **Max 3 tools per report.** Follow `report_batch` in test-plan.csv.
2. **All test cases in the same package** so Claude can reproduce: steps, exact inputs/files (attach or path), expected vs actual, device/browser/viewport, logged-in state & plan, screenshots/recordings, timestamps (ET), API request/response (redact keys).
3. **Read-only.** No settings changes in consoles, marketplaces, admin, Stripe, AdSense, GA. Use test cards only if a Stripe test mode exists; otherwise stop at the Stripe page and screenshot.
4. Drop reports in Claude's handoff folder (from-grok, PROCESS.md B-format). Severity P0 (blocks money/task), P1 (wrong output/false claim), P2 (UX), P3 (polish).
5. Every tool tested on **desktop Chrome + mobile (iOS Safari + Android Chrome)**. Mobile = 21% of users but 30.6% engagement (better than desktop) – treat as first-class.

## 1. Data that drives priority (since Jul 10 2026)
**GA4:** 6,130 users / 7,296 sessions, 23.7% engagement. Singapore 1,780 users at 1.3% engagement = bot traffic (Oct 28 spike); exclude mentally. Real core: US 2,845, India 568. Safari 13% engagement, 5s avg – **test Safari hard**. Channels: Direct 4,604 (10.7% eng), YouTube 1,172, Organic Search 817 (57%), Referral 618 (67%). Events: tool_completed 308 by only 24 users; purchase 3 ($6.99); **no site-search event exists** – homepage search terms not in GA.
**GSC:** 575 clicks / 163K impressions, CTR 0.4%, avg pos 18. Biggest wins: roman numeral converter (48,950 impr, pos 9, 0.1% CTR), tip calculator 5,660, tax calculator 4,746 / income-tax page 7,449, unit converter 4,782, grammar checker 8,397, citation generator 2,448, word count 2,320, barcode 2,045, BMI 504. 1,050 indexed / 1,180 not (229 redirects, 76 duplicates, 328 not indexed, 404s; Page Not Found pages get visits). Mobile CTR 0.8% vs desktop 0.3%.
**AdSense:** $0.39 since Oct 24; page RPM $0.37; viewability 18.6%; auto ads on; no policy issues.
**Site admin:** 2,481 visits, 0 limit hits, 0 checkouts, 0 sales, 93% direct, tracking inconsistent with GA, 32 accounts, repeated "url shortener" searches.
**Conversion research:** trial = Premium 2 uses/day, Professional 10/day; an output action (download/copy/export) = 1 use. Zero limit hits means almost nobody reaches a paywall – verify counting actually works.
**Marketplaces/API (AUDIT, TRACTION, SPLIT-LISTINGS, B-0028..B-0040):** RapidAPI sample snippet broken (empty X-RapidAPI-Host, direct host, 401); watermark `color` missing from spec. Live API bugs (B-0040): Split PDF with 2 ranges returns only first file; QR ignores format/size/colour and has no PNG; Video-to-GIF ignores settings; Merge ignores page selection; Image Resize ignores fit; Audio ignores bitrate – all return success. Invoice returns totals only, no PDF. Only 5/20 wave-1 tools finish the full job via API (Compress PDF, JWT, UUID, Markdown→PPTX, Image Convert).
**Not yet ingested (refresh):** B-0039/B-0040 files and Stripe audit REPORT.md (`/cursor/stores/.../stripe-checkout-audit/REPORT.md`) were not found on the box at build time – figures above come from orchestrator summaries. Bing dropped by owner.

## 2. Per-tool verification checklist (apply to every tool)
- **Prior fixes:** confirm each relevant brief (B-INDEX-qa-backlog, B-0001..B-0040) is live; mark Fixed/Partial/Not fixed with evidence.
- **Core task:** realistic input + edge input (large file, empty, unicode, multi-page); output correct, downloadable, opens.
- **UI vs API parity:** same input via UI and `api.freedailypro.com` (X-API-Key) and via RapidAPI host – options honoured, same output, no silent success.
- **Mobile UX:** no horizontal overflow, touch targets ≥44px, upload from camera roll/Files, download works on iOS.
- **Ad interference:** ads never cover input, result, download or the search box; no layout shift >0.1 when ads load; none on checkout/login/payment; note where an ad after the result would fit (B-0038). Record CLS and time-to-result.
- **Trial counting:** fresh visitor → count shows; each output action = 1 use; Premium blocks at 3rd use, Professional at 11th, same day; reset next day; limit-hit screen shows Day Pass + plans and fires limit_hit event.
- **Checkout path:** from limit-hit and /pricing → Stripe in ≤2 clicks; "Buy Day Pass" label; monthly goes straight to Stripe; no cookie/privacy popup over payment; return URL; magic-link email (observe only).
- **Tracking:** tool_completed, limit_hit, begin_checkout, purchase, search (with search_term) fire once (GA DebugView/Tag Assistant read-only).
- **SEO on page:** title/meta match top query, single H1, canonical, no 404 links, localized versions (/es /fr) work.
- **Search box (homepage + /tools):** visible arrow/search button and "Press Enter" hint; suggestions only after ≥3 chars + ~0.5s pause; Enter and arrow both run full search; mobile keyboard "Go/Search" works; empty-result state suggests nearest tools.

## 3. Search terms → tools (gaps flagged)
| Term (source) | Tool | Status |
|---|---|---|
| url shortener (admin search, 128 views) | /tool/url-shortener | exists – check discoverability & /s/ redirects |
| roman numeral converter (GSC 48,950) | roman-numeral-converter | exists – CTR problem |
| tip calculator (5,660) | ? | verify exists; if not = MISSING |
| citation generator (2,448) | ? | verify; likely MISSING |
| tax / state income tax calculator | income-tax-calculator | state version weak (pos 65) |
| unit / percentage calculator | unit-converter / ? | percentage: verify |
| grammar / spell check | grammar-checker | pos 21–74, quality check |
| take photo / camera online | camera-capture | exists |
| compare audio / voice similarity | audio-comparer | exists, best performer |
| barcode generator / scanner | barcode-generator / ? | scanner: verify |
| cost of living comparison, rewrite sentences, similarity checker | text-paraphraser, text-similarity-checker / ? | cost of living likely MISSING |
| passport photo, yt thumbnail, invisible text, obj/mesh viewer | existing tools | spot-check |
| pdf file recovery, html to pdf | ? | verify / gap |
GA site search is not tracked yet – once the search event is live, add the top terms here.

## 4. Competitor / benchmark checks (per tool, 1 line each)
PDF: iLovePDF, Smallpdf, PDF24. Image: TinyPNG, Squoosh. Audio/video: 123apps, Kapwing. Calculators: calculator.net, Omni. Text: Grammarly, LanguageTool, wordcounter.net. QR/barcode: QR Code Monkey. Roman: RapidTables. API: APIVerve, API-Ninjas on RapidAPI. Score: steps to result, time to result, options, output quality, ads intrusiveness, mobile – note the "best in the world" gap and one concrete improvement.

## 5. Site-wide checks (batch 9+)
Indexing/404 crawl of internal links and sitemap; Page Not Found pages; /developers claims; /pricing figures vs "300+ professional tools, premium applications and workflow products"; homepage video swap (B-0026); blog heroes (B-0025); privacy popup (B-0002); login/profile.

## 6. Loop
Test batch → report to from-grok → Claude fixes → routine (10:00 AM / 7:00 PM ET) hands fixes back → retest → next batch. Escalate P0 to orchestrator immediately.

## Changelog
- 2026-10-29 9:38 PM ET – v1 created from GA/GSC/AdSense (Jul 10–Oct 29 + 28d), admin findings, marketplace AUDIT/TRACTION/SPLIT, briefs B-0024..B-0038 on disk, B-0040 summary. TODO refresh: ingest B-0039/B-0040 files, Stripe audit report, GA site-search terms when tracked.

## 7. Retest now (added Oct 30, 1:45 AM ET) — Claude says pushed; verify independently, "claimed fixed, still failing" if not
Priority order: B-0055 exhausted state (R68-CNT-01/02: shared-IP after 10 uses should show 0 consistently on every server; Claude only checked fresh devices) · B-0051 trial charged only on result/download, not file select (16 upload tools) · B-0027 guest monthly checkout straight to Stripe + redirects · B-0041 ads never over/blocking a tool, collapse when unfilled, none on pay/account/API-key pages, slim consent bar — especially mobile · B-0053 homepage search label, no-match state, above fold · B-0054 Merge PDF size label + Choose pages panel (remove/rotate) · B-0056 Compress PDF: Balanced runs, Aggressive/Extreme stop sentence + "Run anyway" · B-0057 income tax NY 2026/CA 2025 labels, negative-income message, 401k catch-up · B-0050 audio comparer offset alignment · B-0026 homepage video (note JSON-LD uploadDate/duration still old) · B-0052 /es tool pages hreflang/JSON-LD.
Already confirmed by Orchestrator curl (no retest needed beyond a spot check): B-0020 use-case pages 200, B-0061 url-shortener 410. Still failing at 1:40 AM: /tool/book-maker 404 (B-0075, not yet sent to Claude — don't re-report).
Section 3 correction: tip-calculator, citation-generator, percentage-calculator all exist — test them as CTR/quality targets, not gaps.

## 8. Added Oct 30, 7:45 AM ET — new Claude pushes to retest
- B-0059 grammar checker (Claude live-checked): UK spellings untouched; then/than, effect/affect, less/fewer only as suggestions; US/UK/auto select.
- B-0060: one tool_completed per spend (unit converter Copy = 1; grammar Check twice = 1); spot-check AI/video/Event Suite tools.
- B-0062 unit converter: power/angle/frequency/cooking tabs, decimal keypad on mobile. Claude asked for cooking g/cup values to be checked against USDA FoodData Central / King Arthur ingredient weight chart — report mismatches.
- B-0061 spot check only (already 410).
