Sent: 2026-10-30 11:27 ET

# B-0149 Paper format checker: show the check, handle bad files, cover references
Priority: P2 · Estimated effort: S–M · Report: #111 · Source: QA sweep + live competitor fetch 2026-10-30 11:25 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
The check is the value. Students should see what is wrong with their paper, and they should get a clear message for a bad file.

## Why
At 0 trial uses, uploading a .docx opens the paywall with no results, which contradicts "Reading results never uses a trial use". A non-docx makes the drop zone disappear silently. Scribbr's APA guide centres on title page, running head and hanging-indent references, which we do not list.

## Who uses this
College students before submission (174 GSC impressions).

## Outcomes (ranked)
1. Owner decision: show the pass/fail list at 0 trial uses, and gate only the fix or download. 2. "This isn't a valid .docx" message for bad files. 3. Check reference-list hanging indent (0.5 in) and title-page basics. 4. Label the "Check against" control.

## Constraints
Runs on device; never upload the paper.

## Test cases
apa-good.docx (1 in margins, Times 12, double spacing) → all pass. apa-bad.docx (0.5 in, Arial 10, single) → margin, font, size and spacing flagged. notdocx.docx → error message.
