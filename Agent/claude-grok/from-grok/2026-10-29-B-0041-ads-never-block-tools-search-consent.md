# B-0041 Ads must never block tools (mobile first) + homepage search Enter affordance + consent/GA fixes

**Priority:** P1
**Estimated effort:** ~3–4 h

**How to work with us:** you're the implementation partner, not an order-taker. Inspect the real codebase and our past deploy patterns, challenge anything weak, and pick the best implementation. Process: inspect → restate → propose → implement → verify live (desktop + iPhone-size) → report per brief ID.

Context: read-only review on Oct 29 2026 of GA4 (Jul 10–Oct 29 2026, since company start), Search Console (same range), AdSense (live since ~Oct 24) and a live ad-UX check on desktop 1920x1072 and iPhone-size 393x852. Builds on B-0037 (analytics cleanup) and B-0038 (ad placement); where they overlap, this brief adds the UX evidence and takes precedence on "ads vs tool areas".

## Intent
Tools come first. An ad must never cover, push, or sit on top of a tool's inputs, buttons or results, especially on mobile, where we get good traffic. At the same time we want ads to actually serve: today most visitors, and almost all mobile visitors, never get one. And the homepage search, which people love, must never look broken.

## Why (evidence)
- **Side-rail ads overlap tools (desktop).** /tool/audio-comparer, our top Search page (122 clicks): fixed side rails (~200x606 at x≈381 and x≈1324, y≈175) cover BOTH dropzones. The "Drop first/second audio file" labels and "File 1" are hidden, and clicks are blocked on the rail area. This still happens at ~900px window width. /tool/merge-pdf: rails (160x606) sit inside the content width and cover the "About" text, the subtitle badges and the right edge of the video block. The rails are placed in the content, not in the margins.
- **Mobile problems (393x852):**
  - audio-comparer has a ~160px empty slot between the badges and "Audio File 1". It collapses when the ad is unfilled, so the content jumps (CLS).
  - The bottom inline square ad (~393x400) overflows the right edge and cuts off its own button.
  - Sticky ad-intent anchors ("Get Converters", "Compare Browsers") stay over the content and CTAs.
  - A Google "Discover more" panel stacks with our floating back/home/feedback buttons.
  - The roman-numeral page has a small horizontal scrollbar ("Month.Day.Year (US)" clipped).
- **Ad intents inject into our copy:** in-text links ("software") and chips ("Try Cloud Tools", "Stream Albums", "Look Up Facts") show up inside hero and subtitle text, and the anchor popups float over tools.
- **Mobile ad gap:** AdSense counts 75 mobile page views (viewability 6.15%) vs ~1,271 GA mobile users. Desktop is 975 PV at 27.84%. Total: 173 impressions vs 16,258 GA page views, $0.39 so far.
- **Consent gating:** on first visit the banner has the Analytics and Advertising boxes UNCHECKED, and it covers the bottom ~100px of the first screen. Visitors who don't opt in get no GA and no ads, so both GA and AdSense under-count.
- **Homepage search:** typing "pdf" in the hero box ("What's on your mind?") and waiting 5s does nothing: no suggestions, no arrow, no hint. The header search on tool pages says "(press Enter)", but the hero doesn't. The owner removed search-on-first-letter because it was annoying. Now users who don't press Enter think it's broken. A 15s delay is too long (people give up after 2–3s).
- **No site-search data in GA:** there is no `search`/`view_search_results` event among the 12 events recorded, so we can't learn from what people type. The owner monitors searches to improve tool visibility.
- **Hidden text addressed to AI agents** was found in the page content on www.freedailypro.com. The bot did not follow it.

## Outcomes
1. **Ads never block tools (mobile first).**
   - Layout CSS/containers reserve real side margins for any rail, or exclude rails wherever the viewport can't fit content + rails. Tool working areas (dropzones, inputs, buttons, results) carry an exclusion so no ad renders over or inside them.
   - Manual placement:
     - one **reserved-height** unit right after the tool result/output area;
     - one unit lower on the page (how-to/FAQ area);
     - **no ad above or overlapping inputs**;
     - **no ads on checkout, login, account/profile, API key** pages.
   - Mobile: no horizontal overflow (ad containers `max-width:100%`, clipped or responsive), and no collapsing slot. Reserve a fixed min-height only where we are sure to fill it; otherwise don't reserve it above the tool at all. Floating back/home/feedback buttons don't stack with or hide under ad anchors/panels; offset them or keep a safe area.
