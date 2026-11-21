Sent: 2026-11-21 01:50 ET

# FDP-34 Convert Image Format: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | **P1** (policy question) | One trial use per page load: after the first Download, further Downloads of other images, frame ZIPs and batches in the same tab are free (0→1→1→1; 1→1 batch after single). Batch of any size = 1 use, no trial batch limit. | `json/gate2.json` (01:39–01:40 EST), `json/gate3.json` (01:45 EST), `json/gate.json`; `js/index-*.js` (`xI`, `Kt`) | Santosh decides the unit (file / batch ≤ N / visit); then the shared counter, labels, FAQ and blog match. Check other tools using the same hook. |
| 2 | **P1** | The result preview `<img>` is the full converted file (same sha as Download), shown even at 0 remaining when Download is blocked — "Save image as…" bypasses the gate. | `json/gate.json` (`preview.sha` = `download1.sha`), `json/cases-chromium.json` C01/C24, `screens/live/case-C02.png` | Downscaled or marked preview, or reveal the full result only once Download is allowed. |
| 3 | P2 | AVIF output disabled in Chromium and Firefox (Playwright); copy and JSON-LD promise AVIF output; "use a current Chrome or Firefox desktop" unverified. | `json/cases-*` C32, `json/probe.json` | Ship a WASM AVIF encoder or reword to "AVIF where your browser supports it". |
| 4 | P2 | Video vHFSmxgaxAU: old "Convert Formats" UI, "10 free uses daily", ~30 s end card, "200+ Free". | `findings/video-findings.md`, `video/z16-tl.png`, `video/z39-crop.png` | Re-record current features in a clean window; "trial uses". |
| 5 | P2 | Wording/SEO: 13 pair titles "- Free, No Upload"; main title no brand; locale H1 = old name "Convert Formats"; English titles/headings under 9 hreflangs; /ar 404; generic og:image. | `findings/desk-findings.md`, `json/matrix-results.json` | "Online, No Upload"; update translations to "Convert Image Format". |
| 6 | P2 | Blog says SVG is "a different tool path" and to "use bulk tools" for batches; omits ICO, fill colour, EXIF, HEIC. | `html/blog.txt` | Correct those lines; add the tool's real strengths. |
| 7 | P3 | Truncated JPEG converts silently (transparent gap). Batch quality 80 vs single 92 (FAQ: 92). Duplicate FAQ. Cap dialog mark claim. Quality slider unnamed; link-in-text-block; two "Quick Buy"; iPhone SE 9 px / ja 2 px overflow; thumbnail alt; Offer 4.99. | `json/cases-chromium.json` C23, `json/axe-loaded.json`, matrix | Damaged-file warning; one default; aria-label "Quality"; labelled Quick Buy buttons; wrap the row. Keep ad slots reserved. |
