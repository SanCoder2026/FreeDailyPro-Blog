# B-0040a Per-tool task-API spec, tools 1–10 (appendix to B-0039)

**Priority:** P1 (read with B-0039; fixes marked P0 there come first)
**Estimated effort:** reference document; build effort is sized in B-0039

**How to work with us:** you're the implementation partner, not an order-taker. This is our best reading of each tool from its live page and live read-only API calls on Oct 29 2026. Inspect the real handlers before building: if the code already supports something we marked missing, or a param name differs, the code wins. Challenge any endpoint you think is not worth it.

Legend: **exists** = live and works as listed · **exists – fix/extend** = live, needs a bug fix or new params · **NEW** = to build. Weight = billing units per call (B-0039 pricing). Auth everywhere: header `X-API-Key` (RapidAPI: `X-RapidAPI-Key` via proxy). Base: `https://api.freedailypro.com`. Full endpoint list: `2026-10-29-B-0040-task-endpoints.csv`. listings.yaml entries: `2026-10-29-B-0040-listings-snippet.yaml`.

## 1. PDF Redact API – Permanently Remove Text & PII
Site tool: https://www.freedailypro.com/tool/redact-pdf · Category: Data · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Search terms (one per line), Match case, Whole words
- Detectors: email, phone, card, SSN-style, EIN-style, likely names (Select all)
- Draw boxes by hand per page
- Remove comments/links/form values/bookmarks containing the term
- Clear metadata
- Preview then Apply; marked pages become images, unmarked pages untouched

**Gap vs current API (live-tested read-only):**
- API accepts ONLY hand boxes (`boxes` JSON). Search terms, detectors, annotation removal and metadata clearing are UI-only (live test: `terms=John Doe` → 400 'No redaction boxes provided').
- An API caller cannot know where text sits, so the main UI workflow (find & redact a name everywhere) is impossible via API today.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists | `POST /v1/redact-pdf` | Redact PDF areas (boxes) | multipart | file (binary, PDF ≤20 MB, required); boxes (string JSON {page:[{x,y,width,height}]}, points from top-left, required) | application/pdf (marked pages rasterised, black boxes) | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| NEW | `POST /v1/pdf/redact/find` | Find redactable text (no file change) — Returns boxes in the SAME coordinate system as /v1/redact-pdf so callers can review then redact. | multipart | file (PDF ≤20 MB); terms (JSON array or newline list, ≤200 terms); presets (csv of email,phone,card,ssn,ein,names); matchCase (bool, false); wholeWords (bool, false) | application/json {result:{matches:[{page,text,kind,boxes:[{x,y,width,height}]}],count,scannedPagesWithoutText:[n]}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/pdf/redact/search` | Redact by search terms & PII detectors (one call) | multipart | file; terms; presets; matchCase; wholeWords; removeAnnotations (bool, true); stripMetadata (bool, true); extraBoxes (same JSON as boxes, optional) | application/pdf + headers X-Redaction-Count, X-Pages-Redacted, X-Warnings (e.g. scanned pages had no text) | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| NEW | `POST /v1/pdf/redact/pii` | Auto-redact PII (preset only) — Keyword alias for 'pii redaction api' listing; thin wrapper over /redact/search. | multipart | file; presets (default email,phone,card,ssn); stripMetadata (bool,true) | application/pdf (same headers) | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/redact-pdf`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/redact-pdf' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@contract.pdf' \
  -F 'boxes={"1":[{"x":40,"y":40,"width":300,"height":30}]}' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('contract.pdf'), 'contract.pdf');
