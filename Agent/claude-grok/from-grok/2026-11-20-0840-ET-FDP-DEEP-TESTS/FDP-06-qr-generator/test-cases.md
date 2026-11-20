Sent: 2026-11-20 08:40 ET

# Test cases: QR Code Generator (qr-generator)

- **Tool:** https://www.freedailypro.com/tool/qr-generator
- **For:** Claude's retest after a fix, and the browser tester's live pass.
- **Written:** 2026-11-19 12:03:51 EST (box `date`, ET).
- **Files:** `evidence/testfiles/` (logos), or `python3 scripts/make-testfiles.py <dir>`. The wide logo is `logo_wide_800x200_circle.png`.
- **Checking a code without downloading:** read the preview canvas (`canvas.toDataURL()`) and decode it with `scripts/decode-previews.py` (zxing-cpp + OpenCV).
- **Checking downloads:** `scripts/inspect-qr-downloads.py <dir>` reports pixel size, quiet zone, background, non-QR pixels in the bottom-right corner (mark), SVG text and decode results.
- **Rules:** guest or fresh profile only. No sign-in, no payment (stop at the email prompt or Stripe), no ad clicks.
- **Trial uses:** generating and previewing is free; Download PNG/SVG is gated.
- **Results:** "Today" is the live result on 2026-11-19, 11:49–12:05 EST.
  - "Currently: FAIL" should pass after the fix.
  - "**Re-run**" means it needs an uncapped context after midnight UTC (7:00 PM ET), using `scripts/qr-battery.js`.

## A. Content types (decode the preview)

| ID | Input | Expected decoded content | Today |
|---|---|---|---|
| QR-01 | Link default | https://freedailypro.com | PASS |
| QR-02 | https://example.com/café?q=a b&x=1#frag | exact | PASS |
| QR-03 | example.com/menu | https://example.com/menu | PASS |
| QR-04 | Text: 3 lines, Grüße, 日本語, 👍 | exact | PASS |
| QR-05 | WiFi WPA, SSID `Café;Net,"5G":\`, password `p@ss;w,rd:"x"\` | `WIFI:T:WPA;S:Café\;Net\,\"5G\"\:\\;P:p@ss\;w\,rd\:\"x\"\\;;` | PASS |
| QR-06 | WiFi hidden / open / WEP | `H:true` / `T:nopass` / `T:WEP` | PASS |
| QR-07 | Contact, Company "Smith; Jones & Co, LLC" | `ORG:Smith\; Jones & Co\, LLC` | **Currently: FAIL** (`ORG:Smith; Jones & Co\, LLC`) |
| QR-08 | Contact, Last name "Doe;Jr" | `N:Doe\;Jr;…` | Untested live (same escaping function as QR-07; expected FAIL) |
| QR-09 | Email with subject and a 2-line body | percent-encoded mailto | PASS |
| QR-10 | SMS / Phone | `SMSTO:+1…:msg` / `tel:…` | PASS |

## B. Options, limits, warnings

| ID | Action | Expected | Today |
|---|---|---|---|
| QR-11 | EC L / Q / H | Decoder reports that level; the meter shows 2,953 / 1,663 / 1,273 | PASS (L, H checked) |
| QR-12 | 2,400 bytes at M | "Too long… level M holds at most 2,331… choose L" | PASS |
| QR-13 | 2,900 bytes at L | code shown, decodes | PASS |
| QR-14 | Empty link | "Fill in the details and your QR code appears here." | PASS |
| QR-15 | White on black | inverted warning | PASS |
| QR-16 | #9ca3af on white | "Low contrast (2.5:1)…" | PASS |
| QR-17 | Logo PNG / JPG photo / SVG | "Logo added…", EC H, decodes | PASS |
| QR-18 | Wide logo 800×200 | Logo keeps its aspect ratio (circle stays round), decodes | **Currently: FAIL** (squashed into a square) |
| QR-19 | PDF as logo | "Please upload an image file for the logo." | PASS |
| QR-20 | Text renamed .png as logo | Error "That image couldn't be read", no "Logo added" | **Currently: FAIL** (silent "Logo added", no logo) |
| QR-21 | javascript:alert(1) in Link | Note "This isn't a web link" (suggested) | no note (low) |

## C. Gate, offer, disclosure

| ID | Action | Expected | Today |
|---|---|---|---|
| QR-22 | Fresh profile load | "10 remaining today" | **Currently: FAIL** (22/22 at 0; display-only) |
| QR-23 | Download PNG at 0 | Cap dialog, input kept | PASS |
| QR-24 | Download SVG at 0 | Cap dialog | PASS |
| QR-25 | Before download | If trial downloads carry a mark, say so next to Download (as split-pdf does) | **Currently: FAIL** (no disclosure; the dialog mentions the mark) |
| QR-26 | "Next step" card | Says what Premium adds beyond the Pro tool (shapes, gradients, PDF) | **Currently: PARTIAL** (it sells the "logo in the middle", which Pro already has) |

## D. Downloads (needs re-run after midnight UTC)

| ID | Scenario (qr-battery.js) | Verify | Today |
|---|---|---|---|
| QR-27 | B1: PNG 1000, then SVG, then PNG again | usageToday after each (does SVG cost another use? does the repeat?) | **Re-run** |
| QR-28 | B1–B3 PNG 1000 / 2000 / 200 | pixel size equals the chosen size; 4-module quiet zone; decodes | **Re-run** |
| QR-29 | All trial downloads | Is there a "Created with FreeDailyPro.com" mark? If so, it is outside the quiet zone and the code still decodes | **Re-run** |
| QR-30 | B4 WiFi PNG | decodes with the same escaping as QR-05 | **Re-run** |
| QR-31 | B5 vCard PNG | ORG escaping (fails until QR-07 is fixed) | **Re-run** |
| QR-32 | B6 logo PNG + SVG | both decode; SVG contains `<image>`; PNG and SVG logos look the same | **Re-run** |
| QR-33 | B7 colours PNG + SVG | colours kept | **Re-run** |
| QR-34 | B8 2,900 bytes L PNG | decodes from the 1000 px PNG | **Re-run** |
| QR-35 | File names | descriptive (e.g. qr-example-com-menu.png) instead of qrcode.png | fixed names (from JS); re-run to confirm |

## E. Layout and a11y

| ID | Check | Expected | Today |
|---|---|---|---|
| QR-36 | Phones: preview position | QR visible near the inputs, above Download | **Currently: FAIL** (y≈1094–1185, below Download) |
| QR-37 | iPhone SE 320 | no horizontal scroll | **Currently: FAIL** (329) |
| QR-38 | axe main | no critical issues (select names, logo label) | **Currently: FAIL** (3 critical) |
| QR-39 | Tabs: arrow keys | move between types | **Currently: FAIL** |
| QR-40 | Canvas | accessible name, e.g. "QR code for https://…" | **Currently: FAIL** (none) |
| QR-41 | Locales | localized title and H1; no "gratis" | **Currently: FAIL** |
| QR-42 | "When not to use it" / Details copy | describes WiFi, vCard, SVG correctly | **Currently: FAIL** |
