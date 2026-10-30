# B-0040b Per-tool task-API spec, tools 11–20 (appendix to B-0039)

**Priority:** P1 (read with B-0039; fixes marked P0 there come first)
**Estimated effort:** reference document; build effort is sized in B-0039

**How to work with us:** you're the implementation partner, not an order-taker. This is our best reading of each tool from its live page and live read-only API calls on Oct 29 2026. Inspect the real handlers before building: if the code already supports something we marked missing, or a param name differs, the code wins. Challenge any endpoint you think is not worth it.

Legend: **exists** = live and works as listed · **exists – fix/extend** = live, needs a bug fix or new params · **NEW** = to build. Weight = billing units per call (B-0039 pricing). Auth everywhere: header `X-API-Key` (RapidAPI: `X-RapidAPI-Key` via proxy). Base: `https://api.freedailypro.com`. Full endpoint list: `2026-10-29-B-0040-task-endpoints.csv`. listings.yaml entries: `2026-10-29-B-0040-listings-snippet.yaml`.

## 11. PDF Split API – Split by Page Ranges
Site tool: https://www.freedailypro.com/tool/split-pdf · Category: Data · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Ranges; 'Every page' button
- Split into separate files (ZIP) OR combine ranges into one (reorder/drop pages)

**Gap vs current API (live-tested read-only):**
- **BUG:** `ranges=1;2-3` (two outputs) returns only the FIRST file (`split_1.pdf`, 1 page). The second output is lost. Multi-file split is effectively broken via API.
- Every-page and every-N-pages modes missing (UI has every page).

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/pdf/split` | Split PDF by ranges | multipart | file (≤20 MB); ranges (required; ';' separates outputs, ',' joins); combineIntoOne (bool,false) | FIX: application/zip (split_1.pdf…split_n.pdf) when >1 output; application/pdf when 1. Header X-Output-Count. | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/pdf/split/every-page` | Split PDF into single pages | multipart | file | application/zip | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/pdf/split/every` | Split PDF every N pages | multipart | file; n (int ≥1, required) | application/zip | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| exists | `POST /v1/pdf/extract` | Extract pages into one PDF | multipart | file; pages (required, e.g. 1,3-5,8; order kept) | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/pdf/split`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pdf/split' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@doc.pdf' \
  -F 'ranges=1;2-3' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('doc.pdf'), 'doc.pdf');
