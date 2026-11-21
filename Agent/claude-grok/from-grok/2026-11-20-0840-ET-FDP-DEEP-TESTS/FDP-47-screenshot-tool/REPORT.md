Sent: 2026-11-21 06:49 ET

# FDP-47 Screenshot Capture & Editor (screenshot-tool): deep test report for Claude

- **Written:** 2026-11-21 06:48 EST (box `date`, ET). Testing ran 2026-11-21 06:22–06:46 EST.
- **Tool:** https://www.freedailypro.com/tool/screenshot-tool. Row 47 of TEST-ORDER.md: **Premium Application**, Image Tools, plan note "test-plan (unranked): GA top-traffic". Duplicate group **C17** (screen-recorder, voice-recorder, camera-capture, video-studio).
  - Video: lBBMlLTJYMw. Blog: /blog/screenshot-tool ("Capture Clean Screenshots for Bug Reports and Guides").
  - **GSC data is not available.**
- **Offer:** 2 trial uses a day (Premium scope), charged on Download or Copy; capture, crop selection and the editor are open. $3 Day Pass / $9.99 monthly.
  - Everything runs in the browser: `getDisplayMedia` → canvas; crop; editor (pencil, highlighter, arrow, box, text, pixelate, rotate, zoom, undo, fullscreen); "Capture whole page" stitches frames while the user scrolls (16,000 px cap). PNG or JPG.
- **How it was tested (important):** headless Chromium/Firefox/WebKit on this Linux box can't open a real screen-share picker (`getDisplayMedia` → NotSupported/NotReadable, also tried tab/desktop auto-select flags under Xvfb: `st-probe*.js`).
  - So the main runs replace `navigator.mediaDevices.getDisplayMedia` **in the test browser only** with a canvas stream that paints a known test screen (four colours, "Jane Doe 555-0134", an account number), a scrolling 3,120 px page, or a blank page. The site's own code does everything after that.
  - The real picker path was checked for its error handling only ("Screenshot wasn't taken (permission denied or cancelled)"). Confirm real capture by hand on desktop Chrome/Safari.
- **Testers:**
  - **Desk review:** copy, FAQ (5), Details, JSON-LD, locales, blog, JS chunk ScreenshotTool (+ useShareGate, ToolPage).
  - **Headless Playwright:** one long page load with 9 cases plus reload-to-cap and passes (main.json); one-action charge checks in fresh contexts (check-*.json/console); mobile without `getDisplayMedia` (mobile.json); real-picker error (real*.json); Firefox/WebKit subsets.
  - **Checks:** every downloaded image opened and measured; clipboard image read back; a privacy request scan; the matrix (10 devices, 11 locales, 6 geo contexts, axe); the video, frame by frame.
- **Constraints kept:** guest only; no sign-in, card or email; stopped at the Day Pass email prompt and the Stripe Checkout title; no ad clicks; no API/MCP calls; no site or repo changes.
- **Sign-in (untested):** paid-pass behaviour only (no badge, unlimited). This tool has no Save to Drive, cloud save or Open from Drive (none rendered in any state; verified live).
- **Nothing pending a usage reset**, so there's no RERUN-AFTER-RESET row.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Push back where the product intent differs.

**Owner context:** Santosh treats per-page-load charging and full-quality results at 0 trial uses as P1 gate gaps. Copy and results count as trial uses. The "Created with FreeDailyPro.com" badge is intentional, so badge points below are owner questions only.

**Code to look at:**
- **ToolPage gated download** (`vt`, used as `Ht` and inside `ke`) and **useShareGate** (`gateShare` → `tryUse()` for Copy): both charge once per tool per page load and don't re-check the cap afterwards. Same root cause as FDP-44/45/46.
- **`ScreenshotTool-IZ7Q-6dY.js`:**
  - `Rt()` only learns at click time that `getDisplayMedia` is missing ("Screen capture isn't supported in this browser"). Nothing on the page says so up front.
  - `Lt()` draws the highlighter as separate round-capped segments at alpha 0.35, so overlaps show as dark dots.
  - `pe()` (rotate) clears the undo stack (`V([])`).
  - `Dt()` copies the canvas blob without the badge, while Download adds it.

