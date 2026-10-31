---
title: "FreeDailyPro API quickstart: your first call in 60 seconds"
meta_description: "Hit FreeDailyPro's live API with or without a key — word-count in seconds, then authenticate for PDF and PPTX."
---

# FreeDailyPro API quickstart: your first call in 60 seconds

Base URL: `https://api.freedailypro.com`  
Auth: `X-API-Key` (when required)  
Surface: 215+ REST endpoints · 211+ MCP tools at `https://api.freedailypro.com/mcp`

## 0–20s — no key

These three routes work without a key (IP rate-limited ~10/hour):

```bash
curl -X POST https://api.freedailypro.com/v1/text/word-count \
  -H "Content-Type: application/json" \
  -d '{"text":"Ship real PDF tools to your agents."}'
```

Also: `/v1/text/slug`, `/v1/text/case-convert`.

## 20–45s — get a key

1. [https://www.freedailypro.com/developers](https://www.freedailypro.com/developers)
2. Generate API Key (trial **20,000 calls/mo**, no card)

## 45–60s — authenticated call

```bash
curl -X POST https://api.freedailypro.com/v1/security/hash \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text":"hello world","algorithm":"sha256"}'
```

PDF example (multipart):

```bash
curl -X POST https://api.freedailypro.com/v1/pdf/merge \
  -H "X-API-Key: YOUR_API_KEY" \
  -F "file=@a.pdf" \
  -F "file=@b.pdf" \
  -o merged.pdf
```

Markdown → PowerPoint:

```bash
curl -X POST https://api.freedailypro.com/v1/pptx/from-markdown \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"markdown":"# Hello\n\n- Bullet one\n- Bullet two"}' \
  -o deck.pptx
```

## Read the truth, not the blog

| Resource | URL |
|----------|-----|
| Developers | https://www.freedailypro.com/developers |
| OpenAPI | https://api.freedailypro.com/openapi.json |
| Swagger UI | https://api.freedailypro.com/docs |
| llms.txt | https://api.freedailypro.com/llms.txt |
| MCP | https://api.freedailypro.com/mcp |
| Registry | `com.freedailypro/tools` |

## Status codes that matter

| Code | Meaning |
|------|---------|
| 200 | Success |
| 401 | Key missing/invalid (route exists) |
| 404 | Route does not exist (even without a key) |
| 429 | Monthly quota exceeded |

## Privacy & plans

- Files processed in memory; not stored after the response.
- Browser tools ≠ API (browser tools ~10 uses/day).
- Trial 20k → Premium $24/200k · Ultra $69/750k · Mega $129/2M+priority.
- Not in API yet: OCR, Word/Excel, live camera/mic.

## CTA

[https://www.freedailypro.com/developers](https://www.freedailypro.com/developers) · Demos: [github.com/SanCoder2026/FreeDailyPro-MCP-Demos](https://github.com/SanCoder2026/FreeDailyPro-MCP-Demos)
