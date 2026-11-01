# FreeDailyPro on RapidAPI: playbook (research dated 2026-10-31)

Method: read-only. RapidAPI hub search run live in the owner's signed-in Chrome for 25 queries (first screen of results, about 20 per query, relevance order); our six listings and the Studio page opened read-only; four competitor pricing pages read; RapidAPI docs and web search used. Nothing was changed in any account.
"Observed" = seen on the live hub today. "Documented" = RapidAPI docs. "Unverified" = inference, test before relying on it.

---------------------------------------------------------------------
## 0. Findings that change the plan

1. Our six listings have no popularity, latency or service-level figures yet, and unscored listings sort BELOW scored ones even when far more relevant.
   - "pay stub": 4 results total, ours is 4th. Ahead of us: SeatGeek (ticket search, scored 9.2), a Dollar General employee portal, and a document-OCR API. We are the only real pay stub API and still rank last.
   - "paycheck": 7 results, ours 4th, behind Salary After Tax API (9.4) and Kultranz.
   - "kdp": 3 results, ours last, behind an unrelated landscaping listing.
   - Conclusion (observed, strong): once relevance matches, popularity and score decide order. Getting real calls and users matters more than wording.
2. Several of our key phrases are invisible. Search for "401k" returns 1 API (ApiStack); ours is not in it, because our copy says "401(k)". Search for "retirement calculator" returns 6; ours is not among them. For "bmi calculator" (25 results) ours was not on the first screen. Put the exact search words (401k, retirement calculator, bmi calculator, pay stub, paycheck) in the NAME and SHORT description, not only in the long text. (Unverified whether the long description is indexed; docs say it is, results suggest short description and name carry the weight.)
3. Search appears to require every word to match (a 4-word query "401k retirement calculator" returned 0 results). Keep names to the phrases people type: "X Calculator API", "X to Y API".
4. The Studio page shows seven API projects: the six live listings plus "FreeDailyPro Public APIs" (215+ endpoints, one key, one quota). Check that project is not public; a public duplicate of the same endpoints would be a duplicate-listing risk.
5. All six listings show "Subscribers: 1" and the pricing page says "Subscribed to BASIC" for the signed-in owner account. That one subscriber is very likely the owner's own test subscription. Confirm in Studio, Community tab. Real external subscribers may be zero.
6. A "Basic (Deprecated)" plan (500,000 requests a month on the calculator listing) is still shown on all six listings next to the real Basic plan (5,000 a month). It looks messy and confuses buyers. Owner decision, but retiring it from view is a wording and structure change, not a quota change.
7. Competitor free plans are tiny: Salary After Tax API 50 requests a month, Bank Statement PDF to CSV 20, PDF4me 20, PDFSlim 30. Ours is 5,000 a month. Our Pro plan at 9 dollars buys 25,000 calls; theirs buys 1,000. This is the owner's call; the wording opportunity is to say plainly that Basic is enough to build and test a real app.

---------------------------------------------------------------------
## 1. How RapidAPI ranks and surfaces APIs

Documented (RapidAPI docs):
- Popularity is a score from 1 to 10 "based on the number of requests and the number of users". (docs.rapidapi.com/docs/faqs)
- Average latency is the response time over the last 30 days. Service level is the share of successful calls (2xx against 5xx) over the last 30 days. (same FAQ)
- Short and long descriptions are indexed and shown in search results; the short description is the hub tile text and is truncated if long. Tutorials sit on their own tab; spotlights (external links or PDFs) sit on the About tab. (docs.rapidapi.com/docs/documenting-your-api, hub-listing-general-tab)
- An API has exactly one category, set by Rapid. Logo is JPEG or PNG up to 500 by 500. Tags are shown on tiles and can filter searches. New APIs are private until the Terms box is ticked.
- Terms of Use bar APIs that infringe others' intellectual property, including brand identifiers (conductatlas.com summary of rapidapi.com/terms).

