Sent: 2026-11-21 13:37 ET

# FDP-63 Color Picker from Image (color-picker-image): deep test report for Claude

- **Written:** 2026-11-21 13:35 EST (box `date`, ET). Testing ran 2026-11-21 13:21–13:34 EST.
- **Tool:** https://www.freedailypro.com/tool/color-picker-image
  - TEST-ORDER row 63: **Professional Tool**, Design & Marketing. Plan note "test-plan (unranked): SEO backfill 9". Duplicate group C21 (CSS/colour generators).
  - Terms on the page: 10 trial uses a day, $1 Day Pass or $4.99 a month.
  - Video njX53TSw5mA (embedded, 86 s, uploaded 2026-09-30). Blog /blog/color-picker-image "Pull an Exact Brand Red from a Packaging Photo" (200).
  - **GSC data is not available.** No API/MCP testing.
- **How it works (live + `ColorPickerImage-DP4amtAo.js`):**
  - Drop/browse an image, "Open from Google Drive", or "Take photo with camera" (a file input with `capture="environment"`; on desktop it opens the file chooser).
  - The image is drawn to a canvas (max 500 px tall, object-contain). Click/tap a pixel → HEX, RGB, HSL and **CMYK** panels, each with a copy button.
  - A **magnifier** follows the pointer (8× view). **Arrow keys** move the pick by 1 px, Shift+arrow by 10.
  - "Main colors in this image": up to 8 swatches with their share; click one to show its values.
  - Copy is the charge point (`useShareGate` → export gate → `tryUse`). Upload, pick, magnifier and palette are not charged.
- **Testers:**
  - Desk: page copy (FAQ, how-to, limits, privacy), JSON-LD, blog, JS.
  - Playwright, built test images with known pixels (`make63.py`: quadrants, 4000×3000, JPEG q60, 25 % alpha, EXIF orientation 6, 300×3000, 1×1, a non-image).
    - `zero.json` (Chromium) + `extra-firefox.json`: at the cap (10/10).
    - `left.json` (Chromium, fresh context with 10 uses left) and `left-firefox.json`.
    - `cases.json` / `debug.json`: pixel accuracy, mapping, keyboard. (`cases.json` picks with no values were clicks scrolled off screen, a script artifact; `debug.json` repeats them with the canvas scrolled into view.)
    - `touch.json`: tap-to-pick on Pixel 7 (Chromium) and iPhone 14 Pro Max (WebKit).
    - `drive.json`, `camera.json`, `quickbuy.json`.
  - Video frame sheet; matrix: 10 devices, 10 locales + /ar probe, 6 geo contexts, axe.
  - **Banner, layout and locale findings were checked against the screenshots, not the script flags.**
- **Constraints kept:** guest only. No sign-in, card or email entered. No ad clicks. No site or repo changes.
- **Sign-in (untested):** "Open from Google Drive" opens Google sign-in (accounts.google.com, "to continue to freedailypro.com"); stopped there. Paid-pass output stopped at the email prompt and Stripe. Both in SIGNIN-NEEDED.md.
- **RERUN-AFTER-RESET:** none. Behaviour with uses left and at the cap was observed today.

## How to work with us

You know this codebase. Treat this as evidence and judgment, not orders. Each item says why it matters for a designer or marketer who needs one exact colour from a photo, and whether the tool makes them want the pass.

**Owner context:** copy and results count as trial uses (Oct 30). Per-page-load charging is a P1 gate gap (Nov 21). A full-quality result visible at 0 trial uses is a **pending owner question** (Orchestrator, Nov 21 1:19 PM); a real save/download at 0 is P1.

**P1 — where to look:**

