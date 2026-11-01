Sent: 2026-11-01 09:09 AM ET

# Checkout FAQ accuracy: sign-in isn't Google-only

**Intent:** Keep the live two-path checkout FAQ (aa53fe8, confirmed live on /pricing and /developers at 9:08 AM ET by QA) accurate.

**Why:** Path 1 says "sign in with Google first". Email-link sign-in also works; QA used it today for a non-admin account. Users who can't use Google could think they're blocked.

**Outcome:** Path 1 (Workflow Products, API plans, org seats) reads "sign in (Google or email link) first", in both the visible FAQ and the FAQPage JSON-LD. Change nothing else.

Source: owner
