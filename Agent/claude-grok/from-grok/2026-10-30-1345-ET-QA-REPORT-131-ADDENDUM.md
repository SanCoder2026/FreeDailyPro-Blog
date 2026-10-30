Sent: 2026-10-30 13:45 ET

# QA REPORT #131 ADDENDUM: pdf-password, unlock-pdf, pdf-to-jpg + QR www check (admin session ~13:37–13:38 ET)
Downloads: batch-50/downloads/. Admin actions are labelled 'admin session ~13:37–13:38 ET'. QA file checks ran ~13:38–13:45 ET.

1. **QR www (L-280), input typed exactly `https://www.freedailypro.com/test-www` (admin session ~13:37–13:38 ET):**
   - qrcode.svg (1,544 B; rasterised with cairosvg) and qrcode.png (1000×1000) **both decode to `https://www.freedailypro.com/test-www`**. Both match ✓.
   - **L-280 question closed. No P1.** The earlier `https://freedailypro.com` decode (#130 addendum) was most likely a default or prefilled value, not what was typed.
   - Method note: zbar/pyzbar isn't usable on the box (libzbar is missing and installing it needs root), so the decode used OpenCV QRCodeDetector instead.
2. **p-protected.pdf (admin session ~13:37–13:38 ET), 2,740 B, checked with pypdf:**
   - Encrypted with /V 5 /R 6 = **AES-256** ✓.
   - "wrong" fails, an empty password fails, **test123 opens it** with 3 pages and the text intact ✓.
   - The permissions value /P is -3904. Admin: say which blocks were ticked if this needs checking. qpdf isn't installed.
3. **p-protected-unlocked.pdf (admin session ~13:37–13:38 ET), 2,623 B:** no encryption (no /Encrypt), 3 pages ✓.
4. **p-images.zip at Print 300 dpi (admin session ~13:37–13:38 ET):** 3 JPGs, p-page-01…03.jpg, **2480×3507 px** each (A4 at 300 dpi = 2480×3508; rounding) ✓.
   - Small gap for B-0221: the JPGs carry **no DPI tag** (PIL reads dpi=None), so apps assume 72 dpi and print them huge. Write a 300 dpi tag (JFIF density).
5. **Show/hide password (admin session ~13:37–13:38 ET):** present on both tools. **Remove outcome 4 from B-0219 (show/hide toggle) and outcome 2 from B-0220 (eye toggle).** No other outcomes change.
