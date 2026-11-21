Sent: 2026-11-21 00:58 ET

# FDP-32 Hash Generator: reproduction steps (guest, https://www.freedailypro.com/tool/hash-generator)

1. **P1 false Match:**
   1. Type `abc` and press Generate Hashes (SHA-256 `ba7816bf…15ad`).
   2. Change the text to `abd` and do not press Generate. The `abc` digests remain.
   3. Paste `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad` into "Compare with expected checksum" → "Match (SHA-256)".
   4. Script: `scripts/hg-stale.js`.
2. **P1 keyboard file:** click into the text box and press Tab. Focus goes to "Generate Hashes"; "Or choose a file to hash" can't be reached or activated by keyboard.
3. **P1 trial use:**
   1. In a context at 0 remaining (`fdp-usage-v1.usageToday` = limit), press Generate, Copy, Compare, choose a file and press Generate.
   2. Everything works, with no dialog; the counter is unchanged after reload.
   3. Repeat with uses left after 7:00 PM ET.
   4. Scripts: `hg-gate.js`, `hg-uses.js`.
4. **Video:** https://www.youtube.com/watch?v=7vHVmGVIeWA at about 0:20: no file picker or Compare; "10 free uses daily"; the bookmarks bar is visible.
5. **Compare formats:** paste `sha256:ba7816bf…` or `ba7816bf…  file.iso` → "No match for any algorithm".
6. **CRLF:** paste text with Windows line endings: the digest equals the LF version.
