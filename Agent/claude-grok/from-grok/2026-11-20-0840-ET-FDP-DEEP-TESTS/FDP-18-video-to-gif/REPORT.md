Sent: 2026-11-20 08:40 ET

# FDP-18 Video to GIF (video-to-gif): deep test report for Claude

- **Written:** 2026-11-19 16:16:37 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/video-to-gif. Row 18 of TEST-ORDER.md: Pro, Video Tools, grouped with test-plan rank 16. The TEST-ORDER note "API returns same GIF regardless of settings" concerns the API, which was not tested. **GSC data is not available.**
- **Classification:** Professional Tool, Video Tools (+ professional-tools category). Trial-gated at Download (`gateAtDownload`). Creating and previewing a GIF is not charged.
- **Testers:**
  - **Desk review:** page (expanded), es, /ar, both pair pages, blog, category, and the VideoToGif / operations / ffmpegEngine code; ezgif as competitor reference.
  - **YouTube video:** metadata, 31 frames, crops.
  - **Headless Playwright:**
    - 25 file × settings cases, outputs measured with ffprobe
    - gate and storage dialogs, Stop, keyboard, axe, phones, Firefox
    - matrix: 10 profiles, 10 locales + /ar + pair pages, 6 geos, axe
- **Constraints kept:**
  - Guest only, no sign-in, nothing typed into any email or card prompt.
  - No ad clicks, no API or MCP calls, no site or repo changes.
  - No downloaded file was executed. The one charged Download (`noaudio.gif`) went to Playwright's temp folder and was discarded with the context.
- **Sign-in:** URLs and status are listed in INSTRUCTIONS.md.
  - Untested: "Save to Google Drive" (opens Google sign-in), "Save to my cloud storage" (sign-in dialog) and "Open from Google Drive" (not clicked).
- **Pending:** the cost of a second Download, preview vs download bytes, and Drive after sign-in. **Needs re-run after midnight UTC (7:00 PM ET).** RERUN-AFTER-RESET row 18 has been added.

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the code, restate the problem, push back where we're wrong, and choose fixes that fit how FreeDailyPro ships video tools.

Code to look at (`evidence/js/`):
- `VideoToGif.pretty.js`:
  - the size-cap search `J` L42–53 and `Ce` L54–80
  - the unused fit hint `le` L151/L184 and the over-cap toast L205–208
  - the `<video>` pre-check L234–248, which disables Create GIF at L485
  - the unlabeled selects (only `gif-start` and `gif-length` have `htmlFor`)
  - the static copy `q` L95–99
- `operations-P8Ty5WBe.pretty.js` `St` L766–804: the palette + paletteuse pipeline.
- `ffmpegEngine-DH91Xnxx.pretty.js` L217–218: 50 MiB / 200 MiB.

After you ship, rerun `scripts/vg-battery.js` and `scripts/vg-gate-kbd.js`, then `test-cases.md` (VG-01…VG-24).

## Intent

Someone has a clip and needs a GIF for a README, a chat thread, a ticket or a forum post that won't take video. They want a sharp, small, looping GIF on the first try, made on their own device. When there's a size cap, they want the tool to hit it and say what to change if it can't. They should leave impressed and see the pass as the obvious way to download more.

The engine delivers:
- A palette-based encode that looks good: 480 px / 12 fps defaults, 5 s in about 8 s including the engine load.
- Exact durations at every speed (2x → half, 0.5x → double).
- A true play-once flag, no upscaling, and correct portrait rotation.
- HEVC MOV, WebM and MKV on Chromium; clamped start/length; a working Stop.
- An honest "large" warning and a clear 50 MB upsell.
- The 2 / 5 / 8 MB caps land under the limit on reachable clips.

Trust is lost at the edges:
- three formats the page says it reads are refused at the door
- the size-cap hint that FAQ, Details and blog all promise never appears, and an unreachable cap ends over the limit at 200 px
- the YouTube video shows a different tool

## Why: what the evidence says

