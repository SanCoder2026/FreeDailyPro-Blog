---
title: "Building a document cleanup agent with FreeDailyPro MCP"
meta_description: "Design a share-safe cleanup agent: flatten and watermark PDFs, clean and redact PowerPoint decks, with FreeDailyPro MCP."
---

# Building a document cleanup agent with FreeDailyPro MCP

**Outcome:** before a deck or PDF leaves the building, an agent strips residue and applies a clear watermark.

## Tools to bind

| Cleanup job | Endpoint |
|-------------|----------|
| Flatten form fields | `POST /v1/pdf/flatten` |
| Watermark PDF | `POST /v1/pdf/watermark` |
| Strip PPTX notes/comments/author/hidden | `POST /v1/pptx/clean` |
| Redact strings in PPTX | `POST /v1/pptx/redact` |
| Shrink for email | `POST /v1/pptx/compress/medium` |

## System brief

```
You are a document cleanup agent using FreeDailyPro.
Default pipeline for PDF: flatten → watermark "COPY" (or user text).
Default pipeline for PPTX: clean → optional redact patterns → compress/medium.
Confirm destructive redaction with the user when patterns are broad.
No OCR. No Word/Excel.
```

## Example user utterance

> Clean `q3-board.pptx` for external counsel. Remove notes and author metadata. Redact "Project Falcon". Compress for email.

## Implementation sketch

See `02-demo-agents/02-document-cleanup-agent/cleanup_pipeline.py` for a REST version you can run in CI. Wire the same steps as MCP tool calls inside Claude/Cursor.

## Privacy line for your README

> Files are sent to FreeDailyPro for processing and are not stored after the response. Prefer client-side browser tools on freedailypro.com when data must never leave the device.

## CTA

[https://www.freedailypro.com/developers](https://www.freedailypro.com/developers)