Observed on the hub:
- Result cards show category, name, short description, provider, "Updated N ago", then popularity, latency and service level when they exist. Plan prices are not on the card, so the short description and name must sell the job.
- Rating (stars) is not shown on search cards; our own listing pages show "(0)" ratings.
- Pool sizes: Business 20,515 APIs, Data 9,358, Tools 7,346, Finance 2,180, Video and Images 942, Health and Fitness 295, Cryptography 245, Text Analysis 1,082. Small pools help visibility.
- Scoring is lumpy: many scored listings are old (3 to 8 years) and still lead (EU VAT results). Many new listings from other providers have no score yet and sit in the middle (South Star Tools, TidyData, ApiStack). Updated-recently is common among the newer ones, but I could not prove a recency boost.
- Spam and duplicates are present (seven "Audio File to Text Converter" listings by different provider names; scam-recovery posts in the "paycheck" results). The hub tolerates them today; do not copy them.

Unverified: exact weights; whether free-plan presence, docs, tutorials, ratings or the Try-it test feed ranking; whether a "Hub Health" or similar score exists. The provider dashboard analytics (Studio project analytics, views, search impressions) could not be read: the Studio landing page loaded, per-project analytics need clicks into each project. Ask the owner for a screenshot of Studio, Analytics for one listing if numbers are wanted.

---------------------------------------------------------------------
## 2. Per-keyword landscape (first screen of relevance order, 2026-10-31)

Format: query (total results) | top five | notes | our gap.

1. paycheck calculator ("paycheck": 7)
   Salary After Tax API (NeonAPI; 9.4, 866 ms, 100%; Basic 50 a month, Pro 15 dollars for 1,000, Ultra 49 for 10,000, Mega 149 for 50,000), Kultranz (tax, salary and cost-of-living; unscored), ours, an unrelated PPP loan dataset, three scam posts.
   Gap: only two real competitors. Ours covers paycheck, state tax, FICA, self-employment tax, 401k, pay stub; shows the working. Very winnable. Small search pool.

2. VAT API ("vat": 249)
   EU VAT Number Check (RapiHub 9.6, 1415 ms), VAT validation and tax rates (StandingAPI 9.5), Validate VAT Number (FutureAPI), vatlayer (apilayer 8.4), Validate VAT (API Tier). Almost all are EU VAT NUMBER VALIDATION (VIES), many last updated 3 to 8 years ago.
   Gap: we do VAT/GST amount calculation and a country rate table, not number validation. Do not claim validation. Demand is mostly for validation, so mismatch.

3. currency exchange API ("currency exchange": 271)
   Currency Conversion and Exchange Rates (Principal APIs 9.9, 182 ms), Exchange Rates (TJDH), Currency Converter (Geo API 9.9), Currency Exchange (fyhao 9.9, 39% service level), Crypto Market Prices. Dozens of data-feed APIs.
   Gap: none we can prove; it is a data-feed market and rates freshness decides. Skip as a standalone listing.

4. bank statement to CSV ("bank statement": 43)
   IDfy Indian Bank Statement (9.2), Mutasi Bank API, Extracta Bank Statement Parsing, Nordigen, Expenses day. Newer: Bank Statement PDF to Excel and CSV (Brandon Obas, 8.3, 4608 ms, updated 4 days ago; Basic 20 a month, Pro 19.99 dollars for 1,000 plus 0.03 overage), Bank Statement Reconciler (MT940, camt.053; 8.5, 61 ms), Bank Statement and Invoice Parser ("files are never stored"), VisionDock (9.5).
   Gap: ours takes statement TEXT and returns CSV rows. Competitors take the PDF or a scan. Unless our endpoint accepts a PDF upload, we are weaker. Verify before listing.

5. PDF form fill ("pdf form": 187)
   Results are general PDF suites: PDF4me (9.6, 2731 ms, 98%; plans 0/35/85 dollars, per-call overage 0.02 to 0.05), PDF.co (7 years old), Api2Pdf, XLSX Template. No dedicated "fill PDF form by field name" API in the first screen.
   Gap: ours has parse fields, fill by name, optional flatten. Clear niche.

6. PDF compress/merge ("pdf compress": 44)
   PDF4me 9.6, PDF utilities (4 years old), Tesseract Compressor, PDF Compressor (Arnav Dixit), PDF Compression API. Fresh, scored: PDFRam (8.5, 25,183 ms, 87%), PDFSlim (8.5, 3161 ms, 100%; Basic 30, Pro 9 dollars for 1,000, Ultra 29 for 5,000), Papyrio (9.3, 1930 ms, "files deleted immediately"), OCR and PDF Tools (8.5). At least 15 compressors.
   Gap: crowded. Our edge is breadth (merge, split, rotate, watermark, redact, page numbers, forms in one key) and honest errors. Keep as the umbrella PDF listing, not a new compressor listing.

