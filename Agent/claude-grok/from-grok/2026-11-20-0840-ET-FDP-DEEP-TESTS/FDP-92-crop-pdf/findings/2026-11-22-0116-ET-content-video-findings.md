Sent: 2026-11-22 01:18 ET

# FDP-92 Crop PDF: page copy, guide, video, SEO

## Page copy (tool-expanded.txt): mostly accurate

Accurate and verified: scope choices; share-of-page box; Auto-trim union, padding menu (None/2/5/10 %, 5 % default), blank pages skipped; cut-off warning buttons; rotated pages cropped where drawn; CropBox-only disclosure (5 places); "It also will not make the file smaller"; "cropped_" file name; runs in the browser.

Wrong or unclear (P3 #9):
- "Can I undo a crop after downloading? No — … the crop is permanent in that file" vs "can be recovered by software that ignores crop boxes". Suggest: "This tool can't widen it again, but the trimmed content is still in the file."
- "treating anything close to white as background" / "pixels darker than near-white": the cut-off is 250/255, so paper at 249 counts as content (P2 #2). Say "pure white" or relax the threshold.
- Padding "None" still leaves ≈1 % (0.1 in on Letter).
- "Download uses 1 trial use" is not what happens (P1 #1).

## Guide /blog/crop-pdf ("Trim Scanner Shadows and Stray Footers From an 18-Page PDF", 2026-10-17)

Good: explains CropBox-only and points to Redact PDF; warns Auto-trim is fooled by shadows and coloured paper; explains the warning.
Wrong (P3 #9):
- "adds about one percent padding" — default is 5 % (page FAQ says 5 %).
- "The first page appears with Previous and Next buttons above it" — they are below the preview.
- "Each crop run counts toward your 10 trial usages for the day" — charging is per page load (P1 #1).
- Its own scenario (gray-paper scans) is where Auto-trim silently selects the whole page (P2 #2); the guide only warns about the dark shadow band.

Second linked guide /blog/rotate-pdf-fix-sideways-scans: about Rotate PDF; fine as a next step.

## Video IQB9dwWbjEc "How to Use Crop PDF – Free Step-by-Step Walkthrough" (uploaded 2026-09-22, 1:16, 11 views)

- Read via the public watch page (yt-dlp was bot-blocked from this box) and the YouTube storyboard (screens/video-sheet, video-zoom).
- Shows an older Crop PDF: drag a box on a peacock image, Apply, Download. No margin fields, Auto-trim, Padding, scope buttons or cut-off warning. Captions "Drag and drop your PDF then set the crop area or margins", "Download your cropped PDF — 10 free uses daily!" (10/day still true). It never says the cropped area is only hidden (P3 #9). ~45 s of tool, then a 30 s outro.
- JSON-LD VideoObject name "How to Crop PDF Pages Online" (YouTube title differs), no `duration`.

## SEO / indexing

- 200, canonical self, title "Crop PDF Online - Trim Margins on Every Page | FreeDailyPro", meta description fits "crop pdf"; H1 "Crop PDF"; hreflang ×10 + x-default; in sitemap with /blog/crop-pdf; JSON-LD SoftwareApplication (Offer 4.99) + FAQPage (13) + VideoObject.
- Locale pages /de /es /ja /hi … return 200 with the English title, H1 and tool (P2 #3, sitewide). /ar → 404.
