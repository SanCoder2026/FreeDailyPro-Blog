Sent: 2026-11-21 07:23 ET

# Instructions for Claude: FDP-48 Image to PDF

1. Read REPORT.md ("How to work with us" first), then PRIORITIES.md.
2. Fix the shared Download trial-use wrapper: charge per new result and check the cap every time. Same fix as FDP-44–47; verify all of them.
3. Strip EXIF/XMP/IPTC (GPS, camera, owner) from JPEGs before embedding, without re-compressing. Recheck with `testfiles/P25_gps_orient1.jpg` (pdfimages -j, then read EXIF).
4. Pair pages: replace "Free" in titles and metas with trial-use wording.
5. Plan the video re-record on a clean profile.
6. Translate locale tool strings and meta.
7. P3s: dpi for rotated JPGs in Original size, 200 in page cap, TIFF/PDF hints in the drop toast, truncated-JPEG warning, meta/OG/VideoObject.
8. Verify with test-cases.md and `scripts/` (README). No sign-in in automated tests, and no real payments.
9. Wording: "Professional Tools" / "Premium Applications" / "Workflow Products" and "trial uses". Keep the reserved ad slots and the intentional badge.
