Sent: 2026-11-01 03:15 ET (Orchestrator)

# P0 first: markdown-to-html lets javascript: links through (B-API-94)

**Intent:** No FreeDailyPro output should ever carry executable links. The markdown-to-html endpoint is on the paid Text listing and is also the MCP tool `markdown_to_html`.
**Why:** `[click](javascript:alert(1))` comes back as `<a href="javascript:alert(1">`. That's a stored-XSS risk for any customer who renders our output. `<script>` and onerror are already escaped correctly.
**Outcome:** Only safe schemes are allowed in links (http, https, mailto and relative). Strip or neutralize javascript:, data: and vbscript: hrefs, case-insensitively and including obfuscated forms. Fix the broken `"` placement in the href. Add regression tests.

# Also from cycle 18
- **B-API-88:** /mcp/mortgage-loans and /mcp/unit-converter return 404. The 404 body exposes the internal path docs/api-groups-readiness.md. Fix the routes and make the 404 generic.
- **B-API-90:** Garbage input is billed. Invalid input should be a free 4xx.
- **Student-paper workflow (B-API-95 to 98).** Readability and diff are exact. The rest needs work:
  - GPA grades of 5 or -1 are accepted and billed. They should be a 4xx.
  - APA, MLA and Chicago citations are wrong. Match the current style manuals.
  - paper-format returns only a disclaimer. It should return real formatting.
  - Markdown output is missing GFM tables, task lists, footnotes and strikethrough.
- **llms.txt:** It says "about 205 paths". Use multiples of 50 with a plus sign, for example "200+".
- **429 body:** It says "free API key". It should say trial key.
- **Still open:** B-API-14 (16 of 21 keyless calls served), B-API-61 (currency 1.95% above ECB), and B-API-53, 67, 77 and 81.

Source: owner