fd.append('ranges', '1;2-3');
const r = await fetch('https://api.freedailypro.com/v1/pdf/split', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pdf/split',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('doc.pdf','rb'))], data={"ranges": "1;2-3"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
TODAY: 200 application/pdf split_1.pdf (1 page) — 2nd output lost. AFTER FIX: 200 application/zip
```
**Proposed (after build): `POST /v1/pdf/split/every-page`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pdf/split/every-page' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@doc.pdf' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('doc.pdf'), 'doc.pdf');
const r = await fetch('https://api.freedailypro.com/v1/pdf/split/every-page', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pdf/split/every-page',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('doc.pdf','rb'))], data={}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 application/zip (page_1.pdf … page_n.pdf)
```

**Doc text (for listings.yaml / copy.md)**
- Title: PDF Split API – Split by Page Ranges
- One-liner: PDF Split API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: PDF Split API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/split-pdf. Each task is its own endpoint, so you call exactly the option you need (Split PDF by ranges; Split PDF into single pages; Split PDF every N pages; Extract pages into one PDF). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: pdf split, split pdf, extract pages, pdf pages
- Category: Data

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 12. Markdown to PowerPoint API – Generate PPTX
Site tool: https://www.freedailypro.com/tool/markdown-to-powerpoint · Category: Data · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Markdown or Plain outline
- Themes: Clean, Dark, Corporate, Warm, Minimal, Your brand (colour + 2 fonts)
- Warnings for skipped web images / overflow

**Gap vs current API (live-tested read-only):**
- Full parity (mode, theme, brand). Only gap: UI warnings (skipped images, overflow) aren't surfaced in the API response.

**Full UI workflow completable via API?** Today: **yes**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists | `POST /v1/pptx/from-markdown` | Markdown → PPTX | json|multipart | markdown (≤1,000,000 chars) or file (.md ≤10 MB); mode (markdown|outline, markdown); theme (clean|dark|corporate|warm|minimal, clean); brand ({color,headingFont,bodyFont,dark}) | application/vnd.openxmlformats-officedocument.presentationml.presentation; ADD header X-Warnings (JSON array) + X-Slide-Count | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/pptx/from-markdown`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pptx/from-markdown' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"markdown":"# Q4 Plan\nTeam\n## Goals\n- Grow\n- Ship","theme":"dark"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/pptx/from-markdown', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"markdown":"# Q4 Plan\nTeam\n## Goals\n- Grow\n- Ship","theme":"dark"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pptx/from-markdown',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"markdown":"# Q4 Plan\nTeam\n## Goals\n- Grow\n- Ship","theme":"dark"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
200 application/vnd.openxmlformats-officedocument.presentationml.presentation (60,016 bytes, 0.25 s)
```

**Doc text (for listings.yaml / copy.md)**
- Title: Markdown to PowerPoint API – Generate PPTX
- One-liner: Markdown to PowerPoint API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: Markdown to PowerPoint API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/markdown-to-powerpoint. Each task is its own endpoint, so you call exactly the option you need (Markdown → PPTX). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: markdown to pptx, pptx, powerpoint, slides, presentation
- Category: Data

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 13. JSON to PowerPoint API – PPTX from Data
Site tool: https://www.freedailypro.com/tool/excel-to-powerpoint · Category: Data · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Excel to PowerPoint: .xlsx/.xls/CSV ≤25 MB, tick sheets, rows per slide, max columns, header row, look

**Gap vs current API (live-tested read-only):**
- JSON and CSV exist and work. Excel (.xlsx/.xls) input, sheet choice and maxColumns are UI-only.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists | `POST /v1/pptx/from-json` | JSON slides → PPTX | json | slides (array 1–200: {title,subtitle,layout,bullets,numbered,text,table,notes…}, required); title; theme; brand | pptx | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| exists – fix/extend | `POST /v1/pptx/from-csv` | CSV → PPTX table slides | json|multipart | csv or file (≤10 MB); title (Data); rowsPerSlide (1–40, 12); header (true); titleSlide (true); delimiter (auto); theme; brand; ADD maxColumns (1–12, 8) | pptx | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/pptx/from-excel` | Excel → PPTX table slides | multipart | file (.xlsx/.xls ≤25 MB, required); sheets (JSON array of names or 'all', first visible); rowsPerSlide; maxColumns; header; titleSlide; theme; brand | pptx + X-Warnings (hidden sheets skipped, columns cut) | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/pptx/from-json`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pptx/from-json' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"slides":[{"title":"Hello","bullets":["a","b"]}]}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/pptx/from-json', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"slides":[{"title":"Hello","bullets":["a","b"]}]})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pptx/from-json',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"slides":[{"title":"Hello","bullets":["a","b"]}]}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
200 pptx (53,940 bytes, 0.34 s)
```
**Proposed (after build): `POST /v1/pptx/from-excel`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/pptx/from-excel' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@sales.xlsx' \
  -F 'sheets=["Q3"]' \
  -F 'rowsPerSlide=12' \
  -F 'theme=corporate' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('sales.xlsx'), 'sales.xlsx');
fd.append('sheets', '["Q3"]');
fd.append('rowsPerSlide', '12');
fd.append('theme', 'corporate');
const r = await fetch('https://api.freedailypro.com/v1/pptx/from-excel', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/pptx/from-excel',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('sales.xlsx','rb'))], data={"sheets": "[\"Q3\"]", "rowsPerSlide": "12", "theme": "corporate"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 pptx
```

**Doc text (for listings.yaml / copy.md)**
- Title: JSON to PowerPoint API – PPTX from Data
- One-liner: JSON to PowerPoint API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: JSON to PowerPoint API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/excel-to-powerpoint. Each task is its own endpoint, so you call exactly the option you need (JSON slides → PPTX; CSV → PPTX table slides; Excel → PPTX table slides). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: json to pptx, csv to pptx, excel to powerpoint, pptx generator, report automation
- Category: Data

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 14. Image Resize API – JPG, PNG, WebP
Site tool: https://www.freedailypro.com/tool/resize-crop · Category: Video, Images · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Resize: width/height, Maintain aspect ratio (default on), fit cover/contain/fill/inside/outside
- Crop: drag a rectangle
- HEIC/AVIF/WebP inputs (camera)

