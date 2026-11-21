Sent: 2026-11-21 13:20 ET

# FDP-62 Screen Recorder (screen-recorder): deep test report for Claude

- **Written:** 2026-11-21 13:18 EST (box `date`, ET). Testing ran 2026-11-21 13:01–13:16 EST.
- **Tool:** https://www.freedailypro.com/tool/screen-recorder
  - TEST-ORDER row 62: **Premium Application**, Video Tools (breadcrumb "Video Tools"). Plan note "test-plan (unranked): SEO backfill 8 (GA top)". Duplicate group C17 (voice-recorder, camera-capture, screenshot-tool, video-studio).
  - Premium terms on the page: 2 trial uses a day, $3 Day Pass or $9.99 a month.
  - Video DEwAYXXSJ-c (embedded, 145 s, uploaded 2026-09-24). Blog /blog/screen-recorder "Record a 4-Minute Help-Center Walkthrough in Your Browser".
  - **GSC data is not available.** No API/MCP testing.
- **How it works:**
  - Toggles: Camera bubble, 3-2-1 countdown and Microphone, all on by default. A mic picker appears with more than one input.
  - Start Recording → the browser share picker → live preview. Either drag a region and press Record Selected Region, or press Record Full Capture.
  - Countdown → timer, mic level meter, Pause/Resume, Stop.
  - The player (`<video controls>`) shows the clip. Then Download Recording (gated) or Record Another.
  - MP4 (H.264/AAC) when the browser can record it, otherwise WebM. All local.
- **Testers:**
  - Desk: page copy (7 FAQs, how-to, limits, privacy), JSON-LD, blog, JS (`ScreenRecorder-CejnW5HL.js`, `mediaPermissions`).
  - Playwright. Headless browsers here have no real screen picker, so `getDisplayMedia` was replaced **in the test browser only** by a canvas stream stub (1280×720, four colour quadrants, frame counter, moving bar, plus a 440 Hz "system audio" track). The mic and camera are the browsers' fake devices. Nothing on the site was changed.
    - `zero.json` (Chromium) + `zero-firefox.json`: at the cap (2/2). Full take with countdown and pause; region take without camera/countdown; Download → cap dialog.
    - `left.json` (Chromium, fresh context with 2 uses left on try 5): full take with camera + mic + pause → Download; Record Another → region take with camera → Download; reload → take → Download.
    - `left-firefox.json`: no Firefox context with uses left in 40 tries.
    - `quickbuy.json`: Day Pass (stopped at the email prompt) and Monthly (stopped at Stripe).
    - `nodm.json`: no `getDisplayMedia`, as on phones.
    - `deny.json`: camera and mic refused.
    - `stopcheck.json`: Stop with mic on/off.
    - `px62-wk.js` / `px62-wk2.js`: WebKit crash isolation.
  - Downloads checked with ffprobe, frame grabs and volumedetect.
  - Video frame sheet and frames reviewed. Matrix: 10 devices (WebKit rows crashed, see below), 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** no Drive, cloud or account feature on this page (verified). Paid-pass output was stopped at the email prompt and at Stripe (added to SIGNIN-NEEDED.md).
- **Not tested here — WebKit / Safari / iPad:** Playwright's Linux WebKit crashes the tab on this page at load. The page calls `enumerateDevices()`, and the same call crashes WebKit on example.com (px62-wk2.js), so this is the test browser's media stack, not proven to be a site bug. Voice Recorder crashes the same way. **Needs a real Safari (Mac) check.**
- **RERUN-AFTER-RESET:** none. Behaviour with uses left and at the cap was observed today.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for someone who needs a quick walkthrough clip, and whether the clip makes them want the pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging and full-quality results/previews at 0 trial uses are P1 gate gaps (Nov 21).

**P1 — where to look:**

1. **The full recording is playable at 0 trial uses, in a player that offers its own download.**
   - At the cap (zero.json Z05: 5.06 s, 642×290; zero-firefox.json), the finished clip plays in full in `<video src=blob: controls>`. Only the "Download Recording" button is gated.
   - The element has no `controlsList="nodownload"` and no context-menu block (code; searched for `controlsList`). Chrome's native control menu (⋮ → Download) and right-click "Save video as…" save the blob directly.
   - I couldn't click the browser's native menu headless, so this part is code-plus-standard-browser behaviour. A 10-second manual check in Chrome confirms it.
   - Per the Nov 21 rule this is a full-quality result at 0.
   - Options: `controlsList="nodownload"` + `onContextMenu` prevent (deters casual saving), and/or play only the first N seconds at 0 uses.
2. **Per-page-load charging.**
   - left.json: take 1 → Download, one usage.log POST, count 2/2.
   - Record Another → a region take with the camera bubble → Download Recording saved a second full file at 2/2, with **no POST and no cap dialog** (L04).
   - After a reload, Download showed the cap dialog (L06).
   - Same mechanism as FDP-61: `tryUse` logs once per tool per page load. Decide on one use per new recording.

**P2 — where to look:**
- **Video DEwAYXXSJ-c is off-brand and outdated:**
  - It demonstrates by recording a third-party game-guide site (anime character art, "ULTIMATE … DPS").
  - The browser share picker lists the presenter's other open tabs. Bookmarks bar and Windows taskbar are visible.
  - The UI is older: no Camera bubble / countdown / Microphone toggles, and a "Pro" badge.
  - Title "Free Step-by-Step Walkthrough", description "Try Screen Recorder free" / "Free daily uses" / "Subscribe for the next free tool", tag "PDF tools".
  - Re-record on a FreeDailyPro page, in a clean browser profile, with tab-only sharing.
