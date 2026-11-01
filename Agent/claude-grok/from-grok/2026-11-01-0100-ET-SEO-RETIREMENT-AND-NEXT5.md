Sent: 2026-11-01 01:00 ET (Grok Orchestrator)

# SEO: retirement pages + next 5 tool pages

## Intent
Win the 401k/retirement calculator searches and tighten 5 more high-demand tool pages.

## Why
The /tool/retirement-calculator, roth-ira-calculator and pension-calculator URLs return page not found despite demand, and several titles and metas are over length.

## Outcome
Ship the fixes below. Redirect /tool/retirement-calculator to the 401(k) page for now. Before shipping, verify and drop any untrue claim: no upload/no signup on json-formatter and zip-unzip; "without quality loss" on trim-video (Fast cuts only); a salary-raise input on the 401(k) tool; make the pdf-to-word and ocr-pdf FAQs agree on scanned-page languages.

---

# SEO next-5 + retirement pages (Claude-ready) — Nov 1, 2026, 1:00 AM ET
Owner: SEO Engine → Orchestrator → Claude. **SEO only:** change titles, metas, H1s, FAQ copy, on-page wording and related links. Don't change tool behavior.

All pages were fetched live Nov 1, around 12:55 AM ET. Character counts were measured with Python `len()`, where an en dash counts as 1 character. Every FAQ answer comes from the page's own live copy.

**Rules:**
- "Free" appears only in the title and meta. Remove it from the H1 and body.
- Counts use multiples of 50 with a plus (300+).
- Say "10 trial uses per day".
- ⚠ marks a claim to verify before shipping.

---
## A. Retirement pages
Live (from the sitemap): /tool/401k-calculator, /tool/compound-interest, /tool/fire-calculator, /tool/sip-calculator.

Not found (404): /tool/retirement-calculator, /tool/pension-calculator, /tool/roth-ira-calculator.

**Why:** "401k calculator" and "retirement calculator" are high-volume money keywords. The 401(k) page supports both phrases. It projects the balance at retirement with employer match, raises and expected return, applies the IRS yearly limit including catch-up from age 50, and shows today's dollars. Yet its H1 is just "401(k) Calculator", its meta doesn't mention catch-up or today's dollars, and it has only 3 FAQs.

**Outcome:** The 401(k) page ranks for both phrases. The other three pages pick up long-tail "retirement" searches and link to the 401(k) page as the retirement hub.

### A1. /tool/401k-calculator (primary target for "401k calculator" and "retirement calculator")
- Title (52): `401(k) Calculator – Retirement Savings & Match, Free`
- Meta (140): `401(k) retirement calculator: project your balance with employer match, raises and return, using the IRS limit incl. catch-up from 50. Free.`
- H1: `401(k) Retirement Calculator – Balance at Retirement with Employer Match`
- Intro line: "Use this 401(k) calculator as a retirement calculator: enter your age, salary, contribution and employer match to see your projected balance at retirement, in future and today's dollars."
- FAQs (keep the 3 existing ones and add 3 from the live copy):
  1. *Existing:* Should I contribute enough to get the full employer match? Generally yes, because it's an immediate, guaranteed return.
  2. NEW: Does it apply the IRS contribution limit? Yes. It applies the yearly limit, including catch-up contributions from age 50, held at today's level.
  3. NEW: What does "today's dollars" mean? The projected balance is adjusted for the inflation rate you enter. The live example is about $897,550 at 2.5% inflation.
  4. NEW: Can I use it as a general retirement calculator? Yes, for workplace 401(k) savings. For a total early-retirement target, use the FIRE Calculator.
  5. *Existing:* What is the plan start date? It's optional and only labels calendar years.
  6. *Existing:* Does the start date change the balance? No.
- ⚠ The "raises" input appears only in the live copy line ("employer match, raises and expected return"). Claude: confirm there's a salary-increase field before mentioning it in the H1 or meta. It's currently in the meta only via "raises".
- Links: /tool/fire-calculator, /tool/compound-interest, /tool/sip-calculator, /tool/income-tax-calculator, /tool/mortgage-calculator

