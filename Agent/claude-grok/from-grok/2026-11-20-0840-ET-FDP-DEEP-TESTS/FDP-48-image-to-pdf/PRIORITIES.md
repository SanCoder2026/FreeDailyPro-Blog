Sent: 2026-11-21 07:23 ET

# FDP-48 Image to PDF: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | Per-page-load charging: 13 downloads (12 different PDFs, incl. a 60-image and a 16 MB PDF) for 1 trial use in one page load; after the counter synced to 10/10 mid-load, 2 more downloads still went through with no dialog | json/left.json, json/gps.json, outputs/ | Charge per new result (hash of images + options) and check the cap on every Download. Shared ToolPage fix (FDP-44–47) |
| P1 (privacy) | GPS location and camera EXIF are kept inside the PDF: JPGs that need no rotation are embedded byte for byte, so a phone photo's GPS (40°44′54″N 73°59′08″W in the test) travels with the PDF to whoever receives it. Phone photos that needed rotating are re-encoded and lose it, so behaviour is inconsistent | outputs/G01-P25_gps_orient1.pdf, testfiles/P25_gps_orient1.jpg | Strip APP1/EXIF (and XMP/IPTC) segments from JPEGs before `embedJpg` (no re-compression needed: drop the marker segments). Mention it under Privacy |
| P2 | Video: old light UI, "10 free uses daily!", "FREE · PRIVATE · NO LOGIN"; shows the creator's macOS Downloads folder and Chrome downloads list (file names) | video/f17crop.png, f46crop.png, sheet01-02.png | Re-record on a clean profile with the current UI and "trial uses" wording |
| P2 | Five pair pages (PNG/JPG/HEIC/WebP/GIF to PDF) say "Free, No Upload" in the title and "Convert … free" in the meta, while downloads are 10 trial uses a day | json/pairs.json, html/pair-*.html | Use "trial uses" wording (e.g. "PNG to PDF Converter – No Upload, In Your Browser") |
| P2 | Locale pages (see devices-locales findings) | json/matrix-results.json | Translate tool strings and meta |
| P3 | "Original image size" for a JPG with an orientation tag ignores its stored dpi (re-encode drops it): a 300 dpi 1240×1754 scan became a 12.9×18.3 in page instead of 4.1×5.8 in | outputs/L07 | Read the dpi before re-encoding and carry it over |
| P3 | "Original image size" allows pages over the PDF 200 in (14,400 pt) limit: a 20,000 px panorama → 15,000 pt wide page | outputs/L08 | Cap at 200 in (scale down) and say so |
| P3 | TIFF and PDF drops get the generic toast ("2 files can't be used here… Skipped: P08.tiff, P23_document.pdf"), not the tool's helpful "TIFF is not supported yet…" / "use PDF to JPG or Merge PDF" text, which is unreachable from the drop zone | json/left.json L05 | Let the tool's own messages run for .tif/.pdf (or add the hints to the toast) |
| P3 | A truncated JPEG is accepted silently and gives a mostly blank page | outputs/L05 | Warn on decode errors |
| P3 | Meta description 83 chars; og-default; JSON-LD VideoObject title/date differ from the embedded video | html/ | Fuller meta, own OG image, sync VideoObject |

- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:** Save to Google Drive (Google sign-in popup), Save to my cloud storage (email sign-in + $4.99/month add-on dialog), Open from Google Drive; paid-pass behaviour.
