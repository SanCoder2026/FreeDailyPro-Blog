---
title: "How to connect FreeDailyPro MCP to Grok Bot and other MCP clients"
meta_description: "Generic remote MCP setup for FreeDailyPro: endpoint, X-API-Key header, tools/list smoke test, and notes for Grok Bot / any Streamable HTTP client."
---

# How to connect FreeDailyPro MCP to Grok Bot and other MCP clients

FreeDailyPro speaks **remote MCP** over HTTPS:

| | |
|--|--|
| Endpoint | `https://api.freedailypro.com/mcp` |
| Auth | Header `X-API-Key: YOUR_API_KEY` |
| Registry | `com.freedailypro/tools` |
| Agent brief | [https://api.freedailypro.com/llms.txt](https://api.freedailypro.com/llms.txt) |

Any client that supports **Streamable HTTP** (or the transport your client documents for remote servers) can connect the same way.

## Generic checklist

1. Generate a key at [https://www.freedailypro.com/developers](https://www.freedailypro.com/developers).
2. Configure the client with the URL + `X-API-Key` header.
3. Call `tools/list`.
4. Call a cheap tool (`generate_hash` / word-count style) before large file uploads.

### Smoke test (curl)

```bash
curl -X POST https://api.freedailypro.com/mcp \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

Example tool call:

```bash
curl -X POST https://api.freedailypro.com/mcp \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"generate_hash","arguments":{"text":"hello world","algorithm":"sha256"}}}'
```

(Tool names are generated from the live OpenAPI — if a name 404s, re-run `tools/list`.)

## Grok Bot / Cursor-hosted agents

Where a Grok Bot or similar agent runtime supports MCP plugins or custom MCP servers:

- Prefer the **remote URL** above over shipping a local stdio wrapper.
- Put the API key in the platform's secret / vault field.
- Point coding agents at `llms.txt` so they don't invent routes — if a path isn't in [openapi.json](https://api.freedailypro.com/openapi.json), it doesn't exist.

Exact Grok Bot connector UI can change; the protocol facts (URL + header + JSON-RPC methods) stay stable.

## When to use REST instead

Use REST (`https://api.freedailypro.com/v1/...`) from scripts, CI, and large media uploads. Use MCP when an LLM should **choose tools mid-conversation**.

## CTA

[https://www.freedailypro.com/developers](https://www.freedailypro.com/developers)
