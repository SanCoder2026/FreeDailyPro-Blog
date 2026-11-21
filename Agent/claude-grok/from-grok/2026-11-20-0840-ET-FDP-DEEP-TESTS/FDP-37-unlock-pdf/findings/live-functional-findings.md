Sent: 2026-11-21 02:36 ET

# FDP-37 Unlock PDF: live functional findings (guest, headless Chromium + Firefox, Playwright 1.65, 2026-11-21 02:23–02:33 EST)

Locked inputs are synthetic (`scripts/make-locked.py`, built from FDP-36's unprotected sources). Downloads were checked with pikepdf/pypdf (`scripts/verify.py`, `json/verify.json`).

## Unlocking (all PASS)
| Case | Input | Result |
|---|---|---|
| K01 / A | AES-256 user password | dialog → "old123" → "Password removed…"; download opens without a password, unencrypted, and matches the source (pages, title, author, 2 form fields, 3 outlines, 3 links, page size, text) |
| K02 / B | AES-128 | same, matches source |
| K03 / E | RC4-128 | same, matches source |
| K04 | RC4-40 (R2) | unlocked |
| K05 / C | owner-only (no print/copy), no open password | unlocked straight away, no prompt (as documented); download unrestricted, matches source |
| K06 | unicode password `Pässwört-日本語-42`, 50 pages | unlocked; "Showing the first 12 of 50 pages" |
| K07 | password with trailing space | trimmed rejected ("That password didn't work"), exact accepted, as "spaces count" says |
| K08 | user = owner password | unlocked |
| K09 | opened with the **owner** password | unlocked (correct per spec) |
| K10 | wrong case, wrong, then right | two "didn't work", then unlocked; no lockout |
| K11 / D | unprotected PDF | "This PDF was not password-protected… same file, and it does not use a trial use"; download byte-identical to the input |
| K12 / K13 | corrupt PDF / text renamed .pdf | "couldn't be read as a PDF. It may not be a PDF at all, or it may be damaged. Nothing was used." (PASS, clear) |
| K14 | Cancel on the dialog | toast "Skipped … it's password-protected"; back to the drop zone (PASS) |
| K15 | unprotected 50 pages | 12 thumbnails + note |

- **Timing:** about 2 s per file from Unlock to the result.
- **Producer:** unchanged (the source's Producer is kept).
- **Firefox:** K01, K05 and K11 behave the same as in Chromium.
- **Dialog wording:** "your result won't have a password" is correct for this tool. It's the same shared dialog as in FDP-36, where the wording is wrong.

## Privacy (PASS, `json/privacy.json`)
- 231 requests and 13.8 KB of POST bodies (analytics/ads). None contains the password, the PDF title or `%PDF`.
- Storage and cookies are clean. After a reload the file is gone.
- Share copies only the tool URL.

## Trial use, gate and payment (`json/gate.json`, `json/handoff.json`)
- **Uses-left context** (3rd fresh context, `usageToday` 0), 02:25:21–02:27:17 EST:
  - Unlock is free (0 → 0).
  - Download A (AES-256): 0 → **1**. A again: 1 → 1.
  - Save to Google Drive → Google sign-in popup; Save to my cloud storage → email sign-in dialog (both stopped).
  - New + U02 (AES-128) → Download B: 1 → **1**. New + U05 (owner-only) → Download C: 1 → **1**. So **two more unlocked files downloaded free in the same page load**.
  - New + unprotected P02 → D: 1 → 1. Free by design ("does not use a trial use").
  - Reload: 1. U03 (RC4) → Download E: 1 → **10**. The display then jumped to the full daily count, which looks like reconciliation with the server's count (display-only evidence). The download was still served.
- **Verdict:** one trial use per page load, so later unlocked Downloads are free until reload. Under Santosh's Nov 20 every-Download decision this is a **P1 gate gap** (same shared `Kt` code as FDP-34–36).
- **At 0** (02:27:23 EST):
  - Unlock still works and shows up to 12 page thumbnails at **244×316 px** (low resolution; first 12 pages only). The thumbnails don't deliver what the tool sells, a password-free file, so **this is not a full-quality preview leak** (PASS).
  - Download → cap dialog → Buy Day Pass → "Day Pass, $1 … Email | Continue to payment" (stopped).
  - New + unprotected P02 → Download works at 0 (byte-identical pass-through, free by design). The stale banner from the blocked attempt stays on screen: "Today's trial uses are used up, so downloading was not done", even though the file did download (P3).
  - "Continue with Compress PDF" hands the unlocked file over. Compress runs, then its Download → cap dialog (blocked, PASS).
  - "Continue with Remove PDF Pages" hands it over (Remove pages needs a selection; no download offered).
  - Quick Buy day → email prompt; monthly → Stripe Checkout (session id redacted; stopped).
- **Uncounted path:** unprotected files download free. The page says so. Per the Oct 30 / Nov 20 rules, any uncounted path outside the three named tools is a policy question. Here the output is the identical input file, so the risk is nil (P3 policy note).
- **Keyboard:** Tab ×28 + Enter on the drop zone opens the chooser (PASS).
- **Trial uses spent:** 1–2 logged locally before the display jumped to 10 (display-only).