7. BMI / fitness calculator ("bmi calculator": 25)
   BMI Calculator (Navi 9.3, 506 ms), Principal APIs BMI (9.6, 267 ms), Health Calculator API (Dakidarts, 50+ endpoints, 9.0), gym-fit (9.5), APIVerve BMI (8.4), Nutrition Calculator (8.6). Many 2 to 4 year old single-endpoint ones.
   Gap: ours has BMI, BMR, TDEE, body fat (US Navy), ideal weight, water intake, pregnancy due date. Dakidarts is the direct competitor. Small pool (Health and Fitness 295).

8. video compress/convert ("video converter": 74)
   Dominated by YouTube downloaders (not our market and risky). Real converters: Audio/Video Converter (RollySoft, unscored), HLS Converter, All in One File Converter, Confile (9.2, 122 ms, 82%), File Convert Lab (10 months old).
   Gap: a real compress, trim, to-GIF, extract-audio, thumbnail, subtitle API with stated size limits (video 100 MB). Weak field. Service level matters: long jobs risk timeouts, so keep the Try-it sample tiny.

9. image convert/resize ("image resize": 60)
   Bulk Image Converter (9.3, 1248 ms), Image Resize (8.7, 1880 ms, 33% service level), Kellsons Moraes Image Toolkit, WebPify, Squoosh API (4 years old). Many stale.
   Gap: ours converts to AVIF, WebP, ICO, TIFF, crops, rotates, flips. Crowded but low quality.

10. audio convert ("audio converter": 41)
   Mostly YouTube-to-MP3 and speech-to-text clones (seven identical "Audio File to Text Converter"). Real: RollySoft Audio/Video Converter, All in One File Converter, Confile.
   Gap: nobody offers audio convert plus normalize, trim, silence removal. Searchers often want YouTube MP3, which we must not serve.

11. timezone converter ("timezone converter": 16)
   Timezone Converter (AyyazTechSol), timestamp-converter, Time Converter, Timezone Converter API (Juan Cruz Cagnoni), ApiStack. Mostly unscored. South Star Tools 3 (8.9, 138 ms, updated 8 hours ago) is the active one.
   Gap: thin. Ours has timezone offset and timestamp conversion. Fold into a date-and-time utility listing.

12. SEO meta tags ("meta tags": 83)
   SEO API (CodeROG suite, 9.8, 3304 ms, 98%), Metadata (9.1), Meta Tag Extractor, Website to Text, Meta-tags-scrapper. Nearly all EXTRACT tags from a URL. Generators: OpenGraph Meta Tag Generator, SEO Meta Tags Generator, Social Media Meta Tag Generator (ApiStack), all unscored.
   Gap: ours GENERATES meta tags, schema.org JSON-LD, robots.txt and sitemap, and checks keyword density. Few competitors on the generator side.

13. hash / JWT / UUID ("jwt decode": 22, "hash generator": 18)
   Many bundles: APIVerve JWT Decoder (8.7, 769 ms), South Star Tools JWT (9.0, 167 ms, verifies signatures), Dev Utility Toolkit (8.6, 91 ms), DevUtils bundles (computetools 55+ endpoints, jc-coaching 37+), HashForge, Kymora. Hash: APIVerve (8.7), many unscored.
   Gap: none for a standalone listing. We decode but do not verify signatures; competitors do. Keep inside the umbrella.

14. markdown / JSON to PowerPoint ("powerpoint": 29, "pptx": 26)
   Almost all PPT-to-PDF converters or extractors. Generators: AI Presentation Generator (SapienVault, 2 years old), DocMiral (HTML templates to PPTX, 7 months), PPTX wizard (edit, 5 years old), Aspose.Slides (6 years old). Nobody does Markdown, JSON or CSV to PPTX.
   Gap: the clearest open space. We have markdown, JSON and CSV to PPTX plus extract text, notes, images, charts; merge, split, compress, find and replace, redact, watermark, fonts, accessibility check (per the MCP tool list; confirm each is exposed on the REST API).

