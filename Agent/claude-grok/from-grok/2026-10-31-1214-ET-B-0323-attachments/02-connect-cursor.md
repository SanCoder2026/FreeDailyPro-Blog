---
title: "How to connect FreeDailyPro MCP to Cursor"
meta_description: "Add FreeDailyPro's remote MCP server to Cursor so the agent can merge PDFs, build PPTX, and run text/SEO tools mid-chat."
---

# How to connect FreeDailyPro MCP to Cursor

Cursor is a natural home for FreeDailyPro: agents that edit code often also need **document and media side-effects**. FreeDailyPro gives you **211+ MCP tools** (and **215+ REST endpoints**) behind one key.

## 1. API key

Create one at [https://www.freedailypro.com/developers](https://www.freedailypro.com/developers) (trial: 20,000 calls/mo, no card). Store it in your environment or Cursor's secret fields — not in a committed repo.

```bash
export FREEDAILYPRO_API_KEY="YOUR_API_KEY"
```

## 2. Add MCP server in Cursor

**Settings → MCP → Add new MCP server** (or edit `mcp.json`):

```json
{
  "mcpServers": {
    "freedailypro": {
      "url": "https://api.freedailypro.com/mcp",
      "headers": {
        "X-API-Key": "YOUR_API_KEY"
      }
    }
  }
}
```

Enable the server and confirm tools appear in the MCP panel.

## 3. Smoke test

Ask Cursor Agent:

> List FreeDailyPro tools related to PowerPoint, then create a short deck from this Markdown outline using pptx/from-markdown.

Or from a terminal in the project (no key required for this route; IP rate-limited ~10/hour):

```bash
curl -X POST https://api.freedailypro.com/v1/text/word-count \
  -H "Content-Type: application/json" \
  -d '{"text":"hello from Cursor"}'
```

Authenticated example:

```bash
curl -X POST https://api.freedailypro.com/v1/security/hash \
  -H "X-API-Key: $FREEDAILYPRO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text":"hello world","algorithm":"sha256"}'
```

## 4. Project tip

Keep a `demos/` folder (see [FreeDailyPro-MCP-Demos](https://github.com/SanCoder2026/FreeDailyPro-MCP-Demos)) and let the agent call REST for large video files — MCP media tools may use tighter size limits because of base64 overhead.

## Privacy & pricing (short)

- Files transmitted for processing; not stored after response.
- Browser tools are separate from the API (~10 uses/day).
- One key, one quota across PDF / PPTX / media / text.
- Plans: Trial 20k → Premium $24 / Ultra $69 / Mega $129.
- Gaps: no OCR, Word/Excel conversion, or live camera/mic yet.

## CTA

[https://www.freedailypro.com/developers](https://www.freedailypro.com/developers) · OpenAPI: [https://api.freedailypro.com/openapi.json](https://api.freedailypro.com/openapi.json) · llms.txt: [https://api.freedailypro.com/llms.txt](https://api.freedailypro.com/llms.txt)
