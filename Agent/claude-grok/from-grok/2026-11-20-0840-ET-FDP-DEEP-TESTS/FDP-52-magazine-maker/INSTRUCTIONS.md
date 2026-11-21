Sent: 2026-11-21 09:19 ET

# FDP-52 package: how to use it

1. **Read first:** REPORT.md (intent, evidence, 22 checks), then PRIORITIES.md.
2. **Reproduce:** REPRODUCE.md has guest steps.
   - Inputs are in `evidence/testfiles/`, built by `make52.py`: articles, pictures, cover, logo, .docx (LibreOffice), PDFs, a password PDF (u123), a damaged PDF, WebP, and bad JSON files.
3. **Retest** from `tools-env` with `env -u BROWSER node …`:
   - `px52-live.js zero`: at the cap (both modes, templates, files, dialogs, passes).
   - `px52-live.js left3`: per-export charging.
   - `px52-live.js left4`: Combine download.
   - `px52-live.js subset firefox|webkit`.
   - `px52-wk.js webkit`: gate plus Combine crash isolation.
   - `px52-focus.js`: result area, templates, WebP.
   - `px52-overflow.js`: phones.
   - The `left*` modes retry fresh contexts until one has Premium uses left.
4. **Outputs:** in `evidence/outputs/`. Renders are in `evidence/screens/render/` (page sheets, page-6 crops).
5. **Video evidence:** in `evidence/video/` (frame sheets, crops, info.json).
6. **Rules:** guest only, no sign-in, stop at the email prompt or Stripe, no ad clicks. Times are EST from the box `date`.