**After you ship:** rerun `scripts/st-live.js main` with a fresh context (expect +1 per new result and the cap dialog at 2/2 without a reload), then `st-live.js mobile` and test-cases.md. Check one real capture by hand.

## Intent

Someone wants a quick screenshot of a bug, a page or a step, cropped, marked up and with private details hidden, without installing anything and without uploading the image.

The core delivers that well:
- crop selection honoured exactly (a 412×76 css-px box → 590×109 px file, Download and Copy alike)
- a full editor: pencil, highlighter, arrows, boxes, multi-script text (Devanagari, Arabic, CJK shaped correctly), pixelate that makes "Jane Doe 555-0134" unreadable, rotate, zoom, undo, PNG/JPG
- whole-page stitching that lined up 11 frames into a correct 1,280×3,120 px image (rows 0–51 in order, no doubles), with a clear note and a sensible message for a page that wasn't scrolled
- nothing uploaded (no request carried image data)

What undercuts it:
- **Charging per page load:** after the first charged result, 6 more results came out of the same page load, even while the strip said "0 remaining today".
- **Android phones can't use it at all**, and the page doesn't say so, while it sells a $3 / $9.99 pass and its how-to says "especially on mobile".
- **The video is from an older version** (light theme, "Screenshot Tool", pencil/highlighter only, "10 free uses daily").

## Why: what the evidence says

- **P1, per-page-load charging (gate gap).**
  - main.json: the first Download moved the counter 0→2 (see the counter note below). Then 6 more results in the same page load with no dialog: crop Download (C03), Copy (C04, 1280×720 in the clipboard), editor PNG and JPG (C05), the stitched whole page (C06) and a fresh capture's Download (C09). The strip showed "0 remaining today" throughout.
  - After a reload: Download, Copy and the editor Download all open the cap dialog (reloads, copyAtCap, editorAtCap).
  - Clean one-action checks (fresh contexts): one Download, Copy or editor Download = one `usage.log` POST.
- **P1, Android phones: core flow unavailable, no upfront notice, pass still sold.**
  - caniuse (checked today): `getDisplayMedia` is not supported on Chrome for Android, Samsung Internet or Firefox for Android; Safari on iOS supports it from 27.0.
  - mobile.json (Pixel 7 / iPhone 14 Pro Max profiles with `getDisplayMedia` removed, as on Android): the page shows the delay buttons and Take Screenshot; the user only learns from a toast after tapping: "Screen capture isn't supported in this browser" (M-*.png). The strip with "Day pass $3 / Monthly $9.99" is shown above it.
  - The how-to copy says "tap Fullscreen first … especially on mobile". JSON-LD says "operatingSystem: Any (Web Browser)".
  - This is GA top-traffic, so phone visitors are a real share. iOS 27 wasn't tested on a device (unverified).
- **P2 items:**
  - **Video (check 12 FAIL):** 112 s, uploaded 2026-09-23. Old light UI, H1 "Screenshot Tool", only pencil/highlighter (no arrow, box, text, pixelate, whole-page), overlay "Capture your screen and download the screenshot — 10 free uses daily!" (now Premium, 2 trial uses). The title and description say "Free"; about 30 s end card "200+ Free Productivity Tools".
  - **Locale pages:** H1 and tool name are translated; title, meta, the tool controls (Take Screenshot, Capture whole page, delay help), How to use, FAQ headings and the video title stay English on all 10 locales.
- **Owner questions (badge is intentional):**
  - Every download carries **two** badges (top right and bottom right). On a small crop (590×109) they cover part of the subject ("555-0134"; K-download-*.png).
  - **Copy gives a clean, unbadged image** while Download is badged (K-copy-clipboard.png). Copy is charged, so it isn't a gate gap, but the two paths differ.
