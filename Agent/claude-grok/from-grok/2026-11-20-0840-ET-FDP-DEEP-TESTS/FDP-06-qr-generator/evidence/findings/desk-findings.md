Sent: 2026-11-20 08:40 ET

# QR Code Generator: desk findings (no trial uses)

Written: 2026-11-19 12:02 EST. Captured 2026-11-19, 11:48–12:05 EST.

## Method

- Read-only curl of the tool, 10 locale URLs, the related blog posts, the QR topic page and sitemap.xml.
- The JS bundles in `js/`: QrGenerator, qrHelpers, UsageAndUpgradeStrip, useDownloadedResult, index.
- YouTube metadata, captions and frames.
- WebSearch.
- GSC data is not available.

## Page metadata

| Item | Value | Note |
|---|---|---|
| URL | https://www.freedailypro.com/tool/qr-generator | 200 |
| Title | "QR Code Generator Online - Instant, With Logo \| FreeDailyPro" | **"With Logo" competes with the Premium /tool/custom-qr**, whose title is "QR Code Generator with Logo - Custom Colors and Shapes" (cannibalization, P1) |
| Meta description | **75 chars**, "Generate QR codes for URLs, text, WiFi, vCard. Fast, right in your browser." | Thin. It doesn't mention email/SMS/phone, PNG/SVG, colours, logo or trial uses (P2) |
| H1 | "QR Code Generator" | OK |
| Canonical / hreflang | self / 11 | See Locales |
| og:image | og-default | Generic |
| JSON-LD | SoftwareApplication (Offer 4.99, no billing period), VideoObject (2026-10-16), **FAQPage with 1 question**, BreadcrumbList Home › QR Codes & Barcodes › QR Code Generator | Only one FAQ, so the rich-result potential is small (P2) |
| Images | 1 empty alt | Low |

## Copy accuracy (checked against the live UI and the JS)

1. **"When not to use it" contradicts the tool (P1).**
   - It says: "this tool encodes plain text and URLs only, not those specialized formats [WiFi, vCard]; a dedicated WiFi or vCard QR generator is the right tool".
   - It also says: "If your downstream use requires a vector format (SVG)… this tool's PNG output is the wrong format".
   - **Live:**
     - The WiFi tab encodes `WIFI:T:WPA;S:…;P:…;;` with correct escaping.
     - The Contact tab encodes a vCard 3.0.
     - Email, SMS and Phone produce `mailto:`, `SMSTO:` and `tel:`.
     - Download SVG exists.
     - All of these were decoded from the live preview with zxing-cpp and OpenCV (`json/decoded.json`).
   - This text appears in the WebSearch snippet.
