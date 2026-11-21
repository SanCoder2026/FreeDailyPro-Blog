Sent: 2026-11-21 14:42 ET

# FDP-66 test cases

| ID | Input / action | Expected | Result |
|---|---|---|---|
| A01–A07 | 10/10: type, Copy, Save, Print, Ctrl+C, new string+copy, reload+save | Gate or count | All work, 0 POSTs (Owner question) |
| B01–B07 | 0/10: same | Counted | 0 POSTs, stays 0/10 (Owner question) |
| C-iphone | iPhone iOS 17.4 | Mobile Safari, iOS 17.4, Mobile | PASS |
| C-ipad13 | iPadOS desktop UA | Reads as Mac (expected) | PASS |
| C-androidReduced | Chrome Android reduced | Android 10, Device K | PASS (P3 hint) |
| C-samsungTab | SM-X710 | Tablet | PASS |
| C-pixel8Old | Pixel 8 Pro | Pixel 8 Pro | PASS |
| C-edgeWin | Edge NT 10.0 | Windows 10/11 | "Windows 10" + note (P2) |
| C-firefoxMac / C-win7ie | Firefox Mac, IE11 Win7 | Correct | PASS |
| C-googlebot … C-facebook | 8 bots/clients | Bot Yes | PASS (GPTBot/Googlebot labels P3) |
| C-smartTV | Tizen TV | Smart TV | "Smarttv" (P3) |
| C-logLine | Full access-log line | UA extracted | PASS |
| C-secChUa / Win11 | Sec-CH-UA headers | Parsed | PASS; FAQ says No (P2) |
| C-garbage | Random text | Error message | PASS |
| C-empty | Empty box | Blank or prompt | Own UA, Bot No (P3) |
| H-hints | Use My Browser's UA, Chromium / Firefox | Hints / note | PASS |
| M | 10 devices, 10 locales + /ar, 6 geo, axe | Usable | PASS (P2/P3 above) |