- **P3 items:**
  - **Counter display:** in 2 of 5 fresh contexts the strip went 0→2 after a single action with a single `usage.log` POST (main.json C02, check-copy.json). It looks like the server count for a matched device being pulled in, not a double charge. Counters are display-only evidence (unverified).
  - **Highlighter dots** where segments overlap (C05-edited PNG). **Rotate clears undo.**
  - **Copy:** meta description (100 chars) and the subtitle undersell the tool (no whole-page, arrows, text or pixelate). Generic og-default image. FAQ has nothing on phones.
  - **Pixelate** uses 12 blocks across the box with a 6 px minimum, so a very small box over small text gets small blocks. Consider a solid "redact" fill option for secrets.
  - **iPhone SE 9 px overflow** (button row); /ja 3 px; axe label-content-name-mismatch (1).
  - **Ad creative "Download Template Free"** sat in the right rail beside the tool in the WebKit run. Keep the slot; block download-lookalike categories.

## Outcomes we want

1. Each new result (Download or Copy) takes one trial use; re-downloading the same result stays free; at the cap, the dialog shows without needing a reload.
2. Phone visitors on browsers without screen capture see a clear note before they tap (and before any pass offer), plus a pointer to the right tool (for example Camera Capture, or "use your phone's screenshot, then Resize & Crop"). The copy and JSON-LD stop implying it works everywhere.
3. A new video of the current editor (arrows, text, pixelate, whole-page) with "trial uses" wording.
4. Translated tool controls, title and meta on locale pages.
5. Owner decision on the double badge and the unbadged Copy.

## The 22 checks

| # | Check | Result | Evidence / note |
|---|---|---|---|
| 1 | Capability | PASS (desktop) / FAIL (Android) | Desktop flow works end to end with the stub screen (real picker by hand). Android has no `getDisplayMedia`. |
| 2 | Completeness vs competitors | PASS | Compared with Awesome Screenshot / GoFullPage (extensions), Snipping Tool and Markup Hero: in-browser editor with pixelate and stitching, no upload, no install. Missing vs extensions: automatic full-page scroll (explained honestly), blur/solid redact choice, saved history. |
| 3 | Ease of use | PASS (minor) | Clear flow, delay explained, stitch messages are good. Long helper sentences. |
| 4 | Layout attractiveness | PASS (minor) | Clean; iPhone SE 9 px overflow. |
| 5 | Payment process | PASS / stopped | Cap dialog → Day Pass $3 email prompt (stopped); Quick Buy monthly → Stripe Checkout (stopped). |
| 6 | Information correct | PARTIAL | "Especially on mobile"; "Any (Web Browser)"; no phone limitation stated. The rest is accurate and honest. |
| 7 | Indexing | PASS | 200, canonical self, hreflang 10 + x-default. |
| 8 | SEO | PASS (minor) | Title 65; meta 100 chars and undersells; five JSON-LD types; og-default; English locale titles. |
| 9 | Blog exists and accurate | PASS (minor) | Accurate but generic ("capture per the live controls"); doesn't mention whole-page capture or the pixelate tool by name. |
| 10 | YouTube video exists | PASS | lBBMlLTJYMw, embedded. |
| 11 | FAQ and guide correct | PARTIAL | 5 accurate answers; nothing on phone support; "especially on mobile" in How to use. |
| 12 | Video shows current capabilities | **FAIL** | Old UI and tool set; "10 free uses daily". |
| 13 | Storage | PASS (N/A) | Nothing stored or uploaded; no cloud save on this tool. |
| 14 | Sharing | PASS | Share this tool; Copy to clipboard. |
| 15 | Downloads | PASS | Correct PNG/JPG, crop honoured, stitched page correct; badge placement is an owner question. |
| 16 | Usage count | **FAIL (P1)** | Per page load: 7 results for one charge, while the strip said 0 remaining. |
| 17 | Categorization in section | PASS | Image Tools / Premium Applications ("Capture & Create"). |
| 18 | Correct section of site | PASS | Image Tools breadcrumb. |
| 19 | AI need/demand | PASS | GA top-traffic; chat assistants can't capture a user's screen. |
| 20 | Merge better? | No | Distinct from screen-recorder (video) and camera-capture (camera). |
| 21 | Remove? | No | Top traffic. |
| 22 | Duplicates | C17: none | Keep. Cross-link Screen Recorder (already in "When not to use it") and, for phones, Camera Capture / Resize & Crop. |
