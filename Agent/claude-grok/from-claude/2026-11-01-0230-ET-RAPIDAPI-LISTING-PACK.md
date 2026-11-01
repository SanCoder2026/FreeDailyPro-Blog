# FreeDailyPro RapidAPI listing pack

Written 2026-11-01 02:30 ET for the people who create and edit RapidAPI listings (Grok and the owner). Paste each fenced block into the matching field in RapidAPI Studio. Source of truth: origin/main of the FreeDailyPro repo (commit 0e1e9720), the readiness table docs/api-groups-readiness.md, the job-group specs in client/public/api-specs, and the discoverability playbook of 2026-10-31. Nothing in this pack changes any quota number or any price.

## How to use this pack
1. Part A: edit the six live listings first (about one day). Part B: create the new focused listings in the order shown. Part C: the 30-day checklist per wave. Part D: the day-by-day order, never more than 3 listings promoted at the same time.
2. Every fenced block is one Studio field. Fields marked CAPTURE need a real response pasted in before you publish (the pack never invents a response).
3. Two listings in this pack must wait for a check by Claude: Time Zone (B8) and Currency and VAT (B9); Bookkeeping (B11), PDF Forms (B4) and Video (B14) carry a gate too. They are marked GATE.

## Rules applied to all copy
- No code-hosting links. No competitor or brand names in names or tags (the one deliberate brand word is PowerPoint-compatible in the PPTX short and long text; see note 4).
- The word free appears only in tags. No price in any text. The brand name FreeDailyPro is fine.
- Claims are limited to what the code or spec says. Where a limit exists it is written in the Limits section of the long description.
- Counts: numbers of 50 or more are written as multiples of 50 (more than 50, about 200), with a plus sign only for whole-API counts (50+ endpoints, 200+ endpoints across all of FreeDailyPro). Small exact counts (14 categories, 7 endpoints) are written exactly, because they cannot be rounded to a multiple of 50.
- Plans: the descriptions below name no quota number, because Studio already shows each plan's number and this pack must not change them. The one figure I could verify is Basic at 5,000 requests a month and 60 per minute on the calculator listing (playbook, observed live); the Pro figure of 25,000 is from the same playbook. I found no source for the Ultra and Mega numbers or for the other five listings, so none is written.

## Notes that change what you paste
1. Errors are not billed. This is true of FreeDailyPro's own usage meter: utility-api/api/src/index.ts counts a call only when the response is below 400 (commit 067f2226 turned bad input that used to answer 200 into 400 or 422). I could not verify whether RapidAPI's own gateway also counts a 4xx call against a plan's monthly quota. The sentence in the pack says our usage meter does not count them, which is true either way. If the owner wants to say it more strongly, check Studio analytics for a 400 test call first.
2. The older spec files on main for the six live listings do not carry the per-endpoint unbilled-error notes that the new job specs carry, and two of them have grown since the listings were imported (calculators 69 operations, media 24). Re-import definitions from the files named in Part A, then check that example bodies and the endpoint order survived. I could not confirm what a Studio re-import overwrites.
3. Import only the files named in this pack. The folder also holds older duplicates (mortgage-and-loan-api, retirement-and-debt-api, powerpoint-toolkit-api, health-formulas-api, tax-and-paycheck-api, publishing-metadata-api, everyday-math-api) that must not become second listings.
4. PowerPoint is a trademark. The playbook warns against brand names in titles and tags, so the PPTX name and tags use the file-format word only; PowerPoint-compatible appears once in the short description and once in the long text as a plain description. If the owner prefers zero brand words, delete that phrase. Whether the short description is searched as strongly as the name is unverified.
5. Spec URLs: client/public is the site's static folder (vite.config.ts sets publicDir to client/public), so client/public/api-specs/<file> is served at https://freedailypro.com/api-specs/<file>. I could not fetch those URLs from this machine (no response through the proxy), so confirm one in a browser before the first import; if it fails, import the file from disk.
6. Each new Rapid listing needs its own gateway setup or every call returns 401: Gateway tab, secret header X-API-Key (same value the existing project uses), copy the listing's X-RapidAPI-Proxy-Secret, and add it as a new Railway variable of the form RAPID_PROXY_SECRET_<NAME> (utility-api/api/src/auth.ts accepts any suffix; suggested names are in Part D). This is configuration, not a code push.
7. Playbook finding 4: confirm the Studio project FreeDailyPro Public APIs is not public, so no duplicate listing of the same endpoints exists.
8. The six live listing texts were not pasted into the playbook. I built Part A from the draft listing packs in the repo, the playbook's observations and the current specs; if the live text differs, the new text replaces it anyway.

---
# Part A: the six live listings

Do these first. Edit order by impact: A1, A2, A4, A5, A3, A6. All six: set a distinct 500 by 500 PNG logo, add the tutorials below, and hide or unpublish the Basic (Deprecated) plan (see Retire in each section; Studio may refuse to remove a plan that has a subscriber, so hide it from public view instead, which I could not test).

## A1. Finance, Tax, Health and Planning Calculator API
Studio slug: `finance-tax-health-and-planning-calculator-api`. Spec to (re)import: `calculator-api.openapi.json` (69 operations; the older import had fewer, so re-import), served at https://freedailypro.com/api-specs/calculator-api.openapi.json

**Name**
```text
Paycheck, Mortgage, Tax and Retirement Calculator API
```
**Short description** (141 characters)
```text
Paycheck, 401k, retirement, mortgage, loan, income tax, VAT, BMI and TDEE calculators as JSON with the working shown. One key, 50+ endpoints.
```
**Long description** (paste as Markdown)
````markdown
Finance calculators for payroll tools, fintech and health apps, finance blogs and AI agents that need correct numbers, with the working shown, over plain JSON. Paycheck, income tax, 401k and retirement, mortgage and loans, VAT and sales tax, BMI and TDEE, unit conversion and everyday planning behind one key.

## What you can do
**Paycheck and tax**
- `/v1/converters/paycheck`: take-home pay per pay period: 2026 federal tax, FICA, state tax, 401k and section 125 deductions
- `/v1/converters/us-income-tax`: US federal income tax by filing status
- `/v1/converters/state-tax`: state income tax from a state schedule or a flat rate
- `/v1/converters/self-employment-tax`: self-employment tax
- `/v1/converters/uk-tax and /v1/converters/india-income-tax`: UK 2026/27 and India FY 2026-27 income tax
- `/v1/converters/sales-tax and /v1/converters/vat-gst`: sales tax, VAT and GST on an amount

**Mortgage and loans**
- `/v1/converters/loan`: loan payment with payment frequency, compounding, fees and APR
- `/v1/converters/mortgage`: mortgage payment with taxes, insurance, PMI and HOA, extra payments and payoff date
- `/v1/converters/amortization`: amortization schedule with payment dates and working
- `/v1/converters/refinance and /v1/converters/affordability`: refinance break-even and home affordability
- `/v1/converters/student-loan, /v1/converters/debt-payoff, /v1/converters/compound-interest`: student loan, avalanche against snowball payoff, interest

**Retirement and savings**
- `/v1/converters/401k`: 401k projection with the 2026 IRS limits
- `/v1/converters/retirement and /v1/converters/fire`: retirement and FIRE projections
- `/v1/converters/rmd, /v1/converters/social-security, /v1/converters/contribution-limits`: required minimum distribution, Social Security estimate, contribution limits
- `/v1/converters/529, /v1/converters/college-cost, /v1/converters/sip`: 529 plan, college cost, monthly investment projection

**Health and everyday**
- `/v1/converters/bmi, /v1/converters/bmr, /v1/converters/tdee, /v1/converters/body-fat`: BMI, BMR, TDEE and body fat
- `/v1/converters/percentage, /v1/converters/tip, /v1/converters/discount, /v1/converters/gpa`: percentage, tip, discount and GPA
- `/v1/converters/units, /v1/converters/age, /v1/converters/countdown`: unit conversion, age and countdown
- `/v1/planning/*`: budgets, packing lists, event and relocation planners

## Examples
**Take-home pay**
Request:
```
POST /v1/converters/paycheck
{
  "grossAnnual": 85000,
  "payPeriodsPerYear": 26,
  "filingStatus": "single",
  "state": "NY",
  "retirementPct": 5
}
```
Response (abridged):
```
{
  "tool": "Paycheck estimator: 2026 US federal tax, FICA, state tax and pre-tax deductions",
  "result": {
    "taxYear": 2026,
    "filingStatus": "single",
    "payPeriodsPerYear": 26,
    "grossPerCheck": 3269.23,
    "federal": 343.65,
    "state": 144.75,
    "socialSecurity": 202.69,
    "medicare": 47.4,
    "fica": 250.1,
    "retirement": 163.46,
    "netPerCheck": 2367.27,
    "estimatedAnnualNet": 61549
  }
}
```

**Loan payment with dates**
Request:
```
POST /v1/converters/loan
{
  "principal": 250000,
  "annualRatePercent": 6.5,
  "years": 30,
  "previewMonths": 3,
  "firstPaymentDate": "2026-12-01"
}
```
Response (abridged):
```
{
  "tool": "Loan calculator client and server side from freedailypro",
  "result": {
    "monthlyPayment": 1580.17,
    "totalPayment": 568861.22,
    "totalInterest": 318861.22,
    "schedulePreview": [
      {
        "month": 1,
        "principal": 226,
        "interest": 1354.17,
        "balance": 249774,
        "date": "2026-12-01"
      },
      {
        "month": 2,
        "principal": 227.23,
        "interest": 1352.94,
        "balance": 249546.77,
        "date": "2027-01-01"
      }
    ],
    "firstPaymentDate": "2026-12-01",
    "lastPaymentDate": "2056-11-01",
    "payoffDate": "2056-11"
  }
}
```

## Limits
- US tax figures use 2026 tables, UK 2026/27, India FY 2026-27; every tax response carries taxYear, sources and a disclaimer.
- Paycheck estimates leave out city and county taxes and employer-side taxes.
- Rates, returns and inflation are your inputs. There is no live market or mortgage-rate data.
- Currency conversion uses daily reference rates, not live rates.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Estimates for information, not tax, legal, medical or financial advice.
- Health results are general information, not medical advice.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Finance (keep)

**Tags**
```text
paycheck calculator, take home pay, 401k, retirement calculator, mortgage calculator, amortization, loan calculator, income tax, vat calculator, bmi calculator, tdee, free calculator api
```
**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/converters/paycheck`. Pre-fill the example body so one click returns take-home pay.
```json
{
  "grossAnnual": 85000,
  "payPeriodsPerYear": 26,
  "filingStatus": "single",
  "state": "NY",
  "retirementPct": 5
}
```
**Retire / fix**: Hide or unpublish the 'Basic (Deprecated)' plan (the 500,000 a month one) once no subscriber is on it; keep the current Basic. Do not change any quota number.

**Logo idea**: A calculator keypad with a percent sign, green on dark. A different colour from the other five.

**Tutorials (300 to 500 words each, ending on a working request in curl, JavaScript and Python)**: Take-home pay for a US salary in one request; Build a mortgage amortization table with payment dates; Check 401k limits and employer match in code.

## A2. PDF Toolkit API
Studio slug: `pdf-toolkit-api8`. Spec to (re)import: `pdf-toolkit-api.openapi.json` (20 operations), served at https://freedailypro.com/api-specs/pdf-toolkit-api.openapi.json

**Name**
```text
PDF Merge, Split, Compress and Form Fill API
```
**Short description** (136 characters)
```text
PDF merge, split, compress, rotate, watermark, redact and form fill API. One POST per job. Files are processed in memory and not stored.
```
**Long description** (paste as Markdown)
````markdown
Merge, split, compress, rotate, watermark, redact, repair and fill PDF files over HTTP, with one POST per job. For document portals, back-office tools, legal and HR software and no-code automations that need PDF steps without running a PDF library.

## What you can do
**Combine and split**
- `/v1/pdf/merge`: combine PDFs in the order sent
- `/v1/pdf/split`: split by page ranges
- `/v1/pdf/extract`: take chosen pages
- `/v1/pdf/organize`: reorder, rotate, delete or insert pages

**Edit**
- `/v1/pdf/rotate`: rotate chosen pages in steps of 90 degrees
- `/v1/pdf/add-page-numbers`: number every page
- `/v1/pdf/watermark`: stamp a text watermark
- `/v1/pdf/repair`: rebuild a damaged PDF so it opens

**Compress**
- `/v1/pdf/compress`: shrink to about half, or to a target size; headers report the saving
- `/v1/pdf/compress/lossless-bw, /smallest-bw, /greyscale`: scanned-page modes
- `/v1/pdf/compress/balanced, /aggressive, /extreme, /size`: fixed levels or a target size

**Forms and redaction**
- `/v1/fillable-forms/parse`: list the fields of a fillable PDF
- `/v1/fillable-forms/fill`: fill fields from JSON
- `/v1/pdf/flatten`: turn form fields into fixed text
- `/v1/redact-pdf`: remove everything under boxes from the file itself

## Examples
**Merge two PDFs**
Request:
```
POST /v1/pdf/merge  (multipart/form-data)
files = a.pdf
files = b.pdf
```
Response:
```
200 application/pdf: the merged file
```

**Compress a PDF**
Request:
```
POST /v1/pdf/compress  (multipart/form-data)
file = report.pdf
```
Response (headers from the spec example for a 119040 byte test file):
```
200 application/pdf: the smaller file, with headers
X-Original-Bytes: 119040
X-Compressed-Bytes: 28562
X-Reduction-Percent: 76
X-Compress-Note: Reached the target size using the gentlest picture settings that fit; text stays text.
```

## Limits
- Up to 20 MB and 100 pages per PDF.
- Password-protected or unreadable PDFs return 422. Compress returns 422 when nothing can be made smaller.
- Compress has a time budget of about 25 seconds per request.
- Forms: AcroForm fields only, not XFA dynamic forms.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Redaction removes the text and content under each box from the file itself; it does not just cover it.
- Opening an endpoint in a browser sends GET and returns 405: use POST with multipart/form-data.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Tools (change from Data)

**Tags**
```text
pdf merge, pdf split, pdf compress, pdf form fill, pdf redact, pdf watermark, pdf repair, flatten pdf, free pdf api
```
**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Files up to 20 MB and 100 pages. Errors are not billed.
Pro: for apps in production. A larger monthly quota and the larger file limits, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota and the larger file limits, every endpoint included.
Mega: for high-volume use. The largest monthly quota and the larger file limits, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/fillable-forms/parse`. Single file, no other field, so the playground needs only one file picker. Host a small sample fillable PDF on the site and link it in the description (not hosted yet: see Part C).
```json
{
  "file": "(a small fillable PDF)"
}
```
**Retire / fix**: Hide or unpublish 'Basic (Deprecated)'. Rename the listing (the slug keeps the 8). Change the category from Data to Tools.

**Logo idea**: Two page sheets with a merge arrow, red accent. Distinct from the PDF Forms logo (one page with a tick box).

**Tutorials (300 to 500 words each, ending on a working request in curl, JavaScript and Python)**: Merge and compress PDFs from a script in one request each; Fill a PDF form from JSON (and flatten it).

## A3. Text and Developer Utilities API
Studio slug: `text-and-developer-utilities-api`. Spec to (re)import: `text-and-developer-utilities-api.openapi.json` (55 operations), served at https://freedailypro.com/api-specs/text-and-developer-utilities-api.openapi.json

**Name**
```text
Developer Utilities API: JWT, Hash, UUID, Regex, Cron and Text Tools
```
**Short description** (135 characters)
```text
JWT decoder, hash generator, UUID, regex tester, cron explainer, word count, QR code and SEO tag tools as JSON. One key, 50+ endpoints.
```
**Long description** (paste as Markdown)
````markdown
Small developer and text tools for apps, scripts, no-code automations and AI agents, as plain JSON: decode JWTs, hash text, generate UUIDs and passwords, test regex, explain cron expressions, count words, score readability, build QR codes and SEO tags.

## What you can do
**Developer tools**
- `/v1/security/jwt-decode`: decode a JWT header and payload and check its time claims
- `/v1/security/hash`: MD5, SHA-1, SHA-256, SHA-384 or SHA-512
- `/v1/security/uuid`: random version 4 UUIDs, up to 1000 at a time
- `/v1/security/regex`: test a regex pattern
- `/v1/security/cron`: explain and validate a cron expression
- `/v1/security/base64, /v1/security/url, /v1/security/html-entities, /v1/security/json-format, /v1/security/minify`: encode, decode, format
- `/v1/security/qr and /v1/security/barcode-code128`: QR code as SVG, Code 128 barcode

**Text tools**
- `/v1/text/word-count`: words, characters, sentences, reading time
- `/v1/text/readability`: Flesch ease and grade level
- `/v1/text/slug, /v1/text/case-convert, /v1/text/sort, /v1/text/find-replace`: clean and transform text
- `/v1/text/extract-emails and /v1/text/extract-urls`: pull emails and links out of text
- `/v1/security/diff and /v1/text/similarity`: compare two texts
- `/v1/text/grammar-check and /v1/text/paraphrase`: rule-based English fixes and rewording (not AI)