1. **Per-page-load charging.**
   - left.json (Chromium): first copy (HEX) → one `usage.log` POST, 0/10 → 1/10.
   - Then RGB, HSL, CMYK, a palette swatch copy, and a copy from a **second image** in the same load: all copied (clipboard verified), **no POST, count stayed 1/10** (L03–L05).
   - After a reload the next copy charged again (1/10 → 2/10, L06).
   - Firefox shows the same pattern (left-firefox.json L03–L05: only the first copy POSTed).
   - Same mechanism as FDP-61/62: `tryUse` logs once per tool per page load. Decide what one use is here (one copy, or one image) and charge per that.

**Owner question (not P1 under the current rule):**
- **The picked values are fully visible at 0 trial uses.** At the cap (zero.json) upload, pick, magnifier and palette all work and the HEX/RGB/HSL/CMYK text is on screen (and selectable; no `select-none`). Only the copy buttons open the cap dialog. For a colour picker the visible value *is* the result, so the gate only removes the convenience of a copy button. Not a file save, so per the corrected rule this waits for Santosh.

**P2 — where to look:**
- **Page copy describes an older tool and contradicts the live one** (tool-expanded.txt lines 64–76):
  - Limits: "There is no magnifier", "Only the latest pick is shown", "Output is limited to hex, rgb() and hsl()". Live: magnifier, CMYK, palette.
  - Tips: "The page has no zoom, so for a tiny target crop the image". The magnifier and arrow keys now solve this.
  - "Skip it when you need a representative color… a palette extractor suits that job better". The page now has "Main colors in this image".
  - Privacy: "When you add a file the site's usage counter records the tool name…". Adding a file sends nothing (0 POSTs on every upload); the record happens on the first copy.
  - The FAQ answer on formats lists hex/rgb/hsl only.
  - The blog says "three panels appear: HEX, RGB and HSL" and has a section "Precision, without a magnifier".
- **Video njX53TSw5mA is out of date:** older UI with three panels (no CMYK, palette or magnifier), caption "10 free uses daily", title "Free Step-by-Step Walkthrough", description "Try … free", end card "200+ Free Productivity Tools".
- **A non-image file fails silently:** `notanimage.png` (text renamed .png) leaves a blank 300×150 checkerboard canvas, no message (C08, Chromium and Firefox).
- **Locale pages:** chrome, breadcrumb, trial strip, Quick Buy and the Drive button are translated. The H1, subtitle, drop zone text, "Take photo with camera" and the meta title/description stay English (es screenshot; all 9 locales report the English H1).
- **SEO:** meta description 92 chars (short; says nothing of CMYK/palette/magnifier). OG image is the generic `og-default.png`. Offer in JSON-LD is "4.99" (fine for the pass).

**P3:**
- **Large images:** at 4000×3000 one screen pixel is 6 source pixels, so a click cannot land on a chosen single pixel (debug.json: click at source 1000,750 returned the surrounding blue). Arrow keys move 1 *source* pixel, so precision is reachable; mention this in the how-to.
- **Transparency is not shown:** a 25 %-alpha red returns #ff0000 with no alpha note (C04-alpha).
- **Counter jump (observation, as before):** in Firefox the first copy set 0/10 → 10/10 (one POST). Server pooling by network/browser; later copies in that load still worked (per-load).
- **iPhone SE (320 px):** 9 px horizontal overflow from the header menu button (right edge 329; screenshot shows the hamburger at the edge).
- **axe:** desktop label-content-name-mismatch (serious), region (moderate). Pixel 7 color-contrast on an ad caption (keep reserved ad slots; fix the caption colour). ja desktop 1369 px (site-wide).
- **Camera button on desktop** opens the plain file chooser (`capture` is ignored by desktop browsers). Consider hiding it on non-touch devices; check on a real phone.

## Intent

A designer, marketer or developer has a photo, logo or screenshot and needs the exact colour in the format their tool wants, fast and without uploading a client's file. If the pick is accurate and copying is one click, the $1 day pass is an easy buy on a busy day.

## What works (verified)

