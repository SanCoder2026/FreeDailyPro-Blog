Sent: 2026-11-21 14:59 ET

# FDP-67 reproduce

1. Fresh guest window with uses left → https://www.freedailypro.com/tool/stl-ascii-binary-converter. DevTools Network filter `usage.log`.
2. Drop an ASCII STL → Convert to Binary STL → Download. One POST; strip drops by 1.
3. Without reloading: Change file → drop a different STL → convert → Download. **No POST, no count**, file saves. Repeat: same.
4. Use a page whose first download brings the counter to 10/10: further files from step 3 still download, no cap dialog.
5. Control: reload at 10/10 → convert → Download → cap dialog (gate works on a fresh page).
6. Test STLs: `evidence/testfiles/` (generated; see test-cases.md).
