Sent: 2026-11-21 13:37 ET

# FDP-63 test cases

| ID | Case | Expected | Result |
|---|---|---|---|
| Z01 | Upload at cap | No charge | PASS (0 POST) |
| Z02 | Pick at cap | Values shown | Shown (owner question) |
| Z03 | Magnifier | Follows pointer | PASS |
| Z04 | Copy ×4 at cap | Cap dialog, no clipboard | PASS |
| Z05 | Palette click at cap | Values | PASS |
| L01 | Upload with uses left | No charge | PASS |
| L03 | Copy HEX/RGB/HSL/CMYK | Charge per copy | FAIL: only first charged |
| L04 | Palette copy | Charge | FAIL: free |
| L05 | New image, copy | Charge | FAIL: free |
| L06 | Reload, copy | Charge | PASS (+1) |
| C01 | Quadrant accuracy | Exact hex | PASS |
| C02 | 4000×3000 corner (3999,2999) | #123456 | PASS |
| C03 | JPEG q60 | ±2 | PASS |
| C04 | 25 % alpha red | Alpha shown or noted | #ff0000, no note (P3) |
| C05 | EXIF 6 | Upright, picks follow display | PASS |
| C06 | 300×3000 tall | Top/bottom values | PASS |
| C07 | 1×1 | Pick + palette | PASS |
| C08 | Non-image | Error message | FAIL: silent |
| K01 | Arrow / Shift+arrow | 1 / 10 px | PASS (debug.json) |
| T01 | Tap (Pixel 7, iPhone 14) | Pick | PASS |
| D01 | Google Drive | Picker | Sign-in popup (untested) |
| CAM | Take photo (desktop) | File chooser | PASS |
| Q01 | Quick Buy Day / Monthly | Email / Stripe | Stopped |
| FF | Firefox cap + left | Same as Chromium | PASS / same per-load gap |
