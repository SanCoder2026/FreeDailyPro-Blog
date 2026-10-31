# Pricing tiers: owner clarification (31 Oct 2026, 15:26 ET)

Applies to all copy, tests, QA and blog briefs.

1. Workflow Products (Book Writing Toolbox, Event Suite, Seller Studio, Legal Production Desk) are the full bundles. Each has its own pricing (Event Suite $29.99/month). The $1 Day Pass and $4.99 monthly plan do NOT cover them.
2. Their sub-tools are also sold as standalone tools. A customer who wants only one feature pays that tool's own category pricing:
   - Professional Tools: 10 trial uses a day, then $1 Day Pass or $4.99/month.
   - Premium Applications: 2 trial uses a day, then $3 Day Pass or $9.99/month.
3. The 13 Event Suite products (guest-manager, booth-manager, etc.) are Premium Applications, so $3 / $9.99 standalone. Seller Studio and Legal Production Desk are monthly-only with a 7-day trial; their standalone desk tools are Premium Applications.
4. Do not write that the Event Suite tools have "no day pass" or "never get a day pass". Say: the full Event Suite is $29.99/month; individual tools use the Premium Applications pass prices.
5. Source of truth: shared/tiers.ts (PREMIUM_GROUPS, WORKFLOW_PRODUCT_IDS).

Please test that standalone Event Suite tools show the Premium paywall ($3/$9.99) after 2 uses and that the bundle pages show $29.99.
