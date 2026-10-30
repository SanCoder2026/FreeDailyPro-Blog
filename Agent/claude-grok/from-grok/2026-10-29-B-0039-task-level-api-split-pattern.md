# B-0039 Task-level API split: one endpoint per UI option, so every tool can finish its job via API (addendum to B-0028/B-0030)

**Priority:** P1. Three items inside are **P0 must-do before the wave-1 launch** (B-0030 gate).
**Estimated effort:** ~2 nights for P0 + P1 fixes, ~3–4 nights for all NEW endpoints. Split it across nights however you think is best and report per item.

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
A buyer who finds "Video to GIF API" or "PDF Split API" on RapidAPI must be able to do with one or two calls **everything the web tool does**, not a cut-down version. We get there the way we already did for Compress PDF. Every meaningful UI option or mode becomes either its own task endpoint (`/v1/pdf/compress/balanced|aggressive|extreme|size`) or an explicit, documented param. Each endpoint does one job, has a self-explanatory name, works on the first call and returns exactly what the UI user downloads.

## Why (owner, Oct 29, verbatim gist)
"In UI for complex or multitool or multistep tools we can drive the user manually, but in API there are very few options, so complex tools struggle to finish the full task through API. We have to split the API to do a certain task … for compress PDF we created 4 APIs for different levels. You have to understand how the existing tool works … be very thorough on coding, documentation, example, uploading guide, pricing."

Evidence: on Oct 29 we read all 20 wave-1 tool pages and made read-only live calls with small sample files (details in B-0040a/b). Today **only 5 of 20** can finish the full UI workflow via API: Compress PDF, JWT Decoder, UUID, Markdown→PPTX and Image Convert. The other 15 lose a core option. Several silently ignore params, so a marketplace tester sees a success while getting the wrong result. That is the worst first impression on RapidAPI and it gets us bad reviews.

## Outcomes
1. **P0 bugs fixed (before any wave-1 listing goes public):**
   - **Split PDF multi-output.** `POST /v1/pdf/split` with `ranges=1;2-3` returns only `split_1.pdf` (1 page) and the second output is lost. Return `application/zip` when there is more than one output.
   - **Silently ignored params.** Unknown or unsupported fields must return a 400 that names them, not a 200. Seen on `/v1/security/qr` (format/size/color), `/v1/video/to-gif` (start/duration/width/fps gave a byte-identical GIF), `/v1/pdf/merge` (pages), `/v1/image/resize` (fit) and `/v1/audio/convert` (bitrate). Either support them (preferred, see B-0040) or reject them.
   - **No false titles.** Don't publish "QR Code Generator API – PNG & SVG" until PNG exists (API returns SVG-in-JSON only today). Don't call 20 a "Generator" (PDF) until `/v1/business/invoice/pdf` exists. Until then use "QR Code Generator API – SVG" and "Invoice Totals API".
2. **Every wave-1 tool reaches UI parity via API** using the endpoint table in B-0040a/b: 20 tools, 63 endpoints (12 exist as-is, 16 exist and need fixes or extra params, 35 new, of which about 14 are thin keyword aliases).
3. **Consistent contract on every endpoint:**
   - JSON in → `{tool, result}`; file in → file out with `Content-Disposition` filename.
   - Errors are `{error, details}`, using 400/401/405/413/422/429 as today.
   - Useful result headers (`X-Page-Count`, `X-Output-Count`, `X-Warnings`, `X-Original-Bytes`/`X-Result-Bytes`/`X-Kept-Original`).
   - Multipart and (where the endpoint takes files) JSON+base64 both accepted, as the pptx family already does.
4. **Each new or changed endpoint is in `/openapi.json`** with summary, description, param limits/defaults/enums, a real example and the response schema. It also appears in MCP `tools/list`: today there's no EPUB tool, and the new task tools must follow the existing `pdf_compress_*` naming. The B-0028 generator then picks them up with zero hand work (snippet: `2026-10-29-B-0040-listings-snippet.yaml`).
5. **Chained workflows documented** where one call can't do it all:
   - Redact: `/pdf/redact/find` → review boxes → `/redact-pdf`.
   - Split/Extract → Merge → Compress/size.
   - Image crop → convert.
   - EPUB validate → build.

## Pattern rules (how to decide: new endpoint vs param)
- **Split into its own endpoint when the option changes the job or output type.** That covers a different algorithm or quality tier (compress levels), a different output kind (QR PNG vs SVG, invoice PDF vs totals JSON, split ZIP vs single file), a different input kind (Excel vs CSV, file vs text hash) or a different user intent (wifi QR vs vCard QR, verify vs generate).
- **Keep it as a param when it fine-tunes the same job:** colour, opacity, width, page range, quality.
- **Add keyword aliases** (`/image/heic-to-jpg`, `/audio/wav-to-mp3`, `/finance/emi`, `/qr/wifi`) when buyers search the specific task. An alias is a thin wrapper that fixes one param and forwards to the main handler, with no duplicate logic. Aliases are the cheapest way to get more ranked listing titles later (wave 2).
- **Defaults equal the UI defaults** (listed per endpoint in B-0040). A call with only the required fields must give the same result as the UI with nothing changed.
- **Limits equal the UI limits** unless server cost forces lower. Video→GIF UI allows a 2–10 MB GIF while the API caps it at ~1.9 MB, so raise the cap or document the difference.
- **Name of the task = name of the endpoint = MCP tool name = listing operation name.**

