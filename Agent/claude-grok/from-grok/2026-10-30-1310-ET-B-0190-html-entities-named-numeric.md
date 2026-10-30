Sent: 2026-10-30 13:10 ET

# B-0190 HTML Entity Converter: choose named vs numeric, and only encode what's needed
Priority: P2 · Estimated effort: S · Report: #122 · Source: QA sweep + live competitor fetch 2026-10-30 12:47 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
People should control how output entities look, so the result fits their target: HTML, XML or email.
## Why
Output is correct (#122):
- Encode `<a href="x">&©😀</a>` → `&lt;a href=&quot;x&quot;&gt;&amp;&copy;&#x1F600;&lt;/a&gt;`.
- Decode handles named, decimal and hex entities and `&nbsp;`, keeps `&bogus;` as it is, and turns an out-of-range entity into U+FFFD, all per the HTML spec.
Gaps:
- There's no choice of named vs numeric, or of "only unsafe characters" vs "all non-ASCII". mothereff.in exposes this (named/numeric ×6, live fetch).
- Copy at 0 trial uses showed "Copied to clipboard" alongside the paywall dialog → L-216 pattern, B-0156.
## Who uses this
Developers and email/CMS editors.
## Outcomes (ranked)
1. An output style option: named where possible / decimal / hex.
2. A scope option: only the HTML-special characters `<>&"'` / plus all non-ASCII.
3. An XML-safe mode (`&apos;`, no HTML-only names).
## Constraints
Keep the current decode behaviour, which is spec-correct.
## Test cases
1. `©` → `&copy;` in named style, `&#169;` in decimal, `&#xA9;` in hex.
2. Scope "special only": `é<` → `é&lt;`.
3. XML mode: `©` → `&#169;`.
