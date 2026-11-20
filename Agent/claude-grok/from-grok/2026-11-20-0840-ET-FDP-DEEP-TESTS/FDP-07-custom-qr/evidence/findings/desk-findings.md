Sent: 2026-11-20 08:40 ET

# FDP-07 custom-qr: desk findings

- **Written:** 2026-11-19 12:29:38 EST (box `date`, ET). Sources: `html/tool.html`, `html/tool-visible.txt`, `js/`, `html/locales.txt`, sitemap, WebSearch (2026-11-19).
- **GSC data is not available.**

## Identity and indexing
- URL https://www.freedailypro.com/tool/custom-qr: 200, self canonical, `<html lang="en">`, in the sitemap (lastmod 2026-11-19) with a video block (-YoQA8K6x8I).
- Title "QR Code Generator with Logo - Custom Colors and Shapes"; H1 "QR Code Generator with Logo — Custom Colors and Shapes"; meta 105 chars ("…download PNG, SVG or a print-ready vector PDF").
- Brand query "freedailypro custom qr code": the tool ranks #1, the blog post #2 (WebSearch, 2026-11-19).
- JSON-LD: Offer 9.99 USD with no billing period (it is $9.99/month in the cap dialog; there is also a $3 day pass); VideoObject; FAQPage (7 questions); BreadcrumbList.
- Category: QR Codes & Barcodes, **Premium Application**, 2 trial uses a day, $3 day pass or $9.99 a month (category page and cap dialog).

## Copy contradictions (live-verified against the UI)
1. **"When not to use it"** says to skip the tool for Wi-Fi, contact cards, e-mail and text messages because it "encodes only the single line of text you type". The live UI has Link, Text, WiFi, Contact, Email, SMS and Phone tabs, and all of them decode correctly (C18–C22).
2. **Details → How to use** describes a "Content box" and ends "press 'Download PNG' or 'Download SVG'". There are 7 tabs, and a vector PDF and a bulk ZIP also exist.
3. **Limitations:** "Content is a single-line box". The Text tab is multi-line.
4. **FAQ "What exactly does the code contain? … the exact text"** is false for characters beyond Latin-1 (C23: "Grüße 日本 👍" → "Grüße å, =M").
5. **FAQ "vector PDF"** says the frame carries over. It does not mention that non-ASCII frame text becomes "?" in the PDF, or that trial PDFs carry a "Created with FreeDailyPro.com" badge drawn over the code.
6. **Limitations: "border about 4 percent of the image width"** is accurate to the code (`margin: Math.round(size*.04)`), but it is about 1.4 modules for a short URL (50 px at 1000 px, about 36 px modules). The ISO/IEC 18004 quiet zone is 4 modules. The copy treats it as a layout tip, not a scan risk.
7. Nothing on the page says that the free preview is unlimited but each download costs a trial use, apart from the small "Download uses 1 trial use" line. The mark is disclosed only inside the cap dialog ("removes the 'Created with FreeDailyPro.com' mark from your PDFs and images").

## Blog
- Two near-duplicate posts: /blog/brand-qr-code-with-logo-and-colors and /blog/branded-custom-qr-codes-with-logo-and-colors (2026-10-24).
- The branded post is stale against the tool:
  - It says "PNG or SVG" only (there is no PDF).
  - It mentions "PNG 1200 px" (not an option; the options are 300/500/1000/1500/2000).
  - "File downloads count toward Professional Tools trial usage" (the tool is a Premium Application).
  - "This is a styled QR maker, not a bulk engine—use Bulk QR for lists" (the tool now has a 200-code bulk ZIP).
  - It names the tool "QR Code Designer (Logo & Colors)" (an old name).

## Code reading (js/CustomQr-Be2jWJ5d.js, qrHelpers)
- PDF frame text: `replace(/[^\x20-\x7E]/g,"?")`, which confirms the "Escan?ame ??" output.
- Bulk ZIP: `Math.min(Number(size),1e3)` caps the bulk images at 1000 px even when 2000 px is chosen; the UI does not say so (live: 2000 chosen → 1000×1000 files).
- File names are fixed: custom-qr.png/.svg/.pdf and styled-qr-codes.zip.
- EC is H with a logo and M without. The logo is imageSize 0.25 with hideBackgroundDots.
- "Lines are name,value" is an opt-in checkbox (default off). With it off, "name3,https://c.example" is encoded literally, which is expected.

## C04 cluster / duplicates
- qr-generator (Professional Tool) also says "with Logo" in its title, so both pages compete for "QR code generator with logo".
- The bulk section overlaps bulk-qr (Professional Tool, 500 codes, PNG/SVG, EC choice). custom-qr's bulk adds styling, which is a real difference, but the bulk-qr page says "for one code with a logo … a single generator is better" and neither page links to the other's strength.

## Competitors (WebSearch 2026-11-19)
- QRsnapp, genqrfree, ForQRCode, qrmerkez and ZodQR all offer logo, colours, dot/eye shapes and PNG/SVG/PDF (several add EPS), and stress "no watermark, unlimited, no sign-up". qrmerkez has 17 types; QRsnapp has 14 types and a transparent background.
- FreeDailyPro's angle: frame label, gradient, PDF in mm, 200-code styled bulk ZIP with index.csv, contrast warnings. It needs a clean, scannable output and honest trial terms to compete.

## Locales (curl, SSR)
- en 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- es 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- fr 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- de 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- pt 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- it 404 | Page not found | FreeDailyPro | 
- ja 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- zh 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- hi 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- id 200 | QR Code Generator with Logo - Custom Colors and Shapes | 
- ar 404 | Page not found | FreeDailyPro | 
- SSR titles stay English in every locale (lang attribute is localized). hreflang lists ko, but not it/ar. /it and /ar return 404 (not in hreflang, so not a broken link).
