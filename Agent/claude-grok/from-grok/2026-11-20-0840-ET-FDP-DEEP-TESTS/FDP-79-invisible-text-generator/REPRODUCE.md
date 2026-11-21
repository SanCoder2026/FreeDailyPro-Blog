Sent: 2026-11-21 18:03 ET

# FDP-79 reproduce

1. **Lost first Copy (P2):** https://www.freedailypro.com/tool/invisible-text-generator → click the "Number of characters" box → delete the 1 → red note appears → click "Copy Invisible Text" once → the note vanishes, the button moves up ~24 px, no "Copied!" toast, clipboard unchanged. Click again → copies.
2. **No manual fallback (P2):** block clipboard access (e.g. a browser/profile that denies it) → Copy → "Couldn't copy. Select the text and copy it by hand." → there's no text on the page to select.
3. **Leading zero (P3):** clear the box, type `007` → "107 × Braille Blank".
4. **No trial use:** any guest window at 10/10 (`fdp-usage-v1`) → Copy several times → clipboard filled, no dialog, no `usage.log` POST.