15. mortgage calculator ("mortgage calculator": 22)
   API-Ninjas (8.5, 140 ms), CalcX Loan (Dakidarts), BitFactor Mortgage Calculator, Yawin Calculator (8.2, 2226 ms), wenyang21. Fresh and scored: South Star Tools 2 (9.0, 172 ms, "zero data storage"), APIVerve (8.4), FinCalc (9.3), Vickery (8.3). Ours is already in the list (calculator listing). About half the field is unscored.
   Gap: ours has amortization with payment dates, extra payments, refinance, affordability, student loan, debt payoff. Small field, beatable.

16. retirement / 401k calculator ("retirement calculator": 6; "401k": 1)
   401K Calculator (ApiStack, unscored), Yawin, britwi, Financial Tools, Global Retirement Calculator (DigiVims), Financial Calculators Suite. Ours does not appear today.
   Gap: ours has 401(k) with 2026 IRS limits, RMD, Social Security, FIRE, 529, college cost, contribution limits. Almost no competition. Smallest pool of all.

17. word count / readability ("word count": 101, "readability": 157)
   TextGears (9.8), Smodin, APIVerve Readability (8.5), Analyze Text, Text Readability (Translated); plus dozens of one-liners. APIVerve (EvlarSoft) runs many single-job listings named "X API - APIVerve".
   Gap: none; crowded. Keep as part of the utilities umbrella.

Pattern worth copying: EvlarSoft (APIVerve), South Star Tools, ApiStack, Kellsons Moraes and Dakidarts all run many focused listings from one backend and hold scores of 8.4 to 9.3. The split approach is how the visible winners operate.

---------------------------------------------------------------------
## 3. Listing recipe

Title pattern: "[Job words people type] API" or "[Input] to [Output] API". 3 to 7 words. Put the highest-volume phrase first. No brand names that are not ours.
 - Good: "PowerPoint Generator API: Markdown, JSON and CSV to PPTX", "401k and Retirement Calculator API", "Fill PDF Forms API".
 - Avoid: "Toolkit", "Suite", "All-in-one" as the lead word (everyone uses them, low information).

Short description (hub tile; about 110 to 150 characters; no hyphen padding):
 "[Verb] [object], [object] and [object] as JSON/file from one request. [Differentiator in plain words]."
 Example: "Turn Markdown, JSON or CSV into a finished PPTX file with one POST. Files are processed in memory and not stored."
 Use the exact search words (401k, paycheck, pay stub, bmi calculator) in name or this line.

Long description structure (markdown; docs say it renders markdown):
 1. One sentence: the job and who it is for.
 2. "What you can do": 5 to 8 bullets, each with the endpoint path.
 3. A tiny worked example: request body and the key fields of the response. Plain text, no screenshots needed.
 4. Limits: file sizes, page or minute limits, rate limit, formats.
 5. Errors: plain JSON with a reason; say which errors are not billed (only if true; confirm with the billing logic first).
 6. Privacy: nothing you send is stored.
 7. Notes and disclaimers (estimates, drafts, not tax or legal advice).
 8. One line: part of FreeDailyPro with the developer docs URL. No GitHub link anywhere. MCP availability: one line ("also usable by AI agents over MCP") is a differentiator because few competitors say it.
 The word "free" appears only in tags/SEO, never in prose.

Tags and category (one category only):
 - PowerPoint/PPTX: Tools (13 of 29 "powerpoint" results are Tools); tags powerpoint api, pptx generator, markdown to pptx, json to pptx, csv to pptx, slides, presentation api, free pptx api.
 - Paycheck: Finance; tags paycheck calculator, take home pay, payroll tax, fica, salary after tax, self employment tax, pay stub.
 - Retirement: Finance; tags 401k, 401k calculator, retirement calculator, rmd, social security, fire calculator, 529, free retirement api.
 - Mortgage and loan: Finance; tags mortgage calculator, amortization schedule, loan calculator, refinance, student loan, debt payoff.
 - PDF forms: Tools (PDF listings in Tools lead results); tags pdf form fill, fillable pdf, acroform, flatten pdf, form field parser.
 - Video/image/audio: Video, Images; tags video compress, mp4 to gif, extract audio, video thumbnail, image resize, webp, avif, audio converter.
 - SEO meta: Tools; tags meta tags generator, open graph, twitter card, json-ld, schema.org, robots.txt, sitemap, free seo api.
 - BMI/health: Health and Fitness; tags bmi calculator, bmr, tdee, body fat, ideal weight, water intake.
 - Time/date: Tools; tags timezone converter, unix timestamp, date calculator, countdown.
 - Bank statement: Finance; tags bank statement to csv, statement parser, transactions csv (only if PDF input works).

