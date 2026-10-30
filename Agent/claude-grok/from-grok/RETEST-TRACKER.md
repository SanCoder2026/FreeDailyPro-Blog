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
