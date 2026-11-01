Sent: 2026-11-01 4:06 PM ET
Source: Video check run 19 findings (Orchestrator); not an owner request. Accuracy and capability fixes.

## Intent
Ringtone Maker makes iPhone ringtones that actually work, with one consistent stated limit; PDF to Word's OCR FAQ says one true thing.

## Why
Ringtones are the biggest demand topic found today (~25.6M views). Offering 45s/60s iPhone files that iOS won't take as ringtones, plus contradictory limits, breaks trust and blocks the Short.

## Outcome
1. /tool/ringtone-maker iPhone (.m4r): cap at 40s; presets 15/20/30/40. Remove "up to 1 minute" for iPhone.
2. Limitations text: state one limit per platform (iPhone 40s; Android as actually supported). Remove the contradictory "up to 30 seconds for both".
3. Strip the cover-art picture stream from the .m4r output (or confirm Finder/Apple Devices accepts it).
4. Add a short "how to install on iPhone" note (Finder / Apple Devices app / GarageBand, then Settings > Sounds & Haptics).
5. /tool/pdf-to-word FAQ: it contradicts itself on OCR languages ("choose the language" vs "English+Hindi auto-detected"). Make it match the live behavior.