### A2. /tool/fire-calculator
- Title (47): `FIRE Calculator – Early Retirement Number, Free`
  - The current title is exactly 60 chars with awkward wording.
- Meta (141): `Find your FIRE number and how many years to early retirement, with Lean and Fat targets and results in today's dollars. Free FIRE calculator.`
- H1: `FIRE Calculator – Your Early Retirement Number and Date`
- Wording: in the existing FAQ "How is this different from a regular retirement calculator?", add one sentence: "For a 401(k)-only projection with employer match and IRS limits, use the 401(k) Calculator." It already has 8 good FAQs, so add none.
- Links: /tool/401k-calculator, /tool/compound-interest, /tool/sip-calculator, /tool/income-tax-calculator, /tool/mortgage-calculator

### A3. /tool/compound-interest
- Title (55): `Compound Interest Calculator – Retirement Savings, Free`
- Meta (138): `See how savings grow with compound interest and regular contributions, with a year-by-year table and optional start date. Free calculator.`
  - The current meta is 160 chars, which is over the limit.
- H1: `Compound Interest Calculator with Regular Contributions`
- Wording: add one line: "Saving for retirement through a 401(k)? The 401(k) Calculator adds employer match and IRS limits." Don't claim retirement-specific features on this page.
- Links: /tool/401k-calculator, /tool/fire-calculator, /tool/sip-calculator, /tool/mortgage-calculator, /tool/percentage-calculator ⚠ (confirm this page exists)

### A4. /tool/sip-calculator
- Title (48): `SIP Calculator – Step-Up & Retirement Goal, Free`
- Meta (137): `Calculate SIP future value with a lumpsum, yearly step-up and inflation-adjusted result, compounded monthly. Plan a long-term goal. Free.`
- H1: `SIP Calculator – Monthly Investment with Yearly Step-Up`
- Wording: use "retirement goal" only as an example ("e.g. a retirement corpus"). There are no retirement-specific features. It already has 8 FAQs, so add none.
- Links: /tool/compound-interest, /tool/fire-calculator, /tool/401k-calculator, /tool/income-tax-calculator, /tool/mortgage-calculator

### Missing-tool demand (flag for Claude/Orchestrator; claim nothing yet)
- **Retirement calculator, general:** there's no /tool/retirement-calculator. The pages cover savings, but none covers withdrawals or drawdown ("will my savings last", Social Security, pension income). Short term, add a 301 redirect or alias from /tool/retirement-calculator to /tool/401k-calculator. Real fix: a retirement-income/drawdown tool.
- **Roth IRA / IRA calculator:** 404. Roth isn't mentioned on the 401(k) page, so don't claim it.
- **Pension calculator:** 404.

---
## B. Next 5 tool pages (weakest SEO in the next demand tier)

### B1. /tool/json-formatter — keyword: "JSON formatter online" (#27)
**Why:** The meta is 85 chars and generic, and the H1 "JSON / YAML Formatter" leaves out "validator". The strongest features aren't in the snippet: JSON↔YAML conversion, Fix it for me (repairs comments, trailing commas and unquoted keys), and Sort keys.
**Outcome:** Wins the "JSON validator", "JSON to YAML" and "fix invalid JSON" variants.
- Title (47): `JSON Formatter & Validator, JSON to YAML | Free`
- Meta (139): `Format, validate and minify JSON, convert JSON to YAML and back, sort keys and fix trailing commas or comments. Runs in your browser. Free.`
- H1: `JSON Formatter & Validator – Also Converts JSON ↔ YAML`
- FAQ:
  1. Does it convert JSON to YAML and back? Yes, with the third button. Indent and Sort keys apply.
  2. What does Fix it for me repair? Comments, single-quoted strings, unquoted keys and trailing commas, then it re-checks the result.
  3. Will large numbers or 1.10 change? Not when formatting or minifying JSON. In YAML conversion, 1.10 becomes 1.1.
  4. What does Sort keys do? It orders object keys alphabetically at every level and leaves array order alone.
  5. How does it detect YAML? Bracket, brace or quote means JSON. Otherwise it tries JSON first, then YAML.
  6. ⚠ Is my JSON uploaded? Only the meta says it runs "in your browser". Claude: confirm, then add the answer "No, it's formatted in your browser."
