Sent: 2026-11-21 02:08 ET

# FDP-35 Video Converter: priorities

| # | Pri | Item | Evidence | Suggested outcome |
|---|---|---|---|---|
| 1 | **P1** gate gap | Only the first Download per page load costs a trial use; Downloads of other converted videos are free until reload (0→1, then 1→1→1, reload 1→2). Conflicts with Santosh's Nov 20 decision that every Download uses a trial (Barcode, Invoice). Shared counting code. | `json/gate.json` (02:00:59–02:02:36 EST); `index-*.js` `xI`/`Kt` (FDP-34 excerpt) | Count each Download (or whatever unit Santosh confirms) in the shared hook; fix once for all tools. |
| 2 | **P1** gate leak | The preview `<video controls>` is byte-identical to the Download (sha `0762f787…`), also at 0 remaining; no `controlsList="nodownload"`, so the player's own Download / "Save video as…" gives the file without a use. | `json/gate.json` `left.preview`, `zero.preview`, `dlA` | `controlsList="nodownload"` + disable context menu at minimum; better a low-res/short preview until Download is allowed. |
| 3 | P2 | Copy contradicts itself: six outputs live vs "four" (FAQ, How to use, Limitations, blog) and "MP4, WebM and MOV" (subtitle, JSON-LD). Drop zone "over 5 GB" vs enforced 50 MB trial / 200 MB paid. | `html/tool-expanded.txt`, `json/cases-chromium.json` K21, `js/ffmpegEngine-*.pretty.js` | One story everywhere; state the 50 MB trial cap. |
| 4 | P2 | Video zqpLPhmyj9E: old "Format Converter / Convert between MP4 and MOV" UI; personal folders ("CEH", "Crack", "Agent Outros") and bookmarks bar visible; "Free". | `findings/video-findings.md`, `video/z28-tl.png`, `video/z45-tl.png` | Re-record cleanly: iPhone MOV → MP4 rewrap, WebM → MP4; "trial uses". |
| 5 | P2 | 11 pair titles "- Free, No Upload"; English head tags under 9 hreflangs; /ar 404. | `findings/desk-findings.md`, matrix | "Online, No Upload"; translate or drop hreflang. |
| 6 | P2 | Completeness: no quality/resolution/fps controls, no H.265/VP9/AV1 output, WebM VP8 1 Mbps only, no batch; 50 MB trial small for phone video. | `findings/desk-findings.md` | Presets (720p/1080p, quality) as the Premium Applications step. |
| 7 | P3 | Text file named .mp4 → generic "phone codec" error after 11.6 s; "Upgrade to Pro" naming; rewrap scope copy (MKV); cap-dialog mark claim; iPhone SE 9 px / ja 3 px overflow; link-in-text-block; two "Quick Buy"; thumbnail alt; Offer 4.99. | `json/cases-chromium.json` K18, matrix | "This file can't be read as video"; labelled buttons; wrap the row. Keep ad slots reserved. |
