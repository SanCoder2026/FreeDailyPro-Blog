Sent: 2026-11-20 08:40 ET

# FDP-21 Sign PDF: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | P1 | FAQ, Limitations and blog say other-party fields are not fillable in other readers; output has real /Tx form fields and About/toast/note say any reader works; "rather than a plain unverified text box" is untrue outside this tool | S02 `testfiles/out-S02.pdf`, `findings/desk-findings.md` | One consistent, true explanation everywhere |
| 2 | P1 | Fields can only be placed by pointer click/tap on a non-focusable canvas | `json/gate-kbd.json` kbdPlace | Keyboard placement (focusable preview + arrows, or X/Y/page inputs) |
| 3 | P1 | Video: "FREE", "10 free uses daily", "Pro", 0-uses banner, old UI, no final download, mid-video subscribe cut | `screens/video/*` | Re-record today's Premium flow with trial-use wording |
| 4 | P2 | Six style buttons all named "Jane Q. Public"; draw pads unnamed; radios lack `name` | gate names | `aria-label` "Flowing style" etc.; label canvases; group radios |
| 5 | P2 | No live region; success/errors only as toasts | gate liveRegions | `role=status` for "Signed PDF downloaded" and errors |
| 6 | P2 | Phones: field table overflows; Download at y≈2635 px on iPhone SE | gate iphone-se | Stack table rows; sticky Download on phones |
| 7 | P3 | Date/Full Name preview text nearly invisible | `screens/live/pre-S01.png` | Darker preview ink |
| 8 | P3 | Auto signature mixes script font with plain CJK glyphs | `screens/pdf/s13-s05.png` | Note or fall back to drawn/typed |
| 9 | P3 | Owner-restricted PDF output loses its restrictions (toast "Unlocked") | S14 | Say restrictions are removed |
| 10 | P3 | First paint shows "2 remaining" before syncing to 0 | probe vs expanded copy | Render after sync |
| 11 | P3 | FAQ audit text ("signer count") differs from the record page | desk | Align |
| 12 | P3 | /es title/meta English; /ar 404; ja desktop 3 px overflow; 9 px header overflow at 320 px | matrix | Localise; site-wide fixes |
| 13 | P3 | tools.csv lists share/save/copy/print; tool offers only Download | gate resultButtons | Update the catalogue or add the actions |
| 14 | P3 | Cap dialog mentions removing a mark that this tool's trial output doesn't have | dialog text | Tool-aware dialog copy |
| — | untested | S11 existing AcroForm preservation | — | Run `sp-battery.js S11` in a context at 0 |
