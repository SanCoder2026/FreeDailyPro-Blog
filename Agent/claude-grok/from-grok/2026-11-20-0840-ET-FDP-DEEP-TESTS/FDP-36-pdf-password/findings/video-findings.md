Sent: 2026-11-21 02:24 ET

# FDP-36 Add Password to PDF: video findings

- **Video:** https://www.youtube.com/watch?v=qBJKvkcI298, "How to Use Add PDF Password – Free Step-by-Step Walkthrough".
  - Length **111 s**, uploaded 2026-09-24, 4 views at fetch (2026-11-21 02:10 EST).
  - Embedded as "How to Password Protect a PDF Online – Encrypt PDF". Description: "Try Add PDF Password free… Free daily uses".
- **Structure** (`video/sheet01-04.png`, 1 frame / 3 s):
  - Title card "PASSWORD PROTECT A PDF — FREE · PRIVATE · NO LOGIN", logo, wipe.
  - About 60 s of screen recording: Windows file dialog → "MSI-Sample.pdf" → one password field → Protect PDF.
  - Presenter "Subscribe" clip, end card "200+ Free Productivity Tools" (about 20 s).
- **Old UI, wrong security claim (`video/z33-dlg.png`, `z50.png`, `z62.png`):**
  - Page text reads "Adds password protection to a PDF using real **RC4 128-bit** encryption". Today's tool uses AES-256.
  - Single password field: no Confirm, no strength bar, no block options, no Checked line, no Several files.
  - Warning "this tool only adds protection, it doesn't currently support removing an existing password". The tool now unlocks inputs.
  - Chips "10 free uses daily", "Max file size: 50MB".
- **Privacy:** the file dialog shows only an "Assets" folder of sample PDFs. No personal folders were seen in the sampled frames (better than FDP-35).
- **Verdict:** FAIL for check 12. The video shows an older tool and tells viewers the encryption is RC4-128, the weak legacy cipher. For a security tool that undercuts trust (P2).
