Sent: 2026-11-21 00:58 ET

# FDP-32 Hash Generator: test cases

- **URL:** https://www.freedailypro.com/tool/hash-generator, guest.
- **Expected digests:** `testfiles/vectors.json` (Python hashlib).
- **"Live"** = 2026-11-21 00:39–00:44 EST.
- **Scripts:** `hg-live.js`, `hg-stale.js`, `hg-gate.js`, `hg-uses.js`, `hg-share.js`, `hg-misc.js`.

| ID | Step | Expected | Live |
|---|---|---|---|
| HG-01 | "abc" | 5 digests = hashlib | PASS |
| HG-02 | "The quick brown fox…" | = hashlib | PASS |
| HG-03 | "héllo 日本 🚀" (UTF-8) | = hashlib | PASS |
| HG-04 | "abc\n" | = hashlib | PASS |
| HG-05 | "line1\r\nline2" | Either CRLF digest or a note | LF digest, no note (P3) |
| HG-06 | 1,000,000 × "a" | = hashlib, responsive | PASS (~3.2 s) |
| HG-07 | " " | = hashlib | PASS |
| HG-08 | Empty, no file | Message (or the empty digest) | Message only (P3) |
| HG-09 | File 12 B | = hashlib | PASS |
| HG-10 | File 0 B | = hashlib (e3b0c442… for SHA-256) | PASS |
| HG-11 | File 10 MB random | = hashlib | PASS (0.18 s) |
| HG-12 | File 60 MB | = hashlib, progress | PASS (0.85 s) |
| HG-13 | File + text | Clear which is hashed | File hashed, no notice (P3) |
| HG-14 | Remove file | Resets | PASS |
| HG-15 | Edit text after Generate | Results cleared or marked stale | **FAIL (P1)** |
| HG-16 | Compare after editing | No false Match | **FAIL (P1)**: "Match (SHA-256)" for "abd" |
| HG-17 | Compare exact / uppercase / spaced / trailing space | Match | PASS |
| HG-18 | Compare `sha256:<hex>` | Match | FAIL (P3) |
| HG-19 | Compare `<hex>  file.iso` | Match | FAIL (P3) |
| HG-20 | Compare wrong | No match | PASS |
| HG-21 | Copy SHA-256 | Exact digest on the clipboard | PASS |
| HG-22 | Keyboard: reach the file picker | Focusable | **FAIL (P1)** |
| HG-23 | Network scan | No text, file or digest in requests | PASS |
| HG-24 | Share | Tool URL only | PASS |
| HG-25 | At 0: Generate / Copy / Compare / file / Ctrl+C | Per policy | **Policy question**: all work, 10 → 10 |
| HG-26 | With uses left: Generate | Per policy (code: one use) | **PENDING** (RERUN row 32); one unconfirmed context stayed at 0 |
| HG-27 | Print | Digests present | PASS (2 pages) |
| HG-28 | 10 devices | No overflow | PARTIAL: iPhone SE 9 px; ja desktop 3 px |
| HG-29 | Locales + /ar | Translated or no hreflang | PARTIAL: es mixed, 8 English, /ar 404 |
| HG-30 | axe | No serious issues | PARTIAL: label-content-name-mismatch (desktop), ad-caption contrast (Pixel 7) |