Plan names and wording (quota unchanged; wording only):
 - Basic: "Basic: 5,000 requests a month at 60 per minute. Enough to build and test a real app."
 - Pro / Ultra / Mega: say the number of requests and rate, and "shared across all FreeDailyPro APIs on your key" if that is true and the owner wants it stated.
 - Remove the deprecated Basic plan from public view once no subscriber is on it (owner decision).
 - Do not call any plan "free" in prose; the price shows 0 dollars.

Try-it (first endpoint in the list) per listing: put the easiest endpoint first and pre-fill the example body so one click returns a result. JSON endpoints beat file-upload endpoints for first impressions (the playground needs a file picker for multipart).
 - PPTX: markdown-to-pptx with a 3-slide sample (returns a file; state it).
 - Paycheck: converters/paycheck with salary, state, filing status.
 - Retirement: converters/401k with age, balance, contribution.
 - Mortgage: converters/loan or amortization with 400,000, 6.5, 30 years.
 - PDF forms: fillable-forms/parse (needs a PDF). Host a small sample PDF on freedailypro.com and link it in the description.
 - Video: video/thumbnail or image/resize first (small input) rather than compress (slow, hurts service level).
 - SEO: meta tags with a page title and description.

Visuals: a distinct 500 by 500 PNG logo per listing (today all six use the same default "F." mark), so tiles are tell-apart-able. Screenshots are not needed; one response example block in the long description does more.

Docs and tutorials: 2 tutorials per listing, 300 to 500 words, each ending on a working request in curl, JavaScript and Python (no GitHub link; paste the code inline). Add one spotlight linking to a dev.to or site article.

First 30 days (popularity needs calls and users, so every item is about getting a real developer to call):
 Week 1: publish listings; subscribe from a second account only if RapidAPI permits and it is honest test traffic (do not fake users); set a distinct logo; write the 2 tutorials; reply to any discussion. Confirm Studio shows each API public.
 Week 1 to 2: post one dev.to article per listing (problem, working request, response), link to the RapidAPI listing and the developer page; no GitHub links. Cross-post the same code on the site developer page and the blog.
 Week 2: build a Postman collection per listing (Postman public workspace link in the description); ask 3 to 5 early users for a rating.
 Week 2 to 4: answer every discussion within 24 hours; add one example request per week; keep latency low (use tiny samples in tests; service level counts failures).
 Week 4: read Studio analytics (views, subscribers, calls); rename or retag the listing with the weakest views; shift effort to the top performer.

---------------------------------------------------------------------
## 4. Ranked order of NEW listings (demand against our strength)

Scores are judgement; demand is estimated from result counts and competitor scores, not from search volume (not available).

1. PowerPoint Generator API (Markdown, JSON, CSV to PPTX plus PPTX tools). Demand medium and rising (AI output to slides), competition near zero, breadth is ours. Confirm REST exposure first.
2. 401k and Retirement Calculator API. Demand small, competition 1 to 6 weak listings, strength high (2026 limits, RMD, Social Security). Fast win and a good first rating.
3. Paycheck and Payroll Tax API (paycheck, pay stub, self-employment, state tax). Demand medium, only two real rivals; Salary After Tax API shows 9.4 so buyers exist.
4. Fill PDF Forms API (parse and fill). Demand medium, no dedicated rival in view.
5. Mortgage, Loan and Amortization Calculator API. Demand high, field of 22 with half unscored; ours is deeper than most.
6. SEO Meta Tags, Open Graph and JSON-LD Generator API. Demand medium, generators are few.
7. Video Compress and Convert API (with image and audio). Demand high, real converters scarce, but timeouts and size risk. Do after tuning the Try-it sample.
8. BMI, TDEE and Health Calculator API. Demand medium, Dakidarts competes; low effort.
9. Bank Statement to CSV API. Demand high (many entrants) but we are weaker unless PDF upload works.
10. Date, Time and Timezone API. Demand low to medium, thin rivals, thin ours.
11. VAT and Sales Tax Calculator API. Demand is for number validation, which we lack.
12. Currency, hash/JWT/UUID, word count, image only, audio only: skip as standalone; they stay inside the umbrellas.

