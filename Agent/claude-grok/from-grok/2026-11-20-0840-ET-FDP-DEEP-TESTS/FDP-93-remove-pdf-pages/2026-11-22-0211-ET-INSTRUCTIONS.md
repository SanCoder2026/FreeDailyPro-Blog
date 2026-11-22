Sent: 2026-11-22 02:14 ET

# FDP-93 package: how to use it

0. **File names:** every file in this zip starts with the send time `YYYY-MM-DD-HHMM-ET-` (box `date`, ET). Cross-references inside the documents leave that prefix out.
1. **Read first:** REPORT.md (first line `Sent:`), then PRIORITIES.md. Steps are in REPRODUCE.md and cases in test-cases.md. Details are in findings/; start with remove-findings.md, then peers-merge.md (checks 20/22).
2. **Scripts** (`scripts/`): Node scripts run from tools-env with `env -u BROWSER node`; Python with python3 (pikepdf, PyMuPDF, pypdf, pypdfium2, numpy, Pillow). Strip the date prefix first. See scripts/README.md.
3. **Evidence:**
   - `json/`: live runs, matrix, `verify-*.json` (one per output).
   - `files/`: downloaded outputs and `recovered-*.pdf`, the hidden removed pages rebuilt from them. The 49 MB heavy output is left out for size; its numbers are in err.json.
   - `testfiles/`: inputs. heavy.pdf is left out; make93.py copies it from #91.
   - `screens/`: JPG ≤1400 px (cases, recovered pages, matrix, video storyboard).
   - `js/` (incl. `new/` after the 01:24 ET deploy and `peers/`), `html/`, `blog/`, `video/`.
4. **Interruption:** the run was interrupted once, around 02:05 ET, after every live check had finished (a shell call failed to spawn, and the box's /workspace disk was 100 % full). On resume, nothing was rerun: the existing live JSON, downloads and verify output were used. Only the write-up and packaging were done afterwards. Earlier, book.pdf was rebuilt once with seeded images, so core was rerun as `core-r2` against the final file (the first core run was discarded). The site deployed new chunks at 01:24 ET mid-test. `Pt()` is unchanged, and core-r2, extra, err and capload ran on the new build.
5. **Rules:**
   - Guest only. No sign-in, payment, email or ad clicks.
   - deviceId, OAuth and Stripe IDs are redacted.
   - Test data is made up (the SSN is the well-known specimen 078-05-1120).
6. **Competitors:** findings/competitors.md.
Left out for size: heavy output (49 MB), capload-1/mobile-0/core-r2-1 book outputs (2.6 MB each; numbers in json/verify-A05r2.json, capload.json, mobile.json).