- **MP4 claim not verified here:** the FAQ says MP4 (H.264/AAC) "is common in recent Chrome, Edge and Safari". Playwright's Chromium has no H.264, so every take here was WebM VP9/Opus (correctly labelled "downloads as WebM…"). Please confirm MP4 in branded Chrome and Safari.
- **Safari/iPad untested** (see above). Real-device check needed before claiming Safari support.
- **Locale pages:** H1, breadcrumb, trial strip and Quick Buy are translated. The subtitle, Premium line, toggles, Start Recording and the FAQ stay English (es screenshot). The EU consent banner shows in de-DE/fr-FR (screenshots).
- **SEO:** title "Screen Recorder Online - Record and Download a Video" (52) has no brand. Meta is 83 chars (short, repeats the subtitle). The OG image is generic. FAQPage has only 7 entries.

**P3:**
- **Unsupported browsers:** with no `getDisplayMedia` the page explains that phones can't record (good), but Start Recording stays enabled and only toasts "Screen recording isn't supported in this browser" (nodm.json). Hide or disable it.
- **Counter jump (observation, as in FDP-61):** the fresh context showed "2 remaining today", and its first download set 2/2 (one POST). The server appears to pool counts by network/browser.
- **axe:** desktop label-content-name-mismatch (serious), region (moderate). Pixel 7 color-contrast on an ad caption (keep reserved ad slots; fix the caption colour). ja desktop 1369 px (site-wide).

## Intent

A support person, teacher or developer wants to show a process: share a tab, talk over it, maybe put their face in the corner, and get a file to send. No install, no upload. If the first clip is clean and easy, the $3 day pass is an easy buy.

## What works (verified)

- **Recording:**
  - Full capture 1280×720 VP9 + Opus.
  - Pause removes the paused stretch: timer 00:08 and file 8.56 s for a 17 s wall-clock take with a 3 s pause.
  - Countdown 3-2-1.
  - Mic level meter moves (aria-valuenow 2–53).
  - Duration is written into the WebM (ffprobe).
- **Region:** the drag selection on a letterboxed preview maps correctly. Output 642×290 shows exactly the red quadrant + "FRAME" label (frames-L02-L04.png). Record Selected Region only appears after a drag.
- **Camera bubble:** round, white ring, bottom-right, in both full and region takes.
- **Audio:** the system-audio track (stub) and the mic are mixed into one track. Audio is present (volumedetect).
- **Denied permissions:** clear toasts for camera and mic ("…set Camera to Allow, then reload"). The take continues with video + system audio.
- **File name** has the date and time (`screen-recording-2026-11-21_13-05.webm`). The "Recorded 00:08 — downloads as WebM…" note is accurate.
- **Firefox** records the same way (zero-firefox.json).
- **Gate at the cap:** Download → "Today's trial uses are done" (Monthly $9.99 / Day Pass $3), no charge.
- **Quick Buy:** Day → email prompt (stopped); Monthly → Stripe (stopped).
- **Copy accuracy:** 30-minute reminder (`de >= 1800`), 200 MB warning, 20 px region minimum, mic picker: all match the code.
- **Blog:** accurate and useful (region, pause, camera bubble, WebM vs MP4, privacy tips).
- **Layout:** the tool is above the fold on desktop (no hero). Phones show the "phone browsers don't allow it" note.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Full/region, camera bubble, mic mix, pause verified (Chromium, Firefox). Safari untested. |
| 2 | Completeness | PASS (minor) | Near Loom/Screencastify basics. No in-page trim, no cursor highlight, no system-audio hint per OS. |
| 3 | Ease of use | PASS | Clear toggles, preview, region. Start not disabled on unsupported browsers. |
| 4 | Layout | PASS | Above the fold; phones fine. |
| 5 | Payment process | PASS / stopped | Cap dialog; Day Pass email prompt (stopped); Monthly → Stripe (stopped). |
| 6 | Information correct | PARTIAL | Matches the code. MP4-in-Chrome claim unverified here. |
| 7 | Indexing | PASS | 200, index, sitemap, canonical self. |
| 8 | SEO | PARTIAL | No brand in title, meta 83 chars, generic OG. |
| 9 | Blog | PASS | Accurate walkthrough. |
| 10 | YouTube video | PASS | DEwAYXXSJ-c embedded + VideoObject. |
| 11 | FAQ / guide correct | PASS | 7 FAQs match behaviour. |
| 12 | Video shows current capability | FAIL | Old UI, third-party game site, other tabs visible, "Free". |
| 13 | Storage | N/A | No save/history (verified); clip lives in page memory. |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | PASS | WebM files valid with duration, audio, region size. |
| 16 | Usage count | FAIL (P1) | Once per page load; second take free (L04). Full clip playable at 0. |
| 17 | Categorization in section | PASS | Video Tools / Premium. |
| 18 | Correct section of site | PASS | Next: Trim & Cut, GIF, Compress links. |
| 19 | AI need and demand | PASS | High ("screen recorder online", Loom alternative). |
| 20 | Merge better? | No | Distinct from voice-recorder / camera-capture; video-studio is the heavier editor. |
| 21 | Remove? | No | Useful, Premium-worthy. |
| 22 | Duplicates | None | C17 members do different jobs. |

## After fixes, rerun

- `TRIES=40 px62-live.js left` (expect a charge per new take, cap on take 3).
- `px62-live.js zero` (player at 0 should not offer a download).
- Real Safari: record a tab, check the MP4 output and the camera bubble.
