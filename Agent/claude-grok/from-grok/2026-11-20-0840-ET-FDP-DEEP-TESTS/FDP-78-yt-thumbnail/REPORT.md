Sent: 2026-11-21 17:50 ET

# FDP-78 YouTube Thumbnail Downloader (yt-thumbnail): deep test report for Claude

- **Written:** 2026-11-21 17:50 EST (box `date`, ET). Testing ran 2026-11-21 17:36–17:48 EST.
- **Tool:** https://www.freedailypro.com/tool/yt-thumbnail
  - TEST-ORDER row 78: **Pro**, Design & Marketing, "test-plan (unranked): GSC top-50 SEO backfill 16", duplicate group **C42** (thumbnail tools).
  - Strip "Trial: 10 uses/day", Quick Buy $1 day / $4.99 month. Video lDBgQDbgHmY (embedded, 92 s). Blogs /blog/yt-thumbnail and /blog/yt-thumbnail-downloader-creators (both 200, linked).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (`YtThumbnail-BluoGDJ4.js`, pretty copy in `js/`):** the link is parsed locally for the 11-character ID (watch, youtu.be, shorts, embed, live, v, e; www./m./music. hosts; youtube-nocookie; bare ID). The browser loads img.youtube.com maxres/sd/hq/mq/default; a size is left out when it errors or comes back ≤120 px wide. Preview = largest size. Download = `logUsageNow()` + ToolPage downloader (adds the FDP badge); fallback opens the image in a new tab. ZIP = all sizes, built in the browser, gated by the downloader.
- **Testers:** desk (page copy, 7 FAQs, JSON-LD, 2 blogs, JS); Playwright guest: `zero.json` (Chromium 10/10), `left.json` (Chromium 0/10, try 13), `left-firefox.json` (30 tries, none with uses), `parse.json` (25 inputs), `resubmit.json` + Firefox, `quickbuy.json`; downloads compared byte-for-byte with YouTube's originals; video frames; matrix of 10 devices, 10 locales + /ar, 6 geo, axe.
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes. Stripe ID redacted.
- **Sign-in (untested):** paid pass (Quick Buy Day Pass email step; Monthly Stripe checkout).
- **RERUN-AFTER-RESET:** none (uses-left observed in Chromium).

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters to a creator or marketer grabbing a cover for a slide, newsletter or archive.

**Owner context:** downloads count as trial uses. Per-page-load charging is P1. A real way to save a byte-identical file at 0 uses is P1; a visible full-quality preview alone is an owner question. The FDP badge watermark is intentional (Nov 21).

**P1:**
- **One use per page load.** At 0/10 the first Download charged (0→1/10, 1 POST). Then Standard, Small, ZIP ×2, another video's High quality and its ZIP: 7 more files, 0 POSTs. After a reload one Download charged again (1→2/10); the ZIP after it was free. So 9 files cost 2 uses. The FAQ says the ZIP "counts as one download". Likely cause: the page-level "already logged" flag is not reset per download. Fix: charge each Download/ZIP press, or per video if that's the intended unit (say so on the page).
- **Clean original saveable at 0 (owner rule).** At 10/10 Get Thumbnails still renders the 1280×720 preview (X01; old video X07) with no dialog. The preview `<img>` src is the img.youtube.com URL, so right-click → Save image as gives YouTube's clean file (65,324 B), byte-identical. The gated Download gives a badged copy (89,022 B). Nuance: this is a public YouTube image anyone can open; you may decide to accept it, or draw the preview to a canvas/CSS background.

**Owner question:**
- The badge ("Created with FreeDailyPro.com", twice; diff box x 948–1256, y 24–696) is stamped onto another creator's thumbnail. Small 120×90 stays unmarked. Policy says the badge is intentional; the question is whether it should apply to a third-party cover, given the FAQ promises "the same file" and the blog tells people to crop the "1280x720 original" for a newsletter card.

**P2 — where to look:**
- **Same video again → stuck.** Pressing Get Thumbnails again for the same ID (or pasting youtu.be/… for an ID already shown) leaves no preview and "Download all sizes" disabled on "Checking sizes…" forever (Chromium + Firefox, `S02-same-again*.png`). Another video then back works. Likely the size-check state is keyed by ID and the image onLoad never fires again for cached `src`.
- **FAQ "gives the same file"** is false (fallback = clean, download = badged); the page never mentions the badge.
- **Blog /blog/yt-thumbnail** is out of date: "five cards… Not available and its button is disabled", no ZIP, no left-out line.
- **Video lDBgQDbgHmY:** old light UI, "10 free uses daily!" overlay, "Free" in the title, no ZIP.
- **Locale pages:** 10 hreflang pages 200 with `lang` set, but title, H1, meta, labels and FAQ are English.
- **iPhone SE:** "Get Thumbnails" ends at 329/320 px and the Feedback button sits on it; URL box squeezed to 139 px.

**P3:**
- youtube.co.uk, attribution_link and gaming.youtube.com links get the error message; "hello-world" (11 chars) is treated as an ID ("Video not found").
- ja desktop 3 px overflow. axe desktop: label-content-name-mismatch (serious, `.right-2`) + region (moderate); Pixel 7 clean.
- C42: naming is close to the Thumbnail Generator; keep "Downloader" in title/H1/cards.

## Intent

A creator wants the real cover of a video at the biggest size, fast. The tool parses every common link form, detects missing sizes correctly (the 2005 video shows only hq/mq/default with an explanatory line), and the ZIP works. The issues are the gate (one use buys unlimited downloads for that page load, and the preview itself is the clean file), the badge on someone else's image, and a re-submit bug that strands the ZIP.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Real sizes, correct left-out detection. |
| 2 | Completeness | PASS | 5 sizes, preview, ZIP, fallback. |
| 3 | Ease of use | PARTIAL | Re-submit leaves ZIP stuck. |
| 4 | Layout | PASS (minor) | iPhone SE 9 px + FAB overlap. |
| 5 | Payment process | PASS | Day Pass → email dialog; Monthly → Stripe. Stopped. |
| 6 | Information correct | PARTIAL | "same file", "ZIP counts as one download". |
| 7 | Indexing | PASS | 200, canonical self, hreflang. |
| 8 | SEO | PASS | Title 58 chars, meta ~125. |
| 9 | Blog | PARTIAL | /blog/yt-thumbnail old UI; creators blog OK. |
| 10 | YouTube video | PASS | Embedded and linked. |
| 11 | FAQ / guide correct | PARTIAL | See 6. |
| 12 | Video shows current capability | FAIL | Old UI, "free uses", no ZIP. |
| 13 | Storage | PASS | Nothing uploaded; requests go to img.youtube.com only. |
| 14 | Sharing | N/A | "Share this tool" only. |
| 15 | Downloads | PARTIAL | Work; badged; 9 files for 2 uses. |
| 16 | Usage count | **FAIL (P1)** | Per page load. Gate at cap holds for buttons. |
| 17 | Categorization in section | PASS | Design & Marketing. |
| 18 | Correct section of site | PASS | Next steps to image tools. |
| 19 | AI need and demand | PASS | "youtube thumbnail downloader" is a high-volume query; chat AIs can't fetch images. |
| 20 | Merge better? | No | Different job from Thumbnail Generator. |
| 21 | Remove? | No | GSC top-50 backfill. |
| 22 | Duplicates | C42 | Naming only. |

## After fixes, rerun

- `px78-live.js left` (expect 1 POST per Download/ZIP), `zero` (preview policy), `resubmit` (S02/S03 should show the preview and an enabled ZIP).
