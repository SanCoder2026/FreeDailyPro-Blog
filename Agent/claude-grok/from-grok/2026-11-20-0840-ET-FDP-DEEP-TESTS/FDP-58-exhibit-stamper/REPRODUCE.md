Sent: 2026-11-21 11:52 ET

# FDP-58: how to reproduce (guest, fresh profile with trial uses left)

If Chromium/WebKit fresh contexts show 10/10, Firefox fresh contexts gave 0/10 after 10–22 tries on 2026-11-21. Trial uses reset at midnight UTC (7:00 PM ET).

## P1: per-page-load charging
1. Open https://www.freedailypro.com/tool/exhibit-stamper; note "Trial: 10 uses/day · N remaining" (or localStorage `fdp-usage-v1`).
2. Drop contract_letter_5p.pdf and emails_a4_3p.pdf, click **Stamp 2 files**. Count +1, one `/api/trpc/usage.log` POST.
3. Change Text before to "Pl. Ex. " and stamp again. No change.
4. Clear all, drop one_page.pdf, stamp. No change.
5. Reload, drop landscape_2p.pdf, stamp. Count +1.

## P2: download-button ad creatives
Stamp one file. The slot just below **Download stamped PDF / Save to…** and the right rail filled with "Tap 'Download' to Start" creatives with big Download buttons (Firefox 1366×900). Creatives rotate. Do not click them.

## P2: video not embedded
View the tool page: no "Watch:" section, no VideoObject in JSON-LD. The channel has bC9ON6zNcxo "How to Stamp Exhibit Labels on PDFs…".

## P3: Start at 0
Label with Numbers, Start at 0: no error; the index preview shows Exhibit 1, Exhibit 2, and so does the output.

## P3: header covered
Drop header_top_right.pdf, keep defaults (Top right, white box), stamp. Render page 1: the box covers "Filed 11/21/2026".

## P3: non-Latin label
Text before "Anlage ", after " – 証拠", Every page, size 18, twelve_12p.pdf. `pdftotext` shows no stamp; `pdfimages -list` shows 12 images + 12 masks.

## P3: duplicate Save buttons
Stamp one file: two rows, each with Save to Google Drive and Save to my cloud storage.

## P3: Limitations copy
Drop password_u123.pdf: an inline dialog asks for the password; u123 unlocks and it stamps.

## P3: dark page
dark_2p.pdf, box off, Top center: black label on near-black page (crop-E06).
