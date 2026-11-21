Sent: 2026-11-21 01:26 ET

# FDP-33 Video Thumbnail Generator: test cases

- **URL:** https://www.freedailypro.com/tool/thumbnail-gen, guest.
- **Inputs:** `evidence/testfiles/` (V3, V4, V5, X1, X2 shipped; V1/V2 recreated by `make-videos.sh`).
- **"Live"** = 2026-11-21 00:57–01:21 EST. Scripts: `tg-live.js`, `tg-hang.js`, `tg-gate.js`, `tg-drain.js`, `tg-share.js`, `tg-misc.js`, `run-matrix.js`.

| ID | Step | Expected | Live |
|---|---|---|---|
| TG-01 | Drop V1 (H.264 1920×1080), 0:03.5, Capture, Original | PNG 1920×1080 | PASS |
| TG-02 | Drop V2 (1080×1920), Capture | PNG 1080×1920 | PASS |
| TG-03 | Drop V3 (VP9 WebM 1280×720), Capture | PNG 1280×720 | PASS |
| TG-04 | +1 frame | next frame, name 03.53s | PASS (step fixed 1/30 s, P3) |
| TG-05 | YouTube 1280×720, Fill | 1280×720 | PASS |
| TG-06 | YouTube 4K 3840×2160 | 3840×2160, upscale warning | PARTIAL (no warning; "recommended") |
| TG-07 | Shorts 4K 2160×3840 | 2160×3840 | PASS (same upscale note) |
| TG-08 | Shorts/Reels 1080×1920, Fit | black bars, 1080×1920 | PASS |
| TG-09 | Square 1080×1080 + title (Devanagari, emoji) | renders, outlined | PASS |
| TG-10 | Long title | wraps within ~90 % width | PASS |
| TG-11 | JPG format | image/jpeg, smaller | PASS (60 KB vs 201 KB) |
| TG-12 | Time "0:59" on a 5 s clip | clamps, box shows the clamped time | PARTIAL (box keeps 0:59) |
| TG-13 | Time "abc" | clear toast | PASS |
| TG-14 | Suggest frames | ~10 previews, best starred | PASS (1.3 s) |
| TG-15 | V4 HEVC | fallback message; typed time → capture via engine | PASS (1.8 s, jsDelivr) |
| TG-16 | V5 black | captures; Suggest skips dark frames | Not run (file shipped for the rerun) |
| TG-17 | X1 .txt | "isn't a video file" | PASS |
| TG-18 | X2 text renamed .mp4 | "can't be read as video" | PARTIAL ("often iPhone HEVC", then "Could not read that frame") |
| TG-19 | Request scan in all runs | no upload / big POST | PASS |
| TG-20 | Uses left: Capture ×2 | uncounted | PASS (0 → 0; label says Download costs) |
| TG-21 | Uses left: per-image Download | −1 use, badged file | PASS (0 → 1, badge intentional) |
| TG-22 | Uses left: Download all as ZIP (2) | per Santosh's policy | **Policy question** (1 → 1, no dialog) |
| TG-23 | Reload | count persists | PASS |
| TG-24 | At 0: Download | cap dialog → Day Pass email prompt | PASS (stopped) |
| TG-25 | At 0: ZIP | cap dialog | PASS |
| TG-26 | At 0: Capture / Suggest | per policy | Work (results free, download gated) |
| TG-27 | Quick Buy day | Day Pass $1 email prompt | PASS (stopped) |
| TG-28 | Quick Buy monthly | Stripe Checkout | PASS (stopped) |
| TG-29 | Save to Google Drive | — | **Untested: Google sign-in** |
| TG-30 | Save to my cloud storage | — | **Untested: email sign-in, $4.99/month 1 GB** |
| TG-31 | Open from Google Drive | — | Untested (not clicked; presumed sign-in) |
| TG-32 | Keyboard: Tab to drop zone, Enter | file chooser opens | PASS |
| TG-33 | Share | plain tool URL | PASS |
| TG-34 | Matrix: 10 devices, 11 locales, 6 geo, axe | no overflow; translated | PARTIAL (iPhone SE 9 px; English head/headings; /ar 404; 3 axe rules) |
