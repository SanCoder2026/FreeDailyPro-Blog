# New post request: the full blog wishlist (81 rows)
Date and time: 2026-11-10 12:47
Type: REQUEST (new posts). Owner instruction: submit ALL wishlist items so Grok builds them.
Put your answers in normal NEW folders in `handoff/from-grok/` (one folder per batch, `YYYY-MM-DD-HHMM-short-name`, with `NOTE.md`, `posts/`, `images/`), as described in `../../GROK-HANDOFF.md`. Claude publishes; Grok does not touch the site.

## Files in this folder
- `README.md` this brief: rules and the priority-ordered list.
- `wishlist.tsv` and `wishlist.json`: the same 81 rows, machine-readable. Columns: rank, id (the wishlist row number), section, item, tier, existing_post, suggested_title, title_len, slug_suggestion, target_keyword, intent, priority, status, why, effort, raw_title_keyword_cell, keyword_contains_free.
- `wishlist-source-2026-11-09.md`: the original wishlist with its basis notes (built from site commit b8e5fcf3 and the 367 posts then in content/blog).

## Read first
`site-blog-pack/1-NEW-BLOG-RULES.md` (every rule applies), `site-blog-pack/tool-ids.txt` (valid tool and workflow ids; unknown ids are rejected), `site-blog-pack/tool-videos.txt` and `Agent/site/handoff/VIDEOS.md` (embed the primary tool's video when one exists), `Agent/site/handoff/from-grok/HERO-IMAGE-RULE.md`.

## Standing rules for every post in this list
1. **No "free" in the title, subtitle or visible body text.** Say "no-cost", "browser-based", "no install", "professional". A search keyword that contains "free" (row 24: "free bill of sale") goes only in `description` (once) and `tags`, never in visible text. New slugs must not contain "free". The brand name FreeDailyPro is fine. Existing slugs that contain "free" stay as they are; never rename an existing slug.
2. **Trial wording by tier.**
   - Professional tools: the daily allowance is "10 trial usages" per day. Never "free uses", "free tries" or "free tier". After the trial: $1 daily pass or $4.99 a month, only when relevant.
   - Premium Applications: every Premium post must state **2 trial usages**.
   - Workflow Products: monthly plan with a 7-day trial; Book Writing Toolbox previews are watermarked. Titles never say "free".
   - Say "200+ professional tools"; give no other count.
3. **AI Studio is on HOLD.** AI_STUDIO_PUBLIC is off. Rows 79, 80, 81 (10 AI Studio tools) are marked `HOLD_AI_STUDIO`: do not draft them, do not mention AI Studio or any AI Studio tool anywhere in any post. Also no "AI", ChatGPT or AI-powered wording in other posts (the validator rejects it). Row 45 (Image Upscaler and Image Quality Enhancer) is a public Professional tool and is NOT on hold; describe it without calling it AI.
4. **Hero image**: follow `HERO-IMAGE-RULE.md` in `handoff/from-grok/`. 1200x630 WebP under 150 kB, named `<slug>.webp`, one unique image per post, topic-specific photoreal scene with a person doing the real task and the tool UI or props visible, bottom FreeDailyPro.com sticker only (applied with `Agent/scripts/brand_image.py`: F. icon, "FreeDailyPro.com" with only the first F in teal, teal hairline), no logo inside the scene, `imageAlt` describes what is visible.
5. **Front matter**: copy the format of the existing posts exactly (see `site-blog-pack/1-NEW-BLOG-RULES.md` section 3 and any post in `handoff/from-grok/2026-10-17-1830-event-apps-posts/posts/`):
   ```yaml
   ---
   title: "..."            # 70 characters or fewer, no "free"
   subtitle: "..."         # 150 characters or fewer, different from description
   description: "..."      # 70 to 150 characters
   date: 2026-11-10        # go-live day; no scheduling per NEW-RULE-no-scheduling.md
   author: "FreeDailyPro Team"
   topic: <one category id>
   tools: [primary-first, ...]   # 1 to 4 real ids, all linked in the body
   personas: [...]
   workflows: []
   tags: ["...", ...]      # 5 to 15, comma + space; "free" keywords allowed here only
   image: "../images/<slug>.webp"
   imageAlt: "..."
   draft: false
   ---
   ```
   Body layout, 1000+ words, 3+ internal links, 3+ `##` sections, numbered steps, common-mistakes section, closing question linking to /contact: as in section 4 of the rules. Embed the YouTube video with `{{youtube VIDEOID | caption}}` when the primary tool has one.
6. **Write against the real tool.** Open the tool page and the tool code in the registry; describe only what exists. Use worked numbers from real runs. No invented statistics. No offline claims. Do not state that files are never uploaded unless that tool is fully client-side.
7. **Duplicates**: before writing, check `blog-coverage.md`. Where a row says an existing post covers the topic, follow its `status` below instead of adding a post. Slugs must be new (or exactly an existing slug when replacing).
8. **Hub rule** (row 52): no prices or counts in the lede.
9. **API rows 64 to 78**: each post carries one runnable curl, one Postman "Try it" link, one MCP line; say "API key" and "trial limit" (not "free"); do not claim stored data (nothing is stored); rates are daily reference rates, not live.
10. Cross-post to dev.to for rows 64 to 78 is a later step handled by the bots; publish on freedailypro.com first.

## Tier coverage at the time of the wishlist (registry 394 entries)
| Tier | Registry | With a dedicated post | Without |
|---|---|---|---|
| Professional | 281 | 193 | 88 |
| Premium Applications | 92 | 65 | 27 |
| Workflow Products | 11 | 2 (Event Suite, Book Writing Toolbox) | 9 |
| AI Studio | 10 | 0 | 10, all HOLD (AI Studio is not public) |

## Status meanings (column `status`)
- `BUILD`: write the post(s) as listed. 72 rows.
- `BUILD_IF_TIME`: row 51, small tools, one post each only if time allows.
- `VERIFY_FIRST`: row 14. Check whether the existing post names the Cover Letter Maker Premium app. If it does, send a note instead of a post; if not, write the new post.
- `NO_NEW_POST_VERIFY_ONLY`: row 29. Check that the existing post names the app; no new post.
- `DUPLICATE_REVIEW_NO_NEW_POST`: row 31. Two posts overlap; write a short duplicate-review note for Claude (which to keep), do not add a third post.
- `DONE_NO_POST`: row 55. Already covered; listed only so the list is complete.
- `HOLD_UNTIL_LISTINGS_LIVE`: row 78. Do not write until Claude confirms the RapidAPI listings are live.
- `HOLD_AI_STUDIO`: rows 79 to 81. Do not write, do not mention.

So all 81 rows are submitted: 74 are to be written (72 BUILD, plus row 14 verify-first and row 51 if time allows) and 7 are held, verify-only or done (rows 29, 31, 55, 78, 79, 80, 81). Several rows cover more than one post (row 36 five tools, 76 two posts, 77 six posts); propose one slug each in your NOTE.md.

## Suggested order
1. Rows 1 to 8 (the 7 new Workflow desks plus the Seller Studio overview), 2. rows 64 to 68 (the 1.5.x release story: Validation API, Text to Speech API, MCP, Postman, Payroll API), 3. Premium flagships 9 to 13, 4. PowerPoint cluster 36 to 38, 5. the rest of the High rows, then Med, then Low. The `rank` column below and in the TSV/JSON already follows this order.

Send posts in batches of about 5 to 10 by this order, each in its own from-grok folder with a `NOTE.md`. If a title in the table is over 70 characters or a slug is over 90, shorten it. Where the table says "Grok proposes", choose a title and slug yourself within the rules above.

## The list (81 rows, priority order)
| Rank | Wishlist # | Item | Tier | Priority | Status | Title (suggested) | Slug (suggested) | Target keyword | Effort |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | File Conversion Studio | Workflow | High | BUILD | Convert Any File Without Switching Tools | convert-any-file-without-switching-tools | file converter online | L |
| 2 | 2 | Brand Studio | Workflow | High | BUILD | Logo, Colours and Print Files From One Brand Kit | logo-colours-and-print-files-from-one-brand-kit | brand kit maker | L |
| 3 | 3 | Landlord Desk | Workflow | High | BUILD | Lease, Application and Notice for a Rental Unit | lease-application-and-notice-for-a-rental-unit | landlord forms online | M |
| 4 | 4 | Document Operations Desk | Workflow | High | BUILD | Stamp, Number and Hand Off a Document Batch | stamp-number-and-hand-off-a-document-batch | document workflow tools | M |
| 5 | 5 | Print and Publication Studio | Workflow | High | BUILD | From Manuscript Files to a Print-Ready Catalog or Book | from-manuscript-files-to-a-print-ready-catalog-or-book | print publication workflow | L |
| 6 | 6 | Freelancer Desk | Workflow | High | BUILD | Quote, Invoice and Mileage for a Solo Client Job | quote-invoice-and-mileage-for-a-solo-client-job | freelancer invoicing tools | M |
| 7 | 7 | HR Desk | Workflow | High | BUILD | Offer Letter, Handbook and Onboarding Pack for a New Hire | offer-letter-handbook-and-onboarding-pack-for-a-new-hire | HR documents small business | M |
| 8 | 8 | Seller Studio | Workflow | High | BUILD | Seller Studio: Listing Photos, Prices and Text in One Pass | seller-studio-listing-photos-prices-and-text-in-one-pass | etsy seller tools | M |
| 9 | 64 | Validation API (IBAN, BIC, routing, GTIN, VIN, email, phone, GSTIN, PAN) | API-MCP | High | BUILD | Validate IBAN, VIN and GTIN With One API Call | validate-iban-vin-and-gtin-with-one-api-call | validation api | M |
| 10 | 65 | Text to Speech API and MCP (v1.5.1) | API-MCP | High | BUILD | Text to Speech API: Weighted Calls and Trial Limits Explained | text-to-speech-api-weighted-calls-and-trial-limits-explained | text to speech api | M |
| 11 | 66 | MCP server for Claude Desktop and Cursor (239 tools) | API-MCP | High | BUILD | Connect the FreeDailyPro MCP Server to Claude Desktop | connect-the-freedailypro-mcp-server-to-claude-desktop | mcp server setup | M |
| 12 | 67 | Try the API in Postman | API-MCP | High | BUILD | Call the FreeDailyPro API From Postman in Two Minutes | call-the-freedailypro-api-from-postman-in-two-minutes | postman api collection | S |
| 13 | 68 | Payroll and Paycheck Calculator API | API-MCP | High | BUILD | Paycheck Calculator API With 2026 Tax Tables | paycheck-calculator-api-with-2026-tax-tables | paycheck calculator api | M |
| 14 | 9 | Universal File Converter | Premium | High | BUILD | Convert Between Document, Image and Media Formats in One App | convert-between-document-image-and-media-formats-in-one-app | universal file converter | M |
| 15 | 10 | PDF Editor | Premium | High | BUILD | Edit Text, Whiteout and Add Shapes in a PDF in the Browser | edit-text-whiteout-and-add-shapes-in-a-pdf-in-the-browser | edit pdf online | M |
| 16 | 11 | Create Fillable PDF | Premium | High | BUILD | Turn a Flat PDF Into a Fillable Form With Checkboxes and Dropdowns | turn-a-flat-pdf-into-a-fillable-form-with-checkboxes-and-dropdowns | make pdf fillable | M |
| 17 | 12 | Slide Deck Maker | Premium | High | BUILD | Build a Clean Slide Deck From an Outline | build-a-clean-slide-deck-from-an-outline | make a presentation online | M |
| 18 | 13 | Presentation Studio | Premium | High | BUILD | Finish a Deck for Sending: Fonts, Size and Notes | finish-a-deck-for-sending-fonts-size-and-notes | finish powerpoint for sharing | M |
| 19 | 36 | PowerPoint to PDF / Images / HTML / Video / GIF (5 tools) | Professional | High | BUILD | Export a PowerPoint as Images, HTML or Video | export-a-powerpoint-as-images-html-or-video | powerpoint to video | M |
| 20 | 37 | PDF to PowerPoint and Word/Excel/Markdown to PowerPoint | Professional | High | BUILD | Turn a PDF or Word File Into Slides | turn-a-pdf-or-word-file-into-slides | pdf to powerpoint | M |
| 21 | 38 | Compress, Merge, Split PowerPoint | Professional | High | BUILD | Shrink a 90 MB Deck for Email | shrink-a-90-mb-deck-for-email | compress powerpoint | M |
| 22 | 15 | Business Plan Builder | Premium | High | BUILD | A One-Page Business Plan You Can Hand to a Bank | a-one-page-business-plan-you-can-hand-to-a-bank | business plan template | L |
| 23 | 16 | Video Studio | Premium | High | BUILD | Trim, Caption and Export a Video in One Place | trim-caption-and-export-a-video-in-one-place | online video editor | L |
| 24 | 17 | Employee Handbook Builder | Premium | High | BUILD | Write an Employee Handbook for a Small Team | write-an-employee-handbook-for-a-small-team | employee handbook template | M |
| 25 | 18 | Book Cover Maker | Premium | High | BUILD | Design a Paperback Cover With the Right Spine Width | design-a-paperback-cover-with-the-right-spine-width | book cover maker | M |
| 26 | 19 | EPUB Maker | Premium | High | BUILD | Make an EPUB That Passes the Checker | make-an-epub-that-passes-the-checker | create epub | M |
| 27 | 20 | Social Carousel Maker | Premium | High | BUILD | Make a Swipeable Instagram or LinkedIn Carousel | make-a-swipeable-instagram-or-linkedin-carousel | carousel maker | M |
| 28 | 42 | Scan or Photo to Word/Excel/Text, Image to Word, Image to Excel | Professional | High | BUILD | Photo of a Table to Excel | photo-of-a-table-to-excel | image to excel | M |
| 29 | 43 | Video Speed, Reframe, FPS, Add Audio, Add Text and Logo | Professional | High | BUILD | Reframe a Landscape Video for Reels and Shorts | reframe-a-landscape-video-for-reels-and-shorts | resize video for instagram | M |
| 30 | 45 | AI Image Upscaler and Image Quality Enhancer (public Professional) | Professional | High | BUILD | Upscale a Small Photo 2x or 4x | upscale-a-small-photo-2x-or-4x | upscale image | M |
| 31 | 46 | Text to Speech and Text Read Aloud (browser voice) | Professional | High | BUILD | Hear Your Draft Read Aloud Before You Publish | hear-your-draft-read-aloud-before-you-publish | text to speech online | M |
| 32 | 52 | Professional vs Premium vs Workflow: which one do you need | Other | High | BUILD | Which FreeDailyPro Product Fits Your Job | which-freedailypro-product-fits-your-job | how it works | S |
| 33 | 53 | Best online PDF editors compared | Guide | High | BUILD | PDF Editors in the Browser Compared | pdf-editors-in-the-browser-compared | best pdf editor online | M |
| 34 | 54 | FreeDailyPro vs iLovePDF / Smallpdf style comparison | Guide | High | BUILD | Browser PDF Tools Compared: What Stays on Your Device | browser-pdf-tools-compared-what-stays-on-your-device | ilovepdf alternative | M |
| 35 | 72 | PowerPoint Automation API (27 endpoints) | API-MCP | High | BUILD | Generate PowerPoint Files From JSON With an API | generate-powerpoint-files-from-json-with-an-api | pptx api | L |
| 36 | 14 | Cover Letter Maker | Premium | Med | VERIFY_FIRST | Cover Letter From Your Results | - | - | S |
| 37 | 21 | Newsletter and Email Builder | Premium | Med | BUILD | Build an Email Newsletter You Can Paste Anywhere | build-an-email-newsletter-you-can-paste-anywhere | email newsletter builder | M |
| 38 | 22 | Expense Report and Mileage Log | Premium | Med | BUILD | Fill an IRS-Style Mileage Log and Expense Report | fill-an-irs-style-mileage-log-and-expense-report | mileage log template | M |
| 39 | 23 | Real Estate Listing Sheet | Premium | Med | BUILD | One-Page Property Listing Sheet for Open Houses | one-page-property-listing-sheet-for-open-houses | real estate flyer | S |
| 40 | 24 | Bill of Sale Generator | Premium | Med | BUILD | Write a Bill of Sale for a Car or Equipment | write-a-bill-of-sale-for-a-car-or-equipment | bill of sale template | S |
| 41 | 25 | User Manual Writer | Premium | Med | BUILD | Write a Product User Manual Customers Read | write-a-product-user-manual-customers-read | user manual template | M |
| 42 | 26 | Copyright Page Maker | Premium | Med | BUILD | Copyright Page Wording for a Self-Published Book | copyright-page-wording-for-a-self-published-book | copyright page template | S |
| 43 | 27 | ONIX Generator | Premium | Med | BUILD | Generate ONIX Metadata for Distributors | generate-onix-metadata-for-distributors | onix file | M |
| 44 | 28 | Printable Planner Maker | Premium | Med | BUILD | Make a Printable Weekly Planner as PDF | make-a-printable-weekly-planner-as-pdf | printable planner | M |
| 45 | 30 | Photo Slideshow Maker | Premium | Med | BUILD | Turn Photos Into a Slideshow Video With Music | turn-photos-into-a-slideshow-video-with-music | photo slideshow maker | M |
| 46 | 32 | Worksheet and Lesson Plan Maker | Premium | Med | BUILD | Make a Classroom Worksheet and Lesson Plan | make-a-classroom-worksheet-and-lesson-plan | lesson plan template | M |
| 47 | 34 | Seating Floor Planner | Premium | Med | BUILD | Plan Tables and Floor Layout for a Banquet | plan-tables-and-floor-layout-for-a-banquet | seating chart maker | M |
| 48 | 39 | Clean, Redact, Password Protect, Accessibility Checker (PowerPoint) | Professional | Med | BUILD | Prepare a Deck for Sharing: Metadata, Redaction and Passwords | prepare-a-deck-for-sharing-metadata-redaction-and-passwords | remove metadata powerpoint | M |
| 49 | 40 | Find/Replace, Replace Fonts, Slide Numbers, Watermark, Resize, Organize (PowerPoint) | Professional | Med | BUILD | Fix 60 Slides at Once: Fonts, Numbers and Find and Replace | fix-60-slides-at-once-fonts-numbers-and-find-and-replace | replace fonts powerpoint | M |
| 50 | 41 | Word to PDF, Unlock PDF, Flatten PDF, Bates Numbering | Professional | Med | BUILD | Flatten, Unlock and Number PDFs for Legal Filing | flatten-unlock-and-number-pdfs-for-legal-filing | bates numbering pdf | M |
| 51 | 44 | Video to Frames, GIF editor/resizer/to video/to frames, Images to GIF | Professional | Med | BUILD | Shrink a GIF Under 5 MB | shrink-a-gif-under-5-mb | compress gif | S |
| 52 | 47 | Volume Booster, ACX Audiobook Checker, Compare Two Audio Files | Professional | Med | BUILD | Check Audiobook Audio Against ACX Rules | check-audiobook-audio-against-acx-rules | ACX audio requirements | M |
| 53 | 48 | Subnet Calculator, String Escape, URL Encoder | Professional | Med | BUILD | Subnet Mask Cheat Sheet With Worked Examples | subnet-mask-cheat-sheet-with-worked-examples | subnet calculator | S |
| 54 | 50 | Email Signature Generator, Certificate Maker, Name Badge Maker | Professional | Med | BUILD | Email Signature That Works in Gmail and Outlook | email-signature-that-works-in-gmail-and-outlook | email signature generator | S |
| 55 | 56 | Invoice generator comparison for freelancers | Guide | Med | BUILD | Invoice Templates vs an Invoice App for Freelancers | invoice-templates-vs-an-invoice-app-for-freelancers | invoice generator comparison | M |
| 56 | 57 | How to convert any file type: a decision guide | Guide | Med | BUILD | Which Format Should You Convert To? | which-format-should-you-convert-to | file conversion guide | M |
| 57 | 58 | Starting a small business: 10 documents you need | Guide | Med | BUILD | The Paperwork of Starting a Small Business | the-paperwork-of-starting-a-small-business | small business documents checklist | M |
| 58 | 59 | Self-publishing checklist from manuscript to ONIX | Guide | Med | BUILD | (Grok proposes; see raw note in TSV) | - | - | M |
| 59 | 60 | How to host a trade show booth: tool by tool | Guide | Med | BUILD | (Grok proposes; see raw note in TSV) | - | - | M |
| 60 | 61 | Privacy: what happens to your file in a browser tool | Guide | Med | BUILD | (Grok proposes; see raw note in TSV) | - | - | M |
| 61 | 63 | Rental owner's document pack | Guide | Med | BUILD | Landlord Paperwork: Lease, Application, Notice | landlord-paperwork-lease-application-notice | landlord forms | S |
| 62 | 69 | Currency and VAT API | API-MCP | Med | BUILD | Currency and VAT API: Daily Reference Rates, VIES Checks | currency-and-vat-api-daily-reference-rates-vies-checks | vat api | M |
| 63 | 70 | Time Zone and Date Calculator API | API-MCP | Med | BUILD | Time Zone API: DST Gaps and Work-Hour Overlap | time-zone-api-dst-gaps-and-work-hour-overlap | timezone api | M |
| 64 | 71 | Mortgage and Loan Calculator API | API-MCP | Med | BUILD | Mortgage Calculator API With Amortization JSON | mortgage-calculator-api-with-amortization-json | mortgage api | M |
| 65 | 73 | PDF Form Filling and Redact API | API-MCP | Med | BUILD | Fill and Redact PDFs From Code | fill-and-redact-pdfs-from-code | pdf form fill api | M |
| 66 | 75 | API keys, rate limits, errors and billing for 4xx | API-MCP | Med | BUILD | API Errors Not Billed: How Calls Are Counted | api-errors-not-billed-how-calls-are-counted | api rate limits | S |
| 67 | 33 | Paper Submission Desk | Premium | Low | BUILD | Check a Journal Submission Before You Send It | check-a-journal-submission-before-you-send-it | journal submission checklist | S |
| 68 | 35 | Travel Planner (Event Suite) | Premium | Low | BUILD | Plan Group Travel for Event Guests | plan-group-travel-for-event-guests | group travel planner | S |
| 69 | 49 | Period and Ovulation, Pregnancy Scan Date calculators | Professional | Low | BUILD | Read a Cycle Calendar Without Guesswork | read-a-cycle-calendar-without-guesswork | ovulation calculator | S |
| 70 | 51 | Digital Download Packager, Text Cleaner, Business Days Calculator | Professional | Low | BUILD_IF_TIME | (Grok proposes; see raw note in TSV) | - | - | S |
| 71 | 62 | Install the site as an app on your phone | Guide | Low | BUILD | (Grok proposes; see raw note in TSV) | - | - | S |
| 72 | 74 | Image, Video, Audio Processing API | API-MCP | Low | BUILD | Resize Images With the API | resize-images-with-the-api | - | M |
| 73 | 76 | Bookkeeping Helper and Retirement and Debt Planning APIs | API-MCP | Low | BUILD | Bank CSV to Categories With an API | bank-csv-to-categories-with-an-api | - | M |
| 74 | 77 | Use-case pages: ISBN validation, pay stub, loan, word count, text similarity, job experience API | API-MCP | Low | BUILD | (Grok proposes; see raw note in TSV) | - | - | S each |
| 75 | 29 | Seller Pricing Desk | Premium | Low | NO_NEW_POST_VERIFY_ONLY | (Grok proposes; see raw note in TSV) | - | - | S |
| 76 | 31 | Custom QR | Premium | Low | DUPLICATE_REVIEW_NO_NEW_POST | (Grok proposes; see raw note in TSV) | - | - | S |
| 77 | 55 | Book Writing Toolbox vs Vellum, Atticus, Reedsy | Guide | - | DONE_NO_POST | (Grok proposes; see raw note in TSV) | - | - | - |
| 78 | 78 | RapidAPI listing guide: "Call FreeDailyPro APIs from RapidAPI" | API-MCP | Low | HOLD_UNTIL_LISTINGS_LIVE | (Grok proposes; see raw note in TSV) | - | - | S |
| 79 | 79 | AI Document Q&A, AI Invoice Extractor, AI PDF Redactor | AI Studio | Hold | HOLD_AI_STUDIO | Ask Questions of a PDF | - | - | M |
| 80 | 80 | AI Presentation Maker, AI Video Script Writer, AI Video Maker, AI Content Repurposer | AI Studio | Hold | HOLD_AI_STUDIO | (Grok proposes; see raw note in TSV) | - | - | M |
| 81 | 81 | AI Prompt Optimizer, AI Token Trimmer, AI Audio Transcriber | AI Studio | Hold | HOLD_AI_STUDIO | (Grok proposes; see raw note in TSV) | - | - | M |
