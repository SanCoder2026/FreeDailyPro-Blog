Sent: 2026-10-31 11:17 AM ET

# ADDENDUM 1 — P1 CONVERSION-PRIORITY: free-use counter vs gate mismatch (B-0156 family), now on 2+ tools

Updates: 2026-10-31-1112-ET-FLAG-conversion-priority-extract-charts-counter.md. **Priority raised to P1.**

**Intent:** The free-use counter must never promise uses that the paywall then refuses. Today a visitor sees "10 remaining" and gets blocked on the very first action, which breaks trust right at the moment they'd decide to buy.

**Why P1:** This is no longer a one-tool bug. QA-REPORT-196 (case 2) found it on **giveaway-winner-picker** as well: the header showed "10 remaining today" on load, Draw then opened the "You've used today's trial uses" dialog, and the header dropped 10 → 0. That's the same pattern as extract-charts-powerpoint (QA-REPORT-193 case 4). It looks like a shared cause, possibly a daily count shared across tools per visitor or a header that reads a different source than the server gate (unverified).

**Outcome:**
- One source of truth for remaining uses. Header, tool box and server gate always show the same number before any action.
- If the count is shared across tools, say so in the UI. Otherwise make it per tool, as the copy implies.
- An audit of every gated tool, with the list of affected tools reported back. Don't stop at these two.
- A blocked action always shows a clear Day Pass / Monthly prompt, never a silent no-op.
- No Stripe settings or price changes. The Stripe webhook stays the only purchase signal.

## Consistency notes (QA-REPORT-196)

1. **Tool name:** about 20 blog posts write "Guest List Tracker" in the body text, while the tool, the lists and the link buttons say "Guest List & RSVP Tracker". Update the blog bodies to "Guest List & RSVP Tracker".
2. **Tool count:** the site says "300+ tools" on the homepage, /tools, the header search placeholder and /contact. But /tools links 359 pages and the sitemap has 379. Tie this to **B-0322 S-1 (one source for every count)**: work out the real tool count once (and explain why /tools and the sitemap differ), then drive every displayed count from that single source.

Source: owner