fd.append('boxes', '{"1":[{"x":40,"y":40,"width":300,"height":30}]}');
const r = await fetch('https://api.freedailypro.com/v1/redact-pdf', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/redact-pdf',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('contract.pdf','rb'))], data={"boxes": "{\"1\":[{\"x\":40,\"y\":40,\"width\":300,\"height\":30}]}"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 application/pdf (15,790 B, 0.64 s)
```
**Proposed (after build): `POST /v1/pdf/redact/search`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pdf/redact/search' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@contract.pdf' \
  -F 'terms=["John Doe","ACME Ltd"]' \
  -F 'presets=email,phone' \
  -F 'stripMetadata=true' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('contract.pdf'), 'contract.pdf');
fd.append('terms', '["John Doe","ACME Ltd"]');
fd.append('presets', 'email,phone');
fd.append('stripMetadata', 'true');
const r = await fetch('https://api.freedailypro.com/v1/pdf/redact/search', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pdf/redact/search',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('contract.pdf','rb'))], data={"terms": "[\"John Doe\",\"ACME Ltd\"]", "presets": "email,phone", "stripMetadata": "true"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 application/pdf; X-Redaction-Count: 7; X-Pages-Redacted: 1,3
```

**Doc text (for listings.yaml / copy.md)**
- Title: PDF Redact API – Permanently Remove Text & PII
- One-liner: PDF Redact API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: PDF Redact API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/redact-pdf. Each task is its own endpoint, so you call exactly the option you need (Redact PDF areas (boxes); Find redactable text (no file change); Redact by search terms & PII detectors (one call); Auto-redact PII (preset only)). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: pdf redaction, redact pdf, pii, gdpr, privacy
- Category: Data

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 2. QR Code Generator API – PNG & SVG
Site tool: https://www.freedailypro.com/tool/qr-generator · Category: Tools · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Type: Link, Text, WiFi, Contact (vCard), Email, SMS, Phone
- Download size (e.g. 1000 px)
- Error correction L/M/Q/H (M default)
- Foreground colour, background colour
- Logo (optional) → ECC forced to H
- Download PNG or SVG

**Gap vs current API (live-tested read-only):**
- API takes only `text` and returns SVG markup inside JSON. `format`, `size`, `color` are silently ignored (live test with format=svg,size=500,color=#ff0000 → black default SVG).
- No PNG at all, yet the CSV title says 'PNG & SVG' → listing title would be a false claim until fixed.
- No WiFi/vCard/email/SMS/phone builders, no ECC, no logo.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/security/qr` | QR code (text → SVG in JSON) | json | text (string, required, ≤2,953 bytes); ADD: ecc (L|M|Q|H, M); color (hex, 000000); background (hex, ffffff); margin (int 0–16, 4) — and reject unknown fields with 400 instead of ignoring | application/json {tool,result:{svg}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/qr/png` | QR code as PNG image | json | data (string, required); size (int 128–4000 px, 1000); ecc (L|M|Q|H, M); color (hex, 000000); background (hex, ffffff); margin (int 0–16, 4) | image/png | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/qr/svg` | QR code as SVG file | json | same as /v1/qr/png minus size | image/svg+xml | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/qr/wifi` | WiFi QR code | json | ssid (string, required); password (string); encryption (WPA|WEP|nopass, WPA); hidden (bool,false); format (png|svg, png); size; ecc; color; background | image/png | image/svg+xml | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/qr/vcard` | Contact (vCard) QR code | json | firstName, lastName, phone, email, org, title, url, address (strings; at least one of name/phone/email); format; size; ecc; color; background | image/png | image/svg+xml | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/qr/message` | Email / SMS / Phone QR code | json | type (email|sms|phone, required); to (string, required); subject (email); body (email/sms); format; size; ecc; color; background | image/png | image/svg+xml | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/qr/logo` | QR code with centred logo | multipart | data (string, required); logo (PNG/JPEG ≤2 MB, required); logoPercent (10–30, 20); format; size; color; background (ECC forced H) | image/png | image/svg+xml | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/security/qr`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/security/qr' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"text":"https://www.freedailypro.com"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/security/qr', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"text":"https://www.freedailypro.com"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/security/qr',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"text":"https://www.freedailypro.com"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"tool":"QR code generator ...","result":{"svg":"<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 33 33\" ...>"}}
```
**Proposed (after build): `POST /v1/qr/png`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/qr/png' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"data":"https://www.freedailypro.com","size":1000,"ecc":"M","color":"0b6e4f"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/qr/png', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"data":"https://www.freedailypro.com","size":1000,"ecc":"M","color":"0b6e4f"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/qr/png',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"data":"https://www.freedailypro.com","size":1000,"ecc":"M","color":"0b6e4f"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
200 image/png 1000×1000
```

**Doc text (for listings.yaml / copy.md)**
- Title: QR Code Generator API – PNG & SVG  ⚠ keep "PNG" out of the title until /v1/qr/png is live
- One-liner: QR Code Generator API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: QR Code Generator API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/qr-generator. Each task is its own endpoint, so you call exactly the option you need (QR code (text → SVG in JSON); QR code as PNG image; QR code as SVG file; WiFi QR code; Contact (vCard) QR code; Email / SMS / Phone QR code; QR code with centred logo). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: qr code generator, qr code, qr api, png, svg, wifi qr, vcard qr
- Category: Tools

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 3. PDF Merge API – Combine PDFs
Site tool: https://www.freedailypro.com/tool/merge-pdf · Category: Data · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Unlimited files, drag to order
- Per-file page selection (e.g. 1-3,5)
- Blank-page option so each file starts on a front side (duplex)

**Gap vs current API (live-tested read-only):**
- Order = order of `files` fields (fine).
- Per-file page selection is UI-only: sending `pages` is silently ignored (live: 3-page + 1-page with pages=["1-2","1"] → 4 pages).
- No duplex blank-page option.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/pdf/merge` | Merge PDFs | multipart | files (binary[], ≥2, ≤60 MB total, required); ADD: pages (JSON array aligned to files, e.g. ["1-3,5",""] — empty = all); duplexBlankPages (bool,false); outputName (string) | application/pdf + X-Page-Count | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/pdf/merge/urls` | Merge PDFs from URLs — Optional — agents usually hold URLs, not bytes. Enforce SSRF guard (public https only, ≤60 MB). Drop if policy disallows fetching. | json | urls (array 2–20 https URLs, required); pages (array); duplexBlankPages | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/pdf/merge`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pdf/merge' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'files=@a.pdf' \
  -F 'files=@b.pdf' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('files', await fs.openAsBlob('a.pdf'), 'a.pdf');
fd.append('files', await fs.openAsBlob('b.pdf'), 'b.pdf');
const r = await fetch('https://api.freedailypro.com/v1/pdf/merge', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pdf/merge',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('files', open('a.pdf','rb')), ('files', open('b.pdf','rb'))], data={}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 application/pdf, 2 pages (0.21 s)
```

**Doc text (for listings.yaml / copy.md)**
- Title: PDF Merge API – Combine PDFs
- One-liner: PDF Merge API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: PDF Merge API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/merge-pdf. Each task is its own endpoint, so you call exactly the option you need (Merge PDFs; Merge PDFs from URLs). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: pdf merge, combine pdf, merge pdf, join pdf
- Category: Data

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 4. PDF Compress API – Shrink PDF to Target Size
Site tool: https://www.freedailypro.com/tool/compress-pdf · Category: Data · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Balanced / Aggressive / Extreme / Target size
- Each level a full file; keeps original if not smaller
- Several files mode

**Gap vs current API (live-tested read-only):**
- Already split the owner's way (auto, balanced, aggressive, extreme, size, + 3 scanned-B/W variants). This is the REFERENCE pattern.
- Small gap: response doesn't say whether the original was kept or how much it shrank; batch mode UI-only.

**Full UI workflow completable via API?** Today: **yes**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists | `POST /v1/pdf/compress` | Compress PDF (auto) | multipart | file (PDF ≤20 MB); level (auto|medium|strong, auto); targetFileSize (string e.g. 2MB) | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| exists | `POST /v1/pdf/compress/balanced` | Compress PDF – Balanced (text stays selectable) | multipart | file (≤20 MB, ≤100 pages) | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| exists | `POST /v1/pdf/compress/aggressive` | Compress PDF – Aggressive (pages rasterised) | multipart | file | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| exists | `POST /v1/pdf/compress/extreme` | Compress PDF – Extreme (grey → B/W) | multipart | file | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| exists | `POST /v1/pdf/compress/size` | Compress PDF to a target size | multipart | file; targetSize (string, required, e.g. 500KB); limit (balanced|aggressive|extreme, extreme) | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| exists – fix/extend | `POST (all compress routes)` | Add result headers — So API users can tell 'already small' from success, as the UI does. | — | none | ADD headers X-Original-Bytes, X-Result-Bytes, X-Kept-Original (true|false), X-Level-Used | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/pdf/compress/size`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pdf/compress/size' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@scan.pdf' \
  -F 'targetSize=500KB' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('scan.pdf'), 'scan.pdf');
fd.append('targetSize', '500KB');
const r = await fetch('https://api.freedailypro.com/v1/pdf/compress/size', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pdf/compress/size',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('scan.pdf','rb'))], data={"targetSize": "500KB"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 application/pdf (3-page test: 14.7 KB → 1.1 KB, 2.6 s)
```

**Doc text (for listings.yaml / copy.md)**
- Title: PDF Compress API – Shrink PDF to Target Size
- One-liner: PDF Compress API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: PDF Compress API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/compress-pdf. Each task is its own endpoint, so you call exactly the option you need (Compress PDF (auto); Compress PDF – Balanced (text stays selectable); Compress PDF – Aggressive (pages rasterised); Compress PDF – Extreme (grey → B/W); Compress PDF to a target size). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: pdf compress, compress pdf, reduce pdf size, pdf optimizer
- Category: Data

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 5. Loan Amortization Schedule Calculator API
Site tool: https://www.freedailypro.com/tool/loan-calculator · Category: Finance · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Amount, currency (10), annual rate, term in years OR months
- Interest method: reducing balance (EMI) or flat rate
- First payment date
- Extra monthly payment
- Full 360-row schedule, CSV download

**Gap vs current API (live-tested read-only):**
- Two endpoints with inconsistent names: /loan uses annualRatePercent+years (preview ≤12 rows); /amortization uses annualRatePct+months (full schedule).
- Flat-rate method, extra monthly payment (and resulting interest saved / months saved), currency label and CSV export are UI-only.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/converters/loan` | Loan / EMI payment | json | principal (number>0, required); annualRatePercent (0–100, required); years (0–50) OR ADD months (1–600); previewMonths (0–12); firstPaymentDate (YYYY-MM-DD); ADD: interestMethod (reducing|flat, reducing); extraMonthlyPayment (number ≥0, 0); currency (ISO 4217, label only) | application/json {result:{monthlyPayment,totalPayment,totalInterest,schedulePreview[],firstPaymentDate,lastPaymentDate,payoffDate, ADD interestSaved, monthsSaved}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| exists – fix/extend | `POST /v1/converters/amortization` | Full amortization schedule | json | principal; annualRatePct (ADD alias annualRatePercent); months (ADD alias years); firstPaymentDate; ADD interestMethod, extraMonthlyPayment, format (json|csv, json) | application/json {result:{monthlyPayment,totalPaid,totalInterest,schedule[{month,payment,interest,principal,balance,date?}]}} | text/csv | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/finance/emi` | EMI calculator (India keyword alias) — Keyword alias for 'emi calculator' (big India search). Thin wrapper. | json | same as /loan with interestMethod | application/json | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/converters/loan`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/converters/loan' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"principal":250000,"annualRatePercent":6.5,"years":30,"previewMonths":2,"firstPaymentDate":"2026-12-01"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/converters/loan', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"principal":250000,"annualRatePercent":6.5,"years":30,"previewMonths":2,"firstPaymentDate":"2026-12-01"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/converters/loan',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"principal":250000,"annualRatePercent":6.5,"years":30,"previewMonths":2,"firstPaymentDate":"2026-12-01"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"result":{"monthlyPayment":1580.17,"totalPayment":568861.22,"totalInterest":318861.22,"schedulePreview":[{"month":1,"principal":226,"interest":1354.17,"balance":249774,"date":"2026-12-01"},{"month":2,"principal":227.23,"interest":1352.94,"balance":249546.77,"date":"2027-01-01"}],"firstPaymentDate":"2026-12-01","lastPaymentDate":"2056-11-01","payoffDate":"2056-11"}}
```

**Doc text (for listings.yaml / copy.md)**
- Title: Loan Amortization Schedule Calculator API
- One-liner: Loan Amortization Schedule Calculator API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: Loan Amortization Schedule Calculator API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/loan-calculator. Each task is its own endpoint, so you call exactly the option you need (Loan / EMI payment; Full amortization schedule; EMI calculator (India keyword alias)). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: loan calculator, amortization, emi, loan payment, mortgage
- Category: Finance

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 6. JWT Decoder API – Decode & Check Expiry
Site tool: https://www.freedailypro.com/tool/jwt-decoder · Category: Tools · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Paste token (Bearer stripped)
- Header + payload, time claims UTC/local

**Gap vs current API (live-tested read-only):**
- None for the UI workflow — API is richer than UI (now, clockTolerance, status).
- Optional new value: signature verification (UI deliberately doesn't).

**Full UI workflow completable via API?** Today: **yes**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists | `POST /v1/security/jwt-decode` | Decode JWT & check exp/nbf | json | token (string, required, 'Bearer ' stripped); now (epoch|ISO); clockToleranceSeconds (0–86400, 0) | application/json {valid,wellFormed,status,signatureVerified:false,issues[],header,payload,expiresAt,secondsUntilExpiry,expired} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/security/jwt-verify` | Verify JWT signature (HS/RS/ES) — Optional, P3. Never log the secret; document that the secret is sent to us and processed in memory only. | json | token (required); secret (HS*) OR publicKeyPem OR jwksUrl (one required); algorithms (array allow-list); audience; issuer; clockToleranceSeconds | application/json {verified,status,issues[],header,payload} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/security/jwt-decode`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/security/jwt-decode' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJleHAiOjE3MDAwMDAwMDB9.x"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/security/jwt-decode', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJleHAiOjE3MDAwMDAwMDB9.x"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/security/jwt-decode',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJleHAiOjE3MDAwMDAwMDB9.x"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"tool":"Jwt decoder","valid":false,"wellFormed":true,"status":"expired","signatureVerified":false,"issues":["The token expired at 2023-11-14T22:13:20.000Z (exp), ..."],"header":{"alg":"HS256","typ":"JWT"},"payload":{"sub":"123","exp":1700000000},"expiresAt":"2023-11-14T22:13:20.000Z","secondsUntilExpiry":-93323363,"expired":true}
```

**Doc text (for listings.yaml / copy.md)**
- Title: JWT Decoder API – Decode & Check Expiry
- One-liner: JWT Decoder API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: JWT Decoder API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/jwt-decoder. Each task is its own endpoint, so you call exactly the option you need (Decode JWT & check exp/nbf; Verify JWT signature (HS/RS/ES)). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: jwt decode, jwt, token, auth, expiry
- Category: Tools

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 7. Hash Generator API – MD5, SHA-1, SHA-256
Site tool: https://www.freedailypro.com/tool/hash-generator · Category: Cybersecurity · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Text (UTF-8) OR file (any size, 4 MB chunks)
- All five algorithms at once (MD5, SHA-1, SHA-256, SHA-384, SHA-512)
- Paste expected checksum → compare against all five

**Gap vs current API (live-tested read-only):**
- API hashes text only, one algorithm per call (default sha256).
- File hashing and checksum verify are UI-only — the most common developer use (verify a download) is impossible via API.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/security/hash` | Hash text (one algorithm) | json | text (string, required, ≤1 MB); algorithm (md5|sha1|sha256|sha384|sha512, sha256); ADD encoding (hex|base64, hex) | application/json {tool,algorithm,result} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/security/hash/all` | Hash text with all 5 algorithms | json | text (required); encoding (hex|base64) | application/json {result:{md5,sha1,sha256,sha384,sha512}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/security/hash/file` | File checksum (MD5/SHA) | multipart | file (any type ≤100 MB, streamed); algorithm (one or 'all', all) | application/json {result:{bytes, md5?,sha1?,sha256?,sha384?,sha512?}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| NEW | `POST /v1/security/hash/verify` | Verify a checksum | multipart|json | file OR text (one required); expected (hex/base64 string, required) | application/json {result:{match:bool, algorithm:'sha256'|null}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/security/hash`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/security/hash' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"text":"hello world","algorithm":"sha256"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/security/hash', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"text":"hello world","algorithm":"sha256"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/security/hash',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"text":"hello world","algorithm":"sha256"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"tool":"Hash generator client and server side from freedailypro","algorithm":"sha256","result":"b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"}
```
**Proposed (after build): `POST /v1/security/hash/file`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/security/hash/file' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@installer.zip' \
  -F 'algorithm=all' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('installer.zip'), 'installer.zip');
fd.append('algorithm', 'all');
const r = await fetch('https://api.freedailypro.com/v1/security/hash/file', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/security/hash/file',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('installer.zip','rb'))], data={"algorithm": "all"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
{"result":{"bytes":1048576,"md5":"…","sha1":"…","sha256":"…","sha384":"…","sha512":"…"}}
```

**Doc text (for listings.yaml / copy.md)**
- Title: Hash Generator API – MD5, SHA-1, SHA-256
- One-liner: Hash Generator API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: Hash Generator API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/hash-generator. Each task is its own endpoint, so you call exactly the option you need (Hash text (one algorithm); Hash text with all 5 algorithms; File checksum (MD5/SHA); Verify a checksum). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: hash generator, sha256, md5, checksum, sha512
- Category: Cybersecurity

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 8. UUID Generator API – v4 UUIDs in Bulk
Site tool: https://www.freedailypro.com/tool/uuid-generator · Category: Tools · Marketplaces: RapidAPI; API.market

**UI options (live page, Oct 29):**
- Count
- Hyphens on/off
- Uppercase

**Gap vs current API (live-tested read-only):**
- Hyphens/uppercase toggles missing (trivial).
- Optional: v7 (time-ordered) is a strong 2026 keyword.

**Full UI workflow completable via API?** Today: **yes**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/security/uuid` | Generate UUIDs | json | count (1–1000, 1); ADD hyphens (bool,true); uppercase (bool,false); version (4|7, 4) | application/json {tool,result:[...]} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/security/uuid`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/security/uuid' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"count":3}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/security/uuid', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"count":3})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/security/uuid',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"count":3}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"tool":"Uuid generator client and server side from freedailypro","result":["2c087b7b-2842-485f-85c9-db67eccbeab2","a3ddc1bc-5be5-465e-898f-88f767af0e48","adbf18b3-2c26-49d2-8064-bc4a9b1a462f"]}
```

**Doc text (for listings.yaml / copy.md)**
- Title: UUID Generator API – v4 UUIDs in Bulk
- One-liner: UUID Generator API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: UUID Generator API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/uuid-generator. Each task is its own endpoint, so you call exactly the option you need (Generate UUIDs). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: uuid, uuid generator, guid, unique id, uuid v7
- Category: Tools

**Upload notes:** RapidAPI; API.market. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 9. BMI Calculator API
Site tool: https://www.freedailypro.com/tool/bmi-calculator · Category: Health and Fitness · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Metric kg/cm or Imperial lb/ft-in
- Age, sex (optional)
- Waist (optional)
- Asian cut-offs (WHO 23 / 27.5)

**Gap vs current API (live-tested read-only):**
- API returns only bmi+category. Imperial height units unclear (must document inches).
- Age/sex/waist/Asian cut-offs and healthy-weight range are UI-only.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/converters/bmi` | BMI | json | weight (number>0, required); height (number>0, required; cm metric, inches imperial — DOCUMENT); unit (metric|imperial, metric); ADD heightFeet+heightInches (imperial alt); age (2–120); sex (female|male); waist (cm|in); asianCutoffs (bool,false) | application/json {result:{bmi,category, ADD healthyWeightMin,healthyWeightMax,waistToHeightRatio?,cutoffs:'who'|'asian',note}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/converters/bmi`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/converters/bmi' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"weight":70,"height":175,"unit":"metric"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/converters/bmi', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"weight":70,"height":175,"unit":"metric"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/converters/bmi',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"weight":70,"height":175,"unit":"metric"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"tool":"Bmi calculator client and server side from freedailypro","result":{"bmi":22.9,"category":"Normal"}}
```

**Doc text (for listings.yaml / copy.md)**
- Title: BMI Calculator API
- One-liner: BMI Calculator API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: BMI Calculator API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/bmi-calculator. Each task is its own endpoint, so you call exactly the option you need (BMI). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: bmi calculator, bmi, health, body mass index
- Category: Health and Fitness

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 10. PDF Watermark API – Text Stamp with Color & Opacity
Site tool: https://www.freedailypro.com/tool/pdf-watermark · Category: Data · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Text OR Image watermark
- Opacity, size, colour, angle, position or Tiled; logo width
- Skip first page / page range (2-5,8)
- Non-Latin text drawn as picture
- Several files (≤5) → ZIP

**Gap vs current API (live-tested read-only):**
- API: text watermark with position/opacity/color/size/rotation — good.
- Image (logo) watermark, page range and skip-first are UI-only; batch UI-only.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/pdf/watermark` | Text watermark | multipart | file (≤20 MB); text (required); position (center|top-left|top-right|bottom-left|bottom-right|tiled, center); opacity (0.05–1, 0.4); color (hex, 808080); fontSize (6–400, auto); rotationDegrees (-360–360, 45); ADD pages (e.g. 2-5,8; empty=all); skipFirstPage (bool,false) | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/pdf/watermark/image` | Image / logo watermark | multipart | file (PDF); image (PNG/JPEG ≤10 MB, required); widthPercent (5–100, 30); opacity; position (incl. tiled); rotationDegrees (0); pages; skipFirstPage | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/pdf/stamp` | Status stamp (CONFIDENTIAL/DRAFT/PAID…) — Preset keyword alias ('pdf stamp api'). | multipart | file; stamp (confidential|draft|paid|approved|copy|void, required); color (default per stamp); pages | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/pdf/watermark`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pdf/watermark' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@report.pdf' \
  -F 'text=CONFIDENTIAL' \
  -F 'color=ff0000' \
  -F 'opacity=0.3' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('report.pdf'), 'report.pdf');
fd.append('text', 'CONFIDENTIAL');
fd.append('color', 'ff0000');
fd.append('opacity', '0.3');
const r = await fetch('https://api.freedailypro.com/v1/pdf/watermark', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pdf/watermark',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('report.pdf','rb'))], data={"text": "CONFIDENTIAL", "color": "ff0000", "opacity": "0.3"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 application/pdf
```

**Doc text (for listings.yaml / copy.md)**
- Title: PDF Watermark API – Text Stamp with Color & Opacity
- One-liner: PDF Watermark API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: PDF Watermark API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/pdf-watermark. Each task is its own endpoint, so you call exactly the option you need (Text watermark; Image / logo watermark; Status stamp (CONFIDENTIAL/DRAFT/PAID…)). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: pdf watermark, watermark pdf, stamp pdf, confidential stamp
- Category: Data

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


## Source
owner
