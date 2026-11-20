Sent: 2026-11-20 08:40 ET

# FDP-07 custom-qr: live functional findings

- **Written:** 2026-11-19 12:30:07 EST (box `date`, ET). Live window 2026-11-19 about 12:00–12:25 EST. Headless Playwright (Chromium) in guest contexts, no sign-in, no card or email entered, no ad clicks.
- Counters are **display-only** evidence: the strip text and localStorage `fdp-usage-v1`. No backend claims.

## Starting state
- Premium scope `dev:<uuid>:premium`, limit 2. All six battery contexts (A–F) loaded at **2 remaining** (`json/battery-*.json`), and the preview runs never changed the count.
  - This differs from the Professional Tools in FDP-02 to FDP-06, which loaded at 0.
- After the battery, the next fresh Chromium contexts (H, kbd desktop, kbd Pixel 7) loaded at **0 remaining, used 2**, which suggests the count is restored from outside the context.
  - The kbd WebKit iPhone SE context still loaded at 2.
- Fresh contexts used for downloads: 7 (A–F, H). The download-capable state is now used up for today on this box (Chromium).

## Previews (free; usageToday never changed)
- 29 scenarios, canvas read with toDataURL, decoded with zxing-cpp. See `json/decoded.json` and `previews/`.
- **PASS:**
  - All 6 dot styles; corner styles; dark gradient; light-end gradient (decodes, warning shown); inverted (decodes, warning shown).
  - Frame default and non-ASCII frame in the preview.
  - Logos PNG/SVG/wide (aspect kept, EC H); a PDF logo is rejected with a toast.
  - WiFi with `;,:"\` (correct escaping), email (encoded subject), SMS, phone, and a bare domain (https added).
  - Bulk 209 lines → "Only the first 200 lines are used".
- **FAIL:**
  - **C23 Unicode:** "Line 1\nGrüße 日本 👍" decodes as "Line 1\nGrüße å, =M". Characters beyond Latin-1 are truncated (byte mode with charCode&0xff). qr-generator (Pro) encodes the same text correctly.
  - **C19 vCard ";":** `ORG:Smith; Jones & Co\, LLC`. ";" is not escaped (the same qrHelpers `p()` bug as in qr-generator).
  - **C15 fake .png logo:** "Logo added" is shown but the canvas goes blank (no code, no error).
  - **C25 empty content:** a code encoding " " (a space) is shown and downloadable.
  - **Long text crash:** 2,400 or 3,000 characters → the whole page shows "An unexpected error occurred… Reload page"; console "code length overflow (19220>18672)". The user's input is lost. 2,300 is fine. qr-generator shows a quantified "Too long" message instead. Evidence: `screens/live/x-long-2400-crash.png`, `json/long-frame.json`.

## Downloads (battery, display-only counts)
Files are in `downloads/`; inspection is in `json/downloads-inspection.json`.

| Ctx | Step | Strip before → after | File |
|---|---|---|---|
| A | PNG 1000 | 2 → 1 | 1000×1000, 50 px margin, decodes |
| A | SVG | 1 → 1 (not counted) | viewBox 1000, decodes, no mark |
| A | vector PDF | 1 → 1 (not counted) | 50 mm square, **badge over code, does not decode** |
| B | PDF + frame "Escanéame 扫码" + logo | 2 → 1 | frame text "Escan?ame ??", badge over code and frame, **does not decode** |
| B | size 2000 + bulk ZIP | – | no download (the size step failed in the script) |
| C | PNG, text "Grüße 日本 👍" | 2 → **0** | decodes as "Grüße å, =M" (same corruption as the preview) |
| C | vCard PNG | **0 → 0, downloaded** | decodes |
| D | wide-logo SVG | 2 → **0** | `<image>` kept, EC H, decodes |
| D | gradient PNG 2000 | – | no download (script step) |
| E | PNG default | 2 → 1 | decodes |
| E | PNG new URL, SVG new URL, PNG new URL | 1 → 1 → 1 (none counted) | all decode |
| F | bulk ZIP of 3, 2000 px chosen | 2 → **0** | 3 PNGs at **1000×1000** + index.csv, all decode |
| F | PNG 2000 | **0 → 0, downloaded** | 2000×2000, 87 px margin, decodes |
| H (fresh, loaded at 0) | PNG; reload; PNG; reload; PNG | 0 → 0 | **gated every time** (cap dialog) |

**Reading (display-only):**
1. **The gate leaks within a page session.** After the first counted download, every further download on the same page load went through, even when the strip read "0 remaining today" (C2, E2–E4, F2). After a reload, or in a context that loads at 0, the gate holds (H1–H3 show the dialog).
2. **The cost per download is inconsistent.** One click cost 1 (A, B, E) or 2 (C text PNG, D SVG, F ZIP). This may be a sync of an outside count rather than a double charge (unverified). The user just sees the meter fall from 2 to 0 after one download.
3. **Trial PDFs do not scan.** The "Created with FreeDailyPro.com" badge is drawn as a dark pill over the bottom-right of the code (and over the frame text). Neither zxing-cpp nor OpenCV decodes A3 or B1, even at 600 dpi with an added white border. The PNG/SVG trial outputs carry **no** mark and decode.
4. Quiet zone: 50 px of 1000 (about 1.4 modules for a short URL), 87 px of 2000. Below the 4-module spec, but it decoded.
5. The bulk ZIP silently caps images at 1000 px when 2000 is chosen.
6. File names are fixed (custom-qr.png etc.), so a second download overwrites or gets a (1) suffix.

## Other
- Cap dialog: "Today's trial uses are done | Your input stays where it is…" with Monthly $9.99 / Day Pass $3 and "Have an access code?". It is shown for PNG, SVG and vector PDF. The test stopped there; no email or card was entered.
- Sign-in: there are no Drive, cloud or account features in the tool. **Nothing was blocked by sign-in.**