---------------------------------------------------------------------
## 5. Improving the six live listings (ranked by impact against effort)

Rank 1: Finance, Tax, Health and Planning Calculator API (highest impact, low effort)
 - Name: "Tax, Paycheck, Mortgage and Retirement Calculator API" (lead with the searched words).
 - Short: "Paycheck, 401k, retirement, mortgage and loan amortization, US, UK and India income tax, VAT, BMI and TDEE calculators as JSON, with the working shown."
 - Category: Finance (keep).
 - Tags: paycheck calculator, take home pay, 401k, retirement calculator, mortgage calculator, amortization, income tax, vat calculator, bmi calculator, tdee, free calculator api.
 - Long: keep the current structure; add "401k" as a plain token beside "401(k)"; add a worked loan example with the response; add a line listing the 2026 tax-year data covered.
 - Plans: reword Basic as above; retire the deprecated plan from view.
 - Try-it: move Paycheck or Loan to the top of the endpoint list and pre-fill it.
 - Tutorials: "Take-home pay for a US salary", "Build a mortgage amortization table", "Check 401k limits and employer match".

Rank 2: PDF Toolkit API (high impact, trivial effort)
 - Category: change Data to Tools (31 of 44 "pdf compress" results are Tools; only 5 are Data).
 - Name: the name collides with other "PDF Toolkit" listings (the slug already carries an 8). Use "PDF Merge, Split, Compress and Form Fill API".
 - Short: "Merge, split, compress, rotate, watermark, redact and fill PDF forms with one POST. Files are processed in memory and not stored."
 - Tags: pdf merge, pdf split, pdf compress, pdf form fill, pdf redact, pdf watermark, free pdf api.
 - Try-it: parse form fields or rotate (single file); provide a sample PDF download link.
 - Examples: one request per verb in the long description (merge, compress, fill).
 - If a separate PDF Forms listing is made, keep this one as the umbrella and mention forms briefly.

Rank 3: Business Document API (medium impact, low effort)
 - Name: "Pay Stub, Invoice, Receipt and Contract Draft API".
 - Short: keep, but use "pay stub" singular and "invoice" in the first 10 words.
 - Keep category Business (huge pool of 20,515; consider Business Software at 1,218, but effect unverified).
 - Move bank-statement text to CSV down in the list unless PDF input is added; this listing is the home for drafts and pay stubs.
 - Tags: pay stub generator, invoice calculator, receipt, nda template, lease template, profit margin, break even.
 - Try-it: pay-stub with sample hours.

Rank 4: Image, Audio and Video Conversion API (medium impact, low effort)
 - Fix the name mismatch: the Studio card and header say "Image, Audio and Video Conversion API"; the page title says "Video & Image Converter API". Use one name: "Video, Image and Audio Converter API".
 - Category: Media to Video, Images (942 APIs; the top "video converter" result pool is Video, Images 38 and Tools 27).
 - Short: "Compress video, convert MP4 to GIF, extract MP3, convert audio, and resize or convert images (WebP, AVIF, PNG) with one upload."
 - Limits in the first screen of the long text (images 15 MB, audio 30 MB, video 100 MB).
 - Try-it: image/resize or video/thumbnail first with a tiny sample.
 - Verify the Video and Audio endpoint groups are populated (the page text listed only the Image endpoints under their headings; may be collapsed groups).

Rank 5: Text and Developer Utilities API (low to medium impact, low effort)
 - Name: "Developer Utilities API: JWT, Hash, UUID, Regex, Cron and Text Tools".
 - Tags: jwt decoder, hash generator, uuid generator, regex tester, cron expression, base64, word counter, readability score, slug generator, seo meta tags, free developer api.
 - Short: start with "Decode JWTs, hash text, generate UUIDs, test regex, explain cron, count words and build SEO tags as JSON."
 - Be exact: JWT is decoded, not signature-verified.
 - Keep as the umbrella; do not chase single-job text keywords.

Rank 6: Book Publishing API (low impact, low effort)
 - Niche: "kdp" returns 3 results and ours is one; "isbn" is dominated by barcode databases (9.9 scored) that are a different job.
 - Category: Media; consider Tools or Business so writers browsing find it. Unverified.
 - Name: "KDP Spine Width, ISBN and Print Royalty API".
 - Tags: kdp, spine width calculator, isbn validator, print royalty, epub generator, onix.
 - Value is real but small; revisit after the first five.

