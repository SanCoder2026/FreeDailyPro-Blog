Sent: 2026-10-30 12:47 ET

# B-0183 Flip & rotate image: several images, small angles, and auto-straighten from EXIF
Priority: P2 · Estimated effort: S · Report: #120 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Fix a whole camera roll of sideways photos in one go, and straighten a slightly tilted scan.

## Why
Rotate CW gives 300×200 → 200×300 correctly, but it is one file and 90° steps only. The Rotate Image endpoint is live on ApyHub. pinetools leads on batch (×74).

## Who uses this
People fixing phone photos and scans for documents or listings.

## Outcomes (ranked)
1. Multiple images, same operation, one ZIP. 2. "Auto (from camera orientation)" that reads EXIF Orientation before stripping it. 3. Fine angle (−45..45°) with a crop or fill choice.

## Constraints
Keep stripping EXIF on download.

## Test cases
3 images → ZIP of 3 rotated. A JPEG with EXIF Orientation 6 → upright after Auto. 5° → straightened with white fill.
