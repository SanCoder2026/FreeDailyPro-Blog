Sent: 2026-11-21 07:23 ET

# FDP-48: how to reproduce (guest, fresh profile, no sign-in)

**Setup:** open https://www.freedailypro.com/tool/image-to-pdf. Test files are in `evidence/testfiles/` (`make-files.py`; some copied from FDP-34).

## P1: per-page-load charging
1. Use a fresh context with uses left (`localStorage['fdp-usage-v1'].usageToday` < 10; fresh contexts often load at 10, so retry).
2. Add R01–R03 → Convert to PDF → Download: +1.
3. Clear all → add other images → Convert → Download; repeat: the counter doesn't move (13 downloads in one load in left.json).
4. Reload → Convert → Download: +1 (or the cap dialog at 10).

## P1: GPS kept in the PDF
1. Add `P25_gps_orient1.jpg` (a JPG with GPS EXIF and no rotation) → Convert → Download.
2. `pdfimages -j <pdf> out` → the extracted JPEG still has Make "TestCam" and GPS 40°44′54.36″N 73°59′8.5″W (`exiftool` or Pillow `getexif().get_ifd(0x8825)`).
3. Compare `P02_orient6_gps.jpg` (needs rotating): re-encoded, no EXIF.

## P2 items
- **Video:** https://www.youtube.com/watch?v=VeWJoEkv8Kk (0:15–0:18 macOS Downloads folder; about 0:46 the Chrome downloads list).
- **Pair pages:** view source of /tool/image-to-pdf/png-to-pdf: `<title>PNG to PDF Converter - Free, No Upload`.

## P3 items
- Original image size + `P24_orient6_300dpi.jpg` → 930×1315.5 pt page (should be about 298×421 pt at 300 dpi).
- Original image size + `P22_panorama_20000.jpg` → 15,000 pt wide page.
- Drop `P08.tiff` + `P23_document.pdf` → generic toast only.

## Gate at 0
- Add, reorder, rotate, Convert all work; the page strip is 92×120 thumbnails and "Preview first page" a 489×633 image.
- Download / Save to Google Drive → cap dialog. Day Pass → email (stop). Quick Buy monthly → Stripe (stop).