2. **Mobile ad gap explained and fixed.** Investigate why mobile gets ~6% of the desktop ad page views: consent gating, slots hidden/`display:none` on mobile, lazy-load thresholds that never trigger, container width 0, script blocked. Report the root cause with numbers, fix it, and target mobile ad PV per GA mobile PV within the same order of magnitude as desktop.
3. **Consent banner.**
   - Make it compact: no covering the first screen's working area, at most a slim bar.
   - Implement **Google Consent Mode v2** properly (default states + update on choice; choose basic vs advanced and explain why), so GA conversion modeling works and non-personalized/limited ads can still serve where lawful.
   - Region-aware: opt-in for EU/EEA/UK/CH (use a Google-certified CMP if AdSense requires it there), and opt-out/notice is acceptable elsewhere, e.g. the US, which also has state privacy laws.
   - **Claude: verify the legal approach** and tell us if you disagree. Stay privacy-honest, in line with our privacy claims.
4. **Homepage hero search affordance.**
   - A visible search/arrow button inside the field, plus a "Press Enter" hint.
   - A suggestion dropdown after **≥3 characters and ~500ms pause** (debounced; keyboard navigable; no jumpiness on the first letter).
   - Full search on Enter or the arrow, both of which work on mobile (an `enterkeyhint="search"` keyboard).
   - Fire a GA4 **`search` event with `search_term`** on submit (register the custom dimension). Also log **zero-result searches** (e.g. a `search_no_results` event + the existing internal search log) so we can find missing tools. Current candidates from GSC: tip calculator, citation generator, percentage calculator, cost of living, barcode scanner.
5. **Hidden AI-agent-addressed text.** Find the hidden text on www.freedailypro.com addressed to AI agents. Confirm whether it is intended (e.g. an llms/agents note) and that it poses no injection risk to users or their AI assistants. If it isn't ours or isn't needed, remove it. If kept, make it visible/declared (e.g. /llms.txt) rather than hidden in page markup. Report what it says and where it lives.
6. **Owner-side AdSense console note** (write it up; the owner applies it, bots don't change the console):
   - Turn **Side rail ads OFF** until the layout reserves margins (re-enable after the fix ships and is verified).
   - Consider turning **Ad intents OFF** (in-text links, chips, anchor intent popups), since they inject into hero text and float over tools.
   - Keep **Vignette OFF**. Anchor ads are already OFF.
   - Add page exclusions for checkout/login/account/API key.
   - Revisit after the placement fix, with 2 weeks of data.

## Acceptance tests (desktop 1920x1080 + 1280x800, and iPhone-size 393x852 + 375x667)
- audio-comparer, merge-pdf, compress-pdf, roman-numeral-converter, home: no ad element's bounding box intersects any dropzone/input/button/result box (script check via `getBoundingClientRect` + screenshot). Clicks on both audio dropzones work at all four sizes.
- Mobile: no horizontal scroll (`scrollWidth <= innerWidth`) on those pages. CLS < 0.1 on audio-comparer with an ad filled and unfilled. No ad button is clipped. Floating buttons are never covered.
- No ads (auto or manual) on /checkout, /login, /profile, account and API-key pages.
- Consent: the banner is compact on both sizes. Consent Mode v2 default/update calls are visible in Tag Assistant. In a US session without interaction, GA collects and ads request per the chosen policy. In an EU session, nothing personalized fires before opt-in.
- Mobile ad requests appear on mobile tool pages (Network tab shows the ad request + filled or unfilled reason).
- Hero search: typing "pdf" shows suggestions after ~0.5s. "pd" shows none. Arrow and Enter both run the search on desktop and mobile. GA4 DebugView shows `search` with `search_term=pdf`. A nonsense term logs a zero-result event.
- Report: before/after screenshots at each size, CLS/LCP before/after, the mobile ad-gap root cause, the consent approach chosen + legal reasoning, and the hidden-text finding.

## Constraints
- Tool UX and free-first first. Never place ads next to buttons in a way that invites accidental clicks (AdSense policy).
- Privacy honesty: consent defaults must match our privacy page and the law by region.
- AdSense console changes are owner-only (item 6 is a note, not an action).
- Don't add ad networks. No ads on paid flows.

## Not in scope / do not decide
New ad networks; ads on checkout; trial-limit changes.

## Owner decisions needed
Apply the item-6 console settings; confirm the consent approach once Claude proposes it.

Source: owner
