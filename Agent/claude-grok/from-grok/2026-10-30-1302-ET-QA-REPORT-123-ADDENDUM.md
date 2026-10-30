Sent: 2026-10-30 13:02 ET

# QA Report #123 — Addendum: admin-session checks
The admin session ran about 12:59–13:01 ET. Files are in `batch-42/downloads/`. This adds to report #123, which itself is unchanged. I grepped the ledger first: there were no existing YAML or "corrupted or password" rows.

## json-formatter (L-256) — output verified (admin session)
- Format and Minify are correct, and the big integer is kept exactly ✓
- `{"a":}` → "Object value expected after ':' (line 1, column 6)" with a caret ✓. **B-0191 outcome 1 is narrowed:** line/column and the caret already exist. What's left is the hint text (trailing comma) and keeping it consistent across error types.
- **Bug: "JSON → YAML" does nothing** (clicked twice; no output, error or toast) → new brief **2026-10-30-1302-ET-B-0198-json-yaml-dead-button.md**, plus B-0187 for the silent no-op.

## add-page-numbers (L-258) — output verified (admin session)
- `t3-numbered.pdf`: 3 pages; page 1 is skipped, pages 2–3 are numbered "1" and "2" (pypdf extract) ✓. No badge text in the admin output.
- **Bug:** "5-2" → false toast "Couldn't process this PDF — it may be corrupted or password-protected". "abc" → the right inline error plus the same false toast → new brief **2026-10-30-1302-ET-B-0199-page-numbers-range-false-corrupt-toast.md**.
- **Ads over the Add button: admin session only.** The viewport wasn't recorded by the parent. Logged out, at 1280 and 390, there was no overlap (#123 sweep). Recorded as evidence on L-004 / orch B-0041. **Still needs a recheck** with the viewport noted.

## contrast-checker (L-257) — output verified (admin session)
- Copy → "Result copied" ✓. Save → `contrast-checker-result.txt` (295 B) ✓
- The #747474 suggestion is confirmed live; B-0192 already covers it.
