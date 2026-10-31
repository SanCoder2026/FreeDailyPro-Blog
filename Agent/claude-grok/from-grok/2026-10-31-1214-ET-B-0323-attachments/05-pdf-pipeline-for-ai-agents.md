---
title: "PDF pipeline for AI agents: merge, redact, fill forms via MCP"
meta_description: "Wire FreeDailyPro PDF tools into an agent: merge, split, compress, watermark, redact, and fillable forms — with real paths and privacy notes."
---

# PDF pipeline for AI agents: merge, redact, fill forms via MCP

Agents that "help with documents" usually die on file I/O. FreeDailyPro's PDF surface is built for that gap.

## Core routes

| Job | Path |
|-----|------|
| Merge | `POST /v1/pdf/merge` |
| Split | `POST /v1/pdf/split` |
| Compress | `POST /v1/pdf/compress/balanced` (also aggressive/extreme/size/bw) |
| Watermark | `POST /v1/pdf/watermark` |
| Flatten | `POST /v1/pdf/flatten` |
| Redact | `POST /v1/redact-pdf` |
| Parse fields | `POST /v1/fillable-forms/parse` |
| Fill form | `POST /v1/fillable-forms/fill` |

Full list: [OpenAPI](https://api.freedailypro.com/openapi.json) · product page: [developers](https://www.freedailypro.com/developers)

## Agent pattern

1. **Parse** before fill — field names come from the PDF, not your guess.
2. **Redact** with fractional boxes `0–1` relative to page width/height.
3. **Compress** after merge/watermark if emailing.
4. Prefer **MCP** for orchestration; **REST** for batch jobs.

### Redact example

```bash
curl -X POST https://api.freedailypro.com/v1/redact-pdf \
  -H "X-API-Key: YOUR_API_KEY" \
  -F "file=@document.pdf" \
  -F 'boxes={"0":[{"x":0.1,"y":0.1,"w":0.5,"h":0.1}]}' \
  -o redacted.pdf
```

### Fill example

```bash
curl -X POST https://api.freedailypro.com/v1/fillable-forms/fill \
  -H "X-API-Key: YOUR_API_KEY" \
  -F "file=@form.pdf" \
  -F 'values={"fullName":"Jane Doe"}' \
  -o filled.pdf
```

## MCP prompt seed

```
You are a PDF pipeline agent with FreeDailyPro tools.
Never invent OCR. Coordinates for redact are fractional.
After fillable-forms/parse, fill only real field names.
```

Working scripts: growth pack `02-demo-agents/01-pdf-processing-agent/`.

## Honest limits

No OCR, no Word/Excel conversion in the API. Files are processed in memory and not stored.

## CTA

[https://www.freedailypro.com/developers](https://www.freedailypro.com/developers)
