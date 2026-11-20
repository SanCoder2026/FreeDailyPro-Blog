Sent: 2026-11-20 08:40 ET

# FDP-14 Camera Capture (camera-capture): deep test report for Claude

- **Written:** 2026-11-19 14:43:03 EST (box `date`, ET).
- **Tool:** https://www.freedailypro.com/tool/camera-capture. Row 14 of TEST-ORDER.md: Pro, Image Tools; test-plan rank 13, "50 clicks 2,439 impr; many 'take photo online' queries" (quoted from TEST-ORDER, not re-verified); clusters C06 and C17. **GSC data is not available.**
- **Classification:** Professional Tool, Image Tools, gated.
  - Download Full Photo, Download Crop, Copy and Save to Google Drive are all blocked at 0 remaining, consistent with /terms and the Oct 30 owner policy.
  - Start, Capture, Crop and Retake are free.
- **Testers:**
  - **Desk review:** tool page, 9 locales and /ar, blog, /terms and /faq; the CameraCapture chunk and mediaPermissions code; WebSearch.
  - **YouTube video:** metadata, 20 frames, contact sheet and crops.
  - **Headless Playwright with a known fake camera (test card)** covering:
    - capture and crop pixel checks
    - camera picker and Front/rear toggle
    - JPG, Cancel and Retake
    - the no-camera and denied cases (Firefox)
    - the gate at 0 and the cloud buttons
    - keyboard, axe, and the phone flow with touch crop
    - the matrix: 10 profiles, 10 locales + /ar, 6 geos, axe
- **Constraints kept:** guest only, no sign-in, no card or email entered, no ad clicks, no API or MCP calls, no site or repo changes.
- **Sign-in:** "Save to my cloud storage" stops at an in-page dialog ("Sign in with your email first … Sign in"). I didn't sign in, so that feature is untested. No other URL or feature needed sign-in.
- **Pending: RERUN-AFTER-RESET row 14.** Every fresh context loaded at 0 remaining (counted per network, per /terms). Still unobserved: cost per export with uses left, the corner badge on downloaded photos, and real file names. Needs a re-run after midnight UTC (7:00 PM ET).

## How to work with us

You know the codebase better than this report does. Treat these findings as evidence and judgment, not orders. Inspect the real component, restate the problem, challenge anything that looks wrong, and pick the fix that fits how FreeDailyPro has shipped similar work.

Components to look at:
- **CameraCapture** (`evidence/js/CameraCapture-0Z_gFqDj.pretty.js`):
  - the idle block and steps panel order on phones
  - the Front/rear handler `Q`/`Z` (L130–153) and picker sync
  - focus after Start and after Capture
  - `img` alt
  - crop interaction (L191–239)
  - the JPG checkbox only while live (L369–379)
  - `URL.createObjectURL` in render (L466)
- **Page copy:** FAQ, How-to, meta, the blog and the video; the trial-mark disclosure.
- **The shared cap dialog / toast text** for Copy actions.

After you ship, rerun `test-cases.md` (CC-01…CC-24) and the RERUN row.

## Intent

People search "take a picture online" because they need one photo right now, often a headshot for a form, from a laptop or phone, without installing anything. The tool's core is solid: exact captures, a correct crop, 4K requests honoured, clear permission help, nothing uploaded. Two things undercut it:
- On a small phone, the camera button and then the Capture button sit below the fold.
- The page and blog sell headshots and ID crops but never say, before the user starts, that a trial download carries "Created with FreeDailyPro.com" badges in two corners. The user finds out only after posing and capturing.

## Why: what the evidence says

- **Core is correct (PASS):**
  - The 1280×720 capture matches the test card exactly and isn't mirrored.
  - Mouse and touch crops give the right region and size.
  - JPG works.
  - Cancel and Retake work.
  - The permission-denied and no-camera messages are clear.
  - The camera picker switches devices.
