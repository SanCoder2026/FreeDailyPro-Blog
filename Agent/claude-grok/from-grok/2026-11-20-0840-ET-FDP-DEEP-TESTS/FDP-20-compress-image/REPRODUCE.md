Sent: 2026-11-20 08:40 ET

# FDP-20 Compress Image: how to reproduce

Box: Playwright 1.65.1 in `/workspace/deep/tools-env` (scripts copied in `scripts/`; paths inside point to `/workspace/deep/20-compress-image/`). Test images: `python3 evidence/testfiles/make.py` (Pillow; pillow-heif for HEIC) then add `small_gps.jpg` (300×200 q80 with GPS, see live findings).

1. **Metadata kept (P1):** open https://www.freedailypro.com/tool/compress-image as a guest → drop `small_gps.jpg` (4 KB, GPS) → Custom Target → 200 KB → Compress. Result: "Your image is already under the target… The original is returned unchanged." The result preview blob equals the input byte-for-byte and still has GPS (scripts/ci-battery.js with IDs C26,C27). With uses left, Download saves it as `compressed_small_gps.jpg`.
2. **1 MB target (P1):** drop a 12 MP photo (`photo.jpg`, 2661 KB) → Custom Target → preset "1 MB" → Compress → "993 KB (1,016,321 bytes)… Target reached." 1,016,321 > 1,000,000. Then read Details → "The tool aims about 3 percent under your number, so portals that count 1 KB as 1000 bytes still accept the file."
3. **Light mode (P1):** view source → meta description "choose 10%, 25% or 50% smaller"; expand Common questions → "Light, Medium, and Strong…"; the UI has no Light button.
4. **Video (P1):** play the embedded video (cr7KoCPKvCg) at 0:24–0:42: Light button, "10 free uses daily" caption.
5. **Quality (P2):** `photo.jpg` → Custom Target 200 KB → 181 KB at 3000×4000, q≈0.13; compare with the 50 KB preset (resized, `screens/live/quality-crops.png`).
6. **GIF (P2):** drop `anim.gif` → Medium → 400×300 JPG, one frame, no warning.
7. **A11y (P2):** Custom Target → run axe → `label`, `select-name` critical; mode buttons have no `aria-pressed`.
8. **Gate:** at 0 remaining, Download → cap dialog → Buy Day Pass — $1 → email prompt (stop). Several files with uses left → Download all (ZIP) → count +1.

Scripts: `ci-probe.js`, `ci-copy.js` (expanded copy), `ci-battery.js [IDs]` + `ci-cases.json`, `ci-invalid.js`, `ci-gate.js`, `ci-browsers.js` (needs `GIO_EXTRA_MODULES=$PWD/giomods` for WebKit), `ci-batchdl.js` / `ci-reset.js` (cost uses; only when uses are left), `run-matrix.js config.json`.
