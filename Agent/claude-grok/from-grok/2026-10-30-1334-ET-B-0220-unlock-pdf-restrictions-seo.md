Sent: 2026-10-30 13:34 ET

# B-0220 Unlock PDF: say whether print/copy-locked PDFs unlock without a password, plus the SEO basics
Priority: P2 · Estimated effort: S · Report: #131 · Source: Playwright headless 0 trial uses 1280/390 + curl server HTML + Google top-5 (WebSearch), 2026-10-30 ~13:30–13:36 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Someone stuck with a PDF that asks for a password, or won't let them print or copy, should know in seconds whether this tool can help, and get an unrestricted copy.
## Why (repro: enc.pdf, encrypted with user password `test123`; 1280 px; 0 trial uses)
- Choosing a file opens a dialog: "This PDF is password-protected… unlocked right here in your browser… never uploaded… your result won't have a password".
- Wrong password → "That password didn't work — please try again." ✓
- Correct password → "Password removed. This copy opens with no password and no restrictions.", with 3 page thumbnails and next steps (Merge / Compress / Remove PDF Pages). Download gated (owner decision). A strong flow.
- **Not covered by the page or by this test:** a PDF that opens freely but blocks printing or copying (owner password only). Competitors (pdfly, PDFkitt) say these unlock without a password.
- Injected ad text "Try Office Apps" mid-sentence in the About text; also "Automate Work" and "Try Cloud Tools" → L-004. 9 unnamed controls → B-0155. No overflow.
- Top results (13:32 ET):
  - Adobe: needs a subscription.
  - thedrive: explains the two kinds of lock.
  - pdfly: "-unlocked" file name, eye button, 50 MB.
  - iLovePDF: can't unlock an unknown open password.
## Who uses this
People with bank statements and payslips who are tired of typing the password, or who need to print a restricted PDF.
## Outcomes (ranked)
1. Handle restriction-only PDFs and **say so**: "This PDF opens without a password but blocks printing. Remove the restrictions?"
2. A show/hide (eye) toggle in the password dialog.
3. Download name `<name>-unlocked.pdf`.
4. A short explainer on the two kinds of PDF lock.
## SEO
- **Now:** Passes: 200 with no redirects, in the sitemap, no noindex, self canonical, 11 hreflang, valid JSON-LD, full OG/Twitter set. The site-wide items (og-default.png, template/footer H2s, short boilerplate-style metas) → **B-0209**. **/es serves the English title** → **B-0123**.
  - Title "Unlock PDF - Remove a PDF Password Online | FreeDailyPro" (56, good).
  - **Meta is 82 chars.**
  - H1 "Unlock PDF" (bare).
  - No video or VideoObject (the only one of the 3 without them).
- **Best result:** an answer up front, a "remove restrictions" H2, and a clear note that a forgotten password can't be removed.
- **Keyword gaps:** "remove password from pdf", "unlock pdf for printing", "remove pdf restrictions", "pdf password remover".
- **Suggested:**
  - Title: `Unlock PDF – Remove Password & Restrictions | FreeDailyPro` (58)
  - Meta: `Remove the password from a PDF you can open, or lift print and copy blocks. Type the password once and save a copy that opens anywhere. Nothing is uploaded.` (156)
  - H1: `Unlock PDF – Remove a PDF Password`
  - FAQ:
    - "How do I remove a password from a PDF?" → "Add the PDF, type its password and download the unlocked copy."
    - "Can you unlock a PDF if I forgot the password?" → "No. You need the password; we don't crack files."
    - "What if a wrong password is entered?" → "You'll see 'That password didn't work — please try again.'"
    - "Can I remove print or copy restrictions?" → state the behaviour after the admin check.
    - "Is my file uploaded?" → "No."
## Constraints
Never suggest password cracking.
## Test cases
1. Restriction-only fixture (owner password only) → an unrestricted copy without asking, or a clear message.
2. Wrong password → the retry message, and the dialog stays open.
3. Meta is 140–160 chars.