Apply to all six:
 - Unique logo per listing; 2 tutorials each; a spotlight pointing to a dev.to article; a one-line MCP mention; consistent "nothing is stored" line; no GitHub links; the word "free" only in tags.

---------------------------------------------------------------------
## 6. Judgement: split, improve, or both

Evidence for splitting:
 - Our broad listings are scored 0 and rank below scored listings even for terms we own (pay stub, paycheck, kdp).
 - A focused name and short description match what developers type; "401k" and "retirement calculator" return nothing from us today.
 - Other providers with scores of 8.4 to 9.3 run many focused listings from one backend (APIVerve, South Star Tools, ApiStack, Dakidarts).
 - Several niches are nearly empty: PPTX generation, 401k and retirement, PDF form fill, paycheck.
Evidence against splitting alone:
 - Every new listing starts at zero and competes on a thin new score. Splitting does not create demand; it creates more entry points.
 - A split divides ratings, tutorials and subscriber counts across many pages. One good rating on a focused page outweighs six diluted ones.
 - The visible rank mechanics reward real calls. The scarce resource is attention for the first 30 days, not listing slots.
 - Duplicate-listing and spam risk grows with every near-copy (RapidAPI tolerates it today; policy text says nothing explicit, so unverified).
Evidence for improving the broad ones: cheap, a day's work, removes obvious defects (Data category on PDF, wrong or mismatched names, deprecated plan, invisible 401(k)), and keeps them as umbrellas for buyers who want everything.

Recommendation: do both, in this order.
 1. This week: fix the six (section 5); about one day, no risk. Start with the calculator and PDF listings.
 2. Next: launch focused listings only where we win on gap, not breadth: PowerPoint Generator, 401k and Retirement, Paycheck and Payroll Tax, PDF Form Fill. Then Mortgage and Loan, SEO Meta Tags. Hold Video and Bank Statement until their risks (timeouts, PDF input) are fixed.
 3. Keep umbrellas: Calculator (Finance), PDF Toolkit, Text and Developer Utilities, Business Document, Image/Audio/Video. Each focused listing should say "part of a larger set" with one line, not link to the umbrellas.
 4. Do not split commodity jobs (currency, hash/JWT/UUID, word count, timezone, VAT); there we lose to scored incumbents.
 5. Focus promotion on 3 listings at a time for 30 days; do not spread tutorials and articles over 10 pages.
 6. Review Studio analytics at day 30 and double down on whichever gets views.

Hybrid detail: do not duplicate endpoints in a way that makes two listings identical. Differentiate each focused listing with its own name, short description, examples and a narrower endpoint set. Make sure the same endpoint set is not copy-pasted across more than two listings.

---------------------------------------------------------------------
## 7. Risks and policy

 - Intellectual property and trademarks are barred in listings (RapidAPI Terms; conductatlas summary). Do not use competitor or brand names in titles or tags ("PDF4me alternative", "Adobe", "Microsoft PowerPoint" as a brand lead). Describe formats ("PPTX", "PowerPoint-compatible") rather than brand products where possible. File format names are fine.
 - Do not build YouTube downloader or YouTube-to-MP3 features; that category dominates audio and video searches and is a platform-policy risk.
 - Duplicates: RapidAPI hosts many near-identical listings today, but I could not find an explicit written rule. Treat as unverified and avoid identical copies. Check that "FreeDailyPro Public APIs" is not public.
 - Names: avoid claims we cannot meet (VAT number validation, bank PDF parsing, JWT signature verification, currency feed freshness).
 - Tax, legal and medical outputs: keep the disclaimers (estimates, drafts, not advice).
 - Copy rules: no GitHub link anywhere; "free" only in tags/SEO; plain statements ("files are processed in memory and not stored"). State "errors are not billed" only if billing really works that way.
 - Plans: the deprecated Basic plan and a single self-subscription make the subscriber figure misleading; clean up before shared screenshots.

Sources: docs.rapidapi.com/docs/faqs; docs.rapidapi.com/docs/documenting-your-api; docs.rapidapi.com/docs/hub-listing-general-tab; docs.rapidapi.com/docs/hub-listing-overview; conductatlas.com summary of rapidapi.com/terms; live rapidapi.com search and pricing pages (2026-10-31).
