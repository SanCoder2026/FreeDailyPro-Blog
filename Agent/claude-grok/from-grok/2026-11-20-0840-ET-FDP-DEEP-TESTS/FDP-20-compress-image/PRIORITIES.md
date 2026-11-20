Sent: 2026-11-20 08:40 ET

# FDP-20 Compress Image: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | P1 | Returned originals (already under target / not smaller) keep EXIF + GPS; download is named `compressed_…`; page says metadata is removed | C26, C27, C06; `testfiles/preview-C26-1.jpg` (= input, GPS present); `utils` `E()` | Strip metadata losslessly or re-encode; otherwise state "original returned unchanged, including location data" |
| 2 | P1 | 1 MB preset gives 1,016,321 bytes; copy promises 1000-byte-KB portals accept | C10, `testfiles/out-C10.jpg`, Details text | ≥5 % margin for MB targets (or aim under decimal MB); show bytes vs limit |
| 3 | P1 | "Light (10 % smaller)" mode in meta description, 2 FAQ answers + FAQPage JSON-LD, Details ("first three… 90 %"), YouTube description; no such mode | `html/tool-expanded.txt` L90, 94, 108, 132; meta | Rewrite to the 4 live modes (or bring Light back) |
| 4 | P1 | Video shows old UI (Light button, "without losing quality", "10 free uses daily" caption over controls), ≈40 s of 79 s end cards | `screens/video/f009.png`, `f014.png`, `sheet.png` | Re-record on today's UI; caption without "free"; short outro |
| 5 | P2 | Custom Target keeps full resolution at q≈0.13 (heavy blocking) before resizing | C07 vs C09, `screens/live/quality-crops.png` | Quality floor (e.g. 0.5) before stepping down pixels, or offer both |
| 6 | P2 | Strong/Medium on already-compressed JPEG drop to q≈0.19–0.28 without any hint | C03, C04 | Note "quality is now low" when q < 0.4 |
| 7 | P2 | Animated GIF → one-frame JPG, no notice; GIF/BMP missing from accepted-list text | C14 | Warn "animation will be lost" and point to GIF Resizer & Compressor |
| 8 | P2 | Target box and KB/MB select have no accessible name (axe critical ×2) | `json/gate-kbd.json` axeTarget | Associate "Target size" label; `aria-label="Unit"` |
| 9 | P2 | Single-mode buttons expose no selected state | gate modeState | `aria-pressed` like batch mode |
| 10 | P2 | Result line not announced; focus to BODY; invalid targets toast-only, no `aria-invalid` | gate liveRegions/focusAfter, `json/invalid.json` | `role=status` on result; inline error under the field |
| 11 | P2 | iPhone SE: Compress at y≈1532 px (viewport 584) after upload; 32 px buttons | gate iphone-se | Sticky/compact action row on phones |
| 12 | P3 | "Manual Quality can even produce a larger file" (never happens; original returned) | C06 | Fix sentence |
| 13 | P3 | Limitations "down to 30 percent" vs code steps to 12 % | utils | Align text with code |
| 14 | P3 | Toast "Compressed to your target" after Medium/Strong | C01 | "Compressed – 31 % smaller" |
| 15 | P3 | Batch labels "Manual quality/Custom target" vs single "Manual Quality/Custom Target" | gate batch | Same casing |
| 16 | P3 | /es title "…gratis"; YouTube title/description "Free"; video embed title differs from YouTube title | `html/es_tool_compress-image.html`, `video/v.info.json` | "Professional Tools"/"trial uses" wording |
| 17 | P3 | No /blog/compress-image (404); ad caption contrast on Pixel 7 (reserve and style the slot, don't remove) | curl, matrix a11y | Optional guide; caption contrast |
| 18 | P3 | 9 px header overflow at 320 px (site-wide) | matrix iPhone SE | Site-wide header fix |
| — | pending | Single-file Download cost, 2nd download, name/bytes, GPS in downloaded unchanged original | RERUN row 20 | Run `scripts/ci-reset.js` after 7:00 PM ET |