**SEO and design**
- `/v1/seo/meta-tags, /v1/seo/schema, /v1/seo/robots-sitemap`: meta tags, JSON-LD, robots.txt and sitemap.xml
- `/v1/seo/keyword-density and /v1/seo/hashtags`: keyword density and hashtags
- `/v1/design/color-convert and /v1/design/contrast`: colour conversion and contrast ratio

## Examples
**Decode a JWT**
Request:
```
POST /v1/security/jwt-decode
{
  "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZXhwIjoxNTc3ODM2ODAwfQ.c2lnbmF0dXJl"
}
```
Response:
```
{
  "tool": "Jwt decoder",
  "valid": false,
  "wellFormed": true,
  "status": "expired",
  "signatureVerified": false,
  "issues": [
    "The token expired at 2020-01-01T00:00:00.000Z (exp), 215534435 seconds before the time checked."
  ],
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "1234567890",
    "exp": 1577836800
  },
  "signature": "c2lnbmF0dXJl",
  "evaluatedAt": "2026-10-30T14:40:35.000Z",
  "algorithm": "HS256",
  "expiresAt": "2020-01-01T00:00:00.000Z",
  "secondsUntilExpiry": -215534435,
  "expired": true
}
```

**Explain a cron expression**
Request:
```
POST /v1/security/cron
{
  "expression": "30 9 * * 1-5"
}
```
Response:
```
{
  "tool": "Cron builder client and server side from freedailypro",
  "valid": true,
  "expression": "30 9 * * 1-5",
  "description": "At 30, past 9, on every day of the month, in every month, on 1-5.",
  "fields": {
    "minute": "30",
    "hour": "9",
    "dayOfMonth": "*",
    "month": "*",
    "dayOfWeek": "1-5"
  }
}
```

## Limits
- JWT: this endpoint decodes only. It never verifies the signature, so a token that decodes cleanly is not proof it is genuine; signatureVerified is always false.
- Grammar check and paraphrase are rule-based, not an AI model.
- UUID: 1 to 1000 per call.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Many of these are one-liners in any language; the value is one HTTP call from no-code tools and AI agents.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Tools (keep)

**Tags**
```text
jwt decoder, hash generator, uuid generator, regex tester, cron expression, base64, word counter, readability score, slug generator, seo meta tags, qr code generator, free developer api
```
**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/security/jwt-decode`. JSON body, instant answer, shows the honest "signature not verified" fields.
```json
{
  "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZXhwIjoxNTc3ODM2ODAwfQ.c2lnbmF0dXJl"
}
```
**Retire / fix**: Hide or unpublish 'Basic (Deprecated)'. This stays the umbrella: do not chase single-job text keywords with it.

**Logo idea**: Angle brackets with a small key, teal. Distinct from the calculator and PDF marks.

**Tutorials (300 to 500 words each, ending on a working request in curl, JavaScript and Python)**: Decode a JWT and check its expiry from a script; Generate UUIDs, hashes and slugs in a build step.

## A4. Business Document API
Studio slug: `business-document-api`. Spec to (re)import: `business-document-api.openapi.json` (26 operations), served at https://freedailypro.com/api-specs/business-document-api.openapi.json

**Name**
```text
Pay Stub, Invoice, Receipt and Contract Draft API
```
**Short description** (137 characters)
```text
Pay stub generator, invoice and receipt totals, NDA, lease and offer letter drafts, bank statement to CSV, margin and break-even as JSON.
```
**Long description** (paste as Markdown)
````markdown
Finished business documents and document maths from JSON, for payroll, freelancer, property and HR apps that need a pay stub, invoice or receipt totals, or a contract draft, without building templates.

## What you can do
**Pay and money**
- `/v1/business/pay-stub`: pay stub with gross pay, deductions and net pay, as JSON (not a PDF)
- `/v1/business/invoice-totals`: subtotal, discount, tax and total from line items
- `/v1/business/receipt`: receipt from line items and a tax rate
- `/v1/business/profit-margin, /v1/business/product-margin, /v1/business/break-even, /v1/business/marketplace-fee, /v1/business/shipping-estimate`: margin, markup, break-even, fee and shipping maths
- `/v1/business/expenses`: expense totals by category

**Drafts**
- `/v1/business/nda-draft`: mutual non-disclosure agreement
- `/v1/business/offer-letter-draft`: employment offer letter
- `/v1/business/lease-draft`: residential lease
- `/v1/business/bill-of-sale-draft, /v1/business/promissory-note-draft, /v1/business/poa-draft, /v1/business/eviction-notice-draft`: other common drafts
- `/v1/business/proposal, /v1/business/cover-letter, /v1/business/resume-outline, /v1/business/rental-application`: proposal, cover letter, resume outline, rental application

**Data**
- `/v1/business/bank-statement-to-csv`: bank statement (text-based PDF or pasted text) to transactions, CSV and a balance check
- `/v1/business/blind-cv`: remove names and contact details from a CV for fair screening

## Examples
**Pay stub**
Request:
```
POST /v1/business/pay-stub
{
  "employer": "Northwind Design LLC",
  "employee": "Maria Lopez",
  "periodStart": "2026-10-01",
  "periodEnd": "2026-10-15",
  "payDate": "2026-10-20",
  "payType": "hourly",
  "rate": "28.50",
  "hours": "80",
  "overtimeHours": "4",
  "fedPct": "12",
  "statePct": "4",
  "ssPct": "6.2",
  "medPct": "1.45",
  "health": "85"
}
```
Response (abridged):
```
{
  "tool": "Pay stub generator client and server side from freedailypro",
  "result": {
    "figures": {
      "regular": 2280,
      "overtime": 171,
      "gross": 2451,
      "totalDeductions": 664.66,
      "net": 1786.34,
      "regularHours": 80,
      "overtimeHours": 4
    },
    "document": "(title, sections and a suggested filename, as JSON: not a PDF)"
  }
}
```

**Invoice totals**
Request:
```
POST /v1/business/invoice-totals
{
  "lines": [
    {
      "description": "Design",
      "qty": 1,
      "unitPrice": 2400
    },
    {
      "description": "Build",
      "qty": 1,
      "unitPrice": 3600
    }
  ],
  "taxPct": 8.25,
  "discountPct": 5
}
```
Response:
```
{
  "tool": "Invoice totals client and server side from freedailypro",
  "result": {
    "subtotal": 6000,
    "discount": 300,
    "tax": 470.25,
    "total": 6170.25
  }
}
```

## Limits
- The pay stub applies the percentages you send; it does not work out taxes for you. Use the paycheck calculator for that.
- Bank statement: text-based PDFs or pasted text only; scanned PDFs are refused with 422 because OCR is not supported.
- Documents come back as structured JSON (figures and sections), not as a PDF file.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Drafts are starting points, not legal advice. Have a professional review contracts before use.
- Government-forms returns an index of common forms, not the official forms.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Business (keep)

**Tags**
```text
pay stub generator, invoice calculator, receipt, nda template, lease template, offer letter, profit margin, break even, bank statement to csv, free document api
```
**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/business/pay-stub`. Pre-fill the hourly example.
```json
{
  "employer": "Northwind Design LLC",
  "employee": "Maria Lopez",
  "periodStart": "2026-10-01",
  "periodEnd": "2026-10-15",
  "payDate": "2026-10-20",
  "payType": "hourly",
  "rate": "28.50",
  "hours": "80",
  "overtimeHours": "4",
  "fedPct": "12",
  "statePct": "4",
  "ssPct": "6.2",
  "medPct": "1.45",
  "health": "85"
}
```
**Retire / fix**: Hide or unpublish 'Basic (Deprecated)'. Move the bank-statement endpoint lower in the list; pay stub, invoice and receipt lead.

**Logo idea**: A document with a folded corner and a stamp, amber. Distinct from the others.

**Tutorials (300 to 500 words each, ending on a working request in curl, JavaScript and Python)**: Generate a pay stub from hours and rate in code; Calculate invoice totals with tax and discount.

## A5. Image, Audio and Video Conversion API
Studio slug: `image-audio-and-video-conversion-api`. Spec to (re)import: `media-conversion-api.openapi.json` (24 operations; the older import had 22, so re-import), served at https://freedailypro.com/api-specs/media-conversion-api.openapi.json

**Name**
```text
Video, Image and Audio Converter API
```
**Short description** (131 characters)
```text
Video compress, MP4 to GIF, video thumbnail, image resize, WebP and AVIF convert, audio convert and normalize. One upload per call.
```
**Long description** (paste as Markdown)
````markdown
Convert and process media files over HTTP for apps that handle user uploads and need quick conversions without running their own media software: compress and trim video, make GIFs and thumbnails, resize, compress and convert images, convert and clean up audio.

## What you can do
**Image**
- `/v1/image/resize`: resize with fit modes (fill, contain, cover, inside, outside)
- `/v1/image/convert`: PNG, JPEG, WebP, AVIF, GIF, TIFF, BMP or ICO
- `/v1/image/compress`: smaller file with quality and metadata stripping
- `/v1/image/crop, /v1/image/flip, /v1/image/rotate, /v1/image/watermark`: crop, flip, rotate in 90 degree steps, text or picture watermark

**Video**
- `/v1/video/compress`: re-encode to a smaller file
- `/v1/video/convert`: MP4, WebM or MOV
- `/v1/video/to-gif, /v1/video/thumbnail, /v1/video/extract-audio`: GIF, JPEG frame, MP3 track
- `/v1/video/trim, /v1/video/merge, /v1/video/subtitle`: trim, join, burn in SRT subtitles

**Audio**
- `/v1/audio/convert`: MP3, WAV, OGG, M4A or FLAC
- `/v1/audio/compress, /v1/audio/normalize, /v1/audio/denoise, /v1/audio/remove-silence`: smaller, louder-matched, cleaner audio
- `/v1/audio/trim, /v1/audio/merge, /v1/audio/speed, /v1/audio/pitch`: cut, join, change speed 0.5x to 2x or pitch

## Examples
**Resize an image**
Request:
```
POST /v1/image/resize  (multipart/form-data)
file = photo.jpg
width = 800
height = 600
fit = cover
```
Response:
```
200 image (same format as the input unless format is given)
X-Image-Width, X-Image-Height and X-Image-Frames headers describe the result
```

**Thumbnail from a video**
Request:
```
POST /v1/video/thumbnail  (multipart/form-data)
file = clip.mp4
```
Response:
```
200 image/jpeg: the frame at the given time
```

## Limits
- Basic plan: images up to 10 MB; video and audio up to 25 MB and 60 seconds per request. Over the limit returns 413 or 422 and is not billed.
- Paid plans: images up to 15 MB, audio up to 30 MB, video up to 100 MB per file.
- Video is processed on a shared server: large files can take a minute or more, and a busy service answers 503 with Retry-After. Keep uploads small (under 50 MB) for fast results.
- Upload only: no URL input. HEIC photos are not supported. No background removal.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- No transcription, text to speech or downloading from video sites.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Video, Images (the hub lists it as "Video and Images"; change from Media)

**Tags**
```text
video compress, mp4 to gif, extract audio, video thumbnail, image resize, webp, avif, audio converter, watermark, image compress
```
**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Images up to 10 MB; video and audio up to 25 MB and 60 seconds. Errors are not billed.
Pro: for apps in production. A larger monthly quota and the larger file limits, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota and the larger file limits, every endpoint included.
Mega: for high-volume use. The largest monthly quota and the larger file limits, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/image/resize`. Small input, fast, one file. Do not pin video compress first: it is slow and hurts the service level figure.
```json
{
  "file": "(a small PNG)",
  "width": 320,
  "height": 240,
  "fit": "cover"
}
```
**Retire / fix**: Hide or unpublish 'Basic (Deprecated)'. Use ONE name everywhere: the Studio card and header say "Image, Audio and Video Conversion API" while the page title says "Video & Image Converter API". Check that the Video and Audio endpoint groups are populated after the re-import.

**Logo idea**: A play triangle over a picture frame, violet. Distinct from the other five.

**Tutorials (300 to 500 words each, ending on a working request in curl, JavaScript and Python)**: Resize and convert images to WebP in one request; Make a GIF and a thumbnail from a short video.

## A6. Book Publishing API
Studio slug: `book-publishing-api`. Spec to (re)import: `book-publishing-api.openapi.json` (10 operations), served at https://freedailypro.com/api-specs/book-publishing-api.openapi.json

**Name**
```text
Book Spine Width, ISBN and Print Royalty API
```
**Short description** (127 characters)
```text
Book spine width calculator, ISBN validator, print royalty, ONIX, EPUB and print-ready PDF for self-publishers as JSON or file.
```
**Long description** (paste as Markdown)
````markdown
Publishing helpers for self-publishing platforms, author tools and small presses: check and convert ISBNs, work out spine width and full cover size, estimate print cost and royalty, build ONIX records, and produce EPUB and print-ready PDF from structured chapters.

## What you can do
**Numbers**
- `/v1/publishing/isbn`: check an ISBN-10 or ISBN-13, convert and hyphenate
- `/v1/publishing/spine-width`: spine width, full cover size and panel positions
- `/v1/publishing/print-royalty`: print cost, royalty per copy, price for a target royalty

**Metadata and descriptions**
- `/v1/publishing/onix`: ONIX 3.0 product record for one book
- `/v1/publishing/kdp-description`: format a description as the limited HTML the store allows
- `/v1/ecommerce/etsy-listing-check`: check an Etsy shop listing title and tags against Etsy's rules

**Files**
- `/v1/publishing/epub`: EPUB 3 e-book from chapters
- `/v1/publishing/typeset-book`: print-ready book PDF
- `/v1/publishing/typeset-manuscript, /v1/publishing/manuscript-docx`: standard manuscript format as PDF or Word

## Examples
**Check an ISBN**
Request:
```
POST /v1/publishing/isbn
{
  "isbn": "978-0-306-40615-7"
}
```
Response:
```
{
  "result": {
    "input": "978-0-306-40615-7",
    "clean": "9780306406157",
    "kind": "isbn13",
    "wellFormed": true,
    "valid": true,
    "convertedFromCorrected": false,
    "givenCheck": "7",
    "expectedCheck": "7",
    "isbn10": "0306406152",
    "isbn13": "9780306406157",
    "isbn10Hyphenated": "0-306-40615-2",
    "isbn13Hyphenated": "978-0-306-40615-7",
    "groupName": "English language",
    "barcodeDigits": "9780306406157"
  }
}
```

**Spine width and cover size**
Request:
```
POST /v1/publishing/spine-width
{
  "platform": "kdp",
  "trimWidthIn": 6,
  "trimHeightIn": 9,
  "pages": 320,
  "thicknessIn": 0.002252
}
```
Response (abridged):
```
{
  "result": {
    "spineIn": 0.7206,
    "coverWidthIn": 12.9706,
    "coverHeightIn": 9.25,
    "pixels": {
      "width": 3892,
      "height": 2775,
      "dpi": 300
    },
    "panels": {
      "back": {
        "x": 0.125,
        "y": 0.125,
        "w": 6,
        "h": 9
      },
      "spine": {
        "x": 6.125,
        "y": 0.125,
        "w": 0.7206,
        "h": 9
      },
      "front": {
        "x": 6.8456,
        "y": 0.125,
        "w": 6,
        "h": 9
      }
    },
    "warnings": []
  }
}
```
Abridged: the real response also carries a plain-text summary.

## Limits
- Spine and cover numbers are starting values: the printer's own cover template is the authority.
- Spine width: trim 2 to 14 inches, 1 to 2000 pages.
- Typesetting: trim 3 to 14 inches, up to 100 chapters; when busy the answer is 503 with Retry-After.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Royalty maths uses the charges you send; check them against your printer.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Media (keep; Tools or Business are alternatives, unverified which gets more views)

**Tags**
```text
spine width calculator, isbn validator, isbn converter, print royalty, onix, epub generator, print on demand, book cover size, manuscript format
```
**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/publishing/isbn`. JSON body, instant answer.
```json
{
  "isbn": "978-0-306-40615-7"
}
```
**Retire / fix**: Hide or unpublish 'Basic (Deprecated)'. Low priority: edit after the other five.

**Logo idea**: An open book with a ruled spine line, brown. Distinct from the others.

**Tutorials (300 to 500 words each, ending on a working request in curl, JavaScript and Python)**: Check and convert an ISBN in code; Work out spine width and full cover size for a paperback.

---
# Part B: new focused listings

Order: B1 to B6 are Wave 1. B7 to B9 are Wave 2, B10 to B12 Wave 3, B13 and B14 Wave 4. The same endpoint set is never copied into more than two listings (each focused listing is a subset of one umbrella from Part A). Each focused long description ends with a plain one-line pointer to FreeDailyPro and no link to an umbrella listing. For every listing: create the API in Studio, import the named spec, set the base URL and gateway as in note 6, paste the fields, upload the logo, tick the Terms box, then publish.

