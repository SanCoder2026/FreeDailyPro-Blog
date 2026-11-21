Sent: 2026-11-21 16:53 ET

# Live functional findings (FDP-73)

- Gate: per unique content hash on Download (re-download free); fresh pages at 2/2 gated for Download, Drive and Combine. The trial PDF is marked on every page. One download moved 0/2 → 2/2 and blocked the next edited catalog (P1 check).
- Text prices refused; an invalid EAN-13 gives a silent blank back page; WebP fails Combine; 1 row per page with order links.
- Correct: importer (headers, no header, quotes, BOM, TSV, bad-row flags), tax maths, currencies, contents page numbers, links + QR, save/open, encrypted/damaged/unsupported file handling.
