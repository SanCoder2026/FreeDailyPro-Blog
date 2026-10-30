# B-0074 JWT / UUID / Hash: meta descriptions too thin
Priority: P3      Estimated effort: 15 min      Report: #79      Source: Testing Bot

**How to work with us:** you are the implementation partner. Inspect the code, challenge anything below that it contradicts, and choose the fix. Process: inspect → restate → propose → implement → verify live → report per brief ID.

## Intent
Developer searchers should see the real capabilities in the snippet: file hashing and checksum compare, exp/iat expiry check, bulk 1,000 UUIDs.

## Why
- Meta lengths: JWT 73, Hash 74, UUID 76 chars. GSC: "jwt decode online" 1 click / 76 impressions, position 8.4.
- Verified #79: Hash now does files (3 MB SHA-256/MD5 match) with checksum compare; JWT strips "Bearer" and flags "Expired"; UUID makes 1,000 per batch in upper/no-hyphen.
- jwt.io, uuidgenerator.net and emn178 describe input encodings/HMAC; ours doesn't mention its edge.

## Outcomes
Each meta is 130–160 chars and names 2–3 verified capabilities, including "runs in your browser".

## Constraints
"Free" in tags is OK. No claims beyond what was verified.

## Test cases
View source on the 3 pages: meta 130–160 chars; it mentions file checksum (hash), expiry (JWT), bulk 1,000 (UUID).