## B1. PPTX generator
Wave 1, slot 1 (promotion starts Day 3)
Spec to import: `powerpoint-api.openapi.json` (26 operations), served at https://freedailypro.com/api-specs/powerpoint-api.openapi.json. MCP path on the same key: /mcp/powerpoint. Suggested Rapid slug: `pptx-generator-api`.

**Name**
```text
PPTX Generator API: Markdown, JSON and CSV to Slides
```
**Short description** (137 characters)
```text
Create PowerPoint-compatible PPTX decks from Markdown, JSON or CSV with one POST. Themes, tables, notes. Processed in memory, not stored.
```
**Long description** (paste as Markdown)
````markdown
Create editable PowerPoint-compatible .pptx presentations from Markdown, JSON or CSV with one HTTP request, for reporting and BI tools, CRMs, automations and AI agents that need a real deck out of data. The same API reads, edits and checks existing .pptx files.

## What you can do
**Build a deck**
- `/v1/pptx/from-markdown`: Markdown or an indented outline to slides with themes, tables and speaker notes
- `/v1/pptx/from-json`: JSON slides with bullets, numbered lists, tables, pictures with alt text and notes
- `/v1/pptx/from-csv`: a CSV table to table slides, with row ranges in the notes

**Read a deck**
- `/v1/pptx/extract/text`: text of every slide as txt, md or json
- `/v1/pptx/extract/notes`: speaker notes
- `/v1/pptx/extract/images`: the pictures
- `/v1/pptx/extract/charts`: the data behind charts
- `/v1/pptx/fonts`: fonts used

**Edit and combine**
- `/v1/pptx/merge`: 2 to 10 decks into one
- `/v1/pptx/split`: one deck into several
- `/v1/pptx/organize`: reorder, delete, duplicate slides
- `/v1/pptx/find-replace`: find and replace text
- `/v1/pptx/replace-fonts`: swap fonts
- `/v1/pptx/slide-numbers`: add or remove slide numbers
- `/v1/pptx/watermark`: add or remove a watermark
- `/v1/pptx/resize`: change the slide size

**Shrink, clean and check**
- `/v1/pptx/compress/default, /medium, /strong, /size`: re-save pictures at three levels or to a target size
- `/v1/pptx/clean`: remove notes, comments, hidden slides and author details
- `/v1/pptx/redact`: black out sensitive text and pictures
- `/v1/pptx/accessibility-check`: JSON or CSV report of accessibility problems
- `/v1/pptx/repair`: repair a damaged deck
- `/v1/pptx/html-slideshow`: one self-contained HTML slideshow
- `/v1/pptx/to-template`: a .potx template or a re-themed deck

## Examples
**Markdown to a deck**
Request:
```
POST /v1/pptx/from-markdown
{
  "markdown": "# Quarterly Review\nQ3 results and next steps\nNote: Welcome everyone.\n\n## What went well\n- Revenue up **12%**\n  - One new customer in healthcare\n- Support response time under 2 hours\n\n## Numbers\n| Metric | Q2 | Q3 |\n| --- | --- | --- |\n| Revenue | 1.2M | 1.34M |\n\n---\n\n## Next steps\n1. Hire a customer success lead\n2. Launch the new pricing page",
  "theme": "clean"
}
```
Response (headers from the spec example):
```
200 application/vnd.openxmlformats-officedocument.presentationml.presentation (the .pptx file; 84,174 bytes in the spec example)
X-Slides: 4
X-Theme: clean
```

**JSON slides to a deck**
Request:
```
POST /v1/pptx/from-json
{"title": "Q3 Review", "theme": "corporate", "slides": [{"title": "Q3 Review", "subtitle": "Revenue and next steps"}, {"title": "Highlights", "bullets": ["Revenue up **12%** on last quarter", {"text": "Two new customers", "bullets": ["Healthcare", "Logistics"]}], "notes": "Mention the healthcare win by name."}, {"title": "Numbers at a glance", "table": {"header": ["Metric", "Q2", "Q3"], "rows": [["Revenue", "1.2M", "1.34M"], ["New customers", 5, 7]]}}]}
```
Response (structure from the spec; capture the real headers for this exact body before publishing):
```
200 application/vnd.openxmlformats-officedocument.presentationml.presentation (the .pptx file)
X-Slides, X-Theme and X-Warning-Count headers describe the result; X-Warnings lists problems such as a missing picture description.
```

## Limits
- Uploaded .pptx: up to 50 MB and 500 slides; .ppt and password-protected files are not accepted.
- From JSON: up to 200 slides, 40 bullets and 5000 characters per text, tables up to 60 rows and 12 columns, pictures 8 MB each and 24 MB in all, sent as base64 (PNG, JPEG or GIF).
- Markdown: up to 1,000,000 characters or a 10 MB file. Pictures given by web address are never fetched; use from-json to add pictures.
- CSV: up to 10 MB, 12 columns and 200 slides. Cells are kept as plain text.
- Merge: 2 to 10 decks, 100 MB in all; decks with different slide sizes are refused.
- Themes: clean, dark, corporate, warm, minimal, or your own brand colour and fonts.
- No rendering of slides to images or PDF. Text extraction does not read charts or diagrams.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Compress and split use more processing time than the build endpoints.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Tools

**Tags**
```text
pptx generator, markdown to pptx, json to pptx, csv to pptx, slides, presentation api, pptx api, slide deck, speaker notes, free pptx api
```
**Endpoints (path and purpose)**
- `/v1/pptx/from-markdown`: Markdown or an indented outline to slides with themes, tables and speaker notes
- `/v1/pptx/from-json`: JSON slides with bullets, numbered lists, tables, pictures with alt text and notes
- `/v1/pptx/from-csv`: a CSV table to table slides, with row ranges in the notes
- `/v1/pptx/extract/text`: text of every slide as txt, md or json
- `/v1/pptx/extract/notes`: speaker notes
- `/v1/pptx/extract/images`: the pictures
- `/v1/pptx/extract/charts`: the data behind charts
- `/v1/pptx/fonts`: fonts used
- `/v1/pptx/merge`: 2 to 10 decks into one
- `/v1/pptx/split`: one deck into several
- `/v1/pptx/organize`: reorder, delete, duplicate slides
- `/v1/pptx/find-replace`: find and replace text
- `/v1/pptx/replace-fonts`: swap fonts
- `/v1/pptx/slide-numbers`: add or remove slide numbers
- `/v1/pptx/watermark`: add or remove a watermark
- `/v1/pptx/resize`: change the slide size
- `/v1/pptx/compress/default, /medium, /strong, /size`: re-save pictures at three levels or to a target size
- `/v1/pptx/clean`: remove notes, comments, hidden slides and author details
- `/v1/pptx/redact`: black out sensitive text and pictures
- `/v1/pptx/accessibility-check`: JSON or CSV report of accessibility problems
- `/v1/pptx/repair`: repair a damaged deck
- `/v1/pptx/html-slideshow`: one self-contained HTML slideshow
- `/v1/pptx/to-template`: a .potx template or a re-themed deck

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Uploaded decks up to 50 MB. Errors are not billed.
Pro: for apps in production. A larger monthly quota and the larger file limits, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota and the larger file limits, every endpoint included.
Mega: for high-volume use. The largest monthly quota and the larger file limits, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/pptx/from-markdown`. Returns a file: say so in the endpoint description. If the playground cannot show binary output, add a note "use Code Snippets and save the response as deck.pptx".
```json
{
  "markdown": "# Quarterly Review\nQ3 results and next steps\nNote: Welcome everyone.\n\n## What went well\n- Revenue up **12%**\n  - One new customer in healthcare\n- Support response time under 2 hours\n\n## Numbers\n| Metric | Q2 | Q3 |\n| --- | --- | --- |\n| Revenue | 1.2M | 1.34M |\n\n---\n\n## Next steps\n1. Hire a customer success lead\n2. Launch the new pricing page",
  "theme": "clean"
}
```
**Logo and screenshot ideas**: A stack of three slides with a down arrow from a Markdown hash sign, orange. Screenshot: Markdown on the left, the opened deck on the right (one image).

**Tutorial and article titles**
- Turn Markdown into a PPTX deck with one POST (curl, JavaScript, Python)
- Build a weekly report deck from JSON rows, with a table and speaker notes
- Let an AI agent write slides: Markdown or JSON to PPTX over MCP

## B2. 401k and retirement calculator
Wave 1, slot 2 (promotion starts Day 4)
Spec to import: `retirement-debt-api.openapi.json` (11 operations), served at https://freedailypro.com/api-specs/retirement-debt-api.openapi.json. MCP path on the same key: /mcp/retirement-debt. Suggested Rapid slug: `401k-and-retirement-calculator-api`.

**Name**
```text
401k and Retirement Calculator API
```
**Short description** (143 characters)
```text
401k calculator and retirement calculator API: 2026 IRS limits, RMD, Social Security, FIRE, 529 and debt payoff as JSON with the working shown.
```
**Long description** (paste as Markdown)
````markdown
Retirement and savings maths as JSON for fintech apps, benefits portals, planning blogs and AI agents: project a 401k with the 2026 IRS limits, estimate required minimum distributions and Social Security, run retirement and FIRE projections, and compare debt payoff plans.

## What you can do
**Retirement**
- `/v1/converters/401k`: 401k projection with employer match and the 2026 IRS limit for the age you send
- `/v1/converters/retirement`: retirement and FIRE projection: nest egg in today's money, sustainable income, goal gap, drawdown by age
- `/v1/converters/fire`: savings target and years to financial independence
- `/v1/converters/rmd`: required minimum distribution from the IRS Uniform Lifetime Table
- `/v1/converters/social-security`: Social Security retirement benefit estimate with the 2026 bend points
- `/v1/converters/contribution-limits`: 401k, SIMPLE, IRA and HSA limits by tax year with catch-ups and Roth phase-outs

**Savings and education**
- `/v1/converters/sip`: monthly investment projection
- `/v1/converters/529`: 529 plan balance projection
- `/v1/converters/college-cost`: year-by-year college cost with inflation

**Debt**
- `/v1/converters/student-loan`: payoff time and total interest
- `/v1/converters/debt-payoff`: avalanche and snowball side by side, with a minimums-only baseline

## Examples
**401k projection**
Request:
```
POST /v1/converters/401k
{
  "currentBalance": 20000,
  "annualContribution": 7500,
  "employerMatchPct": 50,
  "expectedReturnPct": 7,
  "years": 30,
  "age": 45,
  "startDate": "2026-11-01"
}
```
Response (abridged):
```
{
  "tool": "401(k) projection with the 2026 IRS contribution limits",
  "result": {
    "projectedBalance": 1214928.95,
    "years": 30,
    "totalContributed": 357500,
    "taxYear": 2026,
    "annualContributionUsed": 7500,
    "irsLimits": {
      "employeeDeferral": 24500,
      "catchUpAge50": 8000,
      "catchUpAge60to63": 11250,
      "limitForAge": 24500,
      "ageUsed": 45
    },
    "contributionExceedsIrsLimit": false,
    "dataStatus": "checked",
    "startDate": "2026-11-01",
    "endDate": "2056-11-01"
  }
}
```

**Required minimum distribution**
Request:
```
POST /v1/converters/rmd
{
  "accountBalance": 500000,
  "age": 75,
  "birthYear": 1951
}
```
Response (abridged):
```
{
  "tool": "RMD estimator using the IRS Uniform Lifetime Table",
  "result": {
    "factor": 24.6,
    "rmd": 20325.2,
    "age": 75,
    "accountBalance": 500000,
    "table": "IRS Uniform Lifetime Table (2022 onward)",
    "taxYear": 2026,
    "rmdStartAge": 73,
    "rmdRequiredThisYear": true,
    "dataStatus": "checked"
  }
}
```

## Limits
- US-centred: IRS and SSA rules only.
- Contribution limits cover tax years 2025 and 2026; an unsupported year is a 400 that lists the years held. The API does not guess future limits.
- The 401k projection does not model the overall section 415(c) limit, future limit increases or salary growth.
- RMD uses the Uniform Lifetime Table for account owners; it is not right for a sole beneficiary spouse more than 10 years younger or for inherited accounts.
- Return, inflation and withdrawal rate are your assumptions, never market data.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Estimates for information, not financial or tax advice. Every response carries taxYear, sources and dataStatus.
- Limits are updated by FreeDailyPro each November when the IRS and SSA publish the next figures.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Finance

**Tags**
```text
401k, 401k calculator, retirement calculator, rmd, social security, fire calculator, 529, contribution limits, ira limits, debt payoff, free retirement api
```
**Endpoints (path and purpose)**
- `/v1/converters/401k`: 401k projection with employer match and the 2026 IRS limit for the age you send
- `/v1/converters/retirement`: retirement and FIRE projection: nest egg in today's money, sustainable income, goal gap, drawdown by age
- `/v1/converters/fire`: savings target and years to financial independence
- `/v1/converters/rmd`: required minimum distribution from the IRS Uniform Lifetime Table
- `/v1/converters/social-security`: Social Security retirement benefit estimate with the 2026 bend points
- `/v1/converters/contribution-limits`: 401k, SIMPLE, IRA and HSA limits by tax year with catch-ups and Roth phase-outs
- `/v1/converters/sip`: monthly investment projection
- `/v1/converters/529`: 529 plan balance projection
- `/v1/converters/college-cost`: year-by-year college cost with inflation
- `/v1/converters/student-loan`: payoff time and total interest
- `/v1/converters/debt-payoff`: avalanche and snowball side by side, with a minimums-only baseline

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/converters/401k`. Pre-filled example returns a projected balance and the 2026 limit for the age sent.
```json
{
  "currentBalance": 20000,
  "annualContribution": 7500,
  "employerMatchPct": 50,
  "expectedReturnPct": 7,
  "years": 30,
  "age": 45,
  "startDate": "2026-11-01"
}
```
**Logo and screenshot ideas**: A nest egg with an upward line, deep blue. Screenshot: the 401k response with limitForAge highlighted.

**Tutorial and article titles**
- Check your 401k contribution limit for 2026 with one API call
- Project a 401k balance with employer match in Python
- Build a required minimum distribution checker with the RMD endpoint

## B3. Paycheck and payroll tax
Wave 1, slot 3 (promotion starts Day 5)
Spec to import: `payroll-paycheck-api.openapi.json` (7 operations), served at https://freedailypro.com/api-specs/payroll-paycheck-api.openapi.json. MCP path on the same key: /mcp/payroll-paycheck. Suggested Rapid slug: `paycheck-and-payroll-tax-calculator-api`.

**Name**
```text
Paycheck and Payroll Tax Calculator API
```
**Short description** (142 characters)
```text
Paycheck calculator API: take-home pay, federal and state tax, FICA, self-employment tax and pay stub as JSON. 2026 tax tables, working shown.
```
**Long description** (paste as Markdown)
````markdown
Estimate take-home pay and payroll tax as JSON for payroll tools, HR and finance apps, freelancer tools and AI agents: per-paycheck federal and state tax, FICA, 401k and section 125 deductions, self-employment tax, UK and India income tax, and a pay stub built from hours and rate.

## What you can do
**Take-home pay**
- `/v1/converters/paycheck`: per-check take-home pay from salary: 2026 federal tax, employee FICA, state tax for all 50 states and DC, 401k and section 125 deductions, California SDI
- `/v1/converters/us-income-tax`: US federal income tax by filing status, with FICA and state tax
- `/v1/converters/state-tax`: state income tax from a state schedule or a flat rate

**Self-employed and other countries**
- `/v1/converters/self-employment-tax`: self-employment tax with quarterly estimates
- `/v1/converters/uk-tax`: UK income tax and National Insurance 2026/27, with Scottish rates
- `/v1/converters/india-income-tax`: India income tax FY 2026-27, old and new regime

**Pay stub**
- `/v1/business/pay-stub`: pay stub with gross pay, deductions and net pay from hours, rate and the percentages you send

## Examples
**Take-home pay**
Request:
```
POST /v1/converters/paycheck
{
  "grossAnnual": 85000,
  "payPeriodsPerYear": 26,
  "filingStatus": "single",
  "state": "NY",
  "retirementPct": 5
}
```
Response (abridged):
```
{
  "tool": "Paycheck estimator: 2026 US federal tax, FICA, state tax and pre-tax deductions",
  "result": {
    "taxYear": 2026,
    "filingStatus": "single",
    "payPeriodsPerYear": 26,
    "grossPerCheck": 3269.23,
    "federal": 343.65,
    "state": 144.75,
    "socialSecurity": 202.69,
    "medicare": 47.4,
    "fica": 250.1,
    "retirement": 163.46,
    "netPerCheck": 2367.27,
    "estimatedAnnualNet": 61549
  }
}
```

