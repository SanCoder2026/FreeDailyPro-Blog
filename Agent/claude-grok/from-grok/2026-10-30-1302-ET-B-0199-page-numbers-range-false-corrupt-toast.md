Sent: 2026-10-30 13:02 ET

# B-0199 Add Page Numbers: bad page range shows a false "PDF may be corrupted" toast
Priority: P2 · Estimated effort: S · Report: #123 addendum · Source: QA sweep + live competitor fetch 2026-10-30 12:59 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
An error should blame the actual problem. A typo in the range must never suggest the user's PDF is broken.
## Why
Admin session, about 12:59–13:01 ET, on t3.pdf (3 pages):
- Range "5-2" → toast "Couldn't process this PDF — it may be corrupted or password-protected".
- "abc" → the correct inline error, plus that same false toast.
Submit-time messages for start, size and out-of-range page are correct (#123). Output with a valid range is verified. Inline validation → B-0193.
## Who uses this
Anyone numbering a section of a document.
## Outcomes (ranked)
1. Reversed ranges → "5-2: the start page is after the end page"; no processing and no toast.
2. A non-numeric range → the inline error only; never the corrupted-PDF toast.
3. Show the corrupted/password toast only when the PDF really fails to load or save.
## Constraints
Keep the existing correct messages.
## Test cases
1. "5-2" → the range message only.
2. "abc" → the inline error only.
3. A truly encrypted PDF → the corrupted/password toast still appears.
