Sent: 2026-11-20 08:40 ET

# FDP-20 Compress Image: live functional findings

Run 2026-11-19 16:41–16:59 EST (box `date`, ET), headless Chromium 1366×900, one fresh guest context per case. Compress itself costs no trial use (`gateAtDownload`); outputs were read from memory via a canvas.toBlob hook (`json/battery.json`, `json/battery-C26_C27.json`) and inspected with Pillow. Starting count in every single-file context: `usageToday` 10/10 (0 remaining), so single-file Download was never reached.

## Battery (C01–C27)

| Case | Input | Setting | Result line (verbatim, shortened) | Output | Verdict |
|---|---|---|---|---|---|
| C01 | photo.jpg 12 MP q95, 2661 KB, EXIF+GPS | Medium | 1844 KB, 3000×4000, JPG, Target reached | q≈0.89, −30.7 %, EXIF/GPS gone | PASS |
| C02 | photo.jpg | Strong | 1284 KB, Target reached | q≈0.79, −51.8 % | PASS |
| C03 | lowq.jpg (already q40), 711 KB | Medium | 512 KB, Target reached | q≈0.28 | PASS (target) / quality note |
| C04 | lowq.jpg | Strong | 233 KB, Target reached | q≈0.19, visible blocking (`screens/live/quality-crops.png`) | P2: no quality warning |
| C05 | photo.jpg | Manual 10 % | 126 KB, toast "Compressed! Reduced by 95.2%" | q 0.10 | PASS |
| C06 | photo.jpg | Manual 100 % | "No setting could make this picture smaller…original is returned unchanged" | original file (still has GPS) | P1 (metadata), copy mismatch (Limitations says Manual can be larger) |
| C07 | photo.jpg | Target 200 KB | 181 KB, 3000×4000 (same size), Target reached | q≈0.13 at full 12 MP: heavy blocking | P2 design: quality before resize |
| C08 | photo.jpg | Target 200 KB + Don't change dimensions | same as C07 | — | PASS |
| C09 | photo.jpg | preset 50 KB | "Reached 46 KB…by resizing to 1650 x 2200 px" | q≈0.15 | PASS |
| C10 | photo.jpg | preset 1 MB | 993 KB (**1,016,321 bytes**), Target reached | > 1,000,000 bytes | **P1** vs copy "portals that count 1 KB as 1000 bytes still accept" |
| C11 | small.jpg 4 KB | Target 200 KB | "already under the target…original is returned unchanged" | original | PASS |
| C12 | logo.png transparent | Medium | 8.7 KB, WEBP, transparency kept | RGBA WebP | PASS |
| C13 | screenshot.png (UI text) | Medium | 78 KB, JPG | q≈0.57; text slightly soft | P3 (PNG → JPG for non-photos) |
| C14 | anim.gif 8 frames | Medium | 29 KB, 400×300, JPG, Target reached | **one frame, animation dropped, no notice** | P2 |
| C15 | vector.svg | Medium | "An SVG is already a small vector file…returned unchanged" | — | PASS |
| C16 | photo.heic | Medium | 944 KB of 1454 KB, JPG | −35 % | PASS |
| C17 | img.webp | Medium | 248 KB, JPG | — | PASS |
| C18 | img.bmp | Medium | 132 KB, JPG | — | PASS |
| C19 | notimage.jpg (text) | — | toast "…could not be read as an image. The file may be damaged or not a picture." | — | PASS |
| C20 | photo.png 7 MB opaque | Medium | 2587 KB, JPG | −63 % | PASS |
| C21–C22 | photo.jpg | Target 0 / −5 KB | toast "Enter a valid target size" only (`json/invalid.json`) | — | P2 a11y: no inline error / aria-invalid |
| C23 | photo.jpg | Target 1.5 MB | 1475 KB, Target reached | — | PASS |
| C24 | photo.jpg | Target 10 KB | "Reached 9.6 KB…by resizing to 900 x 1200 px" | 30 % scale | PASS |
| C25 | photo.png | Target 20 KB, Stop after 0.7 s | toast "Stopped", no result | — | PASS |
| C26 | small_gps.jpg (4 KB, GPS) | Target 200 KB | "already under the target…original is returned unchanged" | result blob **byte-identical to input, GPS 40°44′N 73°59′W present** | **P1** |
| C27 | small_gps.jpg | Manual 100 % | "No setting could make this picture smaller…" | byte-identical, GPS present | **P1** |
| inv | photo.jpg | Target 0.4 KB | after ≈20 s: "126 KB…Target not reached - this is the smallest possible" (full size, q 0.1) | — | as documented in Limitations |

Download code (`js/CompressImage.pretty.js` L109) saves `a.blob` as `compressed_<name>.<ext>`. For C06/C11/C26/C27 `a.blob` is the original file (`utils-BCX55KBw.pretty.js` `E()` / `alreadyUnder` branch), so the "compressed_" download keeps all EXIF and GPS, while the page says next to the controls "Metadata such as location is removed" and the FAQ "Does compressing remove location data from a photo? It does… useful before sharing a photo publicly." The result line does not mention that metadata was kept.

## Gate, dialogs, batch (`json/gate-kbd.json`)
- Start 16:43:43 EST: `usageToday` 10/10, strip "Trial: 10 uses/day · 0 remaining today".
- Compress (Medium) at 0 remaining: result shown, count unchanged (Compress is free; Download is gated, consistent with earlier gated-at-Download tools).
- Download at 0 → "Today's trial uses are done" dialog → "Buy Day Pass — $1" → "Day Pass, $1 | Enter your email…" (stopped; nothing typed). Count stayed 10.
- Save to Google Drive at 0 → same cap dialog (Google sign-in not reached). Save to my cloud storage → "Cloud storage | $4.99 per month, 1 GB… Sign in with your email first" (not signed in).
- Several files (fresh context that loaded with **10 remaining**): 6 files → toast "1 file left out — A batch takes up to 5 files on the trial"; Compress all → "5 of 5 done. 3.75 MB to 2.63 MB in total"; per-file buttons `Download compressed_photo.jpg`, `compressed_logo.webp`, `compressed_img.jpg`…; **Download all (ZIP) downloaded `compressed-images.zip` and the count went 0 → 1** (one use per batch, as the copy says). The ZIP was not opened or kept.
- Batch labels say "Manual quality" / "Custom target"; single mode says "Manual Quality" / "Custom Target" (P3).
- 8 further fresh contexts (16:49–16:58 EST, `json/batchdl.json`) all loaded at 0 remaining, so single-file Download cost, a second download, and the downloaded GPS case remain pending → RERUN row 20.

## Browsers (`json/browsers.json`)
Firefox and WebKit 1440×900: Medium on photo.jpg (Firefox 1887 KB, WebKit 1844 KB), transparent logo → 5 KB target → "Reached 4.8 KB by resizing to 480 x 480 px - WEBP, transparency kept", HEIC opens. No crashes.

## Accessibility (axe + manual)
- Custom Target: number box and KB/MB select have no accessible name (axe `label` critical, `select-name` critical); the visible "Target size" label is not associated.
- Single-file mode buttons expose no selected state (no `aria-pressed`; only colour). Batch mode has `aria-pressed` per code.
- Result line `[data-testid=compress-result]` is not in a live region; focus drops to BODY after Compress; the toast (polite) is the only announcement.
- Keyboard: drop zone reachable in 30 Tabs, Enter opens the chooser; mode buttons work with Enter/Space.
- Invalid targets get a toast only.
