Sent: 2026-11-22 05:35 ET

Sent: 2026-11-22 05:34 ET

# FDP-97 output verification (verify97.py)

One row per verified live output. `layer` = position of the watermark stream relative to the original content; `pos` = class measured on the PDFium render (badge masked); `pages` = pages carrying a watermark stream / total; `text/img ops` = Tj / Do operators in watermark streams; `hits` = search hits for the watermark text in the whole file; `strip` = max px difference after removing the added streams (0 = perfectly removable); sizes in bytes.

| Tag | Text | Expected pos | layer | pos (render) | pages | text/img ops | hits | strip | links | fields | toc | hidden | size | all_ok |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B01-doc | BATCH | center | top | center | 6/6 | 6/0 | 6 | 0 | True | True | True | 0 | 11011→13339 | **True** |
| B01-rotated | BATCH | center | top | center | 6/6 | 6/0 | 6 | 0 | True | True | True | 0 | 3966→9026 | **True** |
| B01-three | BATCH | center | top | center | 3/3 | 3/0 | 3 | 0 | True | True | True | 0 | 1483→4512 | **True** |
| E01 | CONFIDENTIAL | center | top | center | 3/3 | 3/0 | 3 | 0 | True | True | True | 0 | 19043→15645 | **True** |
| E03 | DRAFT | tiled | top | tiled | 300/300 | 23400/0 | 13200 | 0 | True | True | True | 0 | 2866511→3993997 | **True** |
| I01 | image | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→23550 | **True** |
| I02 | image | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→10070 | **True** |
| I03 | image | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→31749 | **True** |
| L01 | Brouillon – ÉTÉ | center | top | center | 3/3 | 3/0 | 3 | 0 | True | True | True | 0 | 1483→4552 | **True** |
| L02 | Конфиденциально | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→34600 | **False** |
| L03 | 机密文件 | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→24055 | **False** |
| L04 | गोपनीय | center | top | center | 3/3 | 3/0 | 3 | 0 | True | True | True | 0 | 1483→131274 | **True** |
| L05 | سري للغاية | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→20619 | **False** |
| L06 | 🔒 SECRET | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→27591 | **False** |
| L07 | Entwurf № 3 | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→25130 | **False** |
| L08 | 机密 | tiled | top | tiled | 6/6 | 0/546 | 0 | 0 | True | True | True | 0 | 11011→2112513 | **False** |
| L09 | COPY | tiled | top | tiled | 6/6 | 546/0 | 264 | 0 | True | True | True | 0 | 11011→47689 | **True** |
| W01 | CONFIDENTIAL | center | top | center | 6/6 | 6/0 | 6 | 0 | True | True | True | 0 | 11011→13403 | **True** |
| W02 | DRAFT | center | top | center | 6/6 | 6/0 | 6 | 0 | True | True | True | 0 | 8044→11449 | **True** |
| W03 | CONFIDENTIAL | center | top | center | 6/6 | 6/0 | 6 | 0 | True | True | True | 0 | 3966→9096 | **True** |
| W04 | TOPLEFT | top-left | top | top-left | 6/6 | 6/0 | 6 | 0 | True | True | True | 0 | 3966→8945 | **True** |
| W05 | BRMARK | bottom-right | top | bottom-right | 5/5 | 5/0 | 5 | 0 | True | True | True | 0 | 3422→8003 | **True** |
| W06 | TILE | tiled | top | tiled | 5/5 | 298/0 | 141 | 0 | True | True | True | 0 | 3422→22444 | **True** |
| W07 | TOPRIGHT | top-right | top | top-right | 6/6 | 6/0 | 6 | 0 | True | True | True | 0 | 2813→7952 | **True** |
| W08 | BEHIND | center | behind | center | 5/12 | 5/0 | 5 | 0 | True | True | True | 0 | 8316→14898 | **True** |
| W09 | SKIPPED1 | center | top | center | 2/3 | 2/0 | 2 | 0 | True | True | True | 0 | 18977→14968 | **True** |
| W10 | HIDDEN | center | behind | None,center | 3/3 | 3/0 | 3 | 0 | True | True | True | 0 | 123214→126172 | **True** |
| W11 | VISIBLE | center | top | center | 3/3 | 3/0 | 3 | 0 | True | True | True | 0 | 123214→126139 | **True** |
| W12 | image | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→11487 | **True** |
| W13 | image | bottom-right | top | bottom-right | 6/6 | 0/6 | 0 | 0 | True | True | True | 0 | 3966→15824 | **True** |
| W14 | image | tiled | top | tiled | 5/5 | 0/114 | 0 | 0 | True | True | True | 0 | 3422→18840 | **True** |
| W15 | image | top-left | top | top-left | 6/6 | 0/6 | 0 | 0 | True | True | True | 0 | 8044→19462 | **True** |
| W16 | image | center | top | center | 3/3 | 0/3 | 0 | 0 | True | True | True | 0 | 1483→7520 | **True** |
| W17 | INTERNAL | tiled | top | tiled | 2/20 | 156/0 | 60 | 0 | True | True | True | 0 | 2727326→2741256 | **True** |
| W18 | CONFIDENTIAL - DO NOT DISTRIBUTE | bottom-right | top | bottom-right | 3/3 | 3/0 | 3 | 0 | True | True | True | 0 | 1483→4630 | **True** |

Not row-verified (too large to render fully): E04 heavy (30/30 pages carry a watermark stream, no badge), E07 tiled CJK 300 pages (91 image XObjects on pages 1, 150, 300; 67,820 objects; 107,374,044 bytes).
