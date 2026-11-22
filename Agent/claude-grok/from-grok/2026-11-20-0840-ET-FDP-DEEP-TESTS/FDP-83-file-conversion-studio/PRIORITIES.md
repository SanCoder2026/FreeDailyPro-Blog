Sent: 2026-11-21 19:08 ET

# FDP-83 priorities

**P0:** none found. **P1:** none found as a guest (server-side gate via `workflowProduct.status`; the Studio never renders for a guest).

**P2**
1. No way to see the product before a $29.99/month trial: no video (none on the channel's 511 videos), no screenshot, no sample `results.csv` / ZIP, although "What you get before you pay" lists them.
2. Locale pages untranslated: all 10 hreflang pages show English H1, intro, price card, FAQ and title.
3. Meta description truncated: "…a quality panel, your own file."

**P3**
1. `?checkout=success` shows a guest "Thank you. We are confirming your payment with Stripe…", polls status 20× (~60 s), then the message vanishes without explanation.
2. Listed in PDF Tools with PDF-only "More from" links for a mixed-format product.
3. Full Studio bundle (54 KB) loaded for guests behind the paywall.
4. iPhone SE 9 px; ja desktop 3 px; axe desktop label-content-name-mismatch + region.