- **Accuracy:** every quadrant returned its exact value (#3366cc, #e53935, #43a047, #fdd835); corner pixel (799,599) and (3999,2999) = #123456; tall 300×3000 image top/bottom correct.
- **Formats:** RGB/HSL/CMYK match the hex (e.g. #3366cc = rgb(51, 102, 204) = hsl(220, 60%, 50%) = cmyk(75%, 50%, 0%, 20%)).
- **JPEG q60:** values within 2 of the source (#fdd736 vs #fdd835), as the FAQ warns.
- **EXIF orientation 6:** the photo is displayed upright and the picked colours follow the displayed image (C05).
- **Coordinate mapping:** correct with letterboxing at scales 0.17–500 (1×1 image works, palette #808080 100 %).
- **Keyboard:** from (395,100) blue, 4× → still blue, 10× → red; 21× Shift+↓ → yellow (debug.json).
- **Touch:** tap-to-pick works on Pixel 7 and iPhone 14 Pro Max (WebKit).
- **Palette:** 4 quadrants → 4 swatches at 25 %; clicking one shows its values.
- **Copy:** clipboard holds exactly the shown text; toast "Copied #fdd835".
- **Gate at the cap:** each copy opens "Today's trial uses are done" (Monthly $4.99 / Day Pass $1), no clipboard write, no charge (Chromium and Firefox).
- **Quick Buy:** Day → email prompt (stopped); Monthly → Stripe (stopped).
- **Layout:** tool above the fold on desktop and phones. Geo: same $1/$4.99 everywhere; the consent banner shows in de-DE (screenshot) and does not cover the tool.

## 22 checks

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Capability | PASS | Exact pixel values, 4 formats, magnifier, keyboard, palette, touch. |
| 2 | Completeness | PASS (minor) | Near browser eyedroppers. No pick history, no alpha, no single-pixel click on huge images (keys solve it). |
| 3 | Ease of use | PASS | Click → values → copy. Non-image fails silently. |
| 4 | Layout | PASS (minor) | Above the fold; 9 px overflow on iPhone SE. |
| 5 | Payment process | PASS / stopped | Cap dialog; Day email prompt (stopped); Monthly → Stripe (stopped). |
| 6 | Information correct | FAIL (P2) | Limits/tips/privacy copy describe an older tool (no magnifier, 3 formats, upload counted). |
| 7 | Indexing | PASS | 200, canonical self, 10 hreflang + x-default. |
| 8 | SEO | PARTIAL | Meta 92 chars, generic OG; title fine (58). |
| 9 | Blog | PARTIAL | Useful, but "three panels" and "without a magnifier" are outdated. |
| 10 | YouTube video | PASS | njX53TSw5mA embedded + VideoObject. |
| 11 | FAQ / guide correct | PARTIAL | Formats answer omits CMYK. |
| 12 | Video shows current capability | FAIL | Old UI, "free" wording. |
| 13 | Storage | N/A | No history (verified). |
| 14 | Sharing | N/A (tool link) | "Share this tool" only. |
| 15 | Downloads | N/A | Output is clipboard text; copies verified. |
| 16 | Usage count | FAIL (P1) | Once per page load (L03–L05). Values visible at 0 = owner question. |
| 17 | Categorization in section | PASS | Design & Marketing / Professional. |
| 18 | Correct section of site | PASS | Links to Palette Generator, HEX/RGB/HSL Converter, Gradient Generator. |
| 19 | AI need and demand | PASS | High ("color picker from image", "image color picker"). |
| 20 | Merge better? | No | Distinct from palette generator; could cross-link "Main colors" to it. |
| 21 | Remove? | No | Popular, cheap to run. |
| 22 | Duplicates | None | C21 members generate CSS/colours; this reads them from images. |

## After fixes, rerun

- `TRIES=40 px63-live.js left` (expect a charge per the unit you choose; cap after 10).
- `px63-live.js zero`, `px63-extra.js chromium` (non-image message), re-extract copy (`px63-expand.js`).
