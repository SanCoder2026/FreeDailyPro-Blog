---
title: "PowerPoint from Markdown: agent-driven decks via API"
meta_description: "Turn Markdown or JSON outlines into editable PPTX with FreeDailyPro — paths, examples, and agent prompts."
---

# PowerPoint from Markdown: agent-driven decks via API

FreeDailyPro's PowerPoint toolkit includes **26 endpoints**. The three builders agents use most:

| Builder | Path |
|---------|------|
| Markdown → PPTX | `POST /v1/pptx/from-markdown` |
| JSON → PPTX | `POST /v1/pptx/from-json` |
| CSV → PPTX | `POST /v1/pptx/from-csv` |

Also useful after build: `extract/text`, `clean`, `compress/*`, `merge`, `split`.

## Why agents like Markdown → PPTX

Authors already think in headings and bullets. The model drafts Markdown; FreeDailyPro returns a **real editable .pptx** (not a screenshot).

## Minimal flow

1. Agent drafts outline Markdown (`#` slides, `-` bullets).
2. Call `/v1/pptx/from-markdown`.
3. Optionally `/v1/pptx/clean` before sharing.
4. Optionally `/v1/pptx/compress/medium` for email.

### curl shape

```bash
curl -X POST https://api.freedailypro.com/v1/pptx/from-markdown \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"markdown":"# Title\n\n## Slide 1\n- Point A\n- Point B\n"}' \
  -o deck.pptx
```

If your client prefers multipart, send a `.md` file field instead — see demo `04-pptx-deck-builder-agent/`.

## JSON when you need structure

Use `/v1/pptx/from-json` for explicit titles, tables, notes, and brand color (e.g. `#4FD8C4`). Example payload in `slides.example.json`.

## Agent prompt

> Draft a 6-slide product update in Markdown. Call FreeDailyPro pptx/from-markdown. Return the file. Don't invent slide design buzzwords — keep layout to the API template.

## CTA

[https://www.freedailypro.com/developers](https://www.freedailypro.com/developers)
