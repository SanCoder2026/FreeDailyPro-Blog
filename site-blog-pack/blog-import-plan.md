# Blog import plan: what from the Grok repo can go on freedailypro.com

Generated 2026-10-15 from github.com/SanCoder2026/FreeDailyPro-Blog (192 markdown posts read).

## Summary

| Bucket | Posts |
|---|---|
| Already on the site (same slug or same text) | 35 |
| Single-tool posts (new or replacing the site's thin version) | 55 (15 replace an existing post) |
| REWRITE (new angle): persona / theme posts, one per topic | 22 |
| Not used (duplicates across platforms, covered, brand/AI themed) | 40 |

Every listed post must be rewritten for the site by Grok using `2-REWRITE-BLOG-RULES.md`. Even the "ADD" ones need work: almost all of them use "free" many times, many mention AI, and 36 posts link to pages that do not exist.

Key problems found in the source posts:

- Wording: "free" appears 1 to 58 times per post; the week-sep05, sep12 and oct06 to oct13 Blogger packs mention AI (the "AI-policy proof" theme).
- Broken links: /category/developer-tools, /category/calculators, /category/finance-tools, /category/business-documents and tool ids that do not exist (qr-code-generator, gif-maker, video-trimmer, video-compressor, heic-to-jpg, signature-pdf, base64-encoder). /tool/book-maker redirects to the Book Writing Toolbox.
- The same theme was written up to four times (Blogger, HubSpot, Medium, WordPress). Only one version of each is used here.
- Invented first-person stories in the Medium posts ("The night I replaced my invoice spreadsheet"). The rewrite rules forbid these.
- The owner will delete the external blogs after the site is done, so overlap with them does not matter; overlap between site posts does.

## A. Posts to add (in suggested publish order)

"Site already has" lists an existing site post about the same tool; the new post must take a clearly different scenario and title.

Mode REPLACE = the site already has a post with this exact slug about this tool: Grok writes the better version under the same file name and it replaces the old one (keeps its URL and original date). NEW = a new URL.

Columns: id, publish date, mode, target slug (file name), topic, primary tool, other tools, source file in the Grok repo, source words, "free" count, AI mention, links to fix.

| Id | Date | Mode | Target slug | Topic | Primary tool | Other tools / persona | Source (Agent/...) | Words | "free" | AI | Fix links | Site already has |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R001 | keep | REPLACE | resume-builder | business-tools | resume-builder | word-counter, grammar-checker | site/7day-external/blogger/posts/day6-resume-builder.md | 1003 | 8 |  |  | resume-builder |
| R002 | keep | REPLACE | random-number-generator | converters | random-number-generator | password-generator, hash-generator | site/7day-external/blogger/posts/day1-random-number-generator.md | 979 | 9 |  | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) | random-number-generator |
| R003 | keep | REPLACE | image-to-pdf | pdf-tools | image-to-pdf | compress-pdf, merge-pdf | site/7day-external/blogger/posts/day2-image-to-pdf.md | 1027 | 4 |  |  | image-to-pdf |
| R004 | keep | REPLACE | document-scanner | image-tools | document-scanner | image-to-pdf, compress-pdf | site/7day-external/blogger/posts/day3-document-scanner.md | 996 | 5 |  |  | document-scanner |
| R005 | keep | REPLACE | remove-background | image-tools | remove-background | screenshot-tool, image-to-pdf | site/7day-external/blogger/posts/day4-remove-background.md | 989 | 6 |  |  | remove-background |
| R006 | keep | REPLACE | screenshot-tool | image-tools | screenshot-tool | image-to-pdf | site/7day-external/blogger/posts/day5-screenshot-tool.md | 979 | 4 |  |  | screenshot-tool |
| R007 | keep | REPLACE | binary-ascii-converter | security-tools | binary-ascii-converter | hash-generator, json-formatter | site/7day-external/blogger/posts/day7-binary-ascii-converter.md | 975 | 6 |  | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) | binary-ascii-converter |
| R008 | keep | REPLACE | shipping-cost-estimator | ecommerce-tools | shipping-cost-estimator | unit-converter, percentage-calculator | site/7day-external/hubspot/posts/day1-shipping-cost-estimator.md | 1033 | 11 |  | /category/calculators -> /category/finance-calculators / health-calculators / converters / tax-calculators | shipping-cost-estimator |
| R009 | keep | REPLACE | cost-of-living-comparison | relocation-tools | cost-of-living-comparison | percentage-calculator, unit-converter | site/7day-external/hubspot/posts/day2-cost-of-living-comparison.md | 1031 | 4 |  | /category/calculators -> /category/finance-calculators / health-calculators / converters / tax-calculators | cost-of-living-comparison |
| R010 | keep | REPLACE | text-similarity-checker | college-tools | text-similarity-checker | word-counter, diff-checker | site/7day-external/hubspot/posts/day3-text-similarity-checker.md | 997 | 5 |  |  | text-similarity-checker |
| R011 | keep | REPLACE | diff-checker | security-tools | diff-checker | text-similarity-checker, json-formatter | site/7day-external/hubspot/posts/day4-diff-checker.md | 987 | 6 |  | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) | diff-checker |
| R012 | keep | REPLACE | audio-comparer | audio-tools | audio-comparer | word-counter, hash-generator | site/7day-external/hubspot/posts/day5-audio-comparer.md | 973 | 5 |  |  | audio-comparer |
| R013 | keep | REPLACE | college-529-calculator | college-tools | college-529-calculator | percentage-calculator, loan-calculator | site/7day-external/hubspot/posts/day6-college-529-calculator.md | 977 | 4 |  | /category/calculators -> /category/finance-calculators / health-calculators / converters / tax-calculators | college-529-calculator |
| R014 | keep | REPLACE | csv-converter | file-tools | csv-converter | json-formatter | site/7day-external/medium/posts/day6-csv-converter.md | 1040 | 4 |  | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) | csv-converter |
| R015 | keep | REPLACE | markdown-html-converter | text-tools | markdown-html-converter | word-counter, diff-checker | site/7day-external/medium/posts/day7-markdown-html-converter.md | 1016 | 4 |  |  | markdown-html-converter |
| B001 | 2026-10-16 | NEW tool | rotate-pdf-fix-sideways-scans | pdf-tools | rotate-pdf | document-scanner, compress-pdf, image-to-pdf | blogger/week-oct07/posts/2026-10-06-rotate-pdf-fix-sideways-scans.md | 1177 | 4 |  |  |  |
| B002 | 2026-10-17 | NEW tool | slug-generator-clean-blog-urls | text-tools | slug-generator | case-converter, word-counter, markdown-html-converter | blogger/week-oct06/posts/2026-10-07-slug-generator-clean-blog-urls.md | 1136 | 20 | yes |  |  |
| B003 | 2026-10-18 | NEW tool | receipt-maker-cash-sales-pdf | business-tools | receipt-maker | expense-tracker, merge-pdf, compress-pdf | blogger/week-oct06/posts/2026-10-08-receipt-maker-cash-sales-pdf.md | 1134 | 22 | yes |  |  |
| B004 | 2026-10-19 | NEW tool | yt-thumbnail-downloader-creators | file-tools | yt-thumbnail | compress-image, remove-background, screenshot-tool | blogger/week-oct06/posts/2026-10-09-yt-thumbnail-downloader-creators.md | 1125 | 20 | yes |  |  |
| B005 | 2026-10-20 | NEW tool | mesh-3d-viewer-check-before-print | 3d-tools | mesh-3d-viewer | mesh-3d-converter, compress-image, universal-file-converter | blogger/week-oct06/posts/2026-10-11-mesh-3d-viewer-check-before-print.md | 1124 | 20 | yes |  |  |
| B006 | 2026-10-21 | NEW tool | rmd-calculator-required-minimum-distribution | finance-calculators | rmd-calculator | loan-calculator, college-529-calculator, cost-of-living-comparison | blogger/week-oct06/posts/2026-10-12-rmd-calculator-required-minimum-distribution.md | 1135 | 23 | yes | /category/finance-tools -> /category/finance-calculators / health-calculators / converters / tax-calculators |  |
| B007 | 2026-10-22 | NEW tool | profit-margin-calculator-product-pricing | ecommerce-tools | profit-margin-calculator | marketplace-fee-calculator, break-even-calculator, shipping-cost-estimator | blogger/week-oct13/posts/2026-10-15-profit-margin-calculator-product-pricing.md | 1079 | 12 | yes |  |  |
| B008 | 2026-10-23 | NEW tool | citation-generator-apa-mla-papers | college-tools | citation-generator | word-counter, grammar-checker, reading-level-checker | blogger/week-oct13/posts/2026-10-16-citation-generator-apa-mla-papers.md | 1062 | 13 | yes |  |  |
| B009 | 2026-10-24 | NEW tool | hashtag-generator-social-campaigns | seo-tools | hashtag-generator | word-counter, slug-generator, keyword-density | blogger/week-oct13/posts/2026-10-17-hashtag-generator-social-campaigns.md | 1040 | 13 | yes |  |  |
| B010 | 2026-10-25 | NEW tool | travel-packing-list-trip-ready | travel-tools | travel-packing-list | travel-budget-planner, travel-itinerary-planner, travel-countdown-planner | blogger/week-oct13/posts/2026-10-18-travel-packing-list-trip-ready.md | 1054 | 11 |  |  |  |
| B011 | 2026-10-26 | NEW tool | heic-to-jpg-iphone-work-files | image-tools | convert-image | compress-image | blogger/week-sep05/posts/2026-09-06-heic-to-jpg-iphone-work-files.md | 1029 | 50 | yes | /tool/heic-to-jpg -> /tool/convert-image |  |
| B012 | 2026-10-27 | NEW tool | json-formatter | security-tools | json-formatter | url-encoder, hash-generator | site/7day-external/medium/posts/day3-json-formatter.md | 983 | 4 |  | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) |  |
| B013 | 2026-10-28 | NEW tool | percentage-calculator | converters | percentage-calculator | unit-converter, invoice-generator | site/7day-external/wordpress/posts/day4-percentage-calculator.md | 1047 | 2 |  | /category/calculators -> /category/finance-calculators / health-calculators / converters / tax-calculators |  |
| B014 | 2026-10-29 | NEW tool | gif-maker-social-loops | video-tools | video-to-gif | compress-image | wordpress/week-sep12/posts/2026-09-14-gif-maker-social-loops.md | 1036 | 56 | yes | /tool/gif-maker -> /tool/video-to-gif |  |
| B015 | 2026-10-30 | NEW tool | favicon-generator-websites | design-tools | favicon-generator |  | wordpress/week-sep12/posts/2026-09-15-favicon-generator-websites.md | 1011 | 51 | yes |  |  |
| B016 | 2026-10-31 | NEW theme | teachers-tutors-worksheet-packs | guides | word-to-pdf | merge-pdf, compress-pdf | week-aug23/blogger/posts/2026-08-23-teachers-free-toolkit.md | 1094 | 59 | yes |  |  |
| B017 | 2026-11-01 | NEW theme | event-planner-run-of-show-and-signage-packs | event-tools | merge-pdf | qr-generator, persona:event-planner | medium/unique-from-blogger/posts/05-event-planner-run-of-show-signage.md | 1088 | 43 | yes |  |  |
| B018 | 2026-11-02 | NEW theme | local-business-qr-codes-that-get-scanned | qr-tools | qr-generator | persona:small-business | blogger/week-aug29/posts/2026-08-31-free-qr-codes-local-business.md | 932 | 54 | yes | /tool/qr-code-generator -> /tool/qr-generator |  |
| B019 | 2026-11-03 | NEW tool | fillable-forms-complete-pdf-fields | pdf-tools | fillable-forms | rotate-pdf, pdf-password, document-scanner | blogger/week-oct07/posts/2026-10-09-fillable-forms-complete-pdf-fields.md | 1077 | 1 |  |  |  |
| B020 | 2026-11-04 | NEW tool | ascii-art-generator-readme-banners | text-tools | ascii-art-generator | slug-generator, markdown-html-converter, binary-ascii-converter | blogger/week-oct06/posts/2026-10-10-ascii-art-generator-readme-banners.md | 1134 | 20 | yes | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) |  |
| B021 | 2026-11-05 | NEW tool | nda-generator-freelancer-protection | business-tools | nda-generator | promissory-note-generator, invoice-generator, receipt-maker | blogger/week-oct13/posts/2026-10-19-nda-generator-freelancer-protection.md | 1034 | 15 | yes |  |  |
| B022 | 2026-11-06 | NEW tool | loan-calculator | finance-calculators | loan-calculator | percentage-calculator, college-529-calculator | site/7day-external/hubspot/posts/day7-loan-calculator.md | 971 | 6 |  | /category/calculators -> /category/finance-calculators / health-calculators / converters / tax-calculators |  |
| B023 | 2026-11-07 | NEW theme | etsy-handmade-seller-product-photo-packs | ecommerce-tools | compress-image | remove-background, persona:small-business | medium/unique-from-blogger/posts/01-etsy-handmade-product-photo-packs.md | 1175 | 43 | yes |  | is-it-safe-to-compress-images-online |
| B024 | 2026-11-08 | NEW theme | students-and-remote-workers-who-cannot-install-software | college-tools | - | persona:student | wordpress/posts/2026-08-22-free-tools-for-students-and-remote-work.md | 891 | 31 | yes |  |  |
| B025 | 2026-11-09 | NEW theme | photographers-client-gallery-image-prep | image-tools | compress-image | resize-image, convert-image | week-aug23/blogger/posts/2026-08-25-photographers-free-image-prep.md | 1135 | 49 | yes |  | is-it-safe-to-compress-images-online |
| B026 | 2026-11-10 | NEW tool | url-encoder | security-tools | url-encoder | json-formatter, hash-generator | site/7day-external/medium/posts/day5-url-encoder.md | 1053 | 5 |  | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) |  |
| B027 | 2026-11-11 | NEW tool | unit-converter | converters | unit-converter | shipping-cost-estimator, percentage-calculator | site/7day-external/wordpress/posts/day5-unit-converter.md | 972 | 1 |  | /category/calculators -> /category/finance-calculators / health-calculators / converters / tax-calculators |  |
| B028 | 2026-11-12 | NEW theme | video-trim-and-compress-for-creators | video-tools | trim-video | compress-video | blogger/week-aug29/posts/2026-08-29-free-video-trim-compress-creators.md | 1030 | 59 | yes | /tool/video-trimmer -> /tool/trim-video; /tool/video-compressor -> /tool/compress-video |  |
| B029 | 2026-11-13 | NEW theme | solopreneur-mini-brand-kit-colors-and-logo | design-tools | color-converter | compress-image, persona:small-business | week-aug23/wordpress/posts/2026-08-28-brand-color-logo-free-tools.md | 1062 | 57 | yes |  |  |
| B030 | 2026-11-14 | NEW theme | nonprofit-fundraising-flyer-and-thank-you-packs | guides | compress-image | merge-pdf, word-to-pdf, persona:small-business | week-aug23/blogger/posts/2026-08-24-nonprofit-fundraising-free-tools.md | 1060 | 52 |  |  | is-it-safe-to-compress-images-online |
| B031 | 2026-11-15 | NEW tool | split-pdf-client-contract-packets | pdf-tools | split-pdf | merge-pdf, rotate-pdf, compress-pdf | blogger/week-oct13/posts/2026-10-13-split-pdf-client-contract-packets.md | 1162 | 16 | yes |  |  |
| B032 | 2026-11-16 | NEW tool | password-generator | text-tools | password-generator | hash-generator, url-encoder | site/7day-external/wordpress/posts/day1-password-generator.md | 1179 | 3 |  | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) |  |
| B033 | 2026-11-17 | NEW tool | expense-tracker-receipt-packs | business-tools | expense-tracker | merge-pdf, compress-pdf | blogger/week-sep05/posts/2026-09-10-expense-tracker-receipt-packs.md | 996 | 56 | yes |  |  |
| B034 | 2026-11-18 | NEW tool | loan-mortgage-calculators-orientation | finance-calculators | mortgage-calculator | loan-calculator | wordpress/week-sep12/posts/2026-09-16-loan-mortgage-calculators-orientation.md | 1009 | 56 | yes |  |  |
| B035 | 2026-11-19 | NEW tool | hash-generator | security-tools | hash-generator | password-generator, json-formatter | site/7day-external/wordpress/posts/day7-hash-generator.md | 987 | 1 |  | /category/developer-tools -> /category/security-tools or text-tools (use the category the tool is in) |  |
| B036 | 2026-11-20 | NEW theme | restaurant-cafe-menu-pdf-updates | design-tools | word-to-pdf | qr-generator, persona:small-business | medium/unique-from-blogger/posts/03-restaurant-cafe-menu-pdf-workflow.md | 1086 | 41 | yes |  |  |
| B037 | 2026-11-21 | NEW theme | digital-nomad-cafe-wifi-document-toolkit | guides | compress-pdf | pdf-password, persona:traveler | medium/unique-from-blogger/posts/07-digital-nomad-cafe-document-toolkit.md | 1090 | 40 | yes |  |  |
| B038 | 2026-11-22 | NEW tool | redact-pdf-remove-sensitive-data | pdf-tools | redact-pdf | split-pdf, merge-pdf, compress-pdf | blogger/week-oct13/posts/2026-10-14-redact-pdf-remove-sensitive-data.md | 1119 | 14 | yes |  |  |
| B039 | 2026-11-23 | NEW tool | word-counter | text-tools | word-counter | grammar-checker, text-similarity-checker | site/7day-external/wordpress/posts/day3-word-counter.md | 1113 | 2 |  |  |  |
| B040 | 2026-11-24 | NEW tool | business-card-maker-print | business-tools | business-card | merge-pdf, compress-pdf | blogger/week-sep05/posts/2026-09-11-business-card-maker-free-print.md | 1005 | 58 | yes |  |  |
| B041 | 2026-11-25 | NEW theme | freelancer-first-year-tax-surprise | finance-calculators | - | persona:freelancer | medium/refresh-old/posts/02-freelancer-tax-surprise-year-one.md | 1068 | 45 |  |  |  |
| B042 | 2026-11-26 | NEW theme | everyday-privacy-utilities-passwords-hashes-checksums | security-tools | password-generator | hash-generator | week-aug23/blogger/posts/2026-08-29-privacy-security-free-utilities.md | 1018 | 62 |  |  |  |
| B043 | 2026-11-27 | NEW theme | look-professional-without-canva-or-adobe | design-tools | - | persona:small-business | medium/refresh-old/posts/06-professional-without-canva-adobe.md | 1030 | 48 |  |  |  |
| B044 | 2026-11-28 | NEW theme | replace-five-desktop-apps-with-browser-tools | guides | merge-pdf | compress-image | medium/refresh-old/posts/04-browser-replaced-five-apps.md | 1003 | 38 |  |  |  |
| B045 | 2026-11-29 | NEW tool | add-pdf-password-client-packs | pdf-tools | pdf-password | word-to-pdf, merge-pdf, compress-pdf | blogger/week-sep05/posts/2026-09-05-add-pdf-password-client-packs.md | 1161 | 46 | yes |  |  |
| B046 | 2026-11-30 | NEW tool | grammar-checker | text-tools | grammar-checker | word-counter, text-similarity-checker | site/7day-external/wordpress/posts/day6-grammar-checker.md | 965 | 4 | yes |  |  |
| B047 | 2026-12-01 | NEW tool | invoice-generator | business-tools | invoice-generator | percentage-calculator, word-counter | site/7day-external/medium/posts/day2-invoice-generator.md | 984 | 3 |  | /category/calculators -> /category/finance-calculators / health-calculators / converters / tax-calculators |  |
| B048 | 2026-12-02 | NEW theme | fire-retirement-planning-with-browser-calculators | finance-calculators | fire-calculator | persona:personal-finance | blogger/week-aug29/posts/2026-09-03-free-fire-retirement-calculators.md | 856 | 54 | yes |  |  |
| B049 | 2026-12-03 | NEW tool | pdf-watermark-protect-drafts | pdf-tools | pdf-watermark | word-to-pdf, merge-pdf, compress-pdf | blogger/week-sep05/posts/2026-09-07-pdf-watermark-protect-drafts.md | 994 | 46 | yes |  |  |
| B050 | 2026-12-04 | NEW tool | bill-of-sale-generator | business-tools | bill-of-sale-generator | merge-pdf, compress-pdf | wordpress/week-sep12/posts/2026-09-13-bill-of-sale-generator.md | 1066 | 53 | yes | /tool/signature-pdf -> /tool/sign-pdf |  |
| B051 | 2026-12-05 | NEW tool | excel-to-pdf-finance-packs | pdf-tools | excel-to-pdf | merge-pdf, compress-pdf, pdf-password | blogger/week-sep05/posts/2026-09-08-excel-to-pdf-finance-packs.md | 1037 | 54 | yes |  |  |
| B052 | 2026-12-06 | NEW theme | invoice-and-proposal-pdf-packet-for-clients | business-tools | invoice-generator | word-to-pdf, merge-pdf, persona:freelancer | week-aug23/blogger/posts/2026-08-26-invoice-proposal-pdf-workflow.md | 1111 | 42 | yes |  |  |
| B053 | 2026-12-07 | NEW tool | ocr-pdf-searchable-scans | pdf-tools | ocr-pdf | merge-pdf, compress-pdf, pdf-password | blogger/week-sep05/posts/2026-09-09-ocr-pdf-searchable-scans.md | 996 | 50 | yes |  |  |
| B054 | 2026-12-08 | NEW theme | podcast-guest-one-sheets-and-show-notes | business-tools | word-counter | word-to-pdf, persona:content-writer | medium/unique-from-blogger/posts/04-podcast-guest-onesheet-shownotes.md | 1085 | 41 | yes |  |  |
| B055 | 2026-12-09 | NEW tool | merge-pdf | pdf-tools | merge-pdf | compress-pdf, pdf-to-word | site/7day-external/medium/posts/day1-merge-pdf.md | 1018 | 3 |  |  |  |
| B056 | 2026-12-10 | NEW theme | coaches-client-worksheet-packs | business-tools | word-to-pdf | fillable-forms, persona:freelancer | medium/unique-from-blogger/posts/06-coaches-client-worksheet-packs.md | 1090 | 41 | yes |  |  |
| B057 | 2026-12-11 | NEW tool | pdf-to-word | pdf-tools | pdf-to-word | compress-pdf, merge-pdf | site/7day-external/medium/posts/day4-pdf-to-word.md | 1048 | 5 |  |  | convert-pdf-to-word-without-losing-formatting |
| B058 | 2026-12-12 | NEW theme | when-a-legal-template-is-enough | business-tools | - | persona:legal | medium/refresh-old/posts/03-free-legal-template-when-enough.md | 1117 | 55 |  |  |  |
| B059 | 2026-12-13 | NEW tool | compress-pdf | pdf-tools | compress-pdf | merge-pdf, pdf-to-word | site/7day-external/wordpress/posts/day2-compress-pdf.md | 1270 | 3 |  |  |  |
| B060 | 2026-12-14 | NEW tool | extract-pdf-page-numbers | pdf-tools | extract-pdf | add-page-numbers, merge-pdf, compress-pdf | wordpress/week-sep12/posts/2026-09-17-extract-pdf-page-numbers.md | 1004 | 52 | yes |  |  |
| B061 | 2026-12-15 | NEW theme | parents-school-paperwork-pdf-packs | pdf-tools | merge-pdf | compress-image, image-to-pdf | week-aug23/blogger/posts/2026-08-27-parents-school-paperwork-tools.md | 1075 | 48 | yes |  |  |
| B062 | 2026-12-16 | NEW theme | real-estate-listing-and-open-house-packs | pdf-tools | merge-pdf | compress-image, qr-generator, persona:real-estate | medium/unique-from-blogger/posts/02-real-estate-listing-open-house-packs.md | 1110 | 39 | yes |  |  |

