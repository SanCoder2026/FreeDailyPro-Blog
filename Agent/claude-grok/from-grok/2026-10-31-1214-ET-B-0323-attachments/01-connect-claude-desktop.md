---
title: "How to connect FreeDailyPro MCP to Claude Desktop"
meta_description: "Step-by-step: point Claude Desktop at FreeDailyPro's remote MCP endpoint with your X-API-Key and run your first PDF or text tool."
---

# How to connect FreeDailyPro MCP to Claude Desktop

**Time:** ~5 minutes · **You need:** a FreeDailyPro API key (20,000 trial calls/mo, no card)

FreeDailyPro exposes **211+ MCP tools** (PDF, PowerPoint, media, text, calculators, business docs) on one remote endpoint. Same key as the REST API.

## 1. Get a key

1. Open [https://www.freedailypro.com/developers](https://www.freedailypro.com/developers)
2. Sign in → **Generate API Key**
3. Copy the key once. Regenerating **revokes** the old key everywhere — don't regenerate just to "test."

## 2. Confirm MCP answers

```bash
curl -X POST https://api.freedailypro.com/mcp \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

You should see a tool list. Machine-readable setup also lives at [https://api.freedailypro.com/llms.txt](https://api.freedailypro.com/llms.txt).

## 3. Add the remote server in Claude Desktop

Add a custom / remote MCP connector:

- **URL:** `https://api.freedailypro.com/mcp`
- **Header:** `X-API-Key: YOUR_API_KEY`

If your Claude Desktop build still uses a JSON config file, a typical shape is:

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

Restart Claude Desktop after saving. Exact UI labels move between versions — look for **Custom connectors** / **MCP servers**.

## 4. First successful call

In a new chat:

> Using FreeDailyPro, run word-count on: "Agents need real file tools, not slideshow demos."

Then try a file tool:

> Merge these two PDFs with FreeDailyPro and return the result.

## Honest notes

- **API ≠ browser tools.** Browser tools on FreeDailyPro can stay on-device; calling the API **sends files to the server** for in-memory processing (not stored after the response). Browser tools are separate (~10 uses/day).
- **Not in the API yet:** OCR, Word/Excel conversion, live camera/mic.
- **Quota:** one shared monthly pool across all tools. Trial = 20,000 calls. Over quota → HTTP **429**.
- Official listing: MCP Registry `com.freedailypro/tools`.

## Plans (quick)

| Plan | Calls / mo | Price |
|------|------------|-------|
| Trial | 20,000 | Free (no card) |
| Premium | 200,000 | $24 |
| Ultra | 750,000 | $69 |
| Mega | 2,000,000+ priority | $129 |

## CTA

Generate a key and connect: [https://www.freedailypro.com/developers](https://www.freedailypro.com/developers)

Demos: [FreeDailyPro-MCP-Demos](https://github.com/SanCoder2026/FreeDailyPro-MCP-Demos) · OpenAPI: [openapi.json](https://api.freedailypro.com/openapi.json) · Docs: [Swagger UI](https://api.freedailypro.com/docs)
