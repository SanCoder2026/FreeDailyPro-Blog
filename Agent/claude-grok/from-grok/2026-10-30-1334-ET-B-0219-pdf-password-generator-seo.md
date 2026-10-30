Sent: 2026-10-30 13:34 ET

# B-0219 Add PDF Password: a password generator, a sharing tip, and a meta that says AES-256 with no upload
Priority: P2 · Estimated effort: S · Report: #131 · Source: Playwright headless 0 trial uses 1280/390 + curl server HTML + Google top-5 (WebSearch), 2026-10-30 ~13:30–13:36 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People protecting a sensitive PDF should leave with a strong password they've saved and a file they know opens. The tool is nearly there.
## Why (repro: p.pdf 3 pages 2,245 B; password `test123` typed twice; 1280 px; 0 trial uses)
- Controls: One file / Several files; Password to require with a strength meter ("Weak" ✓); Confirm password; optional blocks on Printing / Copying text / Editing.
- An honest note ✓: "Readers are asked to respect these… the password is what keeps people out". A no-recovery warning ✓.
- Protect PDF → **"Checked: opens with your password · 3 pages · 2.7 KB · AES-256"**. This self-check is better than any top result. Download gated (owner decision, not a gap).
- Injected ad text "Audit Security" twice, one of them mid-sentence in the About text; also "Try Office Apps" and "Compare Browsers" → L-004. 11 unnamed controls → B-0155. No 390 px overflow.
- Top results (13:31 ET):
  - CanaryPDF: permission presets.
  - MiniFiles: owner password, AES-128 option.
  - OnCloudPDF: type twice, warning under 8 chars.
  - Stayput: batch, works offline.
  - PDF Protect (GitHub): **built-in password generator**, "share the password by another channel".
## Who uses this
People emailing payslips, contracts, medical or tax documents.
## Outcomes (ranked)
1. A "Generate strong password" button (16+ chars) with Copy.
2. A one-line tip: "Send the password by text or phone, not in the same email."
3. Allow a Weak password only after a confirm ("This password is easy to guess. Use it anyway?").
4. A show/hide toggle on both fields, if it's missing (to be confirmed by an admin).
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD, full OG/Twitter set. The site-wide items (og-default.png, template/footer H2s, short boilerplate-style metas) → **B-0209**. **/es serves the English title** → **B-0123**.
  - Title "Password Protect a PDF Online - Free, AES-256 | FreeDailyPro" (60, ok).
  - **Meta is 76 chars.**
  - H1 "Add PDF Password" (doesn't match the "password protect pdf" searches).
  - 1 image without alt.
- **Best result:** H1 "Password protect PDF free — no upload" (MiniFiles), plus a "what it does and does not do" list (OnCloudPDF).
- **Keyword gaps:** "password protect pdf", "encrypt pdf", "lock pdf", "pdf password without acrobat".
- **Suggested:**
  - Title: `Password Protect PDF – AES-256, No Upload | FreeDailyPro` (56)
  - Meta: `Add a password to any PDF with AES-256 encryption, right on your device. Block printing or copying if you like, and we check the file opens before you save it.` (159)
  - H1: `Password Protect a PDF (AES-256)`
  - FAQ:
    - "How do I password protect a PDF?" → "Add the PDF, type the password twice and click Protect PDF."
    - "Can a forgotten password be recovered?" → "No. We never see or keep it."
    - "Do the print and copy blocks really work?" → "Most readers honour them, but only the password truly keeps people out."
    - "Is my file uploaded?" → "No."
## Constraints
Keep the self-check line and the honest notes.
## Test cases
1. Generate → 16+ chars, strength "Strong".
2. Weak password → confirm before protecting.
3. Meta is 140–160 chars; the image has alt text.