"Date" is a suggestion at 1 post per day starting 2026-10-16; change freely. Batches of 7 = ids B001-B007, B008-B014, and so on. R-rows are replacements: they keep the existing URL and original date and can be done any time (suggest the first batch).

### Notes on specific posts

- B016 teachers-tutors-worksheet-packs: 4 platform variants exist; write ONE new post
- B018 local-business-qr-codes-that-get-scanned: fix broken tool id
- B024 students-and-remote-workers-who-cannot-install-software: avoid AI-policy wording
- B025 photographers-client-gallery-image-prep: check resize-image/convert-image ids
- B028 video-trim-and-compress-for-creators: fix broken tool ids
- B029 solopreneur-mini-brand-kit-colors-and-logo: verify tool ids
- B036 restaurant-cafe-menu-pdf-updates: site already has a menu/invitation print-design post; use a different scenario (weekly menu changes)
- B041 freelancer-first-year-tax-surprise: site has self-employed-tax-retirement-calculators; keep only if the first-year angle stays distinct. Tax figures need year + official source
- B042 everyday-privacy-utilities-passwords-hashes-checksums: must differ from the password-generator and hash-generator single-tool posts
- B044 replace-five-desktop-apps-with-browser-tools: remove invented first-person story
- B048 fire-retirement-planning-with-browser-calculators: site has retirement-calculators-explained; keep FIRE-specific
- B052 invoice-and-proposal-pdf-packet-for-clients: distinct from the invoice-generator single-tool post
- B058 when-a-legal-template-is-enough: site has free-legal-document-templates-guide; use the decision-checklist angle. Not legal advice

