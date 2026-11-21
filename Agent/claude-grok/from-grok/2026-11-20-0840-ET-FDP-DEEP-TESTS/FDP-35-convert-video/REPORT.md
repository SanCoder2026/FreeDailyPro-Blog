Sent: 2026-11-21 02:08 ET

# FDP-35 Video Converter (convert-video): deep test report for Claude

- **Written:** 2026-11-21 02:07 EST (box `date`, ET). Testing ran 2026-11-21 01:48–02:03 EST.
- **Tool:** https://www.freedailypro.com/tool/convert-video (+11 pair pages). Row 35 of TEST-ORDER.md: Pro, Video Tools. Plan note "L-243 rule 1 (ApyHub billable/live)"; tools.csv tag `gated:file-job`. No duplicate group. **GSC data is not available.**
- **Classification:** Professional Tool. Everything ran in the browser with ffmpeg.wasm from jsDelivr; no ApyHub or upload call was seen.
- **Testers:**
  - **Desk review:** expanded copy, JSON-LD (10 FAQs), 10 locales + /ar, 11 pair pages, the blog, sitemap. JS: `ConvertVideo`, `operations`, `ffmpegEngine`.
  - **YouTube video:** yt-dlp, 41 frames, 4 sheets, 2 zooms.
  - **Headless Playwright:** 17 synthetic files, 23 conversion cases (every input/output pair type, rewrap vs re-encode, 50 MB limit, bad files); 5 pair pages; a uses-left gate run and an at-0 run; Quick Buy; Share; print; keyboard; 10-device / 11-locale / 6-geo / axe matrix.
- **Starting counts (display-only):** fresh contexts mostly at 0 remaining (`usageToday` 10, day key 2026-11-21); the 7th context had 10 left and was used for the gate run. Trial uses spent: **2**.
- **Constraints kept:** guest only, no sign-in, no email or card typed (stopped at the Day Pass email prompt and Stripe Checkout; session id redacted), no ad clicks, no API/MCP, no site or repo changes.
- **Sign-in (untested):** Save to Google Drive (Google sign-in popup), Save to my cloud storage ("Sign in with your email first", $4.99/month 1 GB). Open from Google Drive and Take photo with camera not clicked.
- **Pending:** nothing that needs the 7:00 PM ET reset (the uses-left behaviour was observed this run), so no RERUN-AFTER-RESET row.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect, restate, push back, and choose fixes that fit how FreeDailyPro ships Professional Tools.

Owner context: Santosh decided (Nov 20) that every Download on Barcode Generator and Invoice Generator uses a trial use. Charging only the first Download per page load conflicts with that decision, so it is reported as a P1 gate gap, not a neutral observation.

