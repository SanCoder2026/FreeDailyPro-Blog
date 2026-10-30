Sent: 2026-10-30 13:02 ET

# B-0198 JSON Formatter: "JSON → YAML" button does nothing
Priority: P2 · Estimated effort: S · Report: #123 addendum · Source: QA sweep + live competitor fetch 2026-10-30 12:59 ET

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
Every action button either produces its result or says why it can't.
## Why
- Admin session, about 12:59–13:01 ET: "JSON → YAML" was clicked twice on valid JSON. There was no output, no error and no toast.
- Format and Minify work in the same session, including keeping the big integer exactly.
- This is a working-feature bug; the generic no-silent-no-op rule is B-0187.
## Who uses this
Developers converting config files (Kubernetes, CI).
## Outcomes (ranked)
1. JSON → YAML writes YAML to the output: correct for nested objects and arrays, with strings like "yes", "no" and "007" quoted so they survive a round trip.
2. If the conversion fails, the B-0187 status shows the reason.
## Constraints
Don't change Format or Minify.
## Test cases
1. `{"a":{"b":[1,"yes","007"]}}` → `a:` / `  b:` / `    - 1` / `    - "yes"` / `    - "007"`.
2. YAML → parsing it back gives identical JSON.
