Sent: 2026-11-20 23:25 ET

# Desk findings: mortgage-calculator (2026-11-20 23:02–23:20 EST)

- **SEO:**
  - Title "Mortgage Calculator Online - Payment, Payoff Date | FreeDailyPro"; meta description 122 chars.
  - Canonical OK; 11 hreflang; H1 "Mortgage Calculator".
  - JSON-LD: SoftwareApplication (Offer price **4.99 USD** on a Professional Tool), VideoObject "How to Calculate Mortgage Payments Online No Signup", FAQPage (5 Q), BreadcrumbList.
  - og:image is the default image.
  - The video thumbnail `img` has no alt.
- **Locales:** es, pt, fr, de, ja, hi, zh, ko and id are each 200 with html lang set, but the title, H1 and the whole tool are English. They are English duplicates labelled as other languages through hreflang. /ar/ → 404. US-only maths (USD, FHA/VA/USDA) also limits value for those locales. P2.
- **FAQ:**
  - 5 questions, 4 of them about the first payment date.
  - Nothing on PMI vs MIP, FHA/VA/USDA, DTI, extra payments or biweekly, which are the tool's strengths. P2.
- **Copy contradictions:**
  - Limitations says "Insurance, tax and HOA are flat monthly amounts, so they do not rise over the years". The tool has "Costs that rise over time" inputs and a cost-growth table (M36). P2.
  - Privacy copy vs network behaviour (P0, see live findings).
  - "Files never stored" badge on a calculator with no files.
- **Guides:** "Turn a $90,000 Offer Into a Biweekly Take-Home Number" is a paycheck post. It is fine as a next step, but there is no guide on FHA vs conventional or on extra payments.
- **Blog** /blog/mortgage-calculator (Oct 24, 2026), "What a 10% Down Payment Really Costs Each Month":
  - Every figure reproduced live (B01–B04): $3,284.88 / $2,797.94 / $516,555 vs $459,160 / 109 payments / $22,073 PMI / $3,082.38 / 15-y $4,252.98, $230,037, 37 payments. The 45000-in-percent error is also confirmed. **PASS.**
  - It embeds the outdated video.
- **Category:** Finance, Tax & Retirement with Loan / EMI, Paycheck and Compound Interest. Correct. C28 Loans (loan, mortgage, student-loan): distinct intent, keep.
- **Competitors** (desk knowledge, not re-verified live this run): Bankrate, NerdWallet, Zillow and calculator.net offer:
  - affordability ("how much house can I afford")
  - ARM and points
  - refinance
  - ZIP-based tax/insurance defaults
  - live rate tables
  This tool already beats most on FHA/VA/USDA fees, dated schedule, extra payments, biweekly, DTI and worked steps. Gaps worth considering for the paid tier: affordability mode, points/APR, ARM, refinance break-even, rent-vs-buy.
- **AI need/demand:** high-volume evergreen query. AI is not needed for the maths; an "explain my result" summary could be a Premium hook.
