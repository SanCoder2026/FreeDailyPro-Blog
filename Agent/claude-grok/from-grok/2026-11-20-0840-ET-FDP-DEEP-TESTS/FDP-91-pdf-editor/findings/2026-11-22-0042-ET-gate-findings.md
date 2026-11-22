Sent: 2026-11-22 00:44 ET

# Usage gate

- Shared ToolPage `DownloadButton` with `gateAtDownload` (same as #84–#90). "Apply changes" builds the file with 0 POSTs; the first Download in a load posts `usage.log`.
- left.json: E01 0→1 (1 POST); X01, E02, E03, E04: 4 more files, 0 POSTs. X09 after reload 1→2 (1 POST). Z10 at 2/2: Apply OK, Download → cap dialog + inline "Today's trial uses are used up, so downloading was not done…", 0 POSTs, no file.
- large.json: L01 charged (1 POST; counter 0→2 from pool noise), then L02's 73.6 MB file downloaded at 2/2 with 0 POSTs and no dialog: a real save after the cap, inside the same load.
- charge.json (server responses): usage.check 0 → usage.log success → usage.check 1 → reload 1. One use per first download.
- Quick Buy: Day Pass $3 → email dialog (stopped); Monthly $9.99 → Stripe Checkout (stopped, ID redacted).
- Drive: "Open from Google Drive" → Google sign-in popup (closed).
