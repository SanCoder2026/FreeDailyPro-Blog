Sent: 2026-11-21 02:24 ET

# FDP-36 Add Password to PDF: live functional findings (guest, headless Chromium + Firefox, Playwright 1.65, 2026-11-21 02:08–02:19 EST)

Inputs are synthetic (`scripts/make-pdfs.py`). Outputs were checked with pikepdf and pypdf (`scripts/verify.py`, `json/verify.json`).

## Encryption (all PASS)
- **Encryption type:** every output is AES-256: Standard handler R6 / V5, AESV3. None of them opens without the password; all open with it.
- **Content kept:** pages, title, author, form fields (`employee_name`, `agree`), all outlines (3 and 50) and all links (3 and 50) survive. Text extracts on the first and last page.
- **Passwords:**
  - Unicode `Pässwört-日本語-42` opens (C).
  - A trailing-space password opens only when typed exactly (D). The page warns "Spaces count".
- **Block options:**
  - All three ticked (B): /P −3392. Print, copy and modify are off, accessibility stays on, and the owner password is random (≠ the open password).
  - Printing only (E): /P −2056. Print is off, the rest is on.
- **No options ticked (A, C, D):** /P −3904, the deny-all flag set, with owner password = open password. Readers that authenticate as owner get full rights. This depends on owner = user; explicit "allow all" flags would be safer (P3, real-reader behaviour unverified).
- **Producer metadata:** Producer is rewritten to "FreeDailyPro". Title, author and Creator are kept, as the Limitations say (Producer is not mentioned, P3).
- **Re-downloads:** each Download of the same result gives different bytes (new /ID and ciphertext, same size and content). Harmless.
- **"Created with FreeDailyPro.com" mark:** none appears in the output content streams. The cap dialog says passes remove the mark "from your PDFs" (P3 copy for this tool).
- **Batch:**
  - 5 files → ZIP of 5 AES-256 PDFs, one password.
  - 6 files → toast "1 file left out — A batch takes up to 5 files on the trial. A paid plan removes that limit."
- **Timing:** 3–50 page files take 0.5–1.2 s. A 52 MB file gets a soft-warning toast, then protects in 4.7 s (no hard cap; matches "over 50 MB may take longer").

## Input handling (`json/cases-chromium.json`, `json/unlock.json`)
- **Self-check:** the "Checked: opens with your password · N pages · size · AES-256" line appears every time (PASS).
- **AES-256 user-password PDF (P04):**
  - Dialog "This PDF is password-protected".
  - Wrong password → "That password didn't work"; the right one → "Unlocked", then re-protected with the new password (PASS).
  - The dialog says "your result won't have a password", which is wrong for this tool: the result gets the new password (P3).
- **RC4 user-password PDF (P09):** same flow (PASS).
- **Cancel on the unlock dialog:**
  - The inline alert reads "Unlock it with Unlock PDF first".
  - The toast says "it's in your list, locked. Use Unlock on its row". One-file mode has no list or row (P3).
- **Owner-only restricted PDF (P05):** silently "Unlocked" without the owner password, so the original author's restrictions are dropped. That's common across the industry, but it isn't disclosed (P3 policy note).
- **Corrupt PDF / text renamed .pdf:** "can't be read — it looks damaged. Try the Repair PDF tool" (PASS; for a non-PDF, "not a PDF" would be more accurate, P3).
- **Password checks:**
  - Fewer than 6 characters → "Use at least 6 characters", button disabled.
  - Mismatch → "Passwords don't match", button disabled.
  - "letmein" / "aaaaaaaa" → "Weak (very common)" but still allowed (by design).
  - A leading space shows the space note. Show/Hide toggles both fields. Reset clears.
- **Firefox:** L01, L09 and L15 behave the same as in Chromium.

## Privacy (PASS, `json/privacy.json`)
- Across 225 requests there are 22.5 KB of POST bodies, all analytics/ads. None contains the marker password, the PDF title or `%PDF`.
- Nothing is in localStorage, sessionStorage, IndexedDB or cookies. After a reload the file and password are gone.
- Share copies only the tool URL (`json/share.json`).

## Trial use, gate and payment (`json/gate.json`)
- **Uses-left context** (1st fresh context, `usageToday` 0), 02:11:17–02:14:18 EST:
  - Protect is free (0 → 0).
  - Download A: 0 → **1**. Same file again (A2): 1 → 1.
  - Save to Google Drive → Google sign-in popup; Save to my cloud storage → "Sign in with your email first… $4.99 per month, 1 GB" (both stopped).
  - New + P01 with all blocks (B): 1 → **1**. New + P03 (C): 1 → **1**. New + P02 (D): 1 → **1**. So **three more protected PDFs downloaded free in the same page load**.
  - Reload + P02 (E): 1 → **2**.
  - Reload + batch of 5:
    - Run: 2 → 2.
    - Per-file Download 1: 2 → **3**.
    - Per-file 2: 3 → 3. ZIP: 3 → 3.
  - Reload + batch of 6 (5 kept): file 1 3 → 4, file 2 and ZIP free.
  - End: 4. **Trial uses spent: 4** (display-only).
- **Verdict:** one trial use per page load, so later Downloads are free until reload. Under Santosh's Nov 20 every-Download decision this is a **P1 gate gap**. The ZIP is never charged on its own: "counts as one use" holds, but only because the first per-file download already paid.
- **At 0** (`zero`, 02:14:22 EST):
  - Protect still works and shows the Checked line. No preview, blob, iframe or embed of the result exists (only ad iframes), so **there is no full-quality preview leak** (PASS).
  - Download → cap dialog "Today's trial uses are done … Monthly $4.99 … Day Pass $1" → Buy Day Pass → "Day Pass, $1 … Email | Continue to payment" (stopped).
  - Batch at 0: per-file Download and ZIP → the same cap dialog (blocked, PASS).
  - Quick Buy day → email prompt; Quick Buy monthly → Stripe Checkout (session id redacted; stopped).
- **Keyboard:** Tab ×30 + Enter on the drop zone opens the chooser (PASS).
