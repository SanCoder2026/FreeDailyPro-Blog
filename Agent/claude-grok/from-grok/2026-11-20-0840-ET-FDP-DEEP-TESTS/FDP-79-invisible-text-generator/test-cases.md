Sent: 2026-11-21 18:03 ET

# FDP-79 test cases

Clipboard read back in Chromium through a same-origin helper tab; code points checked.

| ID | Action | Expected | Result |
|---|---|---|---|
| X01–X07 zero (Chromium 10/10) | Copy ×2, Hangul ×10, ZWSP ×50, Line Break ×500, reload + Copy ×2 | Counted or gated (owner) | **All copied, 0 POSTs (owner question)** |
| X01–X07 left (Firefox 0/10, try 20) | Same | — | **0 POSTs, stays 0/10** |
| V01–V09 | Each variant ×5 → Copy | Right code point ×5 | PASS (U+2800, 3164, 200B, 200C, 200D, 2060, 2063, 2003; Line Break = U+2800 U+000A ×5) |
| N01 / N02 / N08 / N12 | 0 / 501 / 999999 / 500 | 1 + note / 500 + note / 500 + note / 500 | PASS |
| N03 / N06 / N11 | empty / abc / １２ → Copy | Copies 1 (note says so) | **Click lost, nothing copied (P2)** |
| N04 / N05 / N07 | 2.5 / -3 / 1e2 | Reject or note | 25 / 3 / 12 silently (P3) |
| N09 | 007 | 7 | **107 (P3)** |
| N10 | " 4 " | 4 | PASS |
| S01 / S02 | Slider after 50 / End | — | 50 shows 20, ArrowLeft → 19 (P3) / max 20 |
| T01 | Copy Hangul ×5, paste in Test box | 5 × U+3164 | PASS |
| T02 / T03 | Mixed text / 60 blanks | Code points | PASS (emoji = 1 code point; list truncated at 40 with …) |
| K01 | Keyboard Enter on Copy | Copies | PASS |
| SH | Lost-click on 4 engines | — | Chromium, Firefox, Pixel 7 lost; iPhone 14 tap OK |
| NC | Clipboard refused | Usable fallback | **Toast asks to select text that isn't on the page (P2)** |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | iPhone SE 9 px; locales English (P2) |
