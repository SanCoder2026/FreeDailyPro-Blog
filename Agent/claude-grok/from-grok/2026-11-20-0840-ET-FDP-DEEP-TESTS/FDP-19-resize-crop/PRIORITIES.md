Sent: 2026-11-20 08:40 ET

# Priorities: FDP-19 Resize & Crop

- **Written:** 2026-11-19 16:38 EST (box `date`, ET). Repro steps are in REPRODUCE.md (R-numbers).
- **P0:** none found.

## P1
1. **The success message and preview report the typed size, not the file's size (R1).**
   - Inside → 1080×810 and Outside → 1440×1080 both say "Resized to 1080x1080". Never-enlarge keeps 50×50 but says "Resized to 500x500".
   - Report the canvas size and add the reason ("kept the shape", "not enlarged").
2. **Copy and video describe a different tool (R2).**
   - FAQ/Details say GIF and BMP keep their type (they become PNG). Also say AVIF/TIFF → PNG.
   - The FAQ preview answer says "actual output dimensions".
   - FAQ/Details list 5 of the 9 ratios.
   - The YouTube video shows the old UI, a "10 free uses daily!" caption, ≈53 s of outro and "200+ Free".

## P2
3. **Accessibility:**
   - Label the unit value box (axe critical).
   - Add `aria-pressed` to the ratio buttons.
   - Put the result size in a live region and move focus to the result.
   - There are two elements named "Unit".
4. **Unlocking the aspect ratio selects Fill (stretch).** Default to Cover or Inside.
5. **Print units:** write the entered DPI into JPEG/PNG (the convertCore DPI writers already exist), so 10 cm at 300 DPI prints at 10 cm.
6. **Next step after the result:** Compress Image (KB limits), Convert Image Format, Remove Background. Document Scanner (Premium) and Flip & Rotate (duplicates the built-in rotate) fit less well.
7. **Named size presets:** e.g. 1200×1200 marketplace, 1080×1350 / 1080×1920 social, 1500×500 header. JPEG quality choice.
8. **Phones:** Apply Crop / Resize Image sit below the fold after a file loads. Consider a sticky action bar.
9. **Locales:** English title/meta/body; /ar 404. 9 px header overflow at 320 px (site-wide).
10. **No share or print** on the result (tools.csv lists share/save/print). Print is an unverified absence beyond the result row.