- Links: /tool/case-converter, /tool/word-counter, /tool/zip-unzip, /tool/qr-generator, /tool/unit-converter

### B2. /tool/pdf-password — keyword: "password protect PDF online free" (#22)
**Why:** The meta is only 76 chars. The title is exactly 60, at the cutoff limit. The H1 "Add PDF Password" doesn't match how people search ("password protect PDF"). Strong trust facts aren't in the snippet: AES-256, password never sent, and a post-check of the result.
**Outcome:** A higher click rate from privacy-minded searchers, and a better H1 match.
- Title (48): `Password Protect PDF – AES-256, No Upload | Free`
- Meta (145): `Add an AES-256 password to a PDF in your browser. The file and password never leave your device, and the result is checked before download. Free.`
- H1: `Password Protect a PDF (AES-256)`
- FAQ (there are already 13; show these 6 first and remove the duplicates "What encryption does it use?" and "Can you recover my password…"):
  1. How strong is it? AES-256, the strongest the PDF format offers.
  2. Is my password sent anywhere? No. Encryption and key derivation run in your browser.
  3. How do I know it worked? The tool reopens the file with your password and compares pages, title and form fields.
  4. Will every reader open it? Every current reader and phone will. Only readers from before 2006 may not.
  5. Can it remove a password? No. It only adds protection.
  6. Forgot the password? There's no recovery. Keep it in a password manager.
- Links: /tool/pdf-watermark, /tool/redact-pdf ⚠ (Reddit rule keeps redact-pdf out of Reddit; on-site links are fine), /tool/merge-pdf, /tool/compress-pdf, /tool/split-pdf

### B3. /tool/pdf-watermark — keyword: "add watermark to PDF free" (#23)
**Why:** The meta is 80 chars, and the H1 "Add Watermark" doesn't say PDF. The FAQ has duplicates: logo formats twice, Tiled twice, copy protection twice. Real strengths are missing from the snippet: text or logo, tiled or 5 positions, opacity, page ranges, skip the cover, nothing uploaded.
**Outcome:** Matches "watermark PDF with logo" and "confidential/draft watermark", and the FAQ is clean.
- Title (41): `Add Watermark to PDF – Text or Logo, Free`
- Meta (147): `Stamp text or a logo on PDF pages: tiled or 5 positions, opacity slider, page ranges, skip the cover. Runs in your browser, nothing uploaded. Free.`
- H1: `Add a Watermark to a PDF – Text or Logo`
- FAQ (cut 14 down to 6 and drop the duplicates):
  1. Can I skip the first page or watermark only some pages? Yes. Use Skip the first page, or a range like 2-5, 8.
  2. Can I use my logo? Yes. Use Image / Logo mode. PNG and JPEG work directly; WebP, GIF, BMP and SVG are converted. TIFF is refused.
  3. Position and transparency? There are 5 presets or Tiled, plus an opacity slider.
  4. Does it stop copying? No, it's a visual label. Use PDF Password to restrict opening.
  5. Other languages? Yes. Latin, Hindi, Marathi and Nepali are real text; other scripts are placed as a picture.
  6. Uploaded? No. Both the PDF and the logo stay on your device.
- Links: /tool/pdf-password, /tool/merge-pdf, /tool/compress-pdf, /tool/split-pdf, /tool/pdf-to-jpg

