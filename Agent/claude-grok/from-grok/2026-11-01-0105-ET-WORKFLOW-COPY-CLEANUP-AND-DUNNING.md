Sent: 2026-11-01 01:05 ET (Grok Orchestrator)

# Workflow pricing copy cleanup + failed-payment recovery

## Intent
One consistent price message for every workflow toolbox, and no lost renewals.

## Why
Conversion audited 36 live pages. The old packs and the $3.99 pass are gone, but "Single book tools are sold separately under Premium Applications pricing" still conflicts with the owner's rule that Book Toolbox is $29.99/month only, and the trial wording differs from page to page. A $4.99 Monthly Pro renewal failed tonight (insufficient funds) and the invoice is still open.

## Outcome
1. Remove "Single book tools are sold separately under Premium Applications pricing." from /tool/book-writing-toolbox, /pricing, /workflow-products, /blog/book-writing-toolbox, /blog/ebook-only-publishing-with-book-writing-toolbox, /blog/book-writing-toolbox-overview-blank-page-to-submission and /blog/book-writing-toolbox-vs-vellum-atticus-reedsy.
2. Standard body copy on all workflow pages and blogs: "$29.99/month after a 7-day trial. Cancel anytime." Button text: "Start 7-day trial · $29.99/mo". Make sure the button text is in the server-rendered HTML on the 4 /tool/ pages, not only rendered in the browser.
3. Don't change the "Event Suite Premium $49.99" copy or the team-seat prices yet; that's waiting on an owner decision.
4. Failed payments: make sure customers get an email with an update-card link when a renewal fails (Stripe failed-payment emails and Smart Retries, or our own email). Report what's set up today.

Source: owner
