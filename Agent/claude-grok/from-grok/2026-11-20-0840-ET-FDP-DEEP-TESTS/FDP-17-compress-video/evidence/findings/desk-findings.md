Sent: 2026-11-20 08:40 ET

# Desk findings: Compress Video

- **Sources:** tool page HTML (2026-11-19 15:28 EST), es, /ar, the blog, the Video Tools category, the `CompressVideo` / `utils` / `megabytes` / `ffmpegEngine` code, the Discord and Gmail help pages, and WhatsApp help (via WebSearch).

## Copy vs behaviour
1. **A "Light" option that doesn't exist.** The FAQ says "Strong or a small Custom Target costs more than Light". The blog says "Light, Medium and Strong aim for… 10, 25 or 50 percent smaller", with 39.6 MB worked as the Light figure. The YouTube description says "Light/Medium/Strong… 10%/25%/50%". The video shows a Light button. The live tool has no Light (`gate-kbd.json`).
2. **Default mode.** The guide says "Manual Quality, which is selected when the tool opens". The code (`useState("medium")`), the live UI and "How it works" ("Medium is selected") disagree.
3. **Number of encodes.** The guide's hint says "adjusts once if it lands over". The FAQ says "all run two full encoding passes" and, elsewhere, "repeats up to twice". The code (`utils` V) runs up to 3 encodes and stops once under.
4. **Size limits.** The drop zone says "Large files (over 200 MB) may take longer". The engine caps trial uses at 50 MB (MiB) and Pro at 200 MB, so trial users learn about the 50 MB limit only after choosing a file. The blog states the 50/200 MB limits correctly.
5. **Preset labels are outdated** (official pages checked 2026-11-19):
   - Discord's File Attachments FAQ (updated 2026-09-30): "For non-Nitro subscribers, the maximum file upload is 20MB… As of August 2026… (up from 10MB)". The tool's "8 MB (Discord)" squeezes a Discord clip to 40% of what Discord allows, and the blog repeats "8 MB (the Discord figure)".
   - WhatsApp Help Center: default video limit 100 MB (fast connections) or 64 MB (slow), and documents up to 2 GB. The tool's "16 MB (WhatsApp)" is the old figure. Both labels cost needless quality.
   - Gmail's 25 MB per personal account matches "25 MB (email)".
6. **Targets above the source.** Custom 50 MB / 100 MB on a smaller file encode *up* to the target (C15: 12.9 MB → 97 MB, "Target reached"). Nothing caps the target at the source bitrate (`utils` L62–63).
7. **Audio bitrate is fixed at 128 kbps AAC** (`utils` f=128). Small targets on long clips can't be reached: 60 s × 128 kbps ≈ 0.96 MB for audio alone. The miss advice "Try Strong or Lower resolution to 720p" is generic (C07).
8. **Manual Quality FAQ.** "Caps the bitrate near 90 percent of the source's, so an already efficient file is less likely to grow". On a noisy 10 Mbps 1080p file the output was 4.4% larger (C03); the message and the Keep original button handled it honestly.
9. **Errors.** Non-video input shows phone-codec advice plus "check the browser console (F12)" (C17).
10. **Units.** Limit messages use MiB ("68.3 MB" for a 71.7 MB file); results and targets use decimal MB (`megabytes` B=1e6). The decimal targets are safer for 1024-based caps.

## SEO and indexing
- **Title:** "Compress Video to a Target Size (MB) | FreeDailyPro". Meta is 153 characters and mentions "WhatsApp and email presets". H1 is "Compress Video". The canonical is self. Tool and blog are in the sitemap. hreflang covers 10 locales plus x-default; /ar is a 404 (not listed).
- **JSON-LD:** SoftwareApplication (4.99 USD), VideoObject, FAQPage (11), BreadcrumbList.
  - The VideoObject name "How to Compress Video Online – Reduce File Size" doesn't match the YouTube title "How to Use Compress Video – Free Step-by-Step Walkthrough".
  - The schema upload date is 2026-09-23; YouTube's is 20260924.
- **OG image:** generic `og-default.png`. One empty alt.
- **Locales:** H1 translated (es "Comprimir Video", ja "動画圧縮"…). Title, meta and most UI are English. The es server HTML has no "gratis".
- **GSC data is not available.** The TEST-ORDER test-plan figures, quoted as-is: "52 views; API returns same GIF regardless of settings". The API was not tested (out of scope).

## Blog (/blog/compress-video, 2026-10-17)
- A strong worked example: 44 MB → 25 MB, with bitrate arithmetic and an honest-results section.
- **Errors:**
  - the Light button
  - "8 MB (the Discord figure)"
  - presets listed as 8, 25, 50, 100 (missing 16)
  - "25 MB is 26,214,400 bytes", while the tool targets 25,000,000 bytes
  - it sends readers to Trim Video, though Custom Target has trim built in

## Placement and overlap
- Video Tools, bundle Video Edit Desk: correct.
- No duplicate tool. gif-resize-compress is GIF-only; Video Converter changes format. Cross-link both.

## Competitors (completeness)
Candid Tools' compress-video page (from the WebSearch snippet, 2026-11-19; page not opened) offers:
- Discord 20 MB / WhatsApp 64 MB / email 18 MB presets
- a plan preview (resolution, bitrate, expected size) before encoding
- hardware WebCodecs encoding

This tool has more modes (percent, quality slider, exact target + trim, 720p), honest result lines and a damaged-file pre-check. Gaps:
- current platform presets
- a pre-encode estimate
- an audio bitrate / mono option
- a resolution choice beyond 720p (e.g. 480p)
- speed (wasm superfast: about 30 s for 10 s of 1080p)
