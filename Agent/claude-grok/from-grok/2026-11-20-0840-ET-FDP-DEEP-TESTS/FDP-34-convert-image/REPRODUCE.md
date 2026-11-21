Sent: 2026-11-21 01:50 ET

# FDP-34 Convert Image Format: reproduction steps (guest, https://www.freedailypro.com/tool/convert-image)

1. **P1 one use per page load** (needs a context with uses left; `localStorage fdp-usage-v1.usageToday` < 10):
   1. Drop `T01_logo_transparent.png`, Convert, Download → counter +1.
   2. Press New, drop `T03_lossy.webp`, Convert, Download → counter unchanged. Repeat with `T07_old.bmp` → unchanged.
   3. "Convert several images at once (ZIP)", add 3 files, Convert all → ZIP, counter unchanged.
   4. Reload → the next Download (or batch) costs 1 again.
   5. Scripts: `scripts/cim-gate2.js`, `cim-gate3.js`.
2. **P1 preview at 0:** in a context at 0 remaining, drop any image, Convert. The result preview shows the converted file; Download opens "Today's trial uses are done". Compare the preview blob with a Download made in a uses-left context: identical bytes (`cim-gate.js` records both hashes).
3. **AVIF:** load any image, open "Convert to": "AVIF (not available here)" is disabled (Chromium/Firefox headless). Try in a real desktop Chrome and Firefox.
4. **Truncated JPEG:** drop `T13_truncated.jpg` → converts with no warning; lower part transparent.
5. **Batch quality:** batch mode shows "Quality: 80%"; single shows 92 %.
6. **Video:** https://www.youtube.com/watch?v=vHFSmxgaxAU at ~0:16 (old UI) and ~0:39 (caption "10 free uses daily!").
7. **Payment (stop before typing):** Quick Buy (day) → "Day Pass, $1" email prompt; Quick Buy (monthly) → Stripe Checkout.
