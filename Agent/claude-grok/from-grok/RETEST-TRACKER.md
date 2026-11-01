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
| 31 | Image to PDF / Password / Case (carry-over) | #86 | outputs verified | B-0081 | — | Image to PDF + Password mature |
| 32 | Barcode / Invoice / Universal (carry-over) | #87 | barcode + universal outputs verified | B-0069, B-0071, B-0070, B-0082 | — | Barcode mature after B-0069 |
| 33 | Capability gap 1: Income Tax / Tip / BMI | #88 | — | B-0089, B-0090, B-0091, B-0057, B-0077, B-0078, B-0073 | — | none mature under the new rule |
| 34 | Capability gap 2: Mortgage / Percentage / Loan | #89 | — | B-0086, B-0087, B-0088, B-0072 | — | none mature; Loan + Percentage re-labelled |
| 35 | Capability gap 3: Roth / 401(k) / Compound Interest | #90 | — | B-0100, B-0101, B-0102, B-0088 | — | none mature; Roth tool missing |
| 36 | Capability gap 4: College 529 / RMD / FIRE | #91 | — | B-0103, B-0104, B-0105 | — | none mature; FIRE closest |
| 37 | Capability gap 5: SIP / Paycheck / Social Security | #92 | — | B-0106, B-0107, B-0108 | — | none mature |
| 38 | Capability gap 6: Unit Converter / Body Fat / GPA; Book DOCX import | #93, #94 | — | B-0109–B-0112, B-0062 verified | — | B-0062 fixed; none mature |
| 39 | Capability gap 7: Cost of Living / Roman Numeral / Random Number | #95 | — | B-0113, B-0114, B-0115 | — | none mature; RNG output blocked by trial gate |
| 40 | Capability gap 8: Currency / Time Zone / Password | #96 | — | B-0116, B-0117, B-0118 | — | none mature; carry-over: RNG + Password output |
| 41 | Capability gap 9: Audio Comparer / Merge PDF / Word Counter (top traffic) | #97 | — | B-0119, B-0120, B-0121 | — | none mature; L-043 partly fixed |
| 42 | Admin carry-over: RNG / Password / Audio / Merge size | #98 | RNG + Password output, Merge label OK | B-0122 new; B-0050 evidence | — | carry-over closed except L-176, B-0051 |
| 43 | Claimed-fixed retest debt (§9): B-0057, B-0056, B-0053, B-0059, B-0060, B-0052, B-0027, B-0055 | #99, #100, #101 | B-0057, B-0056 (UI), B-0053, B-0052, B-0027 verified; B-0055 exhausted state OK | — | B-0059, B-0060, B-0055 CNT-02 need browser | L-022 relabelled; B-0119-v2 |
| 44 | /es + locale H1 (B-0123) | #102 | — | B-0123 | — | L-189 open |
| 45 | Calculators/finance sweep: marketplace-fee, state-tax, sales-tax | #103 | math OK on all 3 (L-194) | B-0124, B-0125, B-0126 | — | L-190–L-193 open |
| 46 | Calculators/finance sweep 2: self-employment-tax, VAT, UK tax | #104 | math OK on all 3 (L-195–L-197) | B-0127, B-0128, B-0129 | — | gap briefs only; L-004 evidence |
| 47 | Calculators/finance sweep 3: break-even, profit-margin, discount | #105 | math OK on all 3 (L-198–L-200) | B-0130, B-0131, B-0132 | — | gap briefs only; L-004 evidence |
| 48 | Calculators/finance sweep 4: GST, India income tax, student loan | #106 | math OK on all 3 (L-201–L-203) | B-0133, B-0134, B-0135 | — | gap briefs only |
| 49 | Calculators sweep 5: budget planner, BMR, calorie | #107 | math OK (L-204–L-206); counter + floor case need browser run | B-0136, B-0137, B-0138 | — | L-004 evidence |
| 50 | Next-category sweep 1 (GA-ranked untested): screenshot-tool, magazine-maker, STL converter | #108 | 1 bug (L-207), 1 a11y (L-208), 1 needs browser (L-209); L-206 verified via #107 addendum | B-0139, B-0140, B-0141 (+B-0138-v2) | — | L-004 + L-143 evidence |
| 51 | Untested-by-traffic sweep 2: emoji-picker, sprite-sheet-tool, passport-photo | #109 | emoji copy gated (L-210 owner decision); passport a11y (L-212); L-209 verified via #108 addendum | B-0142, B-0143, B-0144 (+B-0141-v2) | — | L-004 evidence |
| 52 | Untested-by-GSC sweep 3: audio-speed-changer, mesh-3d-converter, catalog-maker | #110 | mesh strong (L-214); audio duration/a11y (L-213); catalog a11y (L-215) | B-0145, B-0146, B-0147 | — | L-004 evidence |
| 53 | Untested-by-GSC sweep 4: ascii-art, paper-format-checker, text-paraphraser | #111 | ASCII false "Copied" toast (L-216); paper/paraphraser gated, need admin run; #110 addendum verified 4 downloads | B-0148, B-0149, B-0150 | — | L-004 evidence |
| 54 | Untested-by-GSC sweep 5: job-experience, yt-thumbnail, invisible-text | #112 | 2 minor validation bugs (L-219, L-221); #111 addendum: paper checker correct, paraphraser stale-mode bug | B-0151, B-0152, B-0153 (+B-0154) | — | L-004 evidence |
| 55 | Untested-by-GSC sweep 6: audio-trimmer, silence-remover, audio-merger + site-wide | #113 | merger silent drop at 0 trial uses (L-224); fixture v2 (L-225) | B-0155, B-0156 (site-wide), B-0157–B-0159 | — | L-004 evidence |
| 56 | Untested-by-GSC sweep 7: mesh-3d-viewer, image-quality-enhancer, text-similarity-checker | #114 | mesh viewer gated on preview (L-226); #113 addendum: fixture verified, audio fidelity B-0163 | B-0160–B-0162 (+B-0163) | — | L-004 evidence |
| 57 | Untested-by-GSC sweep 8: merge-video, pdf-editor, crop-pdf | #115 | merge-video silent drop (L-230); invalid-PDF silence (L-231/232); #114 addendum mesh+enhancer verified; B-0163-v2 silence bug | B-0164–B-0166 (+B-0161-v2, B-0163-v2) | — | L-004 evidence |
| 58 | sweep 9: fancy-font (last GSC), document-scanner, color-picker-image (GA) | #116 | GSC list exhausted; scanner paywall before preview (L-234); #115 addendum: merge/crop verified, editor rectangle missing (L-231) | B-0167–B-0169 | — | L-004 evidence |
| 59 | GA-views sweep 1: audio-converter, color-converter, user-agent-parser | #117 | all three accurate; minor validation gaps; #116 addendum: scanner black-page bug, picker copy verified, recorder timer | B-0171–B-0173 (+B-0174); B-0170 filed (editor shapes dropped) | — | L-004 evidence |
| 60 | PDF-category sweep (GA top-50 exhausted): rotate-pdf, remove-pdf-pages, pdf-watermark | #118 | UI/validation strong; empty watermark text silent; outputs gated | B-0175–B-0177 | — | L-004 evidence |
| 61 | Rule 1 (live paid API endpoints): redact-pdf, repair-pdf, extract-audio | #119 | redact 6/6, repair recovers; no-audio silent fail; repair copy | B-0178–B-0180 | — | L-004 evidence; L-243 decided |
| 62 | Rule 1: fillable-forms, organize-pdf, flip-rotate-image (+ #119 addendum: redact site clean vs B-0098) | #120 | required-field silent no-op; counter mismatch evidence | B-0181–B-0183 | — | L-004, L-143 evidence |
| 63 | Rule 1: flatten-pdf, base64, markdown-html-converter (+ #118/#120 admin outputs all correct) | #121 | md mobile overflow; base64 paywalled at 0 | B-0184–B-0186 | — | L-004 evidence |
| 64 | Rule 1: diff-checker, url-encoder, html-entity-converter (+ B-0187 site-wide; #121 addendum outputs verified) | #122 | url-encoder paywalled at 0; false Copied toast (L-216) | B-0187 (site-wide), B-0188–B-0190 | — | L-004, L-216 evidence |
| 65 | Rule 1: json-formatter, contrast-checker, add-page-numbers (+ #122 admin outputs verified) | #123 | json paywalled at 0; page-number no inline validation | B-0191–B-0193 | — | L-004 evidence |
| 66 | Rule 1: csv-converter, json-csv-converter, sql-formatter (+ #123 addendum: B-0198 YAML dead button, B-0199 false corrupt toast) | #124 | 2nd 390 px overflow → B-0194 site-wide; CSV unclosed quote silent merge | B-0194 (site-wide), B-0195–B-0199 | — | L-004 evidence |
| 67 | Rule 1: subtitle-adder, rotate-video, text-cleaner (+ #124 admin outputs verified) | #125 | no subtitle success text; counter 2→0 | B-0200–B-0202 | — | L-004, L-143 evidence |
| 68 | Rule 1: text-sorter, video-speed-changer, audio-compressor | #126 | sorter paywalled at 0; no speed result text; compressor promise vs result | B-0203–B-0205 | — | L-004 evidence |
| 69 | Rule 1: text-reverser, audio-to-subtitles, image-splitter + first SEO checks (+ #126 admin outputs) | #127 | audio-to-subtitles drops file at paywall; site-wide SEO template gaps | B-0206–B-0208, B-0209 (site-wide SEO) | — | L-004, L-189 evidence |
| 70 | SEO backfill 1: roman-numeral-converter, audio-comparer, merge-pdf | #128 | roman 0.1% CTR at pos 9; merge meta 83 + pos 35; es audio-comparer English | B-0210–B-0212 | — | L-013, L-045, L-189 notes; L-272, L-273 |
| 71 | Rule 1: thumbnail-gen, convert-image, convert-video (+ SEO) | #129 | size labels wrong (0.0 MB; 1 KB vs 3.8x); convert-image title 64; H1s lack keyword | B-0213–B-0215 | — | L-004, L-189 evidence; L-275–L-277 |
| 72 | SEO backfill 2: compress-pdf, split-pdf, qr-generator | #130 | qr title 65 + meta 84; bare H1s; es split-pdf English | B-0216–B-0218 | — | L-189 note; L-278–L-280 |
| 73 | New tools: pdf-password, unlock-pdf, pdf-to-jpg | #131 | all flows work; metas 76/82/101; es English | B-0219–B-0221 | — | L-281–L-283; L-189, L-004 notes |
| 74 | SEO backfill 3: word-counter, universal-file-converter, sign-pdf | #132 | UFC title 65; Free/Daily Trial in titles; bare H1s; es English | B-0222–B-0224 (v2) | — | L-284–L-286; L-189, L-091 notes |
| 75 | New tools: compare-pdf, extract-pdf, ocr-pdf | #133 | all work; extract text-mode selection carry-over; metas 113/91/123 | B-0225–B-0227 | — | L-287–L-289; L-189, L-004 notes |
| 76 | SEO backfill 4: find-replace, book-writing-toolbox (+book-maker 301), pdf-to-word | #134 | 2 titles 64; meta 79/134 | B-0228–B-0230 | — | L-290–L-292; L-189 note |
| 77 | New tools: excel-to-pdf, html-to-pdf, mail-merge-pdf | #135 | mail-merge blocks loading at 0 trial uses; metas 95/79; book-maker 0 internal links | B-0231–B-0233 | — | L-293–L-295; L-004, L-189, L-291 notes |
| 78 | SEO backfill 5: screenshot-tool, camera-capture, image-to-pdf | #136 | camera title 65; metas 100/131/92; bare H1s | B-0234–B-0236 | — | L-296–L-298; L-189, L-051 notes |
| 79 | New tools: pdf-bookmarks-editor, pdf-to-excel, pdf-to-powerpoint | #137 | bookmarks gate blocks viewing at 0 trial uses; title 65; meta 84 | B-0237–B-0239 | — | L-299–L-301; L-004, L-189 notes |
| 80 | SEO backfill 6: compress-image, magazine-maker, random-number-generator | #138 | compress title % not KB (0.2% CTR); magazine pos 53.6; RNG meta 139 | B-0240–B-0242 | — | L-302–L-304; L-189 note |
| 81 | New tools: powerpoint-to-pdf, government-forms-hub, bates-numbering | #139 | bates gate on drop; forms hub gated + pricing mismatch; pptx meta 97 | B-0243–B-0245 | — | L-305–L-307; L-004, L-189 notes |
| 82 | SEO backfill 7: audio-normalizer, password-generator, resize-crop | #140 | normalizer pos 28.3; password title 62/meta 79; resize meta 137 | B-0246–B-0248 | — | L-099, L-152, L-117, L-189 notes |
| 83 | New tools: document-assembler, exhibit-stamper, caption-generator | #141 | assembler silent no-op; exhibit gate on drop; caption gate + quality | B-0249–B-0251 | — | L-308–L-310; L-004, L-189 notes |
| 84 | SEO backfill 8: case-converter, document-scanner, screen-recorder | #142 | metas 97/97/83; scanner black-page bug P1 | B-0252–B-0254 | — | L-153, L-234, L-236, L-189 notes |
| 85 | New tools: accessibility-checker-powerpoint, accommodation-manager, acx-audiobook-checker | #143 | ACX gate on drop; accommodation title 64/meta 95; pptx checker good | B-0255–B-0257 | — | L-311–L-313; L-004, L-189 notes |
| 86 | SEO backfill 9: color-picker-image, audio-converter, bmi-calculator | #144 | titles 64/64 w/ Free; metas 117/83; bmi 0/504 pos 6.8 | B-0258–B-0260 | — | L-235, L-237, L-131, L-159, L-189 notes |
| 87 | New tools: add-slide-numbers, agenda-builder, agenda-cue-sheet-builder | #145 | agenda-builder no preview + overlap; trial-uses clash; metas 127/93 | B-0261–B-0263 | — | L-314–L-316; L-004, L-189 notes |
| 88 | SEO backfill 10: compress-video, mortgage-calculator, color-converter | #146 | compress 0/733 pos 6.5; mortgage meta 133 no PMI; color meta 78 | B-0264–B-0266 | — | L-106, L-160, L-238, L-189 notes |
| 89 | New tools: arrivals-departures-board, audio-scrambler, avatar-builder | #147 | scrambler pitch-only; arrivals no times; avatar unnamed buttons; titles 63/61 | B-0267–B-0269 | — | L-317–L-319; L-004, L-189 notes |
| 90 | SEO backfill 11: user-agent-parser, stl-ascii-binary-converter, emoji-picker | #148 | metas 98/88/71; titles w/ Free; emoji copy gated | B-0270–B-0272 | — | L-320–L-322; L-239, L-004, L-189 notes |
| 91 | New tools: badge-pass-maker, bank-statement-to-csv, banner-sign-maker | #149 | badge title 64; bank check ✔; banner meta 75, counter mismatch | B-0273–B-0275 | — | L-323–L-325; L-004, L-189 notes |
| 92 | SEO backfill 12: grammar-checker, sprite-sheet-tool, income-tax-calculator | #150 | grammar CTR 0.1%; sprite meta 76; tax CA SDI missing | B-0276–B-0278 | — | L-326–L-328; L-004, L-189, L-086, L-211 notes |
| 93 | New tools: bill-of-sale-generator, binary-ascii-converter, blind-cv-redactor | #151 | bill meta 51; binary 7-bit silent; cv counter mismatch | B-0279–B-0281 | — | L-329–L-331; L-004 note |
| 94 | SEO backfill 13: passport-photo, audio-speed-changer, mesh-3d-converter | #152 | titles w/ Free no brand; metas 139/93/133; /es English | B-0282–B-0284 | — | L-332–L-334; L-004, L-189, L-212–L-214 notes |
| 95 | New tools: book-interior-maker, book-page-estimator, book-spine-calculator | #153 | interior title 65; estimator 374 wpp; spine math ✔ | B-0285–B-0287 | — | L-335–L-337; L-004, L-189 notes |
| 96 | SEO backfill 14: catalog-maker, barcode-generator, ascii-art-generator | #154 | metas 120/151/74; ascii title Free; /es English ×2 | B-0288–B-0290 | — | L-338–L-340; L-004, L-189, L-118, L-215, L-216 notes |
| 97 | New tools: booth-layout-planner, booth-manager, border-radius-generator | #155 | layout-sync finding; false Copied toast; /es English ×3 | B-0291–B-0293 | — | L-341–L-343; L-004, L-189, L-216 notes |
| 98 | SEO backfill 15: paper-format-checker, unit-converter, text-paraphraser | #156 | FAQ contradiction; unit 0% CTR; Light 0 changes; url-shortener skipped (410) | B-0294–B-0296 | — | L-344–L-346; L-004, L-189, L-217, L-172, L-218, L-091 notes |
| 99 | New tools: box-shadow-generator, brand-kit, brochure-flyer-maker | #157 | single shadow; contrast labels/scale; raster PDF, no tri-fold | B-0297–B-0299 | — | L-347–L-349; L-004, L-189 notes |
| 100 | SEO backfill 16: job-experience-calculator, yt-thumbnail, invisible-text-generator | #158 | overlap/labels; snippet + ZIP; zero count | B-0300–B-0302 | — | L-350–L-352; L-004, L-189, L-219, L-220, L-221 notes |
| 101 | New tools: bulk-image, business-card, business-days-calculator | #159 | larger output; trim box/vector; country holidays | B-0303–B-0305 | — | L-353–L-355; L-004, L-189 notes; L-219 correction |
| 102 | SEO backfill 17: audio-trimmer, silence-remover, audio-merger | #160 | snippet + toast; sample rate/padding; durations/crossfade | B-0306–B-0308 | — | L-356–L-358; L-004, L-189, L-216, L-222, L-223, L-224 notes |
| 103 | New tools: calendar-invite-maker, catering-quantity-calculator, certificate-maker | #161 | add links; zero people/kids; layout/logo/fonts | B-0310–B-0312 | — | L-359–L-361; L-004, L-189, L-354 notes |
| 104 | Retest 17:45: roman, random, timezone | #162 | retest | — | B-0114, B-0115, B-0117 verified-fixed | L-012, L-179, L-180, L-182 notes |
| 105 | Retest 17:45: password, magazine, sprite | #163 | retest | — | B-0118, B-0140, B-0143 verified-fixed (outputs blocked) | L-183, L-208, L-211 notes |
| 106 | Retest 17:45: passport, catalog, merge-video | #164 | retest | — | B-0144, B-0147, B-0164 verified-fixed (outputs blocked); notice-box guard unidentified | L-212, L-215, L-230 notes |
| 107 | Retest B-0067: gif, compress-video, sign-pdf | #165 | retest | — | B-0067 2 of 3 verified-fixed; MiB unverified | L-105, L-106, L-113 notes |
| 108 | Retest: compress-image, case-converter, barcode | #166 | retest | — | B-0066, B-0069 verified-fixed; B-0081 blocked | L-115, L-118, L-122, L-153 notes |
| 109 | Retest calculators: mortgage, percentage, loan | #167 | retest | — | B-0086, B-0088 verified-fixed; B-0087 partial; B-0072 still failing | L-129, L-160, L-161, L-162 notes |
| 110 | Retest tip + CLS: tip, /tools, citation | #168 | retest | — | B-0090 partial; B-0072/B-0077 still failing | L-130, L-140, L-149, L-158 notes |
| 111 | Confirm: url-shortener, /developers, openapi + blocked list | #169 | retest | — | B-0061 verified-fixed; B-0097 partial; blocked list | L-091 + blocked notes |
| 112 | Trial-session retest: magazine, catalog, sprite | #170 | retest | — | B-0140, B-0147, B-0143 outputs verified-fixed (Compact no-cover not run) | L-208, L-211, L-215, L-143 notes |
| 113 | Capability sweep (finance first): college-cost, expense-tracker, profit-expense-manager | #171 | NaN on letters; erased on tab close + event wording; income/break-even unverified | B-0313–B-0315 | — | L-362–L-364; L-143, B-0155, B-0187 notes |
| 91 | QA-REPORT-172 | CLS + B-0316 retest, B-0309/B-0099 steps | CLS verified-fixed ×4; B-0316 verified-fixed (Org JSON-LD optional, not seen) | L-129, L-130, L-140, L-149 notes |
| 92 | QA-REPORT-173 | Untested tools 1–3 (Orchestrator list) | all 3 function PASS; meta/title fixes suggested | none (no ledger rows) |
| 93 | QA-REPORT-174 | B-0309 logged-out counter | case 4 PASS (10→9, maxres 1280×720) | L-351 note |
| 94 | QA-REPORT-175 | B-0309 admin session 10:04–10:05 ET | verified-fixed; 4 sweep tools + case 5 open | L-351 note |
| 95 | QA-REPORT-176 | Oct 30 7:45 PM list: B-0119, B-0109, B-0112 | 3 verified-fixed (B-0112 summary minor) | L-184, L-172, L-175 notes |
| 96 | QA-REPORT-177 | Untested tools 4–6 | all function PASS; collage counter 2→0 question; meta fixes | none |
| 97 | QA-REPORT-178 | Oct 30 7:45 PM list: B-0249, B-0253, B-0278 | B-0249, B-0253 verified-fixed; B-0278 SDI fixed, title 64 | L-308, L-234, L-328 notes |
| 98 | QA-REPORT-179 | Untested tools 7–9 | cover-letter, cron PASS; copyright output gated; meta fixes | none |
| 99 | QA-REPORT-180 | Oct 30 7:45 PM list: B-0246, B-0212, B-0216 | all 3 verified-fixed | L-099, L-273, L-278 notes |
| 100 | QA-REPORT-181 | Untested tools 10–12 | all 3 PASS; title/meta fixes | none |
| 101 | QA-REPORT-182 | Oct 30 7:45 PM list: B-0289, B-0295, B-0210-v2 | B-0289, B-0295 verified-fixed; B-0210-v2 H2 part failing | L-339, L-345, L-013 notes |
| 102 | QA-REPORT-183 | Untested tools 13–15 | all pass; email-signature example phone left in the field; SEO fixes | none |
| 103 | QA-REPORT-184 | Oct 30 7:45 PM list: B-0306, B-0307, B-0308 | B-0307, B-0308 verified-fixed; B-0306 MP3 bitrate failing | L-356, L-357, L-358 notes |
| 104 | QA-REPORT-185 | B-0233 + untested tools 16–17 | B-0233 verified-fixed; closure report PASS; schedule partial | L-295 note |
| 105 | QA-REPORT-186 | Oct 30 7:45 PM list: B-0310, B-0311, B-0312 | B-0311, B-0312 verified-fixed; B-0310 next-day note failing | L-359, L-360, L-361 notes |
| 106 | QA-REPORT-187 | B-0286, B-0255 + untested tool 18 | B-0255 verified-fixed; B-0286 failing; profit ledger PASS | L-336, L-311 notes |
| 107 | QA-REPORT-188 | B-0267, B-0228, B-0199 | B-0267, B-0228 verified-fixed; B-0199 password PDF failing | L-317, L-290, L-258 notes |
| 108 | QA-REPORT-189 | B-0252, B-0293 + untested tool 19 | B-0252 verified-fixed; B-0293 % note failing; booth tracker PASS | L-153, L-343 notes |
| 109 | QA-REPORT-190 | untested tool 20 + B-0302, B-0296 | exif PASS; B-0302, B-0296 verified-fixed | L-352, L-346 notes |
| 110 | QA-REPORT-191 | B-0260, B-0264, B-0215 | titles/sizes verified-fixed; 2 H1s still failing | L-131, L-159, L-106, L-277 notes |
| 111 | QA-REPORT-192 | B-0223-v2 | verified-fixed | L-285 note |
| 112 | QA-REPORT-193 | untested tools 21–23 + consistency | 3 PASS; extract-charts counter mismatch note; 3 SEO notes | no ledger rows (new tools) |
| 113 | QA-REPORT-194 | untested tools 24–26 + consistency | 3 PASS; 3 meta notes | no ledger rows (new tools) |
| 114 | QA-REPORT-195 | untested tools 27–29 + consistency | 3 PASS; focus timer blog name mismatch; SEO notes | no ledger rows (new tools) |
| 115 | QA-REPORT-196 | untested tools 30–32 + consistency + site tool count | gpa, guest list PASS; giveaway draw gated (counter mismatch) | no ledger rows (new tools) |
| 116 | QA-REPORT-197 | untested tools 33–35 (no-trial) + consistency | hashtag, http PASS; guest-manager claims; SEO notes | no ledger rows |
| 117 | QA-REPORT-198 | untested tools 36–38 (no-trial) + consistency | ideal weight PASS; 2 NEEDS-ADMIN; SEO notes | no ledger rows |
| 118 | QA-REPORT-199 | untested tools 39–41 (no-trial) + consistency | kdp PASS; label, lease claims; lease meta 46 | no ledger rows |
| 119 | QA-REPORT-200 | untested tools 42–44 (no-trial) + consistency | legal desk price consistent; lorem gated; SEO notes | no ledger rows |
| 120 | QA-REPORT-201 | untested tools 45–47 (no-trial) + consistency | meta-tag PASS; markdown word count note | no ledger rows |
| 121 | QA-REPORT-202 | untested tools 48–50 (no-trial) + consistency | morse, moving PASS; mute gated | no ledger rows |
| 122 | QA-REPORT-203 | admin session 11.23–11.28 AM: NEEDS-ADMIN 1–8 | 8 PASS; L-317 export verified-fixed | L-317 note |
| 123 | QA-REPORT-204 | untested tools 51–53 (no-trial) + consistency | number-to-words PASS; NDA meta 50 | no ledger rows |
| 124 | QA-REPORT-205 | untested tools 54–56 (no-trial) + consistency | claims match; og meta 37 | no ledger rows |
| 125 | QA-REPORT-206 | tools 57–59 | 2 failing, 1 PASS | ad glue on ppt; pay-stub meta 68 |
| 126 | QA-REPORT-207 | tools 60–62 | 2 failing, 1 PASS | paycheck title 62; period title Free |
| 127 | QA-REPORT-208 | admin NA 9–15 | 6 PASS, 1 partial fail | B-0199 verified-fixed; lease NY content generic |
| 128 | QA-REPORT-209 | tools 63–65 | 3 failing | POA meta 44; ppt-to-gif ad glue |
| 129 | QA-REPORT-210 | tools 66–68 | 3 failing | titles over 60 with Free; ad glue x2 |
| 130 | QA-REPORT-211 | tools 69–71 | 3 failing | pregnancy metas short; studio title 63 |
| 131 | QA-REPORT-212 | tools 72–74 | 2 failing, 1 PASS | promissory title 63; metas short |
| 132 | QA-REPORT-213 | tools 75–77 | 2 failing, 1 PASS | reading-level title 63 Free |
| 133 | QA-REPORT-214 | tools 78–80 | 3 failing | ad glue receipt, recipe; titles over 60 |
| 134 | QA-REPORT-215 | tools 81–83 | 3 failing | regex title 63 Free; rental meta 51 |
| 135 | QA-REPORT-216 | tools 84–86 | 3 failing | Free in titles; resume meta 43 |
| 136 | QA-REPORT-217 | tools 87–89 | 3 failing | reverse-video 5 GB note; metas short |
| 137 | QA-REPORT-218 | admin NA 16–28 | 11 PASS, 2 FAIL | markdown-editor word count claimed fixed but still failing; noise-remover hum unchanged (possible P1) |
| 138 | QA-REPORT-219 | tools 90–92 | 2 failing, 1 PASS | metas short; seller-studio PASS |
| 139 | QA-REPORT-220 | tools 93–95 | 2 failing, 1 PASS | SIP title Free; metas short |
| 140 | QA-REPORT-221 | tools 96–98 | 3 failing | split title Free; subnet title 65 |
| 141 | QA-REPORT-222 | tools 99–101 | 2 failing, 1 PASS | template ad glue; TTS meta 89 |
| 142 | QA-REPORT-223 | tools 102–104 | 1 failing, 2 PASS | timestamp title 64; converters orphaned |
| 143 | QA-REPORT-224 | tools 105–107 | 2 failing, 1 PASS | converter metas short; values correct |
| 144 | QA-REPORT-225 | tools 108–110 | 1 failing, 2 PASS | gallons meta 129; values correct |
| 145 | QA-REPORT-226 | tools 111–113 | 2 failing, 1 PASS | kmh title 62; km meta 128 |
| 146 | QA-REPORT-227 | tools 114–116 | 1 failing, 2 PASS | liters meta 129; singular unit wording |
| 147 | QA-REPORT-228 | admin NA 29–44 | 12 PASS, 4 FAIL | packing-slip qty/logo; period window +1 day (P1?); scan NT window; giveaway repeat adds ticket (P1?) |
| 148 | QA-REPORT-229 | tools 117–119 | 2 failing, 1 PASS | mph-kmh title 62; values correct |
| 149 | QA-REPORT-230 | tools 120–122 | 2 failing, 1 PASS | url-extractor works; metas short |
| 150 | QA-REPORT-231 | tools 123–125 | 3 failing | metas short; manager title 63 |
| 151 | QA-REPORT-232 | tools 126–127 | 2 failing | water rounding 10.6 vs 2.7 L; titles Free |
| 152 | QA-REPORT-233 | tools 128–129 | 2 failing | ad glue webp, word-to-ppt; queue done |
| 153 | QA-REPORT-234 | categories PDF, PPT, Image | 3 failing | "free" counts include premium tools; PPT meta 187 |
| 154 | QA-REPORT-235 | categories Video, Audio, Text | 3 failing | metas short; audio normalizer name mismatch |
| 155 | QA-REPORT-236 | categories Converters, Tax, Finance | 3 failing | converter pages unlinked; metas short |
| 156 | QA-REPORT-237 | categories Health, QR, Business + 234-236 timing addendum | 3 failing | metas short; timing corrected |
| 157 | QA-REPORT-238 | categories Design, Security, SEO | 3 failing | metas short; duplicate password names |
| 158 | QA-REPORT-239 | categories File, 3D, E-commerce | 3 failing | file meta claims audio; free count incl. paid |
| 159 | QA-REPORT-240 | categories Travel, Event, Animation + 237-239 timing addendum | 3 failing | metas short; Animation name oversells |
| 160 | QA-REPORT-241 | categories Household, College, Relocation | 3 failing | metas short; titles thin |
| 161 | QA-REPORT-242 | category Marketing & Print | 1 failing | title thin only |
| 162 | QA-REPORT-243 | solutions Marketing, Content Writer, Web Designer | 3 failing | metas short; dangling "day pass below"; toolbox price unmatched |
| 163 | QA-REPORT-244 | solutions Legal, Real Estate, HR | 3 failing | metas short; HR I-9 claim overstates |
| 164 | QA-REPORT-245 | solutions Freelancer, Small Business, Personal Finance | 2 failing, 1 pass | metas short; small-business consistent |
| 165 | QA-REPORT-246 | solutions Developer, Student, Event Planner + 243 wording addendum | 3 failing | dangling day pass; overlapping event cards |
| 166 | QA-REPORT-247 | solutions Traveler, Authors, Online Sellers | 3 failing | metas short; dangling day pass |
| 167 | QA-REPORT-248 | solutions Paralegals, Bookkeepers | 2 failing | dangling day pass; titles thin |
| 168 | QA-REPORT-249 | bundles Podcast, Audio Extract, Video Edit + 246 length addendum | 3 failing | metas short; podcast hum claim vs #218 |
| 169 | QA-REPORT-250 | bundles Print-Ready, Secure Send, Scan to PDF | 3 failing | metas short only |
| 170 | QA-REPORT-251 | bundles Job Application, Freelance Close-Out | 2 failing | metas short; NEEDS-ADMIN one-use run |
| 171 | QA-REPORT-252 | admin NA 45–76 (11.55 AM–12.10 PM ET) | 22 pass, 7 fail/partial, 1 inconclusive, 1 not checkable, 1 not run | relayed tally 26/5/1/1 does not add to 32; noise-remover fail confirmed |

- 12.15 PM ET: reports 253-255 (batches 172-174), blog pass posts 1-9 of the alphabetical list.

- 12.20 PM ET: report 256 (batch-175), admin rows 71 and 77-82; NEEDS-ADMIN 85-86 added.

- 12.21 PM ET: reports 257-259 (batches 176-178), blog pass posts 10-18.

- 12.23 PM ET: reports 260-262 (batches 179-181), admin rows 83-85, site-wide $ fault scan, blog posts 19-27; trial-counter addendum 1.

- 12.25 PM ET: reports 263-265 (batches 182-184), addendum to 260, row 85 table FAIL (possible P1), blog posts 28-36.

- Reports 266-268 (batches 185-187), time addendum for 263-265, blog posts 37-45 (fetch 12.24 PM ET).

- 12.26 PM ET: B-0324 filed (print royalty table, P1), ledger L-365 added; next free B-number checked across ledger, tracker, claude-briefs and the blog repo (highest real B-0323).

- Reports 269-271 (batches 188-190), blog posts 46-54 (fetch 12.26 PM ET).

- Reports 272-274 (batches 191-193), addendum to 269, blog posts 55-63 (fetch 12.28 PM ET).

- Reports 275-277 (batches 194-196), blog posts 64-72 (fetch 12.29 PM ET).

- Reports 278-280 (batches 197-199), blog posts 73-81 (fetch 12.30 PM ET).

- Reports 281-283 (batches 200-202), blog posts 82-90 (fetch 12.31 PM ET).

- Reports 284-286 (batches 203-205), blog posts 91-99 (fetch 12.32-12.33 PM ET).

- Reports 287-289 (batches 206-208), blog posts 100-108 (fetch 12.34 PM ET).

- Reports 290-292 (batches 209-211), blog posts 109-117 (fetch 12.35 PM ET).

- Reports 293-295 (batches 212-214), blog posts 118-126 + Premium nav check (fetch 12.36-12.37 PM ET).

- Reports 296-298 (batches 215-217), blog posts 127-135 (fetch 12.38 PM ET).

- Reports 299-301 (batches 218-220), blog posts 136-144 (fetch 12.39 PM ET).

- Reports 302-304 (batches 221-223), blog posts 145-153 (fetch 12.40 PM ET).
- Batch 224: YouTube ID audit of reports 253-301 (84 IDs, 0 wrong). Reports 305-306 (batches 225-226), posts 154-159.
- Reports 307-309 (batches 227-229), posts 160-168.
- Reports 310-312 (batches 230-232), posts 169-177.
- Reports 313-315 (batches 233-235), posts 178-186.
- Reports 316-318 (batches 236-238), posts 187-195.
- Reports 319-321 (batches 239-241), posts 196-204.
- Reports 322-324 (batches 242-244), posts 205-213.
- Reports 325-327 (batches 245-247), posts 214-222.
- Reports 328-330 (batches 248-250), posts 223-231.
- Reports 331-333 (batches 251-253), posts 232-240; lorem-ipsum addendum; noise-remover post vs P1 measurement.
- Reports 334-336 (batches 254-256), posts 241-249; G1 total 22.
- Reports 337-339 (batches 257-259), posts 250-258; roman 4000 claim conflicts with measured run.
- Reports 340-342 (batches 260-262), posts 259-267; G1 total 24; state-tax CA/NY recheck.
- Reports 343-345 (batches 263-265), posts 268-276; G1 total 25.
- Reports 346-348 (batches 266-268), posts 277-285; list continues (31 pages); G1 total 25.
- Reports 349-351 (batches 269-271), posts 286-294; NEEDS-ADMIN addendum 13 rows 85-86 (state-tax, yt-thumbnail); G1 total 26.
- Reports 352-354 (batches 272-274), posts 295-303; G1 total 26; prices match /pricing.
- Reports 355-357 (batches 275-277), posts 304-312; G1 27; G3 12 (image-to-pdf); audio-comparer overclaim vs L-022.
- NEEDS-ADMIN addendum 14 row 87 (batch 278); reports 358-359 (batches 279-280), posts 313-318; G1 27; G3 15.
- Reports 360-362 (batches 281-283), posts 319-327; G1 27; G3 15; 5 more G10 duplicates.
- Reports 363-365 (batches 284-286), posts 328-336; 'no cap' wording matches /pricing; G1 28 (freelancers); G3 15.
- Addendum (364 meta; row 87: 17 KDP trims + Custom, 2 posts say 15; EPUB/margin blocked by admin download 0 left) and reports 366-367 (batches 287-288), posts 337-342; G1 30; G3 15.
- Reports 368-370 (batches 289-291), posts 343-351; G1 36 (+6); G3 15; 24 posts left.
- Reports 371-373 (batches 292-294), posts 352-360; G1 38 (+2); G3 15; 5 posts left.
- Reports 374-375 (batches 295-296): last 5 posts; list ended (page 32 404). Final G1 57 posts (full-text scan), G3 15, G10 listed; template fix given.
- Reports 376-377 (batches 297-298): claimed-fixed retest, signed-out HTML; L-013/L-277/L-328 still failing; L-359 partial; L-006 unchanged; L-065 superseded; dispatch list in 377.
- Reports 378-380 (batches 299-301), 4:26 PM ET: L-013/277/328 unchanged; Book Toolbox now $29.99/mo subscription on site (no packs), 4 blog posts claim $3.99 pass; counts 215+/211+ and 100+ Premium apps off-rule; G1 template, PDF-Word sign-in, 15 trims unchanged.
- 2026-10-31 07:08 PM ET: L-176 $3.99 blog copy recheck after 4d9ba808: 4/4 posts pass ($29.99/mo, 7-day trial; no $3.99 or packs). Pricing-request curl items: #4 counts 300+/250+/200+ on / /pricing /about /de /ja /es; #6 college cost default 6.52% pass.
- 2026-11-01 12:16 AM ET: 383-v2 retracts the Premium-count FAIL (/premium-apps lists 104 apps, 100+ correct; do not change to 5). Report 384 (batch 302): capability gap for marketplace-fee, sales-tax, state-tax (CAP-384-1..3, unnumbered per throttle); L-366..L-368 added; evidence on L-190/191/193; L-013/277/328 unchanged.
- 2026-11-01 01:15 AM ET: QA-REPORT-388 (batch-303) untested batch A gpa/401k/final-grade; rows L-369..L-372 added, L-013 evidence; Expense Tracker private-window FAIL (minor) carried.
- 2026-11-01 03:50 AM ET: QA-REPORT-391 (batch-304) f7f3943c/31a8ecc7 retest: checkout BLOCKED (non-admin login), sales tax PASS, state tax PASS, Etsy math match + assumptions-line FAIL (minor); rows L-176/L-366/L-367/L-368 updated.
