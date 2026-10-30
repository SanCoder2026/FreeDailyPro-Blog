# Retest tracker — cycle 2
| Plan row | Item | Report | Fix-verified | Still broken | Improve | Next action |
|---|---|---|---|---|---|---|
| 1 | Homepage + search | #66 | H1 space | B-0053 + orch B-0041 (ads/search, confirmed); counts = owner decision | search UX | retest after Claude marks B-0053/45 done |
| 2 | Roman Numeral Converter | #66 | 30 Feb validation, US date order | B-0052 (es hreflang/lang, dup JSON-LD) | B-0036 (open), vinculum | retest B-0036/B-0052 when claimed |
| 3 | Audio Comparer | #66 | core scoring still PASS | B-0050, B-0051 | sample, A/B, share | retest when claimed |
| 4 | Pricing + checkout gate | #67 | prices unchanged PASS | B-0027 items open (not claimed) | — | retest when B-0027 claimed; gate pass needs owner OK |
| 5 | Merge PDF | #67 | counting on download, badge disclosure | B-0054 size label | page-level control | retest when claimed; large-file + iOS still to do |
| 6 | Compress PDF | #68 | B-0022, B-0021, counting | B-0056 modes; B-0055 counter | quick-answer fit badge | retest when claimed; target-size/large/iOS still to do |
| 7 | Split PDF | #68 | multi-range ZIP (UI), validation | — | page picker | mature-candidate; recheck every-page count after B-0055 |
| 8 | QR / Custom / Bulk QR | #69 | #43 mobile targets | bulk ",no name" unverified (blocked) | B-0058 | rerun bulk ZIP + custom functional + 2000px |
| 9 | Income Tax | #70 | default state, pre-tax validation | B-0057 (NY 2025 rates, -1 silent, catch-up) | credits (#21) | retest when claimed |
| 13 | Camera Capture | pre-check only | still PASS | — | — | full test in batch 5 |
Next run: first re-check B-0055 (counter) — professional downloads were blocked after ~22:05 ET Oct 29 by the exhausted/flapping pool; then carry-overs (bulk ZIP, custom QR, compress target-size, 2000px QR) and plan rows 10+.

| 10 | Unit Converter | #72 | — | B-0060 GA | B-0062 coverage | mature-candidate |
| 11 | Grammar Checker | #72 | #31 a/an, its, your, jumpd | B-0059, B-0060 | grouping | retest when claimed |
| 12 | URL Shortener (retired) | #72 | /s 410 | B-0061 | — | retest when claimed |
Carry-overs from batch 2 closed in #71 (bulk ZIP, custom QR, 2000 px, target size). B-0055 is still open: recheck after Claude claims it. Next: plan rows 13–15 (Camera Capture, Word Counter, Audio Normalizer).
| 13 | Camera Capture | #73 | — | B-0063, B-0060, B-0041 | timer/mirror (opt.) | retest when claimed; L-052 real device open |
| 14 | Word Counter | #73 | — | B-0065, B-0060, B-0041 | speaking time, keywords | mature-candidate |
| 15 | Audio Normalizer | #73 | #45 Spotify/ACX copy | B-0064, B-0055 | — | mature after B-0064 |
Next: plan rows 16+; recheck B-0055 when claimed.
| 16 | Compress Video + Video to GIF | #74 | batch-12 GIF fixes verified | B-0067, B-0055, B-0041, B-0060 | 10 MB preset (owner) | mature-candidate |
| 17 | Resize & Crop + Compress Image | #75 | fit modes verified (UI) | B-0066, B-0041, B-0055 | auto-resize to target | resize mature-candidate; compress after B-0066 |
| 18 | Sign PDF | #74 | SIGN-01..04 verified fixed | B-0067, B-0068 | — | mature-candidate |
Next: plan rows 19–21 (Universal Converter/PDF↔Word, Barcode, Invoice); pool exhausted for some tools at 23:06 ET.
| 19 | Universal Converter / PDF↔Word | #76 | — | B-0070, B-0055, B-0041 | snippet; theme fonts | PDF→Word mature-candidate; Universal download retest |
| 20 | Barcode Generator | #77 | — | B-0069, B-0041 | print presets, GS1, UPC-E/ISBN | after B-0069 |
| 21 | Invoice Generator | #77 | plan URL fix (/tool/invoice-generator) | B-0071, B-0055 | — | mature-candidate after B-0071 |
| — | Compress Image recheck | #77 | unticked path OK | B-0066 | — | after B-0066 |
Next: plan rows 22+; retest Universal converted download when pool allows.
 22 | BMI / Mortgage / Loan | #78 
 23 | JWT / UUID / Hash | #79 
 24 | Category pages + /tools | #80 
 25 | /developers | #80 
Plan complete. Proposed rows 26+: Find & Replace + Tip + Percentage calc; Book Maker + Book Writing Toolbox + Magazine Maker; Citation Generator + Image to PDF + Screenshot Tool; Password + Random Number + Case Converter; /workflow-products + /multitool-apps.
 26 | Find & Replace + Tip + Percentage | #81 
 27 | Book Maker URL + Book Writing Toolbox + Magazine Maker | #82 
 — | Universal CSV→XLSX carry-over | #81 (OK) 
Next: groups 3–5 (Citation + Image to PDF + Screenshot; Password + Random Number + Case Converter; /workflow-products + /multitool-apps); Barcode UPC-A/ITF-14 + Invoice desktop when pool allows.
 28 | Citation + Image to PDF + Screenshot | #83 
 29 | Password + Random Number + Case Converter | #84 
 30 | /workflow-products + /multitool-apps | #85 
Next: carry-overs after the next trial-use reset (Image to PDF, Password, Case, Barcode, Invoice); Screenshot headed. Proposed new rows: Grammar/Paraphraser follow-ups by GSC, Roman numeral re-snippet check, Income tax snippet, PDF editor / crop-pdf (897/718 impr), Text similarity (1,282 impr), Catalog maker.
