Sent: 2026-11-21 13:37 ET

# FDP-63 Color Picker from Image: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Why it matters | Suggested fix |
|---|---|---|---|---|
| P1 | One trial use per page load: after the first copy, every further copy (other formats, palette, a second image) is free; reload charges again | left.json L03–L06; left-firefox.json | Nov 21 rule: per-page-load charging | Charge per copy (or per image, owner's choice) |
| Owner Q | Picked values (HEX/RGB/HSL/CMYK) are fully visible and selectable at 0 trial uses; only copy buttons are gated | zero.json Z02–Z05, cases/copy-*-dialog.png | Pending owner ruling on results visible at 0 (Nov 21 1:19 PM) | Santosh to decide |
| P2 | Page copy contradicts the tool: "no magnifier", "only hex/rgb/hsl", "no zoom", palette advice, "usage counter records when you add a file" | tool-expanded.txt 64–76; live magnifier/CMYK/palette; 0 POSTs on upload | Users read limits that aren't true; privacy line is wrong | Rewrite limits/tips/privacy/FAQ formats |
| P2 | Blog "three panels" / "Precision, without a magnifier"; video old UI + "free" wording | curl/blog.html, video/sheet.jpg, info | Outdated marketing undersells the tool | Refresh blog section; re-record video |
| P2 | Non-image file fails silently (blank canvas) | C08-notimage-*.png | Confusing dead end | Show "Couldn't open this file as an image" |
| P2 | Locale pages: H1, subtitle, drop zone, camera button, meta stay English | locales/*es* | Mixed-language page | Translate tool strings (site-wide) |
| P2 | SEO: meta 92 chars, generic OG image | tool.html | CTR | 140–160-char meta naming hex/RGB/HSL/CMYK, magnifier, palette |
| P3 | Huge images: one click can't hit a chosen pixel (keys can) | debug.json | Precision expectation | Mention arrow keys in the how-to |
| P3 | Transparency ignored (25 % alpha red → #ff0000) | C04-alpha.png | Logos with alpha | Show alpha or a note |
| P3 | Firefox counter jumped 0→10 on first copy (server pooling, observation) | left-firefox.json L03 | Shared networks | Owner awareness |
| P3 | iPhone SE 9 px overflow (header menu button); axe label mismatch, region; Pixel 7 ad-caption contrast; ja 3 px | matrix-results.json, devices/iphone-se-fold.png | A11y/layout polish | Fix label, caption colour (keep reserved ad slots) |
| P3 | Camera button on desktop just opens the file chooser | camera.json | Redundant button | Hide on non-touch; real-phone check |