### B4. /tool/zip-unzip — keyword: "zip unzip files online no upload" (#20)
**Why:** The meta is 83 chars and repeats "in browser" twice. The H1 "ZIP / UnZIP Files" has odd casing.
**Outcome:** A clean snippet for both the "create zip" and "extract zip" intents.
- Title (50): `Zip & Unzip Files Online, No Upload | FreeDailyPro`
  - Note: this has no "Free" in the title; the meta carries it.
- Meta (142): `Create a ZIP from several files or extract one in your browser. Files are never uploaded, and you see before-and-after sizes. Free, no signup.`
  - ⚠ "no signup": confirm the tool needs no account given 10 trial uses per day. Otherwise drop it.
  - ⚠ "never uploaded": this comes from the title's "No Upload". Confirm it.
- H1: `Zip and Unzip Files in Your Browser`
- FAQ (all live):
  1. Will zipping JPGs save space? Very little. Text, CSV and uncompressed images shrink most.
  2. How much smaller? It depends on the content. The tool shows exact before and after sizes.
  3. Are folders kept when extracting? No. Files are saved by name only.
  4. Duplicate names? Later ones are numbered: photo (2).jpg and so on.
  5. Password-protected ZIP? It isn't supported.
  6. Create and extract at once? No. Remove the .zip to create a new one.
- Links: /tool/compress-pdf, /tool/compress-image, /tool/merge-pdf, /tool/json-formatter, /tool/image-to-pdf

### B5. /tool/trim-video — keyword: "trim video online free no upload" (#25)
**Why:** The title is 64 chars and gets cut off. The meta is 106 chars. The H1 is "Trim & Cut". The meta doesn't mention Fast lossless vs Exact MP4 or the in-browser FFmpeg.
**Outcome:** The full title shows, and the page wins "cut video without losing quality" searches.
- Title (50): `Trim Video Online – Cut Without Quality Loss, Free`
  - ⚠ Lossless applies to Fast mode only. If Claude prefers to be strict, use instead (44): `Trim & Cut Video Online – No Upload, Free`
- Meta (143): `Cut one or more clips from a video: Fast lossless cuts or Exact MP4 cuts, then merge them into one file. Runs in your browser, no upload. Free.`
- H1: `Trim and Cut Video – Fast Lossless or Exact Cuts`
- FAQ:
  1. Will trimming reduce quality? Fast cuts don't re-encode, but they cut only at keyframes.
  2. Exact vs Fast? Exact re-encodes to MP4 (H.264/AAC 128 kbit/s) at your typed time. Fast is quick and lossless.
  3. Several pieces into one file? Yes. Trim All Segments, then Merge All & Download, which needs at least 2 segments.
  4. How do I type times? 65.5, 1:05.5 or h:mm:ss.
  5. Why is it downloading an engine? FFmpeg (~25 MB) loads once from a CDN, and your video is never uploaded.
  6. Output format? Exact and merged files are MP4. Fast keeps the original extension.
- Links: /tool/compress-image, /tool/zip-unzip, /tool/heic-to-jpg, /tool/webp-converter, /tool/image-to-pdf

### Also: /tool/pdf-to-word title fix (quick win)
- The current title is 64 chars and gets cut off. New title (44): `PDF to Word – Editable .docx with OCR | Free`
- Keep the existing meta (146 chars, good).
- H1: `PDF to Word Converter – Editable .docx` (the current H1 is "PDF to Word").
- ⚠ **FAQ contradiction to fix:** one answer says scanned pages can be read in "Hindi, English + Hindi, Spanish, French, German, Portuguese or Italian". Another says "English and Hindi are automatically recognized". Also, OCR PDF says "English is currently supported". Claude: reconcile with the actual OCR language support.

## Runner-ups for next hour
- /tool/ocr-pdf: meta 123, H1 "OCR PDF", English only.
- /tool/exif-remover: H1 "EXIF Remover".
- /tool/webp-converter: H1 is bare.
- /tool/case-converter: meta 160, over the limit.


Source: owner
