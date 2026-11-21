Sent: 2026-11-21 13:02 ET

# FDP-61: how to reproduce (guest, fresh profile)

Test photos: `evidence/testfiles/` (built by `scripts/make61.py`).

## P1-1 Edit as Word / Excel 404
1. Open https://www.freedailypro.com/tool/document-scanner. Add `p6-straight.png`. Click Continue, then Skip — Already Straight.
2. Click **Edit as Word** → URL `/tools/image-to-word` → "Hmm, we couldn't find that page". Same for **Edit as Excel** (`/tools/image-to-excel`).
3. Compare https://www.freedailypro.com/tool/image-to-word (200).

## P1-2 EXIF rotation
1. Add `p7-exif-orient6.jpg`. Any image viewer shows it upright with the title "EXIF ROTATED" at the top.
2. At the Crop step the photo is turned 90° clockwise (title on the right edge, reading downward). Continue → Straighten → the scan is sideways (M05.png).
3. Same on Chrome, Firefox and Safari.

## P1-3 Per-page-load charging
1. Use a profile with Premium uses left (strip "2 remaining today").
2. Scan `p1-tilted.jpg` → Download PDF (one `usage.log` POST; the counter goes up).
3. Click New, then scan `p2`, `p3` and `p4` and Download PDF each time. Each downloads, with no POST and no cap dialog, even when the strip reads "0 remaining".
4. Reload, scan anything, Download PDF → the cap dialog appears.

## P2 copy
Common questions → "Does this automatically detect…?" says No. Compare the Straighten step message "Page found automatically…". Details → Privacy: "no engine is downloaded" vs the searchable-PDF FAQ.

## P2 video
YouTube fILxNjJP3ZY, 0:20–0:40: one-step page, "10 free uses daily", "Use Camera Instead", "Download Scanned Image", captions about Black & White / threshold.

## P2 below the fold
1366×768 desktop: the drop zone starts at ~1,150 px.

## P3 overlay / keyboard / not-image / stale status
- At the Straighten step, the blue outline covers only the top-left part of the photo. Tab never reaches the handles.
- Add `notanimage.jpg` → empty Crop box, no message.
- At the cap: Download PDF → close the dialog → New → add a photo. The "Today's trial uses are used up…" line is still shown.

## Payment (stop points)
Quick Buy (Day pass) → "Premium Day Pass, $3 · Email" (stop). Quick Buy (Monthly) → checkout.stripe.com (stop).
