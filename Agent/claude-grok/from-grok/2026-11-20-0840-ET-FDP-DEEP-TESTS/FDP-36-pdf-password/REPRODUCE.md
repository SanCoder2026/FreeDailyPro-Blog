Sent: 2026-11-21 02:24 ET

# FDP-36 Add Password to PDF: reproduction steps (guest, https://www.freedailypro.com/tool/pdf-password)

1. **P1 one use per page load** (context with uses left; `localStorage fdp-usage-v1.usageToday` < 10):
   1. Drop `P01_payslip_3p_form.pdf`, type `Tr1al-Horse-42!` twice, Protect PDF (counter unchanged), Download → +1.
   2. Click Download again → unchanged.
   3. New → `P01` + tick all three block boxes → Protect → Download → unchanged.
   4. New → `P03_50pages.pdf` → Download → unchanged. New → `P02_plain_1p.pdf` → Download → unchanged.
   5. Reload → `P02` → Download → +1.
   6. Reload → Several files → B1–B5 → Protect all → download row 1 → +1. Row 2 and Download all (ZIP) → unchanged.
   7. Script: `scripts/pp-gate.js`.
2. **FAQ vs unlock:** drop `P04_already_userpw_old123.pdf` → "This PDF is password-protected" → type `old123` → Unlock → Protect works. Compare with FAQ "Can I remove a password…? … no 'unlock' mode … even if you know it" and Limitations "an already encrypted PDF cannot be loaded here".
3. **FAQ vs block options:** tick Printing → Protect → Download → `pikepdf.open(f, password=…).allow.print_highres` is False (`/P −2056`). Compare with FAQ "It doesn't separately restrict printing, copying, or editing".
4. **Video:** https://www.youtube.com/watch?v=qBJKvkcI298 at ~0:33 (page text "real RC4 128-bit encryption") and ~1:02 (single field, "doesn't currently support removing an existing password").
5. **Cancel toast:** drop `P04`, click Cancel → toast "it's in your list, locked. Use Unlock on its row" with no list on screen.
6. **No-options permissions:** protect with no boxes ticked → `/P −3904` (all off) with owner = open password (`scripts/verify.py`).
7. **Payment (stop before typing):** Quick Buy (day) → "Day Pass, $1" email prompt; Quick Buy (monthly) → Stripe Checkout.
