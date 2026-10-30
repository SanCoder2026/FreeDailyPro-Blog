Sent: 2026-10-30 07:59 ET
# B-0082 Universal Converter: blob URL console errors; scripted download click fails
Priority: P3      Estimated effort: 15–30 min      Report: #87      Source: Testing Bot (admin-session run)

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
A clean download path, so downloads work on every click type (keyboard, assistive tech, automation) and the console isn't noisy.

## Why
- Admin session, 1280, 30 Oct ~07:57 ET, JPG → PNG: the console shows repeated `ERR_FILE_NOT_FOUND` on `blob:` URLs. A scripted `.click()` on Download fired no download; a real mouse click did.
- That usually means the object URL is revoked or re-created before or while it is used, or the handler relies on pointer events. Keyboard (Enter/Space) and screen-reader activation may fail the same way.
- The output itself is fine: a real 1200×800 PNG.
- /tool/universal-file-converter: 129 views (GA raw, rank 11).

## Outcomes
No blob errors in the console; Download works by mouse, keyboard and programmatic click. Revoke object URLs only after the download starts.

## Constraints
No change to gating (see B-0070, still open).

## Test cases
Convert JPG→PNG; press Tab to Download + Enter → file saved; `element.click()` → file saved; console has no ERR_FILE_NOT_FOUND.
