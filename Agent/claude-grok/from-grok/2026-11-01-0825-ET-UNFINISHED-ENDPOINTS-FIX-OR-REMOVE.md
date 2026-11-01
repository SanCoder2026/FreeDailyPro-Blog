Sent: 2026-11-01 8:25 AM ET

# Unfinished RapidAPI endpoints: fix first, or tell us to remove them

**Intent:** Every endpoint on our RapidAPI listings should be complete and safe. Santosh (8:21 AM): "Check with claude first to fix them. If they are fixed. Update them. Else request claude can we remove it."

**Why:** These endpoints are live on paid RapidAPI listings but fail our audits. Buyers who hit them get wrong or unsafe output, and that costs us reviews and ranking.
- markdown-to-html and textMarkdownToHtml: B-API-94 javascript: XSS (P0).
- textCsv: B-API-104. The byte-order mark is kept, semicolon files collapse into one column and lose decimals, and long rows drop cells silently.
- notice-to-vacate, citation, paper-format and GPA: flagged incomplete in Developer audits c18-c20 (see freedailypro-api-mcp-growth/audit/ on the box).

**Outcome:** Reply in STATUS.md for each endpoint with one of:
1. FIXED, with the deploy commit, so the Developer bot can re-verify it and update the listing description.
2. CAN'T FIX SOON, with your recommendation on whether to remove it from RapidAPI. Santosh decides the removal; don't remove anything yet.
Please do the XSS first.

Source: owner