- **P1: first screen on phones.** iPhone SE: Start Camera at y≈828 on a 568 px screen. After Start, Capture is at y≈795, and the result buttons run down to y≈1187.
- **P1: undisclosed trial mark on photos.**
  - After Capture the page shows "This download will carry small "Created with FreeDailyPro.com" badges in the top and bottom right corners."
  - The FAQ, How-to, meta and blog (an HR-portal headshot) don't mention it.
  - The mark is policy. The fix is wording: disclose it up front. Whether the mark lands on the photo is to be verified after the reset.
- **P1: video privacy.** The walkthrough shows a real person (face partly covered by a sticker), the recorder's camera model and an old UI with "free uses" badges.
- **P2:**
  - The Front/rear toggle has no effect on laptops and leaves the picker on "Choose a camera".
  - Focus is lost after Start/Capture; the captured image has no alt (axe critical); crop is mouse/touch only; the picker is unnamed.
  - The JPG choice disappears after capture.
  - The Copy cap dialog says "downloading".
  - Missing countdown, square/aspect lock and mirror (competitor baseline).
  - VideoObject date and name mismatch.
  - 9 English locale copies.

## Outcomes we want

1. On any phone, Start Camera is on the first screen, and the preview and Capture sit together on one screen.
2. Before camera access, the user knows what a trial download looks like (badges) and what a pass changes.
3. Selfie and headshot users can take a hands-free, square photo: a countdown and a 1:1 / passport aspect option.
4. Keyboard and screen-reader users can complete the flow: focus moves to the next control, images have alt text, and the crop has a keyboard path or a preset.
5. The video, blog and FAQ describe the current tool without personal data.

## The 22 checks

| # | Check | Result | Severity | Evidence |
|---|---|---|---|---|
| 1 | Capability | **PASS** | — | Exact capture, correct crops (mouse and touch), JPG, picker, Cancel/Retake, error messages. `findings/live-functional-findings.md`, `json/desk-probe.json`, `json/ui.json` |
| 2 | Completeness vs. competitors | **PARTIAL** | MEDIUM | No countdown, square/aspect lock, mirror or keyboard shutter (Webcam Toy has all of these). Strengths: rear camera, picker, 4K, crop and copy. `findings/desk-findings.md` |
| 3 | Ease of use | **PARTIAL** | HIGH | Simple flow, but on phones the key buttons are below the fold; the JPG choice vanishes after capture; Front/rear does nothing on laptops. |
| 4 | Layout attractiveness | **PARTIAL** | MEDIUM | Clean on desktop. On iPhone SE the steps panel and price lines push the tool down; 9 px header overflow (site-wide). `findings/devices-locales-findings.md` |
| 5 | Payment process | **PASS (up to the cap dialog)** | — | The cap dialog offers Monthly $4.99 / Day Pass $1, matching /pricing. Stopped there; no Stripe, no card. |
| 6 | Information correct | **PARTIAL** | HIGH | FAQ facts hold (file names in code, 4096×2160, permission text). Missing the trial badge on photos; VideoObject date/name mismatch; the Copy dialog says "downloading". |
| 7 | Indexing | **PASS** | — | 200, self-canonical, in the sitemap with the blog. **GSC data is not available.** |
| 8 | SEO | **PARTIAL** | MEDIUM | Strong title and meta for "take a picture online", 7-question FAQPage. The H1 lacks the query words; 9 English locale copies with a foreign `lang`; video schema mismatch. |
| 9 | Blog post | **PARTIAL** | MEDIUM | /blog/camera-capture: accurate steps and a good headshot guide. It omits the corner badge and pushes two more tools (two more trial uses, also marked). |
| 10 | YouTube video exists | **PASS** (low reach) | LOW | qMZFDYLCLfg, 59 s, 6 views, embedded. |
| 11 | FAQ / usage guide | **PARTIAL** | MEDIUM | Accurate and practical; it lacks the mark and trial-use cost. |
| 12 | Video shows current capabilities | **FAIL** | HIGH | Old UI and "free" badges, a real person's face partly visible, the camera model shown, 19 s outro. `findings/video-findings.md` |
| 13 | Storage | **PASS** | — | No upload in code or the filtered network list; no gallery, as stated. Cloud storage is a paid, sign-in add-on (untested). |
| 14 | Sharing | **N/A** | — | No share-result feature (only "Share this tool"); Copy of the crop is the sharing path. |
| 15 | Downloads | **PARTIAL (pending)** | — | Blocked at 0 as designed. File name, format and badge not observable → RERUN row 14. |
| 16 | Usage count | **PASS (at 0) / pending (with uses)** | — | At 0: Download Full, Download Crop, Copy and Drive all gated, count 10 → 10 (14:28–14:40 EST). Matches /terms and the Oct 30 policy. Cost with uses left is pending. Counters are display-only. All starting counts were 10 used. |
| 17 | Categorization | **PASS** | — | Image Tools. |
| 18 | Location in site | **PASS** | — | Breadcrumb, "Next: Passport Photo Maker", Document Scanner upsell, blog. |
| 19 | AI need / demand | **PASS (no AI needed)** | — | High demand (rank 13). An optional background blur or auto-crop-to-face could be a Premium idea later. |
| 20 | Merge? | **N/A: keep** | — | C17 tools take different inputs; C06 OCR is a different job. |
| 21 | Remove? | **N/A: keep** | — | Demand and a correct core. |
| 22 | Duplicates | **PASS** | — | No duplicate. Its listing under C06 in DUPLICATES.md is a cluster artefact (it does no OCR). |

