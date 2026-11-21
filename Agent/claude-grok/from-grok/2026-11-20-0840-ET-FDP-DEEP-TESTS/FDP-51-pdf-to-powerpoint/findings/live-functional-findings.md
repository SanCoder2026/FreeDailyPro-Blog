Sent: 2026-11-21 08:44 ET

# Live functional findings (guest Chromium unless noted; 2026-11-21 EST)

## At the cap (zero.json, context at 10/10)
- Converting works in both modes at 0 uses, and the preview shows every slide. Z01 (P01, 3 slides): 8.5×11 in. Z02 (P02 editable): 13.3×7.5 in.
- Download, "Get a Day Pass to download" and Save to Google Drive all open the cap dialog ("Today's trial uses are done … $4.99/month … Day Pass $1").
- **Buy Day Pass:** goes to the email field ("Continue to payment"). Stopped there.
- **Quick Buy (monthly):** goes to Stripe Checkout (cs_live_REDACTED). Stopped there.
- **Save to my cloud storage:** "Sign in with your email first", $4.99/mo for 1 GB.
- **Open from Google Drive:** opens a Google sign-in popup (closed).
- **Keyboard:** 27 Tabs reach the drop zone.

## With uses left (left.json, one page load plus a reload)
- **Charging:** L01 went 0→1. L01b and L02–L14 (13 new decks) stayed at 1. After a reload, L20 went 1→2 and L21 stayed at 2. There were 2 `usage.log` POSTs (126 B each).
- **Picture:** each page becomes a 1920 px slide background image. No shapes, no text. Correct slide size.
- **Editable on Type3-text PDFs (P01/P02/P07):** "0 pieces … became editable; 16/30 stayed in the background picture". The output is the same as Picture. The message is honest.
- **P03 (SVG shapes, a table, a link; Type3 text):** 0 editable. The link isn't kept (expected for picture text).
- **P04 scan:** "1 page had no text at all (a scan or a picture)".
- **P05 password:** the unlock dialog appears. After typing u123, the toast reads 'Unlocked "P05_password_u123.pdf"' and the 3 slides convert.
- **P06 damaged / P10 non-PDF:** toast "can't be read — it looks damaged. Try the Repair PDF tool". No convert button.
- **P07 60 pages:** Picture 1.4 s and Editable 2.6 s, 60 slides, 1.8 MB. The preview has small pictures for the first 40 slides. The ">40 pages" note appears before converting.
- **L11 Stop (1.5 s):** the conversion had already finished, so this case wasn't measurable. M04 measured it (below).
- **P08 multilingual, editable:** 39 pieces in 4 boxes, and the fonts are listed. The Arabic line is reversed (see cmp-P08). The kana are partly misplaced; the kanji, Hindi, Greek and Cyrillic were Type3 glyphs and stayed in the picture.
- **P09 mixed:** the slide is A4 portrait, and the landscape page 2 is fitted inside it.

## LibreOffice PDFs (left2.json, a context with uses left; first attempt at the cap kept as left2-attempt1-at-cap.*)
- **M01, P11 deck, editable:**
  - 33 of 33 pieces became editable, in 13 text boxes.
  - Only "Deja Vu Sans" was flagged as an unusual font.
  - python-pptx: bold and italic kept. Arial / Times New Roman / DejaVu / Calibri. Sizes 40/24/18/11 pt match the source.
  - Colours: 2759A5 (source 1A4FA0), C92424 (source C00000), 272727–353535 (source 000000).
  - The background has the text removed cleanly (M01-bg-slide1.png).
  - Table rows are merged into single runs (cmp-P11p3).
- **M02, P11 picture:** 425 KB, 4 slides.
- **M03, P12 memo, editable:** 23 pieces in 8 boxes. "Open Symbol" is flagged. The bullets, bold and italic look right. The table text overlaps the cell lines (cmp-P12).
- **M04 Stop at 0.4 s on 60 pages, editable:** the Stop button was present. It returned to the options with no result, no toast and no charge.
- **M05 after Stop:** the next conversion works normally.
- **Charging:** M01 went 0→1. M02, M03 and M05 (new decks) stayed at 1. There was 1 `usage.log` POST.

## Network
- No POST carried PDF bytes or document text (doc=false for every POST, in all runs).
- GETs: fontkit chunk (own domain) and the usual ad/analytics scripts. There are no third-party processing calls.
