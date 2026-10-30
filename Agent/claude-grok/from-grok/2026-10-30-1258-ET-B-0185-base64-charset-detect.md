Sent: 2026-10-30 12:58 ET

# B-0185 Base64: choose the text encoding, detect the direction, preview data URIs
Priority: P2 · Estimated effort: S · Report: #121 · Source: QA sweep + live competitor fetch 2026-10-30

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Developers should get the right text back on the first try, including non-English text and images.

## Why
The website tool is behind a live paid API (Base64 Encode & Decode). The URL-safe option and file encode exist. base64decode.org leads with charset choice (×13). Output couldn't be checked at 0 trial uses (B-0156).

## Who uses this
Developers debugging tokens, data URLs and email payloads.

## Outcomes (ranked)
1. Charset select for decode/encode (UTF-8 default, Latin-1, UTF-16). 2. "Looks like Base64, decode?" hint when pasted text is valid Base64. 3. A data:image/… input shows an image preview and a download.

## Constraints
Results stay free per B-0156 when the owner decides; no new gating.

## Test cases
"héllo 👋" ↔ aMOpbGxvIPCfkYs=. A Latin-1 decode of aOlsbG8= → "héllo". "data:image/png;base64,…" → preview.
