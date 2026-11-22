Sent: 2026-11-22 00:04 ET

# Usage gate

- Shared ToolPage download helper (same as #84–#89): the first Download in a page load charges once (`usage.log` POST); later downloads in the same load don't.
- left.json: F02 0→1 (1 POST), then F02b, F03, F05, F06, F07, F08: 6 more files, 0 POSTs.
- left-b.json: F01 0→1 (1 POST), X01 and F09 0 POSTs; X14 after reload 1→2 (1 POST).
- Fill form itself never charges (0 POSTs).
- At 0 uses (zero.json, left-b Z15): Fill form works, a filled "Page 1 preview" appears, Download → cap dialog "Today's trial uses are done… Your input stays where it is…" + inline "Today's trial uses are used up, so downloading was not done…", 0 POSTs, no file. Real save blocked ✓; visible preview = owner question.
- Hand-off from Create Fillable PDF: the fill costs a second Premium use (handoff.json).
- Quick Buy: Day Pass $3 → email dialog (stopped); Monthly $9.99 → Stripe Checkout (stopped, ID redacted).
- Drive: "Open from Google Drive" → Google sign-in popup (closed).