**Pay stub**
Request:
```
POST /v1/business/pay-stub
{
  "employer": "Northwind Design LLC",
  "employee": "Maria Lopez",
  "periodStart": "2026-10-01",
  "periodEnd": "2026-10-15",
  "payDate": "2026-10-20",
  "payType": "hourly",
  "rate": "28.50",
  "hours": "80",
  "overtimeHours": "4",
  "fedPct": "12",
  "statePct": "4",
  "ssPct": "6.2",
  "medPct": "1.45",
  "health": "85"
}
```
Response (abridged):
```
{
  "tool": "Pay stub generator client and server side from freedailypro",
  "result": {
    "figures": {
      "regular": 2280,
      "overtime": 171,
      "gross": 2451,
      "totalDeductions": 664.66,
      "net": 1786.34,
      "regularHours": 80,
      "overtimeHours": 4
    },
    "document": "(title, sections and a suggested filename as JSON, not a PDF)"
  }
}
```

## Limits
- An estimator, not a payroll compliance engine.
- Not modelled: city and county taxes, employer-side taxes, and the payroll contributions of NY, NJ, HI, RI, WA and MA (the response says so in a note).
- The California SDI rate is flagged unverified in the response (dataStatus).
- The pay stub applies the percentages you send and returns JSON (figures and document sections), not a PDF.
- US figures use 2026 tables; UK 2026/27; India FY 2026-27. Every tax response carries taxYear, sources and a disclaimer.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Estimates for information, not tax or payroll advice. Check results against your payroll provider before you rely on them.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Finance

**Tags**
```text
paycheck calculator, take home pay, payroll tax, fica, salary after tax, self employment tax, pay stub, income tax calculator, state income tax, free paycheck api
```
**Endpoints (path and purpose)**
- `/v1/converters/paycheck`: per-check take-home pay from salary: 2026 federal tax, employee FICA, state tax for all 50 states and DC, 401k and section 125 deductions, California SDI
- `/v1/converters/us-income-tax`: US federal income tax by filing status, with FICA and state tax
- `/v1/converters/state-tax`: state income tax from a state schedule or a flat rate
- `/v1/converters/self-employment-tax`: self-employment tax with quarterly estimates
- `/v1/converters/uk-tax`: UK income tax and National Insurance 2026/27, with Scottish rates
- `/v1/converters/india-income-tax`: India income tax FY 2026-27, old and new regime
- `/v1/business/pay-stub`: pay stub with gross pay, deductions and net pay from hours, rate and the percentages you send

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/converters/paycheck`. Pre-filled New York example returns per-check federal, state, FICA and net.
```json
{
  "grossAnnual": 85000,
  "payPeriodsPerYear": 26,
  "filingStatus": "single",
  "state": "NY",
  "retirementPct": 5
}
```
**Logo and screenshot ideas**: A cheque stub with a scissors cut line, teal. Screenshot: request and response side by side, net per check highlighted.

**Tutorial and article titles**
- Take-home pay for a US salary in one request
- Compare take-home pay across states with a loop
- Estimate self-employment tax and quarterly payments

## B4. PDF forms (fill, parse, flatten)
Wave 1, slot 1 again (promotion starts Day 17)
Spec to import: `pdf-forms-api.openapi.json` (3 operations), served at https://freedailypro.com/api-specs/pdf-forms-api.openapi.json. MCP path on the same key: /mcp/pdf-forms. Suggested Rapid slug: `fill-pdf-forms-api`.

**Name**
```text
Fill PDF Forms API: Parse, Fill and Flatten
```
**Short description** (136 characters)
```text
Fill PDF forms by field name: read the fields of a fillable PDF, fill text, checkbox, dropdown and radio fields from JSON, then flatten.
```
**Long description** (paste as Markdown)
````markdown
Read the fields of a fillable PDF form, fill them from JSON by field name, and flatten the result so the values cannot be edited. For HR, legal, insurance and onboarding tools that fill the same forms over and over.

## What you can do
**Forms**
- `/v1/fillable-forms/parse`: list every field: name, type, current value, options, read-only, required, maximum length
- `/v1/fillable-forms/fill`: fill the fields you name (text, checkbox, dropdown, radio, option list) and return the PDF, or JSON with a per-field report
- `/v1/pdf/flatten`: turn form fields into fixed page content

## Examples
**List the fields**
Request:
```
POST /v1/fillable-forms/parse  (multipart/form-data)
file = form.pdf
```
Response (abridged, from the spec example):
```
{
  "fieldCount": 6,
  "fields": [
    {
      "name": "name",
      "kind": "text",
      "type": "text",
      "readOnly": false,
      "required": false,
      "value": "Jane Doe",
      "multiline": false
    },
    {
      "name": "email",
      "kind": "text",
      "type": "text",
      "readOnly": false,
      "required": false,
      "value": "",
      "multiline": false
    },
    {
      "name": "agree",
      "kind": "checkbox",
      "type": "checkbox",
      "readOnly": false,
      "required": false,
      "checked": false,
      "value": false
    },
    "..."
  ]
}
```

**Fill some fields**
Request:
```
POST /v1/fillable-forms/fill  (multipart/form-data)
file = form.pdf
values = {"name":"Jane Doe","plan":"Pro"}
checked = {"agree":true}
format = json
```
Response (structure from the spec; capture a real one before publishing):
```
200 application/json with fieldsSet, fieldsNotSet (with the reason for each), fieldsUntouched and the PDF as fileBase64.
Without format=json the answer is the filled PDF itself, and any field that could not be set is listed in the X-Fields-Not-Set response headers.
```

## Limits
- AcroForm fields only. XFA (dynamic) forms and PDFs with no fields return an empty list or 422.
- Text must be Latin-1 characters; other scripts are reported as not set.
- Push buttons and signature fields cannot be filled.
- Up to 20 MB per file.
- Only the fields you name change; a field is cleared only when you send null or an empty value on purpose.
- If none of the named fields can be set the call returns 422 with the report.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Not offered: creating forms or adding fields, signing, templates by URL.
- Very custom field fonts may look different in some viewers.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Tools

**Tags**
```text
pdf form fill, fillable pdf, acroform, flatten pdf, form field parser, pdf api, fill pdf from json, pdf forms
```
**Endpoints (path and purpose)**
- `/v1/fillable-forms/parse`: list every field: name, type, current value, options, read-only, required, maximum length
- `/v1/fillable-forms/fill`: fill the fields you name (text, checkbox, dropdown, radio, option list) and return the PDF, or JSON with a per-field report
- `/v1/pdf/flatten`: turn form fields into fixed page content

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Files up to 20 MB. Errors are not billed.
Pro: for apps in production. A larger monthly quota and the larger file limits, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota and the larger file limits, every endpoint included.
Mega: for high-volume use. The largest monthly quota and the larger file limits, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/fillable-forms/parse`. Host a sample fillable PDF on freedailypro.com and link it in the description so a visitor can try the call in one minute.
```json
{
  "file": "(a small fillable PDF)"
}
```
**Logo and screenshot ideas**: A single page with a ticked box and a pen, red. Screenshot: parse response next to the filled PDF.

**Tutorial and article titles**
- Fill a PDF form from JSON with Python
- List every field in a fillable PDF (and why a fill can skip some)
- Fill and flatten a PDF in Node.js

## B5. Mortgage and loan
Wave 1, slot 2 again (promotion starts Day 18)
Spec to import: `mortgage-loans-api.openapi.json` (8 operations)  [do NOT import the older mortgage-and-loan-api.openapi.json], served at https://freedailypro.com/api-specs/mortgage-loans-api.openapi.json. MCP path on the same key: /mcp/loans-mortgage. Suggested Rapid slug: `mortgage-and-loan-calculator-api`.

**Name**
```text
Mortgage and Loan Calculator API
```
**Short description** (147 characters)
```text
Mortgage calculator API: monthly payment with taxes, insurance and PMI, amortization schedule, refinance break-even, affordability and APR as JSON.
```
**Long description** (paste as Markdown)
````markdown
Mortgage and loan maths with the working shown, as JSON, for mortgage and real-estate sites, broker widgets, budgeting apps and AI agents: monthly payment with property tax, insurance, PMI and HOA, extra-payment savings, amortization schedules, refinance break-even, affordability, APR and interest.

## What you can do
**Mortgage**
- `/v1/converters/mortgage`: payment with taxes, insurance, PMI or FHA and VA fees, HOA, extra and biweekly payments, payoff date, yearly table, debt-to-income
- `/v1/converters/refinance`: monthly saving, simple and full-cost break-even month, net advantage by years kept
- `/v1/converters/affordability`: home price you can afford from income and debts, with the 28/36 guideline

**Loans and interest**
- `/v1/converters/loan`: loan payment with frequency, compounding, solve for amount, term or rate, fees and APR, deferred and zero-coupon loans
- `/v1/converters/amortization`: schedule with payment dates and step-by-step working
- `/v1/converters/loan-interest`: loan, simple and compound interest in one call
- `/v1/converters/compound-interest and /v1/converters/simple-interest`: interest earned or owed

## Examples
**Mortgage payment**
Request:
```
POST /v1/converters/mortgage
{
  "homePrice": 400000,
  "downPaymentPct": 20,
  "ratePct": 6.5,
  "years": 30,
  "propertyTaxPct": 1.1,
  "homeInsuranceAnnual": 1200
}
```
Response (abridged):
```
{
  "tool": "Mortgage calculator: payment with taxes, insurance, PMI and HOA, extra payments, biweekly and payoff date",
  "result": {
    "monthly": {
      "principalAndInterest": 2022.62,
      "propertyTax": 366.67,
      "homeInsurance": 100,
      "hoa": 0,
      "mortgageInsurance": 0,
      "mortgageInsuranceName": "PMI",
      "maintenanceAndOther": 0,
      "total": 2489.28,
      "totalAfterMortgageInsuranceEnds": 2489.28
    },
    "payoff": {
      "payments": 360,
      "years": 30,
      "totalInterest": 408142.36,
      "totalPaidToLender": 728142.36
    },
    "loanAmount": 320000
  }
}
```
Abridged. The request is the worked example from the spec; the real response also has a 15 against 30 year comparison and a biweekly plan.

**Amortization schedule**
Request:
```
POST /v1/converters/amortization
{
  "principal": 20000,
  "annualRatePct": 7,
  "months": 36,
  "firstPaymentDate": "2026-12-01"
}
```
Response (abridged):
```
{
  "tool": "Loan amortization schedule with optional payment dates and step-by-step working client and server side from freedailypro",
  "result": {
    "monthlyPayment": 617.54,
    "totalPaid": 22231.51,
    "totalInterest": 2231.51,
    "schedule": [
      {
        "month": 1,
        "payment": 617.54,
        "interest": 116.67,
        "principal": 500.88,
        "balance": 19499.12,
        "date": "2026-12-01"
      },
      {
        "month": 2,
        "payment": 617.54,
        "interest": 113.74,
        "principal": 503.8,
        "balance": 18995.33,
        "date": "2027-01-01"
      },
      {
        "month": 3,
        "payment": 617.54,
        "interest": 110.81,
        "principal": 506.74,
        "balance": 18488.59,
        "date": "2027-02-01"
      },
      "..."
    ]
  }
}
```

## Limits
- No live mortgage rates or lender quotes. Rate, taxes and insurance are your inputs.
- APR uses the actuarial method (Regulation Z, Appendix J); a lender's quoted APR can differ.
- Conventional PMI applies under 20 percent down and ends at 78 percent of the original value unless you set a rate.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Estimates for information, not financial advice.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Finance

**Tags**
```text
mortgage calculator, amortization schedule, loan calculator, refinance, home affordability, apr, pmi, compound interest, free mortgage api
```
**Endpoints (path and purpose)**
- `/v1/converters/mortgage`: payment with taxes, insurance, PMI or FHA and VA fees, HOA, extra and biweekly payments, payoff date, yearly table, debt-to-income
- `/v1/converters/refinance`: monthly saving, simple and full-cost break-even month, net advantage by years kept
- `/v1/converters/affordability`: home price you can afford from income and debts, with the 28/36 guideline
- `/v1/converters/loan`: loan payment with frequency, compounding, solve for amount, term or rate, fees and APR, deferred and zero-coupon loans
- `/v1/converters/amortization`: schedule with payment dates and step-by-step working
- `/v1/converters/loan-interest`: loan, simple and compound interest in one call
- `/v1/converters/compound-interest and /v1/converters/simple-interest`: interest earned or owed

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/converters/mortgage`. Use the worked example below (400000 home, 20 percent down, 6.5 percent, 30 years): it returns 2,022.62 principal and interest and 2,489.28 a month in total.
```json
{
  "homePrice": 400000,
  "downPaymentPct": 20,
  "ratePct": 6.5,
  "years": 30,
  "propertyTaxPct": 1.1,
  "homeInsuranceAnnual": 1200
}
```
**Logo and screenshot ideas**: A house outline over an amortization curve, navy. Screenshot: the monthly block of the mortgage response.

**Tutorial and article titles**
- Calculate a monthly mortgage payment with taxes, insurance and PMI via API
- Build an amortization table with payment dates in JavaScript
- Refinance break-even: is it worth it? An API walk-through

## B6. SEO meta tags
Wave 1, slot 3 again (promotion starts Day 19)
Spec to import: `seo-web-api.openapi.json` (6 operations), served at https://freedailypro.com/api-specs/seo-web-api.openapi.json. MCP path on the same key: /mcp/seo-web. Suggested Rapid slug: `seo-meta-tags-and-json-ld-generator-api`.

**Name**
```text
SEO Meta Tags and JSON-LD Generator API
```
**Short description** (142 characters)
```text
Generate meta tags, Open Graph and Twitter cards, schema.org JSON-LD, robots.txt and sitemap.xml as JSON. Works on text you send; no crawling.
```
**Long description** (paste as Markdown)
````markdown
Generate the markup and copy around a page as JSON, for site builders, CMS plugins, static-site build steps and AI agents: title and meta tags with Open Graph and Twitter cards, schema.org JSON-LD, robots.txt and sitemap.xml, plus keyword density, hashtags and social captions.

## What you can do
**Markup**
- `/v1/seo/meta-tags`: title, description, Open Graph and Twitter Card tags as HTML and as fields
- `/v1/seo/schema`: schema.org JSON-LD for an Article, FAQ page or Organization
- `/v1/seo/robots-sitemap`: robots.txt and sitemap.xml for a domain from a list of page paths

**Text helpers**
- `/v1/seo/keyword-density`: how often a keyword appears and its density
- `/v1/seo/hashtags`: hashtags from text or keywords
- `/v1/seo/caption-generator`: template-based social captions with hashtags

## Examples
**Meta tags**
Request:
```
POST /v1/seo/meta-tags
{
  "title": "Merge PDF files online",
  "description": "Combine several PDFs into one file in your browser. Nothing is uploaded.",
  "url": "https://www.freedailypro.com/merge-pdf",
  "siteName": "FreeDailyPro",
  "twitterCard": "summary_large_image"
}
```
Response (abridged):
```
{
  "tool": "Meta tag generator client and server side from freedailypro",
  "html": "<title>Merge PDF files online</title>\n<meta name=\"description\" content=\"Combine several PDFs into one file in your browser. Nothing is uploaded.\" />\n<meta property=\"og:url\" content=\"https://www.freedailypro.com/merge-pdf\" />\n<meta property=\"og:title\" content=\"Merge PDF files online\" />\n<meta propert...",
  "tags": {
    "title": "Merge PDF files online",
    "description": "Combine several PDFs into one file in your browser. Nothing is uploaded.",
    "og:url": "https://www.freedailypro.com/merge-pdf",
    "og:title": "Merge PDF files online",
    "og:description": "Combine several PDFs into one file in your browser. Nothing is uploaded.",
    "og:type": "website",
    "og:site_name": "FreeDailyPro",
    "twitter:card": "summary_large_image",
    "twitter:title": "Merge PDF files online",
    "twitter:description": "Combine several PDFs into one file in your browser. Nothing is uploaded."
  }
}
```

**Article JSON-LD**
Request:
```
POST /v1/seo/schema
{
  "type": "article",
  "data": {
    "headline": "How to brew pour-over coffee",
    "author": "Maria Lopez",
    "publisher": {
      "name": "Harbor Coffee Co.",
      "logo": "https://example.com/logo.png"
    },
    "datePublished": "2026-10-01",
    "dateModified": "2026-10-20",
    "image": "https://example.com/pour-over.jpg",
    "url": "https://example.com/pour-over"
  }
}
```
Response:
```
{
  "tool": "Schema generator",
  "result": {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "How to brew pour-over coffee",
    "author": {
      "@type": "Person",
      "name": "Maria Lopez"
    },
    "publisher": {
      "@type": "Organization",
      "name": "Harbor Coffee Co.",
      "logo": "https://example.com/logo.png"
    },
    "datePublished": "2026-10-01",
    "dateModified": "2026-10-20",
    "image": "https://example.com/pour-over.jpg",
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://example.com/pour-over"
    },
    "url": "https://example.com/pour-over"
  },
  "warnings": []
}
```

## Limits
- Works only on the text you send: it does not crawl a site, fetch a page, check rankings or return backlink data.
- JSON-LD types: Article, FAQ page and Organization. Required fields are checked and a missing one is a 400 naming the field.
- The JSON-LD is built, not validated against a rich-results test tool.
- Hashtags and captions are rule-based templates, not an AI model.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Nothing is invented: only what you send is put into the markup.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Tools

**Tags**
```text
meta tags generator, open graph, twitter card, json-ld, schema.org, robots.txt, sitemap, seo meta tags, keyword density, hashtag generator, free seo tools
```
**Endpoints (path and purpose)**
- `/v1/seo/meta-tags`: title, description, Open Graph and Twitter Card tags as HTML and as fields
- `/v1/seo/schema`: schema.org JSON-LD for an Article, FAQ page or Organization
- `/v1/seo/robots-sitemap`: robots.txt and sitemap.xml for a domain from a list of page paths
- `/v1/seo/keyword-density`: how often a keyword appears and its density
- `/v1/seo/hashtags`: hashtags from text or keywords
- `/v1/seo/caption-generator`: template-based social captions with hashtags

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/seo/meta-tags`. JSON in, ready-to-paste HTML out.
```json
{
  "title": "Merge PDF files online",
  "description": "Combine several PDFs into one file in your browser. Nothing is uploaded.",
  "url": "https://www.freedailypro.com/merge-pdf",
  "siteName": "FreeDailyPro",
  "twitterCard": "summary_large_image"
}
```
**Logo and screenshot ideas**: Angle brackets around a magnifier, purple. Screenshot: input fields beside the generated head block.

