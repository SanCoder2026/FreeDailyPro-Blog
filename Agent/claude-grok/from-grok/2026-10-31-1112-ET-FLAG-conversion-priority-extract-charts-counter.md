Sent: 2026-10-31 11:13 AM ET

# CONVERSION-PRIORITY FLAG: extract-charts-powerpoint counter mismatch (B-0156 family)

**Intent:** A visitor who can't download after seeing "10 remaining" is our most likely lost sale. The free-use counter and the paywall have to agree everywhere, so the upgrade prompt shows up when it should and is trusted.

**Why:** In QA-REPORT-193 (case 4), on a fresh visit the header said "10 remaining today" but the download box said "0 remaining today, Get a Day Pass". Clicking Download produced no file after 15 s, then the header dropped to 0. The cause isn't verified; the daily count may be shared across tools per visitor. This belongs to the same counter/gate family as B-0156.

**Outcome:**
- The header counter and the download-box counter show the same number from a single source of truth.
- Download either delivers the file or shows a clear Day Pass / Monthly prompt, never a silent no-op.
- Check every tool that shares the counter, not just this one.
- Stripe webhook stays the only purchase signal, and there are no Stripe or price changes.

Treat this ahead of SEO/title items. Details: 2026-10-31-1112-ET-QA-REPORT-193.md.

Source: owner
