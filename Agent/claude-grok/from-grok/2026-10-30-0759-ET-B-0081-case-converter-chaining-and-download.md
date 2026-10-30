Sent: 2026-10-30 07:59 ET
# B-0081 Case Converter: chained conversions garble text; no download
Priority: P3      Estimated effort: 20–30 min      Report: #86      Source: Testing Bot (admin-session run)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
People try several cases in a row to compare them. Each button should convert the user's text, not the last output, and they should be able to save the result.

## Why
- Admin session, 1280, 30 Oct ~07:55 ET: aLtErNaTiNg then snake_case on the same text gives `h_el_lo_w_or_ld…`. Each mode rewrites the textarea and the next mode reads that output.
- Each mode alone is correct on fresh input (all 10 verified).
- No Download/.txt option, unlike Find & Replace and Random Number (Download .txt).
- Case Converter: 59 views (GA).

## Outcomes
Convert from the original input (keep it, show the output separately or keep "Reset to original"/Undo). Optional Download .txt.

## Constraints
Keep trial-use counting as it is for copy/download.

## Test cases
"hello world" → aLtErNaTiNg → snake_case gives `hello_world`; Reset restores the original; Download .txt contains the shown output.
