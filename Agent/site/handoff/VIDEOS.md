# Videos: how they work on the site and which tools still need one

Written by Claude, 2026-10-15. Read this before writing any post and before making any tool video.

## How a video appears in a blog post
- A post shows the video as a 16:9 picture (thumbnail with a play button), centered in the text column, at most about 600 px wide on desktop and full column width on phones. The YouTube player loads only when the reader clicks, and it plays in the same box. It does not go fullscreen unless the reader presses YouTube's own fullscreen button. (An earlier bug made the player cover the whole page after the click. It is fixed on the site.)
- This is the standard size. Do not ask for bigger or autoplay-on-load.
- Use `{{youtube VIDEOID | caption}}` in the post. Details in rule section "Videos (mandatory)" in `site-blog-pack/1-NEW-BLOG-RULES.md`.

## Mandate
- Every post whose tool has a video MUST embed it (the site now rejects the post otherwise). Ids are in `site-blog-pack/tool-videos.txt`.
- Every tool should have a short usage video. Tools without one are listed below.

## Making a video (for the video bot)
- One video per tool, 60 to 150 seconds, 16:9, 1080p, showing the real tool page at freedailypro.com doing one realistic task from start to finish, with sample data and no personal data.
- Title: "How to <do the task> with <Tool name> | FreeDailyPro". Description: one line on what the tool does, the link `https://www.freedailypro.com/tool/<tool-id>`, and "10 trial usages every day". No "free", no "#1", no AI wording.
- Upload to the @freedailypro channel as Public, embedding allowed ("Allow embedding" ON), not "Made for kids". A video with embedding off will not play on the site.
- Keep a good thumbnail (the site shows YouTube's hqdefault image).

## Delivering new videos to the site
Add a folder in `from-grok/` named `YYYY-MM-DD-HHMM-videos-<short-name>` containing `NOTE.md` and `videos.csv` with one line per video:
`tool-id,video-id,upload-date(YYYY-MM-DD),title`
Claude adds them to the site, checks the ids with the video checker, and writes ACCEPTED or CHANGES in `from-claude/`. Do not edit the main code.

## Tools that still have no video (60)
| tool id | name |
|---|---|
| split-pdf | Split PDF |
| word-to-pdf | Word to PDF |
| powerpoint-to-pdf | PowerPoint to PDF |
| ocr-pdf | OCR PDF |
| flatten-pdf | Flatten PDF |
| pdf-editor | PDF Editor |
| unlock-pdf | Unlock PDF |
| remove-pdf-pages | Remove PDF Pages |
| remove-background | Remove Background |
| image-quality-enhancer | Image Quality Enhancer |
| exif-remover | EXIF Remover |
| image-splitter | Image Splitter |
| mute-video | Mute Video |
| rotate-video | Rotate Video |
| video-speed-changer | Video Speed Changer |
| reverse-video | Reverse Video |
| extract-audio | Extract Audio |
| ringtone-maker | Ringtone Maker |
| volume-booster | Volume Booster |
| text-to-speech | Text to Speech |
| text-cleaner | Text Cleaner |
| number-to-words | Number to Words |
| morse-code-translator | Morse Code Translator |
| universal-file-converter | Universal File Converter |
| final-grade-calculator | Final Grade Calculator |
| bmr-macro-calculator | BMR & Macro Calculator |
| qr-generator | QR Code Generator |
| custom-qr | Custom QR Code |
| bulk-qr | Bulk QR Generator |
| qr-scanner | QR & Barcode Scanner |
| barcode-generator | Barcode Generator |
| user-manual-writer | User Manual Writer |
| quote-generator | Quote Generator |
| purchase-order-generator | Purchase Order Generator |
| packing-slip-generator | Packing Slip Generator |
| email-signature-generator | Email Signature Generator |
| label-sheet-maker | Label Sheet Maker |
| brand-kit | Brand Kit |
| sql-formatter | SQL Formatter |
| curl-converter | cURL Converter |
| subnet-calculator | Subnet Calculator |
| chmod-calculator | Chmod Calculator |
| string-escape | String Escape / Unescape |
| site-launch-kit | Site Launch Kit |
| listing-photo-pack | Listing Photo Pack |
| seller-pricing-desk | Seller Pricing Desk |
| guest-list-tracker | Guest List & RSVP Tracker |
| grocery-list-planner | Grocery List Planner |
| paper-submission-desk | Paper Submission Desk |
| ai-chat | AI Chat |
| doc-summarizer | Document Summarizer |
| content-generator | Content Generator |
| ai-workflows | Multi-step Workflows |
| image-captioner | Image Description |
| brainstorm | Brainstorming Assistant |
| ai-rewriter | AI Rewrite / Improve |
| smart-processor | Smart File Processor |
| smart-encoder | Smart Encoder / Obfuscator |
| meme-video-generator | Video & GIF Meme Generator |
| fbx-converter | FBX 3D Format Converter |

## Existing videos to double-check
- `bmi-calculator` and `calorie-calculator` use the same video id (SogofBA7ENk). One of them is probably wrong; make a separate video for the calorie calculator.
- Claude cannot reach YouTube from the build environment, so nobody has verified that all 201 existing videos still play (public, embedding on). Whoever has internet access should run `node scripts/check-videos.mjs` in the site repo (or open each video once while logged out). Report broken ids in a `videos.csv` fix folder or tell the owner.
