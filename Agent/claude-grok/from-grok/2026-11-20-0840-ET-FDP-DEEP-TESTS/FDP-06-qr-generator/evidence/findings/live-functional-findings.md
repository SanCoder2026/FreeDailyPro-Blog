Sent: 2026-11-20 08:40 ET

# QR Code Generator: live functional findings (guest, no downloads)

Written: 2026-11-19 12:03 EST

**When:** guest contexts, 2026-11-19 11:49–12:05 EST. Raw data: `json/`, `screens/live/`, `previews/`.

## Trial state (display-only evidence)

- **All 22 fresh contexts where the count was readable loaded at "Trial: 10 uses/day · 0 remaining today"**: probe, explore, kbd ×3 (desktop, Pixel 7, iPhone SE), 10 matrix devices, the en locale load, 6 geo.
- probe.json: `usageToday 10`, `allowed false`, scope `dev:…`.
- So **no file could be downloaded**. Every download and output check is in `scripts/qr-battery.js` and listed in `/workspace/deep/RERUN-AFTER-RESET.md`. **Needs re-run after midnight UTC (7:00 PM ET).**
- **Generating and previewing is not gated.** All 31 preview scenarios ran at 0 remaining, and `usageToday` stayed 10.

## Method that needs no download

- The live preview `<canvas>` (300×300) was read with `toDataURL`, which is not a download.
- The images were decoded with **zxing-cpp and OpenCV** (`scripts/decode-previews.py`, results in `json/decoded.json`).
- This proves what the code encodes. The downloaded PNG/SVG are drawn by the same library call at a different size (from the JS), but that is unverified until the re-run.

## Results (qr-explore.js, `json/explore-*.json`, `json/decoded.json`)

| ID | Input | Decoded content | Result |
|---|---|---|---|
| Q01 | Default Link | https://freedailypro.com (prefilled) | PASS |
| Q02 | https://example.com/café?q=a b&x=1#frag | exact | PASS (raw spaces and accents are kept, not percent-encoded; most scanners cope) |
| Q03 | example.com/menu | https://example.com/menu | PASS (https added) |
| Q04 | bit.ly link | exact | PASS (no shortener caution) |
| Q05 | Multiline text, German, Japanese, emoji | exact | PASS |
| Q06 | WiFi WPA, SSID `Café;Net,"5G":\` and a password with `;,:"\` | `WIFI:T:WPA;S:Café\;Net\,\"5G\"\:\\;P:…;;` | PASS (correct escaping) |
| Q07 | WiFi hidden | `…;H:true;;` | PASS |
| Q08 | WiFi open | `WIFI:T:nopass;S:GuestOpen;;` | PASS |
| Q09 | WiFi WEP | `WIFI:T:WEP;…` | PASS |
| Q10 | Contact with Company "Smith; Jones & Co, LLC" | `ORG:Smith; Jones & Co\, LLC` | **FAIL**: ";" not escaped, so the org is split |
| Q11 | Contact first name only | valid minimal vCard 3.0 | PASS |
| Q12 | Email + subject "Order #12 & more?" + 2-line body | mailto with percent-encoding | PASS |
| Q13 | SMS | `SMSTO:+15550102030:Reply YES: confirm` | PASS |
| Q14 | Phone | `tel:+44 20 7946 0958` | PASS (spaces kept; scanners accept them) |
| Q15/16 | EC L / H | EC level confirmed by the decoder, and the capacity meter updates (2,953 / 1,273) | PASS |
| Q17 | Size 2000 px | preview stays 300 px (expected); the download size **needs re-run** | — |
| Q18 | White on black | Warning: "inverted… Many phone scanners cannot read inverted codes". zxing decodes it, OpenCV fails, so the warning is justified | PASS |
| Q19 | #9ca3af on white | "Low contrast (2.5:1)… less than about 4:1 often fail" | PASS |
| Q20 | Dark teal on cream | no warning, decodes | PASS |
| Q21–23 | Logo PNG / busy 2400×1600 photo / SVG | "Logo added. Error correction raised automatically", EC H, all decode | PASS |
| Q24 | PDF as logo | toast "Please upload an image file for the logo." | PASS |
| Q25 | Text file renamed .png | "Logo added", EC H, **no logo drawn, no error** | **FAIL (low)**: silent. PNG export may fail ("Couldn't create the PNG", from code); verify on re-run |
| Q26 | 620-byte URL + logo (H) | decodes from the 300 px preview | PASS |
| Q27 | Empty link | "Fill in the details and your QR code appears here." | PASS |
| Q28 | 2,400 bytes at M | "Too long for a QR code: 2,400 bytes, and level M holds at most 2,331. Shorten it or choose error correction L…" | PASS (excellent) |
| Q29 | 2,900 bytes at L | decodes even from the 300 px preview | PASS |
| Q30 | javascript:alert(1) | encoded as typed, no note | low |
| Q31 | 800×200 logo with a round mark | **Logo squashed to a square**: the circle becomes a 15×54 px ellipse | **FAIL** (`screens/live/x-Q31_logo_wide.png`) |

## Gate, offer, a11y (qr-kbd.js, `json/kbd.json`)

- **Download PNG / Download SVG at 0:** no download. Both open the dialog "Today's trial uses are done", with Monthly $4.99, Day Pass $1, an access code option, and "Either pass removes the 'Created with FreeDailyPro.com' mark from your PDFs and images". Closed with Escape.
- **Mark disclosure:** none on the page before download (`markDisclosed:false`). The dialog implies trial-use images carry a mark.
  - A mark on a QR image could hurt print use and the quiet zone.
  - **Verify on re-run** (inspect-qr-downloads.py checks the corners and SVG text).
- **Upsell card:** "Next step: Premium application, QR Code Generator with Logo" → /tool/custom-qr (2 trial uses a day · $3 / $9.99).
- **Tabs:** role=tab inside a tablist, aria-selected set, Enter activates. **Arrow keys don't move between tabs** (no roving tabindex; all tabindex 0, no aria-controls) (P2).
- **Selects:** usable by keyboard (Enter, ArrowDown, Enter → 1500 px).
- **The preview canvas has no accessible name or text alternative.** Screen-reader users can't confirm what was encoded (P2). The live region only says "1 of 3 steps done. Current step: Download."
- **axe on main (desktop):**
  - **button-name critical ×2**: the Download size and Error correction select triggers have no accessible name.
  - **label critical ×1**: the logo file input.
  - label-content-name-mismatch serious ×1.
  - The same critical issues appear on Pixel 7.
- **Not clicked:** Quick Buy (same strip as FDP-02 to FDP-05; no payment pages entered).
- **No sign-in elements** on this tool: there are no Google Drive or cloud buttons in the UI.