### Alternate sources (other platform versions of the same topic; read only for facts, do not copy)

- R001 resume-builder: blogger/week-aug29/posts/2026-09-01-free-private-resume-builder.md; hubspot/posts/2026-08-22-free-private-resume-builder.md
- R011 diff-checker: wordpress/week-sep12/posts/2026-09-18-diff-checker-case-converter.md
- B001 rotate-pdf-fix-sideways-scans: blogger/week-oct06/posts/2026-10-06-rotate-pdf-fix-sideways-scans.md; site/7day-external/blogger-week2/posts/2026-10-06-rotate-pdf-fix-sideways-scans.md
- B002 slug-generator-clean-blog-urls: blogger/week-oct07/posts/2026-10-08-slug-generator-clean-blog-urls.md; site/7day-external/blogger-week2/posts/2026-10-08-slug-generator-clean-blog-urls.md
- B003 receipt-maker-cash-sales-pdf: blogger/week-oct07/posts/2026-10-07-receipt-maker-cash-sales-pdf.md; site/7day-external/blogger-week2/posts/2026-10-07-receipt-maker-cash-sales-pdf.md
- B004 yt-thumbnail-downloader-creators: blogger/week-oct07/posts/2026-10-10-yt-thumbnail-downloader-for-creators.md; site/7day-external/blogger-week2/posts/2026-10-10-yt-thumbnail-downloader-for-creators.md
- B005 mesh-3d-viewer-check-before-print: blogger/week-oct07/posts/2026-10-11-mesh-3d-viewer-check-before-print.md; site/7day-external/blogger-week2/posts/2026-10-11-mesh-3d-viewer-check-before-print.md
- B006 rmd-calculator-required-minimum-distribution: blogger/week-oct07/posts/2026-10-12-rmd-calculator-planning-estimate.md; site/7day-external/blogger-week2/posts/2026-10-12-rmd-calculator-planning-estimate.md
- B016 teachers-tutors-worksheet-packs: week-aug23/hubspot/posts/2026-08-23-teachers-free-toolkit.md; week-aug23/medium/posts/2026-08-23-teachers-free-toolkit.md; week-aug23/wordpress/posts/2026-08-23-teachers-free-toolkit.md
- B018 local-business-qr-codes-that-get-scanned: hubspot/posts/2026-08-17-free-qr-codes-for-marketing-campaigns.md
- B019 fillable-forms-complete-pdf-fields: wordpress/week-sep12/posts/2026-09-12-fillable-forms-signature-pdf.md; site/7day-external/blogger-week2/posts/2026-10-09-fillable-forms-complete-pdf-fields.md
- B025 photographers-client-gallery-image-prep: week-aug23/hubspot/posts/2026-08-25-photographers-free-image-prep.md; week-aug23/medium/posts/2026-08-25-photographers-free-image-prep.md; week-aug23/wordpress/posts/2026-08-25-photographers-free-image-prep.md
- B028 video-trim-and-compress-for-creators: hubspot/posts/2026-08-18-free-browser-video-trim-compress.md
- B029 solopreneur-mini-brand-kit-colors-and-logo: week-aug23/blogger/posts/2026-08-28-brand-color-logo-free-tools.md; week-aug23/hubspot/posts/2026-08-28-brand-color-logo-free-tools.md; week-aug23/medium/posts/2026-08-28-brand-color-logo-free-tools.md
- B030 nonprofit-fundraising-flyer-and-thank-you-packs: week-aug23/hubspot/posts/2026-08-24-nonprofit-fundraising-free-tools.md; week-aug23/medium/posts/2026-08-24-nonprofit-fundraising-free-tools.md; week-aug23/wordpress/posts/2026-08-24-nonprofit-fundraising-free-tools.md
- B042 everyday-privacy-utilities-passwords-hashes-checksums: week-aug23/hubspot/posts/2026-08-29-privacy-security-free-utilities.md; week-aug23/medium/posts/2026-08-29-privacy-security-free-utilities.md; week-aug23/wordpress/posts/2026-08-29-privacy-security-free-utilities.md
- B052 invoice-and-proposal-pdf-packet-for-clients: week-aug23/hubspot/posts/2026-08-26-invoice-proposal-pdf-workflow.md; week-aug23/medium/posts/2026-08-26-invoice-proposal-pdf-workflow.md; week-aug23/wordpress/posts/2026-08-26-invoice-proposal-pdf-workflow.md
- B061 parents-school-paperwork-pdf-packs: week-aug23/hubspot/posts/2026-08-27-parents-school-paperwork-tools.md; week-aug23/medium/posts/2026-08-27-parents-school-paperwork-tools.md; week-aug23/wordpress/posts/2026-08-27-parents-school-paperwork-tools.md

