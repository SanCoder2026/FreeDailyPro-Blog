Sent: 2026-11-21 08:44 ET

# Scripts (run from /workspace/deep/tools-env with `env -u BROWSER node …`; WebKit needs GIO_EXTRA_MODULES=…/giomods)

- **px51-make.js:** builds P01–P04 and P07–P09 with Chromium page.pdf. On this box the text comes out as Type3 glyphs.
- **make-real.py:** builds P11 (python-pptx deck → LibreOffice PDF) and P12 (HTML → LibreOffice Writer PDF) with TrueType text. P05/P06 are reused from FDP-50 (T09/T16); P10 is a text file named .pdf.
- **px51-scripts.js:** first load. Saves the visible text, the JS chunk list and the trial strip.
- **px51-expand.js:** expands the accordions and saves the text, JSON-LD and links.
- **px51-probe.js:** loads P02, dumps the controls, converts without downloading.
- **px51-live.js `<zero|left|left2|subset> [engine]`:** the main run.
  - `zero`: at the cap. Dialogs, Day Pass (stops at the email field), Quick Buy (stops at Stripe), keyboard.
  - `left`: per-page-load charging and all file cases.
  - `left2`: the LibreOffice files and Stop.
  - `subset`: Firefox/WebKit.
- **px51-cat.js:** renders the PDF Tools and PowerPoint & Slides hubs and checks whether the tool is listed.
- **run-matrix.js + config.json:** devices, locales, geo, axe.
- **check-pptx.py:** python-pptx inspection (slide size, shapes, pictures, text, fonts, sizes, colours, FreeDailyPro mentions).
- **Safety:** no sign-in, no payment, no ad clicks. The scripts redact deviceId, OAuth parameters and the Stripe session. The only password typed is the test file's own (u123).