## Pricing (owner rule: keep default tiers, no increases until traction)
- Tiers unchanged on every listing: **Basic free 20,000 units/mo · Pro $24 / 200,000 · Ultra $69 / 750,000 · Mega $129 / 2,000,000** (RapidAPI plan templates as they exist; the image/media free tier stays ≥500 calls per B-0030).
- **Weighting instead of price increases:** heavy endpoints consume more units per call, set per endpoint in RapidAPI ("objects"/endpoint billing) and noted in copy.md. Proposed weights (column `weight_units` in the CSV):
  - JSON calculators/generators: 1.
  - PDF edit (merge/split/watermark/extract): 1.
  - Redact and all compress variants, EPUB and invoice/receipt PDF: 2.
  - File hashing: 2.
  - Audio: 5.
  - Video→GIF: 10.
  - ISBN bulk: 1 per 100 ISBNs.
- Confirm against our real per-call server cost (Railway CPU-seconds for ffmpeg/ghostscript). If a weight can't be set on a marketplace, keep 1 and note it in the report. Do **not** change prices.

## Marketplace upload guide (generator output → each console)
Order: fix P0 → deploy → `gen-listings` → validate → publish. Every listing's example responses must come from a live call after deploy.
1. **RapidAPI (top priority)**
   - Import the per-listing trimmed OpenAPI (B-0028) via the Platform API/PAPI if B-0029 says yes, otherwise Studio → Add API → Import OpenAPI.
   - Set category, tags and title from listings.yaml. Base URL is ours, auth via the RapidAPI proxy secret as on the existing listings.
   - Fill **multipart example bodies** for every file endpoint. The broken sample code is "Traction F1", so verify the generated Node/Python/cURL snippet actually returns 200 in the Studio test console.
   - Attach the existing plan template and set the endpoint weights.
   - Make it public, then run a test subscription call per endpoint and record the status in your report.
2. **Postman:** the generator produces one collection per listing (B-0031). Include saved example responses, environment var `FDP_API_KEY` (name only) and a folder per task endpoint. Publish to the existing public workspace.
3. **API.market:** no upload API, so the generator writes `copy.md` (title ≤60 chars, description, tags, pricing note, example request/response). The owner pastes it, so list it under **Owner actions**. Keep pricing at the default product plans.
4. **ApyHub:** owner says ApyHub already segregates internally, so **no new listings**. Only make sure the new task endpoints are in `/openapi.json` so their internal sync sees them. Any ApyHub spec re-upload is an **Owner action**.
5. **/developers pages (B-0033):** one page per listing generated from the same source, with the same examples. Remove any claim that the live API doesn't back.

## Acceptance tests (run against production after deploy; report pass/fail per line)
1. `POST /v1/pdf/split` with `ranges=1;2-3` on a 3-page PDF → `application/zip` holding 2 PDFs (1 page and 2 pages). `ranges=2` → single PDF.
2. Unknown field on any wave-1 endpoint → 400 naming the field (spot-check qr, to-gif, merge, resize, audio).
3. `POST /v1/video/to-gif` with `start=0.5&duration=2&width=240&fps=8` → GIF is 240 px wide, ~16 frames, and differs from the default call.
4. `POST /v1/qr/png` → `image/png` that decodes (zbar or similar) back to the input. `/v1/qr/wifi` decodes to `WIFI:T:WPA;S:…;P:…;;`.
5. `POST /v1/pdf/merge` with `pages=["1-2","1"]` on 3-page + 1-page → 3 pages.
6. `POST /v1/pdf/redact/search` with `terms=["John Doe"]` on a text PDF → the term is no longer extractable (pdftotext), `X-Redaction-Count ≥1`, and unmarked pages are still text.
7. `POST /v1/security/hash/file` on a known file → its sha256 equals `sha256sum`. `/hash/verify` with that value → `match:true, algorithm:"sha256"`.
8. `POST /v1/business/invoice/pdf` → a valid PDF whose text contains client name, total and balance due, matching `/invoice-totals` math.
9. `POST /v1/publishing/epub/from-markdown` → EPUB passes epubcheck (or our epub-checker) with 0 errors.
10. Each NEW endpoint appears in `/openapi.json` and MCP `tools/list`, and `gen-listings` builds without errors (B-0028 check "operation exists in live spec").
11. A call with only required fields equals the UI default output (spot-check compress/balanced, image/convert, audio/convert).
12. No regression: all endpoints in the CSV marked "exists" still return 200 with the same sample as before.

## Suggested direction (interpret freely)
- Build aliases as route config (one table of `alias → handler + fixed params`) so wave 2 adds them by data, not code.
- Reuse the UI's own client-side logic where it lives in shared modules (redact search, QR builders, invoice PDF layout) instead of writing a second version.
- Do P0 first, then the high-demand gaps in B-0040 rank order: QR PNG, Split, Video→GIF params, Invoice PDF, Redact search, Hash file/verify, Merge pages, Image resize/crop, Audio quality, Excel→PPTX, EPUB from-markdown, the rest.

## Not in scope / do not decide
- Price changes.
- Deleting or privatising the legacy RapidAPI listing (owner decision pending).
- New ApyHub listings.
- Publishing anything before the P0 items pass.
- JWT signature verification is optional (P3); skip it if you see any security concern.
- `/v1/pdf/merge/urls` (URL fetching) only with a strict SSRF guard; skip it if in doubt.

## Owner decisions needed
None to build. The owner pastes the API.market copy and any ApyHub re-upload (Owner actions).

Appendix: `2026-10-29-B-0040a-per-tool-spec-tools-01-10.md`, `2026-10-29-B-0040b-per-tool-spec-tools-11-20.md`, `2026-10-29-B-0040-task-endpoints.csv`, `2026-10-29-B-0040-listings-snippet.yaml`.

## Source
owner
