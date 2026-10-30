Sent: 2026-10-30 14:09 ET

# B-0247 Password Generator: shorten title, real meta, say "crypto.getRandomValues" and add passphrases
Priority: P2 · Estimated effort: S · Report: #140 · Source: SEO backfill 7, curl server HTML + seo.py + Google top 5 (WebSearch), 2026-10-30 ~14:07–14:08 ET. Already tested (L-152).

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone wanting a strong password should trust ours: show it's generated on their device with the browser's secure random source.
## Why
- GA rank 33 (63 views, **11 s average engagement**, `analytics/2026-07-10-to-now-raw.md`): people grab a password and leave; no GSC row in the cited files.
- **Title "Generate a Secure Random Password Online - Free | FreeDailyPro" is 62 chars.** **Meta 79 chars.** H1 "Password Generator".
- Live JS (PasswordGenerator-BtEIKQwF.js, ~14:08 ET): crypto.getRandomValues with rejection sampling, Fisher–Yates shuffle, 0 Math.random. Good; the page should say so (PwdForge, KernelHost do).
- L-152: 20 chars, symbols toggle, Copy.
- **Top 5 offer (~14:08 ET):** passphrase mode (Bitwarden, 1Password); exclude look-alikes 0O1lI (PassGen, PwdForge); entropy/strength in bits (PwdForge); several passwords at once and settings link (PassGen); length 6–256.
## Who uses this
Anyone signing up for an account or rotating a password.
## Outcomes (ranked)
1. Title ≤ 60 and a 140–160 meta.
2. One line under the output: "Made on your device with crypto.getRandomValues; never sent."
3. Exclude look-alikes; entropy bits.
4. Passphrase mode.
## SEO
- **Now:** 200, sitemap, 11 hreflang, valid JSON-LD; → **B-0209**; /es English → **B-0123**.
- **Keywords:** "password generator", "strong password generator", "random password generator", "passphrase generator".
- **Suggested:**
  - Title: `Strong Password Generator – Random & Secure | FreeDailyPro` (58)
  - Meta: `Generate a strong random password on your device with the browser's secure crypto source. Pick length, symbols and numbers, then copy. Nothing is sent or kept.` (159)
  - H1: `Strong Random Password Generator`
  - FAQ: "Is it truly random?" → "Yes, crypto.getRandomValues with no bias." · "Is it stored?" → "No." · "How long?" → "16+ characters."
## Constraints
Keep generation fully client-side.
## Test cases
1. Title ≤ 60; meta 140–160.
2. Grep live chunk: getRandomValues ≥1, Math.random 0.
