Sent: 2026-11-20 08:40 ET

# FDP-07 QR Code Generator with Logo (custom-qr): priorities

- **Written:** 2026-11-19 12:36:49 EST (box `date`, ET).
- **Ordering:** by user-trust and revenue outcome. Each item gives its REPORT.md check and its REPRODUCE.md ID.

## P0: ship first

1. **Make the trial gate consistent (checks 5, 16; R-01, R-02).**
   - **Outcome:** each download click costs exactly 1, nothing downloads at 0 remaining, and every fresh visitor starts at 2.
   - **Why (display-only):**
     - Downloads succeeded at "0 remaining" on the same page load (C2, F2), and E2–E4 were never counted.
     - One click cost 2 in C, D and F.
     - Fresh contexts loaded at 0 or 2 (16 matrix and geo contexts: 10 at 0, 6 at 2).
     - After a reload at 0 the gate holds (H1–H3).
   - Verify server-side.
2. **Make the trial vector PDF scannable (checks 1, 15; R-03).**
   - **Outcome:** every PDF a trial use buys decodes, with the badge outside the code and its quiet zone.
   - **Why:** the dark "Created with FreeDailyPro.com" pill covers the bottom-right modules (and the frame text). A3 and B1 do not decode with zxing-cpp or OpenCV, even at 600 dpi with an added border. PNG/SVG carry no mark and decode fine.

## P1: next

3. **The page crashes on long text (check 1; R-04).** 2,400+ characters replace the whole page with "An unexpected error occurred" and lose the input (console "code length overflow"). Show the same quantified "Too long" message that qr-generator shows.
4. **Characters beyond Latin-1 are corrupted (checks 1, 6; R-05).**
   - "Grüße 日本 👍" encodes as "Grüße å, =M" in the preview and the PNG. Encode as UTF-8.
   - The PDF frame turns non-ASCII into "?" (R-06).
   - The FAQ promises "the exact text".
5. **Copy truth pass (checks 6, 9, 11, 12; R-07).**
   - "When not to use it" denies Wi-Fi, contact, email and SMS; the Details describe a single box and PNG/SVG only.
   - The branded blog post is stale (old name, no PDF, "not a bulk engine", "Professional Tools trial usage").
   - The video shows the old UI, "10 uses/day" and $1/$4.99.
6. **Quiet zone about 1.4 modules (checks 1, 15; R-08).** 4% of the width (50 px at 1000 px). Default to 4 modules, or offer it as an option.
7. **vCard ";" is unescaped (check 1; R-09).** This is the shared qrHelpers `p()` bug: fix it once for both tools.
8. **C04 positioning (checks 20, 22).** The qr-generator title says "with Logo". The custom-qr bulk vs bulk-qr needs one sentence each on who should use which.

## P2: later

9. **Phone layout and a11y (R-10).**
   - Preview above Download on phones.
   - iPhone SE overflow (329 px).
   - axe critical ×5.
   - Canvas aria-label.
   - Arrow-key tabs and aria-controls.
10. **Small honesty and UX items:**
    - the bulk ZIP silently uses 1000 px when 2000 is chosen (R-11)
    - a fake logo blanks the canvas with "Logo added"
    - empty content downloads a " " code
    - fixed file names
    - the Offer has no billing period
    - English title and H1 in 9 locales
    - two near-duplicate blog posts
11. **Disclosure:** say next to "Download vector PDF" that trial PDFs carry the mark (today it is mentioned only in the cap dialog).
