Sent: 2026-10-30 13:01 ET

# QA Report #121 — Addendum: admin-session output checks
The admin session ran about 12:47–12:49 ET. Files are in `batch-40/downloads/`. This addendum adds to report #121, which itself is unchanged.

## flatten-pdf (L-250) — output verified (admin session)
- **Message:** "Flattened 3 fields -- these values are now permanent".
- **File:** `flattened-filled_form.pdf` (6284 B). Checked with pypdf:
  - The page has no `/Annots`, so no widgets are left.
  - `/AcroForm` still exists, but `/Fields` is empty `[]`. That's harmless: no viewer will show fields. It is a cleanliness nit only; filed under B-0184 constraints and not a new bug.
- **pdftotext:** "Jane QA" and "Pro" are drawn as page content. The checkbox shows as an empty "Agree:" in text, which is expected because a check glyph isn't text.

## base64 (L-251) — output verified (admin session)
- Encode "héllo 👋" → `aMOpbGxvIPCfkYs=` (correct UTF-8), and decoding it round-trips.
- URL-safe → `aMOpbGxvIPCfkYs` (padding dropped, correct).
- Decode `###` → "Not valid Base64: unexpected "#" at position 1." with the input outlined in red. That's a good error state, and a model for B-0187.
- The 0-trial-uses paywall stays under B-0156.

## markdown-html-converter (L-252) — output verified (admin session)
- MD→HTML is correct.
- "Copied to clipboard" was confirmed by pasting it back.
- HTML→MD: `<h2>Yo</h2>` → `## Yo`.
- `converted.html` (40 B) is an HTML **fragment** with no `<!doctype>`, `<head>` or `<meta charset>`. **Added to B-0186's capability gaps:** the download should be a full, standalone document, at least when "Full HTML" is on. **Still needed:** a browser/admin check with "Full HTML" toggled on, to see whether it already covers this.
- The 390 px overflow bug is unchanged (open).
