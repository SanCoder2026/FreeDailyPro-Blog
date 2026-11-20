Sent: 2026-11-20 08:40 ET

# FDP-21 Sign PDF: live functional findings

Run 2026-11-19 17:05–17:23 EST (box `date`, ET), headless Chromium 1366×900 unless noted, one fresh guest context per case. Signing builds the PDF in memory and then calls the gated download; at 0 remaining the cap dialog opens, so the signed PDF was captured from the in-memory Blob (init-script hook) and inspected with pypdf / pdftoppm. Premium Application: 2 trial uses a day.

## Starting counts and Download cost
- Most fresh contexts: `usageToday` 2/2, "Trial: 2 uses/day · 0 remaining today". About 1 in 4 contexts loaded with 2 remaining.
- First paint shows "2 remaining today" before the count syncs to 0 (`html/tool-expanded.txt` strip vs `json/probe.json`) — display only.
- **Observed with uses left (17:14:47 EST, `json/battery-S01-spend.json`):** 1st Download Signed PDF → `signed-contract.pdf`, 11,935 bytes, identical to the in-memory PDF; count 0 → 1. 2nd Download of the same work → downloaded again, count stays 1. One use per signed document; no double charge. No "Created with FreeDailyPro.com" mark in the trial download (`testfiles/dl-S01-signed-contract.pdf`).
- Incidental: `sp-import.js` run 1 landed in a context with uses and its Download went through (not saved; count +1).
- At 0: Download → "Today's trial uses are done" → "Buy Day Pass — $3"… → "Premium Day Pass, $3 | Enter your email…" (stopped, nothing typed). Escape keeps name, fields and file (`json/gate-kbd.json`).

## Battery (`json/battery-S02_…json`, `battery-S06_S11_S15.json`, `import.json`, `otherparty.json`, `browsers.json`)
| Case | Input / action | Result | Verdict |
|---|---|---|---|
| S01 | contract.pdf; auto signature; Signature + Date + Full Name; signing record | 3 pages; signature image on the line, "11/19/2026", "Jane Q. Public"; record page with SHA-256 **matching** the input (4250f698…c048), "Signed at 2026-11-19 22:08:47 UTC (device time zone America/New_York)", marks list, honest "not a certified digital signature" note | PASS |
| S02 | 1 own Signature + Signature and Date for **Other party** | own signature stamped; other-party fields are **real AcroForm text fields** `fdp_signature_1_other` (/Tx, tooltip "Sign here") and `fdp_date_2_other` (/Tx) — fillable in any PDF reader | Works as UI says; **contradicts FAQ, Limitations and blog** (P1) |
| S02b | open out-S02.pdf again as the other party | toast "2 fields are waiting for you — they're already placed. Set up your signature, then download."; both fields pre-placed; output has both signatures, form fields consumed | PASS |
| S03 | Initial, All pages | "JQP" on both pages | PASS |
| S04 | rotated page 2 (/Rotate 90) | signature upright as displayed | PASS |
| S05 | drawn signature (mouse) | stamped zig-zag | PASS |
| S06 | imported transparent PNG / white JPG via "Choose image" | accepted; Download proceeds to the gate | PASS (`json/import.json`) |
| S07 | no name, Draw manually, nothing drawn | inline "Set up your signature first (above the field list)." | PASS |
| S08 | field not placed | inline "Place all fields on the page first (1 not yet placed)." | PASS |
| S09 | password PDF | dialog "This PDF is password-protected… unlocked right here in your browser" | PASS (unlock not exercised) |
| S10, S15 | text file / truncated PDF | toast "can't be read — it looks damaged. Try the Repair PDF tool" | PASS |
| S11 | existing AcroForm PDF | not run (every attempt landed in a context with uses; skipped to save them) | untested |
| S12 | DD/MM/YYYY | "19/11/2026" | PASS |
| S13 | name "José Ñúñez 山田太郎", non-Latin PDF | Full Name drawn correctly; auto signature mixes script font (Latin) with plain CJK glyphs | P3 |
| S14 | owner-password-restricted PDF | toast `Unlocked "K_owner_only_restricted_2p.pdf"`; output has no restrictions | P3 (disclosed by toast) |
| S16 | Signature on page range 2-3 + record | stamped on pages 2 and 3; record page 4 | PASS |
| FF/WebKit | auto signature, Signature + Date | both placed, PDF built (10,622 / 10,299 bytes), cap dialog; no crash | PASS |
| metadata | — | Producer/Creator set to "FreeDailyPro"; original Author/Subject kept; Title "Signed contract" | info |

## Keyboard, screen reader, phones (`json/gate-kbd.json`)
- Drop zone reached in 29 Tabs; Enter opens the chooser.
- **A field cannot be placed without a pointer.** The preview `<canvas>` is not focusable (tabIndex −1, no role/name); the "Click page to place" table button only arms a pointer click; there are no X/Y inputs. Keyboard-only and many screen-reader users cannot finish signing.
- The six signature-style buttons all have the accessible name "Jane Q. Public" (the style name is only in `title`); the two draw pads are unnamed canvases; the radio groups have no `name` (arrow keys don't move within a group); no live region (`liveRegions: []`); axe after placing fields: `empty-table-header` (minor). axe idle and after upload: clean.
- Phones: tap placement works (iPhone SE, Pixel 7). The field table overflows its container; Download Signed PDF sits at y≈2635 px (iPhone SE, viewport 609) and y≈2528 px (Pixel 7).
- Placed Date / Full Name boxes show their text in very faint ink in the preview (`screens/live/pre-S01.png`).
