Sent: 2026-11-20 08:40 ET

# FDP-04 Compress PDF: reproduce

- **Written:** 2026-11-19 11:25:55 EST (box `date`, ET).
- **Setup:** guest or fresh profile, no sign-in, no ad clicks. Inputs: `evidence/testfiles/` (small files) or `python3 scripts/make-testpdfs.py <dir>` (all 17; seeded, so the same files are produced).
- **Check outputs:** `OUT_JSON=out.json python3 scripts/inspect-output.py <file.pdf>...`.
- **Trial uses:** Compress is free; each Download spends 1. If the strip shows "0 remaining today", compress steps still work but downloads open the cap dialog; use another fresh context or wait for midnight UTC (7:00 PM ET).
- **Automation:** run from a folder with Playwright installed (`cd /workspace/deep/tools-env`). The scripts write to `/workspace/deep/04-compress-pdf/live/`; edit `OUT`/`T` at the top.

## R-01: fresh contexts load at 0 remaining

1. Open https://www.freedailypro.com/tool/compress-pdf in several fresh incognito profiles, or run `node scripts/cp-probe.js`.
2. Read the strip "Trial: 10 uses/day · N remaining today" and localStorage `fdp-usage-v1` before any action.
3. **Seen 2026-11-19 10:58–11:22 EST:** 28 of 31 at 0, with `usageToday 10` and `allowed false` (`evidence/json/probe.json`, `battery-*.json`, `matrix-results.json`).
4. **Expected:** 10.
5. Display-only evidence; verify server-side.

## R-02: level rows don't wrap

1. Add `A_photos_6p.pdf` → Balanced → Compress PDF.
2. **Desktop 1366 px:** each "Level N: …" label is about 48 px wide, one word per line, next to Compare / Download / (cap note) / Save to Google Drive / Save to my cloud storage.
3. **Pixel 7:** `document.documentElement.scrollWidth` = 958 after Compress, and Compare overlaps the label.
4. Script: `node scripts/cp-kbd.js` (`levelRowWidths`, `phone.sw`). Evidence: `screens/live/desktop-level-rows-crop.png`, `phone-level-rows-crop.jpg`.

## R-03: CMYK file called a JBIG2/JPEG 2000 scan

1. Add `I_cmyk_2p.pdf` (10.26 MB, two DCTDecode /DeviceCMYK photos; see `json/input-inspection.json`) → Balanced → Compress.
2. **Seen:** "This PDF is a scan that is already compressed: its pages are stored as scanner pictures (JBIG2 or JPEG 2000)… so nothing was changed", while the breakdown above says "Most of this file is pictures, so Balanced should shrink it a lot". The batch returns it at 10.26 MB.
3. **Expected:** the true cause (CMYK pictures), or actual shrinking.
4. Evidence: `screens/live/cmyk-misdiagnosis-crop.png`.

## R-04: Extreme stops at colour 70 dpi

1. `A_photos_6p.pdf` → Extreme → Compress → "Stopped at level 2…" → **Run anyway**.
2. **Seen:** L3 "Photo and shaded areas at 70 dpi — 214.7 KB · pages are pictures", then it ends. No grey or B/W level and no note.
3. Script: `node scripts/cp-capped2.js` (`extremeLevels`). Evidence: `screens/live/extreme-runanyway-crop.jpg`.

## R-05: the mark is disclosed only in the cap dialog

1. In a capped context, compress anything and click Download.
2. The dialog says "Either pass removes the 'Created with FreeDailyPro.com' mark from your PDFs and images."
3. Nothing on the page (meta, FAQ, the result card) mentions the mark.
4. **After midnight UTC:** `node scripts/cp-battery.js 6`, then `pdftotext <out> - | grep -c "Created with"`.

## R-06: video outdated

https://www.youtube.com/watch?v=XZDDliVHrLY: frames f05–f11 show "Light / Medium (25% smaller) / Strong (50% smaller) / Target Size" and "10 free uses daily" (`evidence/video/frames/`). Compare the titles: YouTube "How to Use Compress PDF – Free Step-by-Step Walkthrough", JSON-LD "How to Compress PDF File Size Online", sitemap "How to Compress PDF File Size Free Online".

## R-07: locales

- `curl -s https://www.freedailypro.com/de/tool/compress-pdf | grep -o "<title>[^<]*"` → English (the same for pt, fr, ja, hi, zh, ko, id).
- /es → "Comprimir PDF a un tamaño objetivo: gratis, sin registro".

## R-08: blog

https://www.freedailypro.com/blog/compress-pdf: no Target size, levels, Compare or batch; FAQ "Can I compress password-protected files? Unlock… first" (`evidence/html/blog-visible.txt`).

## R-09: non-PDFs called damaged

Add `N_text_renamed.pdf`, `O_png_renamed.pdf` or `P_empty.pdf` → '"…" can't be read — it looks damaged. Try the Repair PDF tool…' (`json/explore-*.json` BAD_*).

## R-10: target bytes

`A_photos_6p.pdf` → Target 1 MB → "1002.6 KB, under your 1.00 MB target". If KB = 1024 that is about 1,026,662 bytes, which is over a decimal 1,000,000-byte limit. Download it after the re-run and check the bytes.

## R-11: mobile empty state

`node run-matrix.js scripts/config.json --only=devices` → iPhone SE scrollWidth 329 > 320; the fold ends at "One file / Several files" (`screens/devices/iphone-se-fold.png`).

## R-12: focus

`node scripts/cp-kbd.js` → `focusAfterAdd` and `focusAfterCompress` are BODY.

## Sign-in-gated (not tested)

On https://www.freedailypro.com/tool/compress-pdf: "Open from Google Drive" and "Save to Google Drive" (Google login), and "Save to my cloud storage" (email sign-in plus a $4.99/month add-on).
