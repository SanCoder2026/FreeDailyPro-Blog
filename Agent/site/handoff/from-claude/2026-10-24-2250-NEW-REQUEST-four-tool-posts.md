# New post request: four tools that have no good dedicated post yet
Date and time: 2026-10-24 22:50
Type: REQUEST (new posts). Put them in a normal NEW folder in `handoff/from-grok/`.

Read `docs/1-NEW-BLOG-RULES.md` first. Every rule applies. The slug of each post is the tool id, so the tool page can find it.

## The four posts
| Slug | Tool (link as /tool/<id>) | Who it is for | Real scenario to build the post on |
|---|---|---|---|
| `split-pdf` | split-pdf | admins, freelancers, legal and HR staff | Cut a 20-page combined packet into client files. Show the page range box (`1-3, 4-6, 7`), the "Every page" button, "split every N pages", and the option to combine the ranges into one PDF in a chosen order. Explain that a range can be typed in any order and that pages can repeat |
| `pdf-to-word` | pdf-to-word | students, office workers, anyone editing a received PDF | Turn a text PDF into an editable .docx; what happens with a scanned PDF (it has an OCR step with a language picker); the page range option; what layout can and cannot be kept. Be honest that complex layouts need a tidy-up in Word |
| `qr-generator` | qr-generator | small businesses, event hosts, teachers | One post covering the types the tool makes (link, text, WiFi, contact card, email, SMS, phone), PNG up to 2,000 px and SVG for print, error-correction levels, the logo option, why a shorter link scans better, and testing with a phone before printing |
| `color-palette` | color-palette | designers, students, small-shop owners | Build a palette from one base colour and pick the harmony type that fits the job. Use real hex codes, and link contrast-checker for the text-on-colour check |

## Rules specific to this request
1. Only describe what the tool does. Open the tool page (https://www.freedailypro.com/tool/<id>) and use what you see. If you are unsure a feature exists, leave it out.
2. Use worked, real numbers: page counts, hex values, pixel sizes, byte counts. No invented statistics.
3. Embed each tool's video with the same `{{youtube ...}}` line used in the other posts (ids: split-pdf `0jI1pCsuiqI`, pdf-to-word `K61zcnXg6sU`, qr-generator `OwklDj1Z5_w`, color-palette `QYe_8G_2wqs`).
4. Say "trial uses", not "free", in visible text. Do not say the site works offline. Files stay in the browser for these four tools.
5. Link only related tools, for example: split-pdf -> merge-pdf, extract-pdf, compress-pdf; pdf-to-word -> ocr-pdf or ocr-tool, word-to-pdf; qr-generator -> custom-qr, bulk-qr, qr-scanner; color-palette -> color-converter, contrast-checker, gradient-generator. Check ids in `docs/tool-ids.txt`.
6. No filler like "Practical anchors", "Inputs that matter" or "Draft offline first". Each post must read differently from the others.

## Also waiting for you
`API-MCP-BLOG-BRIEF.md` (same folder) is the brief for ten API and MCP posts. It was not in this repo before; it is now. Do those after the four posts above.
