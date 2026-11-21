Sent: 2026-11-21 02:08 ET

# FDP-35 Video Converter: test cases

Synthetic inputs from `scripts/make-videos.sh`. Scripts: `cvv-live.js` (K cases), `cvv-gate.js`, `cvv-pairs.js`, `cvv-share.js`, `cvv-misc.js`, `run-matrix.js`.

| ID | Area | Input / action | Expected | Result 2026-11-21 |
|---|---|---|---|---|
| CV-01 | Rewrap | H.264/AAC MP4 → MP4 / MOV / MKV / MP4 for web | copied under 1 s, summary says copied, plays, same streams | PASS (K01–K03, K22) |
| CV-02 | Rewrap | 1080p H.264 MOV → MP4 | copied | PASS (K06) |
| CV-03 | Rewrap | H.264 MKV → MP4 | copied | PASS (K09) |
| CV-04 | Rewrap | 3GP H.264/AAC → MP4 | copied | PASS (K13) |
| CV-05 | Rewrap | H.264 no audio → MOV | copied, no audio track | PASS (K15) |
| CV-06 | Re-encode | → WebM | VP8/Vorbis ≤1280 wide | PASS (K04) |
| CV-07 | Re-encode | → AVI | MPEG-4/MP3; size note shown | PASS (K05) |
| CV-08 | Re-encode | HEVC iPhone MOV → MP4 | H.264/AAC, plays | PASS (K07) |
| CV-09 | Re-encode | VP9/Opus WebM → MP4 | H.264/AAC; >25 % note | PASS (K08) |
| CV-10 | Re-encode | MPEG-4 AVI / WMV / FLV → MP4 | H.264/AAC | PASS (K10–K12) |
| CV-11 | Re-encode | animated GIF → MP4 | silent H.264 MP4 | PASS (K14) |
| CV-12 | Re-encode | H.264 + MP3 audio → MP4 | re-encoded (audio → AAC) | PASS (K16) |
| CV-13 | Re-encode | 1080p VP8 WebM → WebM | scaled to 1280×720, same-format note | PASS (K19, K23) |
| CV-14 | Long | 60 s 40 MB MP4 → WebM | finishes, progress shown | PASS (K20, 33 s) |
| CV-15 | Reject | MP3 audio only | clear 'isn't a video file' | PASS (K17) |
| CV-16 | Reject | text file renamed .mp4 | clear 'not a video' message | FAIL P3 (K18 phone-codec error after 11.6 s) |
| CV-17 | Limit | 70 MB MP4 on trial | clear 50 MB message, Convert disabled; copy agrees | PARTIAL P2 (works; drop zone says over 5 GB) |
| CV-18 | Pairs | mov-to-mp4, mp4-to-webm, gif-to-mp4, mp4-to-avi, wmv-to-mp4 | output preselected | PASS |
| CV-19 | Pairs | all 11 pair titles | no 'Free' | FAIL P2 |
| CV-20 | Privacy | any conversion | no video bytes in requests; only jsDelivr engine | PASS |
| CV-21 | Gate | first Download with uses left | −1 use | PASS (0→1) |
| CV-22 | Gate | second Download of same file | per owner decision | Observed 1→1 |
| CV-23 | Gate | Download of a different video after New | −1 use (Nov 20 every-Download decision) | FAIL P1 (1→1, twice) |
| CV-24 | Gate | Download after reload | −1 use | PASS (1→2) |
| CV-25 | Gate | Convert | no use (charge at Download) | PASS (0→0) |
| CV-26 | Gate | preview player at 0 remaining | no full-quality copy without a use | FAIL P1 (same sha as paid Download; native Download available) |
| CV-27 | Gate | Download at 0 | cap dialog | PASS |
| CV-28 | Payment | cap dialog → Buy Day Pass | email prompt (stop) | PASS |
| CV-29 | Payment | Quick Buy day / monthly | email prompt / Stripe Checkout (stop) | PASS |
| CV-30 | Sign-in | Save to Google Drive | sign-in (untested) | UNTESTED (Google popup) |
| CV-31 | Sign-in | Save to my cloud storage | sign-in (untested) | UNTESTED (email sign-in dialog) |
| CV-32 | Share | Share button | copies tool URL only | PASS |
| CV-33 | Keyboard | Tab to drop zone + Enter | file chooser opens | PASS |
| CV-34 | Copy | output count in FAQ / Limitations / subtitle / JSON-LD | six, matching the menu | FAIL P2 |
| CV-35 | Video | zqpLPhmyj9E | current UI, clean desktop, no 'Free' | FAIL P2 |
| CV-36 | Devices | 10 devices | no overflow | PARTIAL (iPhone SE 9 px) |
| CV-37 | Locales | 10 locales + /ar | translated, no overflow | PARTIAL (English titles, ja 3 px, /ar 404) |
| CV-38 | axe | desktop + Pixel 7 | no serious issues | FAIL P3 (link-in-text-block, label mismatch, ad caption contrast) |