**Tutorial and article titles**
- Generate Open Graph and Twitter Card tags from one API call
- Add Article and FAQ JSON-LD to every blog post in a build step
- Build robots.txt and sitemap.xml for a static site

## B7. Fitness and health calculator
Wave 2, slot 1 (promotion starts Day 31)
Spec to import: `fitness-health-api.openapi.json` (7 operations), served at https://freedailypro.com/api-specs/fitness-health-api.openapi.json. MCP path on the same key: /mcp/fitness-health. Suggested Rapid slug: `bmi-calculator-api`.

**Name**
```text
BMI Calculator API: BMR, TDEE, Body Fat and Ideal Weight
```
**Short description** (135 characters)
```text
BMI calculator API with BMR, TDEE, body fat (US Navy), ideal weight, water intake and due date. WHO classes and cited formulas in JSON.
```
**Long description** (paste as Markdown)
````markdown
Health and fitness formulas as JSON with the working and citations shown, for fitness, nutrition and wellness apps, coaching tools and AI agents: BMI, body fat, BMR and TDEE, ideal weight, daily water intake and pregnancy due date.

## What you can do
**Body measures**
- `/v1/converters/bmi`: BMI, category, BMI Prime, Ponderal Index, WHO class, waist-to-height ratio and target weight, metric or imperial
- `/v1/converters/body-fat`: body fat percentage by the US Navy method
- `/v1/converters/ideal-weight`: ideal weight range from height and sex

**Energy and intake**
- `/v1/converters/bmr`: basal metabolic rate and daily calories
- `/v1/converters/tdee`: total daily energy with cut and bulk targets, optional macros and weekly calorie cycling
- `/v1/converters/water-intake`: daily water intake from body weight and activity

**Pregnancy**
- `/v1/converters/pregnancy-due-date`: due date and gestational age from the last menstrual period

## Examples
**BMI**
Request:
```
POST /v1/converters/bmi
{
  "weight": 70,
  "height": 175,
  "unit": "metric"
}
```
Response (abridged):
```
{
  "tool": "Bmi calculator client and server side from freedailypro",
  "result": {
    "bmi": 22.9,
    "category": "Normal",
    "bmiPrime": 0.91,
    "ponderalIndex": 13.1,
    "whoClass": "Normal range",
    "whoRange": "18.5 to 24.99",
    "healthyWeightRange": {
      "lowKg": 56.7,
      "highKg": 76.3
    }
  }
}
```
Abridged: the real response also carries a steps array that shows the working.

**Daily calories**
Request:
```
POST /v1/converters/tdee
{
  "sex": "female",
  "age": 32,
  "weightKg": 62,
  "heightCm": 168,
  "activity": "light"
}
```
Response:
```
{
  "tool": "Calorie TDEE calculator client and server side from freedailypro",
  "result": {
    "bmr": 1349,
    "tdee": 1855,
    "cut": 1355,
    "bulk": 2155
  }
}
```

## Limits
- BMR and TDEE use the Mifflin-St Jeor equation; the due date uses Naegele's rule.
- Ideal weight and water intake are the simplest endpoints (two formulas; one activity-based estimate).
- There is no food database and no calories-burned lookup.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- General information, not medical advice.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Health and Fitness

**Tags**
```text
bmi calculator, bmr, tdee, body fat, ideal weight, water intake, due date calculator, calorie calculator, macros, free health api
```
**Endpoints (path and purpose)**
- `/v1/converters/bmi`: BMI, category, BMI Prime, Ponderal Index, WHO class, waist-to-height ratio and target weight, metric or imperial
- `/v1/converters/body-fat`: body fat percentage by the US Navy method
- `/v1/converters/ideal-weight`: ideal weight range from height and sex
- `/v1/converters/bmr`: basal metabolic rate and daily calories
- `/v1/converters/tdee`: total daily energy with cut and bulk targets, optional macros and weekly calorie cycling
- `/v1/converters/water-intake`: daily water intake from body weight and activity
- `/v1/converters/pregnancy-due-date`: due date and gestational age from the last menstrual period

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/converters/bmi`. Pre-filled metric example.
```json
{
  "weight": 70,
  "height": 175,
  "unit": "metric"
}
```
**Logo and screenshot ideas**: A tape measure curled into a heart, coral. Screenshot: BMI response with WHO class and healthy weight range.

**Tutorial and article titles**
- Calculate BMI with WHO classes in one request
- TDEE and calorie targets for cutting or bulking via API
- Estimate body fat with the US Navy method from tape measurements

## B8. Time zone and date calculator
Wave 2, slot 2 (promotion starts Day 32). GATE: capture a real IANA example first.
Spec to import: `time-zone-dates-api.openapi.json` (6 operations), served at https://freedailypro.com/api-specs/time-zone-dates-api.openapi.json. MCP path on the same key: /mcp/time-dates. Suggested Rapid slug: `time-zone-converter-api`.

**Name**
```text
Time Zone Converter API: DST, Unix Timestamp and Date Calculator
```
**Short description** (131 characters)
```text
Time zone converter API with daylight saving, working-hours overlap, Unix timestamps, age, countdown and cron descriptions as JSON.
```
**Long description** (paste as Markdown)
````markdown
Time zone and date maths as JSON for scheduling apps, distributed teams, logging tools and AI agents: convert a moment between IANA time zones with daylight saving, convert Unix timestamps and ISO dates, calculate age and the span between dates, count down to a date, and explain cron expressions.

## What you can do
**Time zones**
- `/v1/converters/timezone-offset`: convert between IANA zones (or apply a fixed offset); flags times that do not exist or happen twice; optional next clock change and shared working hours

**Dates and timestamps**
- `/v1/security/timestamp`: Unix seconds, milliseconds, ISO and UTC text
- `/v1/converters/age`: age or span in years, months and days
- `/v1/converters/countdown`: days, hours and minutes until or since a date
- `/v1/converters/job-experience`: years and months between two dates, added across jobs

**Cron**
- `/v1/security/cron`: explain and validate a cron expression in plain words

## Examples
**Fixed-offset conversion**
Request:
```
POST /v1/converters/timezone-offset
{
  "utcIso": "2026-10-30T12:00:00Z",
  "offset": "+05:30"
}
```
Response:
```
{
  "tool": "Timezone converter client and server side from freedailypro",
  "utc": "2026-10-30T12:00:00.000Z",
  "offset": "+05:30",
  "localIso": "2026-10-30T17:30:00",
  "localUnixMs": 1793381400000
}
```

**IANA zones with working hours (request from the spec text; the real response is not captured yet)**
Request:
```
POST /v1/converters/timezone-offset
{
  "localTime": "2026-11-01T01:30",
  "fromZone": "America/New_York",
  "toZones": [
    "Europe/London",
    "Asia/Kolkata"
  ],
  "nextChange": true
}
```
Response (shape from the spec):
```
Each zone in 'conversions' has zone, name, display, offset, offsetMinutes and localIso; a gap or repeated hour is flagged with kind and a note.
CAPTURE THE REAL RESPONSE with capture-openapi-responses.mjs and paste it here before publishing.
```

## Limits
- Takes IANA zone names or fixed offsets only: no lookup by city name, IP address or coordinates, and no list-zones endpoint.
- A fixed offset ignores daylight saving; send IANA zones for real places.
- Daylight saving comes from the platform time zone database.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Thin field: lead with the daylight-saving and working-hours features, not the plain conversion.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Tools

**Tags**
```text
timezone converter, unix timestamp, date calculator, dst, countdown, age calculator, cron expression, working hours overlap
```
**Endpoints (path and purpose)**
- `/v1/converters/timezone-offset`: convert between IANA zones (or apply a fixed offset); flags times that do not exist or happen twice; optional next clock change and shared working hours
- `/v1/security/timestamp`: Unix seconds, milliseconds, ISO and UTC text
- `/v1/converters/age`: age or span in years, months and days
- `/v1/converters/countdown`: days, hours and minutes until or since a date
- `/v1/converters/job-experience`: years and months between two dates, added across jobs
- `/v1/security/cron`: explain and validate a cron expression in plain words

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/converters/timezone-offset`. The minimal fixed-offset call is the only captured example today. Replace it with an IANA example once captured.
```json
{
  "utcIso": "2026-10-30T12:00:00Z",
  "offset": "+05:30"
}
```
**Logo and screenshot ideas**: Two clock faces joined by an arrow, slate blue. Screenshot: a conversion with a flagged daylight-saving gap.

**Tutorial and article titles**
- Convert a meeting time across zones with daylight saving
- Find shared working hours for a distributed team
- Convert Unix timestamps and ISO dates in code

## B9. Currency and VAT
Wave 2, slot 3 (promotion starts Day 33). GATE: one real vat-validate and one real exchange-rates call.
Spec to import: `currency-vat-api.openapi.json` (6 operations), served at https://freedailypro.com/api-specs/currency-vat-api.openapi.json. MCP path on the same key: /mcp/currency-vat. Suggested Rapid slug: `vat-number-validation-and-currency-api`.

**Name**
```text
VAT Number Validation, VAT Rates and Currency API
```
**Short description** (146 characters)
```text
Validate EU VAT numbers (VIES), look up VAT and GST rates, add or extract VAT, convert about 200 currencies with daily reference rates (not live).
```
**Long description** (paste as Markdown)
````markdown
Tax rates and currency conversion as JSON for invoicing, e-commerce and accounting tools: validate EU VAT numbers (layout check plus a VIES lookup), look up VAT and GST rates by country, add or extract VAT or GST on an amount, calculate US sales tax, and convert between about 200 currencies, crypto assets and metals with daily reference rates.

## What you can do
**VAT and sales tax**
- `/v1/converters/vat-validate`: layout check per member state plus a VIES lookup for registered name and address
- `/v1/converters/vat-rates`: standard and reduced VAT and GST rates for more than 50 countries and regions, with a data version and verification note per country
- `/v1/converters/vat-gst`: add or extract VAT or GST on an amount
- `/v1/converters/sales-tax`: US sales tax from a state base-rate table

**Currency**
- `/v1/converters/exchange-rates`: daily reference rates for about 200 currencies, crypto and metals, with the as-of date and source; history ranges for about 30 currencies
- `/v1/converters/currency`: simple conversion between 12 major currencies from a fixed reference table

## Examples
**Exchange rates**
Request:
```
POST /v1/converters/exchange-rates
{
  "amount": 100,
  "from": "USD",
  "to": [
    "EUR",
    "GBP"
  ]
}
```
Response (abridged):
```
{
  "tool": "Exchange rates: daily reference rates for about 200 currencies, crypto and metals, with ECB fallback and ECB history (reference rates, not live)",
  "result": {
    "source": "currency-api by fawazahmed0: community-compiled daily rates for about 200 currencies, crypto and metals (CC0 1.0), served from the jsDelivr CDN",
    "sourceId": "currency-api",
    "note": "Daily reference rates, not live trading rates: they refresh about once a day, can differ from what a bank, card network or exchange charges, and for crypto and metals are not tradable prices. Do not use them for trading or settlement.",
    "live": false,
    "from": "USD",
    "amount": 100,
    "date": "2026-10-31",
    "stale": false,
    "rates": {
      "EUR": 0.86,
      "GBP": 0.75
    },
    "converted": {
      "EUR": 86,
      "GBP": 75
    }
  }
}
```
The request shown is the one the spec example response answers (an amount of 100, from USD, to EUR and GBP).

**VAT number validation (illustrative: capture a real one before publishing)**
Request:
```
POST /v1/converters/vat-validate
{
  "vatNumber": "DE123456789"
}
```
Response (the spec example uses a made-up company; replace with a real captured answer):
```
{
  "tool": "EU VAT number validation: layout check per member state plus a live VIES lookup",
  "result": {
    "vatNumber": "DE123456789",
    "country": "DE",
    "countryName": "Germany",
    "formatValid": true,
    "valid": true,
    "checked": "vies",
    "name": "EXAMPLE GMBH",
    "address": "MUSTERSTRASSE 1, 10115 BERLIN",
    "requestDate": "2026-11-01",
    "note": "valid true means the number is registered for intra-EU trade in VIES at the request date. Some member states return no name or address."
  }
}
```

## Limits
- Rates are daily reference rates, refreshed about once a day: not live, not intraday, and they can differ from what a bank or card network charges. Do not use them for trading, settlement or accounting. The response says live: false.
- Crypto and metal values are not tradable prices. History ranges (up to 366 days and 5 currencies) come from the European Central Bank set only, about 30 currencies.
- A good VAT number layout does not prove registration; only VIES does. UK (GB) numbers are no longer in VIES.
- VIES is often down for single member states: the endpoint then returns 503 with a plain message, which is not billed.
- VAT rate tables carry a data version and a verification note per country.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- VAT validation confirms a number exists, not that a business is trustworthy.
- Results of VIES lookups are cached in memory for 10 minutes; nothing is stored.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Finance

