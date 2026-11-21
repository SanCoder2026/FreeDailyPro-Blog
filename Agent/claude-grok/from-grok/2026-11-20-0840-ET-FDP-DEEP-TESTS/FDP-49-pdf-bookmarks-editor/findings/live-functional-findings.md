Sent: 2026-11-21 07:48 ET

# Live functional findings (Chromium, guest, 2026-11-21 EST)

- **zero.json (fresh context at 2/2):**
  - Loading and editing B01 works. The preview is 520×672.
  - Download → cap dialog: "You've used today's trial uses… Monthly $9.99… Day Pass $3… removes the 'Created with FreeDailyPro.com' mark…". Day Pass → email field (stopped there). Quick Buy monthly → Stripe Checkout (stopped there).
  - Open from Google Drive → Google sign-in popup.
  - The keyboard reaches the drop zone and Open from Google Drive in 29 tabs.
- **left.json:** 2 `usage.log` POSTs for 6 downloads.
  - L01: 0→1.
  - L01b (re-download), L02 and L03: the counter stays at 1.
  - After a reload, L14: 1→2. L15 at 2/2 still downloaded with no dialog.
  - L04 was the password dialog, which blocked the next cases. That was my harness; the cases were rerun in left2.
- **left2.json:** 1 `usage.log` POST for 9 downloads in one load: M01, M02 (password-unlocked B04), L07, L08, L09, L10, L11, L13, L16.
- **Behaviour checks:**
  - Unicode titles (é, 日本語, Arabic, emoji) round-trip correctly.
  - 3-level nesting and /Count are correct.
  - PageMode is set to UseOutlines, and removed again when there's no outline.
  - Form field, link annotation, docinfo and page labels are preserved.
  - A cyclic outline is handled.
  - 300 bookmarks load in 3.5 s.
  - Errors are clear: out-of-range page (Download disabled), empty title, damaged file → Repair PDF, wrong password.
- **Outputs (check-outputs.py → json/orphans.txt):**
  - Old and deleted outline objects stay in every output that had an outline.
  - L08 lost `/C`, `/F` and the negative `/Count`.
  - L03: named, GoTo-named and URI bookmarks were saved with no target or action.
  - No FreeDailyPro mark in any output.
- **Network:** no request carried PDF bytes or bookmark titles.
