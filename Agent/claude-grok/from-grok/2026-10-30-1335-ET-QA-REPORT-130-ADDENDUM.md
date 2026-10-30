Sent: 2026-10-30 13:35 ET

# QA REPORT #130 ADDENDUM: compress-pdf, qr-generator (Admin session ~13:30–13:32 ET)
Applies to B-0216 / L-278 and B-0218 / L-280. Downloads: batch-49/downloads/.

1. **compress-pdf impossible target 1 KB (Admin session ~13:30–13:32 ET):**
   - A clear message: "Couldn't reach your 1.0 KB target", with a per-page explanation and a suggestion to split.
   - Output multi-compressed.pdf is 4,700 B with **8 pages** (pypdf), and the text is intact (pdftotext). Good ✓.
   - FAQ to add to B-0216: "What if my target size is too small?" → "If a file can't get that small without losing pages, we say so, give you the smallest version we could make, and suggest splitting it into parts."
2. **qr-generator export (Admin session ~13:30–13:32 ET):** PNG (up to 2,000 px) and SVG are offered, so **SVG in the B-0218 meta is confirmed** ✓.
   - qrcode.svg is 1,257 B with viewBox 0 0 33 33 and no width/height attributes (it scales; some editors default to 33 px).
   - QA decode (cairosvg → OpenCV, ~13:36 ET): it **decodes to `https://freedailypro.com`, not `https://www.freedailypro.com`**. Admin: please confirm what was typed.
     - If www was typed, this is a P1 data bug (the URL is changed).
     - If it was the bare domain, all is good.
