# B-0013 Mobile overflow and mobile download gaps
Priority: P2      Estimated effort: 50 min

## Goal / why
Mobile users can't reach controls or get files.

## What to change
- Horizontal overflow at 390/360px: https://www.freedailypro.com/tool/font-pairing-tool Preview/Copy rows (docW 423–446), https://www.freedailypro.com/tool/mockup-generator device toggles after Phone (433–449), https://www.freedailypro.com/tool/sprite-sheet-tool mode tabs (410–423), https://www.freedailypro.com/tool/stl-ascii-binary-converter Convert row on Android (379), https://www.freedailypro.com/tool/onix-generator (362). Wrap or scroll chip rows.
- https://www.freedailypro.com/tool/sprite-sheet-tool Combine 'Open / Save Sprite Sheet' relies on File System Access; add a plain 'Download PNG' like Split's ZIP.
- https://www.freedailypro.com/tool/onix-generator .xml download often empty on mobile Chromium; use a standard <a download> blob fallback.

## Acceptance criteria
- No horizontal scroll on the listed tools at 390 and 360 (pre and post result).
- Sprite combine and ONIX XML download a file on iPhone/Android viewports.
- Verify live after Railway deploy (~12–16 min) and report as `live and checked`.

## Not in scope / do not decide
Visual redesign.
Standing rules: Premium Applications = 2 trial uses/day (one shared pool, Day Pass $3 / $9.99 mo); Professional Tools = 10/day. Say "330+ professional tools". Avoid the word "free" in new copy. Do not change pricing, billing or trial limits. No secrets or customer data in commits.

## Owner decisions needed
none

Source: Testing Bot (reports #51, #52, #54)
