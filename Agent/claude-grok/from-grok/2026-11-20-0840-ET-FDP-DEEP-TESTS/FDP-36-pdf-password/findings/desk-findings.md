Sent: 2026-11-21 02:24 ET

# FDP-36 Add Password to PDF: desk findings (2026-11-21 02:07–02:20 EST)

## Page and SEO
- **Basics:** 200, canonical self, in the sitemap with `/blog/pdf-password`, no pair pages.
- **Title and meta:** title "Password Protect a PDF Online - AES-256 | FreeDailyPro" (good keyword fit). The meta description is only 67 characters, "Add real password protection to a PDF, right in your browser. Fast." (P2: too short, no AES-256, batch or no-upload).
- **Headings and JSON-LD:**
  - H1 "Add Password to PDF".
  - JSON-LD: WebSite, SoftwareApplication (Offer 4.99), VideoObject, FAQPage with **13** Q&As, BreadcrumbList.
  - og:image is the generic og-default.png.
- **Locales:** es…id return 200 with a translated H1 (client-side), but title and meta stay English. ja desktop is 1369 px on a 1366 px window (3 px). `/ar` is 404.
- **Naming:** "Add Password to PDF" (page), "Add PDF Password" (video, old UI), "PDF Password" (blog).

## Copy vs behaviour (contradictions, live-verified)
- **FAQ "Can I remove a password from a PDF that already has one? Not with this tool… no 'unlock' mode… even if you know it":**
  - The tool's own drop step unlocks a protected PDF when you type its password (`json/unlock.json`).
  - A separate Unlock PDF tool exists, and this page's alert links to it. The FAQ sends users away from both (P2).
- **Unlocking already-protected files:** the FAQ says "Can I protect a PDF that's already password-protected? Yes… unlocked in your browser first" (true, live). Limitations say "an already encrypted PDF cannot be loaded here" (false) (P2).
- **Block options:** the FAQ says "Does the password protect against editing…? Just opening… It doesn't separately restrict printing, copying, or editing". The same page offers "Also ask readers to block: Printing / Copying text / Editing", and the outputs carry those flags (B, E) (P2).
- **Header count:** "Search 300+ tools" (header), "300+ professional tools" (blog), "200+ Free Productivity Tools" (video end card) (P3).
- **Accurate:** AES-256, the Checked line, the 6-character minimum, the strength bar, the spaces note, the batch of 5 counted as one use, file name and metadata kept, and nothing uploaded.

## Blog `/blog/pdf-password` ("Password a PDF Before It Leaves Your Desk", Oct 17 2026)
- Good process advice (separate channel, assemble then protect, test on a phone).
- It's generic: no AES-256, no Checked line, no block options, no batch; it calls the tool "PDF Password".
- "Protecting five separate files multiplies password chaos" ignores the batch feature, which uses one password.
- PARTIAL (accurate, but doesn't teach the tool).

## Code notes (`evidence/js/`)
- **`PdfPassword-*.pretty.js`:** Protect → `operations.a` (pdf-lib `encrypt`, AES-256, random 24-byte owner password only when a block box is ticked) → `operations.v` self-check (pages, title, field names) → Download through the shared gated `D` button. Batch → `BatchRunner` (cap `batch.b`: 5 trial / 100 paid), per-file and ZIP via `ToolPage.vt` → `index DI` gate.
- **`operations-*.pretty.js` lines ~2880–2970:** encryption, permissions map, self-check.
- **Per-page-load counting:** shared `index-B1CTyGtY.js` `RA`/`xI` with the set `Kt` (excerpt shipped), so `DI` lets any download through once the tool is in `Kt`.

## Completeness vs competitors (desk; Acrobat online, Smallpdf, iLovePDF, PDF24 offer similar AES protection; not re-verified live)
- **Strong:**
  - true in-browser AES-256 with a verified result
  - unicode passwords
  - batch with one password
  - unlocks protected inputs inline
- **Gaps (live UI has no control for these):**
  - no separate permissions (owner) password
  - no metadata removal or rename-on-protect
  - no generate-a-strong-password button (FDP has a Password Generator tool; could link it)
  - no per-file passwords in batch
