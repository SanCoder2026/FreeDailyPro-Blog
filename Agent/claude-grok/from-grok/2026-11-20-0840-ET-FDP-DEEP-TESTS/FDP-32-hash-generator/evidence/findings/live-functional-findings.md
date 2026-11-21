Sent: 2026-11-21 00:58 ET

# FDP-32 Hash Generator: live functional findings (guest, headless Chromium, 2026-11-21 00:39–00:44 EST)

Vectors and expected digests: `testfiles/vectors.json` (computed with Python hashlib). Results: `json/cases.json`, `json/stale-compare.json`, `json/gate.json`, `json/uses-left.json`, `json/share.json`, `json/misc.json`. Big test files (10 MB random, 60 MB zeros) are not in the zip; `testfiles/make-files.py` recreates them.

## Correctness (PASS)
- All five digests (MD5, SHA-1, SHA-256, SHA-384, SHA-512) matched hashlib for: "abc", "The quick brown fox…", unicode "héllo 日本 🚀", "abc\n", 1,000,000 × "a" (~3.2 s), a single space; files of 12 bytes, 0 bytes, 10 MB random (0.18 s) and 60 MB zeros (0.85 s).
- H05 "line1\r\nline2": the digests equal those of "line1\nline2" — browsers normalise textarea line endings to LF, so text pasted from a CRLF file never matches that file's checksum. The FAQ says "the text box hashes exactly what you typed" (P3 copy; suggest "line endings become LF; hash the file instead").
- Empty text and no file → "Enter some text or choose a file to hash." (role=alert). The empty string (a valid input with a well-known digest) cannot be hashed as text; an empty file can (P3).

## P1: stale results produce a false "Match"
- Hash "abc", then edit the text to "abd" without pressing Generate: the five "abc" digests stay on screen with no notice (`screens/live/stale.png`).
- Then paste abc's SHA-256 into "Compare with expected checksum": the page says **"Match (SHA-256)"** while the text box holds "abd" (`json/stale-compare.json`, 2026-11-21 00:40:36 EST; `screens/live/stale-compare.png`).
- Cause in code: the text `onChange` clears only the error, not the results (`js/HashGenerator-*.pretty.js`, the textarea `onChange`). Choosing a file does clear results.
- For an integrity tool, a "Match" for different content is the worst failure mode.

## Compare box
| Pasted | Verdict |
|---|---|
| exact SHA-256 | Match (SHA-256) |
| uppercase | Match |
| MD5 with spaces every 8 chars | Match (MD5) |
| SHA-1 + trailing spaces | Match |
| SHA-512 | Match |
| `sha256:<hex>` | No match (P3: common prefix) |
| `<hex>  file.iso` (sha256sum output line) | No match (P3: Tips say "paste a checksum exactly as copied") |
| 64 zeros | No match |
- The compare box appears only after a first Generate.

## File vs text
- With a file selected and text typed, Generate hashes the file only, with no on-screen notice (documented in Limitations). P3.
- "Remove file" resets to "Or choose a file to hash".
- **P1 accessibility:** the file input is `display:none` inside a label; Tab from the textarea goes straight to "Generate Hashes" (`json/cases.json` `tabAfterTextarea`, `fileInputStyle`). Keyboard-only users cannot choose a file, which is half the tool (WCAG 2.1.1).
- All five Copy buttons are named just "Copy" (no algorithm in the accessible name) (P3).

## Privacy (PASS)
- No request to any host contained the typed text, the file content marker or any digest (`leaks: []`); the URL never changes; Share copies only the tool URL (`json/share.json`, 00:43 EST).

## Trial use (policy question)
- `json/gate.json` (2026-11-21 00:40:52–00:41:50 EST): context 0 loaded at 0 remaining (10/10). Generate (text), Copy SHA-256, Compare, Generate (file), Copy MD5 and selection copy all worked with no dialog; 10 → 10, also after reload.
- **One-off observation:** context 3 (00:41:24 EST) read `usageToday` 0 at load; the same actions (2 Generates, 2 copies, compare, selection copy) left it at 0, also after reload. A follow-up of 6 fresh contexts (`json/uses-left.json`, 00:42:10–00:42:43 EST) all loaded at 10/10, so this could not be repeated, and the full usage record of that context was not captured. Treat it as unconfirmed evidence that nothing is counted even with uses left.
- The code awaits `logUsageNow()` before hashing (Generate is built to be counted). Copy uses `copyText` (no gate). Blog: "remember 10 trial usages a day".
- Not in the Nov 20 uncounted list → **policy question for Santosh**. With uses left: pending (RERUN-AFTER-RESET row 32).
- No cap dialog, pass or Stripe appeared, so the payment path was not reachable.

## Print (PASS)
- `testfiles/outputs/print-preview.pdf` (2 pages): input, the Compare field, all five digests with Copy labels, then the video links.
