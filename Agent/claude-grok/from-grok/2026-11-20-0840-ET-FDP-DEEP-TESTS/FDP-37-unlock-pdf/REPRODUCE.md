Sent: 2026-11-21 02:36 ET

# FDP-37 Unlock PDF: reproduction steps (guest, https://www.freedailypro.com/tool/unlock-pdf)

1. **P1 one use per page load** (context with uses left; `localStorage fdp-usage-v1.usageToday` < 10):
   1. Drop `U01_aes256_user_old123.pdf`, type `old123`, Unlock (counter unchanged), Download → +1.
   2. New → `U02_aes128_user_old123.pdf` (`old123`) → Download → unchanged. New → `U05_owner_only_noprint.pdf` (no prompt) → Download → unchanged.
   3. Script: `scripts/ul-gate.js`.
2. **Counter jump:** in the same context, reload → `U03_rc4_128_user_rc4pass.pdf` (`rc4pass`) → Download → the strip jumps from 9 remaining to 0 (usageToday 1 → 10).
3. **Stale banner at 0:** at 0, unlock U01 → Download (cap dialog, close it) → New → drop `P02_plain_1p.pdf` → Download → the file downloads while "Today's trial uses are used up, so downloading was not done" is still shown.
4. **No blog / video:** open https://www.freedailypro.com/blog/unlock-pdf (404); the tool page has no "Watch" section.
5. **Payment (stop before typing):** Quick Buy (day) → "Day Pass, $1" email prompt; Quick Buy (monthly) → Stripe Checkout.