**Tags**
```text
vat validation, vies, vat number check, vat calculator, gst calculator, vat rates, currency converter, exchange rates, sales tax, free currency api
```
**Endpoints (path and purpose)**
- `/v1/converters/vat-validate`: layout check per member state plus a VIES lookup for registered name and address
- `/v1/converters/vat-rates`: standard and reduced VAT and GST rates for more than 50 countries and regions, with a data version and verification note per country
- `/v1/converters/vat-gst`: add or extract VAT or GST on an amount
- `/v1/converters/sales-tax`: US sales tax from a state base-rate table
- `/v1/converters/exchange-rates`: daily reference rates for about 200 currencies, crypto and metals, with the as-of date and source; history ranges for about 30 currencies
- `/v1/converters/currency`: simple conversion between 12 major currencies from a fixed reference table

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/converters/vat-validate`. Pin only after a real VIES call has been checked.
```json
{
  "vatNumber": "DE123456789"
}
```
**Logo and screenshot ideas**: A tax tag with a tick mark, green. Screenshot: a vat-validate response with the registered name and address.

**Tutorial and article titles**
- Validate an EU VAT number before issuing an invoice
- Add or extract VAT for any country with one call
- Convert amounts with daily reference rates and show the as-of date

## B10. Unit converter
Wave 3, slot 1 (promotion starts Day 45)
Spec to import: `unit-converter-api.openapi.json` (8 operations), served at https://freedailypro.com/api-specs/unit-converter-api.openapi.json. MCP path on the same key: /mcp/units. Suggested Rapid slug: `unit-converter-api`.

**Name**
```text
Unit Converter API: 14 Categories, Length, Weight, Volume, Temperature
```
**Short description** (143 characters)
```text
Unit converter API for 14 categories (length, weight, volume, temperature, pressure, energy, speed and more) with exact cited factors, as JSON.
```
**Long description** (paste as Markdown)
````markdown
Convert between more than 100 units in 14 categories with exact, cited factors, as JSON, for e-commerce, recipe, engineering and logistics apps and AI agents. Also converts file sizes, Roman numerals and scales recipes.

## What you can do
**Convert**
- `/v1/converters/units`: length, weight, temperature, volume, area, speed, pressure, energy, power, time, data transfer, angle, fuel economy and cooking
- `/v1/converters/units-list`: every unit id, symbol, alias and a US, imperial or metric tag
- `/v1/converters/file-size`: bytes to petabytes

**Older single-purpose endpoints**
- `/v1/converters/length, /v1/converters/weight, /v1/converters/temperature`: return a bare number
- `/v1/converters/roman`: numbers to and from Roman numerals, with bars above 3,999
- `/v1/converters/recipe-scale`: scale ingredient amounts to a new serving count

## Examples
**Gallons to litres**
Request:
```
POST /v1/converters/units
{
  "category": "volume",
  "value": 2,
  "from": "gal_us",
  "to": "l"
}
```
Response (abridged):
```
{
  "tool": "Unit converter: 14 categories and over 130 units with exact factors",
  "result": {
    "category": "volume",
    "value": 2,
    "from": "gal_us",
    "fromName": "US gallon",
    "to": "l",
    "toName": "Litre",
    "result": 7.570823568,
    "factor": 3.785411784,
    "note": "US customary and imperial (UK) units share names but not sizes (US gallon 3.785411784 L, imperial gallon 4.54609 L); the unit id says which one was used."
  }
}
```

**Recipe scaling**
Request:
```
POST /v1/converters/recipe-scale
{
  "ingredients": [
    {
      "name": "flour",
      "amount": 250,
      "unit": "g"
    },
    {
      "name": "eggs",
      "amount": 2
    },
    {
      "name": "milk",
      "amount": 300,
      "unit": "ml"
    }
  ],
  "originalServings": 4,
  "targetServings": 10
}
```
Response:
```
{
  "tool": "Recipe scaler client and server side from freedailypro",
  "result": [
    {
      "name": "flour",
      "amount": 625,
      "unit": "g",
      "originalAmount": 250
    },
    {
      "name": "eggs",
      "amount": 5,
      "originalAmount": 2
    },
    {
      "name": "milk",
      "amount": 750,
      "unit": "ml",
      "originalAmount": 300
    }
  ]
}
```

## Limits
- Fixed unit tables, not a full measurement library: no Mach, no ingredient-specific cups to grams, no currency.
- US customary and imperial units share names but not sizes: the unit id says which is used (gal_us, gal_imp).
- Month and year are calendar averages.
- The newer units endpoint returns an object; the older length, weight and temperature endpoints return a bare number.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Factors are exact international definitions and each is cited in the response source.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Tools

**Tags**
```text
unit converter, length converter, weight converter, temperature converter, volume converter, cooking measures, roman numerals, file size converter, recipe scaler, free unit api
```
**Endpoints (path and purpose)**
- `/v1/converters/units`: length, weight, temperature, volume, area, speed, pressure, energy, power, time, data transfer, angle, fuel economy and cooking
- `/v1/converters/units-list`: every unit id, symbol, alias and a US, imperial or metric tag
- `/v1/converters/file-size`: bytes to petabytes
- `/v1/converters/length, /v1/converters/weight, /v1/converters/temperature`: return a bare number
- `/v1/converters/roman`: numbers to and from Roman numerals, with bars above 3,999
- `/v1/converters/recipe-scale`: scale ingredient amounts to a new serving count

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Errors are not billed.
Pro: for apps in production. A larger monthly quota, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota, every endpoint included.
Mega: for high-volume use. The largest monthly quota, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/converters/units`. JSON in, instant answer with the exact factor.
```json
{
  "category": "volume",
  "value": 2,
  "from": "gal_us",
  "to": "l"
}
```
**Logo and screenshot ideas**: A ruler crossing a measuring jug, mustard. Screenshot: the gallon to litre response with its US against imperial note.

**Tutorial and article titles**
- Convert US and imperial units without getting gallons wrong
- Convert file sizes and data rates in code
- Scale a recipe to any number of servings

## B11. Bookkeeping (text-PDF bank statements)
Wave 3, slot 2 (promotion starts Day 46). GATE: test several real bank PDFs first.
Spec to import: `bookkeeping-api.openapi.json` (3 operations), served at https://freedailypro.com/api-specs/bookkeeping-api.openapi.json. MCP path on the same key: /mcp/bookkeeping. Suggested Rapid slug: `bank-statement-to-csv-api`.

**Name**
```text
Bank Statement to CSV API: Text PDF to Transactions
```
**Short description** (145 characters)
```text
Bank statement to CSV API: turn text-based PDFs or pasted statement text into dated transactions, CSV and a balance check. No OCR; scans refused.
```
**Long description** (paste as Markdown)
````markdown
Turn a text-based bank or card statement PDF, or pasted statement text, into dated transactions, a CSV and a balance reconciliation, for bookkeeping, budgeting and accounting tools. Also totals expenses by category and month and totals a monthly budget.

## What you can do
**Statements**
- `/v1/business/bank-statement-to-csv`: text-based PDF (multipart file or fileBase64) or pasted text to transactions, CSV, opening and closing balances and a reconciliation; optional rule-based categories

**Totals**
- `/v1/business/expenses`: expense totals by category, month and share, with a CSV
- `/v1/planning/monthly-budget`: total a monthly budget into spending, savings rate and money remaining

## Examples
**Pasted statement text**
Request:
```
POST /v1/business/bank-statement-to-csv
{
  "text": "Date Description Amount Balance\n10/01 Opening balance 2,500.00\n10/03 GROCERY MART #14 -62.18 2,437.82\n10/05 PAYROLL ACME INC 1,950.00 4,387.82\n10/09 CITY POWER -118.40 4,269.42",
  "year": 2026,
  "dateOrder": "mdy",
  "numberFormat": "us"
}
```
Response:
```
{
  "tool": "Bank statement to CSV client and server side from freedailypro",
  "result": {
    "transactions": [
      {
        "date": "2026-10-03",
        "description": "GROCERY MART #14",
        "amount": -62.18,
        "balance": 2437.82,
        "signGuess": false
      },
      {
        "date": "2026-10-05",
        "description": "PAYROLL ACME INC",
        "amount": 1950,
        "balance": 4387.82,
        "signGuess": false
      },
      {
        "date": "2026-10-09",
        "description": "CITY POWER",
        "amount": -118.4,
        "balance": 4269.42,
        "signGuess": false
      }
    ],
    "openingBalance": 2500,
    "closingBalance": null,
    "dateOrder": "mdy",
    "numberFormat": "us",
    "cardLayout": false,
    "skippedLines": [],
    "reconciliation": {
      "basis": "balances",
      "ok": true,
      "total": 1769.42,
      "mismatchedRows": [],
      "difference": null,
      "message": "All 3 running balances follow from the rows."
    },
    "csv": "Date,Description,Amount,Balance\n2026-10-03,GROCERY MART #14,-62.18,2437.82\n2026-10-05,PAYROLL ACME INC,1950,4387.82\n2026-10-09,CITY POWER,-118.4,4269.42"
  }
}
```

**Expense totals**
Request:
```
POST /v1/business/expenses
{
  "items": [
    {
      "category": "Software",
      "amount": 129,
      "date": "2026-09-02"
    },
    {
      "category": "Travel",
      "amount": 480.5,
      "date": "2026-10-11"
    },
    {
      "category": "Software",
      "amount": 49,
      "date": "2026-10-20"
    }
  ]
}
```
Response:
```
{
  "tool": "Expense tracker client and server side from freedailypro",
  "result": {
    "total": 658.5,
    "byCategory": {
      "Software": 178,
      "Travel": 480.5
    },
    "count": 3,
    "categories": [
      {
        "category": "Travel",
        "total": 480.5,
        "count": 1,
        "sharePct": 72.97
      },
      {
        "category": "Software",
        "total": 178,
        "count": 2,
        "sharePct": 27.03
      }
    ],
    "csv": "Category,Count,Total,Share %\nTravel,1,480.50,72.97\nSoftware,2,178.00,27.03"
  }
}
```

## Limits
- PDFs must contain real text. Scans and photos are refused with 422 because OCR is not supported. Password-protected PDFs are refused.
- Up to 20 MB and 100 pages per PDF.
- Bank layouts differ a lot: check the reconciliation in the response. Tested against generated statement PDFs only so far.
- Categories are generic keywords plus your own rules, not a merchant database; unmatched rows are Uncategorized.
- No receipts, invoices or images, and no ledger or accounting-system reconciliation.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Date order and number format (US 1,234.56 or European 1.234,56) are detected or can be set.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Finance

**Tags**
```text
bank statement to csv, statement parser, transactions csv, bank statement pdf, expense categories, monthly budget
```
**Endpoints (path and purpose)**
- `/v1/business/bank-statement-to-csv`: text-based PDF (multipart file or fileBase64) or pasted text to transactions, CSV, opening and closing balances and a reconciliation; optional rule-based categories
- `/v1/business/expenses`: expense totals by category, month and share, with a CSV
- `/v1/planning/monthly-budget`: total a monthly budget into spending, savings rate and money remaining

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. PDFs up to 20 MB and 100 pages. Errors are not billed.
Pro: for apps in production. A larger monthly quota and the larger file limits, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota and the larger file limits, every endpoint included.
Mega: for high-volume use. The largest monthly quota and the larger file limits, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/business/bank-statement-to-csv`. Pasted text body: no file upload needed for the first call.
```json
{
  "text": "Date Description Amount Balance\n10/01 Opening balance 2,500.00\n10/03 GROCERY MART #14 -62.18 2,437.82\n10/05 PAYROLL ACME INC 1,950.00 4,387.82\n10/09 CITY POWER -118.40 4,269.42",
  "year": 2026,
  "dateOrder": "mdy",
  "numberFormat": "us"
}
```
**Logo and screenshot ideas**: A statement page turning into a table grid, forest green. Screenshot: pasted text beside the transactions table and the reconciliation message.

**Tutorial and article titles**
- Turn a text-based bank statement PDF into CSV
- Categorize transactions with your own rules
- Check a statement against its printed balances

## B12. Image (resize fit modes, compress, watermark)
Wave 3, slot 3 (promotion starts Day 47)
Spec to import: `image-api.openapi.json` (7 operations), served at https://freedailypro.com/api-specs/image-api.openapi.json. MCP path on the same key: /mcp/image. Suggested Rapid slug: `image-resize-and-compress-api`.

**Name**
```text
Image Resize and Compress API: WebP, AVIF, PNG, JPEG, Watermark
```
**Short description** (136 characters)
```text
Resize images with fit modes, compress, convert to WebP or AVIF, crop, rotate, flip and watermark with one upload. Files are not stored.
```
**Long description** (paste as Markdown)
````markdown
Resize, convert, compress, crop, rotate, flip and watermark images with one upload per call, for apps that handle user uploads and need web-ready pictures without running their own image software.

## What you can do
**Image jobs**
- `/v1/image/resize`: width, height or both, with fit modes fill, contain, cover, inside and outside, and withoutEnlargement
- `/v1/image/compress`: quality setting, optional target format, metadata stripping, optional maximum size
- `/v1/image/convert`: PNG, JPEG, WebP, AVIF, GIF, TIFF, BMP or ICO with quality, background, grayscale, blur and sharpen
- `/v1/image/crop`: by pixels or fractions
- `/v1/image/rotate`: 90, 180 or 270 degrees
- `/v1/image/flip`: horizontal or vertical
- `/v1/image/watermark`: text or picture watermark with position, opacity, size, rotation and tiling

## Examples
**Resize with a fit mode**
Request:
```
POST /v1/image/resize  (multipart/form-data)
file = photo.jpg
width = 800
height = 600
fit = cover
```
Response:
```
200 image, same format as the input unless format is given.
X-Image-Width, X-Image-Height and X-Image-Frames headers describe the result.
```

**Compress and convert to WebP**
Request:
```
POST /v1/image/compress  (multipart/form-data)
file = photo.jpg
quality = 75
format = webp
```
Response:
```
200 image/webp: the smaller file.
X-Original-Bytes, X-Output-Bytes and X-Reduction-Percent report the saving. If the result cannot be made smaller, the original bytes come back unchanged and X-Compress-Note says so.
```

## Limits
- Up to 15 MB per file; 10 MB on Basic.
- Reads JPEG, PNG, WebP, AVIF, GIF, TIFF, SVG and BMP. HEIC and HEIF from phones are not supported.
- Rotation is in steps of 90 degrees. Watermark text is one line (Latin, Greek and Cyrillic letters).
- Animated GIF and WebP stay animated in convert, resize and compress; other endpoints use the first frame.
- Upload only: no URL input. No smart crop, face detection or background removal. The saving depends on the picture; an already optimised file may not shrink.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- Output size and look were checked on generated test pictures only; test on your own images.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Video, Images

**Tags**
```text
image resize, image compress, webp, avif, image converter, watermark, crop image, png to webp, free image api
```
**Endpoints (path and purpose)**
- `/v1/image/resize`: width, height or both, with fit modes fill, contain, cover, inside and outside, and withoutEnlargement
- `/v1/image/compress`: quality setting, optional target format, metadata stripping, optional maximum size
- `/v1/image/convert`: PNG, JPEG, WebP, AVIF, GIF, TIFF, BMP or ICO with quality, background, grayscale, blur and sharpen
- `/v1/image/crop`: by pixels or fractions
- `/v1/image/rotate`: 90, 180 or 270 degrees
- `/v1/image/flip`: horizontal or vertical
- `/v1/image/watermark`: text or picture watermark with position, opacity, size, rotation and tiling

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Images up to 10 MB. Errors are not billed.
Pro: for apps in production. A larger monthly quota and the larger file limits, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota and the larger file limits, every endpoint included.
Mega: for high-volume use. The largest monthly quota and the larger file limits, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/image/resize`. Small input, one file, fast.
```json
{
  "file": "(a small PNG)",
  "width": 320,
  "height": 240,
  "fit": "cover"
}
```
**Logo and screenshot ideas**: A picture frame with corner handles and a compress arrow, cyan. Screenshot: one photo at three fit modes.

**Tutorial and article titles**
- Resize images to exact sizes with cover, contain and inside
- Convert PNG and JPEG to WebP and AVIF in one request
- Add a text or logo watermark to images in code

## B13. Audio
Wave 4, slot 1 (promotion starts Day 59)
Spec to import: `audio-api.openapi.json` (9 operations), served at https://freedailypro.com/api-specs/audio-api.openapi.json. MCP path on the same key: /mcp/audio. Suggested Rapid slug: `audio-converter-api`.

**Name**
```text
Audio Converter API: Trim, Merge, Normalize, Denoise and Compress
```
**Short description** (141 characters)
```text
Convert audio to MP3, WAV, OGG, M4A or FLAC; trim, merge, compress, normalize, denoise, change speed or pitch and remove silence. Not stored.
```
**Long description** (paste as Markdown)
````markdown
Process audio files with one upload per call, for apps that handle user recordings, podcasts and voice notes: convert formats, trim, merge, compress, normalize loudness, change speed or pitch, reduce noise and remove silence.

## What you can do
**Audio jobs**
- `/v1/audio/convert`: MP3, WAV, OGG, M4A or FLAC
- `/v1/audio/compress`: smaller MP3, about half the size or a target file size
- `/v1/audio/normalize`: bring the file to one target loudness (default -16 LUFS)
- `/v1/audio/denoise`: reduce background noise
- `/v1/audio/remove-silence`: cut silent gaps
- `/v1/audio/trim and /v1/audio/merge`: cut a clip, join several files
- `/v1/audio/speed and /v1/audio/pitch`: speed 0.5x to 2x, pitch in semitones

## Examples
**Convert to MP3**
Request:
```
POST /v1/audio/convert  (multipart/form-data)
file = voice.wav
format = mp3
```
Response:
```
200 audio/mpeg: the converted file
```

**Normalize loudness**
Request:
```
POST /v1/audio/normalize  (multipart/form-data)
file = clip.mp3
targetLufs = -16
```
Response:
```
200 audio/mpeg: the file brought to one target loudness (EBU R128 integrated loudness, default -16 LUFS)
```

## Limits
- Basic plan: 25 MB and 60 seconds per request. Paid plans: up to 30 MB per file. Over the limit returns 413 or 422 and is not billed.
- Files are processed with ffmpeg on a shared server; a busy service can answer 503 with Retry-After.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- No transcription, text to speech or stem separation. Not a speech API.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Media (Video, Images is the alternative)

