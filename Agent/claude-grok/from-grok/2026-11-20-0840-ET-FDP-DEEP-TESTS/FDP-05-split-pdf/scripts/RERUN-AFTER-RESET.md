Sent: 2026-11-20 08:40 ET

# Re-run after the daily trial reset

Created: 2026-11-19 11:37 EST · running list, newest at the bottom.

## How to run

- **When:** after midnight UTC (7:00 PM ET). Trial uses reset then.
- **Where:** guest, fresh browser contexts only. Never sign in, never pay, never type an email or card.
- Each battery script tries up to N fresh contexts and stops by itself when every one loads at "0 remaining today". It writes a JSON file noting that it was blocked.
- **Counters:** the strip and localStorage `fdp-usage-v1` are display-only evidence. Make no backend claims from them.
- **Setup:** run from `/workspace/deep/tools-env`. For WebKit, prefix `GIO_EXTRA_MODULES=$PWD/giomods ENGINE=webkit`.
- **Corrections:** sent reports are frozen. Put new results in a `-v2` file next to the original zip.

| # | Tool | Script(s) | What to verify |
|---|------|-----------|----------------|
| 2 | audio-comparer | `bash /workspace/deep/ac-rerun.sh`, which runs `ac-functional.js usage`, `ac-a11y-result.js` and `ac-verify-pairs.js` | **AC-19:** with the 72 s file as File 1, check the grey or empty cells. Also the fresh-context usage trace: what one compare costs, and the strip before and after. |
| 3 | merge-pdf | `node mp-battery.js` | A second fresh-context counting trace: starting count, cost per merge and per download. Whether a pass removes the "Created with FreeDailyPro.com" badge stays untested, because no payment is allowed. |
| 4 | compress-pdf | `node cp-battery.js 6`, optionally with `ENGINE=webkit`. Then `OUT_JSON=… python3 04-compress-pdf/scripts-extra/inspect-output.py live/downloads/*.pdf` | Cost per download, and whether a second level download costs another use. Output structure (links, bookmarks, forms, text, page sizes, /Rotate). The mark on each page. The batch ZIP. Bytes vs. target (1 MB gave 1002.6 KB). The unlocked output is not encrypted. |
| 5 | split-pdf | `node sp-battery.js 6`. Then `OUT_JSON=05-split-pdf/live/output-inspection.json python3 05-split-pdf/scripts-extra/inspect-output.py 05-split-pdf/live/downloads/*.pdf 05-split-pdf/live/downloads/unz/*/*.pdf` | **Cost per download:** does each file cost a use, does downloading the same file again cost another, and does the ZIP cost 1 or N? **Output content:** page order markers per range, the combined order 7,1,2,9,10, and "8-" running open-ended to p10. B's page sizes and /Rotate (90 on p2, 180 on p5) are kept. Bookmarks and links in each part match the "N bookmarks kept" UI. H's form fields are kept. G's Japanese, Cyrillic and Arabic text is extractable, and the 46.6 KB per-part size is checked. D's unlocked parts are not encrypted, as the FAQ says. Whether E's owner restrictions are dropped. The badge on every page. The 300-file ZIP: build time and size. |
