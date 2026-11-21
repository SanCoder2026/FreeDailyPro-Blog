Sent: 2026-11-21 09:47 ET

# Live functional findings (2026-11-21 EST, guest)

- **Battery** (func.json, func-firefox.json, func-webkit.json): 45 cases in each engine. All results match the FAQ and code; see the test-cases table.
- **Uniformity:** 10,000 draws of 1–6.
  - Chromium counts [1765, 1665, 1662, 1616, 1636, 1656], chi² 7.99.
  - Firefox 4.27, WebKit 5.77. Critical value at 5%, df 5 = 11.07.
- **Seed:** "class-7B" gives the same 10 numbers twice. "class-7C" differs. Cleared seed: two draws differ, and the method line returns to crypto.
- **Limits:** 10,000 numbers, dice and flips. List up to 10,000 lines. Pool up to 100,000. Up to 1,000,000 sides. 10,001 gives clear errors. The display shows the first 500.
- **Big lists** (biglist.json): 2,000 / 5,000 / 10,000 lines settle in 18–69 ms and draw in 56–88 ms. 10,001 gives "The list can have up to 10,000 lines."
- **Stale result:** when inputs go invalid, Generate is disabled and the error shows, but the previous result card (and its notes) stays.
- **Trial uses** (gate.json):
  - 0/10 context: Generate → 0/10, Copy → 0/10 ("Copied to clipboard"), Download → 0/10 (file saved), Copy → 0/10.
  - No usage POST; the only POSTs were funnel.hit and insight.hit analytics.
  - The 10 retry contexts were all at 10/10. func runs at 10/10 copied and downloaded with no dialog.
- **UX** (ux.json): 17 Tabs to Generate. Enter in Max doesn't generate. No aria-live on results. Switches are labelled. Phones show no overflow apart from iPhone SE (329/320, header).
- **Share** (share.json): share icon → "Link copied to clipboard". Share this tool → "Link copied! Share it with anyone." Create Shortcut → install-not-available hint. Star → no visible feedback.
- **Network:** analytics only. The numbers never leave the page.