## B. Not used

| Source (Agent/...) | Words | Why |
|---|---|---|
| blogger/posts/pre-aug8-upgrade/company-blocking-ai-stay-productive.md | 917 | AI-themed; site has the 'company blocks AI tools' post already |
| medium/refresh-old/posts/08-ai-productivity-myth-browser-tools.md | 1000 | AI-themed; site has the 'company blocks AI tools' post already |
| site/week-sep05/posts/api-automation-example.md | 1129 | Already on the site (api-automation-example) |
| site/week-sep02/posts/2026-09-02-api-mcp-server-side-tools.md | 1128 | Already on the site (api-mcp-server-side-tools) |
| site/week-sep05/posts/audio-comparer.md | 1041 | Already on the site (audio-comparer) |
| site/week-sep05/posts/binary-ascii-converter.md | 1143 | Already on the site (binary-ascii-converter) |
| site/book-writing-toolbox/posts/book-writing-toolbox-overview-blank-page-to-submission.md | 1231 | Already on the site (book-writing-toolbox-overview-blank-page-to-submission) |
| site/book-writing-toolbox/posts/book-writing-toolbox-vs-vellum-atticus-reedsy.md | 1375 | Already on the site (book-writing-toolbox-vs-vellum-atticus-reedsy) |
| site/week-sep02/posts/2026-09-11-bulk-image-batch-processing.md | 1039 | Already on the site (bulk-image-batch-processing) |
| site/week-sep02/posts/2026-09-05-catalog-maker-product-sheets.md | 1169 | Already on the site (catalog-maker-product-sheets) |
| site/week-sep05/posts/college-529-calculator.md | 1069 | Already on the site (college-529-calculator) |
| site/week-sep02/posts/2026-09-06-compare-pdf-document-differences.md | 1064 | Already on the site (compare-pdf-document-differences) |
| site/week-sep02/posts/2026-09-07-compound-interest-sip-calculators.md | 1109 | Already on the site (compound-interest-sip-calculators) |
| site/week-sep02/posts/2026-09-08-contract-templates-free-drafts.md | 1062 | Already on the site (contract-templates-free-drafts) |
| site/week-sep05/posts/corporate-safe-tools.md | 1032 | Already on the site (corporate-safe-tools) |
| site/week-sep05/posts/cost-of-living-comparison.md | 1139 | Already on the site (cost-of-living-comparison) |
| site/week-sep05/posts/csv-converter.md | 1158 | Already on the site (csv-converter) |
| site/week-sep05/posts/diff-checker.md | 1167 | Already on the site (diff-checker) |
| site/week-sep05/posts/document-scanner.md | 1027 | Already on the site (document-scanner) |
| site/book-writing-toolbox/posts/ebook-only-publishing-with-book-writing-toolbox.md | 981 | Already on the site (ebook-only-publishing-with-book-writing-toolbox) |
| site/week-sep05/posts/image-to-pdf.md | 1175 | Already on the site (image-to-pdf) |
| site/week-sep02/posts/2026-09-03-jwt-decoder-debug-tokens.md | 1164 | Already on the site (jwt-decoder-debug-tokens) |
| site/week-sep05/posts/markdown-html-converter.md | 1140 | Already on the site (markdown-html-converter) |
| site/week-sep05/posts/merge-video.md | 1114 | Already on the site (merge-video) |
| site/week-sep05/posts/mesh-3d-converter.md | 1168 | Already on the site (mesh-3d-converter) |
| site/week-sep02/posts/2026-09-04-noise-remover-audio-cleanup.md | 1071 | Already on the site (noise-remover-audio-cleanup) |
| site/book-writing-toolbox/posts/publishing-platform-picker-kdp-ingramspark-bn-lulu.md | 1006 | Already on the site (publishing-platform-picker-kdp-ingramspark-bn-lulu) |
| site/week-sep05/posts/random-number-generator.md | 1145 | Already on the site (random-number-generator) |
| site/week-sep02/posts/2026-09-09-redact-organize-pdf-sensitive.md | 1034 | Already on the site (redact-organize-pdf-sensitive) |
| site/week-sep05/posts/remove-background.md | 1023 | Already on the site (remove-background) |
| site/week-sep05/posts/resume-builder.md | 1181 | Already on the site (resume-builder) |
| site/week-sep02/posts/2026-09-10-screen-recorder-async-demos.md | 1018 | Already on the site (screen-recorder-async-demos) |
| site/week-sep05/posts/screenshot-tool.md | 1156 | Already on the site (screenshot-tool) |
| site/week-sep05/posts/shipping-cost-estimator.md | 1164 | Already on the site (shipping-cost-estimator) |
| site/book-writing-toolbox/posts/shunn-manuscript-onix-preflight-check.md | 969 | Already on the site (shunn-manuscript-onix-preflight-check) |
| site/week-sep05/posts/text-similarity-checker.md | 1025 | Already on the site (text-similarity-checker) |
| site/week-sep05/posts/universal-file-converter.md | 1081 | Already on the site (universal-file-converter) |
| blogger/week-aug29/posts/2026-08-30-free-audio-podcast-voice-tools.md | 961 | Covered by existing audio tools post (see audio-trimmer single-tool idea) |
| hubspot/posts/2026-08-19-free-audio-podcast-voice-cleanup.md | 557 | Covered by existing audio tools post (see audio-trimmer single-tool idea) |
| hubspot/posts/2026-08-23-free-ecommerce-product-listing-toolkit.md | 614 | Covered by existing ecommerce sellers post |
| hubspot/posts/2026-08-21-free-menu-invitation-print-design.md | 679 | Covered by existing menu/invitation design post |
| blogger/posts/2026-08-17-free-image-tools-no-upload-needed.md | 1132 | Covered by existing site post on compressing images safely |
| blogger/posts/pre-aug8-upgrade/compress-resize-clean-images-free.md | 912 | Covered by existing site post on compressing images safely |
| posts/2026-08-14-free-image-tools-privacy-first.md | 587 | Covered by existing site post on compressing images safely |
| wordpress/posts/2026-08-20-free-private-image-tools.md | 1034 | Covered by existing site post on compressing images safely |
| blogger/posts/2026-08-15-why-browser-tools-beat-cloud-uploads.md | 1137 | Covered by existing site post on files staying on the device |
| medium/refresh-old/posts/07-privacy-free-tools-no-upload.md | 1046 | Covered by existing site post on files staying on the device |
| wordpress/posts/2026-08-16-privacy-first-free-browser-tools.md | 1028 | Covered by existing site post on files staying on the device |
| blogger/week-aug29/posts/2026-09-02-free-private-health-calculators.md | 864 | Covered by guide-to-free-health-calculators |
| wordpress/posts/existing-improved/understanding-health-calculators.md | 1103 | Covered by guide-to-free-health-calculators |
| blogger/week-aug29/posts/2026-09-04-free-developer-browser-toolkit.md | 879 | Covered by the existing developer toolkit post |
| hubspot/posts/2026-08-20-free-developer-browser-tools.md | 729 | Covered by the existing developer toolkit post |
| medium/refresh-old/posts/05-developer-free-toolkit.md | 1072 | Covered by the existing developer toolkit post |
| wordpress/posts/existing-improved/thinking-of-moving-dont-guess-cost.md | 1062 | Covered by the existing relocation tools post |
| blogger/posts/2026-08-16-complete-free-pdf-workflow-guide.md | 1099 | Covered by the existing site PDF toolkit/convert posts |
| posts/2026-08-14-free-pdf-toolkit-everyday-workflow.md | 614 | Covered by the existing site PDF toolkit/convert posts |
| wordpress/posts/existing-improved/free-browser-tools-merge-compress-convert-pdfs.md | 1103 | Covered by the existing site PDF toolkit/convert posts |
| blogger/posts/2026-08-18-freelancer-productivity-free-toolkit.md | 1077 | Covered by the existing site post for freelancers |
| medium/refresh-old/posts/01-freelancer-free-tools-2026.md | 1127 | Covered by the existing site post for freelancers |
| posts/2026-08-14-free-tools-for-freelancers-and-solopreneurs.md | 651 | Covered by the existing site post for freelancers |
| wordpress/posts/2026-08-17-free-tools-every-freelancer-needs.md | 1062 | Covered by the existing site post for freelancers |
| blogger/posts/2026-08-21-free-tools-stack-for-small-business.md | 1079 | Covered by the existing site post for small business owners |
| blogger/posts/2026-08-20-build-your-own-favorites-tools-page.md | 1019 | Covered by the existing site post on Favorites |
| posts/2026-08-14-favorites-your-own-tools-page.md | 665 | Covered by the existing site post on Favorites |
| wordpress/posts/2026-08-19-build-your-favorites-tools-page.md | 1055 | Covered by the existing site post on Favorites |
| blogger/posts/2026-08-19-use-freedailypro-in-your-language.md | 1054 | Covered by the existing site post on language support |
| posts/2026-08-14-language-support-multiple-languages.md | 637 | Covered by the existing site post on language support |
| wordpress/posts/2026-08-18-use-freedailypro-in-your-language.md | 1081 | Covered by the existing site post on language support |
| wordpress/posts/2026-08-21-free-tax-finance-calculators-guide.md | 958 | Covered by the existing tax-calculator posts |
| blogger/posts/pre-aug8-upgrade/how-we-made-tools-signup-free.md | 1004 | Founder/brand story, not a task guide. Better as an About page |
| blogger/posts/pre-aug8-upgrade/simple-free-document-workflow.md | 888 | Founder/brand story, not a task guide. Better as an About page |
| blogger/posts/pre-aug8-upgrade/why-i-built-free-productivity-toolbox.md | 846 | Founder/brand story, not a task guide. Better as an About page |
| wordpress/posts/existing-improved/welcome-why-i-built-freedailypro.md | 1131 | Founder/brand story, not a task guide. Better as an About page |
| posts/2026-08-10-free-book-maker-tool-create-book-draft-easily.md | 631 | Old Book Maker launch copy; Book Writing Toolbox posts replace it |
| posts/blogger-test-book-maker.md | 578 | Old Book Maker launch copy; Book Writing Toolbox posts replace it |
