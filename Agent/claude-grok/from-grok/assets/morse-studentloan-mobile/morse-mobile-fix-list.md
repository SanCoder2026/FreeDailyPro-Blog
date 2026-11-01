# Morse Code Translator mobile — ranked fix list (proposals; needs Santosh's approval; nothing sent to Claude)

| # | Fix | Problem (measured) | Why / competitor | Effort |
|---|---|---|---|---|
| 1 | Touch controls: 48px mode tabs + ⇄ swap button (swaps text and direction); speed as −/slider/+ 44px row; Extended toggle as 44px row; big full-width **▶ Play · 15 WPM** (+ Stop) and Copy 48px; output textarea auto-grows; highlight the letter being played | Tabs/Copy/Play 36px, toggle 32×18, slider 28px; output fixed 90px | All 3 competitors use 16px play icons — we'd have the easiest audio on mobile | S |
| 2 | Tap-to-hear A–Z chart card under the tool (26 × 44px keys, "Numbers 0–9 and punctuation ›"), and move the "Discover more" unit to a reserved slot below the chart (S4 smart placement — kept, not removed) | Google "Discover more" auto-ad list sits right under Play; no chart on page | Competitors only link out to a chart; learners want it inline | S |
| 3 | Play should not spend a trial use (only translate/copy count, or none — it's all on-device) or say so: "Play uses 1 trial use" | Play: 10 → 9 remaining | Surprise use-burn on a 2-second beep | XS |
| 4 | JSON-LD: drop `"price":"0"` Offer (or list the Professional tier Offer $4.99/month; Invoice lists 9.99 because it is Premium) | Schema says free | Same "Free" decision as Split/Rotate PDF | XS |
| 5 | Regenerate video thumbnail text "200+ professional tools" → "300+ tools" | Inconsistent with site search "300+ tools" | Counts rule | XS |
| Shared | S1 header overflow (377), S2 floaters, S3 44px, S4 smart ad placement (anchor kept, auto-ads excluded from tool area, reserved slots), single buy link "$1 day pass · $4.99/month" | — | — | — |

## 1. Touch controls
```css
@media (max-width:640px){
 .morse-modes{display:grid;grid-template-columns:1fr 48px 1fr;gap:8px}
 .morse-modes button{min-height:48px;width:100%}
 .morse-speed{display:flex;align-items:center;gap:10px}
 .morse-speed button{width:44px;height:44px}
 .morse-speed input[type=range]{flex:1;min-width:0;height:44px}
 .morse-ext{min-height:44px;display:flex;align-items:center;gap:12px}
 .morse-actions{display:grid;grid-template-columns:2fr 1fr;gap:8px}
 .morse-actions button{min-height:48px;font-size:16px}
 .morse-actions .play{background:var(--primary);color:var(--primary-foreground);font-weight:700}
 textarea.morse-out{field-sizing:content;min-height:90px}  /* + JS fallback: el.style.height=el.scrollHeight+'px' */
 .morse-out .playing{background:color-mix(in srgb,var(--primary) 30%,transparent);border-radius:3px}
}
```
## 2. Chart
```css
.morse-chart{margin-top:16px;border:1px solid var(--border);border-radius:12px;padding:12px}
.morse-chart .keys{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.morse-chart button{min-height:44px;font-size:14px} .morse-chart code{color:var(--primary)}
```
Mockups: fix1-touch-controls-play-before-after.png, fix2-chart-no-autoad-before-after.png (crop1/2-*-before/after.png). Browser-injected mockups, not live code.


## Changelog
- Nov 1 2026: ads rework per Santosh's standing ads rule — removed/turned-off ad suggestions rewritten as smart placement (keep all ads, more slots at natural breaks). See /workspace/web-design/ads-plan-standard.md.

## Ads plan (standing rule, Nov 1 2026)
- Keep every existing ad: anchor, auto-ads, "Discover more", in-content units. Nothing removed or turned off.
- Anchor: stays; sticky action bar sits at `bottom: calc(var(--anchor-h,60px) + 8px)` so it never covers buttons/inputs/results/Download.
- Auto-ads: excluded from the subtitle and tool area (`.tool-area` / `google-auto-ads-ignore`); allowed in content below.
- New reserved slots (fixed min-height, no layout shift): below the result card, after Download success, between About/guides and FAQ, before footer; desktop right sidebar (300×600 sticky).
- Never inside the drop zone → action → result → Download path.


---
**Changelog — Nov 1 2026 (pricing tier rule):** Santosh's rule: Professional Tools = 10 trial uses/day, $1 day pass, $4.99/month; Premium Applications = 2 trial uses/day, $3 day pass, $9.99/month; Workflow Products = own plan $29.99 or $49.99/month, not covered by passes. Schema offer wording clarified by tier.
