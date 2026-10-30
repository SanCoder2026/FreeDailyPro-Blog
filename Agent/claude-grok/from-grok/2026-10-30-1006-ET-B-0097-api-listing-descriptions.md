Sent: 2026-10-30 10:06 ET
# B-0097 — Make every API/MCP listing the clearest, easiest-to-use in its marketplace (copy only, no new endpoints)

## Intent
Developers decide in ~10 seconds from a marketplace card whether to try us. Today our repo-owned listing copy is stale (registry says 61/178 tools, Postman shows `{}` responses, Rapid snippet has an empty `X-RapidAPI-Host`, developers page claims Smithery/Glama/mcp.so sync that doesn't exist). Rule 1: be at least as good as the best competitor (PDF4me, yakpdf, ConvertAPI, top MCP servers) and feel effortless. Outcome: every surface we generate from the repo shows accurate counts, a working first call in under 60 s, and job-to-be-done wording. No new code paths; text, metadata and examples only.

## Why
Rapid top sellers win on a one-line outcome + working snippet; our 7 Rapid listings have 0 tags, 1 subscriber each, ~1k-char READMEs. Registry v1.0.0 (Railway URL) is still active and misleads clients.

## Outcomes (acceptance)
1. **OpenAPI** (`/openapi.json`): every operation has a 1-line `summary` (verb + object + result), a `description` with limits/errors, and a real `example` request + response (no `{}`). Tags grouped: PDF, PowerPoint, Documents, Text, Image, Audio, Video, Calculators. Exclude Book Publishing and `/v1/redact-pdf` (B-0098) from marketplace exports until fixed.
2. **server.json / MCP README**: description "211+ MCP tools: PDF merge/compress/repair, Markdown→PowerPoint, doc conversion, audio/video/image conversion. Files processed in memory, never stored." Publish 1.3.1; mark 1.0.0 deprecated (needs Santosh's DNS key). README gets copy-paste configs for Claude Desktop, Cursor, VS Code, a 3-tool quick demo, limits, and pricing link.
3. **Developers page**: remove "Smithery, Glama & mcp.so synced automatically"; show real listing status with links (RapidAPI, Postman, ApyHub, API.market, MCP Registry); a 60-second curl quickstart; pricing table (trial 20,000 calls/mo, $24/200k, $69/750k, $129/2M + priority — unchanged).
4. **Marketplace snippets**: Rapid examples use `https://<product>.p.rapidapi.com` and filled `X-RapidAPI-Host`; Postman collection regenerated with a pinned "First call" folder (word-count, pdf/merge, pdf/repair) and saved example responses.
5. **Watermark default** — doc text must state the visible default; if the default stays near-invisible, flag to Santosh (behaviour decision is his).
6. Word "free" only in SEO tags/keywords, not titles or descriptions.

## Check
A fresh dev copies one snippet from each surface and gets a 200 with no edits beyond the key. Counts on registry, README, developers page match `openapi.json`.

Source: owner
