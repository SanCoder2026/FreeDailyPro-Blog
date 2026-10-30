# B-0058 QR group: print-ready exports, frames and a stronger search snippet
Priority: P3 (improvement, traffic)      Estimated effort: 120–180 min      Report: #69      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the QR code and page metadata, push back where something is low value, and pick the order. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
The core of our QR tools already works well. This brief is about making them the easiest choice for someone printing a code: a flyer, a menu, a guest pass. It also aims to lift click-through on a group that already gets impressions.

## Why
- **Traffic.** The QR group has 1,273 GSC impressions at average position 13.6 and 48 views (test-plan.csv row 8). "bulk qr code generator" has 86 impressions at position 12.7 (analytics/2026-10-29-raw.md).
- **Live check, Oct 29 2026, 22:12–22:20 ET.** Each content type produced a correctly encoded payload: Link, WiFi with escaped `; , " : \`, vCard with Unicode and an escaped comma, mailto with %-encoding, SMSTO, tel, and Unicode/emoji text. Colour, logo (error correction raised to H), the 200–2000 px menu and the low-contrast warning all work. The PNG and SVG downloads decode.
- **What competitors offer that we don't**, checked Oct 29: qrcode-monkey.com, techwhack.com comparison, oathqr.com.
  - QR Code Monkey exports PDF and EPS, and has frames with call-to-action labels plus dot and eye styles.
  - NeoReader also exports PDF/JPG/WebP, adds frames, and runs a live scan test before download.
  - OathQR and NeoReader do free bulk from a CSV upload.
- **Copy and metadata.**
  - Custom QR's meta description is only 54 characters: "Create QR codes with custom colors, logos, and shapes."
  - Phone codes keep the typed formatting, e.g. `tel:+1 (555) 010-0123`. That's valid, but normalising to `tel:+15550100123` is safer for older scanners.

## Outcomes
- PDF export, and EPS if cheap, for print on QR Generator and Custom QR.
- An optional frame with a short label such as "Scan for menu" on Custom QR.
- A "scan check passed" tick beside the preview, from decoding our own render in the browser.
- Bulk QR accepts a .csv file upload as well as the textarea.
- Custom QR meta description at 140–155 characters, naming logo, colours, dot styles and SVG. Keep "free" in SEO tags (owner rule).
- Phone payloads normalised to E.164 digits.

## Constraints
Everything stays in the browser. Counting is unchanged: one use per download, and Custom QR is a Premium app at 2/day. The API side of QR (format, size, colour) is B-0040; don't duplicate that work here.

## Test cases
R69-QR-01..10 (REPORT-69). After the change: decode the PDF/EPS export, and confirm frame + logo still decodes at H.
Owner decisions needed: which of PDF/EPS/frames to ship first (improvement).
