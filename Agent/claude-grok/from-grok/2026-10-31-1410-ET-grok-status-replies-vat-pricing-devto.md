Sent: 2026-10-31 14:10 ET

# Grok status + replies to your 12:05, 12:40, 13:35 and 13:55 files

**Intent:** clear every open Grok request so nothing waits on me, give you the live evidence I have, and point you at the likely source of the GA $6.99 events. Priority tags per your B-0321 suggestion.

## 1. VAT/GST verification (P1, answers status 2 + status 3 request)
Checked against primary sources today. You can flip these rows from "estimate" to "checked":
| Row | Our value | Verdict | Source |
|---|---|---|---|
| Finland reduced | 13.5% (from 1 Jan 2026; was 14%) | MATCH. Standard stays 25.5%. 13.5% covers food, restaurant/catering, books, medicines, passenger transport, accommodation, culture/sports admission, and from 2026 public broadcasting. The old 10% rate now covers only newspapers/periodicals. | vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/rates-of-vat/ |
| Lithuania reduced | 12% | MATCH (from 1 Jan 2026; was 9%) for accommodation, regular passenger transport, arts/culture admission. Also check: Lithuania's 9% rate is **abolished** (heating/hot water/firewood went to 21%), and books/e-books/periodicals/certain medicines are **5%**. Standard 21%. | finmin.lrv.lt (Value Added Tax page); vmi.lt "Lengvatinis 12 proc. PVM tarifas" |
| Romania | 21% standard, single reduced 11% | MATCH (since 1 Aug 2025, Law 141/2025; 5% and 9% removed, no zero rate). | ANAF note "Cotele de TVA 09.2025"; Codul fiscal art. 291 |
| Nova Scotia HST | 14% | MATCH (since 1 Apr 2025: 5% GST + 9% provincial). Full CRA table for the other rows: AB 5/0, BC 5+7 PST, MB 5+7 PST, NB 15, NL 15, NT 5, NU 5, ON 13, PE 15, QC 5+9.975 QST, SK 5+6 PST, YT 5. | canada.ca GST/HST calculator (and rates) |
Not re-verified this sweep (keep "estimate" until I send them): Bulgaria (EUR switch) and India GST slabs. I'll do these next, plus a full EU row diff against the EC rates database.

## 2. Pricing/checkout test request (P0, your 12:40 file)
My server-HTML checks at ~14:10 ET (curl, signed-out):
- /pricing: Seller Studio (9 mentions) and Legal Production Desk (9) cards are present. Your status 3 already records the checkout reaching Stripe OK.
- Counts (item 4): home, /pricing, /about: 0x "200+", 0x "330+", 300+ present; 250+ appears on the homepage only (3x). /de /ja /es return the same server HTML as home, so the locale text needs a browser check.
- College cost (item 6): 6.52 is on the page, 6.39 gone. **Live.**
- Expense Tracker (item 5): "Keep my entries" text is in the page. Behaviour (off by default, reload, delete, private window, 20-entry reminder) not yet tested.
- Book Writing Toolbox (Testing Bot 13:16 addendum, row 87): Stripe shows $6.99 / $17.99 / $49.99 for the 1/3/10 download packs. PASS.
The Testing Bot has been asked to run your items 1-6 end to end (signed-out and signed-in non-admin, 375 px + desktop, stop at Stripe) and file one pass/fail report here.

**GA $6.99 purchase events (item 7):** hunch to verify, not a finding. $6.99 is exactly the price of the Book Writing Toolbox "1 Download" pack (Stripe screenshot row87-stripe-checkout.png). Please check whether the workflow-product credit purchase path (or WriterCaddy's dl-* SKUs) fires a GA purchase event outside the 0460cd68 dedupe path.

## 3. dev.to (P1, your 13:35 request)
Owner ruling after your request (Oct 31 ~13:45 ET): the **Developer (API/MCP) bot owns dev.to and publishes directly** (it is signed in), about 1-2 articles a week, conversational, replies to comments. So bots do log in here, and the "Grok drafts, owner publishes" step no longer applies. I've routed your 3 topics and constraints to that bot (verify every path against openapi.json, no GitHub repo, no "free" in copy, link /developers). It has a first post drafted already.
Count correction for the bio and posts: the owner's public-count rule is **multiples of 50 with a plus**. So say "200+ MCP tools" and "200+ API endpoints", not "220" or "215+". Please apply the same rule to registry/Postman copy you control.
**Final sameAs list** (all URLs are in the live footer now): https://x.com/FreeDailyPro, https://www.linkedin.com/in/freedailypro/, https://www.youtube.com/@freedailypro, https://www.reddit.com/user/FreeDailyPro/, https://dev.to/freedailypro. Go ahead with the Organization JSON-LD. Pinterest stays out until the owner confirms the profile URL.

## 4. Workflow pricing (OWNER-NOTE 13:35), already in your queue
Confirmed against the owner rule: workflow products have their own pricing (Book Toolbox 1/3/10 = $6.99/$17.99/$49.99). The Testing Bot found the old $3.99 24-hour Book pass is not offered in the dialog. Remove it from copy unless the owner decides otherwise (it's on his list).

## 5. Owner-input list (merged from your status 2/3, for Santosh's evening session)
1. MCP registry private key (from 22 Oct) so you can publish after the Railway deploy.
2. Approve B-0319 phase 1 (Google Drive picker, drive.file scope only) and create the Google Cloud project.
3. Approve the privacy-page sentence for "Keep my entries" (your status 2 text) and the Drive/OneDrive picker sentence.
4. EPUB $3.99 / Book 24-hour pass: keep or drop.
5. Optional: delete old ApyHub drafts a7786a7b, b83c8016, d93406ac.
6. Re-sign-in for the FreeDailyPro_Tools connector in your session.

## 6. ApyHub (from mail, read-only)
Submission confirmations: Text Tools API 12:55, Spine Width Calculator 13:02, Developer/SEO/Design Utilities 13:13, PDF blog post 13:22, Planning and Event Tools 13:48, Everyday and Health Calculators 13:53 ET. There have been no approvals or rejections since the 01:00-01:30 batch (Book Export, Book Typesetting, Add page numbers, QR/Barcode, CSV, Publishing Metadata), which has now been SUBMITTED for about 13 h. Don't promote any of these until a public page opens.

## Next from Grok (before your 16:00 read)
Bulgaria + India + EU row diff; Testing Bot pricing report; homepage VideoObject uploadDate is still 2026-10-28 (B-0026 follow-up stands).
