Sent: 2026-11-21 04:17 ET

# FDP-42: how to reproduce (guest, fresh browser profile, no sign-in)

**P1: full result at 0 trial uses**
1. Open https://www.freedailypro.com/tool/find-replace in a fresh profile.
2. Make sure the guest is at 0 trial uses: the account chip and `fdp-usage-v1.usageToday` show 10 used. On our box, fresh guest contexts arrived already at 0; otherwise use up the trial uses on a counted tool. `scripts/fr-gate.js 2` uses such a context.
3. Drop `F11_rich.docx`. Find "Acme Corp", replace with "Globex", click Replace All, then **Download Corrected .docx**.
4. The file downloads, with formatting kept and no cap dialog. Do the same with `F01_plain.txt` (Download Corrected File) and with pasted text.

**P1: never counted**
1. In a fresh profile with uses left, do several Replace Alls and Downloads.
2. `fdp-usage-v1.usageToday` and the account chip don't change.

**No upsell**
- Scroll the whole page at 0 and with uses left: there's no trial strip, pass offer or cloud save.

**P2: preserve case**
- Paste "Acme Corp, ACME CORP, acme corp", Find "acme corp", Replace "globex", and turn on Preserve case.
- You get "globex, GLOBEX, globex". "Globex" is expected for the first.

**P2: FAQ contradiction**
- Expand "Why might a replacement be missing in my .docx file?" and compare it with "Is my Word formatting kept…".
- Run step 3 of the first P1 with a phrase split across bold/italic runs: it is replaced.

**P2: video**
- https://www.youtube.com/watch?v=ZRbu9e3kDO4 around 0:05–0:40: bookmarks bar and taskbar visible, plus the "10 free uses daily" chip.

**P3 items**
- **.doc / .png:** drop `F08_old.doc` or `F10_image.png` and read the toast.
- **Broken .docx:** drop `F09_broken.docx`.
- **CSV:** in `F03_list.csv`, replace "Acme Corp" with "Globex, Inc" and download.
- **ReDoS:** Regex on, `(a+)+$`, text `aaaaaaaaaaaaaaaaaaaaaaaaaaaab`.
- **Blog:** `curl -s https://www.freedailypro.com/blog/find-replace | grep -o 'root"></div>amp;'`.

**Automated**
- `env -u BROWSER node scripts/fr-gate.js 12` (part 1 looks for a context with uses left; part 2 runs at 0).
- `node scripts/fr-live.js chromium`, then `firefox T01,T03,T05,T11,T13,T17,T20,T21,T23,T24` and the same with `webkit` (WebKit needs `GIO_EXTRA_MODULES`).
- `python testfiles/verify.py`.
- `node scripts/run-matrix.js scripts/config.json`.
