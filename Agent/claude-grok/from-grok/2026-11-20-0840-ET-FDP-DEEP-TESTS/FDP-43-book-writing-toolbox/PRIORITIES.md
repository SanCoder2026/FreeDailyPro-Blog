Sent: 2026-11-21 04:56 ET

# FDP-43 Book Writing Toolbox: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Suggested direction |
|---|---|---|---|
| P1 | Previews are close to full quality at 0 trial uses. The PDF mark is one tiling-pattern fill **under** the content (removable); the .docx mark is one header line | verify.json, screens/cases/B01-pattern-emptied-pages.png, outputs/*preview* | Draw the mark over the content in every page's stream (or rasterise/lower-resolution previews); put the docx mark in the body, or make it a sample |
| P1 | `renderEpub` returns 500 on 11/11 calls; Pre-flight drops the EPUB checks silently | json/responses/*renderEpub*.json, C01/C07 | Fix the EPUB build; Pre-flight shows "EPUB check couldn't run". Confirm the signed-in Export (possible P0) |
| P1 | Per-page-load charging: manuscript .docx preview and ONIX take a Professional trial use once per page load | cases3 D02, cases2 C08 | Save previews/ONIX with `{free:true}` (or the product's own rule) |
| P1 | At 0 trial uses, manuscript .docx preview and ONIX silently do nothing | cases3 D01, D01.png | The same fix; never fail without a message |
| P2 | Video shows the old "Book Maker" with "10 free uses daily", a personal macOS file picker and "no account needed" | video/sheet*.png, f20/f52/f107 | Re-record the current Toolbox on a clean profile |
| P2 | FAQ/Limitations say Bengali, Tamil, Telugu, Gujarati, Kannada and Malayalam aren't supported; the live checker says they are | tool-expanded.txt, B09 | Align the copy with the code |
| P2 | "Save book project" saves metadata only (no chapters), next to the "Erase everything … no other copy" warning | outputs/B11-save-*.book.json | Add a full local backup or rename it "Save book details" |
| P3 | Preview dialog has two close buttons; sidebar front-matter rows overlap after scrolling | B01.png, B07c.png, D01.png | UI fix |
| P3 | iPad Mini 8 px, iPhone SE 9 px, /ja 3 px overflow; mobile selects truncated | matrix-results.json | Layout fix |
| P3 | axe: button-name critical ×19, label critical ×1, ad-caption contrast | matrix-results.json | aria-labels; caption contrast (reserved slots kept) |
| P3 | Old name "Book Maker" in the OG image, VideoObject name and translated H1s; locale titles English; /ar 404 | tool.html, matrix | Rename assets and translations |
| P3 | Not listed on the Publishing & Print Makers category page; blog says the "group sits under PDF tools" | SITE-MAP, blog | List it; fix the blog line |
| P3 | Arabic book: English copyright boilerplate set RTL (punctuation flips) | wm/C04-arabic-rtl-preview-pages.png | Localise or isolate the boilerplate direction |
| P3 | The same 18 trims for Default and IngramSpark vs "filters the list" (unverified) | C03 | Check the platform filter |
| P3 | On /profile an ad overlays the sign-in card | B03b.png | Reserved slot outside the form |

- **RERUN-AFTER-RESET:** none (nothing pending a reset).
- **Sign-in-only, untested:**
  - https://www.freedailypro.com/profile (Start 7-day trial → sign-in → trial/Stripe).
  - The clean Download / Export EPUB / Export Manuscript / print cover for subscribers.
