Sent: 2026-10-30 08:45 AM ET
# B-0098 /v1/redact-pdf erases text outside the redaction box (rasterizes the page)
Priority: **P1**      Estimated effort: 2–4 h      Source: owner

**P1 because:** this is a live, earning API, and it silently destroys text *outside* the redaction box. It returns 200, so callers don't find out until a customer opens the file.

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Redaction has to be trustworthy in both directions. Whatever is inside the box must be gone for good, and nothing outside the box may change. Per Rule 1, this endpoint should match or beat the best redaction tools (Adobe Acrobat, PyMuPDF `apply_redactions`, ApyHub and other redact APIs), because we want to promote PDF redaction to developers.

## Why / evidence
- Live call on 2026-10-30 at 8:42 AM ET returned **HTTP 200**, 30,031 B, 0.40 s.
- The output PDF is a single 1786×2526 JPEG image per page (`pdfimages -list`), so the page was rasterized.
- `pdftotext` on the output returns **nothing**.
- The un-redacted line "Total: 42.00" is **gone from the render** as well. It was probably never drawn, because the input uses the non-embedded base-14 Helvetica font and the rasterizer seems to have no substitute.
- That means we are losing text and fonts, the output isn't searchable, and the file grows from 1.4 KB to 30 KB.
- I've held the endpoint back from community promotion until this is fixed.

## Reproduction
- **Input:** `Agent/claude-grok/from-grok/assets/B-0098/test-input.pdf`
  - Letter-size page, ReportLab, Helvetica (not embedded).
  - Line 1, at x=50, baseline y=742 from the bottom: "Customer SSN: 123-45-6789".
  - Line 2, at x=50, baseline y=700: "Total: 42.00".
- **Request:**
```bash
curl -s -o redacted.pdf -w "%{http_code}\n" \
  -H "X-API-Key: $FDP_API_KEY" \
  -F file=@Agent/claude-grok/from-grok/assets/B-0098/test-input.pdf \
  -F 'boxes={"1":[{"x":45,"y":88,"width":220,"height":18}]}' \
  https://api.freedailypro.com/v1/redact-pdf
```
  The box is in points from the top-left corner, per the spec. It covers only the SSN line.
- **Observed:** `Agent/claude-grok/from-grok/assets/B-0098/observed-output.pdf` and `Agent/claude-grok/from-grok/assets/B-0098/after-render.png`. The bar is drawn, every other piece of text is missing, and nothing can be extracted.
- **Before:** `Agent/claude-grok/from-grok/assets/B-0098/before-render.png`

## Outcomes / expected
1. **True vector redaction.**
   - Remove only the content inside each box: text glyphs, image pixels and vector paths.
   - Remove it from the underlying content stream too, including hidden layers, annotations, form fields and metadata where they overlap the box, so it can't be recovered.
   - Draw an opaque fill over the box.
2. **Everything outside the boxes stays exactly as it was:**
   - Text remains selectable and extractable.
   - Fonts stay as they are, or get embedded. Nothing goes missing.
   - No rasterization.
   - The file size stays close to the original's.
3. **Invalid input gets a 4xx with a clear message.** Cases:
   - The box is outside the page bounds.
   - Width or height is zero or negative.
   - The page index doesn't exist or isn't an integer.
   - The `boxes` JSON is malformed or missing.
   - The file isn't a PDF, or is encrypted.
4. The spec and MCP tool description should state the coordinate system and what "removed" guarantees.

## Acceptance tests
- Diff `pdftotext` before and after: the only lines lost are the redacted strings. "Total: 42.00" is still there.
- The redacted string "123-45-6789" can't be extracted with any of these:
  - `pdftotext`
  - `qpdf --qdf` followed by grep
  - a PyMuPDF `get_text` call
  - the raw streams
- Render diff (pdftoppm 100 dpi): pixels outside the boxes are essentially identical. Within antialiasing tolerance is fine.
- `pdfimages -list` adds no full-page image, and `pdffonts` shows no lost fonts.
- Each invalid case in item 3 above returns a 4xx with its message.
- Run regressions on:
  - a multi-page PDF
  - a PDF with an embedded image under the box
  - a vector path under the box
  - a rotated page
  - a CropBox that differs from the MediaBox
- **Benchmark (Rule 1):** run the same file through PyMuPDF `apply_redactions` and at least one competitor redact API (ApyHub or similar). Report text survival, unrecoverability, size and latency side by side. We should be at least on par with them.

## Suggested direction (interpret freely)
PyMuPDF `add_redact_annot` + `apply_redactions(images=PDF_REDACT_IMAGE_PIXELS)` has proven itself here. Figure out why the current path rasterizes. If rasterizing was meant as the "safe" option, keep it only as an explicit opt-in `mode=raster` that embeds fonts properly.

## Constraints
- Keep the request shape backward compatible: `file`, `boxes`, and the same coordinates.
- Metering is unchanged.
- Don't log file contents.
- Don't claim "unrecoverable" anywhere until the tests above pass.

Source: owner
