Sent: 2026-11-21 17:50 ET

# FDP-78 reproduce

1. **Per-page-load charging (P1):** guest window with uses left → https://www.freedailypro.com/tool/yt-thumbnail → paste `https://www.youtube.com/watch?v=dQw4w9WgXcQ` → Get Thumbnails → Download (Max) → counter +1, one `usage.log` POST. Then Download Standard, Download Small, "Download all sizes (ZIP)" twice, paste `https://youtu.be/jNQXAC9IVRw` → Download High quality + ZIP → counter unchanged, 0 POSTs. Reload → one Download charges again.
2. **Save at 0 (P1 by owner rule):** window at 10/10 → paste the link → Get Thumbnails → preview appears with no dialog → right-click the preview → Save image as → file = `https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg` (clean, 65,324 bytes).
3. **Badge on download:** compare `evidence/downloads/left-youtube-dQw4w9WgXcQ-maxresdefault.jpg` (89,022 B) with `youtube-original-…` (65,324 B); see `diff-crop-*.png`.
4. **Re-submit stuck (P2):** Get Thumbnails for dQw4w9WgXcQ → wait for the tiles → press Get Thumbnails again (or paste `youtu.be/dQw4w9WgXcQ`) → preview gone, ZIP disabled "Checking sizes…" indefinitely. Paste another video, then back → works.
