Sent: 2026-11-21 15:54 ET

# FDP-70 reproduce

1. **Size limit:** a guest window with uses left → https://www.freedailypro.com/tool/passport-photo → drop `testfiles/fdr-1400.jpg` → Photo Size US → File size limit "Under 50 KB" → Download Single Photo. The toast says "50 KB"; the saved file is about 63 KB. India + Under 50 KB → about 80 KB.
2. **DPI:** open any download in an image viewer/Pillow (`Image.open(f).info.get('dpi')` → None; JFIF units 0, density 1:1). Expected 300×300.
3. **Per page load:** same window: after the first download (1 POST), change template, download sheets, press Upload Different Photo and download again: no POST, no dialog, even when the strip shows 0 remaining. Reload → first download charges again.
4. **Auto-fit:** drop `fdr-1400.jpg` → UK → Make background white + auto-fit head. The message says "middle of the allowed range"; the head sits inside the green (smallest) oval.
