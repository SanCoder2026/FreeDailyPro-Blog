Sent: 2026-11-21 11:52 ET

# FDP-58 Exhibit Stamper: priorities (2026-11-21 EST)

| Pri | Item | Why it matters | Suggested fix |
|---|---|---|---|
| P1 | One trial use per page load (13 stamping runs, 47 files = 1 use; 4 runs with 1 reload = 2 uses) | Gate gap by owner rule; a whole exhibit set and its re-stamps cost one use | Charge per Stamp of new content (hash files + settings) and re-check the cap on every run. Same fix as Bates Numbering (FDP-55). |
| P2 | Fake "Download" button ad creatives in the slot right under the result buttons and in the right rail | Users may click an ad instead of the real download; trust on a legal tool | Keep ads. Reserved, labelled slot away from the result buttons; block download-button creatives in the ad network. |
| P2 | Video bC9ON6zNcxo not embedded on the tool page (no VideoObject) | Lost SEO and onboarding | Embed it (site video map) like Bates Numbering. |
| P2 | Locale pages half translated: H1, subtitle, drop zone, FAQ stay English on es/de/ja/… | Mixed-language page | Translate tool strings (site-wide pattern). |
| P3 | Numbers "Start at 0" accepted but outputs Exhibit 1 | Silent wrong label | Allow 0 (`Number.isNaN` check) or validate "1 or more". |
| P3 | Default Top right covers a case header at the top margin (white box hides "Filed 11/21/2026") | Hidden docket text | Default Bottom right, or warn when the stamp overlaps text. |
| P3 | Non-Latin label drawn as a picture: not searchable; one PNG per page (12 pages ≈ 86 KB) | Exhibit labels get searched/cited | Text layer (ToUnicode) or a Limitations line; reuse one image XObject. |
| P3 | Two Save to Google Drive / Save to my cloud storage pairs on a one-file result, unlabelled | Which file is being saved? | Label "Save PDF to…" / "Save index to…", or one Save menu. |
| P3 | Limitations "Locked PDFs have to be unlocked first" vs the inline unlock dialog | Copy undersells | Reword: "you'll be asked for the password; it's never uploaded." |
| P3 | Blog colour section vs black-only stamp; dark page + box off = near-invisible label | Expectation gap | Add a colour/white-text option, or a hint when the box is off. |
| P3 | Cap dialog promises removing a mark this tool never adds | Confusing upsell | Make the mark sentence conditional per tool. |
| P3 | exhibit-index.csv has no UTF-8 BOM | Excel likely mangles "Anlage A – 証拠"-style labels (not opened in Excel) | Write a BOM or offer .xlsx. |
| P3 | Page doesn't link Bates Numbering / Legal Production Desk (FAQ mentions Bates) | C11 discovery | Add cross-links. |
| P3 | Video "200+ professional tools" (live 300+), ~22 s outro of 70 s | Small staleness | Refresh at the next re-record. |
| P3 | axe: label-content-name-mismatch (serious), region; ad-caption contrast on Pixel 7; iPhone SE 9 px overflow, ja desktop 3 px | A11y/layout polish | Fix label and caption contrast (reserved slots kept); header overflow is site-wide. |
