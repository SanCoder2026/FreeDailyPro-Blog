Sent: 2026-10-30 13:29 ET

Supersedes 2026-10-30-1329-ET-B-0218-qr-generator-seo.md. The suggested title there was 64 chars, not the 60 stated, so it broke the under-60 rule. It's replaced here with a 54-char title. Nothing else changed.

# B-0218-v2 QR Code Generator: title under 60, a real meta, and the content the top results all have
Priority: P2 · Estimated effort: S · Report: #130 (SEO backfill 2) · Source: curl server HTML 2026-10-30 ~13:27 ET + GA/GSC (analytics/2026-07-10-to-now-raw.md) + Google top-5 (WebSearch)

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

SEO only. Function verified earlier (L-063 all types encode; L-077 2000 px PNG).
## Intent
People making a QR code for a link, WiFi, menu or business card should see right away that we do every common type with a logo and a print-quality download, and that the codes never expire.
## Why
- GA: 48 views.
- GSC: sister pages /tool/custom-qr 1/685, position 14.0, and /tool/bulk-qr 1/588, position 13.2. Query "bulk qr code generator" 1/86, position 12.7. No rows for /tool/qr-generator itself.
- Top results (13:29 ET): QRGrip, Link2QR, Simplified QR, QRGen, TinyQR. All of them have:
  - "no signup, no watermark, never expires"
  - a static vs dynamic explainer
  - a table of types with what each does (WiFi, vCard, SMS, email, geo, WhatsApp)
  - PNG + SVG (+ PDF), logo with error-correction H
  - a "test before printing" note
  - a bulk-from-CSV link
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, FAQPage, BreadcrumbList, VideoObject), full OG/Twitter set. The site-wide items (og-default.png, template/footer H2s, the boilerplate meta "Free and fast, right in your browser.", empty video alt, unrelated nav category links) → **B-0209**.
  - **Current title "QR Code Generator Online Free - Instant, With Logo | FreeDailyPro" is 65 chars, over the 60 limit.**
  - **Meta is 84 chars.**
  - H1 "QR Code Generator" (ok).
  - /es is translated ✓.
- **Keyword gaps:** "qr code generator with logo", "wifi qr code", "vcard qr code", "qr code that never expires", "static vs dynamic qr".
- **Suggested:**
  - Title: `QR Code Generator – Links, WiFi   - Title: `QR Code Generator – Links, WiFi, vCard, With Logo | FreeDailyPro` (60) vCard | FreeDailyPro` (54)
  - Meta: `Make a QR code for a link, WiFi network, contact card, text or email. Add your logo and colours, then download a sharp PNG. Static codes never expire.` (150)
  - H1: `QR Code Generator – Make a QR Code with Your Logo`
  - H2s:
    - "How to make a QR code"
    - "QR code types and what they open" (a table)
    - "Do these QR codes expire?"
    - "Tips before you print" (size, contrast, test scan)
  - FAQ:
    - "Do the QR codes expire?" → "No. They're static: the content is inside the code."
    - "Can I add a logo?" → "Yes. Error correction is set to High automatically so it still scans."
    - "How do I make a WiFi QR code?" → "Choose WiFi, enter the network name and password."
    - "Can I make many QR codes at once?" → link to Bulk QR.
- Add SVG to the meta only if SVG download exists on the website (the ApyHub SVG item is tracked separately, not here).
## Outcomes (ranked)
1. Title of 60 chars or fewer, and meta as above.
2. A types table and an "expire" H2.
3. Visible cross-links to Custom QR and Bulk QR (both have more GSC impressions than this page).
## Constraints
Keep the URL. Don't claim formats that aren't shipped.
## Test cases
1. Title length ≤60.
2. Meta 140–160.
3. Links to /tool/custom-qr and /tool/bulk-qr inside `<main>`.