2. **The Details "How to use" section only knows "text or URL" and "download… as a PNG image" (P1).** It never mentions the 7 types, SVG, size or EC.
3. "About" and the first "How to use it" are accurate (7 types, PNG up to 2,000 px or SVG, logo, EC raised automatically).
4. **Common questions has 1 entry** ("Should I test my QR code before printing?").
   - Unanswered: do codes expire (they don't), how WiFi works, PNG vs SVG, logo size, do downloads carry a mark.
   - The answer to "do codes expire" is already in the Details text: "doesn't expire or depend on this site".
5. The Tips recommend "a shortened URL" for small prints. Fine, but shorteners add a third-party dependency (they can expire). A one-line caution would help (P2).

## Product overlap: Pro vs Premium (C04)

- The Pro tool already offers a centre logo, colours, PNG/SVG and EC.
- **Its "Next step" card sells the Premium app ($3 day / $9.99 month, 2 trial uses) with "Put your logo in the middle, choose colors and shapes"**, which the Pro tool already does except for shapes.
- The blog /blog/branded-custom-qr-codes-with-logo-and-colors says "QR Generator is fine for quick tests. Custom QR is for pieces that sit next to brand guidelines."
- The difference to clarify: dot and corner shapes, gradients, PDF vector export (from tools.csv for custom-qr).
- The title and meta should stop competing on "with logo" (P1).

## Blog

- No post is dedicated to this tool, based on the QR-related sitemap slugs and /blog/topic/qr-tools (5 posts: brand-qr…, branded-custom-qr…, bulk-qr…, barcodes, scan-qr…). A post under an unrelated slug is an unverified absence.
- The tool links /blog/design-print-ready-restaurant-menu-card and /blog/print-open-house-sign-in-sheet (both link back twice).
- **Near-duplicate posts:** /blog/brand-qr-code-with-logo-and-colors and /blog/branded-custom-qr-codes-with-logo-and-colors target the same intent (custom-qr). The second calls the Pro tool "QR Generator" and the Premium one "QR Code Designer (Logo & Colors)" in its headings, while its link text says "QR Code Generator with Logo" (naming drift, P2).
- **Opportunity (P1 for the #8-ranked tool):** a "WiFi QR code for guests" or "vCard business-card QR" how-to. These are the features the page copy currently denies.

## Locales (server HTML)

| Locale | HTTP | Title / H1 |
|---|---|---|
| es | 200 | **"Generador de códigos QR gratis: enlace, WiFi, vCard"**. Says "gratis" (free), off-brand (P1). H1 localized |
| pt, fr, de, ja, hi, zh, ko, id | 200 | English title, meta and H1 (self canonical) |
| ar | 404 | — |

## Code reading (QrGenerator / qrHelpers bundles; confirmed live where marked)

- **vCard escaping bug (confirmed live).** `p()` replaces ";" with ";" (a no-op) instead of "\;".
  - Company "Smith; Jones & Co, LLC" is encoded as `ORG:Smith; Jones & Co\, LLC`.
  - In vCard, ";" splits ORG into organisation and unit, so phones show "Smith" plus a unit. Names with ";" are affected the same way.
  - The commas are escaped correctly (P1, a one-character fix).
- **The logo is stretched to a square (confirmed live).** `drawImage(m,w,R,h,h)` ignores the aspect ratio.
  - An 800×200 logo with a round mark is squashed: the circle becomes a 15×54 px ellipse in the preview (`screens/live/x-Q31_logo_wide.png`).
  - The SVG export uses `<image width=m height=m>` with the default preserveAspectRatio (meet), so the **PNG and SVG would differ** (verify on re-run) (P1).
- **A broken logo file:** a text file renamed .png shows "Logo added" and raises EC to H, while the preview silently drops the logo. In code, PNG export awaits the logo image and then shows "Couldn't create the PNG" (hypothesis; verify after reset) (P2).
- File names are fixed: `qrcode.png` / `qrcode.svg`. Bulk QR already has a slug helper (`S()`) that could name them from the content (P2).
- Capacity is shown live ("24 of 2,331 bytes used at level M") with a clear over-limit message. The contrast and inverted-colour warnings use a WCAG-style ratio (good).
- **A bare domain gets https://** ("example.com/menu" → "https://example.com/menu"). **"javascript:" is accepted** in Link without a note (low risk; most scanners ignore it) (P2).

## Competitors (WebSearch, 2026-11-19)

- QRGen, Toolo, SimpleTool, Cuelark and SimplifiedQR all offer browser-only static codes with WiFi, vCard, logo and PNG/SVG, plus **"no sign-up, no watermark, unlimited"**.
- Extras some of them have: transparent background, PDF export, calendar/location/WhatsApp/UPI types, "Scan me" frame text, dot styles, presets.
- FreeDailyPro's edge: the byte-capacity meter, contrast warnings and correct WiFi escaping.
- **Its gaps:**
  - 10 downloads/day, then a pass. Whether trial downloads carry a mark **needs re-run**.
  - No transparent background (absent from the controls), no calendar/location types (live-verified absent from the tabs), no frame label.
- **Indexing:** "freedailypro qr code generator" returns the tool first, and the snippet includes the contradictory "When not to use it" text.
