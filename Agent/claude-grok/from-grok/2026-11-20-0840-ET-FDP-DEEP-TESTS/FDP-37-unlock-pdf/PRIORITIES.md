Sent: 2026-11-21 02:36 ET

# FDP-37 Unlock PDF: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | **P1** gate gap | Only the first Download per page load costs a trial use. After A (0→1), the unlocked AES-128 file (B) and the owner-only file (C) downloaded free at 1. Conflicts with Santosh's Nov 20 every-Download decision. | `json/gate.json` (02:25:21–02:27:17 EST); `js/index-B1CTyGtY.excerpt-usage.js` | Count each unlocked Download in the shared hook (keep unprotected pass-through free if Santosh agrees). |
| 2 | P2 | The local counter jumped 1 → 10 at the first Download after a reload (display-only; likely server reconciliation). The user sees "0 remaining" with no explanation. | `json/gate.json` `dlE` | Reconcile on load, not on Download, or explain in the strip. |
| 3 | P2 | No blog post (`/blog/unlock-pdf` 404) and no video (no Watch section; channel search none). | `findings/desk-findings.md`, `findings/video-findings.md` | Write the post; record a 60 s current-UI video. |
| 4 | P2 | SEO: meta 73 chars, FAQPage 5, no VideoObject, H1 "Unlock PDF" untranslated in 9 locales, English title/meta under hreflang, /ar 404, generic og:image. | `findings/desk-findings.md`, matrix | ~150-char meta; FAQs on RC4, owner-only, trial cost; translate head and H1. |
| 5 | P2 | Completeness: no batch / Several files; no "opens without a password" verification line. | live UI (`json/probe.json`) | Batch with one password; reuse Add Password's check pattern. |
| 6 | P3 | At 0, the stale "downloading was not done" banner while a pass-through file downloads; unprotected files uncounted (policy note); RC4 support not in Limitations; owner-only restrictions removed with no password (policy note); iPhone SE 9 px / ja 3 px; eye-button label mismatch; ad-caption contrast. | `json/gate.json` `zero`, `json/cases-chromium.json`, matrix | Clear the banner on New; mention RC4; keep ad slots reserved, fix caption colour. |
