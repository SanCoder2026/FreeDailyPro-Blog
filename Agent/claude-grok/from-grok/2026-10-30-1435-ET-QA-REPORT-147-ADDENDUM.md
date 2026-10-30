Sent: 2026-10-30 14:35 ET

# QA-REPORT-147 ADDENDUM — admin session ~14:33-14:34 ET
Supplements: QA-REPORT-147, B-0267–B-0269 (stamped 1433). Downloads in batch-66/downloads/. Checked with pdftotext, Python/json, ffprobe, FFT pitch, Pillow, XML parser. Ledger grepped first: L-317–L-319 updated, no new rows.

## arrivals-departures-board (B-0267, L-317)
- **arrivals-departures.csv** (416 B): header `Date,Movement,Guest,Organisation,Party size,Notes`, 8 rows: 4 Arrives 2026-11-12; Departs 1 on 11-13, 3 on 11-14. Matches the board. ✔ Notes column empty in the sample, so flight/time placement could not be verified.
- **arrivals-departures.pdf**: 1 page, Letter. "Sample offsite: arrivals and departures · 4 arrivals, 4 departures", grouped by day with names and organisations. ✔ No time, flight or pickup column (as in B-0267).
- **Sample-offsite.fdp-project.json** (9.9 KB): `app, kind:"project", version:1, saved`, `project{name, currency, locale, timeZone, paper, passKey, data}`. `data` holds guests (8), sessions (6), vendors (3), quotes (3), expenses (3), rooms (4), tasks (3), budgets (4), exhibitors (3). Guests have id, name, status, needsStay, **email**, organisation, role, dietary, arrival, departure, table (11 "@" in the file).
  - **Risk:** `passKey` (43-char token, the key the page says signs guest QR codes) is stored in plain text. Anyone the file is shared with (a co-planner, a vendor, or via email) can mint valid guest QR codes, and the file also carries guest emails and dietary notes (personal data).
  - **Is the warning enough?** A page note alone is not: the file is labelled for sharing/backup, and the key is invisible to a user who doesn't open the JSON.
  - **New gap (optional, P3):** (a) a passphrase option to encrypt the project file (e.g. AES-GCM from a PBKDF2/Argon2 key, all in the browser); (b) or an "Export without pass key" choice, with the key re-generated or re-entered on import; (c) a key rotation button that invalidates old QR codes. Owner's decision; not a bug.
  - Downloading this file is gated at 0 trial uses (owner's decision; not a gap).

## audio-scrambler (B-0268, L-318)
- **disguised_acx_a.mp3** (28,025 B) vs source a.mp3 (6.034 s, 128.6 kbps, 44.1 kHz mono, 440 Hz tone):
  - Duration **6.087 s** (+0.05 s, encoder padding) → **no truncation**. ✔
  - 44.1 kHz, mono, MP3 (Lavf59 / ffmpeg.wasm), **Xing header (VBR)**, average **36.8 kbps**.
  - Pitch (FFT peak): 440.0 → 277.0 Hz = **−8.01 semitones**. ✔
  - **Bit rate:** the drop from 128 kbps to 37 kbps average comes from VBR encoding of a pure tone, which compresses very well. With a test tone this is **not a confirmed bug**. Recheck with a speech clip: if speech also comes out below ~96 kbps or in 8–16 kHz bandwidth, file it as a quality bug. The file name keeps the source name ("acx_a" here) ✔.

## avatar-builder (B-0269, L-319)
- **avatar-512.png**: RGBA 512×512; all 4 corners (0,0,0,**0**) → **truly transparent** ✔; centre (255,219,180,255) skin.
- **avatar.svg** (483 B): well-formed XML, `viewBox="0 0 200 200"`, width/height 512 ✔. Vector shapes only (circle, path, g), no embedded raster. It has **no background rect**, which is consistent with transparent background selected. No `<title>`, so it has no accessible name (minor, B-0155).

## Admin checks still open (batch 66)
- audio-scrambler: speech clip at ±8 (bit rate/bandwidth); output with formants untouched (as expected).
- arrivals: a guest with flight notes, to confirm Notes reaches the CSV and PDF; import of the project file (does the key round-trip?).
