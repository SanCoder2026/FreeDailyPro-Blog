# B-0041 / B-0053: owner actions (AdSense, GA4)

Only the owner can do these. Nothing here was changed from the repo.

## AdSense
Owner decision 29 Oct: do not change any AdSense console setting. Ads are made to behave through site code only (no ads on payment/account/API-key pages, one unit below the tool result, collapse when unfilled, never over a tool). Auto-ad formats Google places itself (side rails, vignette, anchor) are not controlled by site code; if one of them ever covers a tool, report the page and I will fix it in the layout.

## GA4
1. Admin > Data display > Custom definitions > Create custom dimension: scope Event, name "Search term", event parameter search_term.
2. DebugView check: submit "pdf" on the homepage, expect `search` with search_term=pdf; a nonsense term also sends `search_no_results`.

## Note
GSC "missing tool" candidates (tip calculator, citation generator, percentage calculator) already exist as tools (tip-calculator, citation-generator, percentage-calculator); they are SEO targets, not gaps.
