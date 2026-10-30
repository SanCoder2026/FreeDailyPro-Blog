Sent: 2026-10-30 13:12 ET

# B-0156-v2 — Zero-trial behaviour: owner decision made

## Intent
Santosh decided at 2026-10-30 13:12 ET: **keep the limit.** Copying and viewing results count against the daily trial in every tool, Emoji Picker included (B-0142). The same applies to Paper Format Checker (B-0149), Base64, URL Encoder, JSON and SQL Formatter, and Document Scanner. Do **not** exempt copy or results. This settles the policy part of B-0156.

## Why
The trial limit is how the site converts users to paid. Competitors offering free copy is not a reason to give it away. What matters is that hitting the limit feels clear and honest, never broken.

## Outcomes (one shared component, every tool)
- At 0 trial uses, any action shows one consistent paywall. It states the real reason ("You've used today's trial uses"), shows when the trial resets, and offers the Day Pass and plan options. The wording must match the action (copy, format, or download) and must never say "download" for a copy.
- Never a false "Copied" toast, a blank output, files silently dropped (Audio Merger, Merge Video, Mesh Viewer), or the paywall and a success toast at the same time.
- The counters must agree: header, build panel and the actual uses consumed (L-143 and B-0055 evidence). One action costs exactly one use.
- Inputs the user already added stay in place behind the paywall, so they don't lose their work after paying.
- B-0142 and B-0149 close as "limit kept by owner". Only the broken-state fixes above remain.

## Acceptance
The Testing Bot reruns every row listed in B-0156 at 0 trial uses and confirms there are no false toasts, no blank output and no dropped inputs. It also checks that the paywall wording is correct for each action and that the counters match.

Source: owner