**Gap vs current API (live-tested read-only):**
- /image/resize needs BOTH width and height, PNG/JPEG only, no fit (sending fit=cover is ignored), no aspect lock.
- Crop is UI-only. /image/convert already has width/height/fit — so resize is the weaker sibling.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/image/resize` | Resize image | multipart | file (≤15 MB; ADD webp/avif/heic/gif input); width (1–16384) and/or height (one is enough → keep aspect); ADD fit (inside|contain|cover|fill|outside, inside); withoutEnlargement (bool,false); background (hex, for contain); format (png|jpeg|webp|avif, input) | image/* | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/image/crop` | Crop image | multipart | file; x,y,width,height (px, required) OR aspect (e.g. 1:1, 16:9) + gravity (center|north|south|east|west|attention, center); format | image/* | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/image/thumbnail` | Square/fixed thumbnail — Keyword alias 'thumbnail api'. | multipart | file; size (16–2048, 256); fit (cover); format (webp) | image/* | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/image/resize`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/image/resize' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@photo.png' \
  -F 'width=300' \
  -F 'height=300' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('photo.png'), 'photo.png');
fd.append('width', '300');
fd.append('height', '300');
const r = await fetch('https://api.freedailypro.com/v1/image/resize', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/image/resize',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('photo.png','rb'))], data={"width": "300", "height": "300"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 image/png 300×300
```
**Proposed (after build): `POST /v1/image/crop`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/image/crop' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@photo.jpg' \
  -F 'aspect=1:1' \
  -F 'gravity=attention' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('photo.jpg'), 'photo.jpg');
fd.append('aspect', '1:1');
fd.append('gravity', 'attention');
const r = await fetch('https://api.freedailypro.com/v1/image/crop', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/image/crop',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('photo.jpg','rb'))], data={"aspect": "1:1", "gravity": "attention"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 image/jpeg
```

**Doc text (for listings.yaml / copy.md)**
- Title: Image Resize API – JPG, PNG, WebP
- One-liner: Image Resize API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: Image Resize API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/resize-crop. Each task is its own endpoint, so you call exactly the option you need (Resize image; Crop image; Square/fixed thumbnail). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: image resize, resize image, thumbnail, crop image, webp
- Category: Video, Images

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 15. Image Converter API – PNG, JPG, WebP, AVIF
Site tool: https://www.freedailypro.com/tool/convert-image · Category: Video, Images · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Target PNG/JPEG/WebP/AVIF/GIF/BMP/ICO/TIFF; quality 40–100; fill colour; ICO sizes; BMP 24/32
- More: width/height+fit, rotate, mirror, greyscale, auto-orient, strip EXIF, DPI
- Inputs incl. HEIC, SVG

**Gap vs current API (live-tested read-only):**
- Near-full parity (richest endpoint we have).
- Owner pattern applies for SEARCH, not capability: buyers search 'heic to jpg api', 'png to webp api'. Fixed-format aliases make those listings.

**Full UI workflow completable via API?** Today: **yes**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists | `POST /v1/image/convert` | Convert image format | multipart | file (≤15 MB); format (png|jpeg|webp|avif|gif|tiff|bmp|ico, required); quality; backgroundColor; lossless; progressive; chromaSubsampling; pngCompressionLevel; pngPalette; effort; width; height; fit; withoutEnlargement; autoOrient; stripMetadata; grayscale; dpi; rotate; flip; flop; sharpen; blur; sizes; bitDepth; tiffCompression; animated | image/* | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/image/heic-to-jpg` | HEIC → JPG — Alias: fixes format, forwards rest to /image/convert. | multipart | file (HEIC/HEIF); quality (1–100, 90); stripMetadata (true) | image/jpeg | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/image/png-to-jpg` | PNG → JPG — Alias. | multipart | file; quality; backgroundColor (white) | image/jpeg | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/image/to-webp` | Any image → WebP — Alias. | multipart | file; quality (85); lossless | image/webp | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/image/to-ico` | Image → ICO favicon — Alias ('favicon generator api'). | multipart | file; sizes (16,32,48) | image/x-icon | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/image/convert`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/image/convert' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@photo.png' \
  -F 'format=webp' \
  -F 'quality=80' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('photo.png'), 'photo.png');
fd.append('format', 'webp');
fd.append('quality', '80');
const r = await fetch('https://api.freedailypro.com/v1/image/convert', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/image/convert',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('photo.png','rb'))], data={"format": "webp", "quality": "80"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 image/webp
```

**Doc text (for listings.yaml / copy.md)**
- Title: Image Converter API – PNG, JPG, WebP, AVIF
- One-liner: Image Converter API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: Image Converter API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/convert-image. Each task is its own endpoint, so you call exactly the option you need (Convert image format; HEIC → JPG; PNG → JPG; Any image → WebP; Image → ICO favicon). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: image convert, png to jpg, heic to jpg, webp, avif, ico
- Category: Video, Images

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 16. Video to GIF API
Site tool: https://www.freedailypro.com/tool/video-to-gif · Category: Video, Images · Marketplaces: RapidAPI; API.market

**UI options (live page, Oct 29):**
- Start (s), Length (s, ≥0.5, default 5)
- Width 240–800 (480)
- FPS 5–20 (12)
- Speed 0.5–2×
- Play once (no loop)
- Largest file 2/5/8/10 MB

**Gap vs current API (live-tested read-only):**
- API takes the file only. Live test: start/duration/width/fps sent → byte-identical GIF (271,525 B, 480×360, 24 frames) — all options ignored.
- API hard cap ~1.9 MB vs UI 2–10 MB. A caller cannot pick the moment to clip — the core UI workflow.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/video/to-gif` | Video → GIF | multipart | file (≤100 MB; recommend ≤50 MB); ADD start (s ≥0, 0); duration (0.5–20 s, 5); width (240–800, 480); fps (5–20, 12); speed (0.5–2, 1); loop (bool,true); maxSizeMB (2|5|8|10, 2) | image/gif + X-Final-Width, X-Final-Fps (if auto-reduced) | 400 · 401 · 413 · 422 clip too long for maxSize · 429 · 504 >55 s ffmpeg cap | 10 |
| NEW | `POST /v1/video/clip-to-gif` | Clip a moment to GIF (start+duration required) — Task-level alias so the listing says exactly what it does. | multipart | file; start (required); duration (required); width; fps; loop | image/gif | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 10 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/video/to-gif`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/video/to-gif' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@clip.mp4' \
  -F 'start=0.5' \
  -F 'duration=3' \
  -F 'width=320' \
  -F 'fps=10' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('clip.mp4'), 'clip.mp4');
fd.append('start', '0.5');
fd.append('duration', '3');
fd.append('width', '320');
fd.append('fps', '10');
const r = await fetch('https://api.freedailypro.com/v1/video/to-gif', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/video/to-gif',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('clip.mp4','rb'))], data={"start": "0.5", "duration": "3", "width": "320", "fps": "10"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
TODAY: options ignored → 480×360, 24 frames, 271 KB. AFTER FIX: 320 px, 10 fps, 3 s
```

**Doc text (for listings.yaml / copy.md)**
- Title: Video to GIF API
- One-liner: Video to GIF API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: Video to GIF API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/video-to-gif. Each task is its own endpoint, so you call exactly the option you need (Video → GIF; Clip a moment to GIF (start+duration required)). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: video to gif, gif maker, mp4 to gif, animated gif
- Category: Video, Images

**Upload notes:** RapidAPI; API.market. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 17. Audio Converter API – MP3, WAV, OGG
Site tool: https://www.freedailypro.com/tool/audio-converter · Category: Media · Marketplaces: RapidAPI; API.market

**UI options (live page, Oct 29):**
- Output MP3/WAV/OGG/M4A/FLAC
- Quality for lossy: Same as original / High / Standard / Small

**Gap vs current API (live-tested read-only):**
- API: format only. Quality/bitrate not exposed (bitrate=64k ignored; output 41.7 kbps in test).
- Search pattern: buyers search 'wav to mp3 api', 'm4a to mp3'.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/audio/convert` | Convert audio | multipart | file (≤30 MB); format (mp3|wav|ogg|m4a|flac, required); ADD quality (same|high|standard|small, same); bitrateKbps (32–320, overrides quality); sampleRate (8000–48000); channels (1|2) | audio/* | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 5 |
| NEW | `POST /v1/audio/wav-to-mp3` | WAV → MP3 — Alias. | multipart | file; quality | audio/mpeg | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 5 |
| NEW | `POST /v1/audio/m4a-to-mp3` | M4A → MP3 — Alias. | multipart | file; quality | audio/mpeg | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 5 |
| NEW | `POST /v1/audio/to-wav` | Any audio → WAV — Alias. | multipart | file; sampleRate | audio/wav | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 5 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/audio/convert`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/audio/convert' \
  -H "X-API-Key: $FDP_API_KEY" \
  -F 'file=@memo.wav' \
  -F 'format=mp3' \
  -F 'quality=standard' \
  -o result.bin
```
```js
import fs from 'node:fs'; // Node 20+ (fs.openAsBlob)
const fd = new FormData();
fd.append('file', await fs.openAsBlob('memo.wav'), 'memo.wav');
fd.append('format', 'mp3');
fd.append('quality', 'standard');
const r = await fetch('https://api.freedailypro.com/v1/audio/convert', { method: 'POST', headers: { 'X-API-Key': process.env.FDP_API_KEY }, body: fd });
if (!r.ok) throw new Error(await r.text());
await fs.promises.writeFile('result.bin', Buffer.from(await r.arrayBuffer()));
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/audio/convert',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    files=[('file', open('memo.wav','rb'))], data={"format": "mp3", "quality": "standard"}, timeout=120)
r.raise_for_status()
open('result.bin','wb').write(r.content)
```
Response:
```
200 audio/mpeg
```

**Doc text (for listings.yaml / copy.md)**
- Title: Audio Converter API – MP3, WAV, OGG
- One-liner: Audio Converter API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: Audio Converter API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/audio-converter. Each task is its own endpoint, so you call exactly the option you need (Convert audio; WAV → MP3; M4A → MP3; Any audio → WAV). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: audio convert, mp3 converter, wav to mp3, m4a to mp3, flac
- Category: Media

**Upload notes:** RapidAPI; API.market. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 18. EPUB Generator API – Build eBooks
Site tool: https://www.freedailypro.com/tool/epub-maker · Category: Media · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Chapters (title + text)
- Title, subtitle, authors, language, publisher, ISBN, copyright holder/year, description, cover
- Check before you build (warnings)

**Gap vs current API (live-tested read-only):**
- API covers the build but the `chapters[].blocks[].runs[]` schema is heavy for a first call (my first attempt with a simple text block → 400).
- `description` metadata (UI) missing. 'Check before build' is UI-only. No MCP tool for EPUB at all.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/publishing/epub` | Build EPUB (structured) | json | bookTitle (≤300, required); authorNames (array, required); language (BCP-47, required); chapters (1–100, each blocks 1–800, required); subtitle; isbn; eisbn; publisherName; coverImageDataUri (≤15 MB); copyrightHolder; copyrightYear (1500–3000); dedicationBlocks; epigraphBlocks; stableId; watermark; ADD description (≤4000) | application/epub+zip | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| NEW | `POST /v1/publishing/epub/from-markdown` | Markdown → EPUB — The easy first call; most callers have Markdown/text. | json|multipart | markdown or file (.md ≤10 MB, required; '# ' = chapter); bookTitle; authorNames; language; + same optional metadata | application/epub+zip | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| NEW | `POST /v1/publishing/epub/validate` | Check an EPUB build request (no file) | json | same body as /publishing/epub | application/json {result:{ok,errors[],warnings[]}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST MCP: publishing_epub` | Add EPUB tools to MCP — MCP tools/list has no epub tool today (211 tools checked). | — | — | — | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/publishing/epub`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/publishing/epub' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"bookTitle":"Test","authorNames":["A B"],"language":"en","chapters":[{"title":"One","blocks":[{"type":"paragraph","runs":[{"text":"Hi"}]}]}]}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/publishing/epub', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"bookTitle":"Test","authorNames":["A B"],"language":"en","chapters":[{"title":"One","blocks":[{"type":"paragraph","runs":[{"text":"Hi"}]}]}]})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/publishing/epub',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"bookTitle":"Test","authorNames":["A B"],"language":"en","chapters":[{"title":"One","blocks":[{"type":"paragraph","runs":[{"text":"Hi"}]}]}]}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
200 application/epub+zip (6,761 bytes)
```
**Proposed (after build): `POST /v1/publishing/epub/from-markdown`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/publishing/epub/from-markdown' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"bookTitle":"My Guide","authorNames":["Jane Roe"],"language":"en","markdown":"# Chapter 1\nHello\n# Chapter 2\nMore"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/publishing/epub/from-markdown', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"bookTitle":"My Guide","authorNames":["Jane Roe"],"language":"en","markdown":"# Chapter 1\nHello\n# Chapter 2\nMore"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/publishing/epub/from-markdown',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"bookTitle":"My Guide","authorNames":["Jane Roe"],"language":"en","markdown":"# Chapter 1\nHello\n# Chapter 2\nMore"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
200 application/epub+zip
```

**Doc text (for listings.yaml / copy.md)**
- Title: EPUB Generator API – Build eBooks
- One-liner: EPUB Generator API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: EPUB Generator API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/epub-maker. Each task is its own endpoint, so you call exactly the option you need (Build EPUB (structured); Markdown → EPUB; Check an EPUB build request (no file)). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: epub, ebook, epub generator, kdp, self publishing
- Category: Media

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 19. ISBN Validator & Converter API – ISBN-10/13
Site tool: https://www.freedailypro.com/tool/isbn-checker · Category: Data · Marketplaces: RapidAPI; API.market

**UI options (live page, Oct 29):**
- Single ISBN
- Bulk list (one per line) → table → CSV

**Gap vs current API (live-tested read-only):**
- Single works and is rich. Bulk + CSV is UI-only.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists | `POST /v1/publishing/isbn` | Validate/convert one ISBN | json | isbn (string ≤40, required) | application/json {result:{kind,valid,expectedCheck,isbn10,isbn13,isbn10Hyphenated,isbn13Hyphenated,groupName,barcodeDigits}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/publishing/isbn/bulk` | Validate ISBNs in bulk — Bill as 1 call per 100 ISBNs (weight noted). | json | isbns (array 1–1000, required); format (json|csv, json) | application/json {result:{items:[…],validCount,invalidCount}} | text/csv | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/publishing/isbn`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/publishing/isbn' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"isbn":"0306406152"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/publishing/isbn', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"isbn":"0306406152"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/publishing/isbn',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"isbn":"0306406152"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"result":{"input":"0306406152","kind":"isbn10","wellFormed":true,"valid":true,"expectedCheck":"2","isbn10":"0306406152","isbn13":"9780306406157","isbn10Hyphenated":"0-306-40615-2","isbn13Hyphenated":"978-0-306-40615-7","groupName":"English language","barcodeDigits":"9780306406157"}}
```
**Proposed (after build): `POST /v1/publishing/isbn/bulk`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/publishing/isbn/bulk' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"isbns":["0306406152","9780306406157","123"],"format":"json"}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/publishing/isbn/bulk', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"isbns":["0306406152","9780306406157","123"],"format":"json"})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/publishing/isbn/bulk',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"isbns":["0306406152","9780306406157","123"],"format":"json"}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"result":{"items":[…],"validCount":2,"invalidCount":1}}
```

**Doc text (for listings.yaml / copy.md)**
- Title: ISBN Validator & Converter API – ISBN-10/13
- One-liner: ISBN Validator & Converter API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: ISBN Validator & Converter API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/isbn-checker. Each task is its own endpoint, so you call exactly the option you need (Validate/convert one ISBN; Validate ISBNs in bulk). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: isbn, isbn validator, isbn-13, isbn converter, books
- Category: Data

**Upload notes:** RapidAPI; API.market. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


---

## 20. Invoice Totals & Receipt Generator API
Site tool: https://www.freedailypro.com/tool/invoice-generator · Category: Business Software · Marketplaces: RapidAPI; API.market; Postman

**UI options (live page, Oct 29):**
- Invoice: business, client, addresses, tax ID, number, date, terms (Due on receipt/Net 15/30/60/custom), due date, currency (10), discount, tax %, tax label, line items, shipping, amount paid, notes, signature line → PDF
- Receipt: business, customer, number, date, payment method, items, currency, tax, tax label, refund (negative), received-by line → PDF

**Gap vs current API (live-tested read-only):**
- API returns totals JSON only (invoice-totals; receipt echoes lines + totals). **No PDF** — the actual product the UI makes. Listing title 'Generator' would over-claim.
- No currency, shipping, amount paid/balance due, terms/due date, notes.

**Full UI workflow completable via API?** Today: **NO**. After this spec: **yes**.

| Status | Method + path | Task | Body | Params (type, default, limits) | Response | Errors | Weight |
|---|---|---|---|---|---|---|---|
| exists – fix/extend | `POST /v1/business/invoice-totals` | Invoice totals (JSON) | json | lines ([{description,qty,unitPrice}], required); taxPct; discountPct; ADD shipping; amountPaid; currency | application/json {result:{subtotal,discount,tax, ADD shipping,total,amountPaid,balanceDue,currency}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| exists – fix/extend | `POST /v1/business/receipt` | Receipt totals (JSON) — Align line field name with invoice (accept description AND name). | json | merchant (required); lines ([{name,qty,unitPrice}], required); taxPct; date | application/json {result:{merchant,date,lines,subtotal,tax,total}} | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 1 |
| NEW | `POST /v1/business/invoice/pdf` | Invoice PDF generator | json | businessName, clientName (required); businessAddress; clientAddress; taxId; invoiceNumber; date; terms (due_on_receipt|net15|net30|net60|custom); dueDate; currency (USD,EUR,GBP,INR,CAD,AUD,JPY,SGD,AED,ZAR); discountPct; taxPct; taxLabel (Tax); lines (1–200, required); shipping; amountPaid; notes (≤2000); signatureLine (bool) | application/pdf (+ ?format=json returns totals) | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |
| NEW | `POST /v1/business/receipt/pdf` | Receipt PDF generator | json | businessName, lines (required); customerName; receiptNumber; date; paymentMethod (cash|card|bank|upi|other); currency; taxPct; taxLabel; refund (bool); receivedBySignature (bool) | application/pdf | 400 bad input · 401 key · 413 too large · 422 unprocessable · 429 quota | 2 |

**Code examples**

**Live-captured Oct 29 2026: `POST /v1/business/invoice-totals`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/business/invoice-totals' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"lines":[{"description":"Design","qty":2,"unitPrice":150}],"taxPct":8,"discountPct":10}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/business/invoice-totals', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"lines":[{"description":"Design","qty":2,"unitPrice":150}],"taxPct":8,"discountPct":10})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/business/invoice-totals',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"lines":[{"description":"Design","qty":2,"unitPrice":150}],"taxPct":8,"discountPct":10}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
{"tool":"Invoice totals ...","result":{"subtotal":300,"discount":30,"tax":21.6,"total":291.6}}
```
**Proposed (after build): `POST /v1/business/invoice/pdf`**

```bash
curl -X POST 'https://api.freedailypro.com/v1/business/invoice/pdf' \
  -H "X-API-Key: $FDP_API_KEY" -H 'Content-Type: application/json' \
  -d '{"businessName":"Studio K","clientName":"Acme Inc","currency":"USD","terms":"net30","taxPct":8,"lines":[{"description":"Logo design","qty":1,"unitPrice":450}],"amountPaid":100}'
```
```js
const r = await fetch('https://api.freedailypro.com/v1/business/invoice/pdf', {
  method: 'POST',
  headers: { 'X-API-Key': process.env.FDP_API_KEY, 'Content-Type': 'application/json' },
  body: JSON.stringify({"businessName":"Studio K","clientName":"Acme Inc","currency":"USD","terms":"net30","taxPct":8,"lines":[{"description":"Logo design","qty":1,"unitPrice":450}],"amountPaid":100})
});
const data = await r.json(); // binary outputs: await r.arrayBuffer()
```
```python
import os, requests
r = requests.post('https://api.freedailypro.com/v1/business/invoice/pdf',
    headers={'X-API-Key': os.environ['FDP_API_KEY']},
    json={"businessName":"Studio K","clientName":"Acme Inc","currency":"USD","terms":"net30","taxPct":8,"lines":[{"description":"Logo design","qty":1,"unitPrice":450}],"amountPaid":100}, timeout=60)
r.raise_for_status()
print(r.json())
```
Response:
```
200 application/pdf (X-Total: 486.00, X-Balance-Due: 386.00)
```

**Doc text (for listings.yaml / copy.md)**
- Title: Invoice Totals & Receipt Generator API  ⚠ say "Totals" until the PDF endpoints are live
- One-liner: Invoice Totals & Receipt Generator API — one POST, results in under a second for typical files, processed in memory and never stored.
- Description: Invoice Totals & Receipt Generator API by FreeDailyPro, the same engine as the free web tool at freedailypro.com/tool/invoice-generator. Each task is its own endpoint, so you call exactly the option you need (Invoice totals (JSON); Receipt totals (JSON); Invoice PDF generator; Receipt PDF generator). Clear 400 messages tell you what to fix. Free Basic plan, then flat monthly tiers.
- Tags: invoice generator, invoice pdf, receipt, receipt generator, tax
- Category: Business Software

**Upload notes:** RapidAPI; API.market; Postman. One listing per row of the top-100 CSV; task endpoints of this tool are the operations inside that listing, and the alias endpoints marked "NEW … Alias" may become their own wave-2 listings if search data supports it.


## Source
owner
