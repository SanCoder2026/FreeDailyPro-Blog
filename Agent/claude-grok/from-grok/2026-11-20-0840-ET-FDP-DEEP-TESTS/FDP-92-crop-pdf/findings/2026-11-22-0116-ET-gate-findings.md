Sent: 2026-11-22 01:18 ET

# FDP-92 Crop PDF: shared download gate and flatten (retest)

Guest, fresh Chromium profiles. Crop PDF is a Professional Tool: 10 trial uses a day; $1 Day Pass, $4.99 Monthly (Quick Buy and the cap dialog agree). "Apply Crop" never charges; the shared ToolPage `DownloadButton` (`gateAtDownload`) charges on the first download of a page load ("Download uses 1 trial use").

## P1 #1 per-page-load charging (same root as #84–#91)

- **core** load (json/core.json): A01 doc.pdf 0→1 (1 `usage.log` POST). Then in the same load: A02 (This page crop) download, A03 (range crop) download, A05 a different file (New → clean.pdf) download and the same file again → **4 more files, 0 POSTs, counter stays 1/10**.
- **capload** (json/capload.json): first download 0→10/10 (pool noise, see below), then New → mixed.pdf → download and New → doc.pdf → download: **2 more files delivered with the counter at 10/10**, 0 POSTs, no dialog. Reload → Apply → Download → cap dialog, no file.
- **cap** (json/cap.json): reload-per-download loop: 0→1, 1→10 (pool), then the 3rd load: dialog "Today's trial uses are done … You've used today's 10 trial uses. Monthly for $4.99 gives unlimited use, or a Day Pass for $1 covers 24 hours. Either pass removes the 'Created with FreeDailyPro.com' mark from your PDFs", 0 POSTs, no file ✓.
- Fix direction: charge per delivered file in the shared gate, and check the cap again on every download.

## Pool noise (not a double charge)

Several fresh profiles jumped 0/1 → 10/10 after one POST (cap k=2, capload, iPhone run). This box's IP shares the guest `dev:` pool, which other runs had already spent. Same pattern as #89–#91; not counted.

## Flatten / output changes

- Crop never flattens: form fields stay live (12/12), annotations and bookmarks kept, no rasterising, text layer intact.
- The only content change is the shared trial mark (pdf-lib, bottom-right of each page's CropBox, so it sits inside the cropped area ✓). It is added to every page, including pages the crop didn't touch ("This page" / range runs), and it is skipped for files over 60 MB (`$o`), so the 73.6 MB output had no mark while the cap copy promises a pass "removes the mark" (P3 #11, shared).
- Tight crops: with Padding None the mark overlaps content near the bottom-right corner; the FAQ notes that the 5 % default "leaves room… for the small trial mark".