Code to look at:
- **Per-page-load counting:** shared `index-*.js` `xI`/`vI` with the set `Kt` (excerpt in FDP-34's evidence; same chunk `index-B1CTyGtY.js` here). After the first allowed use, later uses of the tool in that page load return "allowed" without logging.
- **`ConvertVideo-DJsKNUMk.pretty.js`:** Convert makes no usage call; Download goes through the shared gated button; the result preview `Q({ blob: c })` renders `<video controls src=blob:>` of the same blob, with no `controlsList="nodownload"`.
- **`ffmpegEngine-*.pretty.js` `C()`:** 50 MB trial / 200 MB paid limits — the drop zone says "over 5 GB".
- **`operations-*.pretty.js`:** six outputs `Rt`; rewrap for mp4/mp4-web/mov/mkv when H.264 + AAC/none.

After you ship, rerun `scripts/cvv-gate.js` (expect every Download to follow the decision; the preview not to give a full-quality copy at 0), `cvv-live.js all` (K01–K23 unchanged), then test-cases.md (CV-01…CV-38).

## Intent

Someone has a video in a format a site, editor, TV or phone rejects (MOV from an iPhone, a WebM screen capture, an old AVI/WMV). They want:
- the right container fast, without losing quality when it can be avoided
- a clear statement of what happened (copied vs re-encoded, size change)
- the video never uploaded

The engine is excellent:
- 21 of 23 cases behaved exactly as the page describes; rewraps take under a second and are lossless (K01–K03, K06, K09, K13, K15, K22).
- HEVC, VP9/Opus, MPEG-4 AVI, WMV, FLV, GIF all re-encode correctly; the WebM 1280 px cap and the 50 MB trial cap work.
- The summary line and the "MP4 is often larger than WebM" note are honest; audio-only files are rejected cleanly.
- Nothing is uploaded.

Trust breaks in four places:
- **Gate:** only the first Download per page load costs a use.
- **Gate:** the preview player hands out the full converted file even at 0 remaining.
- **Copy:** the page says four outputs and "over 5 GB"; the tool has six outputs and a 50 MB trial cap.
- **Video:** old "Format Converter" UI with personal folders and bookmarks visible.

## Why: what the evidence says

- **P1 gate gap (conflicts with the Nov 20 decision): one trial use per page load.** `json/gate.json` (02:00:59–02:02:36 EST): Download A 0 → 1; same file again 1 → 1; New + different video B 1 → 1; New + C 1 → 1; reload + D 1 → 2. Same shared code as FDP-34 (and the FDP-33 ZIP).
- **P1: the preview is a free, full-quality download.** Preview blob sha `0762f787…` = the paid Download = the preview in a context at 0 (`json/gate.json` `left.preview`, `zero.preview`). `<video controls>` without `controlsList="nodownload"`: Chrome's player menu offers Download; "Save video as…" also works (neither clicked). At 0 the page's Download opens the cap dialog.
- **P2: copy contradicts itself and the tool.** Six outputs live vs "four" in FAQ / How to use / Limitations / blog and "MP4, WebM and MOV" in the subtitle and JSON-LD; "Large files (over 5 GB)" vs the enforced 50 MB trial / 200 MB paid limit (K21; `ffmpegEngine` `C()`).
- **P2: video zqpLPhmyj9E (124 s, 25 views, 2026-09-24):** old "Format Converter — Convert between MP4 and MOV" UI; Windows file dialog shows personal folders ("CEH", "Crack", "Agent Outros") and the bookmarks bar; "Free" wording; ~25 s end card.
- **P2: wording/SEO:** 11 pair titles "… - Free, No Upload"; English titles under 9 hreflangs; /ar 404.
- **P2: completeness:** no quality/resolution/fps controls, no H.265/AV1/VP9 output, WebM fixed at VP8 1 Mbps, no batch; 50 MB trial is small for phone video.
- **P3 items:** a text file named .mp4 gets a misleading "phone codec" error after 11.6 s; "Upgrade to Pro" vs Day Pass/Monthly naming; How-to says rewrap only for MP4/MOV (MKV too); cap dialog's mark claim; iPhone SE 9 px and ja 3 px overflow; link-in-text-block; two "Quick Buy"; thumbnail alt; Offer 4.99.

## Outcomes we want

1. Every Download is counted as Santosh decided (no free downloads after the first in a page load), with the label saying so.
2. The preview can't be saved at full quality without a use (e.g. `controlsList="nodownload"` plus a short or low-resolution preview, or the preview shown only after Download is allowed).
3. One consistent story: six outputs, 50 MB trial / 200 MB paid, everywhere (drop zone, subtitle, FAQ, Limitations, JSON-LD, blog).
4. A current, clean video (iPhone MOV → MP4 rewrap in seconds, WebM → MP4) with "trial uses" wording and no personal folders.
5. Pair titles without "Free"; translated head tags or no hreflang.
6. A Premium step: quality/resolution presets, H.265/VP9 output, batch.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS | 21/23 cases exact; K18 misleading error; K21 limit works (`json/cases-chromium.json`). |
| 2 | Completeness vs competitors | PARTIAL | Smart rewrap and broad input; no quality/resolution controls, no modern codecs out, no batch (desk). |
| 3 | Ease of use | PASS | One select + Convert; honest summary; format notes. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px, ja 3 px overflow. |
| 5 | Payment process | PASS (stopped) | Cap dialog / Quick Buy day → "Day Pass, $1" email prompt; Quick Buy monthly → Stripe Checkout. Nothing typed. |
| 6 | Information correct | PARTIAL | Four vs six outputs; "over 5 GB" vs 50 MB; rewrap scope; "Pro" naming. |
| 7 | Indexing | PASS | 200; canonical self; sitemap incl. 11 pair pages and blog. |
| 8 | SEO | PARTIAL | Good title/meta, FAQPage (10), VideoObject. Pair titles "Free"; JSON-LD says 3 formats; English titles under hreflang; /ar 404; thumbnail alt. |
| 9 | Blog exists and accurate | PASS (minor) | `/blog/convert-video` accurate on rewrap and 50/200 MB; "four entries" outdated. |
| 10 | YouTube video exists | PASS | zqpLPhmyj9E, 124 s, 25 views, 2026-09-24. |
| 11 | FAQ and guide correct | PARTIAL | "four outputs"; no trial size cap mentioned. |
| 12 | Video shows current capabilities | **FAIL** | Old MP4/MOV-only UI; personal folders and bookmarks visible; "Free". |
| 13 | Storage | PASS | No upload; nothing stored. |
| 14 | Sharing | PASS | Share copies only the tool URL. |
| 15 | Downloads | PASS | Correct names (`_converted` rule), containers and codecs (ffprobe). Drive/cloud need sign-in (untested). |
| 16 | Usage count | **FAIL (P1 gate gap)** | First Download per page load −1, later Downloads free until reload — conflicts with the Nov 20 every-Download decision; preview gives the file at 0. |
| 17 | Categorization in section | PASS | Video Tools. |
| 18 | Correct section of site | PASS | Breadcrumb Home › Video Tools. |
| 19 | AI need/demand | PASS (demand strong) | "mov to mp4", "webm to mp4" are high-volume evergreen queries; pair pages target them. No AI needed. |
| 20 | Merge better? | No | Distinct from Compress Video / Extract Audio / Video to GIF (page explains). |
| 21 | Remove? | No | |
| 22 | Duplicates | None | |

## Severity summary
- P0: 0. Privacy holds: no video data in any request.
- P1: 2 (one use per page load, against the Nov 20 decision; full-quality preview download at 0).
- P2: about 5 (copy contradictions, video, wording/SEO, completeness, size-limit copy).
- P3: several.
