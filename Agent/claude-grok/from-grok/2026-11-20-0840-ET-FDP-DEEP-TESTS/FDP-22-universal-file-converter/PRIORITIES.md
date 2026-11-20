Sent: 2026-11-20 08:40 ET

# FDP-22 Universal File Converter: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | P1 | Presentation conversions upload the file (`POST presentation.convert`: .pptx→.odp 40,246 B; .ppt→PDF / .ppt→.pptx 870,466 B) while title, meta, chip, 2 FAQs, Privacy and on-page note say nothing is uploaded | `json/battery-U02-U21.json` U10/U11, `js/legacyDeck.pretty.js` L53 | Convert in-browser, or disclose per target before the click and fix every "no upload" line |
| 2 | P1 | CSV → Excel/JSON: leading zeros lost (02134→2134, 00501→501); CSV → JSON: `=1+1` text becomes "" | `testfiles/outputs/out-U09-1.xlsx`, `out-U09-2.json` | Keep CSV cells as text where they aren't plain numbers; never blank a cell |
| 3 | P1 | Real `.doc` accepted and offered 3 targets, then generic "That conversion didn't work on this file." (console: NotDocxError) | `json/toasts.json` T2 | Say ".doc (Word 97–2003) isn't supported — save as .docx" at detection, or don't offer targets |
| 4 | P2 | `.pptx` offered "PowerPoint .pptx (from old formats)" → "This file is already a .pptx." | toasts T4 | Hide the target for .pptx |
| 5 | P2 | Format table lists .pps/.odp/.key inputs; picker accept list rejects .odp ("can't be used here") | U12, `Os` L223 | Align list and accept attribute |
| 6 | P2 | Compression levels live: Recommended (~50%) / Medium (~25%) / Strong (~50%); FAQ: Balanced/Aggressive/Extreme/Target size; Tips: "Light before Strong"; Recommended and Strong both "~50%" | `json/gate-kbd.json` compressLevels | One set of names everywhere; distinct estimates |
| 7 | P2 | HTML → Text/PDF include the `<script>` source as visible text (script did not run — good) | `out-U15-1.pdf`, `out-U15-3.txt` | Drop script/noscript content |
| 8 | P2 | Hero image and video show a mock app ("100+ formats", MP4→GIF, JSON→YAML, Convert All 62%) | `screens/devices/iphone-14-pro-max-fold.png`, video | Real screenshot of the tool |
| 9 | P2 | Video: "10 trial usages every day", "$1 day pass / $4.99 monthly", "MultiTool Apps" | `screens/video/quad.png` | Re-record with today's Premium terms |
| 10 | P2 | axe critical: 2 unnamed buttons (a select trigger and a disabled button in the idle panel) | `json/matrix-results.json` a11y | aria-label on the triggers |
| 11 | P2 | iPhone (WebKit) horizontal overflow: SE 9 px (button), 14 Pro Max 50 px (select trigger) | matrix devices | Constrain trigger width |
| 12 | P2 | Excel → JSON dates as serials (46023) vs ISO in CSV; first row omits empty "Total" key while others have "" | `out-U07-3.json` | ISO dates; consistent keys |
| 13 | P3 | Word → HTML loses bold and tables (tabs in `<p>`); PDF → Word plain paragraphs; table PDF → Excel merges columns ("9.99 02134") | U13, U04, U05 | Note in Limitations or improve |
| 14 | P3 | OCR language data loads from cdn.jsdelivr.net (third party); copy says "downloads its English language data" without naming the host | `json/toasts.json` T1 | Name the host or self-host |
| 15 | P3 | Batch toast "1 were left out"; image → same format offered (PNG → PNG) | `screens/live/multi-21.png`, U02 | Grammar; hide same-format target |
| 16 | P3 | Locale pages keep English title/meta; /ar 404; ja desktop 3 px overflow | matrix locales | Localise |
| 17 | P3 | Blog and video say "MultiTool Apps"; breadcrumb says Premium Applications; category PDF Tools | desk | One name |
