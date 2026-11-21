Sent: 2026-11-21 07:48 ET

# Instructions for Claude: FDP-49 PDF Bookmarks Editor

1. Read REPORT.md ("How to work with us" first), then PRIORITIES.md.
2. Fix the shared Download trial-use wrapper: charge per new result, check the cap each time. It's the same fix as FDP-44–48, so verify all of them.
3. Fix the outline writer so that deleted or removed bookmarks don't stay in the file. Recheck with `scripts/check-outputs.py` on a Remove-all download; it should show "orphan outline titles: [] 0".
4. Resolve named destinations. Keep, or clearly warn about, URI/other actions.
5. Optional: keep colour, bold/italic and the collapsed state; show page labels; add a per-delete undo.
6. Verify with test-cases.md and `scripts/` (see the README). Don't sign in during automated tests, and make no real payments.
7. Wording: use "Premium Applications" / "Professional Tools" / "Workflow Products" and "trial uses". Keep the reserved ad slots.
