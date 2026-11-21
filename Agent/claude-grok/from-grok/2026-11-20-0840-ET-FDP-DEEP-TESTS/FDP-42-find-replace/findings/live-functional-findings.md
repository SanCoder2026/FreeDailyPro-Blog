Sent: 2026-11-21 04:17 ET

# FDP-42 Find & Replace: live functional findings (guest, 2026-11-21 03:57–04:05 EST)

Raw data in `evidence/json/`: `gate-1.json` + gate1.log (uses left), `gate-2.json` + gate2.log (at 0), `cases-chromium.json`, `cases-firefox-subset.json`, `cases-webkit-subset.json`, `verify.json`, `privacy.json`, `blog-render.json`. The counter is `fdp-usage-v1.usageToday` in localStorage, which is display-only evidence.

## Gate and trial uses
- **The tool is uncounted, and the full result is available at 0 trial uses (P1 gate gap + policy question).**
  - **At 0** (`gate-2.json`, 03:57–03:58 EST; the counter read 10):
    - Pasted-text Replace All worked.
    - A .txt file Replace All worked: the full corrected text shows in an editable box, and Ctrl+A/C copied all 162 chars including the replacements.
    - **Download Corrected File** saved `F01_plain_edited.txt`.
    - A .docx Replace All + **Download Corrected .docx** saved `F11_rich_edited.docx` with formatting intact.
    - No cap dialog anywhere; the counter stayed at 10.
  - **With uses left** (`gate-1.json`, 03:59–04:00 EST; the counter started at 0):
    - Load, two reloads, typing, 5 pasted Replace Alls with Undo, a .txt Replace All + 2 Downloads, and a .docx Replace All + Download: the counter stayed at **0** throughout.
  - **Code:** `index-B1CTyGtY.js` `Ps` maps `"find-replace":["absorbable","text","Text utility on pasted text; a chat assistant does this for free"]`, and `TA()` treats "absorbable" tools as uncounted (`evidence/js/index-B1CTyGtY.excerpt-absorbable.js`). In `FindReplace-DrPESoBx`, Replace All only calls `logUsageNow` for pasted text and skips it when a file is loaded.
  - **Policy:** the Nov 20 decision names only Unit Converter, Grammar Checker and Word Counter as uncounted on purpose. Find & Replace isn't on that list, so this is a policy question. The code marks **99 tools** absorbable (list in the excerpt).
  - **Why P1:** the "pasted text, a chat assistant does this for free" reasoning doesn't fit the **.docx mode**. That mode is a formatting-preserving file job, which a chat assistant can't return as a Word file. Full-quality .docx downloads at 0 trial uses are the result.
- **Per-page-load charging:** N/A, because nothing is charged at all.
- **No upsell anywhere on the page:**
  - No trial strip, no "Quick Buy" / Day Pass / monthly offer, no badge note, no Save to Google Drive / my cloud storage on the result.
  - The only sign-in surface is "Open from Google Drive" on the drop zone (not clicked).
  - Check 5 (payment): there is no payment path from this page to test.
  - Against the "moved toward paid" goal: **FAIL**.

## Matching and replacing (Chromium, 28 cases; Firefox and WebKit subsets of 10 identical)
| Case | Result |
|---|---|
| T01 default (case-insensitive) | 5 matches incl. ACME CORP, acme corp and "Acme Corporation" → "Globexoration" (documented substring behaviour). PASS |
| T02 Whole word "cat" | 3 (catalog untouched). PASS |
| T03 Whole word + Preserve case | cat→dog, CAT→DOG, Cat→Dog. PASS |
| T04 Case sensitive | 3. PASS |
| T05 Regex `(\d{4})-(\d{2})-(\d{2})` → `$3/$2/$1` | 12/03/2026. PASS |
| T06 Invalid regex | "Invalid pattern — check your regex syntax", Replace All disabled. PASS |
| T07 `\n` in the replacement | real line breaks. PASS |
| T08 / T08b `^Call` with/without "^ $ match each line" | 1 / 0, as documented. PASS |
| T09 Named groups `$<m>/$<y>` | PASS |
| T10 Empty replacement | deletes. PASS |
| T11 Unicode whole word + preserve (café/CAFÉ/Café) | tea/TEA/Tea. PASS |
| T12 Emoji; T12b Cyrillic whole word | PASS |
| T13 JSON broken by the edit | warning toast "…broke the JSON's structure"; file still downloads. PASS |
| T14 XML broken | warning toast. PASS |
| T15 CSV: replace with "Globex, Inc" | P3: the unquoted row gains a column (`Jane,Globex, Inc,2026-03-12`) with no warning |
| T16 HTML / MD | PASS |
| T17 .doc | P3: generic toast "can't be used here. Check the file type this tool accepts." The FAQ promises "refused with advice to save it as .docx", and that message exists in code but never shows (the shared drop zone rejects first). |
| T18 .png | P3: same generic toast; the FAQ promises "a message listing the supported types" |
| T19 broken .docx | P3: raw "Corrupted zip: can't find end of central directory" |
| T20 .docx | 6 replacements. A phrase split across bold/italic runs is found and takes the first run's bold; red 16 pt formatting kept; table cell replaced; image kept; header/footer unchanged and a phrase across two paragraphs unchanged (both documented). PASS |
| T21 .docx Preserve case, "acme corp" → "globex" | **P2:** Title-Case "Acme Corp" → "globex" (lower-case), while ACME CORP → GLOBEX. Multi-word title case isn't recognised (`utils-CRM_dY3d` `M()`). The blog admits it, but the tool's FAQ doesn't. Renaming a product is the headline use. |
| T22 .docx regex `\{\{name\}\}` → Jane | PASS (template fill) |
| T23 6.4 MB .txt, 120,000 matches | counter instant; Replace All 5.1 s; download OK. PASS |
| T24 Undo | restores the text; "Last replace undone."; one step only (documented). PASS |
| T25 Regex `(a+)+$` on 28 "a"s + "b" | **P3:** the tab freezes about 3 s on typing (live counter) and about 11 s on Replace All. It grows exponentially, with no timeout or worker. |
| T26 `x*` | "-a-b-c-" (standard JS). PASS |
| T27 / T28 `$&!` literal vs regex | literal outside Regex, whole match inside. PASS |
- **.docx has no live counter** (documented), so the first number appears only after Replace All. P3.
- Downloads keep the original name + `_edited`, UTF-8, no BOM, LF line endings (`verify.json`).

## Privacy
After a .docx drop, replace and download, the only requests were a page GET, one small site POST, and analytics/ad pings. No request carried the file name or document words (`privacy.json`). PASS.