**Tags**
```text
audio converter, mp3 converter, wav to mp3, normalize audio, remove silence, trim audio, denoise audio, audio compressor
```
**Endpoints (path and purpose)**
- `/v1/audio/convert`: MP3, WAV, OGG, M4A or FLAC
- `/v1/audio/compress`: smaller MP3, about half the size or a target file size
- `/v1/audio/normalize`: bring the file to one target loudness (default -16 LUFS)
- `/v1/audio/denoise`: reduce background noise
- `/v1/audio/remove-silence`: cut silent gaps
- `/v1/audio/trim and /v1/audio/merge`: cut a clip, join several files
- `/v1/audio/speed and /v1/audio/pitch`: speed 0.5x to 2x, pitch in semitones

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Audio up to 25 MB and 60 seconds. Errors are not billed.
Pro: for apps in production. A larger monthly quota and the larger file limits, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota and the larger file limits, every endpoint included.
Mega: for high-volume use. The largest monthly quota and the larger file limits, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/audio/trim`. Keep the sample tiny: media calls are the slowest.
```json
{
  "file": "(a clip of a few seconds)",
  "startSeconds": 0,
  "endSeconds": 5
}
```
**Logo and screenshot ideas**: A waveform with a scissor mark, magenta. Screenshot: a waveform before and after silence removal.

**Tutorial and article titles**
- Convert WAV to MP3 and shrink it to a target size
- Normalize loudness across a batch of podcast clips
- Cut silent gaps out of a recording in code

## B14. Video
Wave 4, slot 2 (promotion starts Day 60). GATE: timeout and Retry-After behaviour confirmed under load.
Spec to import: `video-api.openapi.json` (8 operations), served at https://freedailypro.com/api-specs/video-api.openapi.json. MCP path on the same key: /mcp/video. Suggested Rapid slug: `video-compress-and-convert-api`.

**Name**
```text
Video Compress and Convert API: MP4, WebM, GIF, Thumbnail
```
**Short description** (131 characters)
```text
Compress video, convert to MP4 or WebM, make GIFs, grab thumbnails, trim, merge, burn in subtitles and extract MP3 with one upload.
```
**Long description** (paste as Markdown)
````markdown
Process video files with one upload per call, for apps that handle user uploads: compress, convert, trim, merge, burn in subtitles, grab a thumbnail, extract the audio and make GIFs.

## What you can do
**Video jobs**
- `/v1/video/compress`: re-encode to a target size; headers report how close it got
- `/v1/video/convert`: MP4, WebM or MOV
- `/v1/video/to-gif`: short clip to animated GIF (about 1.9 MB at most; longer or larger clips are made smaller)
- `/v1/video/thumbnail`: JPEG still at a given time
- `/v1/video/extract-audio`: MP3 track
- `/v1/video/trim and /v1/video/merge`: cut a clip, join clips
- `/v1/video/subtitle`: burn in SRT subtitles

## Examples
**Thumbnail**
Request:
```
POST /v1/video/thumbnail  (multipart/form-data)
file = clip.mp4
atSeconds = 2
```
Response:
```
200 image/jpeg: the frame at the given time
```

**Compress to a target size**
Request:
```
POST /v1/video/compress  (multipart/form-data)
file = clip.mp4
targetFileSize = 0.5
```
Response (headers from the spec):
```
200 video/mp4: the smaller file.
X-Met-Target, X-Output-Size and X-Target-Size headers report how close it got.
```

## Limits
- Basic plan: 25 MB and 60 seconds in total. Over the size returns 413, over the length 422; neither is billed. Paid plans: up to 100 MB per file.
- Upload only: no URL input and no job queue. Long clips run inside the request, so keep uploads small (under 50 MB) for fast results; a busy service answers 503 with Retry-After.

## Errors
Errors are not billed. Invalid input returns 400 or 422 with a plain JSON reason, a missing key returns 401 and a plan limit returns 429; none of these is counted by our usage meter.

## Privacy
We do not store your data. Each request is processed in memory and discarded.

## Notes
- No downloading from video sites.
- Heaviest compute of the set: ship last and watch service level.

Also usable by AI agents over MCP with the same key.
Part of FreeDailyPro. Developer page: https://www.freedailypro.com/developers
````
**Category**: Video, Images

**Tags**
```text
video compress, video converter, mp4 to gif, video thumbnail, extract audio, trim video, burn subtitles, webm
```
**Endpoints (path and purpose)**
- `/v1/video/compress`: re-encode to a target size; headers report how close it got
- `/v1/video/convert`: MP4, WebM or MOV
- `/v1/video/to-gif`: short clip to animated GIF (about 1.9 MB at most; longer or larger clips are made smaller)
- `/v1/video/thumbnail`: JPEG still at a given time
- `/v1/video/extract-audio`: MP3 track
- `/v1/video/trim and /v1/video/merge`: cut a clip, join clips
- `/v1/video/subtitle`: burn in SRT subtitles

**Plan wording**
```text
Basic: build and test a real app. Every endpoint is included, with the monthly quota and per-minute rate limit shown on this plan. Video up to 25 MB and 60 seconds. Errors are not billed.
Pro: for apps in production. A larger monthly quota and the larger file limits, every endpoint included.
Ultra: for busy apps and AI agents. A much larger monthly quota and the larger file limits, every endpoint included.
Mega: for high-volume use. The largest monthly quota and the larger file limits, every endpoint included.
```
**Try-it endpoint to pin first**: `POST /v1/video/thumbnail`. Small input and a quick answer. Do not pin compress first.
```json
{
  "file": "(a clip of a few seconds, under 5 MB)",
  "atSeconds": 1
}
```
**Logo and screenshot ideas**: A film frame with a down-arrow, indigo. Screenshot: a clip, its GIF and its thumbnail.

**Tutorial and article titles**
- Compress a video to a target size with one request
- Make an animated GIF from a video clip in code
- Burn SRT subtitles into a video

---
# Part C: 30-day activity checklist per wave

Who: Grok = the Grok bots (Studio edits with the owner, tutorials, dev.to posts, Postman collections, discussion replies; Claude gives instructions only for dev.to). Owner = Santosh (Studio logins and payout details, logos, Railway variable, decisions). Claude = code and checks (capture real responses, host sample files, verify specs, write instructions). Day numbers are relative to the wave's own Day 0 (the day its first listing is published); Part D maps them to calendar dates.
Standing rules for every wave: never create fake users or fake ratings (ask only real early users for a rating); keep test calls tiny so the service-level figure stays high; answer every discussion post within 24 hours; no code-hosting links anywhere; the word free only in tags.

## Wave 0: the six live listings (Part A)
| When | Task | Who |
|---|---|---|
| Day 1 | Edit A1 (calculators) and A2 (PDF): name, short, long, category, tags, plan wording, Try-it order; re-import the spec; hide the Basic (Deprecated) plan; upload a distinct logo | Grok, owner |
| Day 2 | Edit A4 (business documents) and A5 (media); fix the A5 name mismatch and category | Grok, owner |
| Day 3 | Edit A3 (developer utilities) and A6 (book publishing) | Grok, owner |
| Day 3 | Check the Studio project FreeDailyPro Public APIs is not public; check Community tab for the single subscriber (very likely the owner's own test subscription) | Owner |
| Day 7 | Upload tutorials for A1 and A2; check the six listings still return 200 on the Try-it endpoint | Grok, Claude |
| Day 30 | Read analytics for all six; the umbrellas are edited, not promoted | Owner |

## Wave 1: PPTX generator, 401k and retirement, paycheck (Days 3 to 18), then PDF forms, mortgage and loan, SEO meta tags (Days 17 to 32)
Listings: B1 PPTX generator; B2 401k and retirement calculator; B3 Paycheck and payroll tax; B4 PDF forms (fill, parse, flatten); B5 Mortgage and loan; B6 SEO meta tags.

| When | Task | Who |
|---|---|---|
| Day -3 | Create each draft in Studio: import the spec, paste Name, Short, Long, Category, Tags, plan wording from Part B; upload the 500 by 500 logo | Grok, owner |
| Day -2 | Gateway: secret header X-API-Key, copy the proxy secret, add the Railway variable, save. Test one call from the Studio test page | Owner (Claude checks the variable name) |
| Day -1 | Pre-publish checks: Try-it body pre-filled and returns 200; every paste block has no price, no brand word, free only in tags; gate items below done | Claude, Grok |
| Day -1 | Claude makes one live call through RapidAPI to confirm the X-Fields-Not-Set response headers survive the proxy; the tutorials use format=json either way. A small sample fillable PDF is hosted on freedailypro.com. | Claude |
| Day 0 | Tick the Terms box and publish. Pin the Try-it endpoint first. Basic plan visible, no deprecated plan | Owner |
| Day 0 to 2 | Upload tutorial 1 and tutorial 2 on the Tutorials tab (code in curl, JavaScript and Python, no code-hosting links) | Grok |
| Day 1 | First dev.to article (problem, a working request, the response), linking to the RapidAPI listing and the developer page. Claude supplies the instructions and the real example | Grok (Claude briefs) |
| Day 2 to 3 | Postman collection with the listing's requests; add its public link to the description | Grok |
| Day 4 | Blog guide on freedailypro.com for the same job, plus a Spotlight on the About tab pointing to the dev.to article | Grok writes, Claude publishes |
| Day 7 | First review: check Studio, Analytics for views, subscribers and calls; reply to every discussion post; add one more example request | Grok, owner |
| Day 7 to 10 | Ask 3 to 5 genuine early users for a rating. Do not offer anything in return | Owner |
| Day 9 | Second dev.to article with a different angle (a tutorial title from Part B) | Grok |
| Day 14 | End of the promotion window: record views, subscribers, calls and any errors; retag the listing with the weakest views; stop promoting it | Grok, owner |
| Day 15 to 30 | Maintenance only: reply to discussions within 24 hours, one new example request per week, no new articles. Claude fixes any spec or behaviour issue found | Grok, Claude |
| Day 30 | 30-day read of Studio analytics for these listings; send the figures to Claude for the next report for Grok | Owner, Claude |

Wave 1 is two overlapping windows of three listings. B1 to B3 use the table above from Days 3, 4 and 5; B4 to B6 use it from Days 17, 18 and 19 (Day 0 of each listing is its own publish day). Review all six on Day 30 and Day 32, and use these numbers, with the Day 60 reading, to pick the listing that gets the re-push slot on Day 61.

## Wave 2: fitness, time zone, currency and VAT (Days 31 to 46)
Listings: B7 Fitness and health calculator; B8 Time zone and date calculator; B9 Currency and VAT.

| When | Task | Who |
|---|---|---|
| Day -3 | Create each draft in Studio: import the spec, paste Name, Short, Long, Category, Tags, plan wording from Part B; upload the 500 by 500 logo | Grok, owner |
| Day -2 | Gateway: secret header X-API-Key, copy the proxy secret, add the Railway variable, save. Test one call from the Studio test page | Owner (Claude checks the variable name) |
| Day -1 | Pre-publish checks: Try-it body pre-filled and returns 200; every paste block has no price, no brand word, free only in tags; gate items below done | Claude, Grok |
| Day -1 | Claude captures one real IANA conversion (localTime, fromZone, toZones, nextChange) with capture-openapi-responses.mjs and pastes it into the long description and the Try-it body. | Claude |
| Day -1 | Claude runs one real vat-validate and one real exchange-rates call on the deployed API (neither could be reached from the build sandbox) and replaces the illustrative VAT example with the real answer. | Claude |
| Day 0 | Tick the Terms box and publish. Pin the Try-it endpoint first. Basic plan visible, no deprecated plan | Owner |
| Day 0 to 2 | Upload tutorial 1 and tutorial 2 on the Tutorials tab (code in curl, JavaScript and Python, no code-hosting links) | Grok |
| Day 1 | First dev.to article (problem, a working request, the response), linking to the RapidAPI listing and the developer page. Claude supplies the instructions and the real example | Grok (Claude briefs) |
| Day 2 to 3 | Postman collection with the listing's requests; add its public link to the description | Grok |
| Day 4 | Blog guide on freedailypro.com for the same job, plus a Spotlight on the About tab pointing to the dev.to article | Grok writes, Claude publishes |
| Day 7 | First review: check Studio, Analytics for views, subscribers and calls; reply to every discussion post; add one more example request | Grok, owner |
| Day 7 to 10 | Ask 3 to 5 genuine early users for a rating. Do not offer anything in return | Owner |
| Day 9 | Second dev.to article with a different angle (a tutorial title from Part B) | Grok |
| Day 14 | End of the promotion window: record views, subscribers, calls and any errors; retag the listing with the weakest views; stop promoting it | Grok, owner |
| Day 15 to 30 | Maintenance only: reply to discussions within 24 hours, one new example request per week, no new articles. Claude fixes any spec or behaviour issue found | Grok, Claude |
| Day 30 | 30-day read of Studio analytics for these listings; send the figures to Claude for the next report for Grok | Owner, Claude |

Time Zone and Currency and VAT must not be published until their gate item is done. If the gate slips, swap in the next listing of Wave 3 and keep three promoted at a time.

## Wave 3: unit converter, bookkeeping, image (Days 45 to 60)
Listings: B10 Unit converter; B11 Bookkeeping (text-PDF bank statements); B12 Image (resize fit modes, compress, watermark).

| When | Task | Who |
|---|---|---|
| Day -3 | Create each draft in Studio: import the spec, paste Name, Short, Long, Category, Tags, plan wording from Part B; upload the 500 by 500 logo | Grok, owner |
| Day -2 | Gateway: secret header X-API-Key, copy the proxy secret, add the Railway variable, save. Test one call from the Studio test page | Owner (Claude checks the variable name) |
| Day -1 | Pre-publish checks: Try-it body pre-filled and returns 200; every paste block has no price, no brand word, free only in tags; gate items below done | Claude, Grok |
| Day -1 | Claude runs several real bank statement PDFs (different layouts) through the deployed API and reports which layouts reconcile; the listing wording stays "text-based statements" whatever the result. | Claude |
| Day -1 | Claude runs the Try-it resize on the live host and checks one real photo (not a generated picture) for output look and size. | Claude |
| Day 0 | Tick the Terms box and publish. Pin the Try-it endpoint first. Basic plan visible, no deprecated plan | Owner |
| Day 0 to 2 | Upload tutorial 1 and tutorial 2 on the Tutorials tab (code in curl, JavaScript and Python, no code-hosting links) | Grok |
| Day 1 | First dev.to article (problem, a working request, the response), linking to the RapidAPI listing and the developer page. Claude supplies the instructions and the real example | Grok (Claude briefs) |
| Day 2 to 3 | Postman collection with the listing's requests; add its public link to the description | Grok |
| Day 4 | Blog guide on freedailypro.com for the same job, plus a Spotlight on the About tab pointing to the dev.to article | Grok writes, Claude publishes |
| Day 7 | First review: check Studio, Analytics for views, subscribers and calls; reply to every discussion post; add one more example request | Grok, owner |
| Day 7 to 10 | Ask 3 to 5 genuine early users for a rating. Do not offer anything in return | Owner |
| Day 9 | Second dev.to article with a different angle (a tutorial title from Part B) | Grok |
| Day 14 | End of the promotion window: record views, subscribers, calls and any errors; retag the listing with the weakest views; stop promoting it | Grok, owner |
| Day 15 to 30 | Maintenance only: reply to discussions within 24 hours, one new example request per week, no new articles. Claude fixes any spec or behaviour issue found | Grok, Claude |
| Day 30 | 30-day read of Studio analytics for these listings; send the figures to Claude for the next report for Grok | Owner, Claude |

## Wave 4: audio, video and the re-push (Days 59 to 74)
Listings: B13 Audio; B14 Video.

| When | Task | Who |
|---|---|---|
| Day -3 | Create each draft in Studio: import the spec, paste Name, Short, Long, Category, Tags, plan wording from Part B; upload the 500 by 500 logo | Grok, owner |
| Day -2 | Gateway: secret header X-API-Key, copy the proxy secret, add the Railway variable, save. Test one call from the Studio test page | Owner (Claude checks the variable name) |
| Day -1 | Pre-publish checks: Try-it body pre-filled and returns 200; every paste block has no price, no brand word, free only in tags; gate items below done | Claude, Grok |
| Day -1 | Claude confirms the CPU load of audio calls on the host stays acceptable before promotion. | Claude |
| Day -1 | Claude confirms timeout and 503 Retry-After behaviour on a 20 MB clip; the Try-it sample stays tiny. | Claude |
| Day 0 | Tick the Terms box and publish. Pin the Try-it endpoint first. Basic plan visible, no deprecated plan | Owner |
| Day 0 to 2 | Upload tutorial 1 and tutorial 2 on the Tutorials tab (code in curl, JavaScript and Python, no code-hosting links) | Grok |
| Day 1 | First dev.to article (problem, a working request, the response), linking to the RapidAPI listing and the developer page. Claude supplies the instructions and the real example | Grok (Claude briefs) |
| Day 2 to 3 | Postman collection with the listing's requests; add its public link to the description | Grok |
| Day 4 | Blog guide on freedailypro.com for the same job, plus a Spotlight on the About tab pointing to the dev.to article | Grok writes, Claude publishes |
| Day 7 | First review: check Studio, Analytics for views, subscribers and calls; reply to every discussion post; add one more example request | Grok, owner |
| Day 7 to 10 | Ask 3 to 5 genuine early users for a rating. Do not offer anything in return | Owner |
| Day 9 | Second dev.to article with a different angle (a tutorial title from Part B) | Grok |
| Day 14 | End of the promotion window: record views, subscribers, calls and any errors; retag the listing with the weakest views; stop promoting it | Grok, owner |
| Day 15 to 30 | Maintenance only: reply to discussions within 24 hours, one new example request per week, no new articles. Claude fixes any spec or behaviour issue found | Grok, Claude |
| Day 30 | 30-day read of Studio analytics for these listings; send the figures to Claude for the next report for Grok | Owner, Claude |

Day 61: the third slot goes to a re-push of whichever listing has the best Studio numbers at Day 60 (new article, new example, fresh Postman run). It is a repeat promotion, not a new listing.

---
# Part D: day-by-day order (never more than 3 promoted at once)

Day 1 is Monday 2 November 2026. Each listing is promoted for 14 days from its start day, in three slots that never overlap beyond three listings. Publishing a listing and starting its promotion happen on the same day, so no listing sits live and unpromoted. Preparation days are not promotion. The Part A edits are edits, not promotion; the six live listings are not promoted.

Suggested Railway variables (one per new listing): RAPID_PROXY_SECRET_PPTX (B1), RAPID_PROXY_SECRET_RETIRE (B2), RAPID_PROXY_SECRET_PAYROLL (B3), RAPID_PROXY_SECRET_PDFFORMS (B4), RAPID_PROXY_SECRET_MORTGAGE (B5), RAPID_PROXY_SECRET_SEO (B6), RAPID_PROXY_SECRET_FITNESS (B7), RAPID_PROXY_SECRET_TIME (B8), RAPID_PROXY_SECRET_CURRENCY (B9), RAPID_PROXY_SECRET_UNITS (B10), RAPID_PROXY_SECRET_BOOKKEEPING (B11), RAPID_PROXY_SECRET_IMAGE (B12), RAPID_PROXY_SECRET_AUDIO (B13), RAPID_PROXY_SECRET_VIDEO (B14).

| Day | Date | Work that day | Promoted now |
|---|---|---|---|
| 1 | Mon 02 Nov | Part A: edit A1 and A2; Prep B1: create the Studio draft, import spec, paste fields; Prep B2: create the Studio draft, import spec, paste fields | none (0) |
| 2 | Tue 03 Nov | Part A: edit A4 and A5; Prep B1: gateway and Railway variable RAPID_PROXY_SECRET_PPTX; Prep B1: pre-publish checks; Prep B2: gateway and Railway variable RAPID_PROXY_SECRET_RETIRE; Prep B3: create the Studio draft, import spec, paste fields | none (0) |
| 3 | Wed 04 Nov | Part A: edit A3 and A6; confirm the Public APIs project is not public; START promotion and PUBLISH B1 PPTX generator: tutorials 1 and 2, pin Try-it; Prep B2: pre-publish checks; Prep B3: gateway and Railway variable RAPID_PROXY_SECRET_PAYROLL | B1 (1) |
| 4 | Thu 05 Nov | B1: dev.to article 1; START promotion and PUBLISH B2 401k and retirement calculator: tutorials 1 and 2, pin Try-it; Prep B3: pre-publish checks | B1, B2 (2) |
| 5 | Fri 06 Nov | B1: Postman collection; B2: dev.to article 1; START promotion and PUBLISH B3 Paycheck and payroll tax: tutorials 1 and 2, pin Try-it | B1, B2, B3 (3) |
| 6 | Sat 07 Nov | B2: Postman collection; B3: dev.to article 1 | B1, B2, B3 (3) |
| 7 | Sun 08 Nov | B1: blog guide and Spotlight; B3: Postman collection | B1, B2, B3 (3) |
| 8 | Mon 09 Nov | B2: blog guide and Spotlight | B1, B2, B3 (3) |
| 9 | Tue 10 Nov | B3: blog guide and Spotlight | B1, B2, B3 (3) |
| 10 | Wed 11 Nov | B1: first Studio review; ask 3 to 5 real early users for a rating | B1, B2, B3 (3) |
| 11 | Thu 12 Nov | B2: first Studio review; ask 3 to 5 real early users for a rating | B1, B2, B3 (3) |
| 12 | Fri 13 Nov | B1: dev.to article 2; B3: first Studio review; ask 3 to 5 real early users for a rating | B1, B2, B3 (3) |
| 13 | Sat 14 Nov | B2: dev.to article 2 | B1, B2, B3 (3) |
| 14 | Sun 15 Nov | B3: dev.to article 2; Prep B4: create the Studio draft, import spec, paste fields | B1, B2, B3 (3) |
| 15 | Mon 16 Nov | Prep B4: gateway and Railway variable RAPID_PROXY_SECRET_PDFFORMS; Prep B5: create the Studio draft, import spec, paste fields | B1, B2, B3 (3) |
| 16 | Tue 17 Nov | END promotion B1: record views, subscribers, calls; retag if weakest; Prep B4: pre-publish checks and GATE: Claude makes one live call through RapidAPI to confirm the X-Fields-Not-Set response headers survive the proxy; the tutorials use format=json either way. A small sample fillable PDF is hosted on freedailypro.com.; Prep B5: gateway and Railway variable RAPID_PROXY_SECRET_MORTGAGE; Prep B6: create the Studio draft, import spec, paste fields | B1, B2, B3 (3) |
| 17 | Wed 18 Nov | END promotion B2: record views, subscribers, calls; retag if weakest; START promotion and PUBLISH B4 PDF forms (fill, parse, flatten): tutorials 1 and 2, pin Try-it; Prep B5: pre-publish checks; Prep B6: gateway and Railway variable RAPID_PROXY_SECRET_SEO | B2, B3, B4 (3) |
| 18 | Thu 19 Nov | END promotion B3: record views, subscribers, calls; retag if weakest; B4: dev.to article 1; START promotion and PUBLISH B5 Mortgage and loan: tutorials 1 and 2, pin Try-it; Prep B6: pre-publish checks | B3, B4, B5 (3) |
| 19 | Fri 20 Nov | B4: Postman collection; B5: dev.to article 1; START promotion and PUBLISH B6 SEO meta tags: tutorials 1 and 2, pin Try-it | B4, B5, B6 (3) |
| 20 | Sat 21 Nov | B5: Postman collection; B6: dev.to article 1 | B4, B5, B6 (3) |
| 21 | Sun 22 Nov | B4: blog guide and Spotlight; B6: Postman collection | B4, B5, B6 (3) |
| 22 | Mon 23 Nov | B5: blog guide and Spotlight | B4, B5, B6 (3) |
| 23 | Tue 24 Nov | B6: blog guide and Spotlight | B4, B5, B6 (3) |
| 24 | Wed 25 Nov | B4: first Studio review; ask 3 to 5 real early users for a rating | B4, B5, B6 (3) |
| 25 | Thu 26 Nov | B5: first Studio review; ask 3 to 5 real early users for a rating | B4, B5, B6 (3) |
| 26 | Fri 27 Nov | B4: dev.to article 2; B6: first Studio review; ask 3 to 5 real early users for a rating | B4, B5, B6 (3) |
| 27 | Sat 28 Nov | B5: dev.to article 2 | B4, B5, B6 (3) |
| 28 | Sun 29 Nov | B6: dev.to article 2; Prep B7: create the Studio draft, import spec, paste fields | B4, B5, B6 (3) |
| 29 | Mon 30 Nov | Prep B7: gateway and Railway variable RAPID_PROXY_SECRET_FITNESS; Prep B8: create the Studio draft, import spec, paste fields | B4, B5, B6 (3) |
| 30 | Tue 01 Dec | END promotion B4: record views, subscribers, calls; retag if weakest; Prep B7: pre-publish checks; Prep B8: gateway and Railway variable RAPID_PROXY_SECRET_TIME; Prep B9: create the Studio draft, import spec, paste fields; 30-day review of the six live listings and the first Wave 1 listings (feeds the Day 60 re-push pick) | B4, B5, B6 (3) |
| 31 | Wed 02 Dec | END promotion B5: record views, subscribers, calls; retag if weakest; START promotion and PUBLISH B7 Fitness and health calculator: tutorials 1 and 2, pin Try-it; Prep B8: pre-publish checks and GATE: Claude captures one real IANA conversion (localTime, fromZone, toZones, nextChange) with capture-openapi-responses.mjs and pastes it into the long description and the Try-it body.; Prep B9: gateway and Railway variable RAPID_PROXY_SECRET_CURRENCY | B5, B6, B7 (3) |
| 32 | Thu 03 Dec | END promotion B6: record views, subscribers, calls; retag if weakest; B7: dev.to article 1; START promotion and PUBLISH B8 Time zone and date calculator: tutorials 1 and 2, pin Try-it; Prep B9: pre-publish checks and GATE: Claude runs one real vat-validate and one real exchange-rates call on the deployed API (neither could be reached from the build sandbox) and replaces the illustrative VAT example with the real answer. | B6, B7, B8 (3) |
| 33 | Fri 04 Dec | B7: Postman collection; B8: dev.to article 1; START promotion and PUBLISH B9 Currency and VAT: tutorials 1 and 2, pin Try-it | B7, B8, B9 (3) |
| 34 | Sat 05 Dec | B8: Postman collection; B9: dev.to article 1 | B7, B8, B9 (3) |
| 35 | Sun 06 Dec | B7: blog guide and Spotlight; B9: Postman collection | B7, B8, B9 (3) |
| 36 | Mon 07 Dec | B8: blog guide and Spotlight | B7, B8, B9 (3) |
| 37 | Tue 08 Dec | B9: blog guide and Spotlight | B7, B8, B9 (3) |
| 38 | Wed 09 Dec | B7: first Studio review; ask 3 to 5 real early users for a rating | B7, B8, B9 (3) |
| 39 | Thu 10 Dec | B8: first Studio review; ask 3 to 5 real early users for a rating | B7, B8, B9 (3) |
| 40 | Fri 11 Dec | B7: dev.to article 2; B9: first Studio review; ask 3 to 5 real early users for a rating | B7, B8, B9 (3) |
| 41 | Sat 12 Dec | B8: dev.to article 2 | B7, B8, B9 (3) |
| 42 | Sun 13 Dec | B9: dev.to article 2; Prep B10: create the Studio draft, import spec, paste fields | B7, B8, B9 (3) |
| 43 | Mon 14 Dec | Prep B10: gateway and Railway variable RAPID_PROXY_SECRET_UNITS; Prep B11: create the Studio draft, import spec, paste fields | B7, B8, B9 (3) |
| 44 | Tue 15 Dec | END promotion B7: record views, subscribers, calls; retag if weakest; Prep B10: pre-publish checks; Prep B11: gateway and Railway variable RAPID_PROXY_SECRET_BOOKKEEPING; Prep B12: create the Studio draft, import spec, paste fields | B7, B8, B9 (3) |
| 45 | Wed 16 Dec | END promotion B8: record views, subscribers, calls; retag if weakest; START promotion and PUBLISH B10 Unit converter: tutorials 1 and 2, pin Try-it; Prep B11: pre-publish checks and GATE: Claude runs several real bank statement PDFs (different layouts) through the deployed API and reports which layouts reconcile; the listing wording stays "text-based statements" whatever the result.; Prep B12: gateway and Railway variable RAPID_PROXY_SECRET_IMAGE | B8, B9, B10 (3) |
| 46 | Thu 17 Dec | END promotion B9: record views, subscribers, calls; retag if weakest; B10: dev.to article 1; START promotion and PUBLISH B11 Bookkeeping (text-PDF bank statements): tutorials 1 and 2, pin Try-it; Prep B12: pre-publish checks and GATE: Claude runs the Try-it resize on the live host and checks one real photo (not a generated picture) for output look and size. | B9, B10, B11 (3) |
| 47 | Fri 18 Dec | B10: Postman collection; B11: dev.to article 1; START promotion and PUBLISH B12 Image (resize fit modes, compress, watermark): tutorials 1 and 2, pin Try-it | B10, B11, B12 (3) |
| 48 | Sat 19 Dec | B11: Postman collection; B12: dev.to article 1 | B10, B11, B12 (3) |
| 49 | Sun 20 Dec | B10: blog guide and Spotlight; B12: Postman collection | B10, B11, B12 (3) |
| 50 | Mon 21 Dec | B11: blog guide and Spotlight | B10, B11, B12 (3) |
| 51 | Tue 22 Dec | B12: blog guide and Spotlight | B10, B11, B12 (3) |
| 52 | Wed 23 Dec | B10: first Studio review; ask 3 to 5 real early users for a rating | B10, B11, B12 (3) |
| 53 | Thu 24 Dec | B11: first Studio review; ask 3 to 5 real early users for a rating | B10, B11, B12 (3) |
| 54 | Fri 25 Dec | B10: dev.to article 2; B12: first Studio review; ask 3 to 5 real early users for a rating | B10, B11, B12 (3) |
| 55 | Sat 26 Dec | B11: dev.to article 2 | B10, B11, B12 (3) |
| 56 | Sun 27 Dec | B12: dev.to article 2; Prep B13: create the Studio draft, import spec, paste fields | B10, B11, B12 (3) |
| 57 | Mon 28 Dec | Prep B13: gateway and Railway variable RAPID_PROXY_SECRET_AUDIO; Prep B14: create the Studio draft, import spec, paste fields | B10, B11, B12 (3) |
| 58 | Tue 29 Dec | END promotion B10: record views, subscribers, calls; retag if weakest; Prep B13: pre-publish checks and GATE: Claude confirms the CPU load of audio calls on the host stays acceptable before promotion.; Prep B14: gateway and Railway variable RAPID_PROXY_SECRET_VIDEO | B10, B11, B12 (3) |
| 59 | Wed 30 Dec | END promotion B11: record views, subscribers, calls; retag if weakest; START promotion and PUBLISH B13 Audio: tutorials 1 and 2, pin Try-it; Prep B14: pre-publish checks and GATE: Claude confirms timeout and 503 Retry-After behaviour on a 20 MB clip; the Try-it sample stays tiny. | B11, B12, B13 (3) |
| 60 | Thu 31 Dec | END promotion B12: record views, subscribers, calls; retag if weakest; B13: dev.to article 1; START promotion and PUBLISH B14 Video: tutorials 1 and 2, pin Try-it; Pick the re-push listing from Studio numbers | B12, B13, B14 (3) |
| 61 | Fri 01 Jan | B13: Postman collection; B14: dev.to article 1; START promotion: REPUSH best performer re-push (chosen from Studio analytics at Day 60) | B13, B14, REPUSH (3) |
| 62 | Sat 02 Jan | B14: Postman collection; REPUSH: new dev.to article and one new example request | B13, B14, REPUSH (3) |
| 63 | Sun 03 Jan | B13: blog guide and Spotlight | B13, B14, REPUSH (3) |
| 64 | Mon 04 Jan | B14: blog guide and Spotlight | B13, B14, REPUSH (3) |
| 65 | Tue 05 Jan | Maintenance: reply to discussions within 24 hours | B13, B14, REPUSH (3) |
| 66 | Wed 06 Jan | B13: first Studio review; ask 3 to 5 real early users for a rating | B13, B14, REPUSH (3) |
| 67 | Thu 07 Jan | B14: first Studio review; ask 3 to 5 real early users for a rating; REPUSH: second article from a tutorial title; Postman run | B13, B14, REPUSH (3) |
| 68 | Fri 08 Jan | B13: dev.to article 2 | B13, B14, REPUSH (3) |
| 69 | Sat 09 Jan | B14: dev.to article 2 | B13, B14, REPUSH (3) |
| 70 | Sun 10 Jan | Maintenance: reply to discussions within 24 hours | B13, B14, REPUSH (3) |
| 71 | Mon 11 Jan | Maintenance: reply to discussions within 24 hours | B13, B14, REPUSH (3) |
| 72 | Tue 12 Jan | END promotion B13: record views, subscribers, calls; retag if weakest | B13, B14, REPUSH (3) |
| 73 | Wed 13 Jan | END promotion B14: record views, subscribers, calls; retag if weakest | B14, REPUSH (2) |
| 74 | Thu 14 Jan | REPUSH: window review | REPUSH (1) |

After Day 74 every listing is in maintenance. Re-plan from the Studio numbers: promote the top three again and retire effort from the rest.

---
# What I could not verify
- Live listing texts and per-listing plan numbers (see the plan note above).
- Whether RapidAPI's gateway counts a 4xx call against a plan quota (note 1).
- Whether the short description, long description or tags feed RapidAPI search ranking (playbook: unverified); whether Studio lets a plan with a subscriber be removed or only hidden; what a spec re-import overwrites.
- Live behaviour not testable from the build environment: the exchange-rates broad set and the VIES lookup (B9), an IANA time zone conversion (B8, no captured example), the X-Fields-Not-Set headers through the proxy (B4), real bank PDFs (B11), media load and timeouts (B12 to B14). Image outputs were checked on generated pictures only.
- Figures read from secondary sources and marked estimate in dataStatus in the response: the 2026 contribution limits (B2); the California SDI rate is flagged unverified in the paycheck response (B3).
- The contribution-limits spec example shows availableYears as only 2025 while the default taxYear is 2026; check what the live endpoint returns before pinning it anywhere.
- The spec URLs at freedailypro.com/api-specs (note 5).
- Examples labelled capture, illustrative or structure-only are not real captured responses.
