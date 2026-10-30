Sent: 2026-10-30 13:21 ET

# QA Report #122 — Addendum: admin-session output checks
The admin session ran about 12:53–12:56 ET. Results were reported by the parent and are recorded as verified. This adds to report #122, which itself is unchanged.

## url-encoder (L-254) — output verified (admin session)
- Encode `a b&c=ü/?` → `a%20b%26c%3D%C3%BC%2F%3F`, and decoding round-trips ✓
- Decode `%E0%A4%A` → 'Malformed escape "%A" at position 7 …', with the input marked invalid ✓
- **Polish note (added to B-0189):** when that error shows, the Output box keeps the previous value. It's the same stale-output pattern as B-0154 (paraphraser) and L-228. The output should be cleared or marked stale on error.

## html-entity-converter (L-255) — output verified (admin session)
- Encode `<a>&"é` → `&lt;a&gt;&amp;&quot;&eacute;`, and the clipboard matched ✓

## diff-checker (L-253) — output verified (admin session)
- The diff is correct. "Result copied" appears.
- `diff-checker-result.txt` (158 B) includes the footer ✓
- The page states that Copy, Save and Print use 1 trial use per visit.

## markdown-html-converter (L-252, follow-up to the #121 addendum)
- With "Full HTML document" on, the download is a complete document (199 B). **The "fragment" capability-gap note in the #121 addendum is withdrawn.** The default (off) fragment is by design. The 390 px overflow is still open.
