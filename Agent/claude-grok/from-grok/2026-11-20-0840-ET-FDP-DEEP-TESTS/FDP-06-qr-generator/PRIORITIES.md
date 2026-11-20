Sent: 2026-11-20 08:40 ET

# FDP-06 QR Code Generator: priorities

- **Written:** 2026-11-19 12:05:23 EST (box `date`, ET).
- **Ordering:** by user-trust and revenue outcome. Each item gives its REPORT.md check and its REPRODUCE.md ID.

## P0: ship first

1. **Make the trial meter honest for a new visitor (checks 15, 16; R-01).**
   - **Outcome:** a fresh device shows 10 remaining, and the page says what PNG and SVG each cost.
   - **Why:** 22 of 22 readable fresh contexts loaded at 0. This is display-only evidence from one box IP, and the same pattern as FDP-02 to FDP-05. Verify server-side.

## P1: next

2. **Fix the copy that denies the tool's features (checks 6, 11; R-02).**
   - "When not to use it" says plain text and URLs only, no WiFi/vCard, and to use another tool for SVG. All of these work live.
   - The Details How-to mentions PNG only. There is one FAQ. The meta is 75 chars.
   - This is the snippet Google shows for the #8-ranked tool.
3. **vCard ";" escaping (check 1; R-03).** `p()` replaces ";" with ";" (a no-op). Company or names containing ";" are split on import. It's a one-character fix; add a unit test.
4. **Logos are stretched to a square (check 1; R-04).**
   - Contain-fit the logo in the canvas. Make sure the SVG matches.
   - Also report unreadable logo files instead of silently showing "Logo added" (R-05).
5. **C04 positioning (checks 8, 20, 22; R-06).**
   - The Pro title says "With Logo" and the upsell card sells the "logo in the middle", both of which collide with the Premium custom-qr.
   - Give each tool a distinct promise and title.
6. **Locales (check 8; R-07).**
   - /es says "gratis".
   - pt, fr, de, ja, hi, zh, ko and id have an English title, meta and H1 (the H1 isn't localized even client-side).
7. **Mark disclosure (checks 5, 15; R-08, after the re-run).**
   - If trial PNG/SVG carry "Created with FreeDailyPro.com", say so next to Download.
   - Make sure the mark stays outside the quiet zone and the code still decodes.

## P2: enhancements and polish

8. **Phone layout (check 4; R-09).**
   - Show the preview above Download on narrow screens (today it's at y≈1094–1185, below the buttons).
   - Fix the 329 px overflow on iPhone SE.
9. **A11y (R-10):**
   - Name the size and EC select triggers, and label the logo input (3 critical axe issues).
   - Give the canvas a label ("QR code for …").
   - Arrow-key tabs.
10. **Product:**
    - transparent background
    - calendar and location types
    - descriptive file names (qr-<slug>.png)
    - a note for `javascript:` links and a shortener caution
    - a "Test it with QR & Barcode Scanner" link
11. **Content:**
    - a dedicated WiFi/vCard how-to post
    - merge the two near-duplicate custom-qr posts
    - FAQPage with 6 or more questions
    - JSON-LD Offer billing period
    - Video: a WiFi segment, "300+", and "Professional Tool" instead of "free tool"; "trial uses" in the description
12. **Re-run after midnight UTC (R-11):** `scripts/qr-battery.js` (QR-27…QR-35). Put any new defects in a -v2 note.
