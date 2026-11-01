Sent: 2026-10-31 23:45 ET (Grok Orchestrator)

# P0: Workflow Stripe prices + /pricing & /developers copy

## Intent
Every workflow toolbox must be buyable at $29.99/mo with a 7-day trial, and /pricing + /developers must explain access and billing in one read with no unenforced or outdated claims.

## Why
Event Suite checkout is verified live by Santosh ($29.99/mo, 7 days, $0 today). But as of 23:08 ET Stripe shows no active $29.99/mo price for Book Toolbox, Seller Studio or Legal Production Desk, and the old book packs are still active. Copy still claims an unenforced "10 trial tries per hour" and "Single book tools sold separately", which conflicts with the $29.99-only Book rule.

## Outcome
1. Book, Seller Studio, Legal Production Desk each have an active $29.99/mo + 7-day trial Stripe price wired to their Start-trial button. Archive (don't delete) old book pack prices and the $3.99 pass once checkout works.
2. /developers hero + /pricing API section: "One API key. REST and MCP. One shared quota." Sub: "Use the same key for our 200+ REST endpoints and 200+ MCP tools. Every call, REST or MCP, counts toward one monthly quota." Plan note: "Start with 20,000 trial calls a month. Then $24 for 200k, $69 for 750k, or $129 for 2M with priority support."
3. Under every Subscribe/Buy button: "Sign in, then pay securely with Stripe." FAQ "How does checkout work?": sign in first so the plan attaches to your account, then Stripe secure checkout; cancel anytime from your account.
4. Remove "10 trial tries per hour" everywhere (B-API-14 not enforced). Keep "10 trial uses per day on each tool" only if enforced; otherwise drop it.
5. /pricing Book card: delete "Single book tools sold separately". Body: "Book Writing Toolbox: $29.99/month. 7-day trial. Everything to write, format and export your book. Previews are watermarked, and clean files download on your plan. Cancel anytime." Remove leftover $6.99/$17.99/$49.99 packs, AI pack prices and $3.99 pass from /pricing, FAQs and in-tool upsells.
6. /developers: remove the "Honestly: … OCR, Word and Excel" line (don't publish incomplete capabilities); update "Status checked 24 Oct".

Report status per item; Testing Bot will verify checkout without paying.

Source: owner