## Devices, platforms, countries and languages

Full matrix: `evidence/findings/devices-locales-findings.md`.
- All 10 profiles return 200.
- The only layout issue is the phone first screen (plus the site-wide 320 px header).
- Geo contexts are identical (English, USD).
- Locale URLs are English copies.

**Ads:** keep them in reserved fixed-height slots after the result buttons. Never put them between the preview and Capture, or between a crop and its download buttons.

## Suggested direction (interpret freely)

1. **P1: phone first screen.** Below about 640 px:
   - Put Start Camera directly under the H1, or collapse the "How it works" panel into one line.
   - When the camera is live, scroll the preview into view with Capture overlaid or directly under it.
   - After Capture, keep Download/Crop next to the image.
2. **P1: disclose the mark early.**
   - Add one line near Start Camera, plus an FAQ answer: "Trial downloads carry small "Created with FreeDailyPro.com" badges in the top and bottom right corners; a Day Pass or Monthly removes them."
   - Add the same note to the blog's headshot example.
   - Santosh may also want to decide whether face and headshot photos should carry the mark at all.
3. **P1: re-record the video** with a test card or object, in a clean profile, showing the current UI.
4. **P2:**
   - Hide or disable Front/rear when the track has no `facingMode` (or only one camera), and keep the picker value in sync.
   - Move focus to Capture after Start and to Download after Capture; add `alt` ("Captured photo", "Cropped photo").
   - Add aspect presets (Free / 1:1 / passport) that also give a keyboard path to cropping.
   - Add a 3-second countdown and a mirror toggle.
   - Allow the PNG/JPG choice at download time.
   - Name the picker.
   - Revoke blob URLs.
   - Change the Copy cap text to "copying".
   - Fix the VideoObject date and name.
   - Translate or de-list the 9 locales.

## Constraints

- Say "Professional Tools", "Premium Applications" and "trial uses"; never "free tools".
- Do not remove ads; use reserved slots.
- Charging Copy is owner policy, not a bug. Only the wording is in scope.
- Counters are display-only evidence.

## Process

Inspect CameraCapture → restate → propose → implement → verify:
- `scripts/cc-ui.js`, `scripts/cc-cameras.js` and `scripts/cc-kbd.js` (no trial use)
- `scripts/cc-probe.js` (exports; uses trial uses when any are left), then `scripts/cc-inspect.py`
- `test-cases.md`
