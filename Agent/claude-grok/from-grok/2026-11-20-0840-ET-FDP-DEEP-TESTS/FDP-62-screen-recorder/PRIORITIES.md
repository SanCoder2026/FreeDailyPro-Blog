Sent: 2026-11-21 13:20 ET

# FDP-62 Screen Recorder: priorities (2026-11-21 EST)

| Pri | Item | Evidence | Why it matters | Suggested fix |
|---|---|---|---|---|
| P1 | Full recording plays at 0 trial uses in `<video controls>` with no `controlsList="nodownload"`; the browser's own Download / Save video as saves it | zero.json Z05, zero-firefox.json; code (no controlsList) | Nov 21 rule: full-quality result at 0 is a gate gap; the pass becomes optional | nodownload + no context menu, and/or limit playback at 0 |
| P1 | One trial use per page load: a second take in the same load downloads free, no cap; capped after reload | left.json L04 (2/2, no POST), L06 | Nov 21 rule: per-page-load charging | Charge per new recording |
| P2 | Video DEwAYXXSJ-c records a third-party game site; share picker shows other tabs; old UI; "Free" title/description; "PDF tools" tag | video/sheet.png, crop-frames.png, info-min.json | Off-brand, privacy-sloppy demo of a Premium app | Re-record in a clean profile on an FDP page, tab-only share |
| P2 | Safari/iPad untested: Linux WebKit crashes on `enumerateDevices()` (env) | px62-wk.js, px62-wk2.js | Mac Safari is a key desktop browser | Manual Safari check |
| P2 | MP4 (H.264/AAC) claim unverified (Playwright Chromium has no H.264; all takes WebM) | left.json probes | Page promises MP4 in Chrome | Confirm in branded Chrome/Safari |
| P2 | Locale pages: subtitle, Premium line, toggles, Start button, FAQ English; consent banner in de/fr | locales/*es*, geo/*de-de* screenshots | Mixed-language page | Translate tool strings (site-wide) |
| P2 | SEO: title without brand, meta 83 chars, generic OG image | tool.html | CTR | "Screen Recorder Online – Record Your Screen in the Browser | FreeDailyPro"-style title; 140–160-char meta |
| P3 | Start Recording enabled on unsupported browsers (toast only) | nodm.json, N01.png | Dead click on phones | Disable/hide with the note |
| P3 | Counter shows 2 remaining, first download sets 2/2 (server pooling, observation) | left.json L02 | Shared networks | Owner awareness |
| P3 | axe: label-content-name-mismatch (serious), region; Pixel 7 ad-caption contrast; ja 3 px overflow | matrix-results.json | A11y polish | Fix label and caption colour (keep reserved ad slots) |
