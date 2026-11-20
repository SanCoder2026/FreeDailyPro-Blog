Sent: 2026-11-20 08:40 ET

# Test cases: QR Code Generator with Logo (custom-qr)

- **Tool:** https://www.freedailypro.com/tool/custom-qr (Premium Application, 2 trial uses a day).
- **For:** Claude's retest after a fix, and the browser tester's live pass.
- **Written:** 2026-11-19 12:35:14 EST (box `date`, ET).
- **Files:** `evidence/testfiles/` (logos, a fake .png, a PDF), or `python3 scripts/make-testfiles.py <dir>`.
- **Checking a code without downloading:** read `main canvas` with `toDataURL()` and decode with `scripts/decode-previews.py` (zxing-cpp + OpenCV). Previewing is free.
- **Checking downloads:** `scripts/inspect-qr-downloads.py <dir> <out.json>` for PNG/SVG. For PDFs, run `pdftoppm -r 600 -png`, then decode.
- **Rules:** guest or fresh profile only. No sign-in, no payment (stop at the cap dialog / Stripe), no ad clicks.
- **Results:** "Today" is the live result on 2026-11-19, 12:00–12:32 EST. "Currently: FAIL" should pass after the fix. "**Re-run**" needs a context that loads at 2 remaining (after midnight UTC, 7:00 PM ET), using `scripts/cq-battery.js`.

## A. Content types (decode the preview)

| ID | Input | Expected | Today |
|---|---|---|---|
| CQ-01 | Link default | https://freedailypro.com | PASS |
| CQ-02 | Link "example.com/menu" (no scheme) | https://example.com/menu | PASS |
| CQ-03 | Text "Line 1⏎Grüße 日本 👍" | exact text | **Currently: FAIL** ("Grüße å, =M") |
| CQ-04 | WiFi SSID `Café;Net,"5G":\`, password `p@ss;w,rd:"x"\` | WIFI:… with `\` escapes | PASS |
| CQ-05 | Contact name José, Company "Smith; Jones & Co, LLC" | ORG:Smith\; Jones & Co\, LLC | **Currently: FAIL** (";" unescaped) |
| CQ-06 | Email a@example.com, subject "Hi & bye?" | mailto:…?subject=Hi%20%26%20bye%3F | PASS |
| CQ-07 | SMS +15550100 "YES: ok" | SMSTO:+15550100:YES: ok | PASS |
| CQ-08 | Phone +15550100 | tel:+15550100 | PASS |
| CQ-09 | Empty content | no code; a "type something" hint; Download disabled | **Currently: FAIL** (encodes " ") |
| CQ-10 | Text of 2,400 and 3,000 characters | a "too long" message with the byte count; the page stays usable; the input is kept | **Currently: FAIL** (whole page error, input lost) |
| CQ-11 | Text of 2,300 characters | decodes | PASS |

## B. Styling (decode the preview)

| ID | Setting | Expected | Today |
|---|---|---|---|
| CQ-12 | Each dot style (Square, Rounded, Dots, Classy, Classy rounded, Extra rounded) | decodes | PASS ×6 |
| CQ-13 | Corner style Circle, corner centre Dot | decodes | PASS |
| CQ-14 | Dark gradient | decodes, no warning | PASS |
| CQ-15 | Gradient with a light end | amber "Low contrast" warning | PASS (1.5:1 shown) |
| CQ-16 | Inverted (light code on dark) | warning | PASS |
| CQ-17 | Frame default "Scan me" and non-ASCII "Escanéame 扫码" | shown correctly in the preview | PASS |

## C. Logos

| ID | File | Expected | Today |
|---|---|---|---|
| CQ-18 | logo_small_transparent.png | EC H, decodes | PASS |
| CQ-19 | logo_wide_800x200_circle.png | aspect kept, decodes | PASS |
| CQ-20 | logo.svg | decodes | PASS |
| CQ-21 | text_renamed.png (not an image) | an error, previous code kept | **Currently: FAIL** ("Logo added", blank canvas) |
| CQ-22 | not_an_image.pdf | "Please upload an image file" | PASS |

## D. Bulk

| ID | Input | Expected | Today |
|---|---|---|---|
| CQ-23 | 209 lines | "Only the first 200 lines are used" | PASS |
| CQ-24 | 3 lines, size 2000 px, Download ZIP | 3 images at the chosen size + index.csv | **Currently: FAIL** (1000 px, not disclosed) |
| CQ-25 | "Lines are name,value" ticked; "name3,https://c.example" | file named name3, encodes https://c.example | Not run (re-run) |

## E. Downloads and trial uses (display-only counters)

| ID | Action | Expected | Today |
|---|---|---|---|
| CQ-26 | Fresh context: starting strip | the same allowance for every fresh visitor | **Inconsistent**: 0 or 2 (matrix: 10 at 0, 6 at 2) |
| CQ-27 | First PNG download | strip 2 → 1 | Mixed: 1 (A, E) or 2 (C, D, F) |
| CQ-28 | Second download on the same page load at "0 remaining" | cap dialog | **Currently: FAIL** (downloads; C2, F2) |
| CQ-29 | Three more downloads after 1 counted (same page) | each counted, or the policy stated | **Currently: FAIL** (E2–E4 uncounted) |
| CQ-30 | Reload at 0 remaining, then Download | cap dialog | PASS (H1–H3) |
| CQ-31 | PNG 1000 / 2000 | 1000×1000 / 2000×2000, decodes | PASS |
| CQ-32 | SVG | vector, logo as `<image>`, decodes | PASS |
| CQ-33 | Vector PDF 50 mm (trial) | 141.7 pt square, **decodes**; mark outside the code + quiet zone | **Currently: FAIL** (badge over code, no decode) |
| CQ-34 | PDF with frame "Escanéame 扫码" | frame text kept | **Currently: FAIL** ("Escan?ame ??") |
| CQ-35 | Quiet zone in PNG/SVG/PDF | ≥ 4 modules (or an option) | **Currently: FAIL** (about 1.4 modules) |
| CQ-36 | File names | descriptive (content or name) | Fixed custom-qr.* (P2) |
| CQ-37 | B2 bulk ZIP after frame and logo; D2 gradient PNG 2000 | download, decode | **Re-run** |
| CQ-38 | Real phone scan of the PNG, SVG and PDF | scans | **Re-run** (decoders only today) |

## F. Copy, layout, a11y

| ID | Check | Expected | Today |
|---|---|---|---|
| CQ-39 | "When not to use it" | does not deny WiFi/contact/email/SMS | **Currently: FAIL** |
| CQ-40 | Details How-to / Limitations | 7 tabs, PDF, bulk, multi-line text | **Currently: FAIL** |
| CQ-41 | Mark disclosure next to Download | states the trial mark on PDFs | **Currently: FAIL** (in the cap dialog only) |
| CQ-42 | Phone: preview position | preview above or next to Download | **Currently: FAIL** |
| CQ-43 | iPhone SE overflow | scrollWidth ≤ 320 | **Currently: FAIL** (329) |
| CQ-44 | axe critical | 0 | **Currently: FAIL** (button-name ×4, label ×1) |
| CQ-45 | Canvas alternative | aria-label naming the content | **Currently: FAIL** |
| CQ-46 | Arrow keys on tabs | move the selection | **Currently: FAIL** |
| CQ-47 | Locales: title and H1 | localized | **Currently: FAIL** (English in 9) |
| CQ-48 | Video | shows the current UI, price and allowance | **Currently: FAIL** (10/day, $1/$4.99, no tabs/PDF) |
