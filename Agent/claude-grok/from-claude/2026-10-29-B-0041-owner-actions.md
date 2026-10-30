# B-0041 / B-0053: owner actions (AdSense, GA4)

Only the owner can do these. Nothing here was changed from the repo.

## AdSense console (item 6)
1. Auto ads > Ad formats: turn Side rails OFF. Auto-placed side rails are positioned by Google; site code cannot move them. Re-enable only after checking a tool page at 1280 wide.
2. Consider Ad intents OFF (in-text links, chips, anchor intent popups): they inject into hero copy and float over tools. Revisit after 2 weeks of data.
3. Keep Vignette OFF and Anchor OFF.
4. Auto ads > Page exclusions: /checkout*, /login*, /pricing*, /profile*, /account*, /organization*, /admin*, /developers*, /apps/* (site code also stops loading/hides ads there; this is belt and braces).
5. Privacy & messaging: confirm a Google-certified (TCF) consent message is published for EEA/UK/CH only. Our own banner is not TCF-certified.
6. Do not change blocked categories.

## GA4
1. Admin > Data display > Custom definitions > Create custom dimension: scope Event, name "Search term", event parameter search_term.
2. DebugView check: submit "pdf" on the homepage, expect `search` with search_term=pdf; a nonsense term also sends `search_no_results`.

## Note
GSC "missing tool" candidates (tip calculator, citation generator, percentage calculator) already exist as tools (tip-calculator, citation-generator, percentage-calculator); they are SEO targets, not gaps.
