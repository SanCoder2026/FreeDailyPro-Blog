Sent: 2026-11-20 08:40 ET

# FDP-25 Barcode Generator: live functional findings (Chromium unless noted; box times ET)

Starting counts: most fresh contexts load at 10/10 used ("0 remaining today", e.g. 18:25:07 EST); about 1 in 7 loads with 10 left (18:35:3x, 18:37:xx EST). Counters are display-only evidence. Trial uses spent by this test: 3 (one spend context, one privacy context ×2 visits).

## Generation (no trial use; preview PNG captured from memory and decoded with zxing-cpp) — `json/battery.json`
- 20/20 valid inputs decode to the expected data: EAN-13 12 and 13 digits (check digit 1 added → 4006381333931), padded with spaces (trimmed), 000000000000; EAN-8 7/8; UPC-A 11/12 (decodes as 0036000291452 EAN-13 form — normal); ITF-14 13/14; Code 128 SKU, full printable ASCII incl. `\ " { } ~`, numeric (charset C), formula-looking `=HYPERLINK(...)`, 80 and 300 chars; Code 39 incl. `$/+%.` and lower case (shows "Code 39 has no lower-case letters, so this encodes ABC-123", decodes ABC-123).
- Errors are specific and correct: wrong check digit "Check digit should be 1, not 2. Enter 12 digits and it is added for you." (EAN-13/EAN-8/UPC-A/ITF-14); length "needs 12 digits … You entered 11."; letters/spaces/full-width digits "uses digits only"; Code 128 accents/tab; Code 39 `*`/`_`; empty "Enter a value to encode; Download stays off until you do." Download disabled on every error.
- **P3:** when the value is invalid, the "Prints 3.12 in … wide" line still shows the size of the last valid barcode.
- Same results in Firefox and WebKit (EAN-13, UPC-A, Code 128 decode) — `json/browsers.json`.
- No request carries the value while typing or on Download (`json/privacy.json`: distinctive value + caption never in any URL or POST body; Download makes `usage.log` POST 117 B + `usage.check`). "Nothing you enter … is uploaded" holds.

## Print-spec compliance (P1) — measured on outputs
- Quiet zones (white before first / after last bar), in modules: EAN-13 17 / **5** (needs 11 / 7), EAN-8 **5 / 5** (7 / 7), UPC-A 13 / 13 (9 / 9 ✓), ITF-14 **5 / 5** (10 / 10), Code 128 **5 / 5** (10 / 10), Code 39 **5 / 6** (10 / 10). Same in the 4× PNG, SVG and ZIP files (margin 10 px at 2 px/module).
- 4× PNG: 936×482 px, pHYs 300 dpi → 3.12 in (79.2 mm) for EAN-13 = 212% magnification (GS1 retail max 200%); bars 27 mm tall (proportional height at that size ≈48 mm). Page says not to print much smaller — the standard 100% (37.3 mm) is half that.
- ITF-14 has no bearer bars.
- All files decode on screen with zxing (even without padding), so this is about real-world label printing, not on-screen scanning.

## Caption (P2)
- Caption is drawn centred on a canvas exactly as wide as the barcode, so a caption longer than the bars is cut on both sides without warning: "Organic cotton crew-neck T-shirt, navy, size M" on EAN-13 → "anic cotton crew-neck T-shirt, navy, siz" (`screens/live/box-cap-C2.png`, `cap-C2.png`). With number hidden on EAN-13 even the 33-char "Blue T-Shirt, Size M <b>x</b> हिन्दी" loses its first letter (`box-B30.png`). The placeholder text fits on EAN-8 (C1). Markup in captions is drawn as literal text (safe).

## Download gate and usage (`json/dl-spend.json`, `json/dl-gate.json`, `json/privacy.json`)
- Preview is free. With uses left (18:35 EST): 1st Download (the **untouched sample value**) cost 1 (0 → 1) and saved `ean13-5901234123457.png`. Then, in the same page visit, 8 more downloads were all free (1 → 1): EAN-13 4× PNG with caption, SVG, 1× PNG, a different Code 128 value, ITF-14 SVG, ZIP of PNGs, ZIP of SVGs, a 400-char Code 128. After a reload the next Download cost again (1 → 2).
- **Policy question for Santosh (not a PASS):** one trial use unlocks unlimited downloads of any number of different barcodes — including ZIPs of up to 200 — for the rest of that page visit. Owner policy (Oct 30) says results count; this looks like "1 use per visit", not "1 use per result".
- **P2:** the pre-filled sample can be downloaded and charges a trial use, although the step bar treats the sample as "value not entered yet".
- Downloads: no "Created with FreeDailyPro.com" mark on PNG/SVG (scannability kept). PNG at 4× has pHYs 300 dpi; 1× has none. SVG 234×122 px, `font-family="monospace"` live text (digits depend on installed fonts), caption omitted as documented. ZIP: one file per valid line + `index.csv` (formula-escaped); problems/duplicates excluded as promised (10 lines → 3 files; "2 barcodes ready, 3 lines with a problem, 2 repeated values made once" for the 8-line sample); 201 lines → "Only the first 200 are made."
- **P3:** `index.csv` value column mixes forms (590123412345 vs 4006381333931); file names always carry the check digit.
- **P3:** no length guard: 400-char Code 128 makes a 35,560×482 px PNG ("Prints 118.53 in (301.1 cm) wide") with no warning.
- At 0 remaining (18:36 EST): Download PNG → "Today's trial uses are done" ($4.99 month / $1 Day Pass, "Your input stays where it is") → Buy Day Pass → "Day Pass, $1 | Enter your email and go straight to payment" (stopped; nothing typed). "Get a Day Pass to download" opens the same dialog. No Quick Buy buttons on desktop at the cap in that context (the strip shows them on load).
- No Save to Drive / cloud / share on the result (live-verified: buttons are Download PNG/SVG/ZIP and the site-wide "Share this tool").

## Keyboard and accessibility (`json/ui.json`)
- Tab order: Format → One barcode → A list → Value → Caption → number checkbox → Bar height → PNG size → Download PNG → Day Pass link → Download SVG. Format select opens with Enter, Arrow keys move, Enter picks (UPC-A), focus returns. Errors: role=alert + aria-invalid (no aria-describedby).
- axe on `main`: desktop 0 violations; iPhone 13 only ad-label contrast (site-wide). Matrix axe: `label-content-name-mismatch` `.right-2`, region.
- **P3:** the preview canvas has no accessible name or text alternative; screen-reader users can't confirm what was drawn.