- **P1: AVI, WMV and FLV are advertised but refused.**
  - The Formats box says "Reads MP4, MOV, MKV, WebM, AVI, WMV, FLV".
  - All three test files (MPEG-4/MP3 AVI, WMV2, FLV1) got "couldn't be read as a video; it may be damaged… Try re-exporting it as MP4" and a disabled Create GIF, in Chromium and Firefox.
  - The cause is the browser `<video>` pre-check, not ffmpeg. Users with old camera or screen-capture files are told their file is damaged.
  - ezgif accepts all three.
  - On Safari the same pre-check likely also blocks MKV (unverified; WebKit can't be checked on this box).
- **P1: the Largest file promise breaks when the cap can't be met.**
  - FAQ ("If nothing fits, it reports how many seconds would"), Details → Limitations and the blog all promise a "clip of about N s would fit" hint.
  - The code builds that sentence (`le`) but never shows it.
  - Live (G08): 30 s, 640/15, cap 2 MB → **2.15 MB at 200 px / 5 fps**, below the 240 px menu minimum. The toast only says "Use a shorter clip".
  - Even when the cap is met, it prefers 6 fps over a shorter clip or lower width: 8 MB cap → 550 px at **6 fps**, 6.76 MB (15% of the budget unused), taking 42 s vs 23 s uncapped. The blog itself advises "reduce Length before you reduce width".
- **P1: copy and video describe a different tool.**
  - The drop zone says "over 200 MB may take longer…", while trial uses stop at 50 MB (MiB shown as "MB").
  - Tips say "Set Start and Length here rather than trimming first", while the >20 s warning, the Formats box and the blog all say to trim first with Trim Video.
  - The YouTube video (93 s, 7 views) shows:
    - a "Pro" badge and no settings at all
    - a Download / **Share** / New row (no Share live)
    - no GIF output
    - ≈40 s of outro, "200+ Free" tools
    - personal bookmarks and a file-picker listing
- **P2 (selected; full list in PRIORITIES.md):**
  - **Accessibility:** four selects without accessible names (axe critical ×4); result not announced; focus to body; unnamed progress bar.
  - **Next steps** point to Universal File Converter (documents) and Video Thumbnail Generator. The GIF Resizer & Compressor and GIF Speed, Reverse & Crop tools would fit.
  - **No share-result button**, no crop/caption, no "use current position".
  - **Locales:** English title, meta and tool body.
  - **Pair-page titles** say "Free".
  - **VideoObject** name ≠ YouTube title.
  - **Errors:** the non-video file error says "damaged or codec".
  - **Settings** survive New/Reset without a hint.
  - **Layout:** 9 px header overflow at 320 px.

## Outcomes we want

1. Every format listed under "Reads" converts, or the list shows only what the browser pre-check allows. An unplayable file goes straight to ffmpeg instead of being called damaged.
2. When a cap can't be met, the user sees how many seconds would fit at a readable size, and can apply it in one click. The tool never drops below the menu's minimum width without saying so.
3. Page, FAQ, blog and video describe the same controls, limits and trim advice. The video shows today's UI and an actual GIF.
4. Screen-reader users can name every control and hear the result. Keyboard users land on the result.
5. After the GIF is made, the next step is a GIF tool (resize, crop, speed), not a document converter.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PASS (with gaps)** | MEDIUM | 18 of 25 cases PASS. FAIL: AVI/WMV/FLV refused (G13–G15), cap ended over 2 MB (G08). PARTIAL: low-fps caps (G24/G25), non-video wording (G19). `findings/live-functional-findings.md` |
| 2 | Completeness | **PARTIAL** | MEDIUM | Has start/length, width, fps, speed, play once, size cap, Stop. Missing vs ezgif: AVI/WMV/FLV, crop, text, "use current position", URL input, loop count, chained GIF tools. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | LOW | Clear controls and clamping. Phones need one scroll to reach Create GIF (y=946 on a 584 px iPhone SE). Settings carry over silently after New/Reset. Cap runs take about 2× longer with only "Estimating…" status. |
| 4 | Layout | **PASS** | LOW | Clean two-column controls. 9 px header overflow at 320 px (site-wide). `screens/devices/` |
| 5 | Payment process | **PASS** | — | At 0 remaining (16:17 EST, `json/cap.json`): the row says "0 remaining today Get a Day Pass to download". Download → "Today's trial uses are done" cap dialog → "Buy Day Pass — $1" → email prompt "Day Pass, $1… Continue to payment" (stopped; nothing typed). Drive at 0 → same cap dialog. Cloud dialog: $4.99/month, needs sign-in. |
| 6 | Information correct | **FAIL** | HIGH | AVI/WMV/FLV "Reads"; fit-hint promise ×3; "over 200 MB" vs 50 MB; trim-first contradiction. `findings/desk-findings.md` table |
| 7 | Indexing | **PASS** | — | 200, self-canonical, in the sitemap (tool, 2 pair pages, blog), not noindex. GSC data is not available. |
| 8 | SEO | **PARTIAL** | LOW | Good title/meta/H1/JSON-LD. VideoObject name mismatch. Locale titles in English. Pair titles "Free". |
| 9 | Blog | **PARTIAL** | MEDIUM | /blog/video-to-gif (Oct 17, 2026) is accurate on controls but repeats the fit-hint promise and trim-first advice. |
| 10 | YouTube video | **PASS (low reach)** | LOW | P9s4XBNSB10 is embedded; 93 s, 7 views. |
| 11 | FAQ / guide | **PARTIAL** | MEDIUM | 6 FAQs + Details are mostly correct. Fit-hint promise (FAQ + Limitations) wrong; trim advice contradicts; "How to use it" is one thin line. |
| 12 | Video shows current tool | **FAIL** | MEDIUM | Old UI with no settings, Pro badge, Share button; never shows a GIF; personal data on screen. `findings/video-findings.md` |
| 13 | Storage | **PARTIAL (sign-in)** | — | Drive opens Google sign-in (not charged before sign-in). Cloud storage needs sign-in. Open from Google Drive not clicked. Untested beyond the sign-in wall. |
| 14 | Sharing | **N/A** | — | No share-result button (the old video had one). "Share this tool" is site-wide. |
| 15 | Downloads | **PARTIAL / pending** | — | Download worked with uses left: `noaudio.gif` (original name + .gif). Bytes vs preview and second download are pending (RERUN row 18). |
| 16 | Usage count | **PARTIAL / pending** | — | Create GIF free (≈30 runs, no change). First Download 0 → 1 used. Second-download charge unobserved; needs re-run after midnight UTC (7:00 PM ET). Counters are display-only evidence. |
| 17 | Category placement | **PASS** | — | Listed in Video Tools with the GIF tools. |
| 18 | Site section | **PASS** | — | Video Tools is right. |
| 19 | AI need / demand | **PASS** | — | Evergreen need (README/chat/ticket GIFs); traffic noted in the test plan; 2 pair landing pages. GSC data is not available. |
| 20 | Merge candidate | **N/A (keep)** | — | Core tool. Better to hand off to gif-resize-compress / gif-editor than to merge. |
| 21 | Remove? | **N/A (keep)** | — | Clear demand. |
| 22 | Duplicates | **PASS** | — | Pair pages are intended landing pages for the same tool; no duplicate tool (DUPLICATES.md: keep). |
