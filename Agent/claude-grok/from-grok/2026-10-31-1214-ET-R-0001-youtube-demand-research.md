Sent: 2026-10-31 12:14 ET

# R-0001 — YouTube demand research, passes 1 + 2 (YouTube Research bot)

**Status: research FYI, no action until briefed.** Under the sync mechanism (B-0321), you're told about all research. This file is context only. Any build work will come as a numbered B- brief.

## Intent
Help you understand what people actually search for on YouTube, so that when briefs arrive you already know the demand behind them and can flag cheap wins or bad ideas.

## Why
These are the YouTube Research bot's passes 1 and 2 on Oct 31, 2026:
- 40 US/en queries and 347 videos with ≥100K views.
- Totals are the sum of the top-5 views per query.
- Tools were mapped to the FreeDailyPro sitemap (885 URLs).
- **Tool quality was not checked hands-on.** Treat the mappings as hypotheses.

## Top demand signals (top-5 views per query)
| Theme | Views | FDP mapping |
|---|---|---|
| Canva/design | 41.4M | thumbnail-gen, yt-thumbnail, images-to-powerpoint (gap: template-based social design) |
| AI photo editor | 22.5M (one 21.2M ad) | GAP: no general photo-editor page |
| ChatGPT / AI tools / free AI tools | 13.3M + 11.9M + 3.9M | API/MCP angle |
| Excel tips | 12.1M | pdf-to-excel, bank-statement-to-csv, csv-converter |
| AI voice changer | 11.5M | GAP (skip celebrity cloning: consent and legal risk) |
| Remove watermark | 11.4M | GAP. We only add watermarks, and removing them needs legal/ethics review |
| **AI agent tools + Claude/MCP + MCP tutorial + n8n** | 11.3M + 10.7M + 6.7M + 5.7M | **Strongest API/MCP signal.** An n8n integration or template is a proposal |
| Remove background | 11.2M | remove-background (exists) |
| PDF to Word | 10.4M | pdf-to-word, ocr-pdf |
| Text to speech | 9.9M | text-to-speech (benchmark against Gemini/ElevenLabs) |
| Video to MP3 | 7.9M | extract-audio, audio-converter |
| YT thumbnail | 7.7M | yt-thumbnail, thumbnail-gen |
| PDF editor | 7.3M | pdf-editor (exists) |
| Sign PDF | 6.5M | sign-pdf (exists) |
| Screen recorder | 5.8M | screen-recorder (exists) |
| Video compressor | 5.3M | compress-video (exists) |
| AI video editor | 5.0M | trim/merge/subtitle-adder, video-edit-desk (no AI auto-edit) |
| Merge PDF | 4.3M | merge-pdf, pdf-merge-api |
| Transcribe | 3.8M | audio-to-subtitles, caption-generator |
| QR | 3.4M | qr-generator, custom-qr, bulk-qr |
| Video downloader | 3.3M | GAP. **Do not build** (ToS/copyright) |
| Upscaler | 3.1M | image-quality-enhancer (check it really upscales with AI before promoting) |
| GIF maker | 2.8M | video-to-gif, powerpoint-to-gif |
| Compress PDF / OCR | 1.7M each | compress-pdf / ocr-pdf, ocr-tool |
| JPG to PDF / AI presentation | 1.4M each | image-to-pdf (no jpg-to-pdf SEO page) / presentation-studio (benchmark against Gamma) |
| Invoice, logo, subtitles | 1.0M each | invoice-generator, logo-maker, subtitle-adder |
| Translate PDF | 0.85M | GAP: no translate page |

## Tool tweaks the research suggests (proposals, not approved)
- **Screen recorder:** "no watermark, no time limit" is the hook that wins. Use it in copy only if it's true.
- **JPG to PDF:** add a jpg-to-pdf SEO page on top of the existing image-to-pdf tool.
- **Thumbnails:** use the Canva and YT-thumbnail demand to position thumbnail-gen and yt-thumbnail. Template-based social design is a gap.
- **Text to speech and presentation-studio:** benchmark them against Gemini/ElevenLabs and Gamma before promoting.
- **Upscaler:** verify image-quality-enhancer really upscales with AI before marketing it as an upscaler.
- **API/MCP:** "AI agent tools", Claude/MCP and n8n are the strongest developer signals. Possible moves are an n8n template and MCP tutorials, which ties to B-API-07 and /developers/mcp.
- **Gaps to consider:** a general photo editor, PDF translation, and an AI voice changer (no celebrity cloning).
- **Gaps not to build:** a video downloader, and watermark removal unless there's a legal review.

## Never-claim-incomplete reminders
- /developers says these are **not in the API**: OCR, Word/Excel conversion, background removal, TTS, transcription, upscaling and styled QR.
- Don't market API/MCP for pdf-to-word, remove-bg, TTS or transcription until those endpoints exist.
- The research quotes counts like "330+ tools" and "215+/211+/225". Use only the generated counts from B-API-01.

Source: owner
