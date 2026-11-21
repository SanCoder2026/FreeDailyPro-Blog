Sent: 2026-11-21 10:39 ET

# FDP-55: how to reproduce (guest, fresh profile with trial uses left)

## P1: per-page-load charging
1. Open https://www.freedailypro.com/tool/bates-numbering and note "Trial: 10 uses/day · N remaining" (or localStorage `fdp-usage-v1`).
2. Drop contract_letter_5p.pdf and emails_a4_3p.pdf, set prefix ABC, and click **Add numbers to 2 files**. The count goes +1, with one `/api/trpc/usage.log` POST.
3. Change the prefix to XYZ and run again. No change.
4. Clear all, drop one_page.pdf, and run. No change.
5. Reload, drop landscape_2p.pdf, and run. The count goes +1.
(If Chromium/WebKit fresh contexts show 10/10, Firefox fresh contexts had uses on 2026-11-21.)

## P2: download-button ad creative
Scroll to the area between the tool and "Watch: Bates Numbering in Action" (or add a password PDF so the dialog opens). In Firefox at 1366×900, an ad with a big green "Download" button filled that slot. Creatives rotate. Do not click it.

## P3: non-Latin stamp not searchable
Prefix `Ü案件-`, suffix `-é`, size 14, one_page.pdf. Run and download. `pdftotext one_page-bates.pdf -` shows the page text but no stamp. Render it (`pdftoppm`) and the stamp is visible.

## P3: CSV BOM
`head -c 3 bates-index.csv | od -c` starts with `D o c`, so there's no `EF BB BF`.

## P3: Limitations copy
Drop password_u123.pdf, click **Skip this file**: a toast appears and nothing enters the list. Drop damaged.pdf: a toast with Repair PDF appears and nothing enters the list.
