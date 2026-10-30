Sent: 2026-10-30 14:42 ET

# B-0270 User-Agent Parser: accurate, but copy/save cost a trial use; add JSON, bulk mode and Client Hints; rewrite title and meta
Priority: P3 · Estimated effort: S · Report: #148 · Source: curl + seo.py, Playwright headless logged out at 1280/390 px, Google top 5 (WebSearch), 2026-10-30 ~14:36–14:41 ET. SEO backfill 11: GA top-50 list (raw analytics line 29) is exhausted after user-agent-parser (#49), so the next picks follow the GSC Top 50 pages list by clicks among tested tools.

How to work with us: tell us what you changed and how you checked it. If the intent and a test case conflict, follow the intent and flag the conflict.

## Intent
A developer pasting a UA from a log should get browser, OS, device and bot status, and copy the result into a ticket.
## Why
- **GA:** /tool/user-agent-parser 47 views (raw analytics line 29, rank 49). No GSC row in the captured top 50.
- iPhone Safari 18.1 UA → Mobile Safari 18.1, iOS 18.1, Mobile, Apple iPhone, WebKit, CPU "—", Bot No. ✔ (L-239 already verified 7 UAs.)
- Page says "Reading results never uses a trial use. Copying, saving or printing uses 1 per visit." At 0 trial uses, Save as text opens "Your result is ready… needs a pass" (owner's decision).
- **Missing vs competitors (~14:40 ET):** copy/export as JSON (AnyTool, OpenReplay, Wivrix); bulk mode for log lines with CSV/JSON export (Wivrix); Client Hints panel to tell Windows 10 vs 11 (AnyTool, PithLab, Wivrix); a named-bot list incl. AI crawlers GPTBot/ClaudeBot (PithLab, Wivrix); a "UA can be spoofed — verify bots by reverse DNS" note (PithLab, ShowIP).
- No overflow at 390 px. /es serves the English title → L-189 / **B-0123**.
## Who uses this
Developers, SEOs checking crawler hits, support staff.
## Outcomes (ranked)
1. Copy as JSON.
2. Bulk mode (one UA per line → table, CSV).
3. Client Hints for "my browser"; named bots incl. AI crawlers.
## SEO
- **Now:** 200, canonical, 11 hreflang, valid JSON-LD (SoftwareApplication, VideoObject, FAQPage, BreadcrumbList).
  - Title "Parse a User Agent String Online - Free Tool | FreeDailyPro" (59, has "Free"). **Meta 98.** H1 "User-Agent Parser".
- **Keywords:** "user agent parser", "parse user agent string", "what is my user agent", "detect bot user agent".
- **Suggested:**
  - Title: `User Agent Parser – Browser, OS & Device | FreeDailyPro` (55)
  - Meta: `Paste any user-agent string to see its browser and version, operating system, device type, engine and whether it is a bot. Parsing runs in your browser.` (152)
  - H1: `User Agent Parser: Browser, OS, Device and Bot`
  - FAQ: "Can a user agent be faked?" · "How do I tell Windows 10 from 11?" · "Is my UA sent anywhere?"
## Constraints
Website tool only; keep the trial-uses rule per the owner.
## Test cases
1. iPhone Safari UA → Mobile Safari 18.1 / iOS 18.1 / Apple iPhone.
2. Title ≤ 60, no "Free"; meta 140–160.
