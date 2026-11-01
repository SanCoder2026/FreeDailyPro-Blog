# Student Loan Calculator mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)

| # | Fix | Problem (measured) | Why / competitor | Effort |
|---|---|---|---|---|
| 1 | Sticky result card above the fields (sticks under header while typing): Monthly payment $477.54 · Debt-free Nov 2033 · Interest $10,368 · "+$150/mo saves $4,937" | Payment y1187, ~375px below fold | NerdWallet y3902, Bankrate/Calculator.net need a Calculate tap — we'd be the only one visible at load | S |
| 2 | 44px inputs; fold First payment date + lump sum + grace-period note into a 44px "More options" toggle (help text as ⓘ) | Inputs 36px; ~9 lines of help before results | Shorter form; result + fields fit one screen | S |
| 3 | Amortization table: Month/Payment/Interest/Balance only on mobile (Date + Principal in a tap-to-expand row), 44px "Show all 120 months" / Download CSV | 429px table in 341px box, Balance hidden off right | Readable without sideways swipe | S |
| 4 | Action buttons 44px (Copy report, Print, Copy result, Save as text); Clear 31×16 → 44px | 32px / 16px | S3 | XS |
| 5 | JSON-LD Offer price 0 → drop, or list the real Professional tier offer ($1 day / $4.99 month — not $9.99) | Schema "free" | Same "Free" decision | XS |
| 6 | Block the "cash advance / payday" ad category in AdSense for finance tools (ads stay; only that category is blocked) | Anchor showed "Get Cash Advances" | Trust on a debt tool | XS (AdSense setting) |
| Shared | S1 header overflow, S2 floaters (cover result cards), S3, S4 smart ad placement (keep all ads; anchor offset above sticky bars; auto-ads excluded from tool area; reserved slots below result/after download/between sections — see ads-plan-standard.md), single buy link "$1 day pass · $4.99/month" | — | — | — |

## 1. Sticky result card
```css
.sl-summary{position:sticky;top:64px;z-index:30;margin:0 0 14px;padding:12px 14px;border:1px solid var(--border);border-radius:12px;background:var(--card);box-shadow:0 6px 16px rgb(0 0 0/.35)}
.sl-summary .pay{font-size:26px;font-weight:800;color:var(--primary)}
.sl-summary .meta{display:flex;justify-content:space-between;font-size:13px;color:var(--muted-foreground)}
@media (min-width:768px){.sl-summary{position:static}}
```
(JSX: render the existing payment/payoff/interest values in `.sl-summary` above the Loan Balance field; keep the full result cards below.)
## 2. 44px + More options
```css
@media (max-width:640px){ .sl-form input,.sl-form select{min-height:44px} .sl-more{min-height:44px;width:100%} .sl-help{display:none} .sl-more[aria-expanded=true]+.sl-extra .sl-help{display:block} }
```
## 3. Table
```css
@media (max-width:640px){ .sl-amort th:nth-child(2),.sl-amort td:nth-child(2),.sl-amort th:nth-child(5),.sl-amort td:nth-child(5){display:none} .sl-amort table{min-width:0;width:100%} }
```
Mockups: fix1-sticky-result-before-after.png, fix2-44px-fold-extras-before-after.png. Browser-injected mockups, not live code.


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.


---
**Changelog — Nov 1 2026 (pricing tier rule):** Santosh's rule: Professional Tools = 10 trial uses/day, $1 day pass, $4.99/month; Premium Applications = 2 trial uses/day, $3 day pass, $9.99/month; Workflow Products = own plan $29.99 or $49.99/month, not covered by passes. Schema offer clarified to Professional tier.
